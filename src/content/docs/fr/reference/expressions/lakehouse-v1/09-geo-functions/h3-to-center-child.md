---
title: H3_TO_CENTER_CHILD (Lakehouse v1)
description: H3_TO_CENTER_CHILD — renvoie l'index de l'enfant central à la résolution indiquée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-center-child.md
---

Renvoie l'index de l'enfant central à la résolution indiquée.

## Syntaxe Analyze

```python
func.h3_to_center_child(h3, res)
```

## Exemples Analyze

```python
func.h3_to_center_child(599119489002373119, 15)

┌─────────────────────────────────────────────────┐
│ func.h3_to_center_child(599119489002373119, 15) │
├─────────────────────────────────────────────────┤
│                              644155484202336256 │
└─────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_TO_CENTER_CHILD(h3, res)
```

## Exemples SQL

```sql
SELECT H3_TO_CENTER_CHILD(599119489002373119, 15);

┌────────────────────────────────────────────┐
│ h3_to_center_child(599119489002373119, 15) │
├────────────────────────────────────────────┤
│                         644155484202336256 │
└────────────────────────────────────────────┘
```
