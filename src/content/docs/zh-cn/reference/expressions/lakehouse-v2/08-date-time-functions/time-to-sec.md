---
title: TIME_TO_SEC (Lakehouse v2)
description: TIME_TO_SEC — 将时间值转换为秒数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-to-sec.md
---

将时间值转换为秒数。

## Analyze 语法

```python
func.time_to_sec(<time>)
```

## Analyze 示例

```python
func.time_to_sec('01:01:01')

┌──────┐
│ 3661  │
└──────┘
```

## SQL 语法

```sql
TIME_TO_SEC(<time>)
```

## SQL 示例

```sql
SELECT TIME_TO_SEC('01:01:01');

┌──────┐
│ 3661  │
└──────┘
```
