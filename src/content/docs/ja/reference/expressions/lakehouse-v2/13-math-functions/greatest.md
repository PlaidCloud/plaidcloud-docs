---
title: GREATEST (Lakehouse v2)
description: GREATEST — 値のリストから最大の値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/greatest.md
---

値のリストから最大の値を返します。

## Analyzeの構文

```python
func.greatest(<val1>, <val2>[, ...])
```

## Analyzeの例

```python
func.greatest(3, 7, 1, 9, 4)

┌───┐
│ 9  │
└───┘
```

## SQLの構文

```sql
GREATEST(<val1>, <val2>[, ...])
```

## SQLの例

```sql
SELECT GREATEST(3, 7, 1, 9, 4);

┌───┐
│ 9  │
└───┘
```
