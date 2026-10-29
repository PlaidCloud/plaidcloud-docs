---
title: ROUND（Lakehouse v1）
description: ROUND — 引数 x を小数点以下 d 桁に丸めます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/round.md
---

引数 x を小数点以下 d 桁に丸めます。丸めのアルゴリズムは x のデータ型によって異なります。d を指定しない場合のデフォルトは 0 です。d に負の値を指定すると、x の値の小数点より左の d 桁が 0 になります。d の絶対値の最大は 30 で、30（または -30）を超える桁は切り捨てられます。

この関数の結果を計算に使用する場合は、戻り値のデータ型が DOUBLE であるため、最終的な精度に影響する可能性がある精度の問題にご注意ください。

```sql
SELECT ROUND(4/7, 4) - ROUND(3/7, 4); -- Result: 0.14280000000000004
SELECT ROUND(4/7, 4)::DECIMAL(8,4) - ROUND(3/7, 4)::DECIMAL(8,4); -- Result: 0.1428
```

## Analyze 構文

```python
func.round( <x, d> )
```

## Analyze の例

```python
func.round(0.123, 2)

┌──────────────────────┐
│ func.round(0.123, 2) │
├──────────────────────┤
│                 0.12 │
└──────────────────────┘
```

## SQL 構文

```sql
ROUND( <x, d> )
```

## SQL の例

```sql
SELECT ROUND(0.123, 2);

┌─────────────────┐
│ round(0.123, 2) │
├─────────────────┤
│ 0.12            │
└─────────────────┘
```
