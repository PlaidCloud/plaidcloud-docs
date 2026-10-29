---
title: FIND_IN_SET (Lakehouse v2)
description: FIND_IN_SET — 쉼표로 구분된 목록에서 문자열의 위치를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/find-in-set.md
---

쉼표로 구분된 목록에서 문자열의 위치를 반환합니다.

## Analyze 구문

```python
func.find_in_set(<str>, <strlist>)
```

## Analyze 예제

```python
func.find_in_set('b', 'a,b,c')

┌───┐
│ 2  │
└───┘
```

## SQL 구문

```sql
FIND_IN_SET(<str>, <strlist>)
```

## SQL 예제

```sql
SELECT FIND_IN_SET('b', 'a,b,c');

┌───┐
│ 2  │
└───┘
```
