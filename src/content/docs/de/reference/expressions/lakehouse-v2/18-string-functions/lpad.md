---
title: LPAD (Lakehouse v2)
description: LPAD — füllt eine Zeichenfolge links mit einer Füllzeichenfolge auf die angegebene Länge auf.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lpad.md
---

Füllt eine Zeichenfolge links mit einer Füllzeichenfolge auf die angegebene Länge auf.

## Analyze-Syntax

```python
func.lpad(<str>, <len>, <pad>)
```

## Analyze-Beispiele

```python
func.lpad('42', 5, '0')

┌─────────┐
│ '00042'  │
└─────────┘
```

## SQL-Syntax

```sql
LPAD(<str>, <len>, <pad>)
```

## SQL-Beispiele

```sql
SELECT LPAD('42', 5, '0');

┌───────┐
│ 00042  │
└───────┘
```
