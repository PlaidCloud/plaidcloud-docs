---
title: TRUNCATE (Lakehouse v2)
description: TRUNCATE — 숫자를 지정한 소수 자릿수로 버림합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/truncate.md
---

숫자를 지정한 소수 자릿수로 버림합니다.

## Analyze 구문

```python
func.truncate(<x>, <d>)
```

## Analyze 예제

```python
func.truncate(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## SQL 구문

```sql
TRUNCATE(<x>, <d>)
```

## SQL 예제

```sql
SELECT TRUNCATE(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
