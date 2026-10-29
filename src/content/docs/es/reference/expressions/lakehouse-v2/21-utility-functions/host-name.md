---
title: HOST_NAME (Lakehouse v2)
description: HOST_NAME — Devuelve el nombre de host del nodo backend actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/host-name.md
---

Devuelve el nombre de host del nodo backend actual.

## Sintaxis de Analyze

```python
func.host_name()
```

## Ejemplos de Analyze

```python
func.host_name()

┌─────────────┐
│ 'be-node-1'  │
└─────────────┘
```

## Sintaxis de SQL

```sql
HOST_NAME()
```

## Ejemplos de SQL

```sql
SELECT HOST_NAME();

┌───────────┐
│ be-node-1  │
└───────────┘
```
