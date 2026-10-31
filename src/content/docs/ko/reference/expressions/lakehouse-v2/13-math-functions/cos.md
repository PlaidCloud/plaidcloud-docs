---
title: COS (Lakehouse v2)
description: COS — 라디안 단위 숫자의 코사인을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cos.md
---

라디안 단위 숫자의 코사인을 반환합니다.

## Analyze 구문

```python
func.cos(<x>)
```

## Analyze 예제

```python
func.cos(0)

┌─────┐
│ 1.0  │
└─────┘
```

## SQL 구문

```sql
COS(<x>)
```

## SQL 예제

```sql
SELECT COS(0);

┌─────┐
│ 1.0  │
└─────┘
```
