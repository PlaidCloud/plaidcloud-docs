---
title: CLUSTERING_INFORMATION (Lakehouse v1)
description: CLUSTERING_INFORMATION devuelve la información de agrupación en clústeres de una tabla.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/clustering-information.md
---

Devuelve la información de agrupación en clústeres de una tabla.

## Sintaxis de SQL

```sql
CLUSTERING_INFORMATION('<database_name>', '<table_name>')
```

## Ejemplos de SQL

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

| Parámetro               	| Descripción                                                                                                            	|
|-------------------------	|------------------------------------------------------------------------------------------------------------------------	|
| cluster_key         	| La clave de clúster definida.                                                                                               	|
| total_block_count       	| El recuento actual de bloques.                                                                                           	|
| constant_block_count    	| El recuento de bloques en los que los valores mínimo y máximo son iguales, es decir, cada bloque contiene un solo valor (o grupo de valores) de cluster_key. 	|
| unclustered_block_count 	| El recuento de bloques que aún no se han agrupado en clústeres.                                                                  	|
| average_overlaps        	| La proporción media de bloques que se superponen dentro de un intervalo dado.                                                          	|
| average_depth           	| La profundidad media de las particiones superpuestas para la clave de clúster.                                                       	|
| block_depth_histogram   	| El número de particiones en cada nivel de profundidad. Una mayor concentración de particiones en profundidades bajas indica una agrupación en clústeres más eficaz de la tabla.                                                                          	|
