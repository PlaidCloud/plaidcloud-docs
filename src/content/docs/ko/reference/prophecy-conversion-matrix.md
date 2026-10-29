---
title: Prophecy 변환 매트릭스
description: PlaidCloud가 Prophecy 파이프라인과 SQL 프로젝트를 네이티브 고급 워크플로 단계로 변환하는 방식과 젬별 지원 상태를 설명합니다.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/prophecy-conversion-matrix.md
---

PlaidCloud는 Prophecy Spark 파이프라인과 SQL 프로젝트를 네이티브
고급 워크플로로 변환합니다. 가져오기 도구는 각 Prophecy 젬을 워크플로 단계,
프로젝트 변수 또는 캔버스 개체에 매핑하므로, 변환된 워크플로는 에뮬레이션이
아니라 클라우드 네이티브로 실행됩니다.

모든 젬, 커넥터, 프로젝트 구조가 변환됩니다. **전체**는 젬이
해당 젬의 작업을 수행하는 네이티브 PlaidCloud 단계, 변수 또는 캔버스 개체가
된다는 뜻입니다. 변환된 워크플로가 자체적으로 재현하지 않는 몇 가지 동작은
[알려진 예외 사례](#알려진-예외-사례)에 나열되어 있으며, 각 항목에 대처 방법이
함께 설명되어 있습니다.

변환을 실행하려면 [Prophecy 프로젝트 마이그레이션](/ko/guides/workflows/migrate-prophecy-projects/)을 참조하십시오.

## Spark 파이프라인 젬

### 소스/대상

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Lookup | 전체 | [Lookup](/ko/reference/workflow-steps/tables/table-lookup/) | 각 조회 호출은 이를 사용하는 단계 안의 Lookup 단계가 됩니다. 일치하는 항목이 없는 키는 NULL을 읽고, 중복된 키는 해당 행 중 하나를 반환합니다. |
| Source | 전체 | 데이터세트 형식에 따라 선택되는 가져오기 단계([커넥터](#커넥터) 참조) | 각 Source는 데이터세트 이름을 딴 테이블로 가져오는 가져오기 단계가 됩니다. 변환기가 인식하지 못하는 형식은 워크플로의 문서 폴더에 업로드된 CSV 파일로 읽으며 경고가 표시됩니다. |
| Streaming Source | 전체 | 배치 Source와 동일한 가져오기 | 스트리밍 소스는 경고와 함께 일회성 배치 가져오기로 변환됩니다. |
| Streaming Target | 전체 | 배치 추가 로드 | 스트리밍 대상은 경고와 함께 배치 추가로 변환됩니다. |
| Target | 전체 | 데이터세트 형식과 writeMode에 따라 선택되는 테이블 내보내기/로드 단계 | 각 Target은 젬의 쓰기 모드(추가, 덮어쓰기, SET 식을 사용하는 병합, 업서트, SCD2, replaceWhere, insertInto)에 맞는 테이블 로드 또는 내보내기 단계가 됩니다. |

### 준비

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Data Cleansing | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계의 열 식 | null 채우기, 공백 제거, 대소문자 옵션을 열 식으로 변환하며, 정리된 열은 맨 뒤로 이동합니다. |
| Sequence | 전체 | 행 번호 식을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 시작 값과 증분으로 시퀀스 열을 추가합니다. |
| Surrogate Key Generator | 전체 | 행 번호 식을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 초기 값부터 순차 키를 추가합니다. 마지막으로 발급한 키를 저장한 테이블에서 실행 간에 키가 이어집니다. |

### 변환

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Aggregate | 전체 | 집계를 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계. 젬이 피벗하는 경우 [Pivot](/ko/reference/workflow-steps/tables/table-pivot/) | 그룹화하고 집계하며, HAVING 조건을 적용하고, 피벗 값마다 하나의 열로 피벗합니다. propagate-all은 다른 모든 입력 열을 함께 가져옵니다. |
| Bulk Column Expressions | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계에서 열마다 하나의 식으로 확장 | 나열된 열마다 Table Extract 단계의 식 하나가 됩니다. 젬의 레이아웃을 가정했다는 경고가 표시됩니다. |
| Bulk Column Rename | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계의 열 이름 바꾸기 | 나열된 열마다 Table Extract 단계의 이름 바꾸기 하나가 됩니다. 젬의 레이아웃을 가정했다는 경고가 표시됩니다. |
| Deduplicate | 전체 | distinct 또는 행 번호 필터를 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 키마다 한 행을 유지합니다. distinct, 사용자의 정렬 순서에 따른 첫 번째 또는 마지막 행, 임의의 행, 또는 한 번만 나타나는 키만 유지할 수 있습니다. |
| Dynamic Replace | 전체 | 직접 구성하는 동적 바꾸기 변환 | 동적 바꾸기 변환의 바꾸기 규칙으로 변환됩니다. 젬의 레이아웃을 가정했다는 경고가 표시됩니다. |
| Dynamic Select | 전체 | 유형별로 확인되는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계의 열 선택 | 변환 시점에 유형별로 열을 확인하여 명시적인 선택으로 만듭니다. |
| Filter | 전체 | 필터 식을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 필터 식을 사용하는 Table Extract 단계로 변환됩니다. NULL 조건은 행을 제외합니다. |
| Flatten Schema | 전체 | [JSON 구문 분석](/ko/reference/workflow-steps/tables/table-json-parse/) 및 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) | 중첩 필드를 젬의 구분자로 이름 붙인 열로 평탄화하고, 배열을 요소당 한 행으로 분해합니다. |
| Fuzzy Match | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 및 [User Defined Transform](/ko/reference/workflow-steps/general/user-defined-transform/) | 레코드를 짝짓고, 젬의 방법으로 각 일치 필드의 점수를 매기고, 점수를 평균하여, 임계값 이상인 쌍만 유지합니다. |
| Group By Rollup | 전체 | 롤업 수준마다 집계 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계를 유니온한 것 | 롤업을 그룹화 수준마다 하나의 집계로 확장하고, NULL 소계와 함께 유니온합니다. |
| Limit | 전체 | 행 제한을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 행 제한으로 변환됩니다. 구성 참조는 프로젝트 변수가 됩니다. |
| Normalize | 전체 | 분해 식을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 길이 식에 따라 각 레코드를 반복하고, 인덱스마다 출력 열을 계산하며, 종료 조건이 성립하는 첫 인덱스에서 멈춥니다. |
| Order By | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계의 정렬 | 동일한 키, 방향, null 위치를 가진 정렬로 변환됩니다. |
| Reformat | 전체 | 열 식을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 출력 열마다 하나의 식을 가진 Table Extract 단계로 변환됩니다. 나열되지 않은 열은 제외됩니다. |
| Sample Rows | 전체 | 행 제한 또는 무작위 샘플을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 행의 무작위 비율 또는 개수를 유지합니다. 샘플링이 무작위이므로 선택되는 행은 Spark 실행과 다릅니다. |
| Schema Transform | 전체 | 순서대로 적용되는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계의 체인 | 열 추가 또는 바꾸기, 삭제, 이름 바꾸기, 없을 때 기본값으로 추가, 프로젝트 비즈니스 규칙 추가 등 각 작업을 순서대로 적용합니다. |
| Set Operation | 전체 | [Union All](/ko/reference/workflow-steps/tables/table-union-all/). except는 [안티 조인](/ko/reference/workflow-steps/tables/table-anti-join/). intersect는 [내부 조인](/ko/reference/workflow-steps/tables/table-inner-join/) | Union all은 입력을 쌓습니다. except all과 intersect all은 올바른 수의 중복 행을 유지합니다. |
| TransposeAgg | 전체 | 집계를 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 젬의 그룹화, 집계, 피벗을 Aggregate로 변환하며, 검토하라는 경고가 표시됩니다. |
| Unpivot | 전체 | [Melt](/ko/reference/workflow-steps/tables/table-melt/) | 선택한 열을 이름 열과 값 열로 쌓습니다. |
| Watermark | 전체 | 단계 필요 없음 | 제거됨: 배치 실행은 존재하는 모든 데이터를 읽으므로 적용할 지연 데이터 기준이 없습니다. |
| Window Function | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계의 윈도 식 | 젬의 파티션, 정렬, 프레임(행 또는 범위), 무제한/현재 행/오프셋 경계로 윈도 열을 추가합니다. |

### 조인/분할

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Compare Columns | 전체 | 전체 외부 조인과 열별 집계 | 피벗 해제된 데이터의 전체 외부 조인을 통해 일치 및 불일치 개수와 함께 열을 비교합니다. |
| Join | 전체 | [내부 조인](/ko/reference/workflow-steps/tables/table-inner-join/), [다중 테이블 조인](/ko/reference/workflow-steps/tables/table-multi-table-join/), [안티 조인](/ko/reference/workflow-steps/tables/table-anti-join/) 또는 [교차 조인](/ko/reference/workflow-steps/tables/table-cross-join/) | 임의의 조인 조건에서 내부, 왼쪽, 오른쪽, 전체, 세미, 안티, 교차, 자연 조인 등 각 유형의 조인을 구성하고, where 절을 적용하며, 선택 목록을 씁니다. |
| Repartition | 전체 | 단계 필요 없음 | 제거됨: PlaidCloud가 파티셔닝을 관리하므로 다음 단계가 업스트림 테이블을 직접 읽습니다. |
| Row Distributor | 전체 | 출력마다 하나의 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 필터 | 출력마다 하나의 필터로 변환됩니다. 행은 여러 출력에 들어갈 수 있습니다. |

### 구문 분석

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Column Parser | 전체 | [JSON 구문 분석](/ko/reference/workflow-steps/tables/table-json-parse/) / [XML 구문 분석](/ko/reference/workflow-steps/tables/table-xml-parse/) | 지정한 열의 JSON 또는 XML 구문 분석으로 변환됩니다. 젬의 레이아웃을 가정했다는 경고가 표시됩니다. |

### 사용자 지정

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Custom Gem (Gem Builder) | 전체 | 젬이 생성한 코드를 실행하는 [User Defined Transform](/ko/reference/workflow-steps/general/user-defined-transform/) | 파이프라인 내보내기에 있는 젬이 생성한 PySpark 코드가 Python 단계에서 실행되며, 검토하라는 경고가 표시됩니다. |
| CustomReformatBitbucket | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) | 젬이 가진 식을 사용하는 Reformat으로 변환되며, 검토하라는 경고가 표시됩니다. |
| Data Quality Check | 전체 | 검사당 한 결과 행을 [Union All](/ko/reference/workflow-steps/tables/table-union-all/)한 것. 실패 시 중지하려면 [워크플로 오류 발생](/ko/reference/workflow-steps/workflow-control/raise-workflow-error/) | 입력에 대해 각 검사를 평가하고 검사마다 상태와 메시지가 포함된 결과 행을 하나씩 씁니다. 데이터는 그대로 전달되며, 젬의 실패 임계값에 도달하면 실행이 중지됩니다. |
| Deequ | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 검사 | 데이터를 그대로 전달하고 isComplete, isUnique, isNonNegative, isContainedIn 규칙에 대한 제약 조건 결과 테이블을 만듭니다. |
| Delta Table Operations | 전체 | [Table In-Place Delete](/ko/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/ko/reference/workflow-steps/tables/table-update/), [Table Drop](/ko/reference/workflow-steps/tables/table-drop/), [Table Restore to Timestamp](/ko/reference/workflow-steps/tables/table-restore-timestamp/) | 삭제, 업데이트, 드롭, 타임스탬프로 복원은 테이블 단계에 매핑됩니다. 최적화, vacuum, 버전으로 복원은 경고와 함께 데이터를 그대로 전달합니다. |
| Directory | 전체 | [디렉터리 목록](/ko/reference/workflow-steps/document/directory-listing/) | 바인딩된 문서 폴더의 파일을 젬의 열로 나열합니다. 시트 이름 옵션을 사용하면 각 통합 문서가 시트마다 한 행씩 생성됩니다. 폴더가 없으면 행이 0개입니다. |
| Email | 전체 | [Notify Via Email](/ko/reference/workflow-steps/notifications/notify-via-email/) | 바인딩된 이메일 연결을 통해 선택적 데이터 첨부와 함께 이메일을 보냅니다. |
| Email Data | 전체 | [Notify Via Email](/ko/reference/workflow-steps/notifications/notify-via-email/) | 입력 행을 테이블로 이메일로 보내고 입력은 변경 없이 그대로 전달합니다. |
| File Operation | 전체 | [Copy Document File](/ko/reference/workflow-steps/document/copy-document-file/) 또는 [Copy Document Directory](/ko/reference/workflow-steps/document/copy-document-directory/) | 바인딩된 문서 폴더의 파일을 변환된 워크플로의 문서 폴더로 복사, 이동 또는 동기화합니다. 이동하면 원본 파일이 삭제됩니다. |
| Log | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) | 젬의 이벤트 행(시간, 젬 이름, 이벤트 유형, 텍스트)을 출력 테이블에 씁니다. |
| REST API Enrich | 전체 | [REST 요청](/ko/reference/workflow-steps/general/rest-request/) | 행마다 한 번씩 API를 호출하고 응답 열을 추가합니다. |
| Script | 전체 | 프레임 접근 재작성이 적용된 Python 단계 | 스크립트 본문을 python 단계에 포함하며 데이터 프레임 접근이 다시 작성됩니다. Scala 본문은 참고 사항과 함께 보존됩니다. |
| Soda Data Quality Check | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 검사 | Soda 검사에서 검사 결과 테이블을 만듭니다. |
| SQL Statement | 전체 | 출력 탭마다 SQL 단계. 텍스트는 테넌트 방언으로 번역됨 | 각 탭을 SQL 단계로 포함하며 입력은 임시 테이블로 바인딩됩니다. 테넌트 방언으로 번역됩니다. |
| Todo | 전체 | [워크플로 오류 발생](/ko/reference/workflow-steps/workflow-control/raise-workflow-error/) 또는 [Notify via Log](/ko/reference/workflow-steps/notifications/notify-via-log/) | 아직 작성되지 않은 로직을 표시합니다. 이를 읽는 항목이 없으면 로그 메시지가 되고, 이후 단계가 이에 의존하면 젬의 메시지와 함께 실행을 중지하는 단계가 됩니다. |

