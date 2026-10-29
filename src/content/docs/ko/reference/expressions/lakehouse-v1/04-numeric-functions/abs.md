---
title: ABS (Lakehouse v1)
description: ABS — x의 절댓값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/abs.md
---

`x`의 절댓값을 반환합니다.

## Analyze 구문

```python
func.abs( <x> )
```

## Analyze 예시

```python
func.abs((- 5))

┌─────────────────┐
│ func.abs((- 5)) │
├─────────────────┤
│               5 │
└─────────────────┘
```

## SQL 구문

```sql
ABS( <x> )
```

## SQL 예시

```sql
SELECT ABS(-5);

┌────────────┐
│ abs((- 5)) │
├────────────┤
│          5 │
└────────────┘
```
