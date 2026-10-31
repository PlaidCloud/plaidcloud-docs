---
title: MONEY_FORMAT (Lakehouse v2)
description: MONEY_FORMAT：将数字格式化为带千位逗号和两位小数的货币字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/money-format.md
---

将数字格式化为带千位逗号和两位小数的货币字符串。

## Analyze 语法

```python
func.money_format(<num>)
```

## Analyze 示例

```python
func.money_format(1234567.89)

┌────────────────┐
│ '1,234,567.89'  │
└────────────────┘
```

## SQL 语法

```sql
MONEY_FORMAT(<num>)
```

## SQL 示例

```sql
SELECT MONEY_FORMAT(1234567.89);

┌──────────────┐
│ 1,234,567.89  │
└──────────────┘
```
