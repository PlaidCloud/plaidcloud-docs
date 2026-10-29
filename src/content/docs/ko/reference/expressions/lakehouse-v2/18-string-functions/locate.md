---
title: LOCATE (Lakehouse v2)
description: LOCATE — 문자열에서 부분 문자열이 처음 나타나는 위치를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/locate.md
---

문자열에서 부분 문자열이 처음 나타나는 위치를 반환합니다.

## Analyze 구문

```python
func.locate(<substr>, <str>[, <pos>])
```

## Analyze 예제

```python
func.locate('or', 'hello world')

┌───┐
│ 8  │
└───┘
```

## SQL 구문

```sql
LOCATE(<substr>, <str>[, <pos>])
```

## SQL 예제

```sql
SELECT LOCATE('or', 'hello world');

┌───┐
│ 8  │
└───┘
```
