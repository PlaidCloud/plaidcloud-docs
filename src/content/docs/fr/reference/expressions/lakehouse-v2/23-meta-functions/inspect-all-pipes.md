---
title: INSPECT_ALL_PIPES (Lakehouse v2)
description: INSPECT_ALL_PIPES — renvoie des informations sur tous les objets pipe.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-all-pipes.md
---

Renvoie des informations sur tous les objets pipe.

## Syntaxe Analyze

```python
func.inspect_all_pipes()
```

## Exemples Analyze

```python
func.inspect_all_pipes()

┌─────────────┐
│ (pipe info)  │
└─────────────┘
```

## Syntaxe SQL

```sql
INSPECT_ALL_PIPES()
```

## Exemples SQL

```sql
SELECT * FROM TABLE(INSPECT_ALL_PIPES());

┌────────────────┐
│ (pipe details)  │
└────────────────┘
```
