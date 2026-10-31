---
title: SUBSTR (Lakehouse v2)
description: SUBSTR — 지정한 위치부터 시작하는 부분 문자열을 반환하며, 길이는 선택 사항입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substr.md
---

지정한 위치부터 시작하는 부분 문자열을 반환하며, 길이는 선택 사항입니다.

## Analyze 구문

```python
func.substr(<str>, <pos>[, <len>])
```

## Analyze 예제

```python
func.substr('StarRocks', 5, 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL 구문

```sql
SUBSTR(<str>, <pos>[, <len>])
```

## SQL 예제

```sql
SELECT SUBSTR('StarRocks', 5, 5);

┌───────┐
│ Rocks  │
└───────┘
```
