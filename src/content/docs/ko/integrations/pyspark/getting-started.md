---
title: PySpark 시작하기
description: PlaidCloud에서 사용자 정의 함수와 Jupyter 노트북 안에서 분산 데이터 처리를 위해 PySpark를 사용하는 방법을 시작합니다.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/pyspark/getting-started.md
---

## PySpark 문서
PySpark는 Pandas와 비슷하게 사용하지만 분산 컴퓨팅을 지원하며 RAM 용량에 제한받지 않습니다.  PySpark는 UDF와 Jupyter 노트북 모두에서 사용할 수 있습니다.

UDF는 Spark Connect를 통해 Spark 클러스터를 사용하며, PySpark의 DataFrame 및 SQL API(`pyspark.sql`)를 사용합니다. 코드와 함께 Java를 실행해야 하는 PySpark 기능은 UDF에서 사용할 수 없습니다. `SparkContext`, `RDD`, `pyspark.streaming` 및 RDD 기반 `pyspark.mllib` API의 대부분은 가져올 수 없으며, Spark DataFrame을 statsforecast나 Fugue에 전달할 수도 없습니다.

## Spark 클러스터
기본적으로 워크스페이스에서는 Spark 클러스터가 사용 설정되어 있지 않습니다.  Spark 클러스터를 활성화하려면 워크스페이스 관리 앱으로 이동하여 "Spark Compute Cluster" 서비스를 사용 설정하십시오.

활성화한 후에는 클러스터에 Spark 작업을 제출할 수 있습니다.

클러스터는 워크스페이스의 `spark` 하위 도메인(예: `https://spark.my_workspace.plaid.cloud`)에서 모니터링할 수 있습니다.
