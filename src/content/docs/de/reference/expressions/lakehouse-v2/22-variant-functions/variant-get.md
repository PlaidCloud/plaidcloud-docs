---
title: VARIANT_GET (Lakehouse v2)
description: VARIANT_GET — extrahiert einen typisierten Wert aus einem VARIANT-Objekt am angegebenen Pfad.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-get.md
---

Extrahiert einen typisierten Wert aus einem VARIANT-Objekt am angegebenen Pfad.

## Analyze-Syntax

```python
func.variant_get(<variant>, <path>, <type>)
```

## Analyze-Beispiele

```python
func.variant_get(get_column(table, 'data'), '$.name', 'STRING')

┌─────────┐
│ 'Alice'  │
└─────────┘
```

## SQL-Syntax

```sql
VARIANT_GET(<variant>, <path>, <type>)
```

## SQL-Beispiele

```sql
SELECT VARIANT_GET(data, '$.name', 'STRING') FROM events;

┌───────┐
│ Alice  │
└───────┘
```
