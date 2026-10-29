---
title: SQRT（Lakehouse v1）
description: SQRT — 非負の数 x の平方根を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sqrt.md
---

非負の数 `x` の平方根を返します。負の値が入力された場合は NaN を返します。

## Analyze 構文

```python
func.sqrt( <x> )
```

## Analyze の例

```python
func.sqrt(4)

┌──────────────┐
│ func.sqrt(4) │
├──────────────┤
│            2 │
└──────────────┘
```

## SQL 構文

```sql
SQRT( <x> )
```

## SQL の例

```sql
SELECT SQRT(4);

┌─────────┐
│ sqrt(4) │
├─────────┤
│       2 │
└─────────┘
```
