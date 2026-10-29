---
title: REGEXP_EXTRACT (Lakehouse v2)
description: REGEXP_EXTRACT — 정규식 패턴과 일치하는 첫 번째 부분 문자열을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract.md
---

정규식 패턴과 일치하는 첫 번째 부분 문자열을 추출합니다.

## Analyze 구문

```python
func.regexp_extract(<str>, <pattern>[, <group>])
```

## Analyze 예제

```python
func.regexp_extract('price: $42.50', '\\$(\\d+\\.\\d+)', 1)

┌─────────┐
│ '42.50'  │
└─────────┘
```

## SQL 구문

```sql
REGEXP_EXTRACT(<str>, <pattern>[, <group>])
```

## SQL 예제

```sql
SELECT REGEXP_EXTRACT('price: $42.50', '\\$(\\d+\\.\\d+)', 1);

┌───────┐
│ 42.50  │
└───────┘
```
