---
title: Introdução ao PySpark
description: Comece a utilizar o PySpark no PlaidCloud para processamento de dados distribuído em funções definidas pelo utilizador e em blocos de notas Jupyter.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/pyspark/getting-started.md
---

## Documentação do PySpark
A utilização do PySpark é semelhante à do Pandas, mas permite computação distribuída e não está limitada pela RAM.  O PySpark está disponível tanto em UDF como em blocos de notas Jupyter.

Uma UDF utiliza o cluster Spark através do Spark Connect, com a API de DataFrame e SQL do PySpark (`pyspark.sql`). Não é possível utilizar as partes do PySpark que precisam de Java em execução a par do seu código: `SparkContext`, `RDD`, `pyspark.streaming` e a maior parte da API `pyspark.mllib` baseada em RDD não podem ser importados, e um DataFrame do Spark não pode ser passado ao statsforecast nem ao Fugue.

## Cluster Spark
Por predefinição, as áreas de trabalho não têm o cluster Spark ativado.  Para ativar o cluster Spark, aceda à aplicação de gestão da área de trabalho e ative o serviço "Spark Compute Cluster".

Depois de ativado, é possível submeter tarefas Spark ao cluster.

O cluster pode ser monitorizado a partir do subdomínio `spark` da área de trabalho (por exemplo, `https://spark.my_workspace.plaid.cloud`)
