---
title: SIGN (Lakehouse v1)
description: SIGN — x가 음수인지 여부에 따라 인수의 부호를 -1, 0 또는 1로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sign.md
---

`x`가 음수, 0, 양수인지에 따라 인수의 부호를 -1, 0 또는 1로 반환하며, 인수가 NULL이면 NULL을 반환합니다.

## Analyze 구문

```python
func.sign( <x> )
```

## Analyze 예시

```python
func.sign(0)

┌──────────────┐
│ func.sign(0) │
├──────────────┤
│            0 │
└──────────────┘
```

## SQL 구문

```sql
SIGN( <x> )
```

## SQL 예시

```sql
SELECT SIGN(0);

┌─────────┐
│ sign(0) │
├─────────┤
│       0 │
└─────────┘
```
