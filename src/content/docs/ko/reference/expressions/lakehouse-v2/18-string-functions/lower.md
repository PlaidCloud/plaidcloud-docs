---
title: LOWER (Lakehouse v2)
description: LOWER — 문자열을 소문자로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lower.md
---

문자열을 소문자로 변환합니다.

## Analyze 구문

```python
func.lower(<str>)
```

## Analyze 예제

```python
func.lower('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 구문

```sql
LOWER(<str>)
```

## SQL 예제

```sql
SELECT LOWER('HELLO');

┌───────┐
│ hello  │
└───────┘
```
