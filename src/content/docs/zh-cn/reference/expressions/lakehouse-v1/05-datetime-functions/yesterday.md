---
title: YESTERDAY（Lakehouse v1）
description: YESTERDAY——返回昨天的日期，等同于 today() - 1。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/yesterday.md
---

返回昨天的日期，等同于 `today() - 1`。

## Analyze 语法

```python
func.yesterday()
```

## Analyze 示例

```python
func.yesterday()
┌──────────────────┐
│ func.yesterday() │
├──────────────────┤
│ 2021-09-02       │
└──────────────────┘
```

## SQL 语法

```sql
YESTERDAY()
```

## 返回类型

`DATE`，返回“YYYY-MM-DD”格式的日期。

## SQL 示例

```sql
SELECT YESTERDAY();
┌─────────────┐
│ YESTERDAY() │
├─────────────┤
│ 2021-09-02  │
└─────────────┘

SELECT TODAY()-1;
┌───────────────┐
│ (TODAY() - 1) │
├───────────────┤
│ 2021-09-02    │
└───────────────┘
```
