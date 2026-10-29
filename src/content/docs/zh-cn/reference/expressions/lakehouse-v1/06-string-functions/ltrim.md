---
title: LTRIM（Lakehouse v1）
description: LTRIM——从字符串左侧移除指定修剪字符串中出现的所有字符。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ltrim.md
---

从字符串左侧移除指定修剪字符串中出现的所有字符。

另请参阅：

- [TRIM_LEADING](../trim-leading)
- [RTRIM](../rtrim)

## Analyze 语法

```python
func.ltrim(<string>, <trim_string>)
```

## Analyze 示例

```python
func.ltrim('xxdatabend', 'x')
┌────────────────────────────────┐
│ func.ltrim('xxdatabend', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## SQL 语法

```sql
LTRIM(<string>, <trim_string>)
```

## SQL 示例

```sql
SELECT LTRIM('xxdatabend', 'xx'), LTRIM('xxdatabend', 'xy');

┌───────────────────────────────────────────────────────┐
│ ltrim('xxdatabend', 'xx') │ ltrim('xxdatabend', 'xy') │
├───────────────────────────┼───────────────────────────┤
│ databend                  │ databend                  │
└───────────────────────────────────────────────────────┘
```
