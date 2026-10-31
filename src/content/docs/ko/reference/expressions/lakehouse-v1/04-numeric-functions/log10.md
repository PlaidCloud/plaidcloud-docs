---
title: LOG10 (Lakehouse v1)
description: LOG10 — x의 상용로그(밑이 10인 로그)를 반환합니다. 참조 문서입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log10.md
---

`x`의 상용로그(밑이 10인 로그)를 반환합니다. `x`가 0.0E0 이하이면 NULL을 반환합니다.


## Analyze 구문

```python
func.log10( <x> )
```

## Analyze 예시

```python
func.log10(100)

┌─────────────────┐
│ func.log10(100) │
├─────────────────┤
│               2 │
└─────────────────┘
```

## SQL 구문

```sql
LOG10( <x> )
```

## SQL 예시

```sql
SELECT LOG10(100);

┌────────────┐
│ log10(100) │
├────────────┤
│          2 │
└────────────┘
```
