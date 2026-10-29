---
title: SIN (Lakehouse v2)
description: SIN — ラジアンで指定した数値の正弦を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sin.md
---

ラジアンで指定した数値の正弦を返します。

## Analyzeの構文

```python
func.sin(<x>)
```

## Analyzeの例

```python
func.sin(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQLの構文

```sql
SIN(<x>)
```

## SQLの例

```sql
SELECT SIN(0);

┌─────┐
│ 0.0  │
└─────┘
```
