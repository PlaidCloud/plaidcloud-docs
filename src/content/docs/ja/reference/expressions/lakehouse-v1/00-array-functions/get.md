---
title: "GET（配列、Lakehouse v1）"
description: GET — インデックス（1から始まる）を指定して、配列から要素を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/get.md
---

インデックス（1から始まる）を指定して、配列から要素を返します。

## Analyzeの構文

```python
func.get( <array>, <index> )
```

## Analyzeの例

```python
func.get([1, 2], 2)

┌─────────────────────┐
│ func.get([1, 2], 2) │
├─────────────────────┤
│                   2 │
└─────────────────────┘
```

## SQLの構文

```sql
GET( <array>, <index> )
```

## エイリアス

- [ARRAY_GET](../array-get)

## SQLの例

```sql
SELECT GET([1, 2], 2), ARRAY_GET([1, 2], 2);

┌───────────────────────────────────────┐
│ get([1, 2], 2) │ array_get([1, 2], 2) │
├────────────────┼──────────────────────┤
│              2 │                    2 │
└───────────────────────────────────────┘
```
