---
title: LOG (Lakehouse v2)
description: LOG – gibt den Logarithmus einer Zahl zur angegebenen Basis zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log.md
---

Gibt den Logarithmus einer Zahl zur angegebenen Basis zurück.

## Analyze-Syntax

```python
func.log(<base>, <x>)
```

## Analyze-Beispiele

```python
func.log(10, 100)

┌─────┐
│ 2.0  │
└─────┘
```

## SQL-Syntax

```sql
LOG(<base>, <x>)
```

## SQL-Beispiele

```sql
SELECT LOG(10, 100);

┌─────┐
│ 2.0  │
└─────┘
```
