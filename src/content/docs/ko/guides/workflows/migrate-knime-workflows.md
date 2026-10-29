---
title: KNIME 워크플로 마이그레이션
description: KNIME 워크플로(.knwf) 또는 워크플로 그룹(.knar)을 Analyze 앱, REST API 또는 MCP에 연결된 AI 에이전트에서 PlaidCloud 고급 워크플로로 변환하고, 입력과 연결을 바인딩하며, 변환 보고서를 읽는 방법을 설명합니다.
sidebar:
  order: 31.7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-knime-workflows.md
---

PlaidCloud는 KNIME을 그대로 대체할 수 있습니다. KNIME 노드 구성의 98.5%가 완전히 변환되며, 핵심 노드 유형 207개 중 205개가 Full입니다. 각 노드는 해당 노드의 작업을 수행하는 표준 PlaidCloud 워크플로 단계로 변환됩니다. 변환기는 KNIME 워크플로 아카이브를 실행 가능한 고급 워크플로로 바꾸고, 원래의 그래프를 유지하며, 설정해야 할 항목을 알려 주는 변환 보고서를 반환합니다. 모든 노드는 [KNIME 변환 매트릭스](/ko/reference/knime-conversion-matrix/)에서 확인할 수 있습니다.

변환은 지정한 아카이브만 읽습니다. KNIME 노드가 읽거나 쓰는 시스템에는 연결하지 않습니다.

변환은 한 번만 수행하는 작업입니다. 같은 아카이브를 다시 변환하면 새 워크플로가 만들어지며, PlaidCloud에서 수정한 내용은 이후의 내보내기 결과와 병합되지 않습니다.

## PlaidCloud가 만드는 항목

- KNIME 워크플로마다 고급 워크플로 하나. `.knwf`는 워크플로 하나를 만들고, `.knar`는 그룹에 포함된 워크플로마다 하나씩 만듭니다.
- 각 KNIME 노드는 그에 해당하는 워크플로 단계, 프로젝트 변수 또는 캔버스 개체가 되며, 업스트림과 다운스트림 관계가 유지됩니다. 메타노드와 컴포넌트는 워크플로에 풀어서 포함되므로, 그 안의 노드는 일반 단계로 실행됩니다.
- 흐름 변수와 Configuration 및 Widget 노드는 기본값을 가진 프로젝트 변수가 됩니다. 변환 시점에 값을 알 수 있는 스위치와 루프는 제거되고, 실제로 실행되는 단계로 확장됩니다.
- KNIME 식 언어인 Expression, String Manipulation, Math Formula, Column Expressions, Rule Engine은 PlaidCloud 식으로 변환됩니다.
- 아카이브 안에 포함된 데이터 파일은 프로젝트 기본 문서 계정의 `knime/` 폴더에 워크플로별로 폴더를 나누어 업로드되며, 변환된 리더가 그곳에서 파일을 가져옵니다.
- 뷰, 차트, 색상 관리자는 데이터에 영향을 주지 않습니다. 이들은 제외되며 변환 보고서에 나열됩니다.

## 시작하기 전에

