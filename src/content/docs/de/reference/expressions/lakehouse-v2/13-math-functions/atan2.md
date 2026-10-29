---
title: ATAN2 (Lakehouse v2)
description: ATAN2 – gibt den Arkustangens von y/x zurück, wobei die Vorzeichen den Quadranten bestimmen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan2.md
---

Gibt den Arkustangens von y/x zurück, wobei die Vorzeichen den Quadranten bestimmen.

## Analyze-Syntax

```python
func.atan2(<y>, <x>)
```

## Analyze-Beispiele

```python
func.atan2(1, 1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## SQL-Syntax

```sql
ATAN2(<y>, <x>)
```

## SQL-Beispiele

```sql
SELECT ATAN2(1, 1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
