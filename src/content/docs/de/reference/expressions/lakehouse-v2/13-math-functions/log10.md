---
title: LOG10 (Lakehouse v2)
description: LOG10 – gibt den Logarithmus einer Zahl zur Basis 10 zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log10.md
---

Gibt den Logarithmus einer Zahl zur Basis 10 zurück.

## Analyze-Syntax

```python
func.log10(<x>)
```

## Analyze-Beispiele

```python
func.log10(1000)

┌─────┐
│ 3.0  │
└─────┘
```

## SQL-Syntax

```sql
LOG10(<x>)
```

## SQL-Beispiele

```sql
SELECT LOG10(1000);

┌─────┐
│ 3.0  │
└─────┘
```
