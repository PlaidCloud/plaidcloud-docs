---
title: UCASE (Lakehouse v2)
description: UCASE — 문자열을 대문자로 변환합니다. `UPPER`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ucase.md
---

문자열을 대문자로 변환합니다. `UPPER`의 별칭입니다.

## Analyze 구문

```python
func.ucase(<str>)
```

## Analyze 예제

```python
func.ucase('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## SQL 구문

```sql
UCASE(<str>)
```

## SQL 예제

```sql
SELECT UCASE('hello');

┌───────┐
│ HELLO  │
└───────┘
```
