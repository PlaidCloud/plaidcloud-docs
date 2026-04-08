---
title: HOST_NAME
description: "Learn how to use the HOST_NAME utility function in PlaidCloud Lakehouse. Returns the host name of the current backend node - with syntax and examples."
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
