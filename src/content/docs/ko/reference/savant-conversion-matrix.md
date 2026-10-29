---
title: Savant 변환 매트릭스
description: PlaidCloud가 Savant Labs 분석을 네이티브 고급 워크플로로 변환하는 방식과, 각 에이전트의 매핑 티어 및 이름이 지정된 일부 예외 사례를 설명합니다.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/savant-conversion-matrix.md
---

PlaidCloud는 Savant Labs 분석을 네이티브 고급 워크플로로 변환합니다. 가져오기 도구는
각 Savant 에이전트를 워크플로 단계, 프로젝트 변수 또는 캔버스 객체에 매핑하므로,
변환된 워크플로는 클라우드 네이티브로 실행됩니다.

변환을 실행하려면 [Savant 분석 마이그레이션](/ko/guides/workflows/migrate-savant-analyses/)을 참조하십시오.

각 에이전트에는 매핑 티어가 있습니다. **전체**는 에이전트의 모든 옵션이
PlaidCloud 단계에 유효하게 매핑된다는 뜻입니다. 이름을 지정하여 거부하는 구문은
이름이 지정된 거부 항목 아래에 나열되어 있습니다.

외부 시스템 커넥터는 **연결되며 변환되지 않습니다**. 자세한 내용은
[외부 시스템 연결](#외부-시스템-연결)을 참조하십시오.

## 에이전트 지원

33개 에이전트가 모두 전체 티어로 변환됩니다.

| 에이전트 | 티어 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Adapter 에이전트 (`adapter`) | 전체 | 선택 및 스키마 프로젝션 단계 | 필드의 이름을 바꾸고, 유형을 변경하고, 순서를 지정합니다. |
| API / Infer 에이전트(레거시 서비스) (`service`) | 전체 | serviceType에 따라 API 에이전트 또는 Infer 에이전트와 동일 | LLMService는 Infer 에이전트로, APIService는 API 에이전트로 변환됩니다. serviceType이 없거나 철자가 잘못된 경우 노드의 키에서 읽으며 경고가 표시됩니다. |
| API 에이전트 (`apiService`) | 전체 | Table Extract, [REST 요청](/ko/reference/workflow-steps/general/rest-request/), 그리고 왼쪽 조인으로 되돌리기 | 입력 행마다 GET, POST, PUT, PATCH 또는 DELETE 요청을 한 번씩 보냅니다. 원시 응답 본문은 텍스트 열에 저장되고, HTTP 오류는 행으로 유지되며, 모든 입력 행이 보존되고, 기간당 할당량은 초당 요청 수(소수)로 변환됩니다. 상대 URL은 api_bindings의 기본 URL 또는 REST 연결 호스트와 결합됩니다. 행 필드의 호스트, 포트 또는 경로는 행마다 대체되며, 다음 URL, Link 헤더, 오프셋 및 페이지 방식의 페이징을 따르고, 행 필드로 템플릿화된 시작 위치, 페이지 크기 또는 매개변수 이름도 포함합니다. |
| Blend 에이전트 (`blend`) | 전체 | [내부 조인](/ko/reference/workflow-steps/tables/table-inner-join/), [외부 조인](/ko/reference/workflow-steps/tables/table-outer-join/), [안티 조인](/ko/reference/workflow-steps/tables/table-anti-join/) | 내부, 왼쪽, 오른쪽, 전체, 안티, 내부 제외 외부 블렌드와 OR 조인, 포함 및 일부 조건을 일치/불일치 스트림과 함께 지원합니다. 피벗 또는 구문 분석이 실행 시에만 이름을 지정하는 열도 그대로 전달됩니다. |
| Dedupe 에이전트 (`deduplicate`) | 전체 | 고유 행을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 그룹화 기준 그룹 내에서 키별로 첫 번째 레코드를 유지하고, 중복은 두 번째 스트림으로 보내거나 플래그로 표시합니다. |
| Destination 에이전트 (`destination`) | 전체 | [내보내기: CSV](/ko/reference/workflow-steps/export/export-to-csv/), [내보내기: Excel](/ko/reference/workflow-steps/export/export-to-excel/), Export: Parquet, JSON, Avro 또는 XML, [Export to PDF](/ko/reference/workflow-steps/export/export-to-pdf/), [내보내기: Tableau Hyper](/ko/reference/workflow-steps/export/export-hyper/)와 [Publish to Tableau](/ko/reference/workflow-steps/export/export-to-tableau/)의 조합, [내보내기: External Database Tables](/ko/reference/workflow-steps/export/export-external-tables/), [Export to Google Spreadsheet](/ko/reference/workflow-steps/export/export-to-google-spreadsheet/), [Notify via Slack](/ko/reference/workflow-steps/notifications/notify-via-slack/) 또는 이메일 | destination_bindings를 통해 문서 계정(CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF 또는 Tableau .hyper. 별칭, CESU-8 및 바이트 순서 표시 형식을 포함한 모든 Java 문자 집합 지원, 문자 집합에 없는 문자는 ?로 기록), 연결 테이블, Google 스프레드시트, Tableau 데이터 원본, Slack 채널 또는 이메일 수신자에 기록합니다. 바인딩되지 않은 대상은 프로젝트 테이블 또는 Document 파일에 기록합니다(아래 'PlaidCloud에서의 위치' 참조). 필드 값별로 파일, 하위 폴더 또는 탭을 나누어 CSV, Excel, Parquet, PDF 파일과 Google 스프레드시트 탭을 분할하며, 템플릿은 분할된 모든 통합 문서의 기반이 됩니다. Excel 옵션은 다음과 같이 매핑됩니다. 빈 값은 `Sheet1`로 이동하고, 시트 이름이 충돌하면 접미사가 붙으며, `formatFromTemplate`, `topLeftCell`, 모드 `create`를 지원합니다. Append, upsert, update 및 groupReplace는 일치 키를 기준으로 병합합니다(파일 또는 테이블을 다시 읽어 다시 기록하며, 분할 시에는 실행에서 각 값이 기록되는 파일을 다시 읽어 그 안에서 병합하고 다른 파일은 그대로 둡니다. Tableau는 해당 행을 제자리에서 업데이트합니다). 데이터에서만 이름이 정해지는 열(승격된 헤더의 열, 피벗의 값, 구문 분석된 JSON 또는 XML의 키)은 알려진 열 옆에 모든 내보내기와 테이블 쓰기에서 기록되고, 정렬 및 분할에 사용되며, 테이블에 추가·병합되거나 모든 열을 가진 파일로 다시 읽어 병합됩니다. |
| Explode 에이전트 (`explode`) | 전체 | [교차 조인](/ko/reference/workflow-steps/tables/table-cross-join/) | 작은 쪽을 기본 스트림과 교차 조인합니다. |
| Filter 에이전트 (`filter`) | 전체 | 필터 식을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 마법사 또는 식에 따라 레코드를 참 경로와 거짓 경로로 나눕니다. |
| Filter Pushdown (`pdfilter`) | 전체 | 필터 식을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 데이터베이스 측 필터로, Filter와 동일하게 변환됩니다. |
| Format 에이전트 (`format`) | 전체 | 열 이름 바꾸기를 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 또는 Promote Header | 이름(포함, 시작, 끝)이나 비어 있음 여부로 일치하는 필드를 숨기고, 유형을 변경하고, 이름을 바꾸고, 채웁니다. 채우기는 기본값을 변환할 수 있는 유형(텍스트, 숫자, 날짜)의 모든 열에 기본값을 기록합니다. 헤더 행 승격과 비어 있음 일치는 Promote Header 단계에서 실행 시에 수행되며, 승격된 헤더는 파일의 모든 열을 읽습니다. |
| Fuse 에이전트 (`fuzzy_match`) | 전체 | Union All과 두 개의 조인 사이에 있는 [Fuzzy Match](/ko/reference/workflow-steps/tables/table-fuzzy-match/) | 두 입력을 쌓고, 유사도 임계값 80으로 키 필드의 레코드를 일치시킨 다음, 신뢰도 점수와 함께 양쪽을 다시 조인합니다. |
| Group (`group`) | 전체 | 캔버스 컨테이너 | 워크플로 구성으로 보존됩니다. |
| Infer 에이전트 (`gen_ai`) | 전체 | [AI/NLP](/ko/reference/workflow-steps/text-documents/nlp-ai/) 프롬프트 작업 | Savant의 공급자 및 모델과 일치하는 표시된 LLM 연결에서 입력 필드를 기준으로 행마다 프롬프트를 실행하며, 응답은 모든 입력 열 옆의 AI Answer 열에 저장됩니다. rowLimit은 실행당 응답할 행 수를 제한하고 이전 응답을 유지합니다. 이전에 응답한 행(동일한 프롬프트, 모델, 입력 값)은 응답을 유지하며, 응답하지 않은 행만 제한에 포함됩니다. |
| JSON 에이전트 (`json`) | 전체 | [JSON 구문 분석](/ko/reference/workflow-steps/tables/table-json-parse/) | JSON 필드를 점으로 구분된 키 열로 평면화하거나 배열을 요소당 한 행으로 펼칩니다. 키는 실행 시 데이터에서 읽습니다. |
| Notes 에이전트 (`notes`) | 전체 | 캔버스 주석 | 워크플로 컨텍스트로 보존됩니다. |
| Pivot 에이전트 (`pivot`) | 전체 | [Pivot](/ko/reference/workflow-steps/tables/table-pivot/) | 행을 열로 피벗하며 집계를 적용합니다. |
| Recursion 에이전트 (`hierarchy`) | 전체 | Hierarchy Closure, [Table Extract](/ko/reference/workflow-steps/tables/table-extract/), [다중 테이블 조인](/ko/reference/workflow-steps/tables/table-multi-table-join/) | 부모/자식 트리를 임의의 깊이까지 탐색하며, 각 노드를 자기 자신을 포함해 루트까지의 경로에 있는 ID에 대해 집계하고 Depth와 Path를 기록합니다. 루프는 반복된 노드에서 멈춥니다. |
| Sample 에이전트 (`sample`) | 전체 | 행 제한을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 처음 N개 행을 유지하며, 선택적으로 그룹별, 임의의 비율 또는 N개 행, 또는 N개 행마다 한 행을 유지합니다. |
| Search and Replace (`search_replace`) | 전체 | 단계로 나뉜 중첩 바꾸기 식을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 찾기/바꾸기 규칙(포함 또는 일치, 바꾸기 또는 추가, 대소문자 구분 여부, 전체 단어 여부)을 선택한 텍스트 필드에 순서대로 적용하며, 지정한 필드가 없으면 모든 텍스트 필드에 적용합니다. |
| Source 에이전트 (`source`) | 전체 | `source_bindings`를 통해 바인딩된 가져오기 단계([가져오기: CSV](/ko/reference/workflow-steps/import/import-csv/), [가져오기: Excel](/ko/reference/workflow-steps/import/import-excel/), [가져오기: SQL](/ko/reference/workflow-steps/import/import-sql/)) 또는 기존 테이블 | 바인딩된 테이블 또는 문서를 읽습니다. 바인딩되지 않은 소스는 빈 가져오기를 만들고 경고를 표시합니다. XML 텍스트는 XML 가져오기를 통해 문서를 읽습니다(바인딩되지 않은 경우 savant/<workflow>/<name>.xml을 읽습니다). XML 문서에 바인딩된 소스는 내보내기의 다른 열도 기록하며, 문서의 파일 이름 또는 경로 열은 채우고 나머지는 비워 둡니다. 헤더 행을 승격하는 Format 아래의 소스는 CSV, Excel(Excel 97 .xls 포함), JSON, Parquet 또는 Avro 파일의 모든 열을 위치 기준으로 읽습니다. |
| Spatial Match 에이전트 (`spatial_match`) | 전체 | [공간 매치(실행기)](/ko/reference/workflow-steps/spatial/spatial-match-executor/), [교차 조인](/ko/reference/workflow-steps/tables/table-cross-join/) 또는 [가장 가까운 항목 찾기](/ko/reference/workflow-steps/spatial/spatial-find-nearest/) | 교차, 내부, 포함, 접함, 가로지름, 겹침, 같음, 분리 및 AND/OR 다중 규칙 일치, 임의 지오메트리(점, 선, 폴리곤: 반지름 6371km 구에서의 최단 거리) 간의 측지 거리 이내 일치, 최대 거리가 있는 동일 거리 기준의 가장 가까운 N개(단독 nearest 규칙은 Savant와 마찬가지로 Distance 열을 기록하지 않으며, 다른 규칙과 함께 nearest 후 필터로 결합될 때는 AND 조인과 OR 합집합이 적용되고 각 nearest 규칙은 자체 Distance 열을 추가함), 그리고 Cross를 일치/불일치 스트림과 함께 지원합니다. |
| Spatial Summarize 에이전트 (`spatial_summarize`) | 전체 | [공간 결합](/ko/reference/workflow-steps/spatial/spatial-combine/), Spatial Centroid 및 점-선 변환 단계 | 그룹별로 선택적 정렬과 함께 합집합, 교집합, 경계 상자, 하나 이상의 기하 중심, 폴리라인 또는 폴리곤 생성을 지원합니다. |
| Split 에이전트 (`split`) | 전체 | Split Text 또는 split_part 열을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 임의 길이의 리터럴 구분 기호로 텍스트 필드를 행 또는 열로 분할하며, 공백 제거와 원본 유지를 지원합니다. 열 수는 실행 시 데이터에서 읽습니다. |
| 출력 분할 (`outlet`) | 전체 | 워크플로 에지 | 이름이 지정된 출력을 해당 소비자에게 라우팅합니다. |
| Stack 에이전트 (`multi_stack`) | 전체 | [Union All](/ko/reference/workflow-steps/tables/table-union-all/) | 이름 또는 위치를 기준으로 임의 개수의 입력을 쌓습니다. |
| Summarize 에이전트 (`summarize`) | 전체 | 집계를 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 그룹화하고 집계하며, 결정적 정렬 기준의 첫 번째/마지막 값과 행별 윈도 집계(useWindow)를 포함합니다. |
| Summarize Pushdown (`pdsummarize`) | 전체 | 집계를 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 데이터베이스 측 집계로, Summarize와 동일하게 변환됩니다. |
| Text (`text`) | 전체 | 캔버스 주석 | 워크플로 컨텍스트로 보존됩니다. |
| Time Series 에이전트 (`rollup`) | 전체 | 기간 버킷 식에 대한 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 집계, Period Spine, [안티 조인](/ko/reference/workflow-steps/tables/table-anti-join/) 및 [Union All](/ko/reference/workflow-steps/tables/table-union-all/) | 선택적 시작일과 종료일 사이의 레코드를 그룹별로 일, 주, 월, 분기, 연도 또는 10년 단위 기간으로 롤업하며, NULL 날짜는 제외하고 비어 있는 기간은 0으로 채웁니다. |
| Transform 에이전트 (`edit`) | 전체 | 열 식을 사용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/) 단계 | 계산 열, 유형 변경, 윈도 계산(lag, lead, 누적 합계, 행 번호, 앞뒤 방향 채우기)을 순서대로 평가합니다. 컴파일된 단계만 가진 편집은 해당 단계를 순서대로 적용하며 각 단계가 다음 단계에 입력을 전달하는 방식으로 변환됩니다. |
| Unpivot 에이전트 (`unpivot`) | 전체 | [Melt](/ko/reference/workflow-steps/tables/table-melt/) | 열을 이름/값 쌍의 행으로 변환합니다. |
| Vision 에이전트 (`vision`) | 전체 | [Image OCR](/ko/reference/workflow-steps/text-documents/image-ocr/) 다음 [AI/NLP](/ko/reference/workflow-steps/text-documents/nlp-ai/) 프롬프트 작업 | 공급자가 해당 유형과 크기를 허용하면 각 문서를 이미지 또는 PDF로 보내고, 그렇지 않으면 PDF 텍스트 계층 또는 OCR 텍스트를 보냅니다. 프롬프트의 응답은 AI Answer 열에 저장됩니다. |
| XML 에이전트 (`xml`) | 전체 | [XML 구문 분석](/ko/reference/workflow-steps/tables/table-xml-parse/) | 요소를 선택하고, 자식 값과 속성을 열로 추출하거나, XML을 JSON으로 변환합니다. 단순한 //a/b 경로는 기존과 같이 변환되며, 그 외의 XPath 1.0 경로(조건자, 속성 테스트, 와일드카드, count(), name(), contains() 같은 함수)는 네임스페이스를 인식하거나 작성된 그대로 XPath로 평가됩니다. |

