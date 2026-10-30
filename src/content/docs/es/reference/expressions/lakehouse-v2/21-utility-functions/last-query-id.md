---
title: LAST_QUERY_ID (Lakehouse v2)
description: LAST_QUERY_ID — Devuelve el ID de la consulta ejecutada más recientemente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/last-query-id.md
---

Devuelve el ID de la consulta ejecutada más recientemente.

## Sintaxis de Analyze

```python
func.last_query_id()
```

## Ejemplos de Analyze

```python
func.last_query_id()

┌───────────────┐
│ 'abc-123-def'  │
└───────────────┘
```

## Sintaxis de SQL

```sql
LAST_QUERY_ID()
```

## Ejemplos de SQL

```sql
SELECT LAST_QUERY_ID();

┌─────────────────┐
│ abc-123-def-456  │
└─────────────────┘
```
