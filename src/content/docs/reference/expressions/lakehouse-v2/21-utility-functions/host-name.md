---
title: HOST_NAME (Lakehouse v2)
description: HOST_NAME — Returns the host name of the current backend node.
---

Returns the host name of the current backend node.

## Analyze Syntax

```python
func.host_name()
```

## Analyze Examples

```python
func.host_name()

┌─────────────┐
│ 'be-node-1'  │
└─────────────┘
```

## SQL Syntax

```sql
HOST_NAME()
```

## SQL Examples

```sql
SELECT HOST_NAME();

┌───────────┐
│ be-node-1  │
└───────────┘
```
