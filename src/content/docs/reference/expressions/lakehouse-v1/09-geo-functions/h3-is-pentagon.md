---
title: H3_IS_PENTAGON (Lakehouse v1)
description: H3_IS_PENTAGON — checks if the given H3 index represents a pentagonal cell.
---

Checks if the given [H3](https://eng.uber.com/h3/) index represents a pentagonal cell. 

## Analyze Syntax

```python
func.h3_is_pentagon(h3)
```

## Analyze Examples

```python
func.h3_is_pentagon(599119489002373119)

┌─────────────────────────────────────────┐
│ func.h3_is_pentagon(599119489002373119) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_IS_PENTAGON(h3)
```

## SQL Examples

```sql
SELECT H3_IS_PENTAGON(599119489002373119);

┌────────────────────────────────────┐
│ h3_is_pentagon(599119489002373119) │
├────────────────────────────────────┤
│ true                               │
└────────────────────────────────────┘
```
