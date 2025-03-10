---
title: H3_TO_STRING
---

Converts the representation of the given [H3](https://eng.uber.com/h3/) index to the string representation. 

## Analyze Syntax

```python
func.h3_to_string(h3)
```

## Analyze Examples

```python
func.h3_to_string(635318325446452991)

┌───────────────────────────────────────┐
│ func.h3_to_string(635318325446452991) │
├───────────────────────────────────────┤
│ 8d11aa6a38826ff                       │
└───────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_TO_STRING(h3)
```

## SQL Examples

```sql
SELECT H3_TO_STRING(635318325446452991);

┌──────────────────────────────────┐
│ h3_to_string(635318325446452991) │
├──────────────────────────────────┤
│ 8d11aa6a38826ff                  │
└──────────────────────────────────┘
```