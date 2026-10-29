---
title: TRUNCATE（Lakehouse v1）
description: TRUNCATE — 数値 x を小数点以下 d 桁に切り捨てて返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/truncate.md
---

数値 `x` を小数点以下 `d` 桁に切り捨てて返します。`d` が 0 の場合、結果には小数点も小数部もありません。`d` に負の値を指定すると、値 `x` の小数点より左の `d` 桁が 0 になります。`d` の絶対値の最大は 30 で、30（または -30）を超える桁は切り捨てられます。

## Analyze 構文

```python
func.truncate( <x, d> )
```

## Analyze の例

```python
func.truncate(1.223, 1)

┌─────────────────────────┐
│ func.truncate(1.223, 1) │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQL 構文

```sql
TRUNCATE( <x, d> )
```

## SQL の例

```sql
SELECT TRUNCATE(1.223, 1);

┌────────────────────┐
│ truncate(1.223, 1) │
├────────────────────┤
│ 1.2                │
└────────────────────┘
```
