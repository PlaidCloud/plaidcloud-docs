---
title: ATAN2 (Lakehouse v1)
description: ATAN2 — 두 변수 x와 y의 아크탄젠트를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan2.md
---

두 변수 `x`와 `y`의 아크탄젠트를 반환합니다. `y` / `x`의 아크탄젠트를 계산하는 것과 비슷하지만, 두 인수의 부호를 모두 사용하여 결과의 사분면을 결정합니다. `ATAN(y, x)`는 `ATAN2(y, x)`의 동의어입니다.

## Analyze 구문

```python
func.atan2( <y, x> )
```

## Analyze 예시

```python
func.atan2((- 2), 2)

┌─────────────────────┐
│ func.atan2((- 2), 2)│
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```

## SQL 구문

```sql
ATAN2( <y, x> )
```

## SQL 예시

```sql
SELECT ATAN2(-2, 2);

┌─────────────────────┐
│   atan2((- 2), 2)   │
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```
