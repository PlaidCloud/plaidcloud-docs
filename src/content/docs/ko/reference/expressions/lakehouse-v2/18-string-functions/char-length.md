---
title: CHAR_LENGTH (Lakehouse v2)
description: CHAR_LENGTH — 문자열의 문자 수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char-length.md
---

문자열의 문자 수를 반환합니다.

## Analyze 구문

```python
func.char_length(<str>)
```

## Analyze 예제

```python
func.char_length('hello world')

┌────┐
│ 11  │
└────┘
```

## SQL 구문

```sql
CHAR_LENGTH(<str>)
```

## SQL 예제

```sql
SELECT CHAR_LENGTH('hello world');

┌────┐
│ 11  │
└────┘
```
