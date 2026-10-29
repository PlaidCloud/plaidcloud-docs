---
title: CLUSTERING_INFORMATION (Lakehouse v1)
description: CLUSTERING_INFORMATION — 테이블의 클러스터링 정보를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/clustering-information.md
---

테이블의 클러스터링 정보를 반환합니다.

## SQL 구문

```sql
CLUSTERING_INFORMATION('<database_name>', '<table_name>')
```

## SQL 예제

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

| 매개변수 | 설명 |
|-------------------------|------------------------------------------------------------------------------------------------------------------------|
| cluster_key | 정의된 클러스터 키입니다. |
| total_block_count | 현재 블록 수입니다. |
| constant_block_count | 최솟값과 최댓값이 같은 블록의 수입니다. 즉, 각 블록에 cluster_key 값이 하나(또는 한 그룹)만 들어 있습니다. |
| unclustered_block_count | 아직 클러스터링되지 않은 블록의 수입니다. |
| average_overlaps | 지정한 범위 내에서 겹치는 블록의 평균 비율입니다. |
| average_depth | 클러스터 키에 대해 겹치는 파티션의 평균 깊이입니다. |
| block_depth_histogram | 각 깊이 수준의 파티션 수입니다. 낮은 깊이에 파티션이 더 많이 몰려 있을수록 테이블 클러스터링이 더 효과적입니다. |
