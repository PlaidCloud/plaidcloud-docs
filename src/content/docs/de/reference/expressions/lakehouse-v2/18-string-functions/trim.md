---
title: TRIM (Lakehouse v2)
description: TRIM — entfernt führende und nachgestellte Leerzeichen oder angegebene Zeichen aus einer Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/trim.md
---

Entfernt führende und nachgestellte Leerzeichen oder angegebene Zeichen aus einer Zeichenfolge.

## Analyze-Syntax

```python
func.trim(<str>)
```

## Analyze-Beispiele

```python
func.trim('  hello  ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL-Syntax

```sql
TRIM(<str>)
```

## SQL-Beispiele

```sql
SELECT TRIM('  hello  ');

┌───────┐
│ hello  │
└───────┘
```
