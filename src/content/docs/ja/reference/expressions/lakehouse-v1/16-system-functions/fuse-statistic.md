---
title: FUSE_STATISTIC（Lakehouse v1）
description: FUSE_STATISTIC — テーブル内の各列の異なる値の推定数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-statistic.md
---

テーブル内の各列の異なる値の推定数を返します。


## SQLの構文

```sql
FUSE_STATISTIC('<database_name>', '<table_name>')
```

## SQLの例

この関数は、`ANALYZE TABLE <table_name>` と組み合わせて、テーブルの統計情報を生成し確認する用途で使用するのが一般的です。詳しい説明と例については、OPTIMIZE TABLEを参照してください。
