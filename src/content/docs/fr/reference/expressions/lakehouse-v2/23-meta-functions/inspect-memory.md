---
title: INSPECT_MEMORY (Lakehouse v2)
description: INSPECT_MEMORY — renvoie des informations sur l'utilisation de la mémoire du nœud courant.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory.md
---

Renvoie des informations sur l'utilisation de la mémoire du nœud courant.

## Syntaxe Analyze

```python
func.inspect_memory()
```

## Exemples Analyze

```python
func.inspect_memory()

┌───────────────┐
│ (memory info)  │
└───────────────┘
```

## Syntaxe SQL

```sql
INSPECT_MEMORY()
```

## Exemples SQL

```sql
SELECT * FROM TABLE(INSPECT_MEMORY());

┌──────────────────┐
│ (memory details)  │
└──────────────────┘
```
