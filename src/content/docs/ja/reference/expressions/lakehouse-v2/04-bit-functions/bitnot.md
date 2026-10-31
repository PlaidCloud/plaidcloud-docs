---
title: BITNOT (Lakehouse v2)
description: BITNOT — 数値のビット単位の NOT を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitnot.md
---

数値のビット単位の NOT を返します。

## Analyzeの構文

```python
func.bitnot(<x>)
```

## Analyzeの例

```python
func.bitnot(0)

┌──────┐
│ '-1'  │
└──────┘
```

## SQLの構文

```sql
BITNOT(<x>)
```

## SQLの例

```sql
SELECT BITNOT(0);

┌────┐
│ -1  │
└────┘
```
