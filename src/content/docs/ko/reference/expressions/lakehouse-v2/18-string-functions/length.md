---
title: LENGTH (Lakehouse v2)
description: LENGTH — 문자열의 길이를 바이트 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/length.md
---

문자열의 길이를 바이트 단위로 반환합니다.

## Analyze 구문

```python
func.length(<str>)
```

## Analyze 예제

```python
func.length('hello')

┌───┐
│ 5  │
└───┘
```

## SQL 구문

```sql
LENGTH(<str>)
```

## SQL 예제

```sql
SELECT LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
