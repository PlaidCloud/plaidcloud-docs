---
title: XXHASH32（Lakehouse v1）
description: XXHASH32 — 文字列のxxHash32 32ビットハッシュ値を計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash32.md
---

文字列のxxHash32 32ビットハッシュ値を計算します。値はUInt32として返されます。引数がNULLの場合はNULLが返されます。

## Analyzeの構文

```python
func.xxhash32(<expr>)
```

## Analyzeの例

```python
func.xxhash32('1234567890')

┌─────────────────────────────┐
│ func.xxhash32('1234567890') │
├─────────────────────────────┤
│                  3896585587 │
└─────────────────────────────┘
```

## SQLの構文

```sql
XXHASH32(<expr>)
```

## SQLの例

```sql
SELECT XXHASH32('1234567890');

┌────────────────────────┐
│ xxhash32('1234567890') │
├────────────────────────┤
│             3896585587 │
└────────────────────────┘
```
