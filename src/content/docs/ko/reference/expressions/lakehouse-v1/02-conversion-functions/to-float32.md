---
title: TO_FLOAT32 (Lakehouse v1)
description: TO_FLOAT32 — 값을 FLOAT32 데이터 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float32.md
---

값을 FLOAT32 데이터 형식으로 변환합니다.

## Analyze 구문

```python
func.to_float32( <expr> )
```

## Analyze 예제

```python
func.to_float32('1.2')

┌─────────────────────────┐
│ func.to_float32('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQL 구문

```sql
TO_FLOAT32( <expr> )
```

## SQL 예제

```sql
SELECT TO_FLOAT32('1.2');

┌───────────────────┐
│ to_float32('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
