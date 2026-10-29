---
title: SUBSTR (Lakehouse v2)
description: SUBSTR — gibt eine Teilzeichenfolge ab einer angegebenen Position mit optionaler Länge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substr.md
---

Gibt eine Teilzeichenfolge ab einer angegebenen Position mit optionaler Länge zurück.

## Analyze-Syntax

```python
func.substr(<str>, <pos>[, <len>])
```

## Analyze-Beispiele

```python
func.substr('StarRocks', 5, 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL-Syntax

```sql
SUBSTR(<str>, <pos>[, <len>])
```

## SQL-Beispiele

```sql
SELECT SUBSTR('StarRocks', 5, 5);

┌───────┐
│ Rocks  │
└───────┘
```
