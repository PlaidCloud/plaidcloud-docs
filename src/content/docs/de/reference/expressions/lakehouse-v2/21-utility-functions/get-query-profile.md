---
title: GET_QUERY_PROFILE (Lakehouse v2)
description: GET_QUERY_PROFILE — gibt das Abfrageprofil für eine angegebene Abfrage-ID zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/get-query-profile.md
---

Gibt das Abfrageprofil für eine angegebene Abfrage-ID zurück. Nützlich für Leistungsanalysen und Debugging.

## Analyze-Syntax

```python
func.get_query_profile('query_id')
```

## Analyze-Beispiele

```python
func.get_query_profile('abc-123')

┌──────────────────────┐
│ (query profile text) │
└──────────────────────┘
```

## SQL-Syntax

```sql
GET_QUERY_PROFILE(<query_id>)
```

## SQL-Beispiele

```sql
SELECT GET_QUERY_PROFILE(LAST_QUERY_ID());

┌──────────────────────────┐
│ (detailed query profile) │
└──────────────────────────┘
```
