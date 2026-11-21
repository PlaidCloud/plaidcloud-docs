---
title: 내보내기 단계
description: 프로젝트 테이블을 파일 형식, 문서 계정, 외부 데이터베이스 등 외부 대상에 기록하는 워크플로 단계입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/index.md
---

프로젝트 테이블을 파일 형식, 문서 계정, 외부 데이터베이스 등 외부 대상에 기록하는 워크플로 단계입니다.

## 단계

- [테이블 보관](/ko/reference/workflow-steps/export/archive-tables/)
- [Export External Database Tables 단계](/ko/reference/workflow-steps/export/export-external-tables/)
- [Kafka 내보내기](/ko/reference/workflow-steps/export/export-kafka/)
- [MongoDB 내보내기](/ko/reference/workflow-steps/export/export-mongodb/)
- [프로젝트 아카이브 내보내기](/ko/reference/workflow-steps/export/export-project-archive/)
- [Export Project Table 단계](/ko/reference/workflow-steps/export/export-project-table/)
- [Export Quandl 단계](/ko/reference/workflow-steps/export/export-quandl/)
- [SQL 내보내기](/ko/reference/workflow-steps/export/export-sql/)
- [Export Templated 단계](/ko/reference/workflow-steps/export/export-templated/)
- [Export to Avro 단계](/ko/reference/workflow-steps/export/export-to-avro/)
- [Export to CSV 단계](/ko/reference/workflow-steps/export/export-to-csv/)
- [Export to Excel 단계](/ko/reference/workflow-steps/export/export-to-excel/)
- [Export to Excel Sheets 단계](/ko/reference/workflow-steps/export/export-to-excel-sheets/)
- [Export to Google Spreadsheet 단계](/ko/reference/workflow-steps/export/export-to-google-spreadsheet/)
- [Export to HDF 단계](/ko/reference/workflow-steps/export/export-to-hdf/)
- [Export to JSON 단계](/ko/reference/workflow-steps/export/export-to-json/)
- [Export to ORC 단계](/ko/reference/workflow-steps/export/export-to-orc/)
- [Export to Parquet 단계](/ko/reference/workflow-steps/export/export-to-parquet/)
- [Export to PDF 단계](/ko/reference/workflow-steps/export/export-to-pdf/)
- [Export to Table Archive 단계](/ko/reference/workflow-steps/export/export-to-table-archive/)
- [Export to XML 단계](/ko/reference/workflow-steps/export/export-to-xml/)
- [문서 전기](/ko/reference/workflow-steps/export/post-documents/) — 설정한 모든 ERP 시스템에 문서 테이블을 전기합니다
- [공간 파일 내보내기](/ko/reference/workflow-steps/spatial/spatial-file-export/)
- [Publish to Tableau 단계](/ko/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export 단계](/ko/reference/workflow-steps/export/export-hyper/)

## 기록되는 열

대부분의 내보내기 단계는 데이터 매퍼에 대상 열이 없으면, 즉 **열** 탭의 오른쪽 테이블이 비어 있으면 단계를 실행하는 시점의 소스 테이블 열을 테이블의 열 순서대로 모두 기록합니다. 따라서 구성이 덜 끝난 단계는 실패하는 대신 테이블 전체를 대상으로 내보내므로, 외부 대상으로 내보내기를 실행하기 전에 데이터 매퍼를 확인하십시오.

매핑된 열이 없고 소스 테이블에도 열이 없으면 CSV, JSON, SQL, Excel, PDF, Google 스프레드시트 또는 Kafka 내보내기는 아무것도 기록하지 않고 경고와 함께 완료됩니다. XML, Parquet, ORC, Avro 또는 Excel Sheets처럼 여러 테이블을 내보내는 경우에는 해당 테이블 이름을 밝힌 경고와 함께 그 테이블을 건너뜁니다.
