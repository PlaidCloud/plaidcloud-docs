---
title: REGEXP_COUNT (Lakehouse v2)
description: "Use la función de coincidencia de patrones REGEXP_COUNT en PlaidCloud Lakehouse. Devuelve el número de veces que un patrón de expresión regular aparece en una cadena."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-count.md
---

Devuelve el número de veces que un patrón de expresión regular aparece en una cadena.

## Sintaxis de Analyze

```python
func.regexp_count(<str>, <pattern>)
```

## Ejemplos de Analyze

```python
func.regexp_count('banana', 'an')

┌───┐
│ 2  │
└───┘
```

## Sintaxis de SQL

```sql
REGEXP_COUNT(<str>, <pattern>)
```

## Ejemplos de SQL

```sql
SELECT REGEXP_COUNT('banana', 'an');

┌───┐
│ 2  │
└───┘
```
