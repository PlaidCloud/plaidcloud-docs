---
title: POW (Lakehouse v2)
description: POW — 숫자를 다른 숫자만큼 거듭제곱한 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pow.md
---

숫자를 다른 숫자만큼 거듭제곱한 값을 반환합니다.

## Analyze 구문

```python
func.pow(<x>, <y>)
```

## Analyze 예제

```python
func.pow(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## SQL 구문

```sql
POW(<x>, <y>)
```

## SQL 예제

```sql
SELECT POW(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
