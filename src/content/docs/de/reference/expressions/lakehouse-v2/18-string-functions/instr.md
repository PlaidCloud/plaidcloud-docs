---
title: INSTR (Lakehouse v2)
description: INSTR — gibt die Position des ersten Vorkommens einer Teilzeichenfolge in einer Zeichenfolge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/instr.md
---

Gibt die Position des ersten Vorkommens einer Teilzeichenfolge in einer Zeichenfolge zurück.

## Analyze-Syntax

```python
func.instr(<str>, <substr>)
```

## Analyze-Beispiele

```python
func.instr('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## SQL-Syntax

```sql
INSTR(<str>, <substr>)
```

## SQL-Beispiele

```sql
SELECT INSTR('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
