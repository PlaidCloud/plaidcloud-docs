---
title: H3_GET_BASE_CELL
description: "Learn how to use the H3_GET_BASE_CELL utility function in PlaidCloud Lakehouse. Returns the base cell number of the given H3 index. With syntax and examples."
---

Returns the base cell number of the given [H3](https://eng.uber.com/h3/) index. 

## Analyze Syntax

```python
func.h3_get_base_cell(h3)
```

## Analyze Examples

```python
func.h3_get_base_cell(644325524701193974)

┌───────────────────────────────────────────┐
│ func.h3_get_base_cell(644325524701193974) │
├───────────────────────────────────────────┤
│                                         8 │
└───────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_GET_BASE_CELL(h3)
```

## SQL Examples

```sql
SELECT H3_GET_BASE_CELL(644325524701193974);

┌──────────────────────────────────────┐
│ h3_get_base_cell(644325524701193974) │
├──────────────────────────────────────┤
│                                    8 │
└──────────────────────────────────────┘
```