---
title: RIGHT (Lakehouse v2)
description: RIGHT — 문자열의 오른쪽에서 N개의 문자를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/right.md
---

문자열의 오른쪽에서 N개의 문자를 반환합니다.

## Analyze 구문

```python
func.right(<str>, <len>)
```

## Analyze 예제

```python
func.right('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL 구문

```sql
RIGHT(<str>, <len>)
```

## SQL 예제

```sql
SELECT RIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
