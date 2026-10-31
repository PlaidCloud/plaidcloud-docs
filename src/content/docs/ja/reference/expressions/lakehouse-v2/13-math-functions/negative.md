---
title: NEGATIVE (Lakehouse v2)
description: NEGATIVE — 数値の符号を反転した値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/negative.md
---

数値の符号を反転した値を返します。

## Analyzeの構文

```python
func.negative(<x>)
```

## Analyzeの例

```python
func.negative(5)

┌────┐
│ -5  │
└────┘
```

## SQLの構文

```sql
NEGATIVE(<x>)
```

## SQLの例

```sql
SELECT NEGATIVE(5);

┌────┐
│ -5  │
└────┘
```
