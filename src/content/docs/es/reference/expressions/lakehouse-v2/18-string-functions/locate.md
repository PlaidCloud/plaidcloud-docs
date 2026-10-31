---
title: LOCATE (Lakehouse v2)
description: LOCATE — Devuelve la posición de la primera aparición de una subcadena en una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/locate.md
---

Devuelve la posición de la primera aparición de una subcadena en una cadena.

## Sintaxis de Analyze

```python
func.locate(<substr>, <str>[, <pos>])
```

## Ejemplos de Analyze

```python
func.locate('or', 'hello world')

┌───┐
│ 8  │
└───┘
```

## Sintaxis de SQL

```sql
LOCATE(<substr>, <str>[, <pos>])
```

## Ejemplos de SQL

```sql
SELECT LOCATE('or', 'hello world');

┌───┐
│ 8  │
└───┘
```
