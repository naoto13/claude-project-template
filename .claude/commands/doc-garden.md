# doc-garden

ドキュメントと実装の整合性を点検し、事実情報のズレを直す。

## チェック項目

1. `docs/architecture.md` に書かれたパスが実在するか
2. `CLAUDE.md` のコマンド記述と `package.json` scripts が一致しているか
3. `docs/domain/data-model.md` のエンティティ記述が実装と大きくズレていないか
4. `docs/spec/` の仕様が古くなっていないか
5. `docs/todo.md` の状態が実態とズレていないか

## 注意

- 説明文を全面的に書き換えない
- 事実ベースの差分だけ更新する
