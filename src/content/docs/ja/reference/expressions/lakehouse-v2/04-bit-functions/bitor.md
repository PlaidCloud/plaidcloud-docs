---
title: BITOR (Lakehouse v2)
description: BITOR — 2 つの数値のビット単位の OR を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitor.md
---

2 つの数値のビット単位の OR を返します。

## Analyzeの構文

```python
func.bitor(<x>, <y>)
```

## Analyzeの例

```python
func.bitor(12, 10)

┌────┐
│ 14  │
└────┘
```

## SQLの構文

```sql
BITOR(<x>, <y>)
```

## SQLの例

```sql
SELECT BITOR(12, 10);

┌────┐
│ 14  │
└────┘
```
