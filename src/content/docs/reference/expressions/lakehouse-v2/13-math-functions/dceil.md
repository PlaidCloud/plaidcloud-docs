---
title: DCEIL (Lakehouse v2)
description: DCEIL — alias for `CEIL`. See [CEIL](ceil).
---

Alias for `CEIL`. See [CEIL](ceil).

## Analyze Syntax

```python
func.dceil(3.2)
```

## Analyze Examples

```python
func.dceil(3.2)

┌───┐
│ 4 │
└───┘
```

## SQL Syntax

```sql
DCEIL(<x>)
```

## SQL Examples

```sql
SELECT DCEIL(3.2);

┌───┐
│ 4 │
└───┘
```
