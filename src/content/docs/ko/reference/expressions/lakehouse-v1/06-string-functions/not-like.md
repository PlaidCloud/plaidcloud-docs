---
title: NOT LIKE (Lakehouse v1)
description: NOT LIKE — SQL 패턴을 사용하여 패턴 불일치를 검사합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-like.md
---

SQL 패턴을 사용하여 패턴 불일치를 검사합니다. 1(TRUE) 또는 0(FALSE)을 반환합니다. expr 또는 pat 중 하나라도 NULL이면 결과는 NULL입니다.

## Analyze 구문

```python
<column>.not_like(<pattern>)
```

## Analyze 예제

```python
my_clothes.not_like('%pants)
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants XL  │
│ plaid hat       │
│ plaid shirt     │
└─────────────────┘
```

## SQL 구문

```sql
<expr> NOT LIKE <pattern>
```

## SQL 예제

```sql
SELECT name, category FROM system.functions WHERE name like 'tou%' AND name not like '%64' ORDER BY name;
┌──────────┬────────────┐
│ name     │ category   │
├──────────┼────────────┤
│ touint16 │ conversion │
│ touint32 │ conversion │
│ touint8  │ conversion │
└──────────┴────────────┘
```
