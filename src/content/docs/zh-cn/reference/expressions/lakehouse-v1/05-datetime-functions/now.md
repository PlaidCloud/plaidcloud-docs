---
title: NOW（Lakehouse v1）
description: NOW——返回当前日期和时间。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/now.md
---

返回当前日期和时间。

## Analyze 语法

```python
func.now()
```

## Analyze 示例

```python
┌─────────────────────────────────────────────────────────┐
│  func.current_timestamp()  │         func.now()         │
├────────────────────────────┼────────────────────────────┤
│ 2024-01-29 04:38:12.584359 │ 2024-01-29 04:38:12.584417 │
└─────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
NOW()
```

## 返回类型

TIMESTAMP

## 别名

- [CURRENT_TIMESTAMP](../current-timestamp)

## SQL 示例

此示例返回当前日期和时间：

```sql
SELECT CURRENT_TIMESTAMP(), NOW();

┌─────────────────────────────────────────────────────────┐
│     current_timestamp()    │            now()           │
├────────────────────────────┼────────────────────────────┤
│ 2024-01-29 04:38:12.584359 │ 2024-01-29 04:38:12.584417 │
└─────────────────────────────────────────────────────────┘
```