### 보고서

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Tableau | 전체 | [Publish to Tableau](/ko/reference/workflow-steps/export/export-to-tableau/) | Hyper 추출을 쓰고 바인딩된 Tableau 연결에 게시합니다. |

### ML/AI

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Bedrock | 전체 | [Text NLP AI](/ko/reference/workflow-steps/text-documents/nlp-ai/) | 워크스페이스 AI 연결을 통해 텍스트 열을 임베딩합니다. |
| OpenAI | 전체 | [Text NLP AI](/ko/reference/workflow-steps/text-documents/nlp-ai/) | 워크스페이스 AI 연결을 통해 질문에 답하거나 텍스트를 임베딩합니다. |
| Pinecone Lookup | 전체 | [REST 요청](/ko/reference/workflow-steps/general/rest-request/) | 행마다 Pinecone 인덱스를 쿼리하고 pinecone_matches 및 pinecone_error 열을 추가합니다. |
| SageMaker Endpoint | 전체 | [Text NLP AI](/ko/reference/workflow-steps/text-documents/nlp-ai/) | 워크스페이스 AI 연결을 통해 질문에 답합니다. |
| Text Processing | 전체 | 청크 분할은 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/). 웹 스크래핑은 [REST 요청](/ko/reference/workflow-steps/general/rest-request/) | 청크 분할은 문자 청크 식이 되고, 웹 스크래핑은 각 행의 URL을 가져와 페이지 콘텐츠를 행에 다시 조인합니다. |

