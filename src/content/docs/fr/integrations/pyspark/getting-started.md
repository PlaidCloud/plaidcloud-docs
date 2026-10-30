---
title: Premiers pas avec PySpark
description: Découvrez comment utiliser PySpark dans PlaidCloud pour le traitement distribué des données dans les fonctions définies par l'utilisateur et les Notebooks Jupyter.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/pyspark/getting-started.md
---

## Documentation PySpark
PySpark s'utilise comme Pandas, mais il permet un calcul distribué et n'est pas limité par la RAM.  PySpark est disponible dans les UDF et dans les Notebooks Jupyter.

Une UDF utilise le cluster Spark via Spark Connect, avec l'API DataFrame et SQL de PySpark (`pyspark.sql`). Les parties de PySpark qui nécessitent l'exécution de Java en parallèle de votre code ne peuvent pas être utilisées dans une UDF : `SparkContext`, `RDD`, `pyspark.streaming` et la plupart de l'API `pyspark.mllib` basée sur les RDD ne peuvent pas être importés, et un DataFrame Spark ne peut pas être transmis à statsforecast ou à Fugue.

## Cluster Spark
Par défaut, le cluster Spark n'est pas activé dans les espaces de travail.  Pour l'activer, accédez à l'application de gestion de l'espace de travail et activez le service « Spark Compute Cluster ».

Une fois le cluster activé, vous pouvez lui soumettre des tâches Spark.

Vous pouvez surveiller le cluster depuis le sous-domaine `spark` de l'espace de travail (par exemple `https://spark.my_workspace.plaid.cloud`)
