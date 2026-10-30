---
title: H3_TO_CENTER_CHILD (Lakehouse v1)
description: H3_TO_CENTER_CHILD — gibt den zentralen Kindindex bei der angegebenen Auflösung zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-center-child.md
---

Gibt den zentralen Kindindex bei der angegebenen Auflösung zurück.

## Analyze-Syntax

```python
func.h3_to_center_child(h3, res)
```

## Analyze-Beispiele

```python
func.h3_to_center_child(599119489002373119, 15)

┌─────────────────────────────────────────────────┐
│ func.h3_to_center_child(599119489002373119, 15) │
├─────────────────────────────────────────────────┤
│                              644155484202336256 │
└─────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_TO_CENTER_CHILD(h3, res)
```

## SQL-Beispiele

```sql
SELECT H3_TO_CENTER_CHILD(599119489002373119, 15);

┌────────────────────────────────────────────┐
│ h3_to_center_child(599119489002373119, 15) │
├────────────────────────────────────────────┤
│                         644155484202336256 │
└────────────────────────────────────────────┘
```
