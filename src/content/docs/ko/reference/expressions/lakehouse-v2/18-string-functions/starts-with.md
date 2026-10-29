---
title: STARTS_WITH (Lakehouse v2)
description: STARTS_WITH — 문자열이 지정한 접두사로 시작하는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/starts-with.md
---

문자열이 지정한 접두사로 시작하는지 확인합니다.

## Analyze 구문

```python
func.starts_with(<str>, <prefix>)
```

## Analyze 예제

```python
func.starts_with('StarRocks', 'Star')

┌───┐
│ 1  │
└───┘
```

## SQL 구문

```sql
STARTS_WITH(<str>, <prefix>)
```

## SQL 예제

```sql
SELECT STARTS_WITH('StarRocks', 'Star');

┌───┐
│ 1  │
└───┘
```
