---
title: POW (Lakehouse v2)
description: POW – gibt eine Zahl potenziert mit einer anderen Zahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pow.md
---

Gibt eine Zahl potenziert mit einer anderen Zahl zurück.

## Analyze-Syntax

```python
func.pow(<x>, <y>)
```

## Analyze-Beispiele

```python
func.pow(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## SQL-Syntax

```sql
POW(<x>, <y>)
```

## SQL-Beispiele

```sql
SELECT POW(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
