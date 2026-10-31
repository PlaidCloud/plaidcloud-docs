---
title: STR_TO_JODATIME (Lakehouse v2)
description: STR_TO_JODATIME — 使用 Joda-Time 格式模式将字符串解析为日期时间。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-jodatime.md
---

使用 Joda-Time 格式模式将字符串解析为日期时间。

## Analyze 语法

```python
func.str_to_jodatime(<str>, <pattern>)
```

## Analyze 示例

```python
func.str_to_jodatime('2024/06/15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 语法

```sql
STR_TO_JODATIME(<str>, <pattern>)
```

## SQL 示例

```sql
SELECT STR_TO_JODATIME('2024/06/15', 'yyyy/MM/dd');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
