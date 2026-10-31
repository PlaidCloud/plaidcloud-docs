---
title: ACOS (Lakehouse v2)
description: ACOS – gibt den Arkuskosinus einer Zahl im Bogenmaß zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/acos.md
---

Gibt den Arkuskosinus einer Zahl im Bogenmaß zurück.

## Analyze-Syntax

```python
func.acos(<x>)
```

## Analyze-Beispiele

```python
func.acos(0.5)

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```

## SQL-Syntax

```sql
ACOS(<x>)
```

## SQL-Beispiele

```sql
SELECT ACOS(0.5);

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```
