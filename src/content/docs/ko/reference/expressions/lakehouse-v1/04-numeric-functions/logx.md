---
title: LOG(x) (Lakehouse v1)
description: LOG(x) — x의 자연로그를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logx.md
---

`x`의 자연로그를 반환합니다. x가 0.0E0 이하이면 NULL을 반환합니다.

## Analyze 구문

```python
 func.log( <x> )
```

## Analyze 예시

```python
 func.log(2)

┌────────────────────┐
│    func.log(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## SQL 구문

```sql
LOG( <x> )
```

## SQL 예시

```sql
SELECT LOG(2);

┌────────────────────┐
│       log(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
