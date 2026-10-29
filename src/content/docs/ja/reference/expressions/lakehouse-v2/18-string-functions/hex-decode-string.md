---
title: HEX_DECODE_STRING（Lakehouse v2）
description: HEX_DECODE_STRING — 16進数文字列をVARCHAR文字列にデコードします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-string.md
---

16進数文字列をVARCHAR文字列にデコードします。

## Analyze 構文

```python
func.hex_decode_string(<hex_str>)
```

## Analyze の例

```python
func.hex_decode_string('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL 構文

```sql
HEX_DECODE_STRING(<hex_str>)
```

## SQL の例

```sql
SELECT HEX_DECODE_STRING('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
