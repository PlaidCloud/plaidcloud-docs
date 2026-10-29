---
title: SPACE (Lakehouse v2)
description: SPACE — Devuelve una cadena formada por un número especificado de espacios.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/space.md
---

Devuelve una cadena formada por un número especificado de espacios.

## Sintaxis de Analyze

```python
func.space(<n>)
```

## Ejemplos de Analyze

```python
func.space(5)

┌─────────┐
│ '     '  │
└─────────┘
```

## Sintaxis de SQL

```sql
SPACE(<n>)
```

## Ejemplos de SQL

```sql
SELECT CONCAT('>', SPACE(5), '<');

┌─────────┐
│ >     <  │
└─────────┘
```
