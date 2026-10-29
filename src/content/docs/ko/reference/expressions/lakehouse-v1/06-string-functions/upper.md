---
title: UPPER (Lakehouse v1)
description: UPPER — 모든 문자를 대문자로 바꾼 문자열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/upper.md
---

모든 문자를 대문자로 바꾼 문자열을 반환합니다.

## Analyze 구문

```python
func.unhex(<expr>)
```

## Analyze 예제

```python
func.upper('hello, plaidcloud lakehouse!')
┌────────────────────────────────────────────┐
│ func.upper('hello, plaidcloud lakehouse!') │
├────────────────────────────────────────────┤
│ 'HELLO, PLAIDCLOUD LAKEHOUSE!'             │
└────────────────────────────────────────────┘
```

## SQL 구문

```sql
UPPER(<str>)
```

## 별칭

- [UCASE](../ucase)

## 반환 형식

VARCHAR

## SQL 예제

```sql
SELECT UPPER('hello, databend!'), UCASE('hello, databend!');

┌───────────────────────────────────────────────────────┐
│ upper('hello, databend!') │ ucase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ HELLO, DATABEND!          │ HELLO, DATABEND!          │
└───────────────────────────────────────────────────────┘
```
