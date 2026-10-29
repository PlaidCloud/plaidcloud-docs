---
title: 가져오기 단계
description: 외부 소스의 데이터를 프로젝트 테이블로 가져오는 워크플로 단계입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/index.md
---

외부 소스의 데이터를 프로젝트 테이블로 가져오는 워크플로 단계입니다.

파일 가져오기는 실행하기 전에 대상 테이블을 로드하는 쿼리를 검사합니다. 유형이 지정된 열에 대한 일반 SQL 문 이외의 내용이 포함된 쿼리는 대상 테이블이 생성, 교체 또는 로드되기 전에 거부되므로, 테이블은 이전 상태 그대로 유지됩니다.

소스 파일이 없는 것은 오류가 아닙니다. 가져오기는 경로를 명시한 경고를 표시하고 선언된 열이 있는 빈 대상 테이블을 그대로 두므로, 이후 단계는 행을 0개 읽습니다. 이는 CSV, Excel, JSON, 고정 너비, YXDB, dBASE, ORC, Avro, Parquet, XML, Db2 추출 가져오기에 적용됩니다. 태그가 지정된 XML 가져오기는 필드를 선언한 태그에 대해서만 빈 테이블을 생성합니다. 아카이브 및 Access 가져오기도 경고하지만 열을 선언하지 않으므로 테이블을 생성하지 않습니다. 문서 검색으로 파일을 찾는 아카이브 가져오기는 파일 누락 경고를 표시하지 않습니다.

단계가 실행되기 전에도 마찬가지입니다. 파일 가져오기 매핑의 **채우기**와, REST API 또는 AI 어시스턴트를 통한 파일 열 읽기는 파일이 없거나 비어 있을 때 오류 대신 경로를 명시한 경고와 함께 *채울 항목이 없습니다*(API에서는 빈 열 목록)라고 응답합니다. 문서에서 새 테이블이나 단계로 없는 파일을 가져오면 아무것도 생성되지 않으며, 파일은 **건너뜀**으로 표시되고 경로를 명시한 경고가 표시됩니다.

## 단계

- [Access 가져오기](/ko/reference/workflow-steps/import/import-access/)
- [Alteryx YXDB 가져오기](/ko/reference/workflow-steps/import/import-alteryx-yxdb/)
- [아카이브 가져오기](/ko/reference/workflow-steps/import/import-archive/)
- [Avro 가져오기](/ko/reference/workflow-steps/import/import-avro/)
- [CSV 가져오기](/ko/reference/workflow-steps/import/import-csv/)
- [Delta Lake 가져오기](/ko/reference/workflow-steps/import/import-delta/)
- [DB2 추출 가져오기](/ko/reference/workflow-steps/import/import-db2-extract/)
- [Import dBASE 단계](/ko/reference/workflow-steps/import/import-dbf/)
- [Excel 가져오기](/ko/reference/workflow-steps/import/import-excel/)
- [Import Delimited 단계](/ko/reference/workflow-steps/import/import-delimited/)
- [외부 데이터베이스 테이블 가져오기](/ko/reference/workflow-steps/import/import-external-database-tables/)
- [고정 너비 가져오기](/ko/reference/workflow-steps/import/import-fixed-width/)
- [Import Google BigQuery 단계](/ko/reference/workflow-steps/import/import-google-bigquery/)
- [Google 스프레드시트 가져오기](/ko/reference/workflow-steps/import/import-google-spreadsheet/)
- [Import HDF 단계](/ko/reference/workflow-steps/import/import-hdf/)
- [JSON 가져오기](/ko/reference/workflow-steps/import/import-json/)
- [Kafka 가져오기](/ko/reference/workflow-steps/import/import-kafka/)
- [Monday 가져오기](/ko/reference/workflow-steps/import/import-monday/)
- [MongoDB 가져오기](/ko/reference/workflow-steps/import/import-mongodb/)
- [ORC 가져오기](/ko/reference/workflow-steps/import/import-orc/)
- [Parquet 가져오기](/ko/reference/workflow-steps/import/import-parquet/)
- [Import Project Table 단계](/ko/reference/workflow-steps/import/import-project-table/)
- [Import Quandl 단계](/ko/reference/workflow-steps/import/import-quandl/)
- [Import Singer Source 단계](/ko/reference/workflow-steps/import/import-singer/)
- [Import SPSS 단계](/ko/reference/workflow-steps/import/import-spss/)
- [SQL 가져오기](/ko/reference/workflow-steps/import/import-sql/)
- [Import Stata 단계](/ko/reference/workflow-steps/import/import-stata/)
- [XML 가져오기](/ko/reference/workflow-steps/import/import-xml/)
- [테이블 복원](/ko/reference/workflow-steps/import/restore-tables/)
