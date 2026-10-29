---
title: POW（Lakehouse v1）
description: POW — x の y 乗の値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pow.md
---

`x` の `y` 乗の値を返します。 

## Analyze 構文

```python
func.pow( <x, y> )
```

## Analyze の例

```python
func.pow(-2, 2)

┌────────────────────┐
│ func.pow((- 2), 2) │
├────────────────────┤
│                  4 │ 
└────────────────────┘
```

## SQL 構文

```sql
POW( <x, y> )
```

## エイリアス

- [POWER](../power)

## SQL の例

```sql
SELECT POW(-2, 2), POWER(-2, 2);

┌─────────────────────────────────┐
│ pow((- 2), 2) │ power((- 2), 2) │
├───────────────┼─────────────────┤
│             4 │               4 │
└─────────────────────────────────┘
```
