---
title: EXISTS（Lakehouse v1）
description: EXISTS — EXISTS条件はサブクエリと組み合わせて使用し、サブクエリが1行以上を返す場合に「満たされた」とみなされます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/exists.md
---

EXISTS条件はサブクエリと組み合わせて使用し、サブクエリが1行以上を返す場合に「満たされた」とみなされます。

## SQLの構文

```sql
WHERE EXISTS ( <subquery> );
```

## SQLの例
```sql
SELECT number FROM numbers(5) AS A WHERE exists (SELECT * FROM numbers(3) WHERE number=1); 
┌────────┐
│ number │
├────────┤
│      0 │
│      1 │
│      2 │
│      3 │
│      4 │
└────────┘
```
