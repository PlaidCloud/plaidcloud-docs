---
title: LAST_QUERY_ID (Lakehouse v1)
description: LAST_QUERY_ID gibt die ID der letzten Abfrage in der aktuellen Sitzung zurück; der Index kann (-1, 1, 1+2) sein.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/last-query-id.md
---

Gibt die ID der letzten Abfrage in der aktuellen Sitzung zurück. Der Index kann (-1, 1, 1+2) ... sein; bei einem Index außerhalb des gültigen Bereichs wird eine leere Zeichenfolge zurückgegeben.

## Analyze-Syntax

```python
func.last_query_id(<index>)
```

## Analyze-Beispiele

```python
func.last_query_id(-1)

┌──────────────────────────────────────┐
│    func.last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```


## SQL-Syntax

```sql
LAST_QUERY_ID(<index>)
```

## SQL-Beispiele

```sql
SELECT LAST_QUERY_ID(-1);

┌──────────────────────────────────────┐
│         last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```
