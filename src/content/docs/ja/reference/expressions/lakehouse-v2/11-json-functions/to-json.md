---
title: TO_JSON (Lakehouse v2)
description: TO_JSON — SQL値をJSON値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/to-json.md
---

SQL値をJSON値に変換します。

## Analyzeの構文

```python
func.to_json(get_column(table, 'struct_col'))
```

## Analyzeの例

```python
func.to_json(func.named_struct('name', 'Alice', 'age', 30))

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## SQLの構文

```sql
TO_JSON(<struct_col>)
```

## SQLの例

```sql
SELECT TO_JSON(NAMED_STRUCT('name', 'Alice', 'age', 30));

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
