---
title: "LOG(b, x) (Lakehouse v1)"
description: LOG(b, x) — x의 밑이 b인 로그를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logbx.md
---

`x`의 밑이 b인 로그를 반환합니다. `x`가 0.0E0 이하이면 NULL을 반환합니다.

## Analyze 구문

```python
func.log( <b, x> )
```

## Analyze 예시

```python
func.log(2, 65536)

┌────────────────────┐
│ func.log(2, 65536) │
├────────────────────┤
│                 16 │
└────────────────────┘
```

## SQL 구문

```sql
LOG( <b, x> )
```

## SQL 예시

```sql
SELECT LOG(2, 65536);

┌───────────────┐
│ log(2, 65536) │
├───────────────┤
│            16 │
└───────────────┘
```
