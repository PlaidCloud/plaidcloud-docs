---
title: ROW (Lakehouse v2)
description: ROW — 값 목록으로 구조체를 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/row.md
---

값 목록으로 구조체를 생성합니다.

## Analyze 구문

```python
func.row(<val1>[, <val2>, ...])
```

## Analyze 예제

```python
func.row('Alice', 30)

┌────────────────────────────┐
│ {'col1':'Alice','col2':30}  │
└────────────────────────────┘
```

## SQL 구문

```sql
ROW(<val1>[, <val2>, ...])
```

## SQL 예제

```sql
SELECT ROW('Alice', 30);

┌────────────────────────────┐
│ {"col1":"Alice","col2":30}  │
└────────────────────────────┘
```
