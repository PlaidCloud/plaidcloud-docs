---
title: STRPOS (Lakehouse v2)
description: STRPOS — Devuelve la posición de la primera aparición de una subcadena. Alias de `LOCATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strpos.md
---

Devuelve la posición de la primera aparición de una subcadena. Alias de `LOCATE`.

## Sintaxis de Analyze

```python
func.strpos(<str>, <substr>)
```

## Ejemplos de Analyze

```python
func.strpos('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## Sintaxis de SQL

```sql
STRPOS(<str>, <substr>)
```

## Ejemplos de SQL

```sql
SELECT STRPOS('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
