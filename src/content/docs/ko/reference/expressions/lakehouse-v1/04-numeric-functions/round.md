---
title: ROUND (Lakehouse v1)
description: ROUND — 인수 x를 소수점 이하 d자리로 반올림합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/round.md
---

인수 x를 소수점 이하 d자리로 반올림합니다. 반올림 알고리즘은 x의 데이터 형식에 따라 달라집니다. d를 지정하지 않으면 기본값은 0입니다. d가 음수이면 값 x의 소수점 왼쪽 d자리가 0이 됩니다. d의 최대 절댓값은 30이며, 30(또는 -30)을 초과하는 자릿수는 잘립니다.

이 함수의 결과를 계산에 사용할 때는 반환 데이터 형식이 DOUBLE이므로 정밀도 문제가 발생해 최종 정확도에 영향을 줄 수 있다는 점에 유의하십시오.

```sql
SELECT ROUND(4/7, 4) - ROUND(3/7, 4); -- Result: 0.14280000000000004
SELECT ROUND(4/7, 4)::DECIMAL(8,4) - ROUND(3/7, 4)::DECIMAL(8,4); -- Result: 0.1428
```

## Analyze 구문

```python
func.round( <x, d> )
```

## Analyze 예시

```python
func.round(0.123, 2)

┌──────────────────────┐
│ func.round(0.123, 2) │
├──────────────────────┤
│                 0.12 │
└──────────────────────┘
```

## SQL 구문

```sql
ROUND( <x, d> )
```

## SQL 예시

```sql
SELECT ROUND(0.123, 2);

┌─────────────────┐
│ round(0.123, 2) │
├─────────────────┤
│ 0.12            │
└─────────────────┘
```
