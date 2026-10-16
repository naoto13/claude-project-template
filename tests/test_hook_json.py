import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import uuid

ROOT = Path(__file__).resolve().parents[1]
DETAIL = 'quote " and slash \\ and literal \\n\nsecond line\twith tab'

class HookJsonTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix='hook-json-')
        self.work = Path(self.directory.name)
        self.bin = self.work / 'bin'
        self.bin.mkdir()
        self.session = 'json-fixture-' + uuid.uuid4().hex
        self.counter = Path('/tmp') / ('claude-stop-ci-' + self.session + '.count')
        self.env = dict(os.environ, PATH=str(self.bin) + os.pathsep + os.environ['PATH'],
                        CLAUDE_PROJECT_DIR=str(self.work), CLAUDE_SESSION_ID=self.session,
                        FIXTURE_DETAIL=DETAIL, FIXTURE_FAIL='test',
                        FIXTURE_CALL_LOG=str(self.work / 'calls'))
        self.stub('pnpm', '#!/bin/sh\nprintf \'pnpm %s\\n\' \"$1\" >> \"$FIXTURE_CALL_LOG\"\nprintf "%s" "$FIXTURE_DETAIL"\n[ "$1" != "$FIXTURE_FAIL" ]\n')
        self.stub('curl', '#!/bin/sh\nprintf \'curl\\n\' >> \"$FIXTURE_CALL_LOG\"\nexit 22\n')

    def tearDown(self):
        self.counter.unlink(missing_ok=True)
        self.directory.cleanup()

    def stub(self, name, source):
        target = self.bin / name
        target.write_text(source)
        target.chmod(0o755)

    def package(self, scripts):
        (self.work / 'package.json').write_text(json.dumps({'scripts': scripts}))

    def run_hook(self, name, value=''):
        # Mock only profile sourcing; execute the unchanged hook text via builtin source.
        # This prevents a host nvm profile from replacing the fixture PATH.
        runner = 'function .() { return 0; }; builtin source \"$1\"'
        result = subprocess.run(['bash', '-c', runner, 'hook-json-fixture',
                                 str(ROOT / '.claude/hooks' / name)], input=value,
                                text=True, capture_output=True, env=self.env, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_stop_failure_preserves_output(self):
        self.package({'test': 'inert'})
        response = json.loads(self.run_hook('stop-ci.sh'))
        self.assertEqual(response['decision'], 'block')
        self.assertIn(DETAIL, response['reason'])
        self.assertIn('試行 1/3', response['reason'])
        self.assertEqual(self.counter.read_text().strip(), '1')
        self.assertEqual((self.work / 'calls').read_text(), 'pnpm test\n')

    def test_stop_third_failure_preserves_limit(self):
        self.package({'test': 'inert'})
        self.counter.write_text('2')
        response = json.loads(self.run_hook('stop-ci.sh'))
        self.assertEqual(response['decision'], 'block')
        self.assertIn('3回連続', response['reason'])
        self.assertIn(DETAIL, response['reason'])
        self.assertFalse(self.counter.exists())

    def test_stop_success_clears_counter(self):
        self.package({'check': 'inert'})
        self.counter.write_text('1')
        self.assertEqual(self.run_hook('stop-ci.sh'), '')
        self.assertFalse(self.counter.exists())

    def test_stop_without_package_does_nothing(self):
        self.assertEqual(self.run_hook('stop-ci.sh'), '')

    def test_guard_warning_is_valid_json(self):
        response = json.loads(self.run_hook('guard-npm-install.sh', json.dumps({
            'tool_name': 'Bash', 'tool_input': {'command': 'npm install fixture-package'}
        })))['hookSpecificOutput']
        self.assertEqual(response['hookEventName'], 'PreToolUse')
        self.assertEqual(response['permissionDecision'], 'ask')
        self.assertIn('fixture-package', response['permissionDecisionReason'])
        self.assertEqual((self.work / 'calls').read_text(), 'curl\n')
        self.assertIn('\n- ', response['permissionDecisionReason'])

    def test_guard_quotes_and_backslashes_remain_literal(self):
        name = 'fixture"back\\slash'
        response = json.loads(self.run_hook('guard-npm-install.sh', json.dumps({
            'tool_name': 'Bash', 'tool_input': {'command': 'npm install ' + name}
        })))['hookSpecificOutput']
        self.assertIn(name, response['permissionDecisionReason'])
        self.assertEqual(response['permissionDecision'], 'ask')

    def test_guard_unrelated_command_does_nothing(self):
        self.assertEqual(self.run_hook('guard-npm-install.sh', json.dumps({
            'tool_name': 'Bash', 'tool_input': {'command': 'git status'}
        })), '')

    def test_guard_safe_package_does_not_ask(self):
        self.stub('curl', '#!/bin/sh\nprintf \'%s\' \'{"downloads":2000,"time":{}}\'\n')
        self.assertEqual(self.run_hook('guard-npm-install.sh', json.dumps({
            'tool_name': 'Bash', 'tool_input': {'command': 'npm install react'}
        })), '')

if __name__ == '__main__':
    unittest.main()
