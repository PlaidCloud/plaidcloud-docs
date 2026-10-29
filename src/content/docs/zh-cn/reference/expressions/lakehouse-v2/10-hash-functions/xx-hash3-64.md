---
title: XX_HASH3_64 (Lakehouse v2)
description: XX_HASH3_64 — 返回值的 64 位 xxHash3 哈希。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-64.md
---

返回值的 64 位 xxHash3 哈希。

## Analyze 语法

```python
func.xx_hash3_64(<expr>[, ...])
```

## Analyze 示例

```python
func.xx_hash3_64('hello')

┌──────────┐
│ (bigint)  │
└──────────┘
```

## SQL 语法

```sql
XX_HASH3_64(<expr>[, ...])
```

## SQL 示例

```sql
SELECT XX_HASH3_64('hello');

┌──────────────────────┐
│ -7685981735718036227  │
└──────────────────────┘
```
