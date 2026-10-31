---
title: TIMEZONE（Lakehouse v1）
description: TIMEZONE——返回当前连接的时区。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timezone.md
---

返回当前连接的时区。 

PlaidCloud Lakehouse 默认使用 UTC（协调世界时）作为时区，并允许将时区更改为您当前所在的地理位置。`timezone` 设置可使用的取值请参阅 https://docs.rs/chrono-tz/latest/chrono_tz/enum.Tz.html。详见下面的示例。

## Analyze 语法

```python
func.timezone()
```

## Analyze 示例

```python
func.timezone()
┌─────────────────────┐
│ timezone            │
├─────────────────────┤
│ UTC                 │
└─────────────────────┘
```

## SQL 语法

```sql
SELECT TIMEZONE();
```

## SQL 示例

```sql
-- Return the current timezone
SELECT TIMEZONE();
┌─────────────────┐
│ TIMEZONE('UTC') │
├─────────────────┤
│ UTC             │
└─────────────────┘

-- Set the timezone to China Standard Time
SET timezone='Asia/Shanghai';

SELECT TIMEZONE();
┌───────────────────────────┐
│ TIMEZONE('Asia/Shanghai') │
├───────────────────────────┤
│ Asia/Shanghai             │
└───────────────────────────┘
```
