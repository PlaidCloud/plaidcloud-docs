---
title: SHA2 (Lakehouse v2)
description: SHA2 — 指定したビット長（224、256、384、512）で、文字列の SHA-2 ハッシュを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sha2.md
---

指定したビット長（224、256、384、512）で、文字列の SHA-2 ハッシュを返します。

## Analyzeの構文

```python
func.sha2(<str>, <bit_length>)
```

## Analyzeの例

```python
func.sha2('hello', 256)

┌───────────────┐
│ '2cf24dba...'  │
└───────────────┘
```

## SQLの構文

```sql
SHA2(<str>, <bit_length>)
```

## SQLの例

```sql
SELECT SHA2('hello', 256);

┌──────────────────────────────────────────────────────────────────┐
│ 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824  │
└──────────────────────────────────────────────────────────────────┘
```
