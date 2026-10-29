---
title: CLUSTERING_INFORMATION (Lakehouse v1)
description: CLUSTERING_INFORMATION：返回表的聚簇信息。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/clustering-information.md
---

返回表的聚簇信息。

## SQL 语法

```sql
CLUSTERING_INFORMATION('<database_name>', '<table_name>')
```

## SQL 示例

```sql
CREATE TABLE mytable(a int, b int) CLUSTER BY(a+1);

INSERT INTO mytable VALUES(1,1),(3,3);
INSERT INTO mytable VALUES(2,2),(5,5);
INSERT INTO mytable VALUES(4,4);

SELECT * FROM CLUSTERING_INFORMATION('default','mytable')\G
*************************** 1. row ***************************
            cluster_key: ((a + 1))
      total_block_count: 3
   constant_block_count: 1
unclustered_block_count: 0
       average_overlaps: 1.3333
          average_depth: 2.0
  block_depth_histogram: {"00002":3}
```

| 参数 | 说明 |
|-------------------------|------------------------------------------------------------------------------------------------------------------------|
| cluster_key | 已定义的聚簇键。 |
| total_block_count | 当前的块数量。 |
| constant_block_count | 最小值与最大值相等的块数量，即每个块只包含一个（组）cluster_key 值。 |
| unclustered_block_count | 尚未聚簇的块数量。 |
| average_overlaps | 给定范围内重叠块的平均比例。 |
| average_depth | 聚簇键重叠分区的平均深度。 |
| block_depth_histogram | 每个深度级别上的分区数量。较多分区集中在较低深度，表示表的聚簇效果更好。 |
