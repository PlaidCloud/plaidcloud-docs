---
title: CRC32（Lakehouse v1）
description: CRC32——返回 x 的 CRC32 校验和，其中 x 应为字符串（如有可能，非字符串也会按字符串处理）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/crc32.md
---

返回 `x` 的 CRC32 校验和，其中 'x' 应为字符串；如果不是字符串，则在可能的情况下将其按字符串处理。

## Analyze 语法

```python
func.crc32( '<x>' )
```

## Analyze 示例

```python
func.crc32('databend')

┌────────────────────────┐
│ func.crc32('databend') │
├────────────────────────┤
│             1177678456 │
└────────────────────────┘
```

## SQL 语法

```sql
CRC32( '<x>' )
```

## SQL 示例

```sql
SELECT CRC32('databend');

┌───────────────────┐
│ crc32('databend') │
├───────────────────┤
│        1177678456 │
└───────────────────┘
```
