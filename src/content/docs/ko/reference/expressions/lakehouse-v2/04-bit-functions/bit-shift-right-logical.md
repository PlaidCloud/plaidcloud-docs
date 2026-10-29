---
title: BIT_SHIFT_RIGHT_LOGICAL (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 BIT_SHIFT_RIGHT_LOGICAL 비트 함수를 사용합니다. 숫자 값의 비트를 지정한 위치 수만큼 오른쪽으로 이동합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right-logical.md
---

숫자 값의 비트를 지정한 위치 수만큼 오른쪽으로 이동합니다(논리 이동).

## Analyze 구문

```python
func.bit_shift_right_logical(<value>, <shift>)
```

## Analyze 예제

```python
func.bit_shift_right_logical(16, 2)

┌───┐
│ 4  │
└───┘
```

## SQL 구문

```sql
BIT_SHIFT_RIGHT_LOGICAL(<value>, <shift>)
```

## SQL 예제

```sql
SELECT BIT_SHIFT_RIGHT_LOGICAL(16, 2);

┌───┐
│ 4  │
└───┘
```
