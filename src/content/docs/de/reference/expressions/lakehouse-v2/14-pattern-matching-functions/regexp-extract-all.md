---
title: REGEXP_EXTRACT_ALL (Lakehouse v2)
description: REGEXP_EXTRACT_ALL – extrahiert alle Teilzeichenfolgen, die einem Muster eines regulären Ausdrucks entsprechen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract-all.md
---

Extrahiert alle Teilzeichenfolgen, die einem Muster eines regulären Ausdrucks entsprechen.

## Analyze-Syntax

```python
func.regexp_extract_all(<str>, <pattern>)
```

## Analyze-Beispiele

```python
func.regexp_extract_all('a1b2c3', '\\d+')

┌───────────────┐
│ ['1','2','3']  │
└───────────────┘
```

## SQL-Syntax

```sql
REGEXP_EXTRACT_ALL(<str>, <pattern>)
```

## SQL-Beispiele

```sql
SELECT REGEXP_EXTRACT_ALL('a1b2c3', '\\d+');

┌───────────────┐
│ ["1","2","3"]  │
└───────────────┘
```
