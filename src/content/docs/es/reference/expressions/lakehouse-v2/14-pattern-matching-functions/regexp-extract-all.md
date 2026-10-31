---
title: REGEXP_EXTRACT_ALL (Lakehouse v2)
description: REGEXP_EXTRACT_ALL — extrae todas las subcadenas que coinciden con un patrón de expresión regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract-all.md
---

Extrae todas las subcadenas que coinciden con un patrón de expresión regular.

## Sintaxis de Analyze

```python
func.regexp_extract_all(<str>, <pattern>)
```

## Ejemplos de Analyze

```python
func.regexp_extract_all('a1b2c3', '\\d+')

┌───────────────┐
│ ['1','2','3']  │
└───────────────┘
```

## Sintaxis de SQL

```sql
REGEXP_EXTRACT_ALL(<str>, <pattern>)
```

## Ejemplos de SQL

```sql
SELECT REGEXP_EXTRACT_ALL('a1b2c3', '\\d+');

┌───────────────┐
│ ["1","2","3"]  │
└───────────────┘
```
