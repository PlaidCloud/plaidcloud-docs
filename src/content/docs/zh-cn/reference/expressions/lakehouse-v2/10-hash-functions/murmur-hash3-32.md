---
title: MURMUR_HASH3_32 (Lakehouse v2)
description: MURMUR_HASH3_32 — 返回值的 32 位 MurmurHash3 哈希。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/murmur-hash3-32.md
---

返回值的 32 位 MurmurHash3 哈希。

## Analyze 语法

```python
func.murmur_hash3_32(<expr>[, ...])
```

## Analyze 示例

```python
func.murmur_hash3_32('hello')

┌───────────┐
│ 613153351  │
└───────────┘
```

## SQL 语法

```sql
MURMUR_HASH3_32(<expr>[, ...])
```

## SQL 示例

```sql
SELECT MURMUR_HASH3_32('hello');

┌───────────┐
│ 613153351  │
└───────────┘
```
