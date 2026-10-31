---
title: LAST_QUERY_ID (Lakehouse v2)
description: LAST_QUERY_ID — Retorna o ID da consulta executada mais recentemente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/last-query-id.md
---

Retorna o ID da consulta executada mais recentemente.

## Sintaxe do Analyze

```python
func.last_query_id()
```

## Exemplos do Analyze

```python
func.last_query_id()

┌───────────────┐
│ 'abc-123-def'  │
└───────────────┘
```

## Sintaxe SQL

```sql
LAST_QUERY_ID()
```

## Exemplos de SQL

```sql
SELECT LAST_QUERY_ID();

┌─────────────────┐
│ abc-123-def-456  │
└─────────────────┘
```
