---
title: NAMED_STRUCT (Lakehouse v2)
description: NAMED_STRUCT — 지정한 필드 이름과 값으로 구조체를 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/named-struct.md
---

지정한 필드 이름과 값으로 구조체를 생성합니다.

## Analyze 구문

```python
func.named_struct(<name1>, <val1>[, <name2>, <val2>, ...])
```

## Analyze 예제

```python
func.named_struct('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {'name':'Alice','age':30}  │
└───────────────────────────┘
```

## SQL 구문

```sql
NAMED_STRUCT(<name1>, <val1>[, <name2>, <val2>, ...])
```

## SQL 예제

```sql
SELECT NAMED_STRUCT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30}  │
└───────────────────────────┘
```
