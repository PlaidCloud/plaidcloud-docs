---
title: TRUNCATE (Lakehouse v2)
description: TRUNCATE — 数値を指定した小数桁数で切り捨てます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/truncate.md
---

数値を指定した小数桁数で切り捨てます。

## Analyzeの構文

```python
func.truncate(<x>, <d>)
```

## Analyzeの例

```python
func.truncate(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## SQLの構文

```sql
TRUNCATE(<x>, <d>)
```

## SQLの例

```sql
SELECT TRUNCATE(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
