---
title: LAST_QUERY_ID (Lakehouse v1)
description: LAST_QUERY_ID — zwraca identyfikator ostatniego zapytania w bieżącej sesji; indeks może mieć postać (-1, 1, 1+2).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/last-query-id.md
---

Zwraca identyfikator ostatniego zapytania w bieżącej sesji; indeks może mieć postać (-1, 1, 1+2)... Indeks spoza zakresu zwraca pusty ciąg znaków.

## Składnia Analyze

```python
func.last_query_id(<index>)
```

## Przykłady Analyze

```python
func.last_query_id(-1)

┌──────────────────────────────────────┐
│    func.last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```


## Składnia SQL

```sql
LAST_QUERY_ID(<index>)
```

## Przykłady SQL

```sql
SELECT LAST_QUERY_ID(-1);

┌──────────────────────────────────────┐
│         last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```
