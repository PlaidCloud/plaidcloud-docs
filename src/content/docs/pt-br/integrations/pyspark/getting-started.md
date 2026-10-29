---
title: Introdução ao PySpark
description: Comece a usar o PySpark no PlaidCloud para processamento distribuído de dados em funções definidas pelo usuário e em Notebooks Jupyter.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/pyspark/getting-started.md
---

## Documentação do PySpark
O PySpark é semelhante ao uso do Pandas, mas permite computação distribuída e não é limitado pela RAM. O PySpark está disponível tanto em UDFs quanto em Notebooks Jupyter.

Uma UDF usa o cluster Spark por meio do Spark Connect, com a API de DataFrame e SQL do PySpark (`pyspark.sql`). As partes do PySpark que precisam do Java em execução junto com o seu código não podem ser usadas em uma UDF: `SparkContext`, `RDD`, `pyspark.streaming` e a maior parte da API `pyspark.mllib` baseada em RDD não podem ser importados, e um DataFrame do Spark não pode ser passado para o statsforecast ou o Fugue.

## Cluster Spark
Por padrão, os espaços de trabalho não têm o cluster Spark habilitado. Para ativar o cluster Spark, acesse o aplicativo de gerenciamento do espaço de trabalho e habilite o serviço "Spark Compute Cluster".

Depois de ativado, os trabalhos do Spark podem ser enviados ao cluster.

O cluster pode ser monitorado pelo subdomínio `spark` do espaço de trabalho (por exemplo, `https://spark.my_workspace.plaid.cloud`)
