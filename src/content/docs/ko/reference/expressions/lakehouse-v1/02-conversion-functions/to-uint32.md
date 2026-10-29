---
title: TO_UINT32 (Lakehouse v1)
description: TO_UINT32 — 값을 UINT32 데이터 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint32.md
---

값을 UINT32 데이터 형식으로 변환합니다.

## Analyze 구문

```python
func.to_uint32( <expr> )
```

## Analyze 예제

```python
func.to_uint32('123')

┌───────────────────────┐
│ func.to_uint32('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQL 구문

```sql
TO_UINT32( <expr> )
```

## SQL 예제

```sql
SELECT TO_UINT32('123');

┌──────────────────┐
│ to_uint32('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
