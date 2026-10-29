---
title: REGEXP_COUNT (Lakehouse v2)
description: "Verwenden Sie die Mustervergleichsfunktion REGEXP_COUNT in PlaidCloud Lakehouse. Gibt zurück, wie oft ein Muster eines regulären Ausdrucks in einer Zeichenfolge vorkommt."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-count.md
---

Gibt zurück, wie oft ein Muster eines regulären Ausdrucks in einer Zeichenfolge vorkommt.

## Analyze-Syntax

```python
func.regexp_count(<str>, <pattern>)
```

## Analyze-Beispiele

```python
func.regexp_count('banana', 'an')

┌───┐
│ 2  │
└───┘
```

## SQL-Syntax

```sql
REGEXP_COUNT(<str>, <pattern>)
```

## SQL-Beispiele

```sql
SELECT REGEXP_COUNT('banana', 'an');

┌───┐
│ 2  │
└───┘
```
