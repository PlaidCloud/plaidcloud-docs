---
title: PI（Lakehouse v1）
description: PI — π の値を浮動小数点数として返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pi.md
---

π の値を浮動小数点数として返します。

## Analyze 構文

```python
func.pi()
```

## Analyze の例

```python
func.pi()

┌───────────────────┐
│     func.pi()     │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```

## SQL 構文

```sql
PI()
```

## SQL の例

```sql
SELECT PI();

┌───────────────────┐
│        pi()       │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```
