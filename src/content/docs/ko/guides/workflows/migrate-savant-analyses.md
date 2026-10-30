---
title: Savant 분석 마이그레이션
description: Analyze 앱, REST API 또는 MCP에 연결된 AI 에이전트에서 Savant Labs 분석 내보내기 파일을 PlaidCloud 고급 워크플로로 변환하고, 소스를 바인딩한 다음 변환 보고서를 확인합니다.
sidebar:
  order: 31
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-savant-analyses.md
---

PlaidCloud는 Savant를 그대로 대체할 수 있습니다. 모든 Savant 에이전트, 식, 설정이 PlaidCloud로 변환되어 실행됩니다. 변환기는 Savant Labs 분석 내보내기 파일을 실행 가능한 고급 워크플로로 변환합니다. 각 Savant 에이전트를 워크플로 단계, 프로젝트 변수 또는 캔버스 개체에 매핑하고, 원래 그래프를 유지하며, 변환하지 못한 항목을 알려 주는 변환 보고서를 반환합니다.

변환은 지정한 내보내기 파일과, 소스에 바인딩한 파일의 헤더만 읽습니다. Savant 소스나 대상이 연결되는 시스템에는 접속하지 않습니다.

## PlaidCloud가 만드는 항목

- 각 Savant 에이전트는 상위 및 하위 관계가 유지된 상태로 대응하는 워크플로 단계가 됩니다. [Savant 변환 매트릭스](/ko/reference/savant-conversion-matrix/)에는 모든 에이전트와 매핑 티어가 나열되어 있습니다.
- Savant 분석 매개변수는 프로젝트 변수가 되며, 에이전트 설정 안에서 이를 참조하는 부분은 PlaidCloud 변수 구문으로 다시 작성됩니다.
- 메모와 그룹은 캔버스에 메모와 그룹으로 표시됩니다.
- 각 소스는 바인딩 방식에 따라 가져오기 단계가 되거나 기존 테이블을 읽습니다.
- 모든 Savant 에이전트 유형이 완전히 변환되며, 모든 옵션에 매핑이 있습니다. Savant 자체에서 실패하거나 문서화되지 않은 구성은 이름이 지정된 자리 표시자 단계로 표시됩니다. [변환되지 않은 구성의 자리 표시자](#변환되지-않은-구성의-자리-표시자)를 참조하십시오.

## 시작하기 전에

1. Savant에서 **Export JSON**으로 분석을 내보냅니다.
2. 읽을 수 있는 [문서 계정](/ko/guides/documents/adding-accounts/)에 `.json` 파일을 업로드합니다.
3. 워크플로를 받을 PlaidCloud 프로젝트를 선택합니다. 해당 프로젝트에 대한 쓰기 권한이 있어야 합니다.
4. 분석의 소스 파일을 읽을 문서 계정과 기본 폴더를 선택합니다.

## 분석 변환

Analyze 앱, REST API 또는 MCP 도구 카탈로그에서 변환할 수 있습니다. 세 가지 방법 모두 같은 필드를 사용합니다.

### Analyze 앱

1. **Analyze**를 열고 **도구 → Savant 분석 가져오기**를 선택합니다.
2. **대상 프로젝트**와 문서 계정에 업로드한 **Savant 내보내기 파일(.json)** 을 선택합니다.
3. **소스 로드**를 선택합니다. 창에 내보내기 파일의 각 소스 노드가 나열됩니다.
4. 소스를 이미 가지고 있는 데이터에 연결하려면 소스를 선택하고 **바인딩…** 을 선택합니다. 대상 프로젝트의 테이블을 읽으려면 **프로젝트 테이블**을, 문서 계정의 파일을 읽으려면 **문서**를 선택합니다(Excel의 경우 워크시트 이름은 선택 사항). 바인딩을 제거하려면 **바인딩 해제**를 선택합니다.
5. **바인딩되지 않은 소스 디렉터리**에서 바인딩되지 않은 소스의 파일을 읽을 문서 계정과 기본 폴더를 선택합니다.
6. **변환 옵션**에서 **워크플로 유형**을 선택하고 **변환되지 않은 자리 표시자 허용** 여부를 선택합니다. **개체 접두사**에서 필요에 따라 워크플로, 단계, 테이블 접두사를 설정합니다.
7. **변환**을 선택합니다.

변환이 완료되면 창에 변환 보고서가 표시됩니다. 보고서에는 워크플로 이름과 테이블 접두사, 경고, 바인딩되지 않은 소스의 파일을 업로드할 문서 경로 표, 검토가 필요한 단계가 들어 있습니다. 소스 목록을 불러올 수 없으면 소스마다 노드 ID와 바인딩할 테이블의 `analyzetable_` ID가 있는 행을 추가하십시오.

### 필드

REST API와 MCP 도구는 다음 필드를 사용합니다.

| 필드 | 필수 | 용도 |
| --- | --- | --- |
| `source_account_id` | 예 | Savant 내보내기 파일이 있는 문서 계정입니다. |
| `source_file_path` | 예 | 해당 계정 내 내보내기 파일의 경로입니다. |
| `project_id` | 예 | 워크플로를 만들 프로젝트입니다. |
| `document_account_id` | 예 | 바인딩되지 않은 소스를 읽을 문서 계정입니다. |
| `document_account_path` | 예 | 해당 계정에서 바인딩되지 않은 소스를 읽을 기본 폴더입니다. 비어 있거나 `/`이면 계정 루트이며, 앞의 `/`는 무시됩니다. `..` 또는 점으로 시작하는 세그먼트, 중괄호, 드라이브 문자나 URL 스키마, 제어 문자가 있는 경로는 거부됩니다. |
| `workflow_prefix` | 아니요 | 워크플로 이름에 추가할 접두사입니다. |
| `step_prefix` | 아니요 | 단계 이름에 추가할 접두사입니다. |
| `table_prefix` | 아니요 | 테이블 이름에 추가할 접두사입니다. 기본값은 워크플로 자체 이름입니다. 기존 테이블 이름을 재사용하게 되는 접두사는 아무것도 만들기 전에 거부됩니다. 사용된 접두사는 변환 보고서에 반환됩니다. |
| `workflow_type` | 아니요 | `advanced`(기본값)는 그래프를 DAG 캔버스에 배치합니다. `standard`는 순차적인 단계 목록을 만듭니다. |
| `source_bindings` | 아니요 | 소스를 기존 데이터에 바인딩합니다. [소스 바인딩](#소스-바인딩)을 참조하십시오. |
| `destination_bindings` | 아니요 | 대상을 문서 계정, 연결 테이블, Google 시트, Tableau 데이터 소스, Slack 채널 또는 이메일 수신자로 보냅니다. REST와 MCP에서만 사용할 수 있습니다. [대상](#대상)을 참조하십시오. |
| `api_bindings` | 아니요 | API 에이전트의 상대 URL이 향할 위치(기본 URL 또는 REST 연결)를 지정합니다. REST와 MCP에서만 사용할 수 있습니다. [API 요청 바인딩](#api-요청-바인딩)을 참조하십시오. |
| `allow_unconverted_placeholders` | 아니요 | 자리 표시자가 실행 시점에 하는 동작을 제어합니다. [변환되지 않은 구성의 자리 표시자](#변환되지-않은-구성의-자리-표시자)를 참조하십시오. |

### REST

필드를 JSON 본문으로 다음 주소에 전송합니다.

```text
POST /rest/v1/analyze/savant/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/savant/quarterly-margin.json",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/savant-inputs"
}
```

`source_bindings`를 만들기 전에 내보내기 파일의 소스 노드를 나열하려면 `source_account_id`와 `source_file_path`를 다음 주소에 전송합니다.

```text
POST /rest/v1/analyze/savant/sources
```

응답의 각 항목에는 소스의 `node_id`, `name`, `connector`가 있습니다.

### MCP

MCP에 연결된 AI 에이전트는 같은 필드로 `savant_convert` 도구를 호출합니다. 에이전트를 연결하려면 [AI 에이전트(MCP)](/ko/integrations/ai-coding-agents/)를 참조하십시오. 이 도구는 프로젝트를 변경하므로 승인하기 전에 호출 내용을 검토하십시오.

## 변환 시점 바인딩

Savant 내보내기 파일에는 데이터, 자격 증명, 연결이 들어 있지 않으므로, 변환 시점 매개변수 세 가지로 이를 사용자의 환경에 연결합니다. 각 매개변수는 Savant 노드 ID 또는 이름에서 대상으로 이어지는 맵이며, 사용할 수 없는 바인딩이 있으면 아무것도 만들기 전에 전체 변환이 거부됩니다.

| 매개변수 | 바인딩 대상 | 섹션 |
| --- | --- | --- |
| `source_bindings` | 소스 에이전트를 테이블 또는 파일에 바인딩 | [소스 바인딩](#소스-바인딩) |
| `destination_bindings` | 대상 에이전트를 파일, 테이블, 시트, Tableau 데이터 소스, Slack 채널 또는 이메일에 바인딩 | [대상](#대상) |
| `api_bindings` | 상대 URL이 있는 API 에이전트를 기본 URL 또는 REST 연결에 바인딩 | [API 요청 바인딩](#api-요청-바인딩) |

## 소스 바인딩

Savant 내보내기 파일에는 데이터의 출처가 기술되어 있지만 데이터와 자격 증명은 들어 있지 않습니다. `source_bindings`를 사용하여 각 소스를 PlaidCloud에 이미 있는 데이터에 연결합니다. 키는 소스의 노드 ID, 데이터 세트 ID 또는 이름입니다. 값은 다음 중 하나입니다.

- 대상 프로젝트에 있는 테이블의 `analyzetable_` ID입니다. 변환된 워크플로가 해당 테이블을 직접 읽습니다.
- 문서 계정의 파일을 읽기 위한 `account`, `path`, 선택 사항인 `sheet`가 포함된 개체입니다.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "Budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

읽을 수 없는 바인딩은 거부됩니다. 어떤 소스와도 일치하지 않는 키는 경고로 보고됩니다.

내보내기 파일의 소스 파일 경로는 `/`로 시작하거나 `.archive` 같은 점 폴더를 거쳐도 변환됩니다. XML을 읽는 소스는 XML 텍스트를 변환하며, XML 문서 소스에는 Savant의 파일 컨텍스트 열도 함께 들어갑니다.

### 바인딩되지 않은 소스

바인딩이 없는 소스는 아직 데이터가 없는 가져오기 단계가 되며, 변환 보고서에 이에 대한 경고가 표시됩니다. 이 단계는 다음 위치에서 읽습니다.

```text
<document_account_path>/savant/<workflow id>/<source name>.csv
```

해당 경로에 파일을 업로드한 다음 워크플로를 실행하십시오. 파일이 없는 동안에는 가져오기 단계가 경고와 함께 완료되고 빈 테이블을 만들며, 워크플로는 계속 진행됩니다.

## 에이전트 변환 방식

대부분의 에이전트는 직접 만들었을 법한 단계로 변환됩니다. [Savant 변환 매트릭스](/ko/reference/savant-conversion-matrix/)에 모든 에이전트가 나열되어 있습니다. 다음 에이전트는 추가로 주의가 필요합니다.

| Savant 에이전트 | 변환 결과 | 주의 사항 |
| --- | --- | --- |
| Infer Agent(`gen_ai`, 그리고 LLM 서비스가 있는 레거시 `service`) | **프롬프트** 작업이 있는 [AI/NLP](/ko/reference/workflow-steps/text-documents/nlp-ai/) 단계입니다. 프롬프트는 입력 필드에 대해 행마다 한 번 실행되고, 답변은 모든 입력 열 옆의 **AI Answer** 열에 들어갑니다. 행 제한은 **최대 행 수**가 되며, 소스가 비어 있으면 경고하고 빈 테이블을 씁니다. **Max New Rows**는 새로 추가된 행에만 답하고 이전 실행의 답변은 유지합니다. | LLM이 답변하므로 출력이 Savant와 바이트 단위로 같지 않으며 실행마다 달라질 수 있습니다. 호출마다 비용이 발생합니다. [AI 공급자](#ai-공급자)를 참조하십시오. 실패한 배치는 행을 유지하되 답변을 비워 두고 경고합니다. |
| Vision Agent(`vision`) | [Document Read Blob](/ko/reference/workflow-steps/text-documents/document-blob-extract/) 단계, [Image OCR](/ko/reference/workflow-steps/text-documents/image-ocr/), 그다음 AI/NLP **프롬프트** 작업입니다. 공급자가 해당 유형과 크기를 허용하면 각 문서가 이미지 또는 PDF로 공급자에게 전달됩니다. 허용하지 않으면 PDF 텍스트 레이어 또는 OCR 텍스트를 전송합니다. | Infer Agent와 같은 LLM 주의 사항이 적용됩니다. 문서 전체가 PlaidCloud에서 공급자로 전송되며 변환 시 경고가 표시됩니다. TIFF와 BMP 파일은 OCR 텍스트로 전송되며 최대 문서 크기 설정은 없습니다. 찾을 수 없는 문서는 건너뛰고 단계가 해당 경로와 함께 경고합니다. |
| API Agent(`apiService`, 그리고 API 서비스가 있는 레거시 `service`) | 입력 행마다 요청 하나를 보내는 [REST 요청](/ko/reference/workflow-steps/general/rest-request/) 단계와, 모든 입력 행을 유지하는 조인입니다. 원시 응답 본문은 텍스트 열에, 상태는 그 옆 열에 들어갑니다. 기간당 할당량은 소수 값의 **초당 최대 요청 수**가 됩니다. 상대 URL은 `api_bindings`로 바인딩한 기본 URL 또는 REST 연결에 결합됩니다. 행 필드에서 가져오는 호스트, 포트, 경로는 행마다 채워집니다. 다음 URL, Link 헤더, 오프셋, 페이지 방식의 페이징을 따라가며, 페이징 값(시작, 페이지 크기 또는 매개변수 이름)은 입력 필드나 매개변수에서 가져올 수 있습니다. | GET 이외의 메서드는 워크플로를 실행할 때마다 입력 행마다 한 번씩 실제 시스템에 대해 실행되므로 첫 실행 전에 대상을 확인하십시오. GET이 아닌 요청은 자동으로 재시도되지 않습니다. 실패한 요청은 상태와 함께 행으로 남습니다. 자격 증명이 있는 요청은 행 필드에서 호스트를 가져올 수 없습니다. 자격 증명은 [자격 증명이 있는 API 단계](#자격-증명이-있는-api-단계)에 설명된 대로 처리됩니다. |
| Recursion Agent(`hierarchy`) | 각 행을 상위 체인을 따라 임의의 깊이까지 올라가며 탐색한 다음 루트까지의 경로(자기 자신 포함)에 있는 ID에 대해 각 노드를 집계하는 [Hierarchy Closure](/ko/reference/workflow-steps/tables/table-hierarchy-closure/) 단계입니다. Depth와 Path를 기록합니다. 상위가 비어 있거나 자기 자신을 상위로 지정한 행은 루트입니다. | 상위 ID에 루프가 있으면 반복되는 노드에서 멈추고 그 앞의 모든 상위 항목을 유지합니다. 상위가 여러 개인 행은 각각 자신의 값을 유지합니다. |
| Search and Replace(`search_replace`) | 선택한 텍스트 열에 각 규칙을 순서대로 적용하는 [Table Extract](/ko/reference/workflow-steps/tables/table-extract/)이며, 대/소문자 구분 여부와 단어 단위 여부를 지정할 수 있습니다. 각 규칙은 자신의 모드로 실행됩니다. 일치한 텍스트 교체, 텍스트가 포함된 경우 셀 전체 교체, 정확히 일치하는 경우 셀 전체 교체, 셀에 추가가 있습니다. | 규칙은 패턴이 아닌 리터럴 텍스트입니다. |
| Split(`split`) | [Split Text](/ko/reference/workflow-steps/tables/table-split-text/) 단계입니다. 임의 길이의 리터럴 구분자로 열 또는 행으로 분할하며, 열 수는 워크플로가 실행될 때 데이터에서 결정합니다. | 없음. |
| Time Series(`rollup`) | 기간 식으로 그룹화하는 Table Extract이며, 레코드가 없는 기간을 0으로 채우기 위해 [Period Spine](/ko/reference/workflow-steps/tables/table-period-spine/), 안티 조인, 유니온을 사용합니다. | 날짜가 NULL인 레코드는 제외됩니다. 스파인은 100,000개 기간에서 멈춥니다. |
| Format(`format`) | 이름 바꾸기, 형식 변경, 숨기기, 채우기를 적용하는 Table Extract 또는, 이름을 행으로 바꾸기에는 [Promote Header](/ko/reference/workflow-steps/tables/table-promote-header/) 단계입니다. | 텍스트가 아닌 열의 채우기는 기본값을 열의 형식으로 변환합니다. 열이 선언되지 않은 소스에서 헤더를 승격하면 CSV, Excel, XLS, JSON, Parquet, Avro 파일의 모든 열을 읽습니다. [선언된 열이 없는 파일](#선언된-열이-없는-파일)을 참조하십시오. |
| Spatial Match Agent(`spatial_match`) | intersects, within, contains, touches, crosses, overlaps, equals, disjoint에는 여러 규칙을 결합한 [Spatial Match (executor)](/ko/reference/workflow-steps/spatial/spatial-match-executor/) 단계, 교차 일치에는 Cross Join, 최근접 일치에는 [Find Nearest](/ko/reference/workflow-steps/spatial/spatial-find-nearest/)입니다. | 최근접 일치는 Savant와 같이 대원 거리로 순위를 매기고 필터링합니다. 다른 규칙과 결합된 최근접 규칙은 먼저 가장 가까운 레코드를 찾은 다음 다른 규칙을 적용합니다. AND이면 모든 규칙을 충족하는 레코드를 유지하고, OR이면 가장 가까운 레코드와 다른 규칙에 일치하는 레코드의 합집합을 취합니다. 개수나 최대 거리가 없는 최근접 규칙은 가장 가까운 레코드 하나를 유지합니다. 거리 이내 일치도 변환되며, 규칙에 단위가 없으면 킬로미터를 사용하고 점뿐 아니라 모든 지오메트리 사이의 측지 거리를 측정합니다. 구문 분석할 수 없는 지오메트리는 경고와 함께 NULL이 되거나 일치하지 않습니다. |
| Spatial Summarize Agent(`spatial_summarize`) | 합집합, 교집합, 경계 상자에는 [공간 결합](/ko/reference/workflow-steps/spatial/spatial-combine/), 기하학적 중심과 선 또는 다각형 생성에는 [Spatial Centroid](/ko/reference/workflow-steps/spatial/spatial-centroid/), [Spatial Point to Line](/ko/reference/workflow-steps/spatial/spatial-point-to-line/), [Spatial Line to Polygon](/ko/reference/workflow-steps/spatial/spatial-line-to-polygon/)입니다. | 3개 미만의 점으로 만든 다각형은 빈 다각형입니다. |
| Destination Agent(`destination`) | 바인딩한 대상으로의 내보내기 단계이며, 바인딩하지 않으면 프로젝트 테이블 또는 파일입니다. [대상](#대상)을 참조하십시오. | [제한이 남아 있는 사항](#what-stays-limited)을 참조하십시오. |

`GEO_POINT`, `GEO_TYPE`, `GEO_SPATIAL_DISTANCE`는 식으로 변환됩니다. 전체 식이 `GEO_AREA`나 `GEO_UNION` 같은 다른 `GEO_*` 함수인 편집은 [Spatial Info](/ko/reference/workflow-steps/spatial/spatial-info/)를 포함하여 해당하는 공간 단계로 변환됩니다. 지오메트리는 WKT 텍스트로 전달됩니다. 마일 단위의 `GEO_AREA`, `GEO_PERIMETER`, `GEO_SPATIAL_DISTANCE`는 법정 마일을 사용합니다.

Vision 에이전트가 읽는 문서처럼 바이너리 파일을 읽는 소스는 바인딩한 문서 또는 바인딩되지 않은 소스 경로에서 예상되는 파일에 대한 문서 추출로 변환됩니다.

## AI 공급자

Infer 또는 Vision 에이전트는 LLM 연결을 사용하는 AI/NLP 단계로 변환됩니다. 변환기는 Anthropic, OpenAI, Gemini, Azure OpenAI, Grok, GitHub Models를 지원합니다.

- 변환기는 가져오는 사용자가 볼 수 있는 LLM 연결 중에서 에이전트가 지정한 공급자와 모델에 맞는 연결을 선택합니다. 사용자가 볼 수 없는 연결은 지정하지 않습니다. AI 어시스턴트(MCP)를 통하는 경우 어시스턴트의 사용자가 볼 수 있는 연결을 의미합니다.
- 공급자에 보이는 연결이 없거나 Savant의 공급자와 일치하는 PlaidCloud 항목이 없는 경우(클라우드 호스팅 모델 API 또는 Savant 워크스페이스의 자체 키 공급자), 사용자가 볼 수 있다면 단계는 워크스페이스 기본 연결을 사용합니다. 그렇지 않으면 연결을 비워 두고, 단계가 실행될 때 워크스페이스 기본값을 사용합니다. 어느 경우든 변환 보고서에 경고가 표시되므로, 다른 연결이 답변해야 한다면 단계에서 연결을 선택하십시오.

## 대상

Savant 대상은 받은 테이블을 바인딩한 대상에 씁니다. REST 본문이나 MCP 호출에서 `destination_bindings`로 대상을 바인딩합니다. 키는 대상의 노드 ID 또는 이름입니다. Analyze 창에서는 대상을 바인딩할 수 없으므로 그곳에서 변환한 대상은 [바인딩되지 않은 대상](#바인딩되지-않은-대상)에 설명된 바인딩 없는 결과를 씁니다.

| 대상 | 바인딩 | 결과 |
| --- | --- | --- |
| 문서 계정 | `{account, path[, file_name]}` | 대상 종류에 따라 CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF 또는 Tableau Hyper 파일입니다. 해당 계정에 대한 문서 저장소 쓰기 권한이 필요합니다. |
| 연결의 테이블 | `{connection, table[, schema, replace]}` | [Export: External Database Tables](/ko/reference/workflow-steps/export/export-external-tables/) 단계입니다. 연결 쓰기 권한이 필요합니다. 테이블을 교체하려면 `replace: true`가 필요합니다. |
| Google Sheets | `{connection, spreadsheet_name[, sheet_name, replace]}` 또는 `{connection, spreadsheet_id[, sheet_name, replace]}` | Google Sheets 연결에서 [Export to Google Spreadsheet](/ko/reference/workflow-steps/export/export-to-google-spreadsheet/) 단계입니다. 탭은 기본적으로 대상이 지정한 탭이며, 없으면 `Sheet1`입니다. 시트의 행을 교체하는 대상은 탭을 지우므로 `replace: true`가 필요합니다. |
| Tableau | `{account, connection[, path, file_name, replace, datasource_name, tableau_project]}` | 계정 폴더에 기록된 Tableau Hyper 추출과, 이어서 [Tableau 연결](/ko/reference/connectors/collaboration/tableau/)에서 [Publish to Tableau](/ko/reference/workflow-steps/export/export-to-tableau/) 단계입니다. 데이터 소스를 교체하거나 일치 키를 기준으로 행을 변경하려면 `replace: true`가 필요합니다. |
| Slack | `{connection[, channel]}` | CSV가 문서 계정에 기록된 다음 [Notify via Slack](/ko/reference/workflow-steps/notifications/notify-via-slack/) 단계가 이를 채널에 업로드합니다. 연결에 봇 토큰이 있어야 하며, 채널은 바인딩에서 가져오거나 그렇지 않으면 내보내기 파일에서 가져온 채널 ID여야 합니다. |
| 이메일 | `{email_to: [...]}`, 내보내기 파일에 나열된 수신자도 사용하려면 `email_export_recipients: true` | CSV가 첨부 파일로 메일 전송됩니다. 이메일 쓰기 권한이 필요합니다. |

Sheets, Tableau 또는 Slack 연결은 테이블 연결과 같은 방식으로 확인됩니다. 해당 연결을 볼 수 있고 연결 쓰기 권한이 있어야 하며, 그렇지 않으면 변환이 거부됩니다.

### 쓰기 모드

- 추가하는 파일 또는 테이블 대상은 이전 파일을 다시 읽어 새 행과 함께 다시 씁니다. 덮어쓰지 않습니다.
- upsert, update, groupReplace 대상은 대상의 일치 키를 기준으로 병합합니다. 파일 또는 테이블은 다시 읽어서 다시 쓰고, Tableau 데이터 소스는 일치하는 행이 제자리에서 변경됩니다.
- 추가와 병합은 값별로 분할된 기존 파일, 헤더가 없는 파일(행을 위치로 일치), 왼쪽 위 셀에 고정된 Excel 파일, UTF-8이 아닌 문자 집합의 파일에서도 동작합니다. 분할은 각 값이 기록된 파일을 다시 읽어 그 안에서 병합하며 다른 파일은 그대로 둡니다.
- Tableau 대상은 Savant의 모드를 [Publish to Tableau](/ko/reference/workflow-steps/export/export-to-tableau/#모드)의 여섯 가지 모드에 매핑합니다. append와 insert는 행을 추가하고, replace는 덮어쓰며, upsert, update, groupReplace는 키를 기준으로 일치시킵니다. 기존 데이터를 변경하는 모드는 바인딩에 `replace: true`가 있을 때만 게시하며, 그렇지 않으면 대상이 새 데이터 소스를 게시하고 보고서에 이를 알립니다.
- 출력 인코딩이 있는 대상은 해당 Java 문자 집합으로 파일을 씁니다. 문자 집합에 없는 문자는 Savant처럼 `?`로 기록됩니다. Java 별칭, CESU-8, 바이트 순서 표시 형식이 허용됩니다. 일부 드문 문자 집합(예: `x-ISCII91` 또는 `JIS_X0212`)은 쓸 수 없으며, 이 경우 파일은 UTF-8로 기록되고 보고서에 경고가 표시됩니다. UTF-8이 아닌 문자 집합의 분할은 폴더로 변환됩니다.
- 내보내기 파일 이름은 바인딩한 폴더 안에 있어야 합니다.

### AI 호출자가 바인딩할 수 있는 항목

AI 어시스턴트(MCP)를 통한 변환은 같은 형태를 바인딩하되 일부 항목은 제외되며, 각각에 대해 해당 항목을 알리는 경고가 표시됩니다.

| 제외되는 항목 | 대신 일어나는 일 |
| --- | --- |
| 테이블, 시트 또는 Tableau 데이터 소스의 `replace` | 추가하는 대상은 바인딩한 테이블 또는 시트에 계속 추가합니다. 교체하는 대상은 CSV를 씁니다. Tableau 대상은 새 데이터 소스를 게시합니다. |
| 이메일 수신자 | 이메일 대신 CSV가 기록됩니다. |
| Slack | Slack 게시 대신 CSV가 기록됩니다. |

이러한 항목을 바인딩하려면 Analyze 앱 또는 REST API에서 변환하거나, 어시스턴트를 거치지 않고 직접 로그인하십시오.

### 바인딩되지 않은 대상

바인딩이 없는 대상은 PlaidCloud의 대응 항목에 쓰고 원래 대상을 밝히는 **Destination target unbound** 경고를 표시합니다. 변환은 대상 시스템에 접속하지 않습니다.

| 대상 | 결과 |
| --- | --- |
| 데이터베이스, 웨어하우스 또는 SaaS 대상(Oracle, 일반 데이터베이스, Looker Studio, NetSuite, SAP, 그리고 연결이 바인딩되지 않은 Google Sheets, Tableau 또는 Slack) | 대상 노드의 이름을 딴 프로젝트의 테이블입니다. |
| 파일 저장소(S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | 바인딩되지 않은 소스용으로 지정한 계정 아래 문서 폴더에 대상의 파일 형식으로 기록된 파일입니다. 폴더는 대상 폴더를 그대로 따릅니다. 자격 증명과 공유 토큰은 경로에서 제거됩니다. |
| 이메일 | 바인딩되지 않은 소스용으로 지정한 문서 계정의 CSV입니다. |

경고는 실제 대상에 도달하기 위해 무엇을 바인딩해야 하는지 알려 줍니다. 바인딩을 사용할 수 없는 대상은 CSV를 쓰고 원래 대상이 메시지에 포함된 **Fallback, target not written** 경고를 표시하므로, 해당 CSV를 사용하기 전에 확인하십시오. 일반 CSV 대상은 자체 파일을 씁니다.

### 분할 대상

필드 값마다 파일, 하위 폴더 또는 탭을 쓰는 대상은 CSV, Excel, Parquet, PDF 파일과 Google Sheets 탭을 분할합니다.

- **Parquet 및 PDF.** 값마다 파일 하나입니다.
- **Google Sheets.** 값마다 탭 하나입니다.
- **템플릿.** 템플릿 통합 문서가 모든 값의 통합 문서의 기반이 됩니다. 템플릿이 없으면 경고하고 템플릿 없이 통합 문서를 씁니다.
- **Null 값.** NULL 분할 값은 삭제되지 않고 자체 파일 또는 탭에 기록됩니다.
- **입력에 없는 필드.** 입력에 없는 필드에 대한 분할 또는 정렬은 Savant가 이에 대해 실패하므로 이름과 함께 거부됩니다.
- **값에 포함된 `/` 또는 `\`.** 슬래시 또는 백슬래시가 포함된 분할 값은 파일 또는 탭 이름이 될 수 없으므로 정리됩니다. 변경된 값에는 파일 확장명 앞에 `-`와 값의 MD5 해시 첫 6자로 이루어진 고정 여섯 문자 접미사가 붙습니다. 변경이 필요 없는 값은 이름이 유지됩니다.

### 내보낸 값과 행 순서

- **일반 숫자와 불리언.** CSV, TSV, TXT 내보내기는 숫자를 일반 숫자로, 불리언을 `true`와 `false`로 기록하며 타임스탬프에 `+00:00`을 붙이지 않습니다.
- **안정적인 행 순서.** 정렬하는 대상은 실행할 때마다 같은 행 순서로 기록합니다. 동순위는 매번 같은 방식으로 처리되며, 분할 및 파트 경로도 정렬합니다. Parquet, Google Sheets, Tableau, 테이블 대상은 행 순서를 유지하지 않습니다.

### Excel 옵션

Excel 대상은 다음 옵션을 매핑합니다.

- **필드 값별 탭.** 필드의 각 값이 시트가 됩니다. 빈 값은 `Sheet1`로 가고, 이름이 충돌하는 시트에는 숫자 접미사가 붙습니다.
- **템플릿에서 형식 가져오기.** 실행할 때마다 먼저 같은 폴더의 `<name>_template.xlsx`를 통합 문서 위에 복사한 다음 그 안에 쓰므로 통합 문서는 항상 교체됩니다. 템플릿이 없으면 복사 시 경고하고 템플릿 없이 통합 문서를 씁니다.
- **왼쪽 위 셀.** 행이 해당 셀에서 시작하여 통합 문서에 기록됩니다.
- **`create` 모드.** 실행할 때마다 대상의 쓰기 모드에 따라 파일을 씁니다.

## API 요청 바인딩

`/v2/customers`처럼 URL이 상대 경로인 API 에이전트에는 요청을 보낼 호스트가 없습니다. `api_bindings`로 호스트를 바인딩하십시오. 키는 API 노드의 ID 또는 이름이며, 자체 바인딩이 없는 모든 API 노드에는 `*`를 사용합니다. 값은 다음 중 하나입니다.

- 문자열 또는 `{"base_url": "https://host/path"}` 형태의 기본 URL입니다. 상대 URL이 여기에 결합됩니다. URL은 공개 호스트의 `http` 또는 `https`여야 하며 사용자, 쿼리, 프래그먼트가 없어야 합니다.
- `{"connection": "<REST connection id>"}`입니다. 요청은 해당 [REST 연결](/ko/reference/connectors/rest/generic-rest/)의 호스트로 전송되며 그 자격 증명을 사용합니다. 연결 쓰기 권한이 필요하며, 연결은 볼 수 있는 REST 연결이어야 합니다.

```json
"api_bindings": {
  "*": "https://api.example.com/v1",
  "Customers": { "connection": "<REST connection id>" }
}
```

일치하지 않는 키는 경고이며, 사용할 수 없는 바인딩은 거부됩니다. 바인딩이 없는 상대 URL은 이름이 지정된 자리 표시자로 남습니다.

연결 쓰기 권한이 없는 AI 어시스턴트(MCP)는 연결 바인딩이 경고와 함께 무시되며, 결합되었을 상대 URL은 자리 표시자로 남습니다. 기본 URL을 바인딩하거나 Analyze 앱 또는 REST API에서 변환하십시오.

입력 필드에서 가져오는 호스트, 포트, 경로에는 바인딩이 필요하지 않습니다. 행마다 채워지며 각 값은 사용 시점에 확인되고, 보고서에는 행이 지정할 수 있는 호스트가 나열됩니다. 자격 증명이 있는 요청은 행 필드에서 호스트를 가져올 수 없습니다. 데이터가 선택한 호스트로 자격 증명을 보내는 것은 거부됩니다.

페이징도 변환됩니다. 응답의 다음 페이지 URL, `Link` 헤더, 오프셋, 페이지 번호는 각각 모든 페이지를 읽는 [REST 요청](/ko/reference/workflow-steps/general/rest-request/) 단계의 페이징 모드가 됩니다. 페이징 값은 입력 필드(`{{Field}}`) 또는 매개변수(`{{Param}}`)에서 가져올 수 있으며, `10.0`처럼 숫자 텍스트로 작성된 값은 숫자로 읽힙니다.

## 자격 증명이 있는 API 단계

API 에이전트의 헤더, URL 경로, 쿼리 또는 본문에 있는 자격 증명은 가져오기가 만드는 PlaidCloud REST 연결로 이동합니다. REST 요청 단계가 해당 연결을 참조하므로 자격 증명이 단계에 남지 않습니다.

- 응답의 `connections` 아래에 가져오기가 만들거나 재사용한 연결이 나열되며 가져오기 보고서에도 이름이 표시됩니다. 같은 분석을 다시 가져오면 다른 연결을 만들지 않고 같은 연결을 재사용합니다.
- URL 사용자 정보와 헤더의 자격 증명은 연결 자체의 인증 필드 또는 기본 헤더로 들어갑니다. 경로, 쿼리, 본문의 비밀 값은 연결에 암호화되어 저장되며, 해당 연결 자체의 `https` 호스트로 가는 요청에 한해 실행 시점에 채워집니다.
- 암호화되지 않은 `http://` 엔드포인트는 자격 증명과 함께 변환되지 않습니다. 자격 증명은 제외되고 변환 보고서에 복사되지 않았다는 경고가 표시됩니다.
- AI 어시스턴트(MCP)를 통한 가져오기는 연결을 만들지 않습니다. 자격 증명이 제외되고 경고가 이를 알립니다. 대신 Analyze 앱 또는 REST API에서 가져오거나, REST 연결에 자격 증명을 직접 추가하여 단계에서 선택하십시오.
- 연결 쓰기 권한이 없는 사용자도 같은 결과를 얻습니다. 자격 증명이 제외되고 경고가 표시됩니다.
- API 자격 증명 슬롯만 매개변수를 연결로 이동시킵니다. API 자격 증명이 들어가는 헤더, 쿼리, 경로 또는 본문에서 사용된 파이프라인 매개변수는 연결의 암호화된 `secret_values`로 이동하며, 단계는 연결을 통해 이를 참조합니다. 매개변수 이름과 관계없이 워크플로 변수로 만들어지지 않습니다.
- 이름에 비밀 관련 단어(`password`, `token`, `secret`, `key` 등. 단, `key`는 `sort`나 `partition` 같은 데이터 관련 단어 뒤에 오면 제외)가 포함된 그 밖의 모든 매개변수는 값이 비어 있는 워크플로 변수가 되고 경고가 표시됩니다. `api_key_2` 같은 이름도 비워집니다. 가져온 후 프로젝트 변수에 값을 설정하십시오.
- `max_tokens`처럼 개수나 제한을 나타내는 이름의 매개변수는 값이 유지됩니다.
- 수식, 필터 또는 교체 값에 입력된 비밀 값은 단계에서 제외되고 변환 보고서에 경고가 표시됩니다. 경로, URL, 40자 또는 64자 16진수 다이제스트는 그 일부나 비밀 이름이 달리 나타내지 않는 한 유지됩니다. 폴더 공유 링크와 수신자 이메일 주소는 경고나 메모에 표시되지 않습니다.
- 자격 증명을 그대로 돌려주는 응답은 받은 그대로 저장됩니다. 이러한 요청의 출력 테이블은 민감한 데이터로 취급하십시오.

## JWT_ENCODE

`JWT_ENCODE`는 [JWT Encode](/ko/reference/workflow-steps/tables/table-jwt-encode/) 단계로 변환됩니다. 리터럴 서명 키는 단계에 바인딩된 전용 연결에 들어가고 토큰은 실행 시점에 서명되므로 키가 단계 구성에 나타나지 않습니다. AI 어시스턴트를 통하거나 연결 쓰기 권한이 없으면 키가 제외되고 토큰이 NULL이 되며, 경고가 연결을 만들 권한으로 다시 가져오라고 안내합니다.

## 데이터 행을 열 헤더로 승격

**replace names with row**로 설정한 Format 에이전트는 [Promote Header](/ko/reference/workflow-steps/tables/table-promote-header/) 단계로 변환됩니다. 실행 시점에 1부터 센 선택된 행이 열 이름이 되고 그 행은 제거됩니다. 레코드 순서가 없는 소스에는 메모가 표시되는데, 어느 행이 열 이름이 되는지가 실행마다 달라질 수 있기 때문입니다. 해당 행이 이름을 지정하지만 이후 어떤 단계에서도 언급되지 않는 열은, 읽는 열을 나열하는 단계 이후로는 전달되지 않습니다.

## 선언된 열이 없는 파일

선언된 열이 없는 소스는 다음 열을 유지합니다.

- 가져올 때 바인딩된 CSV, TSV 또는 TXT 소스는 파일 헤더의 모든 열을 유지합니다.
- 그 밖의 파일 형식과 바인딩되지 않은 모든 소스는 이후 단계에서 이름을 지정한 열만 유지하며 변환 보고서에 경고가 표시됩니다.
- 이러한 소스에서 승격된 헤더는 CSV, Excel, XLS, JSON, Parquet, Avro 파일의 모든 열을 읽습니다.

이러한 소스가 승격된 헤더에만 연결되는 경우 가져오기는 모든 열을 위치로 읽는 [Import Delimited](/ko/reference/workflow-steps/import/import-delimited/) 단계입니다. 승격된 헤더 뒤에서 내보내거나 조인하는 단계는 실행 시점에 테이블에 있는 모든 열을 전달합니다([Table Extract](/ko/reference/workflow-steps/tables/table-extract/)의 **실행 시점에 지정된 열도 함께 전달** 참조).

## 알아 둘 동작

이러한 변환은 다음과 같이 동작합니다.

| 에이전트 | 동작 |
| --- | --- |
| Blend(`blend`) | OR로 결합된 조건자, contains, is-part-of를 기준으로 조인합니다. 내부 조인을 제외한 외부 블렌드와 일치하지 않는 출력은 해당하는 조인 스트림으로 변환됩니다. 모든 연산자에서 오른쪽의 중복 키는 출력에서 제거됩니다. |
| Dedupe(`deduplicate`) | **그룹화 기준** 그룹마다 키당 첫 번째 레코드를 유지합니다. 중복 플래그는 중복 그룹의 모든 구성원을 표시하며, 중복은 두 번째 스트림으로 보낼 수도 있습니다. 출력구를 하나만 연결하면 Savant와 같이 동작합니다. |
| Summarize(`summarize`) | 윈도 집계는 그룹을 축소하는 대신 모든 행에 집계값을 추가합니다. |
| Sample(`sample`) | 그룹별 또는 전체의 처음 N개 행, 무작위 비율 또는 행 수, 또는 N번째마다 한 행입니다. |
| Time Series(`rollup`) | 그룹별로 선택적 시작 날짜와 종료 날짜 사이의 일, 주, 월, 분기, 연, 10년 기간입니다. 월 기간은 `YYYY-MM`으로 표시되며 레코드가 없는 기간은 0으로 나타납니다. 날짜가 NULL인 레코드는 제외됩니다. |
| Pivot(`pivot`) | COUNT는 행을 셉니다. |
| XML(`xml`) | SELECT는 요소를 추출하고, 경로에는 네임스페이스를 포함할 수 있으며, TO_JSON은 XML을 JSON으로 변환합니다. 조건자, 특성 테스트, 와일드카드, `count()`, `name()`, `contains()` 같은 함수를 포함하여 모든 XPath 1.0 경로가 변환되며, [XML 구문 분석](/ko/reference/workflow-steps/tables/table-xml-parse/) 단계가 이를 XPath로 읽습니다. `processNs`가 꺼져 있으면 이름은 접두사를 포함하여 문자 그대로 일치시킵니다. 변환할 때 없는 XML 파일은 워크플로가 실행될 때 루트 요소를 확인합니다. |
| JSON(`json`) | 넓은 열로 평탄화합니다. 유효한 JSON이 아닌 텍스트는 NULL이 되고 배열은 텍스트로 나옵니다. |
| Split(`split`) | 열 또는 행으로 분할하며, 열 수는 워크플로가 실행될 때마다 데이터에서 읽습니다. |

다음 식 함수는 Savant의 결과를 따릅니다.

| 함수 | 동작 |
| --- | --- |
| `DATE_DIFF` | 주와 분기를 Savant와 같은 방식으로 계산합니다. |
| `PAD` | 대상 너비보다 긴 값을 자르지 않습니다. |
| 텍스트에 대한 `+` | 텍스트를 연결합니다. 선언된 형식이 없는 소스의 열은 숫자로 읽히므로 `+`가 더하기로 동작하며 메모가 이를 알립니다. |
| 행으로 분할 | 빈 조각을 행으로 유지합니다. |
| 정렬 없는 `LAST` | 행이 도착한 순서에서 마지막 행을 반환하며, 웨어하우스가 그 순서를 보장하지 않는다는 메모가 표시됩니다. |
| `JOIN_STR` | 소수는 Savant가 쓰는 방식 그대로, 끝에 0을 채우지 않고 결합합니다. |
| `JSON_FORMAT` | JSON을 보기 좋게 출력하며, Snowflake에서는 JSON을 한 줄로 압축하여 씁니다. |
| `JSON_SET` | Savant의 키 순서를 유지합니다. |
| `GREATEST` 및 `LEAST` | NULL 인수를 건너뜁니다. 모든 인수가 NULL일 때만 결과가 NULL입니다. |
| `ROUNDUP` | 다음 정수 단위로 올림하므로 음수는 0 방향으로 올림됩니다. -1.5는 -1이 됩니다. `ROUNDDOWN`은 변경되지 않습니다. |
| `DURING_DAYLIGHT_SAVING` 및 `DURING_STANDARD` | NULL을 입력하면 NULL이 출력됩니다. |
| 날짜 형식이 있는 `TO_TEXT` | 형식 토큰을 Savant와 같은 방식으로 읽습니다. `YYYY`, `w`, `u`는 ISO 주 연도, 주, 요일이며, 시간대 또는 연호 문자는 UTC 시간의 경우처럼 기록됩니다. |
| `TO_TEXT` 및 숫자-텍스트 출력 | `12.0000000000`이 아닌 `12` 같은 일반 숫자를 씁니다. |
| 숫자 패턴이 있는 `TO_TEXT` | Java `DecimalFormat`처럼 서식을 지정하며 짝수로 반올림(round half to even)하고, `##0.##E0` 같은 과학 표기 패턴도 지원합니다. |
| 행별 형식이 있는 `TO_TEXT` 및 날짜 구문 분석 | 각 행에서 형식을 읽습니다. |
| 소수 초, 좁은 월, 주 기반 날짜 토큰 | 변환됩니다. 주 토큰은 ISO 주로 읽힙니다. |
| 두 자리 연도(`yy`, `y`) | 현재 연도를 기준으로 80년 전부터 20년 후까지의 범위로 읽습니다. |
| `REGEX_MATCH` | 부분 일치입니다. 패턴이 텍스트 전체가 아니라 텍스트의 어느 위치에서든 일치합니다. |

`TO_TEXT`와 날짜 형식은 [Text Function](/ko/reference/workflow-steps/tables/table-text-function/) 단계에서 변환됩니다. 식 없이 컴파일된 단계만 있는 편집은 각 단계가 다음 단계로 이어지도록 순서대로 적용한 것으로 변환되며, 변환 보고서에 가정한 순서가 기록됩니다. 변환기는 Savant 자체에서 실패하거나 변환할 대상이 없는 항목을 이름과 함께 거부하며, 해당 단계는 자리 표시자가 됩니다. Transform 또는 Filter 식 안의 일반 집계 또는 윈도 함수(계산 또는 Summarize 안에서는 변환됨), `md5` 또는 `sha1`이 아닌 리터럴 알고리즘이 있는 `HASH`, PlaidCloud가 읽을 수 없는 정규식 구문(클래스 안의 클래스, 클래스 교집합 또는 알 수 없는 `\p{}` 속성), 식도 컴파일된 단계도 없는 Transform 편집(프롬프트만 있는 Copilot 편집 등), XPath 1.0이 아닌 XML 경로, 자격 증명이 있고 행 필드에서 호스트를 가져오는 API 요청이 해당합니다. [Savant 변환 매트릭스](/ko/reference/savant-conversion-matrix/#이름이-지정된-거부-항목)에 각 항목과 그 이유가 나열되어 있습니다.

`sha1`, `NOT_TRUE`, `LEVENSHTEIN`, 일광 절약 시간 함수(`DST`), n번째 일치를 가져오는 정규식 함수에 대해서도 식 함수가 변환됩니다. `DAY_OF_WEEK`는 일요일을 7로 번호를 매기고, `DAY_NAME`은 요일의 이름을 반환합니다.

## 변환 보고서 읽기

응답에 변환 보고서가 포함됩니다. 보고서에는 신뢰도가 높음, 보통, 낮음으로 변환된 단계 수와 변환되지 않은 단계 수의 요약, 경고, 변환기가 다른 노드에 흡수한 노드가 들어 있습니다. 워크플로를 실행하기 전에 읽어 보십시오. 모든 자리 표시자, 바인딩되지 않은 모든 소스와 일치하지 않는 바인딩, 사용된 테이블 접두사가 표시됩니다.

## 변환되지 않은 구성의 자리 표시자

변환기가 재현할 수 없는 구성은 에이전트의 이름이 있는 자리 표시자 단계로 만들어지며 변환 보고서에 이름이 표시됩니다. 변환기가 이름과 함께 거부하는 구문([Savant 변환 매트릭스](/ko/reference/savant-conversion-matrix/#이름이-지정된-거부-항목) 참조)이거나, API 구성이 누락된 경우처럼 내보내기 파일에 충분히 기술되지 않은 구성에 대해 자리 표시자가 나타납니다. 기본적으로 자리 표시자는 워크플로가 도달하면 실패하므로, 실제로 수행되지 않은 작업에 대해 실행이 성공으로 보고되는 일이 없습니다.

`allow_unconverted_placeholders`를 `true`로 설정하면 각 자리 표시자가 통과 단계로 가져와집니다. 그러면 실행이 해당 단계를 지나 계속되며, 자리 표시자의 출력은 입력과 같습니다. 그 결과가 중요하다면 네이티브 단계로 기능을 다시 구성하십시오.

## 변환된 워크플로 실행

1. 프로젝트에서 새 워크플로를 엽니다.
2. Savant 매개변수에서 비롯된 프로젝트 변수를 설정합니다.
3. 바인딩되지 않은 소스의 파일을 보고서에 표시된 경로에 업로드합니다.
4. 워크플로를 실행하고 각 단계의 출력 테이블을 검토합니다.

## 예외 사항

Savant와 알려진 차이는 다음뿐입니다. 변환 보고서는 해당하는 항목마다 이를 알려 줍니다.

- **날짜 형식.** `[`, `]`, `'`, `\`, `^` 리터럴이 포함된 형식으로 9999-12-30 또는 9999-12-31 텍스트를 읽는 `TO_DATE` 또는 `TO_DATETIME`은 웨어하우스가 보유하는 마지막 타임스탬프를 넘어가며, 보고서에 경고가 표시됩니다.
- **비밀 매개변수.** 이름에 비밀 관련 단어가 포함되거나 값이 자격 증명처럼 보이는 매개변수는 설계상 값이 빈 프로젝트 변수가 됩니다. 변수에 값을 설정하십시오.
- **선언되지 않은 매개변수.** 노드가 사용하지만 내보내기 파일에 선언되지 않은 매개변수는 값이 빈 프로젝트 변수로 들어옵니다.
- **Snowflake의 `JSON_FORMAT`.** 압축된 JSON을 한 줄로 씁니다.
- **행 순서.** 정렬된 Parquet, Google Sheets, Tableau, 테이블 대상은 행 순서를 유지하지 않습니다.
- **Google Sheets 및 Tableau.** 둘 중 하나에 게시하려면 `destination_bindings`로 해당 계정을 바인딩해야 합니다.

## 관련 가이드

- [Savant 변환 매트릭스](/ko/reference/savant-conversion-matrix/)
- [REST 연결](/ko/reference/connectors/rest/generic-rest/)
- [문서 계정 추가](/ko/guides/documents/adding-accounts/)
- [워크플로 변수 관리](/ko/guides/workflows/manage-workflow-variables/)
- [AI/NLP 단계](/ko/reference/workflow-steps/text-documents/nlp-ai/)
- [REST 요청 단계](/ko/guides/workflows/rest-request-step/)
- [워크플로 실행](/ko/guides/workflows/run-a-workflow/)
