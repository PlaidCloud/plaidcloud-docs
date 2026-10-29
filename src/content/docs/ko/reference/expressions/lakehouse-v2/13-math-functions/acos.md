---
title: ACOS (Lakehouse v2)
description: ACOS — 숫자의 아크코사인을 라디안 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/acos.md
---

숫자의 아크코사인을 라디안 단위로 반환합니다.

## Analyze 구문

```python
func.acos(<x>)
```

## Analyze 예제

```python
func.acos(0.5)

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```

## SQL 구문

```sql
ACOS(<x>)
```

## SQL 예제

```sql
SELECT ACOS(0.5);

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```
