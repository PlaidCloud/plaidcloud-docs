---
title: TAN (Lakehouse v2)
description: TAN — 라디안 단위 숫자의 탄젠트를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tan.md
---

라디안 단위 숫자의 탄젠트를 반환합니다.

## Analyze 구문

```python
func.tan(<x>)
```

## Analyze 예제

```python
func.tan(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQL 구문

```sql
TAN(<x>)
```

## SQL 예제

```sql
SELECT TAN(0);

┌─────┐
│ 0.0  │
└─────┘
```
