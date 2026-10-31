---
title: SPLIT_PART (Lakehouse v2)
description: SPLIT_PART — 구분자로 문자열을 분할하여 지정한 인덱스의 요소를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split-part.md
---

구분자로 문자열을 분할하여 지정한 인덱스의 요소를 반환합니다.

## Analyze 구문

```python
func.split_part(<str>, <delimiter>, <index>)
```

## Analyze 예제

```python
func.split_part('a-b-c', '-', 2)

┌─────┐
│ 'b'  │
└─────┘
```

## SQL 구문

```sql
SPLIT_PART(<str>, <delimiter>, <index>)
```

## SQL 예제

```sql
SELECT SPLIT_PART('a-b-c', '-', 2);

┌───┐
│ b  │
└───┘
```
