---
title: TO_SECOND（Lakehouse v1）
description: TO_SECOND——将带时间的日期（timestamp/datetime）转换为 UInt8 数字，表示分钟中的秒数（0-59）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-second.md
---

将带时间的日期（timestamp/datetime）转换为 UInt8 数字，表示分钟中的秒数（0-59）。

## Analyze 语法

```python
func.to_second(<expr>)
```

## Analyze 示例

```python
func.to_second('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_second('2023-11-12 09:38:18.165575') │
│                   UInt8                      │
├──────────────────────────────────────────────┤
│                                           18 │
└──────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_SECOND(<expr>)
```

## 参数

| 参数      | 说明        |
|-----------|-------------|
| `<expr>`  | 时间戳      |

## 返回类型

`TINYINT`

## SQL 示例

```sql
SELECT
    to_second('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_second('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      18 │
└─────────────────────────────────────────┘
```