### 서브그래프/제어

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Control Flow Input | 전체 | 제거됨(경계 표시 전용) | 제거됩니다. 반복기 하위 워크플로의 입력 경계만 표시합니다. |
| Control Flow Output | 전체 | 제거됨(경계 표시 전용) | 제거됩니다. 반복기 하위 워크플로의 출력 경계만 표시합니다. |
| Subgraph (Basic) | 전체 | 인라인 프로세스에서 만든 캔버스 컨테이너 / 중첩 워크플로 | 인라인 내부 그래프를 입력/출력 테이블 매개변수를 가진 중첩 워크플로(또는 인라인 단계)로 변환합니다. |
| Table Iterator | 전체 | [Workflow Loop](/ko/reference/workflow-steps/workflow-control/workflow-loop/) | 입력 행마다 루프 본문을 한 번씩 실행하며, 각 구성 값을 해당 열에서 설정하고 maxIteration까지 반복합니다. |
| While Iterator | 전체 | [Workflow Loop](/ko/reference/workflow-steps/workflow-control/workflow-loop/) | 패스마다 루프 본문을 한 번씩 실행하며 반복 횟수를 전달하고, 본문이 행을 반환하지 않거나 젬의 최대값에 도달할 때까지 계속합니다. |

## SQL / 분석가 젬

