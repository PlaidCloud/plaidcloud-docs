---
title: UNHEX (Lakehouse v2)
description: UNHEX — 16진수 문자열을 문자열로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/unhex.md
---

16진수 문자열을 문자열로 변환합니다.

## Analyze 구문

```python
func.unhex(<hex_str>)
```

## Analyze 예제

```python
func.unhex('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL 구문

```sql
UNHEX(<hex_str>)
```

## SQL 예제

```sql
SELECT UNHEX('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
