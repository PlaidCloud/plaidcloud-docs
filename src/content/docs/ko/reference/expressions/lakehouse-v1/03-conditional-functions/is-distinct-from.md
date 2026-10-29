---
title: "IS [ NOT ] DISTINCT FROM (Lakehouse v1)"
description: IS [ NOT ] DISTINCT FROM — NULL 허용 여부를 고려하여 두 식이 같은지(또는 같지 않은지) 비교하며, NULL을 알려진 값으로 취급합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-distinct-from.md
---

NULL 허용 여부를 고려하여 두 식이 같은지(또는 같지 않은지) 비교합니다. 같음을 비교할 때 NULL을 알려진 값으로 취급합니다.

## SQL 구문

```sql
<expr1> IS [ NOT ] DISTINCT FROM <expr2>
```

## SQL 예시

```sql
SELECT NULL IS DISTINCT FROM NULL;

┌────────────────────────────┐
│ null is distinct from null │
├────────────────────────────┤
│ false                      │
└────────────────────────────┘
```
