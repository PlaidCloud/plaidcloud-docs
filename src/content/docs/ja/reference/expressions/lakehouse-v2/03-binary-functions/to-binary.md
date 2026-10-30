---
title: TO_BINARY (Lakehouse v2)
description: TO_BINARY — 指定したバイナリ形式に基づいて、VARCHAR 文字列をバイナリ値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/to-binary.md
---

指定したバイナリ形式に基づいて、VARCHAR 文字列をバイナリ値に変換します。

## Analyzeの構文

```python
func.to_binary(<str>, <format>)
```

## Analyzeの例

```python
func.to_binary('Hello', 'utf8')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQLの構文

```sql
TO_BINARY(<str>, <format>)
```

## SQLの例

```sql
SELECT TO_BINARY('Hello', 'utf8');

┌────────────┐
│ 48656C6C6F  │
└────────────┘
```
