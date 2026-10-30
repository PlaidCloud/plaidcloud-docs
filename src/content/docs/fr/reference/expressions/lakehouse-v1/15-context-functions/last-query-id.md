---
title: LAST_QUERY_ID (Lakehouse v1)
description: LAST_QUERY_ID — renvoie l'ID de la dernière requête de la session en cours ; l'index peut être (-1, 1, 1+2).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/last-query-id.md
---

Renvoie l'ID de la dernière requête de la session en cours ; l'index peut être (-1, 1, 1+2)... Un index hors plage renvoie une chaîne vide.

## Syntaxe Analyze

```python
func.last_query_id(<index>)
```

## Exemples Analyze

```python
func.last_query_id(-1)

┌──────────────────────────────────────┐
│    func.last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```


## Syntaxe SQL

```sql
LAST_QUERY_ID(<index>)
```

## Exemples SQL

```sql
SELECT LAST_QUERY_ID(-1);

┌──────────────────────────────────────┐
│         last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```
