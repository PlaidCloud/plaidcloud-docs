---
title: TRUNCATE (Lakehouse v1)
description: TRUNCATE — 수 x를 소수점 이하 d자리로 버림하여 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/truncate.md
---

수 `x`를 소수점 이하 `d`자리로 버림하여 반환합니다. `d`가 0이면 결과에는 소수점이나 소수 부분이 없습니다. `d`가 음수이면 값 `x`의 소수점 왼쪽 `d`자리가 0이 됩니다. `d`의 최대 절댓값은 30이며, 30(또는 -30)을 초과하는 자릿수는 잘립니다.

## Analyze 구문

```python
func.truncate( <x, d> )
```

## Analyze 예시

```python
func.truncate(1.223, 1)

┌─────────────────────────┐
│ func.truncate(1.223, 1) │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQL 구문

```sql
TRUNCATE( <x, d> )
```

## SQL 예시

```sql
SELECT TRUNCATE(1.223, 1);

┌────────────────────┐
│ truncate(1.223, 1) │
├────────────────────┤
│ 1.2                │
└────────────────────┘
```
