---
title: REGEXP_EXTRACT (Lakehouse v2)
description: REGEXP_EXTRACT – extrahiert die erste Teilzeichenfolge, die einem Muster eines regulären Ausdrucks entspricht.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract.md
---

Extrahiert die erste Teilzeichenfolge, die einem Muster eines regulären Ausdrucks entspricht.

## Analyze-Syntax

```python
func.regexp_extract(<str>, <pattern>[, <group>])
```

## Analyze-Beispiele

```python
func.regexp_extract('price: $42.50', '\\$(\\d+\\.\\d+)', 1)

┌─────────┐
│ '42.50'  │
└─────────┘
```

## SQL-Syntax

```sql
REGEXP_EXTRACT(<str>, <pattern>[, <group>])
```

## SQL-Beispiele

```sql
SELECT REGEXP_EXTRACT('price: $42.50', '\\$(\\d+\\.\\d+)', 1);

┌───────┐
│ 42.50  │
└───────┘
```
