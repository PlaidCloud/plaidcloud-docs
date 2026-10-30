---
title: CRC32（Lakehouse v1）
description: CRC32 — x の CRC32 チェックサムを返します。x は文字列であることが想定され、可能であれば文字列以外の値も文字列として扱われます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/crc32.md
---

`x` の CRC32 チェックサムを返します。'x' は文字列であることが想定され、文字列でない場合は（可能であれば）文字列として扱われます。

## Analyze 構文

```python
func.crc32( '<x>' )
```

## Analyze の例

```python
func.crc32('databend')

┌────────────────────────┐
│ func.crc32('databend') │
├────────────────────────┤
│             1177678456 │
└────────────────────────┘
```

## SQL 構文

```sql
CRC32( '<x>' )
```

## SQL の例

```sql
SELECT CRC32('databend');

┌───────────────────┐
│ crc32('databend') │
├───────────────────┤
│        1177678456 │
└───────────────────┘
```
