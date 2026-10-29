---
title: ACOS (Lakehouse v1)
description: ACOS – gibt den Arkuskosinus von x zurück, also den Wert, dessen Kosinus x ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/acos.md
---

Gibt den Arkuskosinus von `x` zurück, also den Wert, dessen Kosinus `x` ist. Gibt NULL zurück, wenn `x` nicht im Bereich von -1 bis 1 liegt.

## Analyze-Syntax

```python
func.abs( <x> )
```

## Analyze-Beispiele

```python
func.abs(1)

┌──────────────┐
│ func.acos(1) │
├──────────────┤
│            0 │
└──────────────┘
```

## SQL-Syntax

```sql
ACOS( <x> )
```

## SQL-Beispiele

```sql
SELECT ACOS(1);

┌─────────┐
│ acos(1) │
├─────────┤
│       0 │
└─────────┘
```
