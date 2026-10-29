---
title: XXHASH64（Lakehouse v1）
description: XXHASH64 — 文字列のxxHash64 64ビットハッシュ値を計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash64.md
---

文字列のxxHash64 64ビットハッシュ値を計算します。値はUInt64として返されます。引数がNULLの場合はNULLが返されます。

## Analyzeの構文

```python
func.xxhash64(<expr>)
```

## Analyzeの例

```python
func.xxhash64('1234567890')

┌─────────────────────────────┐
│ func.xxhash64('1234567890') │
├─────────────────────────────┤
│        12237639266330420150 │
└─────────────────────────────┘
```

## SQLの構文

```sql
XXHASH64(<expr>)
```

## SQLの例

```sql
SELECT XXHASH64('1234567890');

┌────────────────────────┐
│ xxhash64('1234567890') │
├────────────────────────┤
│   12237639266330420150 │
└────────────────────────┘
```
