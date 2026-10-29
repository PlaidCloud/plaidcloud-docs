---
title: TRIM_LEADING (Lakehouse v1)
description: TRIM_LEADING：从字符串开头删除所有指定的修剪字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-leading.md
---

从字符串开头删除所有指定的修剪字符串。

另请参阅：

- [LTRIM](../ltrim)
- [TRIM_TRAILING](../trim-trailing)

## Analyze 语法

```python
func.trim_leading(<string>, <trim_string>)
```

## Analyze 示例

```python
func.trim_leading('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_leading('xxdatabendxx', 'x')   │
├──────────────────────────────────────────┤
│ databendxx                               │
└──────────────────────────────────────────┘
```

## SQL 语法

```sql
TRIM_LEADING(<string>, <trim_string>)
```

## SQL 示例

```sql
SELECT TRIM_LEADING('xxdatabend', 'xxx'), TRIM_LEADING('xxdatabend', 'xx'), TRIM_LEADING('xxdatabend', 'x');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_leading('xxdatabend', 'xxx') │ trim_leading('xxdatabend', 'xx') │ trim_leading('xxdatabend', 'x') │
├───────────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ xxdatabend                        │ databend                         │ databend                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
