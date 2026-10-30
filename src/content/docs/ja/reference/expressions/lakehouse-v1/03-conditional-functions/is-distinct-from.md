---
title: "IS [ NOT ] DISTINCT FROM（Lakehouse v1）"
description: IS [ NOT ] DISTINCT FROM — NULL 許容性を考慮して、2 つの式が等しいか（または等しくないか）を比較します。NULL は既知の値として扱われます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-distinct-from.md
---

NULL 許容性を考慮して、2 つの式が等しいか（または等しくないか）を比較します。等しいかどうかの比較では、NULL を既知の値として扱います。

## SQL 構文

```sql
<expr1> IS [ NOT ] DISTINCT FROM <expr2>
```

## SQL の例

```sql
SELECT NULL IS DISTINCT FROM NULL;

┌────────────────────────────┐
│ null is distinct from null │
├────────────────────────────┤
│ false                      │
└────────────────────────────┘
```
