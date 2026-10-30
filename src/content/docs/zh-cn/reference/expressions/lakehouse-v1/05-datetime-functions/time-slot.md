---
title: TIME_SLOT（Lakehouse v1）
description: TIME_SLOT——将时间舍入到半小时。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/time-slot.md
---

将时间舍入到半小时。

## Analyze 语法

```python
func.time_slot(<expr>)
```

## Analyze 示例

```python
func.time_slot('2023-11-12 09:38:18.165575')
┌───────────────────────────────-───-───-──────┐
│ func.time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                     │
├─────────────────────────────────-───-────────┤
│ 2023-11-12 09:30:00                          │
└─────────────────────────────────-───-────────┘
```

## SQL 语法

```sql
time_slot(<expr>)
```

## 参数

| 参数        | 说明        |
| ----------- | ----------- |
| `<expr>`    | 时间戳      |

## 返回类型

`TIMESTAMP`，以“YYYY-MM-DD hh:mm:ss.ffffff”格式返回。

## SQL 示例

```sql
SELECT
  time_slot('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                │
├─────────────────────────────────────────┤
│ 2023-11-12 09:30:00                     │
└─────────────────────────────────────────┘
```
