---
title: TO_DECADES（Lakehouse v1）
description: TO_DECADES——将指定数量的十年转换为 Interval 类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-decades.md
---

将指定数量的十年转换为 Interval 类型。

- 接受正整数、零和负整数作为输入。

## Analyze 语法

```python
func.to_decades(<decades>)
```

## Analyze 示例

```python
func.to_decades(2)
┌──────────────────────────────────────────────────────┐
│ func.to_decades(2)                                   │
├──────────────────────────────────────────────────────┤
│ 20 years                                             │
└──────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_DECADES(<decades>)
```

## 返回类型

Interval（以年表示）。

## SQL 示例

```sql
SELECT TO_DECADES(2), TO_DECADES(0), TO_DECADES((- 2));

┌─────────────────────────────────────────────────┐
│ to_decades(2) │ to_decades(0) │ to_decades(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 20 years      │ 00:00:00      │ -20 years       │
└─────────────────────────────────────────────────┘
```
