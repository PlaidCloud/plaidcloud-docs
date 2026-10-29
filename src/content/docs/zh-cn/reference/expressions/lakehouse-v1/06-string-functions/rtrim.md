---
title: RTRIM（Lakehouse v1）
description: RTRIM——从字符串右侧移除指定修剪字符串中出现的所有字符。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rtrim.md
---

从字符串右侧移除指定修剪字符串中出现的所有字符。

另请参阅：

- [TRIM_TRAILING](../trim-trailing)
- [LTRIM](../ltrim)

## Analyze 语法

```python
func.rtrim(<string>, <trim_string>)
```

## Analyze 示例

```python
func.rtrim('databend'xx, 'x')
┌────────────────────────────────┐
│ func.rtrim('databendxx', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## SQL 语法

```sql
RTRIM(<string>, <trim_string>)
```

## SQL 示例

```sql
SELECT RTRIM('databendxx', 'x'), RTRIM('databendxx', 'xy');

┌──────────────────────────────────────────────────────┐
│ rtrim('databendxx', 'x') │ rtrim('databendxx', 'xy') │
├──────────────────────────┼───────────────────────────┤
│ databend                 │ databend                  │
└──────────────────────────────────────────────────────┘
```
