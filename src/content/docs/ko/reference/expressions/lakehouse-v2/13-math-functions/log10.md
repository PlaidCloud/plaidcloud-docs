---
title: LOG10 (Lakehouse v2)
description: LOG10 — 숫자의 상용로그(밑 10)를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log10.md
---

숫자의 상용로그(밑 10)를 반환합니다.

## Analyze 구문

```python
func.log10(<x>)
```

## Analyze 예제

```python
func.log10(1000)

┌─────┐
│ 3.0  │
└─────┘
```

## SQL 구문

```sql
LOG10(<x>)
```

## SQL 예제

```sql
SELECT LOG10(1000);

┌─────┐
│ 3.0  │
└─────┘
```
