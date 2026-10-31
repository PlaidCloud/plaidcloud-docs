---
title: STR2DATE (Lakehouse v2)
description: STR2DATE — 使用格式字符串将字符串解析为日期。是 `STR_TO_DATE` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str2date.md
---

使用格式字符串将字符串解析为日期。是 `STR_TO_DATE` 的别名。

## Analyze 语法

```python
func.str2date(<str>, <format>)
```

## Analyze 示例

```python
func.str2date('2024/06/15', '%Y/%m/%d')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 语法

```sql
STR2DATE(<str>, <format>)
```

## SQL 示例

```sql
SELECT STR2DATE('2024/06/15', '%Y/%m/%d');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
