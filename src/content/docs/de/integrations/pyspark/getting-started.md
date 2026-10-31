---
title: Erste Schritte mit PySpark
description: Erste Schritte mit PySpark in PlaidCloud für verteilte Datenverarbeitung in benutzerdefinierten Funktionen und Jupyter-Notebooks.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/pyspark/getting-started.md
---

## PySpark-Dokumentation
PySpark ähnelt der Verwendung von Pandas, ermöglicht aber verteilte Berechnungen und ist nicht an den Arbeitsspeicher gebunden.  PySpark steht sowohl in UDFs als auch in Jupyter-Notebooks zur Verfügung.

Eine UDF nutzt den Spark-Cluster über Spark Connect mit der DataFrame- und SQL-API von PySpark (`pyspark.sql`). Teile von PySpark, die eine parallel zu Ihrem Code laufende Java-Umgebung benötigen, lassen sich in einer UDF nicht verwenden: `SparkContext`, `RDD`, `pyspark.streaming` und der Großteil der RDD-basierten `pyspark.mllib`-API können nicht importiert werden, und ein Spark-DataFrame kann nicht an statsforecast oder Fugue übergeben werden.

## Spark-Cluster
Standardmäßig ist der Spark-Cluster in Workspaces nicht aktiviert.  Um den Spark-Cluster zu aktivieren, öffnen Sie die App für die Workspace-Verwaltung und aktivieren Sie den Dienst „Spark Compute Cluster“.

Nach der Aktivierung können Spark-Jobs an den Cluster übermittelt werden.

Der Cluster kann über die Subdomain `spark` des Workspace überwacht werden (z. B. `https://spark.my_workspace.plaid.cloud`)
