---
title: STRLEFT (Lakehouse v2)
description: STRLEFT — 문자열의 왼쪽에서 N개의 문자를 반환합니다. `LEFT`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strleft.md
---

문자열의 왼쪽에서 N개의 문자를 반환합니다. `LEFT`의 별칭입니다.

## Analyze 구문

```python
func.strleft(<str>, <len>)
```

## Analyze 예제

```python
func.strleft('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL 구문

```sql
STRLEFT(<str>, <len>)
```

## SQL 예제

```sql
SELECT STRLEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
