---
title: SM3 (Lakehouse v2)
description: SM3：返回字符串的 SM3 哈希。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sm3.md
---

返回字符串的 SM3 哈希。

## Analyze 语法

```python
func.sm3(<str>)
```

## Analyze 示例

```python
func.sm3('hello')

┌───────────────┐
│ 'becbbfaa...'  │
└───────────────┘
```

## SQL 语法

```sql
SM3(<str>)
```

## SQL 示例

```sql
SELECT SM3('hello');

┌──────────────────────────────────────────────────────────────────┐
│ becbbfaae6548b8bf0cfcad5a27183cd1be6093b1cceccc303d9c61d0a645268  │
└──────────────────────────────────────────────────────────────────┘
```
