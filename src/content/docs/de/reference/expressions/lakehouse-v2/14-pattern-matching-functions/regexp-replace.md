---
title: REGEXP_REPLACE (Lakehouse v2)
description: "Verwenden Sie die Mustervergleichsfunktion REGEXP_REPLACE in PlaidCloud Lakehouse. Ersetzt Teilzeichenfolgen, die einem Muster eines regulären Ausdrucks entsprechen, durch eine Ersetzungszeichenfolge."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-replace.md
---

Ersetzt Teilzeichenfolgen, die einem Muster eines regulären Ausdrucks entsprechen, durch eine Ersetzungszeichenfolge.

## Analyze-Syntax

```python
func.regexp_replace(<str>, <pattern>, <replacement>)
```

## Analyze-Beispiele

```python
func.regexp_replace('hello   world', '\\s+', ' ')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## SQL-Syntax

```sql
REGEXP_REPLACE(<str>, <pattern>, <replacement>)
```

## SQL-Beispiele

```sql
SELECT REGEXP_REPLACE('hello   world', '\\s+', ' ');

┌─────────────┐
│ hello world  │
└─────────────┘
```
