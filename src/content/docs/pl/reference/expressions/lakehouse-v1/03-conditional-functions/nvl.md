---
title: NVL (Lakehouse v1)
description: NVL — jeśli <expr1> ma wartość NULL, zwraca <expr2>, w przeciwnym razie zwraca <expr1>.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/nvl.md
---

Jeśli `<expr1>` ma wartość NULL, zwraca `<expr2>`, w przeciwnym razie zwraca `<expr1>`.

## Składnia Analyze

```python
func.nvl(<expr1>, <expr2>)
```

## Przykłady Analyze

```python
func.nvl(null, 'b'), func.nvl('a', 'b')

┌──────────────────────────────────────────┐
│ func.nvl(null, 'b') │ func.nvl('a', 'b') │
├─────────────────────┼────────────────────┤
│ b                   │ a                  │
└──────────────────────────────────────────┘

func.nvl(null, 2), func.nvl(1, 2)

┌────────────────────────────────────┐
│ func.nvl(null, 2) │ func.nvl(1, 2) │
├───────────────────┼────────────────┤
│                 2 │              1 │
└────────────────────────────────────┘
```

## Składnia SQL

```sql
NVL(<expr1>, <expr2>)
```

## Aliasy

- [IFNULL](../ifnull)

## Przykłady SQL

```sql
SELECT NVL(NULL, 'b'), NVL('a', 'b');

┌────────────────────────────────┐
│ nvl(null, 'b') │ nvl('a', 'b') │
├────────────────┼───────────────┤
│ b              │ a             │
└────────────────────────────────┘

SELECT NVL(NULL, 2), NVL(1, 2);

┌──────────────────────────┐
│ nvl(null, 2) │ nvl(1, 2) │
├──────────────┼───────────┤
│            2 │         1 │
└──────────────────────────┘
```
