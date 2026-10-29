---
title: LTRIM (Lakehouse v2)
description: LTRIM — 문자열 앞쪽의 공백 또는 지정한 문자를 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ltrim.md
---

문자열 앞쪽의 공백 또는 지정한 문자를 제거합니다.

## Analyze 구문

```python
func.ltrim(<str>)
```

## Analyze 예제

```python
func.ltrim('   hello')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 구문

```sql
LTRIM(<str>)
```

## SQL 예제

```sql
SELECT LTRIM('   hello');

┌───────┐
│ hello  │
└───────┘
```
