---
title: TO_BOOLEAN (Lakehouse v1)
description: TO_BOOLEAN — 값을 BOOLEAN 데이터 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-boolean.md
---

값을 BOOLEAN 데이터 형식으로 변환합니다.

## Analyze 구문

```python
func.to_boolean( <expr> )
```

## Analyze 예제

```python
func.to_boolean('true')

┌──────────────────────────┐
│ func.to_boolean('true')  │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## SQL 구문

```sql
TO_BOOLEAN( <expr> )
```

## SQL 예제

```sql
SELECT TO_BOOLEAN('true');

┌────────────────────┐
│ to_boolean('true') │
├────────────────────┤
│ true               │
└────────────────────┘
```
