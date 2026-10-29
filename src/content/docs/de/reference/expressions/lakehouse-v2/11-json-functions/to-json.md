---
title: TO_JSON (Lakehouse v2)
description: TO_JSON – wandelt einen SQL-Wert in einen JSON-Wert um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/to-json.md
---

Wandelt einen SQL-Wert in einen JSON-Wert um.

## Analyze-Syntax

```python
func.to_json(get_column(table, 'struct_col'))
```

## Analyze-Beispiele

```python
func.to_json(func.named_struct('name', 'Alice', 'age', 30))

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## SQL-Syntax

```sql
TO_JSON(<struct_col>)
```

## SQL-Beispiele

```sql
SELECT TO_JSON(NAMED_STRUCT('name', 'Alice', 'age', 30));

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
