---
title: NOT LIKE (Lakehouse v1)
description: NOT LIKE — brak dopasowania do wzorca SQL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-like.md
---

Sprawdza brak dopasowania do wzorca SQL. Zwraca 1 (TRUE) lub 0 (FALSE). Jeśli expr lub pat ma wartość NULL, wynikiem jest NULL.

## Składnia Analyze

```python
<column>.not_like(<pattern>)
```

## Przykłady Analyze

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

## Składnia SQL

```sql
<expr> NOT LIKE <pattern>
```

## Przykłady SQL

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
