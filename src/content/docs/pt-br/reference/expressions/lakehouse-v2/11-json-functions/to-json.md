---
title: TO_JSON (Lakehouse v2)
description: TO_JSON — converte um valor SQL em um valor JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/to-json.md
---

Converte um valor SQL em um valor JSON.

## Sintaxe do Analyze

```python
func.to_json(get_column(table, 'struct_col'))
```

## Exemplos do Analyze

```python
func.to_json(func.named_struct('name', 'Alice', 'age', 30))

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## Sintaxe SQL

```sql
TO_JSON(<struct_col>)
```

## Exemplos de SQL

```sql
SELECT TO_JSON(NAMED_STRUCT('name', 'Alice', 'age', 30));

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