연결, 캔버스 및 푸시다운 변형(출력 분할, Group, Text, Filter Pushdown, Summarize Pushdown)은 도움말 센터에 자체 에이전트 문서가 없는 Savant 노드 유형이며, 각각 대응하는 에이전트와 동일하게 변환됩니다.

API 에이전트 요청의 자격 증명은 워크플로 단계에 복사되지 않습니다. https를 통한 경우 REST 연결로 이동하며, http를 통한 경우, 연결을 쓸 권한이 없는 경우 또는 MCP를 통해 수행한 변환에서는 경고와 함께 보류됩니다. 이는 의도된 동작이며 티어를 낮추지 않습니다.

두 가지 대상 제한은 티어를 낮추지 않습니다. 일부 드문 문자 집합(예: `x-ISCII91` 또는 `JIS_X0212`)은 기록할 수 없으며, 이 경우 파일은 UTF-8로 기록되고 변환 시 경고가 표시됩니다. 키를 기준으로 병합하는 Tableau 게시에는 대상 바인딩에 `replace: true`가 필요합니다. 이것이 없으면 변환 시 경고가 표시되고 새 데이터 원본이 게시되며, 데이터 원본이 이미 있는 실행에서는 실패합니다.

## 이름이 지정된 거부 항목

여덟 가지 구문은 변환되지 않고 이름을 지정하여 거부됩니다. 어느 것도 에이전트의 티어를 낮추지 않습니다.

