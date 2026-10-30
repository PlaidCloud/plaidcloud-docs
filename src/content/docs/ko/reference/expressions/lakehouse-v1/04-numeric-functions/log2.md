---
title: LOG2 (Lakehouse v1)
description: LOG2 — x의 밑이 2인 로그를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log2.md
---

`x`의 밑이 2인 로그를 반환합니다. `x`가 0.0E0 이하이면 NULL을 반환합니다.

## Analyze 구문

```python
func.log2( <x> )
```

## Analyze 예시

```python
func.log2(65536)

┌──────────────────┐
│ func.log2(65536) │
├──────────────────┤
│               16 │
└──────────────────┘
```

## SQL 구문

```sql
LOG2( <x> )
```

## SQL 예시

```sql
SELECT LOG2(65536);

┌─────────────┐
│ log2(65536) │
├─────────────┤
│          16 │
└─────────────┘
```
