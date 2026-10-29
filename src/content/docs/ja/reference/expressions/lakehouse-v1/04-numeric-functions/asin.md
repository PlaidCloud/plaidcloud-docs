---
title: ASIN（Lakehouse v1）
description: ASIN — x のアークサイン、つまりサインが x になる値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/asin.md
---

`x` のアークサイン、つまりサインが `x` になる値を返します。`x` が -1 から 1 の範囲外の場合は NULL を返します。

## Analyze 構文

```python
func.asin( <x> )
```

## Analyze の例

```python
func.asin(0.2)

┌────────────────────┐
│   func.asin(0.2)   │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```

## SQL 構文

```sql
ASIN( <x> )
```

## SQL の例

```sql
SELECT ASIN(0.2);

┌────────────────────┐
│      asin(0.2)     │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```
