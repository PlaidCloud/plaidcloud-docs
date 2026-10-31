---
title: "ELEMENT_AT (配列, Lakehouse v2)"
description: ELEMENT_AT — 配列の指定した位置にある要素を返します（1 始まり）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/element-at.md
---

配列の指定した位置にある要素を返します（1 始まり）。

## Analyzeの構文

```python
func.element_at([10, 20, 30], 2)
```

## Analyzeの例

```python
func.element_at([10, 20, 30], 2)

┌────┐
│ 20 │
└────┘
```

## SQLの構文

```sql
ELEMENT_AT([10, 20, 30], 2)
```

## SQLの例

```sql
SELECT ELEMENT_AT([10, 20, 30], 2);

┌────┐
│ 20 │
└────┘
```
