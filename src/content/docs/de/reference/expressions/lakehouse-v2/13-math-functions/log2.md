---
title: LOG2 (Lakehouse v2)
description: LOG2 – gibt den Logarithmus einer Zahl zur Basis 2 zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log2.md
---

Gibt den Logarithmus einer Zahl zur Basis 2 zurück.

## Analyze-Syntax

```python
func.log2(<x>)
```

## Analyze-Beispiele

```python
func.log2(8)

┌─────┐
│ 3.0  │
└─────┘
```

## SQL-Syntax

```sql
LOG2(<x>)
```

## SQL-Beispiele

```sql
SELECT LOG2(8);

┌─────┐
│ 3.0  │
└─────┘
```
