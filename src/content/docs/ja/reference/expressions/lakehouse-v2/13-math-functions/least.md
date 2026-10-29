---
title: LEAST (Lakehouse v2)
description: LEAST — 値のリストから最小の値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/least.md
---

値のリストから最小の値を返します。

## Analyzeの構文

```python
func.least(<val1>, <val2>[, ...])
```

## Analyzeの例

```python
func.least(3, 7, 1, 9, 4)

┌───┐
│ 1  │
└───┘
```

## SQLの構文

```sql
LEAST(<val1>, <val2>[, ...])
```

## SQLの例

```sql
SELECT LEAST(3, 7, 1, 9, 4);

┌───┐
│ 1  │
└───┘
```
