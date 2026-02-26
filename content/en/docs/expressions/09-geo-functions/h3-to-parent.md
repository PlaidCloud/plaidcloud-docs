---
title: H3_TO_PARENT
---

Returns the parent index containing the `h3` at resolution `parent_res`. Returning 0 means an error occurred.

## Analyze Syntax

```python
func.h3_to_parent(h3, parent_res)
```

## Analyze Examples

```python
func.h3_to_parent(635318325446452991, 12)

┌───────────────────────────────────────────┐
│ func.h3_to_parent(635318325446452991, 12) │
├───────────────────────────────────────────┤
│                        630814725819082751 │
└───────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_TO_PARENT(h3, parent_res)
```

## SQL Examples

```sql
SELECT H3_TO_PARENT(635318325446452991, 12);

┌──────────────────────────────────────┐
│ h3_to_parent(635318325446452991, 12) │
├──────────────────────────────────────┤
│                   630814725819082751 │
└──────────────────────────────────────┘
```