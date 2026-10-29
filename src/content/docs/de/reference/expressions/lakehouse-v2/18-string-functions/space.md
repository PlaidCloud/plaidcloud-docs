---
title: SPACE (Lakehouse v2)
description: SPACE — Gibt eine Zeichenfolge zurück, die aus der angegebenen Anzahl von Leerzeichen besteht.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/space.md
---

Gibt eine Zeichenfolge zurück, die aus der angegebenen Anzahl von Leerzeichen besteht.

## Analyze-Syntax

```python
func.space(<n>)
```

## Analyze-Beispiele

```python
func.space(5)

┌─────────┐
│ '     '  │
└─────────┘
```

## SQL-Syntax

```sql
SPACE(<n>)
```

## SQL-Beispiele

```sql
SELECT CONCAT('>', SPACE(5), '<');

┌─────────┐
│ >     <  │
└─────────┘
```
