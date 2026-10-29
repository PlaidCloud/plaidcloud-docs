---
title: BIN (Lakehouse v2)
description: BIN — 返回整数的二进制字符串表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/bin.md
---

返回整数的二进制字符串表示。

## Analyze 语法

```python
func.bin(<x>)
```

## Analyze 示例

```python
func.bin(10)

┌────────┐
│ '1010'  │
└────────┘
```

## SQL 语法

```sql
BIN(<x>)
```

## SQL 示例

```sql
SELECT BIN(10);

┌──────┐
│ 1010  │
└──────┘
```
