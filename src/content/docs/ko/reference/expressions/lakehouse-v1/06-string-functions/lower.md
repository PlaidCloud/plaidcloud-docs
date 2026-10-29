---
title: LOWER (Lakehouse v1)
description: LOWER — 모든 문자를 소문자로 변경한 문자열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lower.md
---

모든 문자를 소문자로 변경한 문자열을 반환합니다.

## Analyze 구문

```python
func.lower(<str>)
```

## Analyze 예제

```python
func.lower('Hello, PlaidCloud!')
┌──────────────────────────────────┐
│ func.lower('Hello, PlaidCloud!') │
├──────────────────────────────────┤
│ hello, plaidcloud!               │
└──────────────────────────────────┘
```

## SQL 구문

```sql
LOWER(<str>)
```

## 별칭

- [LCASE](../lcase)

## 반환 형식

VARCHAR

## SQL 예제

```sql
SELECT LOWER('Hello, Databend!'), LCASE('Hello, Databend!');

┌───────────────────────────────────────────────────────┐
│ lower('hello, databend!') │ lcase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ hello, databend!          │ hello, databend!          │
└───────────────────────────────────────────────────────┘
```
