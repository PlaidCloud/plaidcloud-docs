---
title: CBRT（Lakehouse v1）
description: CBRT — 非負の数 x の立方根を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cbrt.md
---

非負の数 `x` の立方根を返します。

## Analyze 構文

```python
func.cbrt( <x> )
```

## Analyze の例

```python
func.cbrt(27)

┌───────────────┐
│ func.cbrt(27) │
├───────────────┤
│             3 │
└───────────────┘
```

## SQL 構文

```sql
CBRT( <x> )
```

## SQL の例

```sql
SELECT CBRT(27);

┌──────────┐
│ cbrt(27) │
├──────────┤
│        3 │
└──────────┘
```
