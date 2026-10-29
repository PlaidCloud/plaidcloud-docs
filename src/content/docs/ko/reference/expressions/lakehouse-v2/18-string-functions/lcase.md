---
title: LCASE (Lakehouse v2)
description: LCASE — 문자열을 소문자로 변환합니다. `LOWER`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lcase.md
---

문자열을 소문자로 변환합니다. `LOWER`의 별칭입니다.

## Analyze 구문

```python
func.lcase(<str>)
```

## Analyze 예제

```python
func.lcase('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 구문

```sql
LCASE(<str>)
```

## SQL 예제

```sql
SELECT LCASE('HELLO');

┌───────┐
│ hello  │
└───────┘
```
