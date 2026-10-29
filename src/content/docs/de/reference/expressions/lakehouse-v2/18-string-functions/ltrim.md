---
title: LTRIM (Lakehouse v2)
description: LTRIM — Entfernt führende Leerzeichen oder angegebene Zeichen aus einer Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ltrim.md
---

Entfernt führende Leerzeichen oder angegebene Zeichen aus einer Zeichenfolge.

## Analyze-Syntax

```python
func.ltrim(<str>)
```

## Analyze-Beispiele

```python
func.ltrim('   hello')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL-Syntax

```sql
LTRIM(<str>)
```

## SQL-Beispiele

```sql
SELECT LTRIM('   hello');

┌───────┐
│ hello  │
└───────┘
```
