---
title: REGEXP_EXTRACT (Lakehouse v2)
description: REGEXP_EXTRACT — extrae la primera subcadena que coincide con un patrón de expresión regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract.md
---

Extrae la primera subcadena que coincide con un patrón de expresión regular.

## Sintaxis de Analyze

```python
func.regexp_extract(<str>, <pattern>[, <group>])
```

## Ejemplos de Analyze

```python
func.regexp_extract('price: $42.50', '\\$(\\d+\\.\\d+)', 1)

┌─────────┐
│ '42.50'  │
└─────────┘
```

## Sintaxis de SQL

```sql
REGEXP_EXTRACT(<str>, <pattern>[, <group>])
```

## Ejemplos de SQL

```sql
SELECT REGEXP_EXTRACT('price: $42.50', '\\$(\\d+\\.\\d+)', 1);

┌───────┐
│ 42.50  │
└───────┘
```
