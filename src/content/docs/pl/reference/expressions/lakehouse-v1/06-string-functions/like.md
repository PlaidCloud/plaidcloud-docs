---
title: LIKE (Lakehouse v1)
description: LIKE — dopasowywanie wzorca za pomocą wzorca SQL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/like.md
---

Dopasowywanie wzorca za pomocą wzorca SQL. Zwraca 1 (TRUE) lub 0 (FALSE). Jeśli expr lub pat ma wartość NULL, wynikiem jest NULL.

## Składnia Analyze

```python
<column>.like('plaid%')
```

## Przykłady Analyze

```python
my_clothes.like('plaid%)
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants     │
│ plaid hat       │
│ plaid shirt     │
└─────────────────┘
```

## Składnia SQL

```sql
<expr> LIKE <pattern>
```

## Przykłady SQL

```sql
SELECT name, category FROM system.functions WHERE name like 'tou%' ORDER BY name;
┌──────────┬────────────┐
│ name     │ category   │
├──────────┼────────────┤
│ touint16 │ conversion │
│ touint32 │ conversion │
│ touint64 │ conversion │
│ touint8  │ conversion │
└──────────┴────────────┘
```
