---
title: H3_TO_CENTER_CHILD (Lakehouse v1)
description: H3_TO_CENTER_CHILD — devuelve el índice del hijo central en la resolución especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-center-child.md
---

Devuelve el índice del hijo central en la resolución especificada.

## Sintaxis de Analyze

```python
func.h3_to_center_child(h3, res)
```

## Ejemplos de Analyze

```python
func.h3_to_center_child(599119489002373119, 15)

┌─────────────────────────────────────────────────┐
│ func.h3_to_center_child(599119489002373119, 15) │
├─────────────────────────────────────────────────┤
│                              644155484202336256 │
└─────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_TO_CENTER_CHILD(h3, res)
```

## Ejemplos de SQL

```sql
SELECT H3_TO_CENTER_CHILD(599119489002373119, 15);

┌────────────────────────────────────────────┐
│ h3_to_center_child(599119489002373119, 15) │
├────────────────────────────────────────────┤
│                         644155484202336256 │
└────────────────────────────────────────────┘
```
