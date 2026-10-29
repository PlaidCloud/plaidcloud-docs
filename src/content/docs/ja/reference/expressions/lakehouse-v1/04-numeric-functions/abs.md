---
title: ABS（Lakehouse v1）
description: ABS — x の絶対値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/abs.md
---

`x` の絶対値を返します。

## Analyze 構文

```python
func.abs( <x> )
```

## Analyze の例

```python
func.abs((- 5))

┌─────────────────┐
│ func.abs((- 5)) │
├─────────────────┤
│               5 │
└─────────────────┘
```

## SQL 構文

```sql
ABS( <x> )
```

## SQL の例

```sql
SELECT ABS(-5);

┌────────────┐
│ abs((- 5)) │
├────────────┤
│          5 │
└────────────┘
```
