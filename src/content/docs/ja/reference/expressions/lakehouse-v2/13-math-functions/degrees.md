---
title: DEGREES (Lakehouse v2)
description: DEGREES — ラジアンを度に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/degrees.md
---

ラジアンを度に変換します。

## Analyzeの構文

```python
func.degrees(<x>)
```

## Analyzeの例

```python
func.degrees(3.141592653589793)

┌───────┐
│ 180.0  │
└───────┘
```

## SQLの構文

```sql
DEGREES(<x>)
```

## SQLの例

```sql
SELECT DEGREES(PI());

┌───────┐
│ 180.0  │
└───────┘
```
