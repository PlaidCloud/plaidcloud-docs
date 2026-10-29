---
title: ASIN (Lakehouse v2)
description: ASIN — 숫자의 아크사인을 라디안 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/asin.md
---

숫자의 아크사인을 라디안 단위로 반환합니다.

## Analyze 구문

```python
func.asin(<x>)
```

## Analyze 예제

```python
func.asin(0.5)

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```

## SQL 구문

```sql
ASIN(<x>)
```

## SQL 예제

```sql
SELECT ASIN(0.5);

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```
