---
title: TRIM_TRAILING (Lakehouse v1)
description: TRIM_TRAILING：从字符串末尾删除所有指定的修剪字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-trailing.md
---

从字符串末尾删除所有指定的修剪字符串。

另请参阅：

- [RTRIM](../rtrim)
- [TRIM_LEADING](../trim-leading)

## Analyze 语法

```python
func.trim_trailing(<string>, <trim_string>)
```

## Analyze 示例

```python
func.trim_trailing('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_trailing('xxdatabendxx', 'x')  │
├──────────────────────────────────────────┤
│ xxdatabend                               │
└──────────────────────────────────────────┘
```

## SQL 语法

```sql
TRIM_TRAILING(<string>, <trim_string>)
```

## SQL 示例

```sql
SELECT TRIM_TRAILING('databendxx', 'xxx'), TRIM_TRAILING('databendxx', 'xx'), TRIM_TRAILING('databendxx', 'x');

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_trailing('databendxx', 'xxx') │ trim_trailing('databendxx', 'xx') │ trim_trailing('databendxx', 'x') │
├────────────────────────────────────┼───────────────────────────────────┼──────────────────────────────────┤
│ databendxx                         │ databend                          │ databend                         │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
