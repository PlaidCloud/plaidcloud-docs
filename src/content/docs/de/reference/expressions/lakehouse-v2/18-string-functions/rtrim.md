---
title: RTRIM (Lakehouse v2)
description: RTRIM — entfernt nachgestellte Leerzeichen oder angegebene Zeichen aus einer Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rtrim.md
---

Entfernt nachgestellte Leerzeichen oder angegebene Zeichen aus einer Zeichenfolge.

## Analyze-Syntax

```python
func.rtrim(<str>)
```

## Analyze-Beispiele

```python
func.rtrim('hello   ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL-Syntax

```sql
RTRIM(<str>)
```

## SQL-Beispiele

```sql
SELECT RTRIM('hello   ');

┌───────┐
│ hello  │
└───────┘
```
