---
title: TRIM_BOTH（Lakehouse v1）
description: TRIM_BOTH——从字符串的开头、结尾或两端移除所有出现的指定修剪字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-both.md
---

从字符串的开头、结尾或两端移除所有出现的指定修剪字符串。

另请参阅：[TRIM](../trim)

## Analyze 语法

```python
func.trim_both(<string>, <trim_string>)
```

## Analyze 示例

```python
func.trim_both('xxdatabendxx', 'x')
┌──────────────────────────────────────┐
│ func.trim_both('xxdatabendxx', 'x')  │
├──────────────────────────────────────┤
│ databend                             │
└──────────────────────────────────────┘
```

## SQL 语法

```sql
TRIM_BOTH(<string>, <trim_string>)
```

## SQL 示例

```sql
SELECT TRIM_BOTH('xxdatabendxx', 'xxx'), TRIM_BOTH('xxdatabendxx', 'xx'), TRIM_BOTH('xxdatabendxx', 'x');

┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_both('xxdatabendxx', 'xxx') │ trim_both('xxdatabendxx', 'xx') │ trim_both('xxdatabendxx', 'x') │
├──────────────────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ xxdatabendxx                     │ databend                        │ databend                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
