---
title: TRIM (Lakehouse v2)
description: TRIM — 문자열 앞뒤의 공백 또는 지정한 문자를 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/trim.md
---

문자열 앞뒤의 공백 또는 지정한 문자를 제거합니다.

## Analyze 구문

```python
func.trim(<str>)
```

## Analyze 예제

```python
func.trim('  hello  ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 구문

```sql
TRIM(<str>)
```

## SQL 예제

```sql
SELECT TRIM('  hello  ');

┌───────┐
│ hello  │
└───────┘
```
