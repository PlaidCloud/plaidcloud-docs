---
title: SIGN (Lakehouse v2)
description: "SIGN — 数値の符号（-1、0、1のいずれか）を返します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sign.md
---

数値の符号（-1、0、1のいずれか）を返します。

## Analyzeの構文

```python
func.sign(<x>)
```

## Analyzeの例

```python
func.sign(-42)

┌────┐
│ -1  │
└────┘
```

## SQLの構文

```sql
SIGN(<x>)
```

## SQLの例

```sql
SELECT SIGN(-42);

┌────┐
│ -1  │
└────┘
```
