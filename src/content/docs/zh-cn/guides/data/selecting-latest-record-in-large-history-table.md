---
title: 在大型版本历史表中选择最新记录
description: 了解如何使用优化的查询技巧，在 PlaidCloud 的大型历史表中高效选择最新记录。
sidebar:
  label: 在大型版本历史表中选择最新记录
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/selecting-latest-record-in-large-history-table.md
---

## 挑战

有一个表包含每条记录的多个版本，但您必须使用最新版本。

## 讨论

可以先把 ID 和最大更新日期选入一个临时表，再将该临时表与历史表做 INNER JOIN 以获得结果，从而解决此问题。遗憾的是，这需要两个步骤，并且要存储一个除查找最新更新之外别无用处的中间表。

更优雅的做法是使用带排序的窗口函数加上筛选器，在单个查询中完成该操作。

## 解决方案

### 版本历史表

| employee_id | department | salary    | update_date  |
|-------------|------------|-----------|--------------|
| 3           | IT         | 90000     | 2024-09-17   |
| 2           | HR         | 85000     | 2024-09-17   |
| 5           | HR         | 82000     | 2024-09-17   |
| 3           | IT         | 77000     | 2023-10-01   |
| 3           | IT         | 75000     | 2022-10-04   |
| 5           | IT         | 72000     | 2024-07-12   |
| 2           | IT         | 67000     | 2024-03-18   |
| 1           | Sales      | 62000     | 2022-02-28   |
| 5           | Sales      | 60000     | 2023-01-14   |
| 4           | Sales      | 58000     | 2021-11-19   |

### 步骤设置
使用提取步骤，在名为 `Rank` 的列中创建窗口函数表达式，例如：

```python
func.rank().over(order_by=table.updated_date.desc(), partition_by=table.employee_id)
```

在提取步骤的筛选器选项卡中，设置如下筛选器：

```python
table.Rank == 1
```

### 结果

| employee_id | department | salary    | update_date  | Rank |
|-------------|------------|-----------|--------------|------|
| 3           | IT         | 90000     | 2024-09-17   | 1    |
| 2           | HR         | 85000     | 2024-09-17   | 1    |
| 5           | HR         | 82000     | 2024-09-17   | 1    |
| 1           | Sales      | 62000     | 2022-02-28   | 1    |
| 4           | Sales      | 58000     | 2021-11-19   | 1    |

这种方法非常高效，只需一个步骤即可在多版本历史表中选出最新记录。其原理是在 `employee_id` 分组内按 `update_date` 对每条记录排名，然后只选取第一条记录。

如果唯一行键由多个列组成，可以将它们作为列表添加到 `partition_by` 参数中，例如：

```python
partition_by=[table.first_column, table.second_column, table.third_column]
```

如果需要应用多列排序，同样可以使用列的列表来实现，例如：

```python
order_by=[table.first_column.desc(), table.second_column, table.third_column.desc()]
```
