---
title: COT (Lakehouse v1)
description: COT — x의 코탄젠트를 반환합니다. 이때 x는 라디안 단위입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cot.md
---

`x`의 코탄젠트를 반환합니다. 이때 `x`는 라디안 단위입니다.

## Analyze 구문

```python
func.cot( <x> )
```

## Analyze 예시

```python
func.cot(12) 

┌─────────────────────┐
│    func.cot(12)     │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```

## SQL 구문

```sql
COT( <x> )
```

## SQL 예시

```sql
SELECT COT(12);

┌─────────────────────┐
│       cot(12)       │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```
