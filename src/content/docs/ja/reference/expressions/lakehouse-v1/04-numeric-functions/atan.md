---
title: ATAN（Lakehouse v1）
description: ATAN — x のアークタンジェント、つまりタンジェントが x になる値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan.md
---

`x` のアークタンジェント、つまりタンジェントが `x` になる値を返します。

## Analyze 構文

```python
func.atan( <x> )
```

## Analyze の例

```python
func.atan(-2)

┌─────────────────────┐
│  func.atan((- 2))   │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```

## SQL 構文

```sql
ATAN( <x> )
```

## SQL の例

```sql
SELECT ATAN(-2);

┌─────────────────────┐
│     atan((- 2))     │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```
