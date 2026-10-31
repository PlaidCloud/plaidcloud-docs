---
title: ATAN (Lakehouse v2)
description: ATAN — 数値の逆正接をラジアンで返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan.md
---

数値の逆正接をラジアンで返します。

## Analyzeの構文

```python
func.atan(<x>)
```

## Analyzeの例

```python
func.atan(1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## SQLの構文

```sql
ATAN(<x>)
```

## SQLの例

```sql
SELECT ATAN(1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
