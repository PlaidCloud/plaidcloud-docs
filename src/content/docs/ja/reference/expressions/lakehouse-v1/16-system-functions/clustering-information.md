---
title: CLUSTERING_INFORMATION（Lakehouse v1）
description: CLUSTERING_INFORMATION — テーブルのクラスタリング情報を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/clustering-information.md
---

テーブルのクラスタリング情報を返します。

## SQLの構文

```sql
CLUSTERING_INFORMATION('<database_name>', '<table_name>')
```

## SQLの例

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

| パラメータ               	| 説明                                                                                                            	|
|-------------------------	|------------------------------------------------------------------------------------------------------------------------	|
| cluster_key         	| 定義されたクラスターキー。                                                                                               	|
| total_block_count       	| 現在のブロック数。                                                                                           	|
| constant_block_count    	| 最小値と最大値が等しいブロックの数。つまり、各ブロックにcluster_key値（のグループ）が1つだけ含まれています。 	|
| unclustered_block_count 	| まだクラスタリングされていないブロックの数。                                                                  	|
| average_overlaps        	| 指定した範囲内で重複するブロックの平均比率。                                                          	|
| average_depth           	| クラスターキーに対して重複するパーティションの平均の深さ。                                                       	|
| block_depth_histogram   	| 各深さレベルのパーティション数。浅い深さにパーティションが多く集中しているほど、テーブルのクラスタリングが効果的であることを示します。                                                                          	|
