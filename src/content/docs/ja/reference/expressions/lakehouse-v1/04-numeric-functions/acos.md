---
title: ACOS（Lakehouse v1）
description: ACOS — x のアークコサイン、つまりコサインが x になる値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/acos.md
---

`x` のアークコサイン、つまりコサインが `x` になる値を返します。`x` が -1 から 1 の範囲外の場合は NULL を返します。

## Analyze 構文

```python
func.abs( <x> )
```

## Analyze の例

```python
func.abs(1)

┌──────────────┐
│ func.acos(1) │
├──────────────┤
│            0 │
└──────────────┘
```

## SQL 構文

```sql
ACOS( <x> )
```

## SQL の例

```sql
SELECT ACOS(1);

┌─────────┐
│ acos(1) │
├─────────┤
│       0 │
└─────────┘
```
