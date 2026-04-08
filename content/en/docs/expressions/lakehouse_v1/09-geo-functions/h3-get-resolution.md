---
title: H3_GET_RESOLUTION
description: "Learn how to use the H3_GET_RESOLUTION utility function in PlaidCloud Lakehouse. Returns the resolution of the given H3 index. Includes syntax and examples."
---

Returns the resolution of the given [H3](https://eng.uber.com/h3/) index. 

## Analyze Syntax

```python
func.h3_get_resolution(h3)
```

## Analyze Examples

```python
func.h3_get_resolution(644325524701193974)

┌────────────────────────────────────────────┐
│ func.h3_get_resolution(644325524701193974) │
├────────────────────────────────────────────┤
│                                         15 │
└────────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_GET_RESOLUTION(h3)
```

## SQL Examples

```sql
SELECT H3_GET_RESOLUTION(644325524701193974);

┌───────────────────────────────────────┐
│ h3_get_resolution(644325524701193974) │
├───────────────────────────────────────┤
│                                    15 │
└───────────────────────────────────────┘
```