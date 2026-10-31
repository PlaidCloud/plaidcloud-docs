---
title: TO_INT32 (Lakehouse v1)
description: TO_INT32 — 값을 INT32 데이터 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int32.md
---

값을 INT32 데이터 형식으로 변환합니다.

## Analyze 구문

```python
func.to_int32( <expr> )
```

## Analyze 예제

```python
func.to_int32('123')

┌──────────────────────┐
│ func.to_int32('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQL 구문

```sql
TO_INT32( <expr> )
```

## SQL 예제

```sql
SELECT TO_INT32('123');

┌─────────────────┐
│ to_int32('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
