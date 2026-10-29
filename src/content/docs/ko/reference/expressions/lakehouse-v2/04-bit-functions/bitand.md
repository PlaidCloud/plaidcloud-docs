---
title: BITAND (Lakehouse v2)
description: BITAND — 두 숫자 값의 비트 AND 연산 결과를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitand.md
---

두 숫자 값의 비트 AND 연산 결과를 반환합니다.

## Analyze 구문

```python
func.bitand(<x>, <y>)
```

## Analyze 예제

```python
func.bitand(12, 10)

┌───┐
│ 8  │
└───┘
```

## SQL 구문

```sql
BITAND(<x>, <y>)
```

## SQL 예제

```sql
SELECT BITAND(12, 10);

┌───┐
│ 8  │
└───┘
```
