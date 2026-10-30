---
title: TANH (Lakehouse v2)
description: TANH — 数値の双曲線正接を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tanh.md
---

数値の双曲線正接を返します。

## Analyzeの構文

```python
func.tanh(<x>)
```

## Analyzeの例

```python
func.tanh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQLの構文

```sql
TANH(<x>)
```

## SQLの例

```sql
SELECT TANH(0);

┌─────┐
│ 0.0  │
└─────┘
```
