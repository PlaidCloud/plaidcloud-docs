---
title: APPEND_TRAILING_CHAR_IF_ABSENT (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 APPEND_TRAILING_CHAR_IF_ABSENT 문자열 함수를 사용합니다. 문자열 끝에 지정한 문자가 없으면 해당 문자를 추가합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/append-trailing-char-if-absent.md
---

문자열 끝에 지정한 문자가 없으면 해당 문자를 추가합니다.

## Analyze 구문

```python
func.append_trailing_char_if_absent(<str>, <char>)
```

## Analyze 예제

```python
func.append_trailing_char_if_absent('hello', '!')

┌──────────┐
│ 'hello!'  │
└──────────┘
```

## SQL 구문

```sql
APPEND_TRAILING_CHAR_IF_ABSENT(<str>, <char>)
```

## SQL 예제

```sql
SELECT APPEND_TRAILING_CHAR_IF_ABSENT('hello', '!');

┌────────┐
│ hello!  │
└────────┘
```
