---
title: Pierwsze kroki z PySpark
description: Zacznij korzystać z PySpark w PlaidCloud do rozproszonego przetwarzania danych w funkcjach zdefiniowanych przez użytkownika i Notebookach Jupyter.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/pyspark/getting-started.md
---

## Dokumentacja PySpark
PySpark działa podobnie do Pandas, ale umożliwia obliczenia rozproszone i nie jest ograniczony pamięcią RAM.  PySpark jest dostępny zarówno w UDF, jak i w Notebookach Jupyter.

UDF korzysta z klastra Spark przez Spark Connect, za pomocą interfejsu DataFrame i SQL PySpark (`pyspark.sql`). Nie można używać elementów PySpark, które wymagają działającej obok kodu Javy: nie można zaimportować `SparkContext`, `RDD`, `pyspark.streaming` ani większości interfejsu `pyspark.mllib` opartego na RDD, a DataFrame Spark nie może być przekazany do statsforecast ani Fugue.

## Klaster Spark
Domyślnie w obszarach roboczych klaster Spark nie jest włączony.  Aby go aktywować, przejdź do aplikacji do zarządzania obszarem roboczym i włącz usługę „Spark Compute Cluster".

Po aktywacji zadania Spark można przesyłać do klastra.

Klaster można monitorować w poddomenie `spark` obszaru roboczego (np. `https://spark.my_workspace.plaid.cloud`)
