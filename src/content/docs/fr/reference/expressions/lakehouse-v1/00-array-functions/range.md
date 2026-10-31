---
title: RANGE (Lakehouse v1)
description: "RANGE : renvoie un tableau constitué des valeurs de l'intervalle [début, fin[."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/range.md
---

Renvoie un tableau constitué des valeurs de l'intervalle [début, fin[.

## Syntaxe Analyze

```python
func.range( <start>, <end> )
```

## Exemples Analyze

```python
func.range(1, 5)

┌────────────────────┐
│  func.range(1, 5)  │
├────────────────────┤
│ [1,2,3,4]          │
└────────────────────┘
```

## Syntaxe SQL

```sql
RANGE( <start>, <end> )
```

## Exemples SQL

```sql
SELECT RANGE(1, 5);

┌───────────────┐
│  range(1, 5)  │
├───────────────┤
│ [1,2,3,4]     │
└───────────────┘
```
