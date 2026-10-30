---
title: TO_UINT16 (Lakehouse v1)
description: TO_UINT16 — 값을 UINT16 데이터 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint16.md
---

값을 UINT16 데이터 형식으로 변환합니다.

## Analyze 구문

```python
func.to_uint16( <expr> )
```

## Analyze 예제

```python
func.to_uint16('123')

┌───────────────────────┐
│ func.to_uint16('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQL 구문

```sql
TO_UINT16( <expr> )
```

## SQL 예제

```sql
SELECT TO_UINT16('123');

┌──────────────────┐
│ to_uint16('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