### 소스/대상

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| External table Source/Target (BigQuery, Databricks, SAP HANA, MongoDB, MSSQL, Oracle, Postgres, Redshift, Salesforce, Snowflake, Synapse) | 전체 | 해당 데이터베이스 연결을 사용하는 외부 데이터 가져오기/내보내기 단계 | PlaidCloud 연결을 통해 외부 데이터베이스의 테이블을 읽거나 씁니다. |
| File storage Source/Target (ADLS, Databricks Volumes, GCS, OneDrive, S3, SFTP, SharePoint, Smartsheet) | 전체 | 문서 계정(ADLS/GCS/S3/SFTP/SharePoint/OneDrive)에 대한 파일 가져오기/내보내기 단계 | 와일드카드 유니온, 트리거, 삭제/이동, 암호화 옵션과 함께 클라우드/SFTP 스토리지의 파일을 읽거나 씁니다. |
| Model | 전체 | 업스트림 단계 출력 테이블 | 다른 모델을 참조된 업스트림 단계가 생성한 테이블로 읽습니다. |
| Seed | 전체 | [가져오기: CSV](/ko/reference/workflow-steps/import/import-csv/) | 시드 CSV가 PlaidCloud 테이블로 가져와집니다. |
| Source | 전체 | 데이터세트 형식에 따라 선택되는 가져오기 단계([커넥터](#커넥터) 참조) | 각 Source는 데이터세트 이름을 딴 테이블로 가져오는 가져오기 단계가 됩니다. 변환기가 인식하지 못하는 형식은 워크플로의 문서 폴더에 업로드된 CSV 파일로 읽으며 경고가 표시됩니다. |
| Target Model / Table (Target) | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/), [Upsert](/ko/reference/workflow-steps/tables/table-upsert/), [테이블 복사](/ko/reference/workflow-steps/tables/table-copy/), [Union All](/ko/reference/workflow-steps/tables/table-union-all/) | 모델의 최종 select를 바꾸기, 추가, 업서트, 삭제 후 삽입, SCD2 또는 조건자로 바꾸기 방식으로 PlaidCloud 테이블에 씁니다. |
| Upload Files | 전체 | [가져오기: CSV](/ko/reference/workflow-steps/import/import-csv/) | 업로드된 로컬 파일이 가져오기 단계를 통해 테이블이 됩니다. |

### 준비

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Data Cleansing | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계의 열 식 | null 채우기, 공백 제거, 대소문자 옵션을 열 식으로 변환하며, 정리된 열은 맨 뒤로 이동합니다. |
| Data Masking | 전체 | 문자 마스킹 또는 해싱을 위한 열 식 | 선택한 문자열 열을 제자리에서 또는 새 열로 마스킹하거나 해시합니다. |
| Find Duplicates | 전체 | 행 번호 윈도 식과 필터 | 키별로 고유 행, 중복 행 또는 개수/위치로 선택한 행을 반환합니다. |
| Generate Rows | 전체 | 입력 행마다 조인하고 필터링한 시퀀스 테이블 | init, condition, loop 식으로 입력 행마다 행을 생성합니다. |
| Imputation | 전체 | 집계와 조인 백, 열 식 | null 또는 센티널 값을 평균, 중앙값, 최빈값 또는 고정 값으로 바꿉니다. |
| Multi-Column Edit | 전체 | 템플릿에서 확장된 열별 식 | 하나의 식 템플릿을 선택한 모든 열에 적용합니다. |
| Multi-Column Rename | 전체 | 선택 단계의 열 이름 바꾸기 매핑 | 접두사, 접미사 또는 이름 식으로 선택한 열의 이름을 바꿉니다. |
| Record ID | 전체 | 행 번호 또는 uuid 열 식 | UUID 또는 순차 레코드 ID 열을 추가합니다. |
| Sample | 전체 | 추출 단계의 행 제한 또는 샘플 옵션 | 전체 또는 그룹별로 처음/마지막/무작위/N번째/백분율 행을 가져옵니다. |
| Tile | 전체 | 타일 번호와 시퀀스를 위한 윈도 식 | 동일 합계, 동일 개수, 표준 편차 구간, 고유 값 또는 수동 기준값으로 타일 번호를 할당합니다. |

### 변환

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Aggregate | 전체 | 집계를 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계. 젬이 피벗하는 경우 [Pivot](/ko/reference/workflow-steps/tables/table-pivot/) | 그룹화하고 집계하며, HAVING 조건을 적용하고, 피벗 값마다 하나의 열로 피벗합니다. propagate-all은 다른 모든 입력 열을 함께 가져옵니다. |
| Count Records | 전체 | 개수 함수를 사용하는 Aggregate 단계 | 전체, null이 아닌 값 또는 고유 값의 개수를 한 행으로 반환합니다. |
| Data Encoder/Decoder | 전체 | base64/hex 인코딩 및 디코딩을 위한 열 식 | 선택한 열을 인코딩하거나 디코딩합니다. AES는 Databricks에서만 지원됩니다. |
| Deduplicate | 전체 | distinct 또는 행 번호 필터를 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 키마다 한 행을 유지합니다. distinct, 사용자의 정렬 순서에 따른 첫 번째 또는 마지막 행, 임의의 행, 또는 한 번만 나타나는 키만 유지할 수 있습니다. |
| Dynamic Select | 전체 | 유형별로 확인되는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계의 열 선택 | 변환 시점에 유형별로 열을 확인하여 명시적인 선택으로 만듭니다. |
| Filter | 전체 | 필터 식을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 필터 식을 사용하는 Table Extract 단계로 변환됩니다. NULL 조건은 행을 제외합니다. |
| Finance | 전체 | 재무 함수를 구현하는 열 식 | 재무 함수 결과(FV, PV, NPV, IRR 등)를 새 열로 추가합니다. |
| Flatten Schema | 전체 | [JSON 구문 분석](/ko/reference/workflow-steps/tables/table-json-parse/) 및 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) | 중첩 필드를 젬의 구분자로 이름 붙인 열로 평탄화하고, 배열을 요소당 한 행으로 분해합니다. |
| Fuzzy Match | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 및 [User Defined Transform](/ko/reference/workflow-steps/general/user-defined-transform/) | 레코드를 짝짓고, 젬의 방법으로 각 일치 필드의 점수를 매기고, 점수를 평균하여, 임계값 이상인 쌍만 유지합니다. |
| Limit | 전체 | 행 제한을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 행 제한으로 변환됩니다. 구성 참조는 프로젝트 변수가 됩니다. |
| Order By | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계의 정렬 | 동일한 키, 방향, null 위치를 가진 정렬로 변환됩니다. |
| Pivot | 전체 | [Pivot](/ko/reference/workflow-steps/tables/table-pivot/) | 선택한 피벗 값을 집계 열로 바꿉니다. 설계 시점에 가져온 Simple 모드의 값 목록은 나열된 값으로 변환됩니다. |
| Reformat | 전체 | 열 식을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 출력 열마다 하나의 식을 가진 Table Extract 단계로 변환됩니다. 나열되지 않은 열은 제외됩니다. |
| Running Total | 전체 | 누적 합계 윈도 식 열 | 선택한 열마다 누적 합계를 추가합니다. |
| Snowflake Unpivot (third-party) | 전체 | [Melt](/ko/reference/workflow-steps/tables/table-melt/) | Snowflake UNPIVOT으로 열을 피벗 해제합니다. |
| Transpose | 전체 | [Melt](/ko/reference/workflow-steps/tables/table-melt/) | 데이터 열을 이름 열과 문자열 값 열로 쌓습니다. |
| TransposeAgg | 전체 | 집계를 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 젬의 그룹화, 집계, 피벗을 Aggregate로 변환하며, 검토하라는 경고가 표시됩니다. |
| Unpivot | 전체 | [Melt](/ko/reference/workflow-steps/tables/table-melt/) | 데이터 열을 이름 열과 값 열로 쌓습니다. |
| Weighted Average | 전체 | 가중 평균 식을 사용하는 Aggregate 단계 | 전체 또는 그룹별로 가중 평균을 계산합니다. |
| Window Function | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계의 윈도 식 | 젬의 파티션, 정렬, 프레임(행 또는 범위), 무제한/현재 행/오프셋 경계로 윈도 열을 추가합니다. |

