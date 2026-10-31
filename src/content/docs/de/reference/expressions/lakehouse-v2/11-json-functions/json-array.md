---
title: JSON_ARRAY (Lakehouse v2)
description: JSON_ARRAY – erstellt ein JSON-Array aus einer Liste von Werten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-array.md
---

Erstellt ein JSON-Array aus einer Liste von Werten.

## Analyze-Syntax

```python
func.json_array(1, 'hello', None)
```

## Analyze-Beispiele

```python
func.json_array(1, 'hello', None)

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```

## SQL-Syntax

```sql
JSON_ARRAY(1, 'hello', None)
```

## SQL-Beispiele

```sql
SELECT JSON_ARRAY(1, 'hello', NULL);

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```
