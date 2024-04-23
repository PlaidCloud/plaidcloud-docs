---
title: H3_IS_RES_CLASS_III
---

Checks if the given [H3](https://eng.uber.com/h3/) index has a resolution with Class III orientation.

## Analyze Syntax

```python
func.h3_is_res_class_iii(h3)
```

## Analyze Examples

```python
func.h3_is_res_class_iii(635318325446452991)

┌──────────────────────────────────────────────┐
│ func.h3_is_res_class_iii(635318325446452991) │
├──────────────────────────────────────────────┤
│ true                                         │
└──────────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_IS_RES_CLASS_III(h3)
```

## SQL Examples

```sql
SELECT H3_IS_RES_CLASS_III(635318325446452991);

┌─────────────────────────────────────────┐
│ h3_is_res_class_iii(635318325446452991) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```