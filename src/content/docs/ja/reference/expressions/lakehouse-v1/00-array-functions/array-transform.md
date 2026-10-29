---
title: ARRAY_TRANSFORM (Lakehouse v1)
description: ARRAY_TRANSFORM — 入力配列の各要素にラムダ関数を適用した結果の配列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-transform.md
---

入力配列の各要素にラムダ関数を適用した結果の配列を返します。

## Analyzeの構文

```python
func.array_transform( <array>, <lambda> )
```

## Analyzeの例

```python
func.array_transform([1, 2, 3], x -> (x + 1))

┌───────────────────────────────────────────────┐
│ func.array_transform([1, 2, 3], x -> (x + 1)) │
├───────────────────────────────────────────────┤
│ [2,3,4]                                       │
└───────────────────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_TRANSFORM( <array>, <lambda> )
```

## エイリアス

- [ARRAY_APPLY](../array-apply)

## SQLの例

```sql
SELECT ARRAY_TRANSFORM([1, 2, 3], x -> x + 1);

┌──────────────────────────────────────────┐
│ array_transform([1, 2, 3], x -> (x + 1)) │
├──────────────────────────────────────────┤
│ [2,3,4]                                  │
└──────────────────────────────────────────┘
```
