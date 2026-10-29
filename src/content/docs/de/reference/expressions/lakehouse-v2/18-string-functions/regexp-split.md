---
title: REGEXP_SPLIT (Lakehouse v2)
description: REGEXP_SPLIT — teilt eine Zeichenfolge anhand eines regulären Ausdrucks und gibt ein Array von Teilzeichenfolgen zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/regexp-split.md
---

Teilt eine Zeichenfolge anhand eines regulären Ausdrucks und gibt ein Array von Teilzeichenfolgen zurück.

## Analyze-Syntax

```python
func.regexp_split('one1two2three', '[0-9]')
```

## Analyze-Beispiele

```python
func.regexp_split('one1two2three', '[0-9]')

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```

## SQL-Syntax

```sql
REGEXP_SPLIT(<str>, <pattern>)
```

## SQL-Beispiele

```sql
SELECT REGEXP_SPLIT('one1two2three', '[0-9]');

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```
