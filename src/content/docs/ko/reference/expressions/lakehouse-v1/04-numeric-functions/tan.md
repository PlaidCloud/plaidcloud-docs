---
title: TAN (Lakehouse v1)
description: TAN — x의 탄젠트를 반환합니다. 이때 x는 라디안 단위입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/tan.md
---

`x`의 탄젠트를 반환합니다. 이때 `x`는 라디안 단위입니다.

## Analyze 구문

```python
func.tan( <x> )
```

## Analyze 예시

```python
func.tan(90)

┌────────────────────┐
│    func.tan(90)    │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```

## SQL 구문

```sql
TAN( <x> )
```

## SQL 예시

```sql
SELECT TAN(90);

┌────────────────────┐
│       tan(90)      │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```
