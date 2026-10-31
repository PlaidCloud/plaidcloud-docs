---
title: Introducción a PySpark
description: Comience a usar PySpark en PlaidCloud para el procesamiento de datos distribuido dentro de funciones definidas por el usuario y Cuadernos de Jupyter.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/pyspark/getting-started.md
---

## Documentación de PySpark
PySpark es similar a usar Pandas, pero permite el cómputo distribuido y no está limitado por la RAM.  PySpark está disponible tanto en las UDF como en los Cuadernos de Jupyter.

Una UDF usa el clúster de Spark a través de Spark Connect, con la API de DataFrame y SQL de PySpark (`pyspark.sql`). Las partes de PySpark que necesitan Java en ejecución junto con su código no se pueden usar en una UDF: `SparkContext`, `RDD`, `pyspark.streaming` y la mayor parte de la API `pyspark.mllib` basada en RDD no se pueden importar, y un DataFrame de Spark no se puede pasar a statsforecast ni a Fugue.

## Clúster de Spark
De forma predeterminada, los espacios de trabajo no tienen habilitado el clúster de Spark.  Para activar el clúster de Spark, vaya a la aplicación de administración del espacio de trabajo y habilite el servicio "Spark Compute Cluster".

Una vez activado, se pueden enviar trabajos de Spark al clúster.

El clúster se puede supervisar desde el subdominio `spark` del espacio de trabajo (por ejemplo, `https://spark.my_workspace.plaid.cloud`)
