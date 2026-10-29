---
title: MODULO（Lakehouse v1）
description: MODULO — x を y で割った余りを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/modulo.md
---

`x` を `y` で割った余りを返します。`y` が 0 の場合はエラーを返します。

## Analyze 構文

```python
func.modulo( <x>, <y> )
```

## Analyze の例

```python
func.modulo(9, 2)

┌───────────────────┐
│ func.modulo(9, 2) │
├───────────────────┤
│                 1 │
└───────────────────┘
```

## SQL 構文

```sql
MODULO( <x>, <y> )
```

## エイリアス

- [MOD](../mod)

## SQL の例

```sql
SELECT MOD(9, 2), MODULO(9, 2);

┌──────────────────────────┐
│ mod(9, 2) │ modulo(9, 2) │
├───────────┼──────────────┤
│         1 │            1 │
└──────────────────────────┘
```
