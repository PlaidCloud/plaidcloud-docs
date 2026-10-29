---
title: POW (Lakehouse v2)
description: POW — ある数値を別の数値でべき乗した値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pow.md
---

ある数値を別の数値でべき乗した値を返します。

## Analyzeの構文

```python
func.pow(<x>, <y>)
```

## Analyzeの例

```python
func.pow(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## SQLの構文

```sql
POW(<x>, <y>)
```

## SQLの例

```sql
SELECT POW(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
