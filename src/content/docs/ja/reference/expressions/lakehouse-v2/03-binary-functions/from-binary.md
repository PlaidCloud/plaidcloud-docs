---
title: FROM_BINARY (Lakehouse v2)
description: FROM_BINARY — 指定したバイナリ形式に基づいて、バイナリ値を VARCHAR 文字列に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/from-binary.md
---

指定したバイナリ形式に基づいて、バイナリ値を VARCHAR 文字列に変換します。

## Analyzeの構文

```python
func.from_binary(<binary>, <format>)
```

## Analyzeの例

```python
func.from_binary(b'\x48\x65\x6c\x6c\x6f', 'utf8')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQLの構文

```sql
FROM_BINARY(<binary>, <format>)
```

## SQLの例

```sql
SELECT FROM_BINARY(X'48656C6C6F', 'utf8');

┌───────┐
│ Hello  │
└───────┘
```
