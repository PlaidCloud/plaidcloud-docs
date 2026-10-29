---
title: CONCAT (Lakehouse v2)
description: CONCAT — Concatena dos o más cadenas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat.md
---

Concatena dos o más cadenas.

## Sintaxis de Analyze

```python
func.concat(<str1>, <str2>[, ...])
```

## Ejemplos de Analyze

```python
func.concat('Star', 'Rocks')

┌─────────────┐
│ 'StarRocks'  │
└─────────────┘
```

## Sintaxis de SQL

```sql
CONCAT(<str1>, <str2>[, ...])
```

## Ejemplos de SQL

```sql
SELECT CONCAT('Star', 'Rocks');

┌───────────┐
│ StarRocks  │
└───────────┘
```
