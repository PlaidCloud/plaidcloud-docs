---
title: H3_TO_CENTER_CHILD
description: "Learn how to use the H3_TO_CENTER_CHILD utility function in PlaidCloud Lakehouse. Returns the center child index at the specified resolution."
---

Returns the center child index at the specified resolution.

## Analyze Syntax

```python
func.h3_to_center_child(h3, res)
```

## Analyze Examples

```python
func.h3_to_center_child(599119489002373119, 15)

┌─────────────────────────────────────────────────┐
│ func.h3_to_center_child(599119489002373119, 15) │
├─────────────────────────────────────────────────┤
│                              644155484202336256 │
└─────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_TO_CENTER_CHILD(h3, res)
```

## SQL Examples

```sql
SELECT H3_TO_CENTER_CHILD(599119489002373119, 15);

┌────────────────────────────────────────────┐
│ h3_to_center_child(599119489002373119, 15) │
├────────────────────────────────────────────┤
│                         644155484202336256 │
└────────────────────────────────────────────┘
```
