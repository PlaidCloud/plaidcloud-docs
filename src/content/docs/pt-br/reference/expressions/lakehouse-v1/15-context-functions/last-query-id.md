---
title: LAST_QUERY_ID (Lakehouse v1)
description: LAST_QUERY_ID — retorna o ID da última consulta da sessão atual; o índice pode ser (-1, 1, 1+2).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/last-query-id.md
---

Retorna o ID da última consulta da sessão atual; o índice pode ser (-1, 1, 1+2)... Um índice fora do intervalo retorna uma string vazia.

## Sintaxe no Analyze

```python
func.last_query_id(<index>)
```

## Exemplos no Analyze

```python
func.last_query_id(-1)

┌──────────────────────────────────────┐
│    func.last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```


## Sintaxe SQL

```sql
LAST_QUERY_ID(<index>)
```

## Exemplos de SQL

```sql
SELECT LAST_QUERY_ID(-1);

┌──────────────────────────────────────┐
│         last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```
