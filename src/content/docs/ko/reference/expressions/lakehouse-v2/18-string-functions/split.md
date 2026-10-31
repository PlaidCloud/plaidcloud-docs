---
title: SPLIT (Lakehouse v2)
description: SPLIT — 구분자로 문자열을 분할하여 배열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split.md
---

구분자로 문자열을 분할하여 배열을 반환합니다.

## Analyze 구문

```python
func.split(<str>, <delimiter>)
```

## Analyze 예제

```python
func.split('a,b,c', ',')

┌───────────────┐
│ ['a','b','c']  │
└───────────────┘
```

## SQL 구문

```sql
SPLIT(<str>, <delimiter>)
```

## SQL 예제

```sql
SELECT SPLIT('a,b,c', ',');

┌───────────────┐
│ ["a","b","c"]  │
└───────────────┘
```
