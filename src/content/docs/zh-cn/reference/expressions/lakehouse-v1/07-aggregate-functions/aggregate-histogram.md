---
title: HISTOGRAM (Lakehouse v1)
description: HISTOGRAM：使用等高分桶策略生成数据分布直方图。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-histogram.md
---

使用“等高”分桶策略生成数据分布直方图。

## Analyze 语法

```python
func.histogram(<expr>)
```

## Analyze 示例
详见 SQL 示例

## SQL 语法

```sql
HISTOGRAM(<expr>)

-- The following two forms are equivalent:
HISTOGRAM(<max_num_buckets>)(<expr>)
HISTOGRAM(<expr> [, <max_num_buckets>])
```

| 参数         | 说明                                                                         |
|-------------------|-------------------------------------------------------------------------------------|
| `expr`            | `expr` 的数据类型应可排序。                                         |
| `max_num_buckets` | 可选的正整数，指定存储桶的最大数量。默认为 128。 |

## 返回类型

返回空字符串或具有以下结构的 JSON 对象：

- **buckets**：包含详细信息的存储桶列表：
  - **lower**：存储桶的下限。
  - **upper**：存储桶的上限。
  - **count**：存储桶中的元素数量（计数）。
  - **pre_sum**：截至当前存储桶的元素累计数量。
  - **ndv**：存储桶中不同值的数量。

## SQL 示例

此示例展示 HISTOGRAM 函数如何分析 `histagg` 表中 `c_int` 值的分布，返回存储桶边界、不同值计数、元素计数和累计计数：

```sql
CREATE TABLE histagg (
  c_id INT,
  c_tinyint TINYINT,
  c_smallint SMALLINT,
  c_int INT
);

INSERT INTO histagg VALUES
  (1, 10, 20, 30),
  (1, 11, 21, 33),
  (1, 11, 12, 13),
  (2, 21, 22, 23),
  (2, 31, 32, 33),
  (2, 10, 20, 30);

SELECT HISTOGRAM(c_int) FROM histagg;

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                              histogram(c_int)                                                                                                             │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [{"lower":"13","upper":"13","ndv":1,"count":1,"pre_sum":0},{"lower":"23","upper":"23","ndv":1,"count":1,"pre_sum":1},{"lower":"30","upper":"30","ndv":1,"count":2,"pre_sum":2},{"lower":"33","upper":"33","ndv":1,"count":2,"pre_sum":4}] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

结果以 JSON 数组形式返回：

```json
[
  {
    "lower": "13",
    "upper": "13",
    "ndv": 1,
    "count": 1,
    "pre_sum": 0
  },
  {
    "lower": "23",
    "upper": "23",
    "ndv": 1,
    "count": 1,
    "pre_sum": 1
  },
  {
    "lower": "30",
    "upper": "30",
    "ndv": 1,
    "count": 2,
    "pre_sum": 2
  },
  {
    "lower": "33",
    "upper": "33",
    "ndv": 1,
    "count": 2,
    "pre_sum": 4
  }
]
```

此示例展示 `HISTOGRAM(2)` 如何将 c_int 值分到两个存储桶中：

```sql
SELECT HISTOGRAM(2)(c_int) FROM histagg;
-- Or
SELECT HISTOGRAM(c_int, 2) FROM histagg;

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                  histogram(2)(c_int)                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [{"lower":"13","upper":"30","ndv":3,"count":4,"pre_sum":0},{"lower":"33","upper":"33","ndv":1,"count":2,"pre_sum":4}] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

结果以 JSON 数组形式返回：

```json
[
  {
    "lower": "13",
    "upper": "30",
    "ndv": 3,
    "count": 4,
    "pre_sum": 0
  },
  {
    "lower": "33",
    "upper": "33",
    "ndv": 1,
    "count": 2,
    "pre_sum": 4
  }
]
```
