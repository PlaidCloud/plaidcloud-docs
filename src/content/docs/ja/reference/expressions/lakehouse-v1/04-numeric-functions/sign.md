---
title: SIGN（Lakehouse v1）
description: SIGN — x が負の数かどうかに応じて、引数の符号を -1、0、1 で返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sign.md
---

`x` が負、ゼロ、正のいずれであるかに応じて、引数の符号を -1、0、1 で返します。引数が NULL の場合は NULL を返します。

## Analyze 構文

```python
func.sign( <x> )
```

## Analyze の例

```python
func.sign(0)

┌──────────────┐
│ func.sign(0) │
├──────────────┤
│            0 │
└──────────────┘
```

## SQL 構文

```sql
SIGN( <x> )
```

## SQL の例

```sql
SELECT SIGN(0);

┌─────────┐
│ sign(0) │
├─────────┤
│       0 │
└─────────┘
```
