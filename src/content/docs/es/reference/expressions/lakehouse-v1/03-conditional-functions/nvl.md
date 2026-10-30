---
title: NVL (Lakehouse v1)
description: NVL — si <expr1> es NULL, devuelve <expr2>; de lo contrario, devuelve <expr1>.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/nvl.md
---

Si `<expr1>` es NULL, devuelve `<expr2>`; de lo contrario, devuelve `<expr1>`.

## Sintaxis de Analyze

```python
func.nvl(<expr1>, <expr2>)
```

## Ejemplos de Analyze

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

## Sintaxis de SQL

```sql
NVL(<expr1>, <expr2>)
```

## Alias

- [IFNULL](../ifnull)

## Ejemplos de SQL

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
