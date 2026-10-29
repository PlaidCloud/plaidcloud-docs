---
title: ATAN2 (Lakehouse v2)
description: ATAN2 — renvoie l'arc tangente de y/x, en utilisant les signes pour déterminer le quadrant.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan2.md
---

Renvoie l'arc tangente de y/x, en utilisant les signes pour déterminer le quadrant.

## Syntaxe Analyze

```python
func.atan2(<y>, <x>)
```

## Exemples Analyze

```python
func.atan2(1, 1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## Syntaxe SQL

```sql
ATAN2(<y>, <x>)
```

## Exemples SQL

```sql
SELECT ATAN2(1, 1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
