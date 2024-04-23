---
title: H3_IS_VALID
---

Checks if the given [H3](https://eng.uber.com/h3/) index is valid.

## Analyze Syntax

```python
func.h3_is_valid(h3)
```

## Analyze Examples

```python
func.h3_is_valid(644325524701193974)

┌──────────────────────────────────────┐
│ func.h3_is_valid(644325524701193974) │
├──────────────────────────────────────┤
│ true                                 │
└──────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_IS_VALID(h3)
```

## SQL Examples

```sql
SELECT H3_IS_VALID(644325524701193974);

┌─────────────────────────────────┐
│ h3_is_valid(644325524701193974) │
├─────────────────────────────────┤
│ true                            │
└─────────────────────────────────┘
```