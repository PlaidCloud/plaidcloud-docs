---
title: REPLACE (Lakehouse v2)
description: REPLACE — 문자열에서 일치하는 모든 부분 문자열을 다른 부분 문자열로 바꿉니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/replace.md
---

문자열에서 일치하는 모든 부분 문자열을 다른 부분 문자열로 바꿉니다.

## Analyze 구문

```python
func.replace(<str>, <old>, <new>)
```

## Analyze 예제

```python
func.replace('hello world', 'world', 'there')

┌───────────────┐
│ 'hello there'  │
└───────────────┘
```

## SQL 구문

```sql
REPLACE(<str>, <old>, <new>)
```

## SQL 예제

```sql
SELECT REPLACE('hello world', 'world', 'there');

┌─────────────┐
│ hello there  │
└─────────────┘
```
