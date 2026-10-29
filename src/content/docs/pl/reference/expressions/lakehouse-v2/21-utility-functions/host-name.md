---
title: HOST_NAME (Lakehouse v2)
description: HOST_NAME — zwraca nazwę hosta bieżącego węzła zaplecza.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/host-name.md
---

Zwraca nazwę hosta bieżącego węzła zaplecza.

## Składnia Analyze

```python
func.host_name()
```

## Przykłady Analyze

```python
func.host_name()

┌─────────────┐
│ 'be-node-1'  │
└─────────────┘
```

## Składnia SQL

```sql
HOST_NAME()
```

## Przykłady SQL

```sql
SELECT HOST_NAME();

┌───────────┐
│ be-node-1  │
└───────────┘
```
