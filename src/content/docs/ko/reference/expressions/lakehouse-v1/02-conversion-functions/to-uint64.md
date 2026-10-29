---
title: TO_UINT64 (Lakehouse v1)
description: TO_UINT64 — 값을 UINT64 데이터 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint64.md
---

값을 UINT64 데이터 형식으로 변환합니다.

## Analyze 구문

```python
func.to_uint64( <expr> )
```

## Analyze 예제

```python
func.to_uint64('123')

┌───────────────────────┐
│ func.to_uint64('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQL 구문

```sql
TO_UINT64( <expr> )
```

## SQL 예제

```sql
SELECT TO_UINT64('123');

┌──────────────────┐
│ to_uint64('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
