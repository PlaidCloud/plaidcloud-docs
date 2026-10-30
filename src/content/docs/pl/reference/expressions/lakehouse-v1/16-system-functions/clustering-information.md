---
title: CLUSTERING_INFORMATION (Lakehouse v1)
description: CLUSTERING_INFORMATION — zwraca informacje o klastrowaniu tabeli.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/clustering-information.md
---

Zwraca informacje o klastrowaniu tabeli.

## Składnia SQL

```sql
CLUSTERING_INFORMATION('<database_name>', '<table_name>')
```

## Przykłady SQL

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

| Parametr               	| Opis                                                                                                            	|
|-------------------------	|------------------------------------------------------------------------------------------------------------------------	|
| cluster_key         	| Zdefiniowany klucz klastrowania.                                                                                               	|
| total_block_count       	| Bieżąca liczba bloków.                                                                                           	|
| constant_block_count    	| Liczba bloków, w których wartości minimalna i maksymalna są równe, co oznacza, że każdy blok zawiera tylko jedną (grupę) wartość cluster_key. 	|
| unclustered_block_count 	| Liczba bloków, które nie zostały jeszcze poddane klastrowaniu.                                                                  	|
| average_overlaps        	| Średni stosunek nakładających się bloków w danym zakresie.                                                          	|
| average_depth           	| Średnia głębokość nakładających się partycji dla klucza klastrowania.                                                       	|
| block_depth_histogram   	| Liczba partycji na każdym poziomie głębokości. Większe skupienie partycji na mniejszych głębokościach oznacza skuteczniejsze klastrowanie tabeli.                                                                          	|
