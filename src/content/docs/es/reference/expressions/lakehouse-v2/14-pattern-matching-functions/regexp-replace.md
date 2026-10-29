---
title: REGEXP_REPLACE (Lakehouse v2)
description: "Use la función de coincidencia de patrones REGEXP_REPLACE en PlaidCloud Lakehouse. Reemplaza las subcadenas que coinciden con un patrón de expresión regular por una cadena de reemplazo."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-replace.md
---

Reemplaza las subcadenas que coinciden con un patrón de expresión regular por una cadena de reemplazo.

## Sintaxis de Analyze

```python
func.regexp_replace(<str>, <pattern>, <replacement>)
```

## Ejemplos de Analyze

```python
func.regexp_replace('hello   world', '\\s+', ' ')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## Sintaxis de SQL

```sql
REGEXP_REPLACE(<str>, <pattern>, <replacement>)
```

## Ejemplos de SQL

```sql
SELECT REGEXP_REPLACE('hello   world', '\\s+', ' ');

┌─────────────┐
│ hello world  │
└─────────────┘
```
