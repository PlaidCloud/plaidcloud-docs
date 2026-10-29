---
title: FROM_BINARY (Lakehouse v2)
description: FROM_BINARY：根据指定的二进制格式，将二进制值转换为 VARCHAR 字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/from-binary.md
---

根据指定的二进制格式，将二进制值转换为 VARCHAR 字符串。

## Analyze 语法

```python
func.from_binary(<binary>, <format>)
```

## Analyze 示例

```python
func.from_binary(b'\x48\x65\x6c\x6c\x6f', 'utf8')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL 语法

```sql
FROM_BINARY(<binary>, <format>)
```

## SQL 示例

```sql
SELECT FROM_BINARY(X'48656C6C6F', 'utf8');

┌───────┐
│ Hello  │
└───────┘
```
