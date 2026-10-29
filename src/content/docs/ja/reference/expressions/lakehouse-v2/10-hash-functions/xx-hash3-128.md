---
title: XX_HASH3_128 (Lakehouse v2)
description: XX_HASH3_128 — 値の128ビットxxHash3ハッシュを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-128.md
---

値の128ビットxxHash3ハッシュを返します。

## Analyzeの構文

```python
func.xx_hash3_128(<expr>[, ...])
```

## Analyzeの例

```python
func.xx_hash3_128('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQLの構文

```sql
XX_HASH3_128(<expr>[, ...])
```

## SQLの例

```sql
SELECT XX_HASH3_128('hello');

┌──────────────────────┐
│ (128-bit hash value)  │
└──────────────────────┘
```
