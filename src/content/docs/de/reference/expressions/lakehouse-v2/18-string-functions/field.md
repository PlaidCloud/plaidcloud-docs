---
title: FIELD (Lakehouse v2)
description: FIELD — Gibt die Indexposition eines Werts in einer Liste von Argumenten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/field.md
---

Gibt die Indexposition eines Werts in einer Liste von Argumenten zurück.

## Analyze-Syntax

```python
func.field(<str>, <val1>, <val2>[, ...])
```

## Analyze-Beispiele

```python
func.field('b', 'a', 'b', 'c')

┌───┐
│ 2  │
└───┘
```

## SQL-Syntax

```sql
FIELD(<str>, <val1>, <val2>[, ...])
```

## SQL-Beispiele

```sql
SELECT FIELD('b', 'a', 'b', 'c');

┌───┐
│ 2  │
└───┘
```
