---
title: RADIANS (Lakehouse v1)
description: RADIANS — 도 단위의 인수 x를 라디안으로 변환하여 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/radians.md
---

도 단위의 인수 `x`를 라디안으로 변환하여 반환합니다.

## Analyze 구문

```python
func.radians( <x> )
```

## Analyze 예시

```python
func.radians(90)

┌────────────────────┐
│  func.radians(90)  │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```

## SQL 구문

```sql
RADIANS( <x> )
```

## SQL 예시

```sql
SELECT RADIANS(90);

┌────────────────────┐
│     radians(90)    │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```
