---
title: CRC32（Lakehouse v2）
description: CRC32 — 文字列のCRC-32チェックサムを符号なし整数で返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/crc32.md
---

文字列のCRC-32チェックサムを符号なし整数で返します。

## Analyze 構文

```python
func.crc32(<str>)
```

## Analyze の例

```python
func.crc32('hello')

┌───────────┐
│ 907060870  │
└───────────┘
```

## SQL 構文

```sql
CRC32(<str>)
```

## SQL の例

```sql
SELECT CRC32('hello');

┌───────────┐
│ 907060870  │
└───────────┘
```