### 조인/분할

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Except | 전체 | 모든 열에 대한 [안티 조인](/ko/reference/workflow-steps/tables/table-anti-join/)과 distinct [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) | 다른 어떤 입력에도 나타나지 않는 첫 번째 입력의 행을 유지합니다. |
| Intersect | 전체 | 모든 열에 대한 [내부 조인](/ko/reference/workflow-steps/tables/table-inner-join/)과 Distinct | 모든 입력에 있는 행을 유지합니다. |
| Join | 전체 | [내부 조인](/ko/reference/workflow-steps/tables/table-inner-join/), [다중 테이블 조인](/ko/reference/workflow-steps/tables/table-multi-table-join/), [안티 조인](/ko/reference/workflow-steps/tables/table-anti-join/) 또는 [교차 조인](/ko/reference/workflow-steps/tables/table-cross-join/) | 임의의 조인 조건에서 내부, 왼쪽, 오른쪽, 전체, 세미, 안티, 교차, 자연 조인 등 각 유형의 조인을 구성하고, where 절을 적용하며, 선택 목록을 씁니다. |
| Union | 전체 | [Union All](/ko/reference/workflow-steps/tables/table-union-all/) | 위치를 기준으로 입력을 쌓으며, 젬이 중복을 유지하지 않는 경우 중복을 제거합니다. |
| Union By Name | 전체 | [Union All](/ko/reference/workflow-steps/tables/table-union-all/) | 열을 이름으로 맞추고 누락된 열은 null로 채우는 Union All이 됩니다. |

### 구문 분석

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| JSON Parse | 전체 | [JSON 구문 분석](/ko/reference/workflow-steps/tables/table-json-parse/) | JSON 텍스트 열을 구조화된 필드로 구문 분석합니다. |
| Regex | 전체 | Table Extract / Transform 단계의 정규식 식 | 정규식으로 텍스트 열을 바꾸거나, 구문 분석하거나, 일치시키거나, 토큰화합니다. |
| Text To Columns | 전체 | 정규식 구분자를 사용하는 열 분할 / 분해 단계 | 정규식 구분자를 사용하여 구분된 열을 여러 열 또는 행으로 분할합니다. |
| XML Parse | 전체 | [XML 구문 분석](/ko/reference/workflow-steps/tables/table-xml-parse/) | XML 텍스트 열을 구조화된 필드로 구문 분석합니다. |

