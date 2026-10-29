---
title: BIT_SHIFT_LEFT (Lakehouse v2)
description: BIT_SHIFT_LEFT — 숫자 값의 비트를 지정한 위치 수만큼 왼쪽으로 이동합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-left.md
---

숫자 값의 비트를 지정한 위치 수만큼 왼쪽으로 이동합니다.

## Analyze 구문

```python
func.bit_shift_left(<value>, <shift>)
```

## Analyze 예제

```python
func.bit_shift_left(1, 4)

┌────┐
│ 16  │
└────┘
```

## SQL 구문

```sql
BIT_SHIFT_LEFT(<value>, <shift>)
```

## SQL 예제

```sql
SELECT BIT_SHIFT_LEFT(1, 4);

┌────┐
│ 16  │
└────┘
```
