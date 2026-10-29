---
title: CLUSTERING_INFORMATION (Lakehouse v1)
description: CLUSTERING_INFORMATION gibt Clustering-Informationen einer Tabelle zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/clustering-information.md
---

Gibt Clustering-Informationen einer Tabelle zurück.

## SQL-Syntax

```sql
CLUSTERING_INFORMATION('<database_name>', '<table_name>')
```

## SQL-Beispiele

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

| Parameter               	| Beschreibung                                                                                                            	|
|-------------------------	|------------------------------------------------------------------------------------------------------------------------	|
| cluster_key         	| Der definierte Cluster-Schlüssel.                                                                                               	|
| total_block_count       	| Die aktuelle Anzahl der Blöcke.                                                                                           	|
| constant_block_count    	| Die Anzahl der Blöcke, in denen Minimal- und Maximalwert gleich sind, die also jeweils nur einen Wert (oder eine Gruppe von Werten) des cluster_key enthalten. 	|
| unclustered_block_count 	| Die Anzahl der Blöcke, die noch nicht geclustert wurden.                                                                  	|
| average_overlaps        	| Das durchschnittliche Verhältnis überlappender Blöcke innerhalb eines bestimmten Bereichs.                                                          	|
| average_depth           	| Die durchschnittliche Tiefe überlappender Partitionen für den Cluster-Schlüssel.                                                        	|
| block_depth_histogram   	| Die Anzahl der Partitionen je Tiefenstufe. Eine höhere Konzentration von Partitionen in geringeren Tiefen weist auf ein effektiveres Clustering der Tabelle hin.                                                                          	|
