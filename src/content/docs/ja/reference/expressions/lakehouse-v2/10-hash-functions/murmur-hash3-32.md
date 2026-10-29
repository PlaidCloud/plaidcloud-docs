---
title: MURMUR_HASH3_32 (Lakehouse v2)
description: MURMUR_HASH3_32 — 値の32ビットMurmurHash3ハッシュを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/murmur-hash3-32.md
---

値の32ビットMurmurHash3ハッシュを返します。

## Analyzeの構文

```python
func.murmur_hash3_32(<expr>[, ...])
```

## Analyzeの例

```python
func.murmur_hash3_32('hello')

┌───────────┐
│ 613153351  │
└───────────┘
```

## SQLの構文

```sql
MURMUR_HASH3_32(<expr>[, ...])
```

## SQLの例

```sql
SELECT MURMUR_HASH3_32('hello');

┌───────────┐
│ 613153351  │
└───────────┘
```
