---
title: CLUSTERING_INFORMATION (Lakehouse v1)
description: CLUSTERING_INFORMATION — retorna informações de clusterização de uma tabela.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/clustering-information.md
---

Retorna informações de clusterização de uma tabela.

## Sintaxe SQL

```sql
CLUSTERING_INFORMATION('<database_name>', '<table_name>')
```

## Exemplos de SQL

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

| Parâmetro               	| Descrição                                                                                                            	|
|-------------------------	|------------------------------------------------------------------------------------------------------------------------	|
| cluster_key         	| A chave de cluster definida.                                                                                               	|
| total_block_count       	| A contagem atual de blocos.                                                                                           	|
| constant_block_count    	| A contagem de blocos em que os valores mín./máx. são iguais, ou seja, cada bloco contém apenas um valor (ou grupo de valores) de cluster_key. 	|
| unclustered_block_count 	| A contagem de blocos que ainda não foram clusterizados.                                                                  	|
| average_overlaps        	| A razão média de blocos sobrepostos dentro de um determinado intervalo.                                                          	|
| average_depth           	| A profundidade média das partições sobrepostas para a chave de cluster.                                                       	|
| block_depth_histogram   	| O número de partições em cada nível de profundidade. Uma concentração maior de partições em profundidades menores indica uma clusterização de tabela mais eficaz.                                                                          	|
