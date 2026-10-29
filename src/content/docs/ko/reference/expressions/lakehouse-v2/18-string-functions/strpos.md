---
title: STRPOS (Lakehouse v2)
description: STRPOS — 부분 문자열이 처음 나타나는 위치를 반환합니다. `LOCATE`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strpos.md
---

부분 문자열이 처음 나타나는 위치를 반환합니다. `LOCATE`의 별칭입니다.

## Analyze 구문

```python
func.strpos(<str>, <substr>)
```

## Analyze 예제

```python
func.strpos('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## SQL 구문

```sql
STRPOS(<str>, <substr>)
```

## SQL 예제

```sql
SELECT STRPOS('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