| 구문 | 거부되는 이유 |
| --- | --- |
| 자격 증명을 포함하고 호스트를 입력 필드에서 가져오는 API 에이전트 요청 | 각 행이 데이터가 선택한 호스트로 자격 증명을 보낼 수 있습니다. 요청은 이름이 지정된 플레이스홀더가 됩니다. 자격 증명이 없는 요청과 고정 호스트의 자격 증명은 변환됩니다. |
| 식도 컴파일된 단계도 없는 Transform 편집(예: 프롬프트만 있는 Copilot 편집) | 변환할 내용이 없습니다. 프롬프트는 수식이 아닙니다. 컴파일된 단계가 있는 편집은 변환됩니다. |
| PlaidCloud가 읽을 수 없는 Transform 또는 Filter 식의 정규식 구문: 클래스 안의 클래스, 클래스 교집합(`&&`) 또는 알 수 없는 `\p{}` 속성 | 해당 단계는 실행 시 거부하는 이름이 지정된 플레이스홀더가 됩니다. |
| Transform 또는 Filter 식의 집계 또는 윈도 함수 | Savant 자체도 실행 시 실패합니다. Transform 계산이나 Summarize에서는 변환됩니다. |
| `HASH`를 Transform 또는 Filter 식에서 `md5` 또는 `sha1`이 아닌 리터럴 알고리즘과 함께 사용하는 경우 | Savant 자체도 실패합니다(알고리즘은 `md5` 또는 `sha1`이어야 함). 열에서 읽은 알고리즘은 변환되며, 그 외의 값에는 NULL을 반환합니다. |
| 입력에 없는 열을 기준으로 한 대상 정렬 | Savant 자체도 실행 시 실패합니다. |
| 입력에 없는 열의 값마다 대상 파일, 하위 폴더, 탭 또는 워크시트를 나누는 경우 | Savant 자체도 실행 시 실패합니다. |
| XPath 1.0이 아닌 XML 에이전트 경로 | Savant도 실행할 수 없습니다. |

