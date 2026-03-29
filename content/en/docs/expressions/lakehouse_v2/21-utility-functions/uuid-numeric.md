---
title: UUID_NUMERIC
---

Returns a random UUID as a 128-bit LARGEINT value.

## Analyze Syntax

```python
func.uuid_numeric()
```

## Analyze Examples

```python
func.uuid_numeric()

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQL Syntax

```sql
UUID_NUMERIC()
```

## SQL Examples

```sql
SELECT UUID_NUMERIC();

┌─────────────────────────────────────────┐
│ 113304629137197850819971302868472922876  │
└─────────────────────────────────────────┘
```
