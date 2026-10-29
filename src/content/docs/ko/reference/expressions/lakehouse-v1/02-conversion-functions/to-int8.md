---
title: TO_INT8 (Lakehouse v1)
description: TO_INT8 — 값을 INT8 데이터 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int8.md
---

값을 INT8 데이터 형식으로 변환합니다.

## Analyze 구문

```python
func.to_int8( <expr> )
```

## Analyze 예제

```python
func.to_int8('123')

┌─────────────────────┐
│ func.to_int8('123') │
├─────────────────────┤
│                 123 │
└─────────────────────┘
```

## SQL 구문

```sql
TO_INT8( <expr> )
```

## SQL 예제

```sql
SELECT TO_INT8('123');

┌────────────────┐
│ to_int8('123') │
│      UInt8     │
├────────────────┤
│            123 │
└────────────────┘
```
