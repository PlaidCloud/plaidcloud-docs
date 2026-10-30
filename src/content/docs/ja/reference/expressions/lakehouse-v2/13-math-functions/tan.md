---
title: TAN (Lakehouse v2)
description: TAN — ラジアンで指定した数値の正接を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tan.md
---

ラジアンで指定した数値の正接を返します。

## Analyzeの構文

```python
func.tan(<x>)
```

## Analyzeの例

```python
func.tan(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQLの構文

```sql
TAN(<x>)
```

## SQLの例

```sql
SELECT TAN(0);

┌─────┐
│ 0.0  │
└─────┘
```
