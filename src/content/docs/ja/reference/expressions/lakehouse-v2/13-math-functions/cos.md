---
title: COS (Lakehouse v2)
description: COS — ラジアンで指定した数値の余弦を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cos.md
---

ラジアンで指定した数値の余弦を返します。

## Analyzeの構文

```python
func.cos(<x>)
```

## Analyzeの例

```python
func.cos(0)

┌─────┐
│ 1.0  │
└─────┘
```

## SQLの構文

```sql
COS(<x>)
```

## SQLの例

```sql
SELECT COS(0);

┌─────┐
│ 1.0  │
└─────┘
```
