---
title: RAND(n)（Lakehouse v1）
description: RAND(n) — 0 &lt;= v &lt; 1.0 の範囲のランダムな浮動小数点値 v を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/randn.md
---

0 &lt;= v &lt; 1.0 の範囲のランダムな浮動小数点値 v を返します。i &lt;= R &lt; j の範囲のランダムな整数 R を取得するには、式 FLOOR(i + RAND() * (j − i)) を使用します。引数 `n` はシード値として使用されます。引数の値が同じであれば、RAND(n) は毎回同じ値を返すため、再現可能な列値のシーケンスを生成できます。

## Analyze 構文

```python
func.rand( <n>)
```

## Analyze の例

```python
func.rand(1)

┌────────────────────┐
│    func.rand(1)    │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```

## SQL 構文

```sql
RAND( <n>)
```

## SQL の例

```sql
SELECT RAND(1);

┌────────────────────┐
│       rand(1)      │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```