### 사용자 지정

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Directory | 전체 | [디렉터리 목록](/ko/reference/workflow-steps/document/directory-listing/) | 바인딩된 문서 폴더의 파일을 젬의 열로 나열합니다. 시트 이름 옵션을 사용하면 각 통합 문서가 시트마다 한 행씩 생성됩니다. 폴더가 없으면 행이 0개입니다. |
| DynamicInput | 전체 | 쿼리 템플릿은 SQL 단계. 다중 파일 모드는 워크플로 루프 | 쿼리 템플릿 모드는 템플릿을 SQL 단계로 포함하고, 다중 파일 모드는 가정을 두고 매핑합니다. |
| Email | 전체 | [Notify Via Email](/ko/reference/workflow-steps/notifications/notify-via-email/) | 바인딩된 이메일 연결을 통해 선택적 데이터 첨부와 함께 이메일을 보냅니다. |
| RestAPI | 전체 | [REST 요청](/ko/reference/workflow-steps/general/rest-request/) | 사용자의 URL, 헤더, 쿼리, 본문, 재시도 설정으로 입력 행마다 요청을 하나씩 보내고, 응답을 유지하며, 비동기 요청은 완료될 때까지 폴링합니다. 자격 증명은 바인딩한 연결에서 가져옵니다. |
| Script | 전체 | 프레임 접근 재작성이 적용된 Python 단계 | 스크립트 본문을 python 단계에 포함하며 데이터 프레임 접근이 다시 작성됩니다. Scala 본문은 참고 사항과 함께 보존됩니다. |
| SQL Statement | 전체 | 출력 탭마다 SQL 단계. 텍스트는 테넌트 방언으로 번역됨 | 각 탭을 SQL 단계로 포함하며 입력은 임시 테이블로 바인딩됩니다. 테넌트 방언으로 번역됩니다. |
| StoredProcedure | 전체 | [Agent Remote Execution of SQL](/ko/reference/workflow-steps/agent/agent-remote-execution-of-sql/) | 선택한 연결을 통해 웨어하우스에서 프로시저를 호출합니다. 각 인수를 해당 열에서 바인딩하여 입력 행마다 한 번, 또는 인수가 없으면 한 번만 호출합니다. 입력 열은 그대로 전달됩니다. |
| Table Operations | 전체 | [Table In-Place Delete](/ko/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/ko/reference/workflow-steps/tables/table-update/), [Table Drop](/ko/reference/workflow-steps/tables/table-drop/) | 업데이트, 삭제, 드롭은 테이블 단계에 매핑됩니다. vacuum과 optimize는 테이블 최적화가 되거나 경고와 함께 아무 작업도 하지 않습니다. |
| ToDo | 전체 | [워크플로 오류 발생](/ko/reference/workflow-steps/workflow-control/raise-workflow-error/) 또는 [Notify via Log](/ko/reference/workflow-steps/notifications/notify-via-log/) | 아직 작성되지 않은 로직을 표시합니다. 이를 읽는 항목이 없으면 로그 메시지가 되고, 이후 단계가 이에 의존하면 젬의 메시지와 함께 실행을 중지하는 단계가 됩니다. |

### 공간

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Buffer | 전체 | [Spatial Buffer](/ko/reference/workflow-steps/spatial/spatial-buffer/) | 구성된 거리(마일 또는 킬로미터)만큼 각 지오메트리를 확장합니다. |
| CreatePoint | 전체 | `geom_point`를 사용하는 [Table Extract](/ko/reference/workflow-steps/spatial/spatial-sql-recipes/) | 경도 및 위도 열에서 포인트 지오메트리를 만듭니다. |
| Distance | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) | 두 WKT 포인트 사이의 거리, 방위(기본 방위), 방위각을 계산합니다. |
| FindNearest | 전체 | 교차 조인을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) | 최대 거리 안에서 각 소스 포인트에 가장 가까운 N개의 대상 포인트를 찾습니다. |
| HeatMap | 전체 | [Heat Map (macro)](/ko/reference/workflow-steps/macros/macro-heat-map/) | 젬의 해상도로 포인트를 H3 육각형에 구간화하고, 감쇠를 적용해 격자 거리만큼 열을 퍼뜨리며, 각 육각형의 밀도와 윤곽을 제공합니다. |
| PolyBuild | 전체 | [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 및 Python 단계 | 그룹별 순서가 지정된 포인트에서 폴리곤 또는 폴리라인 WKT를 만듭니다. |
| Simplify | 전체 | [Spatial Generalize](/ko/reference/workflow-steps/spatial/spatial-generalize/) | 마일/킬로미터 단위의 허용 오차로 WKT 지오메트리를 단순화합니다. |
| SpatialMatch | 전체 | [공간 매치](/ko/reference/workflow-steps/spatial/spatial-match/) | intersects/contains/within/touches/envelope로 소스 및 대상 지오메트리를 매치합니다. |

### 보고서

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| PowerBIWrite | 전체 | [REST 요청](/ko/reference/workflow-steps/general/rest-request/) | Power BI 데이터세트를 만들고 Power BI REST API를 통해 행을 푸시합니다. |
| TableauWrite | 전체 | [Publish to Tableau](/ko/reference/workflow-steps/export/export-to-tableau/) | Hyper 추출을 쓰고 바인딩된 Tableau 연결에 게시합니다. |
| Visualize | 전체 | [테이블 복사](/ko/reference/workflow-steps/tables/table-copy/) | 행을 변경 없이 전달합니다. 차트는 동일한 테이블에 대한 PlaidCloud 대시보드로 만드십시오. |

### 서브그래프/제어

| 젬 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Condition | 전체 | [교차 조인](/ko/reference/workflow-steps/tables/table-cross-join/) 및 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) | 전체 입력에 대해 조건을 평가하고 모든 행을 조건이 성립하는 첫 번째 출력으로 보내며, 없으면 마지막 출력으로 보냅니다. |
| Macro | 전체 | 매크로 본문이 확장된 SQL 단계 | 매크로 본문을 테넌트 방언으로 번역된 SQL 단계로 포함하며, 입력은 임시 테이블로 바인딩됩니다. |
| Pipeline (trigger) | 전체 | [Workflow Loop](/ko/reference/workflow-steps/workflow-control/workflow-loop/) | 사용자의 매개변수와 트리거 조건으로 지정된 파이프라인을 입력 행마다 한 번씩 실행하고, 실패한 실행을 넘어 계속 진행하며, 실행마다 한 행을 반환합니다. |
| Subgraph (Basic) | 전체 | 인라인 프로세스에서 만든 캔버스 컨테이너 / 중첩 워크플로 | 인라인 내부 그래프를 입력/출력 테이블 매개변수를 가진 중첩 워크플로(또는 인라인 단계)로 변환합니다. |

## 커넥터

데이터세트 형식과 커넥터는 젬이 아니라 젬의 소스 및 대상 설정입니다. 각 형식은 표시된 가져오기 또는 내보내기 단계로 변환되며, 변환은 소스 또는 대상 시스템에 접속하지 않습니다.

