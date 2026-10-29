---
title: CLUSTERING_INFORMATION (Lakehouse v1)
description: CLUSTERING_INFORMATION — renvoie les informations de clustering d'une table.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/clustering-information.md
---

Renvoie les informations de clustering d'une table.

## Syntaxe SQL

```sql
CLUSTERING_INFORMATION('<database_name>', '<table_name>')
```

## Exemples SQL

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

| Paramètre               	| Description                                                                                                            	|
|-------------------------	|------------------------------------------------------------------------------------------------------------------------	|
| cluster_key         	| La clé de clustering définie.                                                                                               	|
| total_block_count       	| Le nombre actuel de blocs.                                                                                           	|
| constant_block_count    	| Le nombre de blocs dont les valeurs min/max sont égales, c'est-à-dire que chaque bloc ne contient qu'une seule valeur (ou un seul groupe de valeurs) de cluster_key. 	|
| unclustered_block_count 	| Le nombre de blocs qui n'ont pas encore été clusterisés.                                                                  	|
| average_overlaps        	| Le ratio moyen de blocs qui se chevauchent dans une plage donnée.                                                          	|
| average_depth           	| La profondeur moyenne des partitions qui se chevauchent pour la clé de clustering.                                                       	|
| block_depth_histogram   	| Le nombre de partitions à chaque niveau de profondeur. Une concentration plus élevée de partitions aux faibles profondeurs indique un clustering de la table plus efficace.                                                                          	|
