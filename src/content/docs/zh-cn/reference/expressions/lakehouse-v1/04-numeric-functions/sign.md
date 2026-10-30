---
title: SIGN（Lakehouse v1）
description: SIGN——根据 x 为负、零还是正，以 -1、0 或 1 返回参数的符号。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sign.md
---

根据 `x` 为负、零还是正，以 -1、0 或 1 返回参数的符号；如果参数为 NULL，则返回 NULL。

## Analyze 语法

```python
func.sign( <x> )
```

## Analyze 示例

```python
func.sign(0)

┌──────────────┐
│ func.sign(0) │
├──────────────┤
│            0 │
└──────────────┘
```

## SQL 语法

```sql
SIGN( <x> )
```

## SQL 示例

```sql
SELECT SIGN(0);

┌─────────┐
│ sign(0) │
├─────────┤
│       0 │
└─────────┘
```
