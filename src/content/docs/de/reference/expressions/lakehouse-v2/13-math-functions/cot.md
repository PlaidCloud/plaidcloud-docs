---
title: COT (Lakehouse v2)
description: COT – gibt den Kotangens einer Zahl im Bogenmaß zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cot.md
---

Gibt den Kotangens einer Zahl im Bogenmaß zurück.

## Analyze-Syntax

```python
func.cot(<x>)
```

## Analyze-Beispiele

```python
func.cot(1)

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```

## SQL-Syntax

```sql
COT(<x>)
```

## SQL-Beispiele

```sql
SELECT COT(1);

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```
