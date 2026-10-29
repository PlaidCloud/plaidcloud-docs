---
title: TASK_HISTORY (Lakehouse v1)
description: TASK_HISTORY：根据给定变量显示任务运行历史。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/task-history.md
---

根据给定变量显示任务运行历史。

## SQL 语法
```sql
TASK_HISTORY(
      [ SCHEDULED_TIME_RANGE_START => <constant_expr> ]
      [, SCHEDULED_TIME_RANGE_END => <constant_expr> ]
      [, RESULT_LIMIT => <integer> ]
      [, TASK_NAME => '<string>' ]
      [, ERROR_ONLY => { TRUE | FALSE } ]
      [, ROOT_TASK_ID => '<string>'] )
```



## 参数

所有参数均为可选。

`SCHEDULED_TIME_RANGE_START => <constant_expr>`、`SCHEDULED_TIME_RANGE_END => <constant_expr>`

任务计划执行的时间范围（TIMESTAMP_LTZ 格式），须在最近 7 天内。如果时间范围不在最近 7 天内，则返回错误。

* 如果未指定 `SCHEDULED_TIME_RANGE_END`，函数将返回已完成、正在运行或计划在未来运行的任务。
* 如果 `SCHEDULED_TIME_RANGE_END` 为 CURRENT_TIMESTAMP，函数将返回已完成或正在运行的任务。请注意，在当前时间之前刚刚执行的任务仍可能被识别为已计划。
* 若只查询已完成或正在运行的任务，请添加 `WHERE query_id IS NOT NULL` 作为筛选器。TASK_HISTORY 输出中的 QUERY_ID 列仅在任务开始运行后才会填充。

如果未指定开始或结束时间，则返回最近的任务，数量不超过指定的 RESULT_LIMIT 值。

`RESULT_LIMIT => <integer>`

指定函数返回的最大行数的数字。

如果匹配的行数大于此限制，则返回时间戳最新的任务执行记录，数量不超过指定限制。

范围：`1` 至 `10000`

默认：`100`。

`TASK_NAME => <string>`

指定任务的字符串，不区分大小写。仅支持非限定的任务名称。仅返回指定任务的执行记录。请注意，如果多个任务同名，函数将返回其中每个任务的历史记录。

`ERROR_ONLY => { TRUE | FALSE }`

设置为 TRUE 时，此函数仅返回失败或被取消的任务运行。

`ROOT_TASK_ID => <string>`

任务图中根任务的唯一标识符。该 ID 与 SHOW TASKS 输出中同一任务的 ID 列值一致。指定 ROOT_TASK_ID 可显示根任务及属于该任务图的所有子任务的历史记录。

## 使用说明
* 此函数最多返回 10,000 行，由 RESULT_LIMIT 参数值设定。默认值为 100。
* 此函数仅对 ACCOUNTADMIN 角色返回结果。


## SQL 示例

```sql
SELECT
  *
FROM TASK_HISTORY() order by scheduled_time;
```
上述 SQL 查询从 TASK_HISTORY 函数检索所有任务历史记录，并按 scheduled_time 列排序。（最多 10,000 条）



```sql
SELECT *
  FROM TASK_HISTORY(
    SCHEDULED_TIME_RANGE_START=>TO_TIMESTAMP('2022-01-02T01:12:00-07:00'),
    SCHEDULED_TIME_RANGE_END=>TO_TIMESTAMP('2022-01-02T01:12:30-07:00'))
```

上述 SQL 查询从 TASK_HISTORY 函数检索所有计划时间范围从 '2022-01-02T01:12:00-07:00' 开始、到 '2022-01-02T01:12:30-07:00' 结束的任务历史记录。这意味着它将返回计划在这个 30 秒时间窗口内运行的任务。结果将包含符合此条件的任务的详细信息。
