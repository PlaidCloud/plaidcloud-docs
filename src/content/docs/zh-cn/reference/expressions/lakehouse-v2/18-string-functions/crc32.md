---
title: CRC32 (Lakehouse v2)
description: CRC32：以无符号整数形式返回字符串的 CRC-32 校验和。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/crc32.md
---

以无符号整数形式返回字符串的 CRC-32 校验和。

## Analyze 语法

```python
func.crc32(<str>)
```

## Analyze 示例

```python
func.crc32('hello')

┌───────────┐
│ 907060870  │
└───────────┘
```

## SQL 语法

```sql
CRC32(<str>)
```

## SQL 示例

```sql
SELECT CRC32('hello');

┌───────────┐
│ 907060870  │
└───────────┘
```
