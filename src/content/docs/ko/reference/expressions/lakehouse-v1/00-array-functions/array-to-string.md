---
title: ARRAY_TO_STRING (Lakehouse v1)
description: ARRAY_TO_STRING — 지정한 구분자를 사용하여 배열의 요소를 하나의 문자열로 연결합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-to-string.md
---

지정한 구분자를 사용하여 배열의 요소를 하나의 문자열로 연결합니다.

## Analyze 구문

```python
func.array_to_string( <array>, '<separator>' )
```

## Analyze 예제

```python
func.array_to_string(['apple', 'banana', 'cherry'], ', ') 

┌────────────────────────────────────────────────────────────┐
│ func.array_to_string(['apple', 'banana', 'cherry'], ', ')  │
├────────────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                      │
└────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_TO_STRING( <array>, '<separator>' )
```

## SQL 예제

```sql
SELECT ARRAY_TO_STRING(['Apple', 'Banana', 'Cherry'], ', ');

┌──────────────────────────────────────────────────────┐
│ array_to_string(['apple', 'banana', 'cherry'], ', ') │
├──────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                │
└──────────────────────────────────────────────────────┘
```
