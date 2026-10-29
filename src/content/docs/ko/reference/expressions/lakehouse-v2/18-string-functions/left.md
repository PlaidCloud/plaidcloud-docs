---
title: LEFT (Lakehouse v2)
description: LEFT — 문자열의 왼쪽에서 N개의 문자를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/left.md
---

문자열의 왼쪽에서 N개의 문자를 반환합니다.

## Analyze 구문

```python
func.left(<str>, <len>)
```

## Analyze 예제

```python
func.left('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL 구문

```sql
LEFT(<str>, <len>)
```

## SQL 예제

```sql
SELECT LEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
