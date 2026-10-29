---
title: RTRIM (Lakehouse v2)
description: RTRIM — 문자열 뒤쪽의 공백 또는 지정한 문자를 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rtrim.md
---

문자열 뒤쪽의 공백 또는 지정한 문자를 제거합니다.

## Analyze 구문

```python
func.rtrim(<str>)
```

## Analyze 예제

```python
func.rtrim('hello   ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 구문

```sql
RTRIM(<str>)
```

## SQL 예제

```sql
SELECT RTRIM('hello   ');

┌───────┐
│ hello  │
└───────┘
```
