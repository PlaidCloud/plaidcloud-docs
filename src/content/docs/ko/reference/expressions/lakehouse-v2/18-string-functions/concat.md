---
title: CONCAT (Lakehouse v2)
description: CONCAT — 둘 이상의 문자열을 연결합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat.md
---

둘 이상의 문자열을 연결합니다.

## Analyze 구문

```python
func.concat(<str1>, <str2>[, ...])
```

## Analyze 예제

```python
func.concat('Star', 'Rocks')

┌─────────────┐
│ 'StarRocks'  │
└─────────────┘
```

## SQL 구문

```sql
CONCAT(<str1>, <str2>[, ...])
```

## SQL 예제

```sql
SELECT CONCAT('Star', 'Rocks');

┌───────────┐
│ StarRocks  │
└───────────┘
```