`api_bindings`로 기본 URL 또는 REST 연결을 바인딩하면 상대 API URL이 변환됩니다. [변환 시 바인딩](/ko/guides/workflows/migrate-savant-analyses/#변환-시점-바인딩)을 참조하십시오.

## 식 언어

Savant 식 함수와 연산자는 PlaidCloud 식으로 변환됩니다. 티어: **전체**. 숫자 패턴이 있는 `TO_TEXT`, 행별로만 알 수 있는 형식, 소수 초, 주 기반, 분기 및 시간대 날짜 토큰, 두 자리 연도, Java 정규식 구문을 포함하여 모든 함수와 형식이 변환됩니다. 식 안의 어느 위치에 있든 GEO_* 함수는 보조 Spatial 단계에서 실행됩니다. 예외는 [이름이 지정된 거부 항목](#이름이-지정된-거부-항목)입니다.

알려진 예외 사례: `TO_DATE` 또는 `TO_DATETIME`에서 형식에 `[`, `]`, 따옴표, 백슬래시 또는 `^` 리터럴이 포함되고 텍스트가 9999-12-30 또는 9999-12-31로 읽히는 경우로, 이는 웨어하우스가 보유하는 마지막 타임스탬프를 지난 값이며 변환 시 경고가 표시됩니다.

## 내보내기 형식

로더는 평면, 모델 래핑, 서버 레코드, 레시피 엔벌로프, 배열 래핑, BOM 접두사, 레거시 유형 별칭 등 모든 Savant 내보내기 형태를 받아들여 하나의 모델로 정규화합니다. 티어: **전체**.

## 분석 매개변수

Savant 분석 매개변수는 워크플로 변수로 변환되며, 노드 구성 안에서 이를 참조하는 부분은 PlaidCloud 변수 구문으로 다시 작성됩니다. 목록, 딕셔너리, 별칭 형태의 매개변수가 모두 로드됩니다. 티어: **전체**.

알려진 예외 사례: 이름에 비밀 관련 단어가 포함되거나 값이 자격 증명처럼 보이는 매개변수는 값이 비어 있는 변수가 되며 경고가 표시됩니다. 노드가 사용하지만 내보내기에 선언되지 않은 매개변수는 값이 빈 변수가 되며 경고가 표시됩니다.

## 외부 시스템 연결

Savant 커넥터는 단계가 아니라 소스 및 대상 타깃이며, 내보내기에는 데이터 세트나 자격 증명이 포함되지 않습니다. PlaidCloud는 캔버스의 노드가 아니라 연결을 통해 이러한 시스템에 접근합니다.

| Savant | PlaidCloud에서의 위치 |
| --- | --- |
| 소스 커넥터 | `source_bindings`가 Savant 노드 또는 데이터 세트를 PlaidCloud 테이블 또는 Document 파일에 매핑하며, 해당하는 가져오기 단계를 통해 읽습니다. 바인딩되지 않은 소스는 경고를 표시하고 아무것도 처리하지 않습니다 |
| 대상: CSV, Excel 및 기타 파일 형식 | 내보내기 단계([내보내기: CSV](/ko/reference/workflow-steps/export/export-to-csv/), [내보내기: Excel](/ko/reference/workflow-steps/export/export-to-excel/), [Export to PDF](/ko/reference/workflow-steps/export/export-to-pdf/)) |
| 대상: Google 스프레드시트, Tableau, Slack | `destination_bindings`로 바인딩한 연결을 통한 [Export to Google Spreadsheet](/ko/reference/workflow-steps/export/export-to-google-spreadsheet/), [Publish to Tableau](/ko/reference/workflow-steps/export/export-to-tableau/) 또는 [Notify via Slack](/ko/reference/workflow-steps/notifications/notify-via-slack/) |
| 대상: 바인딩되지 않은 데이터베이스, 웨어하우스 또는 SaaS 대상(Oracle, 일반 데이터베이스, Looker Studio, NetSuite, SAP, 그리고 연결이 바인딩되지 않은 Google 스프레드시트, Tableau 또는 Slack) | 대상 노드의 이름을 딴 프로젝트 테이블이며, 원래 대상을 명시한 경고가 표시됩니다 |
| 대상: 바인딩되지 않은 파일 시스템 대상(S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | 대상의 파일 유형으로 된 파일이며, 대상 폴더를 반영하는 Document 폴더에 저장되고 경고가 표시됩니다. 자격 증명과 공유 토큰은 폴더 경로에서 제거됩니다 |
| 대상: 바인딩되지 않은 이메일 | 경고와 함께 CSV |
| 대상: 사용할 수 없는 바인딩 | 원래 대상을 명시한 경고와 함께 CSV |

변환은 소스 또는 대상 시스템에 연결하지 않습니다.
