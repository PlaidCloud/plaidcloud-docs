---
title: TO_JSON (Lakehouse v2)
description: TO_JSON — konwertuje wartość SQL na wartość JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/to-json.md
---

Konwertuje wartość SQL na wartość JSON.

## Składnia Analyze

```python
func.to_json(get_column(table, 'struct_col'))
```

## Przykłady Analyze

```python
func.to_json(func.named_struct('name', 'Alice', 'age', 30))

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## Składnia SQL

```sql
TO_JSON(<struct_col>)
```

## Przykłady SQL

```sql
SELECT TO_JSON(NAMED_STRUCT('name', 'Alice', 'age', 30));

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
