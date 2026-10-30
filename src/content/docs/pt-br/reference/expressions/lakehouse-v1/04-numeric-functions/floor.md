---
title: FLOOR (Lakehouse v1)
description: FLOOR — arredonda o número para baixo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/floor.md
---

Arredonda o número para baixo.

## Sintaxe do Analyze

```python
func.floor( <x> )
```

## Exemplos do Analyze

```python
func.floor(1.23)

┌──────────────────┐
│ func.floor(1.23) │
├──────────────────┤
│                1 │
└──────────────────┘
```

## Sintaxe SQL

```sql
FLOOR( <x> )
```

## Exemplos de SQL

```sql
SELECT FLOOR(1.23);

┌─────────────┐
│ floor(1.23) │
├─────────────┤
│           1 │
└─────────────┘
```
