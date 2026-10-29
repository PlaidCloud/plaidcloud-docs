---
title: GET_QUERY_PROFILE (Lakehouse v2)
description: GET_QUERY_PROFILE — retorna o perfil de consulta de um ID de consulta especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/get-query-profile.md
---

Retorna o perfil de consulta de um ID de consulta especificado. Útil para análise de desempenho e depuração.

## Sintaxe do Analyze

```python
func.get_query_profile('query_id')
```

## Exemplos do Analyze

```python
func.get_query_profile('abc-123')

┌──────────────────────┐
│ (query profile text) │
└──────────────────────┘
```

## Sintaxe SQL

```sql
GET_QUERY_PROFILE(<query_id>)
```

## Exemplos de SQL

```sql
SELECT GET_QUERY_PROFILE(LAST_QUERY_ID());

┌──────────────────────────┐
│ (detailed query profile) │
└──────────────────────────┘
```
