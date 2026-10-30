---
title: HOST_NAME (Lakehouse v2)
description: HOST_NAME — renvoie le nom d'hôte du nœud backend courant.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/host-name.md
---

Renvoie le nom d'hôte du nœud backend courant.

## Syntaxe Analyze

```python
func.host_name()
```

## Exemples Analyze

```python
func.host_name()

┌─────────────┐
│ 'be-node-1'  │
└─────────────┘
```

## Syntaxe SQL

```sql
HOST_NAME()
```

## Exemples SQL

```sql
SELECT HOST_NAME();

┌───────────┐
│ be-node-1  │
└───────────┘
```
