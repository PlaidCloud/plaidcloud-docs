---
title: IFNULL (Lakehouse v1)
description: IFNULL — jeśli <expr1> ma wartość NULL, zwraca <expr2>, w przeciwnym razie zwraca <expr1>.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/ifnull.md
---

Jeśli `<expr1>` ma wartość NULL, zwraca `<expr2>`, w przeciwnym razie zwraca `<expr1>`.

## Składnia Analyze

```python
func.ifnull(<expr1>, <expr2>)
```

## Przykłady Analyze

```python
func.ifnull(null, 'b'), func.ifnull('a', 'b')

┌────────────────────────────────────────────────┐
│ func.ifnull(null, 'b') │ func.ifnull('a', 'b') │
├────────────────────────┼───────────────────────┤
│ b                      │ a                     │
└────────────────────────────────────────────────┘

func.ifnull(null, 2), func.ifnull(1, 2)

┌──────────────────────────────────────────┐
│ func.ifnull(null, 2) │ func.ifnull(1, 2) │
├──────────────────────┼───────────────────┤
│                    2 │                 1 │
└──────────────────────────────────────────┘
```

## Składnia SQL

```sql
IFNULL(<expr1>, <expr2>)
```

## Aliasy

- [NVL](../nvl)

## Przykłady SQL

```sql
SELECT IFNULL(NULL, 'b'), IFNULL('a', 'b');

┌──────────────────────────────────────┐
│ ifnull(null, 'b') │ ifnull('a', 'b') │
├───────────────────┼──────────────────┤
│ b                 │ a                │
└──────────────────────────────────────┘

SELECT IFNULL(NULL, 2), IFNULL(1, 2);

┌────────────────────────────────┐
│ ifnull(null, 2) │ ifnull(1, 2) │
├─────────────────┼──────────────┤
│               2 │            1 │
└────────────────────────────────┘
```
