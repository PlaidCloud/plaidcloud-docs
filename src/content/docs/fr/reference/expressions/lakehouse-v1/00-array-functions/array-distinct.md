---
title: ARRAY_DISTINCT (Lakehouse v1)
description: "ARRAY_DISTINCT : supprime tous les doublons et les valeurs NULL du tableau sans conserver l'ordre d'origine."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-distinct.md
---

Supprime tous les doublons et les valeurs NULL du tableau sans conserver l'ordre d'origine.

## Syntaxe Analyze

```python
func.array_distinct( <array> )
```

## Exemples Analyze

```python
func.array_distinct([1, 2, 2, 4, 3])

┌───────────────────────────────────────┐
│ func.array_distinct([1, 2, 2, 4, 3])  │
├───────────────────────────────────────┤
│ [1,2,4,3]                             │
└───────────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_DISTINCT( <array> )
```

## Exemples SQL

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 4, 3]);

┌─────────────────────────────────┐
│ array_distinct([1, 2, 2, 4, 3]) │
├─────────────────────────────────┤
│ [1,2,4,3]                       │
└─────────────────────────────────┘
```
