---
title: "IS [ NOT ] DISTINCT FROM（Lakehouse v1）"
description: IS [ NOT ] DISTINCT FROM——在考虑可空性的前提下比较两个表达式是否相等（或不相等），即把 NULL 视为已知值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-distinct-from.md
---

在考虑可空性的前提下比较两个表达式是否相等（或不相等），即在比较相等性时把 NULL 视为已知值。

## SQL 语法

```sql
<expr1> IS [ NOT ] DISTINCT FROM <expr2>
```

## SQL 示例

```sql
SELECT NULL IS DISTINCT FROM NULL;

┌────────────────────────────┐
│ null is distinct from null │
├────────────────────────────┤
│ false                      │
└────────────────────────────┘
```
