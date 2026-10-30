---
title: BITXOR (Lakehouse v2)
description: BITXOR — 두 숫자 값의 비트 XOR 연산 결과를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitxor.md
---

두 숫자 값의 비트 XOR 연산 결과를 반환합니다.

## Analyze 구문

```python
func.bitxor(<x>, <y>)
```

## Analyze 예제

```python
func.bitxor(12, 10)

┌───┐
│ 6  │
└───┘
```

## SQL 구문

```sql
BITXOR(<x>, <y>)
```

## SQL 예제

```sql
SELECT BITXOR(12, 10);

┌───┐
│ 6  │
└───┘
```
