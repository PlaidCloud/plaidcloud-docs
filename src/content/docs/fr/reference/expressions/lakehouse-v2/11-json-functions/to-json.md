---
title: TO_JSON (Lakehouse v2)
description: TO_JSON — convertit une valeur SQL en valeur JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/to-json.md
---

Convertit une valeur SQL en valeur JSON.

## Syntaxe Analyze

```python
func.to_json(get_column(table, 'struct_col'))
```

## Exemples Analyze

```python
func.to_json(func.named_struct('name', 'Alice', 'age', 30))

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## Syntaxe SQL

```sql
TO_JSON(<struct_col>)
```

## Exemples SQL

```sql
SELECT TO_JSON(NAMED_STRUCT('name', 'Alice', 'age', 30));

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
