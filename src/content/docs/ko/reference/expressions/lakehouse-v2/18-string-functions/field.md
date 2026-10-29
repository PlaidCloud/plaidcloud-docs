---
title: FIELD (Lakehouse v2)
description: FIELD — 인수 목록에서 값의 인덱스 위치를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/field.md
---

인수 목록에서 값의 인덱스 위치를 반환합니다.

## Analyze 구문

```python
func.field(<str>, <val1>, <val2>[, ...])
```

## Analyze 예제

```python
func.field('b', 'a', 'b', 'c')

┌───┐
│ 2  │
└───┘
```

## SQL 구문

```sql
FIELD(<str>, <val1>, <val2>[, ...])
```

## SQL 예제

```sql
SELECT FIELD('b', 'a', 'b', 'c');

┌───┐
│ 2  │
└───┘
```
