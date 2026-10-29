---
title: RPAD (Lakehouse v2)
description: RPAD — füllt eine Zeichenfolge rechts mit einer Füllzeichenfolge auf die angegebene Länge auf.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rpad.md
---

Füllt eine Zeichenfolge rechts mit einer Füllzeichenfolge auf die angegebene Länge auf.

## Analyze-Syntax

```python
func.rpad(<str>, <len>, <pad>)
```

## Analyze-Beispiele

```python
func.rpad('hello', 10, '.')

┌──────────────┐
│ 'hello.....'  │
└──────────────┘
```

## SQL-Syntax

```sql
RPAD(<str>, <len>, <pad>)
```

## SQL-Beispiele

```sql
SELECT RPAD('hello', 10, '.');

┌────────────┐
│ hello.....  │
└────────────┘
```
