---
title: HEX_DECODE_BINARY (Lakehouse v2)
description: HEX_DECODE_BINARY — 16진수 문자열을 바이너리 값으로 디코딩합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-binary.md
---

16진수 문자열을 바이너리 값으로 디코딩합니다.

## Analyze 구문

```python
func.hex_decode_binary(<hex_str>)
```

## Analyze 예제

```python
func.hex_decode_binary('48656C6C6F')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQL 구문

```sql
HEX_DECODE_BINARY(<hex_str>)
```

## SQL 예제

```sql
SELECT HEX_DECODE_BINARY('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
