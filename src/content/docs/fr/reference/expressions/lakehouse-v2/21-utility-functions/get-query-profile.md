---
title: GET_QUERY_PROFILE (Lakehouse v2)
description: GET_QUERY_PROFILE — renvoie le profil de requête correspondant à un ID de requête donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/get-query-profile.md
---

Renvoie le profil de requête correspondant à un ID de requête donné. Utile pour l'analyse des performances et le débogage.

## Syntaxe Analyze

```python
func.get_query_profile('query_id')
```

## Exemples Analyze

```python
func.get_query_profile('abc-123')

┌──────────────────────┐
│ (query profile text) │
└──────────────────────┘
```

## Syntaxe SQL

```sql
GET_QUERY_PROFILE(<query_id>)
```

## Exemples SQL

```sql
SELECT GET_QUERY_PROFILE(LAST_QUERY_ID());

┌──────────────────────────┐
│ (detailed query profile) │
└──────────────────────────┘
```
