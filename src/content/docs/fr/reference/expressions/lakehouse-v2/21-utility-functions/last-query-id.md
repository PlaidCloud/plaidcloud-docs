---
title: LAST_QUERY_ID (Lakehouse v2)
description: LAST_QUERY_ID — renvoie l'ID de la requête exécutée le plus récemment.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/last-query-id.md
---

Renvoie l'ID de la requête exécutée le plus récemment.

## Syntaxe Analyze

```python
func.last_query_id()
```

## Exemples Analyze

```python
func.last_query_id()

┌───────────────┐
│ 'abc-123-def'  │
└───────────────┘
```

## Syntaxe SQL

```sql
LAST_QUERY_ID()
```

## Exemples SQL

```sql
SELECT LAST_QUERY_ID();

┌─────────────────┐
│ abc-123-def-456  │
└─────────────────┘
```
