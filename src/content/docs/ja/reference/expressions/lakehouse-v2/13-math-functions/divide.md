---
title: DIVIDE (Lakehouse v2)
description: DIVIDE — ある数値を別の数値で割った結果を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/divide.md
---

ある数値を別の数値で割った結果を返します。

## Analyzeの構文

```python
func.divide(<x>, <y>)
```

## Analyzeの例

```python
func.divide(10, 3)

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```

## SQLの構文

```sql
DIVIDE(<x>, <y>)
```

## SQLの例

```sql
SELECT DIVIDE(10, 3);

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```
