---
title: CONTAINS (Lakehouse v1)
description: CONTAINS — 配列に特定の要素が含まれているかどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/contains.md
---

配列に特定の要素が含まれているかどうかを確認します。


## Analyzeの構文

```python
func.contains( <array>, <element> )
```

## Analyzeの例

```python
func.contains([1, 2], 1)

┌───────────────────────────┐
│ func.contains([1, 2], 1)  │
├───────────────────────────┤
│ true                      │
└───────────────────────────┘
```

## SQLの構文

```sql
CONTAINS( <array>, <element> )
```

## エイリアス

- [ARRAY_CONTAINS](../array-contains)

## SQLの例

```sql
SELECT ARRAY_CONTAINS([1, 2], 1), CONTAINS([1, 2], 1);

┌─────────────────────────────────────────────────┐
│ array_contains([1, 2], 1) │ contains([1, 2], 1) │
├───────────────────────────┼─────────────────────┤
│ true                      │ true                │
└─────────────────────────────────────────────────┘
```
