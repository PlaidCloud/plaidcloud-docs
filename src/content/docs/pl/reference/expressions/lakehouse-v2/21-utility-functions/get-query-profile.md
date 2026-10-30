---
title: GET_QUERY_PROFILE (Lakehouse v2)
description: GET_QUERY_PROFILE — zwraca profil zapytania dla podanego identyfikatora zapytania.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/get-query-profile.md
---

Zwraca profil zapytania dla podanego identyfikatora zapytania. Przydatna w analizie wydajności i debugowaniu.

## Składnia Analyze

```python
func.get_query_profile('query_id')
```

## Przykłady Analyze

```python
func.get_query_profile('abc-123')

┌──────────────────────┐
│ (query profile text) │
└──────────────────────┘
```

## Składnia SQL

```sql
GET_QUERY_PROFILE(<query_id>)
```

## Przykłady SQL

```sql
SELECT GET_QUERY_PROFILE(LAST_QUERY_ID());

┌──────────────────────────┐
│ (detailed query profile) │
└──────────────────────────┘
```
