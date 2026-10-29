---
title: TO_JSON (Lakehouse v2)
description: TO_JSON — SQL 값을 JSON 값으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/to-json.md
---

SQL 값을 JSON 값으로 변환합니다.

## Analyze 구문

```python
func.to_json(get_column(table, 'struct_col'))
```

## Analyze 예제

```python
func.to_json(func.named_struct('name', 'Alice', 'age', 30))

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## SQL 구문

```sql
TO_JSON(<struct_col>)
```

## SQL 예제

```sql
SELECT TO_JSON(NAMED_STRUCT('name', 'Alice', 'age', 30));

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
