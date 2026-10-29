---
title: TO_JSON (Lakehouse v2)
description: TO_JSON — convierte un valor SQL en un valor JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/to-json.md
---

Convierte un valor SQL en un valor JSON.

## Sintaxis de Analyze

```python
func.to_json(get_column(table, 'struct_col'))
```

## Ejemplos de Analyze

```python
func.to_json(func.named_struct('name', 'Alice', 'age', 30))

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_JSON(<struct_col>)
```

## Ejemplos de SQL

```sql
SELECT TO_JSON(NAMED_STRUCT('name', 'Alice', 'age', 30));

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
