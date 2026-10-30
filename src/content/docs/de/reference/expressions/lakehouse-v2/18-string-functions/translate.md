---
title: TRANSLATE (Lakehouse v2)
description: TRANSLATE — Ersetzt Zeichen in einer Zeichenfolge anhand einer Zeichenzuordnung.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/translate.md
---

Ersetzt Zeichen in einer Zeichenfolge anhand einer Zeichenzuordnung.

## Analyze-Syntax

```python
func.translate(<str>, <from>, <to>)
```

## Analyze-Beispiele

```python
func.translate('hello', 'el', 'ip')

┌─────────┐
│ 'hippo'  │
└─────────┘
```

## SQL-Syntax

```sql
TRANSLATE(<str>, <from>, <to>)
```

## SQL-Beispiele

```sql
SELECT TRANSLATE('hello', 'el', 'ip');

┌───────┐
│ hippo  │
└───────┘
```
