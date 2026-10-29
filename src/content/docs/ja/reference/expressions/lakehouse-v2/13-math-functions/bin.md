---
title: BIN (Lakehouse v2)
description: BIN — 整数の2進数文字列表現を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/bin.md
---

整数の2進数文字列表現を返します。

## Analyzeの構文

```python
func.bin(<x>)
```

## Analyzeの例

```python
func.bin(10)

┌────────┐
│ '1010'  │
└────────┘
```

## SQLの構文

```sql
BIN(<x>)
```

## SQLの例

```sql
SELECT BIN(10);

┌──────┐
│ 1010  │
└──────┘
```