1. KNIME Analytics Platform에서 워크플로를 `.knwf` 파일로 내보냅니다. 여러 워크플로를 한 번에 변환하려면 워크플로 그룹을 `.knar` 파일로 내보냅니다. 리더가 사용하는 파일은 워크플로의 `data` 폴더에 두어 아카이브에 함께 포함되도록 합니다.
2. 읽을 수 있는 [문서 계정](/ko/guides/documents/adding-accounts/)에 아카이브를 업로드합니다. Analyze 앱에서는 가져오기 창의 **찾아보기**로 컴퓨터에서 업로드할 수 있습니다.
3. 워크플로를 받을 PlaidCloud 프로젝트를 선택합니다. 해당 프로젝트의 아키텍트 또는 관리자여야 하며, 프로젝트에 기본 문서 계정이 있어야 합니다.
4. 워크플로의 리더와 커넥터 노드가 사용할 PlaidCloud 테이블, 파일, 연결을 확인해 둡니다. [소스 바인딩](#소스-바인딩)을 참조하십시오.

## 워크플로 변환

Analyze 앱, REST API 또는 MCP에 연결된 AI 에이전트에서 변환할 수 있습니다. REST API와 MCP 도구는 같은 필드를 사용하며, 창에서는 창에 표시되는 필드를 사용합니다.

### Analyze 앱

1. **분석**을 열고 **Tools → KNIME 워크플로 가져오기**를 선택합니다.
2. **소스 및 대상 가져오기**에서 **대상 프로젝트**와 문서 계정에 있는 **KNIME 아카이브(.knwf 또는 .knar)** 를 선택합니다. 컴퓨터에서 아카이브를 업로드하려면 **찾아보기**를 선택합니다.
3. **개체 접두사**에서 필요하면 **워크플로 접두사**, **단계 접두사**, **테이블 접두사**를 설정합니다. 테이블 접두사의 기본값은 워크플로 이름입니다.
4. **원본 바인딩(선택 사항)** 에서 필요하면 리더를 대상 프로젝트의 기존 테이블에 바인딩합니다. **추가**를 선택한 다음 **KNIME 리더**(`12:3` 같은 노드 ID, 노드 이름 또는 파일 이름)와 **테이블 ID**를 입력합니다. 연결, 문서 또는 다른 프로젝트의 테이블을 바인딩하려면 REST API 또는 MCP 도구를 사용하십시오. [소스 바인딩](#소스-바인딩)을 참조하십시오.
5. **가져오기**를 선택합니다.

창에는 아카이브를 변환하는 동안 진행 상황이 표시된 다음 변환 보고서가 표시됩니다. 보고서에는 단계 수(**단계**, **높은 신뢰도**, **보통**, **낮음**, **변환되지 않음**), 변환할 수 없었던 노드와 그 다운스트림 단계, 부분 변환, 경고, 업로드할 소스 파일, 단계가 없는 노드가 포함됩니다. 검토할 항목이 없는 변환은 그 사실을 알려 주며 창이 자동으로 닫힙니다.

### 필드

| 필드 | 필수 | 용도 |
| --- | --- | --- |
| `source_account_id` | 예 | KNIME 아카이브가 있는 문서 계정입니다. |
| `source_file_path` | 예 | 해당 계정 내 `.knwf` 또는 `.knar` 파일의 경로입니다. |
| `project_id` | 예 | 워크플로를 만들 프로젝트입니다. |
| `workflow_prefix` | 아니요 | 워크플로 이름에 붙일 접두사입니다. |
| `step_prefix` | 아니요 | 단계 이름에 붙일 접두사입니다. |
| `table_prefix` | 아니요 | 테이블 이름에 붙일 접두사입니다. 기본값은 워크플로 자체 이름입니다. 기존 테이블 이름을 재사용하게 되는 접두사는 아무것도 만들어지기 전에 거부됩니다. `.knar`의 경우 각 워크플로의 접두사 뒤에 해당 워크플로의 이름이 붙습니다. |
| `source_bindings` | 아니요 | 리더와 커넥터 노드를 이미 가지고 있는 데이터 및 연결에 바인딩하며, 최대 500개 항목까지 지정할 수 있습니다. [소스 바인딩](#소스-바인딩)을 참조하십시오. |

### REST

필드를 JSON 본문으로 다음 주소에 보냅니다.

```text
POST /rest/v1/analyze/knime/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/knime/monthly-close.knwf",
  "project_id": "<project id>"
}
```

### MCP

MCP에 연결된 AI 에이전트는 같은 필드로 `knime_convert` 도구를 호출합니다. 에이전트를 연결하려면 [AI 에이전트(MCP)](/ko/integrations/ai-coding-agents/)를 참조하십시오. 이 도구는 프로젝트를 변경하므로 승인하기 전에 호출 내용을 검토하십시오.

## 소스 바인딩

`source_bindings`를 사용하면 KNIME 리더가 아카이브에 있는 사본 대신 PlaidCloud에 이미 있는 데이터를 가리키도록 할 수 있습니다. 키는 노드 ID(예: `12:3`), 노드 이름, 포함된 파일 경로(예: `data/sales.csv`) 또는 파일 이름이며, 이 순서대로 처음 일치하는 항목이 적용됩니다. 값은 다음 중 하나입니다.

- 대상 프로젝트에 있는 테이블의 `analyzetable_` ID. 해당 테이블이 리더를 대체합니다.
- 읽을 수 있는 다른 프로젝트의 테이블에 대한 `{"project": "<project id>", "table": "<table id>"}`. 리더는 해당 테이블을 복사하는 [Import Project Table](/ko/reference/workflow-steps/import/import-project-table/) 단계가 됩니다. 원본 프로젝트는 대상 프로젝트와 읽기 권한을 공유해야 하며, 그렇지 않으면 단계가 경고합니다. 행 액세스로 관리되는 테이블은 거부됩니다.
- 읽을 수 있는 문서에 대한 `{"account": "<document account id>", "path": "/finance/budget.xlsx"}`. 리더가 해당 문서를 가져옵니다.
- 데이터베이스 또는 REST 커넥터 노드에 대한 `{"connection": "<connection id>"}`. 변환된 단계가 해당 연결에서 실행됩니다.

Analyze 앱 창에서는 테이블 ID로 리더를 대상 프로젝트의 테이블에 바인딩합니다. 연결, 문서, 다른 프로젝트의 테이블은 REST API 또는 MCP 도구로 바인딩하십시오.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "data/budget.xlsx": { "account": "<document account id>", "path": "/finance/budget.xlsx" }
}
```

바인딩한 테이블이 없거나 어떤 리더와도 일치하지 않는 키는 경고로 처리됩니다. 적용된 바인딩은 프로젝트 및 테이블 이름과 함께 변환 보고서의 `bindings`에 나열됩니다.

### 바인딩되지 않은 입력

아카이브에 파일이 없는 리더는 기본 문서 계정에 있는 워크플로 폴더의 `inputs/<file name>`에서 읽으며, 변환 보고서는 해당 경로를 `missing_inputs`에 경고와 함께 나열합니다. 그 위치에 파일을 업로드한 다음 워크플로를 실행하십시오. 파일이 업로드되기 전까지는 가져오기가 경고와 함께 끝나고 빈 테이블이 만들어지며, 워크플로는 계속 진행됩니다.

## 자격 증명과 연결

KNIME 자격 증명은 마이그레이션되지 않습니다. 다른 시스템에 로그인하는 각 단계는 사용자가 설정한 PlaidCloud 연결 또는 프로젝트 변수에서 자격 증명을 읽으며, 변환 보고서에 있는 해당 단계의 경고가 어느 쪽인지 알려 줍니다.

| KNIME | 설정할 항목 |
| --- | --- |
| 데이터베이스 커넥터 | 데이터베이스 연결입니다. `{"connection": "<id>"}`로 바인딩하거나 단계에서 선택합니다. |
| 로그인이 필요한 REST 및 웹 서비스 노드 | [REST 연결](/ko/reference/connectors/rest/generic-rest/)입니다. `{"connection": "<id>"}`로 바인딩하거나 단계에서 선택합니다. |
| Speech Recognizer(IBM Watson) | 기본 URL이 경고에 표시된 Watson 서비스 URL이고, 사용자가 `apikey`이며 API 키가 기본 로그인 비밀번호인 REST 연결입니다. 이를 노드에 바인딩합니다. |
| Email Reader 또는 Email Mover와 함께 사용하는 Email Connector | 경고에 표시된 이름으로 메일 서버 비밀번호를 담은 프로젝트 변수입니다. 호스트와 사용자는 Email Connector에서 가져옵니다. |
| 통합 문서 비밀번호가 있는 Excel Reader 또는 Excel Writer | 경고에 표시된 이름으로 비밀번호를 담은 프로젝트 변수입니다. |
| LLM 커넥터와 인증기 | AI 단계의 LLM 연결입니다. |

프로젝트 변수를 설정하려면 [워크플로 변수 관리](/ko/guides/workflows/manage-workflow-variables/)를 참조하십시오.

## 변환 보고서 읽기

가져오기가 끝나면 Analyze 앱 창에 변환 보고서가 표시되고, REST 및 MCP 응답에도 보고서가 포함됩니다. 워크플로를 실행하기 전에 보고서를 읽어 보십시오.

- `summary`는 생성된 단계 수와 그중 높은 신뢰도, 보통 신뢰도, 낮은 신뢰도로 매핑된 단계 수를 집계합니다.
- `warnings`는 각 경고를 해당 노드, 단계, 취해야 할 조치와 함께 나열하며, 설정해야 하는 모든 자격 증명 또는 연결이 포함됩니다.
- `missing_inputs`는 바인딩되지 않은 입력의 파일을 업로드할 문서 경로를 나열합니다.
- `bindings`는 적용된 바인딩을 나열합니다.
- `table_prefix`는 사용된 접두사입니다. `.knar`의 경우 `workflows`가 각 워크플로를 해당 접두사와 함께 나열합니다.
- 보고서와 함께 제공되는 `uploaded_files`는 기본 문서 계정에 업로드된 포함 파일을 나열합니다.
- `dropped_tools`는 제외된 뷰와 차트를 나열합니다.

## 자리 표시자

변환 경로가 없는 노드는 이름이 지정된 자리 표시자로 캔버스에 남습니다. 자리 표시자는 데이터를 그대로 전달하고 KNIME 노드의 이름과 함께 경고하며, 그 다운스트림의 모든 단계는 보고서에 표시되므로 누락된 결과가 조용히 넘어가지 않습니다. 결과가 중요하면 표준 단계로 해당 기능을 다시 구성하십시오.

## 변환된 워크플로 실행

1. 프로젝트에서 새 워크플로를 엽니다.
2. 경고에 나온 프로젝트 변수와 연결을 설정합니다.
3. 바인딩되지 않은 입력의 파일을 창의 **업로드할 소스 파일** 아래 또는 `missing_inputs`에 있는 경로에 업로드합니다.
4. [워크플로를 실행](/ko/guides/workflows/run-a-workflow/)하고 각 단계의 출력 테이블을 검토합니다.

## 예외 사례

KNIME과 다른 점은 다음이 전부입니다.

- **Crosstab.** [Table: Pivot](/ko/reference/workflow-steps/tables/table-pivot/) 단계로 변환됩니다. 일부 설정 조합은 KNIME과 결과가 다릅니다.
- **Loop End (Column Append).** [테이블: 내부 조인](/ko/reference/workflow-steps/tables/table-inner-join/) 단계로 변환됩니다. 일부 설정 조합은 KNIME과 결과가 다릅니다.
- **무작위 추출.** Row Sampler, Table Partitioner, Equal Size Sampling은 [Table: KNIME Random Sample](/ko/reference/workflow-steps/tables/table-knime-random-sample/) 단계로 KNIME 자체의 무작위 추출을 수행하므로, 시드가 있는 노드는 KNIME과 같은 행을 선택합니다. 추출 대상 테이블은 최대 10,000,000행이며, 이보다 큰 테이블은 단계가 실패합니다.

## 관련 가이드

- [KNIME 변환 매트릭스](/ko/reference/knime-conversion-matrix/)
- [REST 연결](/ko/reference/connectors/rest/generic-rest/)
- [문서 계정 추가](/ko/guides/documents/adding-accounts/)
- [워크플로 변수 관리](/ko/guides/workflows/manage-workflow-variables/)
- [워크플로 실행](/ko/guides/workflows/run-a-workflow/)
