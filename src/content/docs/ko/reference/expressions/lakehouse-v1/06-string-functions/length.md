---
title: LENGTH (Lakehouse v1)
description: LENGTH — 지정한 입력 문자열 또는 이진 값의 길이를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/length.md
---

지정한 입력 문자열 또는 이진 값의 길이를 반환합니다. 문자열의 경우 길이는 문자 수를 나타내며, 각 UTF-8 문자를 하나의 문자로 계산합니다. 이진 데이터의 경우 길이는 바이트 수에 해당합니다.

## Analyze 구문

```python
func.length(<expr>)
```

## Analyze 예제

```python
func.length('Hello')
┌──────────────────────┐
│ func.length('Hello') │
├──────────────────────┤
│                    5 │
└──────────────────────┘
```

## SQL 구문

```sql
LENGTH(<expr>)
```

## 별칭

- [CHAR_LENGTH](../char-length)
- [CHARACTER_LENGTH](../character-length)
- [LENGTH_UTF8](../length-utf8)

## 반환 형식

BIGINT

## SQL 예제

```sql
SELECT LENGTH('Hello'), LENGTH_UTF8('Hello'), CHAR_LENGTH('Hello'), CHARACTER_LENGTH('Hello');

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ length('hello') │ length_utf8('hello') │ char_length('hello') │ character_length('hello') │
├─────────────────┼──────────────────────┼──────────────────────┼───────────────────────────┤
│               5 │                    5 │                    5 │                         5 │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```
