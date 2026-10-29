---
title: Apache Spark
description: PlaidCloud에서 Apache Spark 데이터베이스 연결을 설정하여 분산 쿼리를 실행하고 빅데이터를 워크플로에 통합합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/spark.md
---

**Apache Spark**는 대규모 데이터 세트에 대한 ETL에 흔히 사용되는 분산 컴퓨팅 엔진입니다. 이 커넥터를 사용하여 Spark SQL 엔드포인트(일반적으로 Spark Thrift Server)를 통해 데이터를 읽고 쓸 수 있습니다. Databricks에서 관리하는 Spark에는 [Azure Databricks](../azure-databricks/) 커넥터를 사용하는 것이 좋습니다.

## 업스트림 문서
[Apache Spark 문서](https://spark.apache.org/documentation.html).

[Apache 프로젝트](https://spark.apache.org/).

## 설정

이 커넥터는 공급업체별 인증 흐름을 사용하며, 워크스페이스의 **연결** 화면에서 직접 구성합니다. 표시되는 구성 필드는 테넌트 관리자가 해당 통합을 위해 프로비저닝한 자격 증명에 따라 달라집니다.

최신 설정 세부 정보는 업스트림 [spark 문서](https://spark.apache.org/docs/latest/)를 참조하십시오.

이 커넥터를 테넌트에 설정하는 데 도움이 필요하면 계정 담당 팀에 문의하십시오. 커넥터별 자격 증명, 환경 URL, 필요한 사전 프로비저닝은 일반적으로 PlaidCloud 지원팀과 조율해야 합니다.
