---
title: CBRT (Lakehouse v1)
description: CBRT — 음수가 아닌 수 x의 세제곱근을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cbrt.md
---

음수가 아닌 수 `x`의 세제곱근을 반환합니다.

## Analyze 구문

```python
func.cbrt( <x> )
```

## Analyze 예시

```python
func.cbrt(27)

┌───────────────┐
│ func.cbrt(27) │
├───────────────┤
│             3 │
└───────────────┘
```

## SQL 구문

```sql
CBRT( <x> )
```

## SQL 예시

```sql
SELECT CBRT(27);

┌──────────┐
│ cbrt(27) │
├──────────┤
│        3 │
└──────────┘
```
