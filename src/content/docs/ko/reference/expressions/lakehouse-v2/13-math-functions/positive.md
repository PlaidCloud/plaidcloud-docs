---
title: POSITIVE (Lakehouse v2)
description: POSITIVE — 값을 변경하지 않고 그대로 반환합니다(단항 플러스).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/positive.md
---

값을 변경하지 않고 그대로 반환합니다(단항 플러스).

## Analyze 구문

```python
func.positive(<x>)
```

## Analyze 예제

```python
func.positive(-5)

┌────┐
│ -5  │
└────┘
```

## SQL 구문

```sql
POSITIVE(<x>)
```

## SQL 예제

```sql
SELECT POSITIVE(-5);

┌────┐
│ -5  │
└────┘
```