| 형식 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Avro | 전체 | 가져오기: [Avro](/ko/reference/workflow-steps/import/import-avro/), 내보내기: [Avro](/ko/reference/workflow-steps/export/export-to-avro/) | Avro 파일을 읽고 씁니다. |
| BigQuery | 전체 | 테이블 가져오기를 사용하는 외부 데이터베이스 연결 | 연결을 통해 읽고 씁니다. |
| Binary files | 전체 | 파일 내용을 포함한 [디렉터리 목록](/ko/reference/workflow-steps/document/directory-listing/). 쓰기는 [Alteryx 실행기](/ko/reference/workflow-steps/general/alteryx-executor/) | 폴더의 각 파일을 경로, 수정 시간, 길이, 내용과 함께 읽고, 각 행의 내용을 해당 행의 경로가 가리키는 파일에 씁니다. |
| Catalog table | 전체 | 기존 PlaidCloud 테이블 바인딩 | 이름으로 테이블에 바인딩됩니다. 읽기와 모든 쓰기 모드가 변환됩니다. |
| Cosmos DB | 전체 | 가져오기 및 내보내기: [REST 요청](/ko/reference/workflow-steps/general/rest-request/) | Cosmos DB 연결을 통해 컨테이너의 문서를 읽고 씁니다. |
| CSV | 전체 | [가져오기: CSV](/ko/reference/workflow-steps/import/import-csv/), 내보내기: CSV | 헤더, 구분자, 따옴표, 이스케이프, 인코딩 옵션으로 구분된 파일을 읽고 씁니다. |
| Data Generator | 전체 | [Table Faker](/ko/reference/workflow-steps/tables/table-faker/) | 데이터세트의 열을 동일한 종류의 가짜 데이터로 생성합니다. |
| DataHub table | 전체 | [SQL 가져오기](/ko/reference/workflow-steps/import/import-sql/) | 연결을 통해 데이터세트가 지정한 테이블을 읽습니다. 쓰기는 PlaidCloud 테이블에 기록됩니다. |
| Delta | 전체 | 기존 PlaidCloud 테이블 바인딩 | 모든 쓰기 모드로 테이블을 읽고 씁니다. 이전 버전 읽기는 바인딩한 Databricks 연결을 통해 읽습니다. |
| Excel (XLSX) | 전체 | 가져오기: Excel, 내보내기: Excel | 통합 문서의 시트와 범위를 읽고 씁니다. |
| Fixed format | 전체 | 가져오기: [고정 너비](/ko/reference/workflow-steps/import/import-fixed-width/), 내보내기: [CSV](/ko/reference/workflow-steps/export/export-to-csv/) | 데이터세트의 열 너비에 맞춰 배치된 고정 너비 파일을 읽고, 구분된 파일을 씁니다. |
| Hive | 전체 | [SQL 가져오기](/ko/reference/workflow-steps/import/import-sql/), 내보내기: [외부 테이블](/ko/reference/workflow-steps/export/export-external-tables/) | Hive 연결을 통해 테이블을 읽고 씁니다. |
| Iceberg | 전체 | 기존 PlaidCloud 테이블 바인딩 | 테이블을 읽고 씁니다. |
| JDBC | 전체 | 테이블 가져오기를 사용하는 외부 데이터베이스 연결 | 연결을 통해 테이블 또는 쿼리를 읽고 바꾸기 또는 추가 모드로 씁니다. 쓰기 후 문은 쓰기가 끝난 뒤에 실행됩니다. |
| JSON | 전체 | [JSON 구문 분석](/ko/reference/workflow-steps/tables/table-json-parse/) | 레코드를 로드하고 중첩 필드를 평탄화합니다. |
| Kafka | 전체 | [Kafka 가져오기](/ko/reference/workflow-steps/import/import-kafka/), [Kafka 내보내기](/ko/reference/workflow-steps/export/export-kafka/) | 토픽을 메시지의 한 배치로 읽고 행을 메시지로 씁니다. |
| MongoDB | 전체 | 가져오기: [MongoDB](/ko/reference/workflow-steps/import/import-mongodb/), 내보내기: [MongoDB](/ko/reference/workflow-steps/export/export-mongodb/) | MongoDB 연결을 통해 컬렉션을 읽고 씁니다. |
| ORC | 전체 | 가져오기: [ORC](/ko/reference/workflow-steps/import/import-orc/), 내보내기: ORC | ORC 파일을 읽고 씁니다. |
| Parquet | 전체 | 가져오기: Parquet, 내보내기: Parquet | Parquet 파일을 읽고 씁니다. |
| Pinecone | 전체 | 가져오기 및 내보내기: [REST 요청](/ko/reference/workflow-steps/general/rest-request/) | Pinecone REST API를 통해 인덱스의 레코드를 읽고 행을 벡터로 업서트합니다. |
| Redshift | 전체 | 테이블 가져오기를 사용하는 외부 데이터베이스 연결 | 연결을 통해 읽고 씁니다. |
| Salesforce | 전체 | 가져오기: [Query Salesforce Object](/ko/reference/workflow-steps/salesforce/query-salesforce-object/), 내보내기: [REST 요청](/ko/reference/workflow-steps/general/rest-request/) | Salesforce 연결을 통해 개체 또는 SOQL 쿼리를 읽고 레코드를 씁니다. |
| Seed (inline) | 전체 | [가져오기: CSV](/ko/reference/workflow-steps/import/import-csv/) | 인라인 행을 테이블로 로드합니다. |
| Slack | 전체 | 가져오기: [Singer](/ko/reference/workflow-steps/import/import-singer/), 내보내기: [REST 요청](/ko/reference/workflow-steps/general/rest-request/) | Slack 연결을 통해 채널 메시지를 읽고 각 행을 메시지로 게시합니다. |
| Smartsheet | 전체 | 가져오기 및 내보내기: [REST 요청](/ko/reference/workflow-steps/general/rest-request/) | Smartsheet 연결을 통해 시트의 행을 읽고 씁니다. |
| Snowflake | 전체 | 테이블 가져오기를 사용하는 외부 데이터베이스 연결 | 연결을 통해 읽고 씁니다. |
| SQL file types (CSV, Excel, JSON, Parquet, Text, XML, fixed-width) | 전체 | 문서 계정에 대한 파일 가져오기 및 내보내기 단계 | 파일 유형을 읽고 씁니다. PlaidCloud에 대응하는 항목이 없는 옵션에는 표시가 붙습니다. |
| Text | 전체 | 단일 열로 [가져오기: CSV](/ko/reference/workflow-steps/import/import-csv/) | 각 줄을 하나의 열로 읽습니다. |
| Web page | 전체 | [REST 요청](/ko/reference/workflow-steps/general/rest-request/) | 데이터세트의 URL에 있는 페이지를 테이블로 읽습니다. |
| XML | 전체 | [XML 구문 분석](/ko/reference/workflow-steps/tables/table-xml-parse/) | 행 태그를 기준으로 레코드를 로드합니다. |

