---
title: Aggregate Functions (Lakehouse v1)
description: "Lakehouse v1 SQL 聚合函数：汇总行数据，包括 SUM、AVG、MIN、MAX、COUNT 以及统计类聚合函数。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/index.md
---

聚合函数是 SQL 中的重要工具，可对一组值进行计算并返回单个结果。

这些函数可帮助您从数据库中提取并汇总数据，从而获得有价值的洞察。

| 函数名称                                                    | 功能                                                                 | 
|------------------------------------------------------------------|------------------------------------------------------------------------------|
| [ANY](aggregate-any)                                             | 检查是否有任何行满足指定条件                              | 
| [APPROX_COUNT_DISTINCT](aggregate-approx-count-distinct)         | 使用 HyperLogLog 估算不同值的数量                     | 
| [ARG_MAX](aggregate-arg-max)                                     | 查找最大 val 值所对应的 arg 值                                | 
| [ARG_MIN](aggregate-arg-min)                                     | 查找最小 val 值所对应的 arg 值                                | 
| [AVG_IF](aggregate-avg-if)                                       | 计算满足条件的行的平均值                          | 
| [ARRAY_AGG](aggregate-array-agg)                                 | 将列的所有值转换为数组                              |
| [AVG](aggregate-avg)                                             | 计算指定列的平均值                            | 
| [COUNT_DISTINCT](aggregate-count-distinct)                       | 统计列中不同值的数量                             | 
| [COUNT_IF](aggregate-count-if)                                   | 统计满足指定条件的行数                                    | 
| [COUNT](aggregate-count)                                         | 统计满足特定条件的行数                         | 
| [COVAR_POP](aggregate-covar-pop)                                 | 返回一组数值对的总体协方差                   | 
| [COVAR_SAMP](aggregate-covar-samp)                               | 返回一组数值对的样本协方差                       | 
| [GROUP_ARRAY_MOVING_AVG](aggregate-group-array-moving-avg)       | 返回一个数组，其元素为输入值的移动平均值 |
| [GROUP_ARRAY_MOVING_SUM](aggregate-group-array-moving-sum)       | 返回一个数组，其元素为输入值的移动总和     |
| [HISTOGRAM](aggregate-histogram)                                | 使用等高分桶生成数据分布直方图        | 
| [JSON_ARRAY_AGG](aggregate-json-array-agg)                      | 将值转换为 JSON 数组，跳过 NULL                           | 
| [JSON_OBJECT_AGG](aggregate-json-object-agg)                    | 将键值对转换为 JSON 对象                                 | 
| [KURTOSIS](aggregate-kurtosis)                                   | 计算一组值的超额峰度                            | 
| [MAX_IF](aggregate-max-if)                                       | 查找满足条件的行的最大值                         | 
| [MAX](aggregate-max)                                             | 查找指定列中的最大值                                 | 
| [MEDIAN](aggregate-median)                                       | 计算指定列的中位数                             | 
| [MEDIAN_TDIGEST](aggregate-median-tdigest)                       | 使用 t-digest 算法计算指定列的中位数    | 
| [MIN_IF](aggregate-min-if)                                       | 查找满足条件的行的最小值                         | 
| [MIN](aggregate-min)                                             | 查找指定列中的最小值                                | 
| [QUANTILE_CONT](aggregate-quantile-cont)                         | 计算指定列经插值得到的分位数                   |
| [QUANTILE_DISC](aggregate-quantile-disc)                         | 计算指定列的分位数                                | 
| [QUANTILE_TDIGEST](aggregate-quantile-tdigest)                   | 使用 t-digest 算法计算分位数                             |
| [QUANTILE_TDIGEST_WEIGHTED](aggregate-quantile-tdigest-weighted) | 使用 t-digest 算法计算加权分位数               |
| [RETENTION](aggregate-retention)                                 | 计算一组事件的留存                                     | 
| [SKEWNESS](aggregate-skewness)                                   | 计算一组值的偏度                                   | 
| [STDDEV_POP](aggregate-stddev-pop)                               | 计算列的总体标准差                     | 
| [STDDEV_SAMP](aggregate-stddev-samp)                             | 计算列的样本标准差                         | 
| [STRING_AGG](aggregate-string-agg)                               | 将所有非 NULL 值转换为字符串，并以分隔符分隔       |
| [SUM_IF](aggregate-sum-if)                                       | 对指定列中满足条件的值求和                  | 
| [SUM](aggregate-sum)                                             | 对指定列的值求和                                      | 
| [WINDOW_FUNNEL](aggregate-windowfunnel)                          | 分析按时间排序的事件序列中的用户行为                  |
