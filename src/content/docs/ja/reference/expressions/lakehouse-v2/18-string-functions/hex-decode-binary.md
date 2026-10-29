---
title: HEX_DECODE_BINARY（Lakehouse v2）
description: HEX_DECODE_BINARY — 16進数文字列をバイナリ値にデコードします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-binary.md
---

16進数文字列をバイナリ値にデコードします。

## Analyze 構文

```python
func.hex_decode_binary(<hex_str>)
```

## Analyze の例

```python
func.hex_decode_binary('48656C6C6F')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQL 構文

```sql
HEX_DECODE_BINARY(<hex_str>)
```

## SQL の例

```sql
SELECT HEX_DECODE_BINARY('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