## 식 및 프로젝트 구조

| 영역 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| 식 | 전체 | 함수 단위로 번역된 Spark 및 웨어하우스 SQL 식 | 함수와 연산자는 PlaidCloud 식으로 변환됩니다. 대응하는 항목이 없는 함수는 이름과 함께 표시됩니다. |
| 프로젝트 및 그래프 구조 | 전체 | 프로젝트 로더 | 모든 Prophecy 내보내기 형태가 하나의 모델로 로드되고 정규화됩니다. |

## 알려진 예외 사례

| 사례 | 동작 |
| --- | --- |
| 내보내기에 포함되지 않은 코드 또는 데이터 | 코드가 내보내기에 없는 Gem Builder 또는 기타 사용자 지정 젬, 그리고 내보내기에서 제외된 dbt 패키지의 매크로 호출은 누락된 항목을 명시하는 단계가 됩니다. 파이프라인 코드와 dbt 패키지를 포함하여 프로젝트를 내보내거나, Python 또는 SQL 단계에서 로직을 다시 구축하십시오. Ab Initio Error Detection 및 MTime 젬은 적용하는 규칙이 내보내기에 없으므로 입력을 그대로 전달합니다. 프로젝트 밖의 파일에서 읽는 Soda 검사, 이전 스캔이나 다른 데이터세트와 비교하는 Soda 검사, Soda가 이름으로 지정한 형식을 테스트하는 Soda 검사는 결과 테이블에 행이 없으므로 이후 단계에서 계산하십시오. |
| 파이프라인을 실행할 때만 알 수 있는 결과 | 응답을 평탄화하는 REST API 젬은 필드 이름이 선언되지 않은 경우(실행해야만 알 수 있음) 전체 응답을 하나의 열에 넣습니다. 필요한 필드는 이후 단계에서 추출하십시오. dbt가 컴파일하는 동안 웨어하우스를 쿼리하는 dbt 매크로는 이를 명시하는 단계가 됩니다. 쿼리를 그 쿼리가 반환하는 값으로 바꾸십시오. Spark StoredProcedure 젬은 실행되지만 OUT 값은 반환되지 않으며, 출력은 전달되는 열입니다. `input_file_name()`은 이름을 붙일 파일이 없는 테이블 또는 Delta 소스에서는 빈 문자열을 반환하며, 집계, 윈도 또는 입력이 여러 개인 젬 안의 `hash()` / `xxhash64()`는 웨어하우스에서 계산되므로 Spark의 결과와 다를 수 있습니다. |
| 프로젝트가 변환될 때 단계에 기록되는 값 | 따옴표, 백슬래시 또는 중괄호가 포함된 매개변수 값, SQL 단계가 읽는 파이프라인 값, 구성을 통해 Delta 테이블 작업이 지정하는 데이터베이스는 고정 값으로 단계에 기록되므로, 워크플로 변수를 바꿔도 이 값들은 바뀌지 않습니다. 구성이 바뀌면 단계를 편집하십시오. |
| Scala 코드 | Scala 스크립트, Scala 식, Scala 사용자 정의 함수 또는 집계 함수는 이를 명시하는 단계가 됩니다. SQL 또는 Python으로 다시 작성하십시오. |
| Kafka Kerberos 로그인 | Kerberos(GSSAPI)로 로그인하는 Kafka 소스 또는 대상은 Kerberos 서비스 이름과 로그인 메커니즘 없이 변환됩니다. 이 값들은 PlaidCloud 연결에서 설정하십시오. |
| 스트리밍 | 스트리밍 소스, 대상, 파이프라인은 실행 시점에 존재하는 데이터에 대한 배치 워크플로로 실행됩니다. 필요한 빈도로 실행되도록 워크플로 일정을 설정하십시오. |
| 작업 구성 요소 | Spark 작업은 하나의 파이프라인과 일정이 변환됩니다. 다른 구성 요소, 실행 조건, 구성 재정의는 변환되지 않습니다. |
| 흔하지 않은 호출 | 롤업 또는 윈도에서 호출되는 사용자 정의 집계 함수, 그리고 if, for, set 및 일반적인 필터를 넘어 Jinja를 사용하는 dbt 매크로는 해당 젬을 명시하는 단계가 됩니다. Aggregate 젬에서 함수를 호출하거나 매크로를 인라인으로 풀어 사용하십시오. |

## 변환된 워크플로 검증

변환된 워크플로의 출력을 자체 Prophecy 파이프라인의 출력과 비교하십시오. 스키마, 행 수, 행 값을 비교합니다. 워크플로가 행 순서에 의존하지 않는 한 행 순서는 무시합니다.
