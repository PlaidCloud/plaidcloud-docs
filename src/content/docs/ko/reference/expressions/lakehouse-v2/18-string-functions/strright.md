---
title: STRRIGHT (Lakehouse v2)
description: STRRIGHT — 문자열의 오른쪽에서 N개의 문자를 반환합니다. `RIGHT`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strright.md
---

문자열의 오른쪽에서 N개의 문자를 반환합니다. `RIGHT`의 별칭입니다.

## Analyze 구문

```python
func.strright(<str>, <len>)
```

## Analyze 예제

```python
func.strright('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL 구문

```sql
STRRIGHT(<str>, <len>)
```

## SQL 예제

```sql
SELECT STRRIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
