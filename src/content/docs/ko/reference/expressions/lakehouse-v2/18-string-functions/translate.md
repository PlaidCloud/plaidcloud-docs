---
title: TRANSLATE (Lakehouse v2)
description: TRANSLATE — 문자 매핑에 따라 문자열의 문자를 바꿉니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/translate.md
---

문자 매핑에 따라 문자열의 문자를 바꿉니다.

## Analyze 구문

```python
func.translate(<str>, <from>, <to>)
```

## Analyze 예제

```python
func.translate('hello', 'el', 'ip')

┌─────────┐
│ 'hippo'  │
└─────────┘
```

## SQL 구문

```sql
TRANSLATE(<str>, <from>, <to>)
```

## SQL 예제

```sql
SELECT TRANSLATE('hello', 'el', 'ip');

┌───────┐
│ hippo  │
└───────┘
```
