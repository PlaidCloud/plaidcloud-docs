---
title: SUBSTRING (Lakehouse v2)
description: SUBSTRING — 지정한 위치부터 시작하는 부분 문자열을 반환합니다. `SUBSTR`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring.md
---

지정한 위치부터 시작하는 부분 문자열을 반환합니다. `SUBSTR`의 별칭입니다.

## Analyze 구문

```python
func.substring(<str>, <pos>[, <len>])
```

## Analyze 예제

```python
func.substring('StarRocks', 1, 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL 구문

```sql
SUBSTRING(<str>, <pos>[, <len>])
```

## SQL 예제

```sql
SELECT SUBSTRING('StarRocks', 1, 4);

┌──────┐
│ Star  │
└──────┘
```
