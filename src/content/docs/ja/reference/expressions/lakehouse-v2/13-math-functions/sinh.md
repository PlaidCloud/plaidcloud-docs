---
title: SINH (Lakehouse v2)
description: SINH — 数値の双曲線正弦を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sinh.md
---

数値の双曲線正弦を返します。

## Analyzeの構文

```python
func.sinh(<x>)
```

## Analyzeの例

```python
func.sinh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQLの構文

```sql
SINH(<x>)
```

## SQLの例

```sql
SELECT SINH(0);

┌─────┐
│ 0.0  │
└─────┘
```
