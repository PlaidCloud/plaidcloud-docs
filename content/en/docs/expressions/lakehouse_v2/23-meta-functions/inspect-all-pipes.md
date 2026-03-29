---
title: INSPECT_ALL_PIPES
---

Returns information about all pipe objects.

## Analyze Syntax

```python
func.inspect_all_pipes()
```

## Analyze Examples

```python
func.inspect_all_pipes()

┌─────────────┐
│ (pipe info)  │
└─────────────┘
```

## SQL Syntax

```sql
INSPECT_ALL_PIPES()
```

## SQL Examples

```sql
SELECT * FROM TABLE(INSPECT_ALL_PIPES());

┌────────────────┐
│ (pipe details)  │
└────────────────┘
```
