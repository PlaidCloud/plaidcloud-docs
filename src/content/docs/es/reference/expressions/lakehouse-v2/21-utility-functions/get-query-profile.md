---
title: GET_QUERY_PROFILE (Lakehouse v2)
description: GET_QUERY_PROFILE — Devuelve el perfil de consulta de un ID de consulta especificado. Es útil para el análisis de rendimiento y la depuración.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/get-query-profile.md
---

Devuelve el perfil de consulta de un ID de consulta especificado. Es útil para el análisis de rendimiento y la depuración.

## Sintaxis de Analyze

```python
func.get_query_profile('query_id')
```

## Ejemplos de Analyze

```python
func.get_query_profile('abc-123')

┌──────────────────────┐
│ (query profile text) │
└──────────────────────┘
```

## Sintaxis de SQL

```sql
GET_QUERY_PROFILE(<query_id>)
```

## Ejemplos de SQL

```sql
SELECT GET_QUERY_PROFILE(LAST_QUERY_ID());

┌──────────────────────────┐
│ (detailed query profile) │
└──────────────────────────┘
```
