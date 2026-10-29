---
title: CONV (Lakehouse v2)
description: CONV — 数値をある基数から別の基数に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/conv.md
---

数値をある基数から別の基数に変換します。

## Analyzeの構文

```python
func.conv(<num>, <from_base>, <to_base>)
```

## Analyzeの例

```python
func.conv('ff', 16, 10)

┌───────┐
│ '255'  │
└───────┘
```

## SQLの構文

```sql
CONV(<num>, <from_base>, <to_base>)
```

## SQLの例

```sql
SELECT CONV('ff', 16, 10);

┌─────┐
│ 255  │
└─────┘
```
