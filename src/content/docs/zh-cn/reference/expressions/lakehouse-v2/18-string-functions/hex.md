---
title: HEX (Lakehouse v2)
description: HEX：返回字符串或数字的十六进制表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex.md
---

返回字符串或数字的十六进制表示。

## Analyze 语法

```python
func.hex(<expr>)
```

## Analyze 示例

```python
func.hex(255)

┌──────┐
│ 'FF'  │
└──────┘
```

## SQL 语法

```sql
HEX(<expr>)
```

## SQL 示例

```sql
SELECT HEX(255);

┌────┐
│ FF  │
└────┘
```
