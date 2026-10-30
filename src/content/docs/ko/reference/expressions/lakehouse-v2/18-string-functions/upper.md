---
title: UPPER (Lakehouse v2)
description: UPPER — 문자열을 대문자로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/upper.md
---

문자열을 대문자로 변환합니다.

## Analyze 구문

```python
func.upper(<str>)
```

## Analyze 예제

```python
func.upper('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## SQL 구문

```sql
UPPER(<str>)
```

## SQL 예제

```sql
SELECT UPPER('hello');

┌───────┐
│ HELLO  │
└───────┘
```
