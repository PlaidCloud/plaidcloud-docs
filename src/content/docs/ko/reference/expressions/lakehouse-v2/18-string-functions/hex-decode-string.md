---
title: HEX_DECODE_STRING (Lakehouse v2)
description: HEX_DECODE_STRING — 16진수 문자열을 VARCHAR 문자열로 디코딩합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-string.md
---

16진수 문자열을 VARCHAR 문자열로 디코딩합니다.

## Analyze 구문

```python
func.hex_decode_string(<hex_str>)
```

## Analyze 예제

```python
func.hex_decode_string('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL 구문

```sql
HEX_DECODE_STRING(<hex_str>)
```

## SQL 예제

```sql
SELECT HEX_DECODE_STRING('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
