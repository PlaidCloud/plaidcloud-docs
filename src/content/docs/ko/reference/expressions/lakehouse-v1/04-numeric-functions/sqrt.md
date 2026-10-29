---
title: SQRT (Lakehouse v1)
description: SQRT — 음수가 아닌 수 x의 제곱근을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sqrt.md
---

음수가 아닌 수 `x`의 제곱근을 반환합니다. 음수를 입력하면 Nan을 반환합니다.

## Analyze 구문

```python
func.sqrt( <x> )
```

## Analyze 예시

```python
func.sqrt(4)

┌──────────────┐
│ func.sqrt(4) │
├──────────────┤
│            2 │
└──────────────┘
```

## SQL 구문

```sql
SQRT( <x> )
```

## SQL 예시

```sql
SELECT SQRT(4);

┌─────────┐
│ sqrt(4) │
├─────────┤
│       2 │
└─────────┘
```
