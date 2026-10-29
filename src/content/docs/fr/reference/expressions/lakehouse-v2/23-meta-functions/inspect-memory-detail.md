---
title: INSPECT_MEMORY_DETAIL (Lakehouse v2)
description: INSPECT_MEMORY_DETAIL — renvoie des informations détaillées sur l'utilisation de la mémoire.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory-detail.md
---

Renvoie des informations détaillées sur l'utilisation de la mémoire.

## Syntaxe Analyze

```python
func.inspect_memory_detail()
```

## Exemples Analyze

```python
func.inspect_memory_detail()

┌──────────┐
│ (detail)  │
└──────────┘
```

## Syntaxe SQL

```sql
INSPECT_MEMORY_DETAIL()
```

## Exemples SQL

```sql
SELECT * FROM TABLE(INSPECT_MEMORY_DETAIL());

┌─────────────────┐
│ (memory detail)  │
└─────────────────┘
```
