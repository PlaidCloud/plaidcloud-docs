---
title: CITY64WITHSEED (Lakehouse v1)
description: CITY64WITHSEED — 문자열의 City64WithSeed 64비트 해시를 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/city64withseed.md
---

문자열의 City64WithSeed 64비트 해시를 계산합니다.

## Analyze 구문

```python
func.city64withseed(<expr1>, <expr2>)
```

## Analyze 예제

```python
func.city64withseed('1234567890', 12)

┌───────────────────────────────────────┐
│ func.city64withseed('1234567890', 12) │
├───────────────────────────────────────┤
│                  10660895976650300430 │
└───────────────────────────────────────┘
```

## SQL 구문

```sql
CITY64WITHSEED(<expr1>, <expr2>)
```

## SQL 예제

```sql
SELECT CITY64WITHSEED('1234567890', 12);

┌──────────────────────────────────┐
│ city64withseed('1234567890', 12) │
├──────────────────────────────────┤
│             10660895976650300430 │
└──────────────────────────────────┘
```
