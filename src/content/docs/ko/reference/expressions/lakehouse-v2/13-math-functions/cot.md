---
title: COT (Lakehouse v2)
description: COT — 라디안 단위 숫자의 코탄젠트를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cot.md
---

라디안 단위 숫자의 코탄젠트를 반환합니다.

## Analyze 구문

```python
func.cot(<x>)
```

## Analyze 예제

```python
func.cot(1)

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```

## SQL 구문

```sql
COT(<x>)
```

## SQL 예제

```sql
SELECT COT(1);

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```
