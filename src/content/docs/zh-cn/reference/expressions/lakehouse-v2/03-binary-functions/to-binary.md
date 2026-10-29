---
title: TO_BINARY (Lakehouse v2)
description: TO_BINARY：根据指定的二进制格式，将 VARCHAR 字符串转换为二进制值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/to-binary.md
---

根据指定的二进制格式，将 VARCHAR 字符串转换为二进制值。

## Analyze 语法

```python
func.to_binary(<str>, <format>)
```

## Analyze 示例

```python
func.to_binary('Hello', 'utf8')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQL 语法

```sql
TO_BINARY(<str>, <format>)
```

## SQL 示例

```sql
SELECT TO_BINARY('Hello', 'utf8');

┌────────────┐
│ 48656C6C6F  │
└────────────┘
```
