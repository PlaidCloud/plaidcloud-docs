---
title: HOST_NAME (Lakehouse v2)
description: HOST_NAME — Retorna o nome do host do nó de backend atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/host-name.md
---

Retorna o nome do host do nó de backend atual.

## Sintaxe do Analyze

```python
func.host_name()
```

## Exemplos do Analyze

```python
func.host_name()

┌─────────────┐
│ 'be-node-1'  │
└─────────────┘
```

## Sintaxe SQL

```sql
HOST_NAME()
```

## Exemplos de SQL

```sql
SELECT HOST_NAME();

┌───────────┐
│ be-node-1  │
└───────────┘
```
