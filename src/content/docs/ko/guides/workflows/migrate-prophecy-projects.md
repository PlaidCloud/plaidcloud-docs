---
title: Prophecy 프로젝트 마이그레이션
description: Analyze 앱, REST API 또는 MCP에 연결된 AI 에이전트에서 Prophecy 프로젝트 내보내기 파일을 PlaidCloud 워크플로로 변환하고, 데이터 세트와 연결을 바인딩한 다음 변환 보고서를 확인합니다.
sidebar:
  order: 31.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-prophecy-projects.md
---

PlaidCloud는 Prophecy를 그대로 대체할 수 있습니다. 모든 Prophecy 젬은 해당 젬이 하는 일을 수행하는 PlaidCloud 네이티브 워크플로 단계로 변환됩니다. 변환기는 Spark 파이프라인마다 워크플로를 하나씩, SQL 프로젝트용으로 워크플로를 하나 만들고, 각 젬을 워크플로 단계, 프로젝트 변수 또는 캔버스 개체에 매핑하며, 원래 그래프를 유지한 채 변환 보고서를 반환합니다. 변환된 워크플로가 자체적으로 재현하지 못하는 일부 동작은 [예외 사항](#예외-사항)에 나와 있습니다.

변환은 지정한 내보내기 파일만 읽습니다. Prophecy 데이터 세트가 읽거나 쓰는 시스템에는 접속하지 않으며, 프로젝트 코드도 실행하지 않습니다.

변환은 일회성 작업입니다. 같은 프로젝트를 다시 변환하면 새 워크플로와 테이블이 만들어지며, PlaidCloud에서 직접 수정한 내용이 이후 내보내기 파일과 병합되지는 않습니다.

## PlaidCloud가 만드는 항목

- 각 Prophecy 젬은 상위 및 하위 관계가 유지된 상태로 대응하는 워크플로 단계가 됩니다.
- Prophecy 매개변수는 프로젝트 변수가 되며, 젬 설정 안에서 이를 참조하는 부분은 PlaidCloud 변수 구문으로 다시 작성됩니다. 변환할 때 매개변수 값을 재정의할 수 있습니다.
- 젬이 읽는 각 데이터 세트는 바인딩 방식에 따라 가져오기 단계가 되거나 기존 테이블 또는 문서를 읽습니다.
- 각 Prophecy 작업 또는 SQL 파이프라인 일정은 변환된 워크플로의 [예약된 이벤트](/ko/administration/scheduled-events/)가 되며, Prophecy에서 사용 설정되어 있으면 사용 설정됩니다. [일정](#서비스-및-제어)을 참조하십시오.
- 스크립트, SQL 문, 매크로 및 기타 프로젝트 코드는 해당 코드를 담은 단계 안에 들어갑니다. [단계 안의 프로젝트 코드](#단계-안의-프로젝트-코드)를 참조하십시오.
- Gem Builder 젬을 포함한 사용자 지정 젬은 내보내기 파일에 포함된 코드를 Python 단계에서 실행합니다. [단계 안의 프로젝트 코드](#단계-안의-프로젝트-코드)를 참조하십시오.
- HAVING 조건이나 모든 값 열이 있는 Pivot 젬이 변환되며, Prophecy가 제공하는 정렬 및 Deduplicate 유형도 변환됩니다.
- 식은 null 처리, 정수 나눗셈, 암시적 형 변환에 대해 Spark SQL 동작을 가정하여 변환됩니다. PlaidCloud 엔진에서 이러한 동작이 다른 경우 결과를 확인하십시오.

## 시작하기 전에

1. Prophecy에서 프로젝트를 `.zip` 파일로 내보내거나, 단일 파이프라인, 모델 또는 서브그래프를 `.json` 파일로 내보냅니다.
2. 읽을 수 있는 [문서 계정](/ko/guides/documents/adding-accounts/)에 파일을 업로드합니다.
3. 워크플로를 받을 PlaidCloud 프로젝트를 선택합니다. 해당 프로젝트에 대한 쓰기 권한이 있어야 합니다.
4. 바인딩되지 않은 데이터 세트의 파일을 읽을 위치를 정합니다. 문서 계정과 기본 폴더를 선택합니다.

## 프로젝트 변환

Analyze 앱, REST API 또는 MCP 도구 카탈로그에서 변환할 수 있습니다. 세 가지 방법 모두 같은 필드를 사용합니다.

### Analyze 앱

1. **Analyze**를 열고 **도구 → Prophecy 프로젝트 가져오기**를 선택합니다.
2. **대상 프로젝트**, 문서 계정에 업로드한 **Prophecy 프로젝트(.zip 또는 .json)**, 그리고 바인딩되지 않은 데이터 세트의 파일을 읽을 문서 계정과 기본 폴더인 **소스 파일 위치**를 선택합니다.
3. **개체 이름 및 옵션**에서 필요에 따라 워크플로, 단계, 테이블 접두사를 설정하고, **워크플로 유형**을 선택하고, 변환되지 않은 구성 요소를 통과 자리 표시자로 가져올지 선택합니다.
4. **소스 바인딩 및 매개변수**에서 필요에 따라 데이터 세트 이름과 테이블 ID를 입력하여 데이터 세트를 기존 테이블에 바인딩하고, 이름으로 Prophecy 매개변수를 재정의합니다. 연결을 바인딩하려면 REST API 또는 MCP 도구를 사용하십시오. [연결 바인딩](#연결-바인딩)을 참조하십시오.
5. **가져오기**를 선택합니다.

창에는 프로젝트를 읽고, 파이프라인을 구문 분석하고, PlaidCloud 작업에 매핑하고, 워크플로, 테이블, 단계를 만드는 진행 상황이 표시됩니다. 완료되면 창에 변환 보고서가 표시됩니다. 보고서에는 신뢰도별 단계 수, 경고, 부분 변환, 변환되지 않은 자리 표시자, 제외된 구성 요소, 업로드할 소스 파일이 들어 있습니다.

### 필드

REST API와 MCP 도구는 다음 필드를 사용합니다.

| 필드 | 필수 | 용도 |
| --- | --- | --- |
| `source_account_id` | 예 | Prophecy 내보내기 파일이 있는 문서 계정입니다. |
| `source_file_path` | 예 | 해당 계정 내 프로젝트 `.zip` 또는 단일 파이프라인, 모델, 서브그래프 `.json` 파일의 경로입니다. |
| `project_id` | 예 | 워크플로를 만들 프로젝트입니다. |
| `document_account_id` | 예 | 바인딩되지 않은 데이터 세트를 읽을 문서 계정입니다. |
| `document_account_path` | 예 | 해당 계정에서 바인딩되지 않은 데이터 세트를 읽을 기본 폴더입니다. 비어 있거나 `/`이면 계정 루트이며, 앞의 `/`는 무시됩니다. `..` 또는 점으로 시작하는 세그먼트, 중괄호, 드라이브 문자나 URL 스키마, 제어 문자가 있는 경로는 거부됩니다. |
| `workflow_prefix` | 아니요 | 워크플로 이름에 추가할 접두사입니다. |
| `step_prefix` | 아니요 | 단계 이름에 추가할 접두사입니다. |
| `table_prefix` | 아니요 | 테이블 이름에 추가할 접두사입니다. 기본값은 워크플로 자체 이름입니다. 기존 테이블 이름을 재사용하게 되는 접두사는 아무것도 만들기 전에 거부됩니다. 사용된 접두사는 변환 보고서에 반환됩니다. |
| `workflow_type` | 아니요 | `advanced`(기본값)는 그래프를 DAG 캔버스에 배치합니다. `standard`는 순차적인 단계 목록을 만듭니다. |
| `source_bindings` | 아니요 | 데이터 세트와 작업을 기존 데이터에 바인딩합니다. [소스 바인딩](#소스-바인딩)을 참조하십시오. |
| `connection_bindings` | 아니요 | 프로젝트가 접근하는 데이터베이스, 파일 저장소, REST API, 이메일을 PlaidCloud 연결 및 문서 계정에 바인딩합니다. [연결 바인딩](#연결-바인딩)을 참조하십시오. |
| `parameters` | 아니요 | Prophecy 매개변수를 재정의합니다. [매개변수](#매개변수)를 참조하십시오. |
| `allow_unconverted_placeholders` | 아니요 | 자리 표시자가 실행 시점에 하는 동작을 제어합니다. [변환되지 않은 젬의 자리 표시자](#변환되지-않은-젬의-자리-표시자)를 참조하십시오. |

### REST

필드를 JSON 본문으로 다음 주소에 전송합니다.

```text
POST /rest/v1/analyze/prophecy/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/prophecy/customer-360.zip",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/prophecy-inputs"
}
```

`analyze.workflow.write` 역할이 필요합니다.

### MCP

MCP에 연결된 AI 에이전트는 같은 필드로 `prophecy_convert` 도구를 호출합니다. 에이전트를 연결하려면 [AI 에이전트(MCP)](/ko/integrations/ai-coding-agents/)를 참조하십시오. 이 도구는 프로젝트를 변경하므로 승인하기 전에 호출 내용을 검토하십시오.

## 소스 바인딩

Prophecy 내보내기 파일에는 데이터의 출처가 기술되어 있지만 데이터와 자격 증명은 들어 있지 않습니다. `source_bindings`를 사용하여 각 데이터 세트를 PlaidCloud에 이미 있는 데이터에 연결합니다. 키는 변환 보고서에 나열된 데이터 세트 이름입니다. 값은 다음 중 하나입니다.

- 대상 프로젝트에 있는 테이블의 `analyzetable_` ID입니다. 변환된 워크플로가 해당 테이블을 직접 읽습니다.
- 문서 계정의 파일을 읽기 위한 `account`, `path`, 선택 사항인 `sheet`가 포함된 개체입니다.

```json
"source_bindings": {
  "customers": "analyzetable_1234",
  "budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

읽을 수 없는 바인딩은 거부됩니다. 어떤 데이터 세트와도 일치하지 않는 키는 경고로 보고됩니다. Analyze 창에서는 데이터 세트를 테이블에 바인딩할 수 있으며, 데이터 세트를 문서 파일에 바인딩하려면 REST API 또는 MCP 도구를 사용하십시오.

### 바인딩되지 않은 데이터 세트

바인딩이 없는 데이터 세트는 아직 데이터가 없는 가져오기 단계가 되며, 변환 보고서에 이에 대한 경고가 표시됩니다. 이 단계는 다음 위치에서 읽습니다.

```text
<document_account_path>/prophecy/<workflow id>/<dataset name>.csv
```

해당 경로에 파일을 업로드한 다음 워크플로를 실행하십시오. 파일이 없는 동안에는 가져오기 단계가 경고와 함께 완료되고 빈 테이블을 만들며, 워크플로는 계속 진행됩니다. 보고서의 **업로드할 소스 파일**에 각 경로가 나열됩니다.

### 테이블 및 파일 작업 바인딩

Table Operations(업데이트, 삭제, 삭제 처리)나 File Operation(복사)처럼 테이블 또는 파일을 변경하는 젬은 변환 과정에서 만든 데이터에만 작용합니다. 이미 존재하는 데이터에 대해 작업하게 하려면 `operation:<pipeline>/<id>` 형식의 키로 바인딩하십시오. `<pipeline>`은 파이프라인 이름이고 `<id>`는 젬의 ID입니다. 변환 보고서에 해당하는 각 젬의 키가 표시됩니다.

```json
"source_bindings": {
  "operation:daily_load/Operation_1": "analyzetable_5678"
}
```

데이터를 파괴하는 테이블 또는 파일 작업은 바인딩한 경우에만 실행됩니다. 바인딩이 없으면 Table Operations 젬은 같은 프로젝트의 다른 젬이 쓴 테이블에 대해 작업하고, 그렇지 않으면 해당 키를 알려 주는 자리 표시자가 됩니다. File Operation은 자체 스테이징 폴더에서 복사합니다. 바인딩하지 않으면 변환 자체의 테이블과 폴더 밖에 있는 어떤 것도 변경되지 않습니다.

## 연결 바인딩

Prophecy 프로젝트는 연결을 통해 데이터베이스, 파일 저장소, REST API, 메일 서버에 접근합니다. 내보내기 파일에는 연결 이름만 있고 자격 증명은 없으므로, `connection_bindings`를 사용하여 각 연결을 이미 가지고 있는 PlaidCloud 연결 또는 문서 계정에 지정하십시오. 변환 보고서의 바인딩 항목 아래에 모든 키가 나열됩니다.

```json
"connection_bindings": {
  "connection:warehouse_pg": "<connection id>",
  "connection:landing_s3": "<document account id>",
  "operation:daily_load/Email_1": "<connection id>"
}
```

키는 다음 중 하나입니다.

| 키 | 바인딩 대상 | 값 |
| --- | --- | --- |
| `connection:<name>` | 젬 또는 데이터베이스 데이터 세트가 지정하는 Prophecy 연결입니다. 바인딩 하나로 해당 연결을 사용하는 모든 젬을 처리합니다. 연결을 지정하지 않은 젬은 `connection:<pipeline>/<gem id>`를 사용하고, 데이터베이스 데이터 세트는 `connection:<dataset name>`을 사용합니다. | PlaidCloud 연결 ID입니다. 데이터베이스 연결(BigQuery와 SAP HANA 포함), MongoDB 또는 Apache Kafka 연결, Salesforce 읽기 및 쓰기용 Salesforce 연결, Tableau 젬용 Tableau 연결, Azure Cosmos DB, Pinecone, Power BI 및 Smartsheet와 Slack 쓰기용 REST 연결, Smartsheet, Slack, Iceberg 읽기용 Singer 기반 연결이 해당합니다. File Storage 또는 Directory 젬에는 문서 계정 ID를 사용합니다. |
| `operation:<pipeline>/<gem id>` | GET, HEAD, OPTIONS 이외의 요청을 보내는 REST 젬과 모든 Email 젬입니다. | 연결 ID입니다. REST의 경우 자격 증명을 보유한 REST 연결입니다. |

바인딩은 변환 범위 밖의 대상을 변경하는 젬에 대한 사용자의 동의로 간주됩니다.

- API에 저장된 내용을 변경할 수 있는 REST 요청과 실제 사람에게 전달되는 이메일은 해당 `operation:` 키를 바인딩한 경우에만 동작하는 단계로 변환됩니다. 바인딩하지 않으면 해당 젬은 키를 알려 주는 자리 표시자가 됩니다.
- File Storage 또는 Directory 젬에 바인딩된 문서 계정은 해당 젬의 단계가 그 계정의 파일을 쓰거나 삭제하거나 이동할 수 있게 합니다.
- GET, HEAD, OPTIONS 요청은 젬이 보내는 그대로 전송됩니다. 바인딩하지 않으면 변환된 단계에서 REST 연결을 선택할 때까지 자격 증명이 없습니다.

바인딩이 없는 데이터베이스 데이터 세트 또는 External Table 젬은 자신의 키를 알려 주고 연결을 선택하기를 기다리는 단계로 변환되며, 보고서에 경고가 표시됩니다. 키를 바인딩하여 다시 변환하거나 단계에서 연결을 선택하십시오. 젬에 맞지 않는 종류의 저장소 ID이거나 사용할 수 없는 ID로 바인딩하면 거부됩니다. 어떤 것과도 일치하지 않는 키는 경고로 보고됩니다.

## 매개변수

`parameters`는 변환 시 Prophecy 매개변수를 재정의합니다.

```json
"parameters": {
  "instance": "prod",
  "values": { "run_date": "2026-10-01", "region": "EMEA" },
  "pipelines": {
    "daily_load": { "instance": "prod", "values": { "region": "APAC" } }
  }
}
```

`instance`는 구성 인스턴스의 이름입니다. `values`는 텍스트, 숫자 또는 불리언입니다. 파이프라인 항목은 해당 파이프라인에 한해 프로젝트 전체 값을 재정의합니다. 보고서에는 사용된 매개변수와 PlaidCloud 변수 이름에 맞게 이름이 바뀐 매개변수가 나열됩니다.

## 변환 보고서 읽기

응답에 변환 보고서가 포함됩니다. 워크플로를 실행하기 전에 읽어 보십시오.

| 섹션 | 알려 주는 내용 |
| --- | --- |
| 요약 | 신뢰도가 높음, 보통, 낮음으로 변환된 단계 수와 변환되지 않은 단계 수입니다. |
| 경고 | 바인딩되지 않은 데이터 세트와 어떤 것과도 일치하지 않은 바인딩 키를 포함하여, 변환기가 가정하거나 근사하거나 건너뛴 모든 내용입니다. |
| 부분 변환 | 변환은 되지만 특정 모드나 옵션에서 젬과 다른 단계입니다. 각 항목에 확인할 사항이 메모로 포함됩니다. |
| 변환되지 않은 자리 표시자 | PlaidCloud에 대응하는 항목이 없는 젬과 그 이유입니다. |
| 제외된 구성 요소 | 제어 흐름 경계 표시처럼 자체 작업이 없는 젬과, 각각을 흡수한 단계입니다. |
| 업로드할 소스 파일 | 바인딩되지 않은 각 데이터 세트가 읽는 문서 경로입니다. |
| 워크플로 | 파이프라인마다 만들어진 워크플로를 실행 순서대로 나열한 것입니다. 변환기가 거부한 파이프라인은 표시됩니다. |

보고서에는 사용된 테이블 접두사와 적용된 매개변수도 표시됩니다. 변환기가 확신하지 못하는 단계는 가장 가능성이 높은 해석으로 변환되고 보고서에 메모가 남습니다. 이러한 단계는 Prophecy 출력과 대조하여 확인하십시오.

## 단계 안의 프로젝트 코드

Prophecy 프로젝트에는 Script 젬, SQL 문, 매크로, 동적 입력, 저장 프로시저 호출, 사용자 지정 젬 같은 코드가 포함됩니다. 변환기는 이 코드를 실행하지 않고 단계 안에 넣습니다.

- SQL은 테넌트의 SQL 방언으로 변환되어 SQL 단계에 들어가며, 젬의 입력은 쿼리가 읽는 이름으로 사용할 수 있습니다.
- Python 스크립트는 테이블 접근 방식이 다시 작성되어 Python 단계에 들어갑니다. Spark 데이터 프레임 메서드를 호출하는 스크립트는 그 호출을 그대로 유지하고 단계에서 실행합니다.
- Gem Builder 젬을 포함한 사용자 지정 젬은 파이프라인 내보내기 파일에 포함된 PySpark 코드를 Python 단계에서 실행합니다.
- 알려진 dbt 패키지의 매크로는 그 매크로가 하는 일을 수행하는 표준 단계가 됩니다. 자체 프로젝트의 매크로나 내보내기 파일에 포함된 패키지의 매크로도 읽어서 변환하며, if와 for 블록, set, 필터, 중첩 매크로, 어댑터 디스패치도 포함됩니다.
- Aggregate 젬의 Python 사용자 정의 집계 함수는 그룹마다 Python 단계에서 실행됩니다.

프로젝트 코드를 담은 모든 단계에는 경고가 표시되며, 변환된 SQL에도 마찬가지입니다. 워크플로를 실행하기 전에 해당 단계의 코드를 검토하십시오. 변환기는 코드 문자열과 주석에서 발견한 자격 증명으로 보이는 모든 내용을 제외하므로, 자격 증명은 코드가 아니라 연결에 추가하십시오.

## 변환되지 않은 젬의 자리 표시자

변환기가 재현할 수 없는 젬은 젬의 이름이 있는 자리 표시자 단계로 만들어집니다. 내보내기 파일에 코드가 없는 사용자 지정 젬이나, `operation:` 키를 바인딩하지 않은 상태에서 데이터를 변경할 수 있는 REST 요청, Email, 테이블 또는 파일 작업처럼 변환 범위 밖의 데이터를 변경하는 젬이 그 예입니다. 연결이 바인딩되지 않은 데이터베이스 데이터 세트 또는 External Table은 자리 표시자가 아니라 연결을 선택하기를 기다리는 단계로 변환됩니다. 기본적으로 자리 표시자는 워크플로가 도달하면 실패하므로, 실제로 수행되지 않은 작업에 대해 실행이 성공으로 보고되는 일이 없습니다.

`allow_unconverted_placeholders`를 `true`로 설정하면(창에서는 **변환되지 않은 구성 요소를 통과 자리 표시자로 가져오기**) 각 자리 표시자가 통과 단계로 가져와집니다. 그러면 실행이 해당 단계를 지나 계속되며, 자리 표시자의 출력은 입력과 같습니다. 보고서에는 통과 자리 표시자의 수와 해당 단계가 나열됩니다. 그 결과가 중요하다면 네이티브 단계로 기능을 다시 구성하십시오.

## 변환된 워크플로 실행

1. 프로젝트에서 새 워크플로를 엽니다. 보고서에 실행 순서대로 나열되어 있습니다.
2. Prophecy 매개변수에서 비롯된 프로젝트 변수를 설정합니다.
3. 바인딩되지 않은 데이터 세트의 파일을 보고서에 표시된 경로에 업로드합니다.
4. 프로젝트 코드를 담은 단계를 검토합니다.
5. 워크플로를 실행하고 각 단계의 출력 테이블을 검토합니다.

Prophecy 일정에서 만들어진 예약된 이벤트는 Prophecy에서 사용 설정되어 있었다면 사용 설정되므로, 일정에 따라 변환된 워크플로를 실행하기 시작합니다. 먼저 워크플로를 검토하려면 [예약된 이벤트](/ko/administration/scheduled-events/)에서 이벤트를 사용 중지했다가 준비되면 사용 설정하십시오.

## 변환되는 항목

모든 Prophecy 젬은 제공하는 옵션과 함께 네이티브 단계, 프로젝트 변수, 예약된 이벤트 또는 캔버스 개체로 완전히 변환됩니다. [Prophecy 변환 매트릭스](/ko/reference/prophecy-conversion-matrix/)에는 모든 젬과 그것이 되는 PlaidCloud 단계가 나열되어 있고, [예외 사항](#예외-사항)에는 확인해야 할 일부 동작이 나열되어 있습니다. 변환 보고서는 해당 동작이 발생하는 위치마다 이를 알려 줍니다.

### 데이터 이동

| 기능 | 변환 방식 |
| --- | --- |
| 쓰기 모드 | 대상 쓰기 모드는 플랫폼 단계로 변환됩니다. 확인 및 타임스탬프 전략의 SCD2(타임스탬프 전략은 젬의 `scd2.updatedAtColumn`이 지정하는 열로 각 버전의 날짜를 지정합니다), merge, `replaceWhere`, `insertInto`가 해당합니다. merge는 일치 시 업데이트 및 불일치 시 삽입 절의 열별 SET 식을 적용하며, 열을 설정하지 않는 절은 들어오는 행의 모든 열을 가져옵니다. 빈 대상에 대한 첫 실행은 dbt와 Delta처럼 모든 행을 씁니다. 첫 실행에는 미리 만들어 둔 테이블이 필요하지 않으며, 자신이 쓰는 데이터 세트를 읽는 파이프라인도 마찬가지입니다. 단, 내보내기 파일에 해당 데이터 세트의 열이 명시되어 있지 않다면 첫 실행 전에 테이블을 만드십시오. 이후 실행에서는 증분 필터 또는 merge 조건이 적용됩니다. `error` 및 `ignore` 모드는 [테이블 존재 조건](/ko/guides/workflows/step-conditions/#테이블-존재-조건)으로 확인합니다. |
| 타임 트래블 | `versionAsOf` 또는 `timestampAsOf`로 테이블의 이전 버전을 읽는 Delta 또는 카탈로그 테이블 소스는 바인딩한 연결을 통해 Databricks에서 해당 버전을 읽습니다. |
| 스트리밍 | 스트리밍 소스와 대상은 예약된 배치로 실행됩니다. 스트리밍 싱크는 행을 추가하는 대신 테이블을 교체하므로 다시 실행해도 행이 중복되지 않습니다. 새로 도착한 데이터를 가져오려면 워크플로를 예약하십시오. |
| 데이터베이스 | JDBC, Snowflake, Redshift, Hive, BigQuery, SAP HANA, External Table 젬은 바인딩한 PlaidCloud 연결을 통해 읽고 씁니다. BigQuery 데이터 세트는 [SQL 가져오기](/ko/reference/workflow-steps/import/import-sql/)로 읽고, [BigQuery 연결](/ko/reference/connectors/google/big-query/)에서 [Export External Database Tables](/ko/reference/workflow-steps/export/export-external-tables/) 단계로 씁니다. HANA 젬의 모든 merge 모드(SCD2와 삭제 모드 포함)로 쓰는 SAP HANA 테이블은 대상 옆에 스테이징된 뒤 대상의 기본 키 또는 젬의 merge 열을 기준으로 병합됩니다. 대상이 없으면 먼저 만들어집니다. |
| MongoDB 및 Kafka | MongoDB 데이터 세트는 필터나 집계 파이프라인을 포함하여 [MongoDB 가져오기](/ko/reference/workflow-steps/import/import-mongodb/)로 읽으며, 열을 선언하지 않은 읽기는 Spark 커넥터처럼 처음 몇 개의 문서에서 열을 가져옵니다. 쓰기는 해당하는 쓰기 모드에서 [MongoDB 내보내기](/ko/reference/workflow-steps/export/export-mongodb/)를 사용합니다. `update`는 일치하는 문서의 필드를 업데이트하거나 문서를 삽입하고, `ignore`는 컬렉션에 문서가 없을 때만 쓰며, `error`는 컬렉션에 문서가 있으면 실행을 중지합니다. Kafka 소스는 시작 오프셋과 종료 오프셋 사이의 토픽을 [Kafka 가져오기](/ko/reference/workflow-steps/import/import-kafka/)로 읽고, Kafka 대상은 [Kafka 내보내기](/ko/reference/workflow-steps/export/export-kafka/)로 각 행을 보냅니다. `OAUTHBEARER`로 로그인하는 Kafka 데이터 세트는 내보내기 파일에 자격 증명이 없으므로, 바인딩한 Kafka 연결의 [OAuth 로그인](/ko/reference/connectors/databases/apache-kafka/#oauthoauthbearer)을 사용합니다. |
| Azure Cosmos DB | 읽기는 데이터 세트의 쿼리를 보내거나 모든 문서를 읽으며, Cosmos DB 인증이 설정된 REST 연결에서 [REST 요청](/ko/reference/workflow-steps/general/rest-request/) 단계를 사용하고 페이지마다 연속 헤더를 따라갑니다. 쓰기는 젬의 쓰기 전략(덮어쓰기, 추가, 삭제, 패치)에 따라 행마다 요청을 하나씩 보냅니다. 문서의 ETag가 있는 행은 그 이후 문서가 변경되지 않은 경우에만 교체되거나 삭제되며, 이 때문에 또는 문서가 없거나 이미 있다는 이유로 컨테이너가 거부한 행은 Spark 커넥터처럼 건너뜁니다. `ignore` 모드는 컨테이너에 문서가 없을 때만 씁니다. |
| Salesforce | 읽기는 [Salesforce: 개체 쿼리](/ko/reference/workflow-steps/salesforce/query-salesforce-object/)를 사용하며, 젬이 요청하면 삭제되거나 보관된 레코드도 포함합니다. 쓰기는 행마다 요청 하나로 삽입, 업데이트, 업서트 또는 삭제를 수행합니다. 업서트는 젬의 외부 ID 필드를 기준으로 일치시키며, 지정하지 않으면 `Id`를 사용합니다. |
| Smartsheet, Slack, Pinecone | 열이 선언된 이름 있는 시트의 Smartsheet 읽기는 REST 연결을 통해 시트를 가져와 시트 행마다 행 하나, 선언된 열마다 열 하나로 저장합니다. 그 밖의 Smartsheet 읽기와 Slack 및 Iceberg 읽기는 [Import Singer Source](/ko/reference/workflow-steps/import/import-singer/) 단계를 사용합니다. Smartsheet 쓰기는 이름 있는 시트에 행을 추가하고, 덮어쓰기는 먼저 시트의 행을 삭제합니다. Slack 쓰기는 행마다 메시지 하나를 게시하며, Slack이 거부한 메시지는 단계를 실패시킵니다. Pinecone 인덱스는 벡터와 해당 메타데이터로 읽고, 쓰기는 행을 벡터로 업서트합니다. |
| Tableau 및 Power BI | Tableau와 Tableau Write는 바인딩한 Tableau 연결에서 [Publish to Tableau](/ko/reference/workflow-steps/export/export-to-tableau/) 단계를 통해 입력을 Hyper 추출로 게시합니다. Power BI Write는 OAuth 2.0이 설정된 REST 연결을 통해 입력을 Power BI 푸시 데이터 세트로 푸시하며, 이름으로 워크스페이스를 찾고 데이터 세트가 새것이면 만듭니다. |
| 파일 형식 | CSV, JSON, Parquet, Avro, Excel, XML, 고정 너비, ORC([ORC 가져오기](/ko/reference/workflow-steps/import/import-orc/) 사용)를 지원합니다. 형식 옵션은 매핑되거나, 어떤 행도 변경하지 않는 경우 중립으로 표시됩니다. Avro 읽기의 수정 시간 범위, 고정 너비 파일의 EBCDIC 인코딩, 헤더 및 푸터 레코드와 줄바꿈이 없는 레코드, Excel 읽기의 시트 맵과 암호, CSV 쓰기의 따옴표 옵션, 값마다 시트 하나씩 만드는 Excel 쓰기가 여기에 해당합니다. 압축된 텍스트 파일은 gzip, Deflate(zlib), Zstandard, LZ4, Snappy, LZO로 읽고 쓰며, 이름이 코덱의 확장명으로 끝나는 압축 파일을 읽습니다. 암호화된 파일은 제자리에서 암호 해독 및 암호화됩니다. [암호화된 파일](#암호화된-파일)을 참조하십시오. |
| File Operation | Copy와 Move는 바인딩한 폴더에서 [문서: 파일 복사](/ko/reference/workflow-steps/document/copy-document-file/) 또는 Copy Directory로 변환되며, 이름이 젬의 `filenameRegex`와 일치하는 파일만 유지하고, 젬이 재귀 처리하는 경우 각 파일의 경로를 소스 폴더 아래에서 유지합니다. |
| Directory | 바인딩된 문서 폴더의 파일을 젬의 열 구성으로 [디렉터리 목록](/ko/reference/workflow-steps/document/directory-listing/) 단계에서 나열합니다. 시트 이름 옵션을 켜면 Excel 통합 문서마다 시트별로 행 하나와 해당 `sheet_name`이 만들어지고, 다른 파일은 `sheet_name`이 비어 있는 행 하나를 만듭니다. |

### 열 및 행

| 젬 또는 함수 | 변환 방식 |
| --- | --- |
| Surrogate Key | 젬의 키 파일처럼 마지막으로 발급한 키를 보관하는 테이블에서 이어서 키를 발급합니다. 같은 키 파일을 지정한 모든 젬이 해당 테이블을 공유하므로 키가 겹치지 않습니다. 행이 없는 실행은 테이블을 그대로 두며, 발급된 키가 없으면 키는 초기값에서 시작합니다. |
| Column Parser, XML Parse, JSON parsing | XML 및 JSON 텍스트는 [XML 구문 분석](/ko/reference/workflow-steps/tables/table-xml-parse/) 단계와 [JSON 구문 분석](/ko/reference/workflow-steps/tables/table-json-parse/) 단계로 구문 분석하며, 요소의 텍스트, 특성 또는 자식 요소에서 각 필드를 읽습니다. 스키마 없이 구문 분석한 XML은 Spark의 `schema_of_xml`처럼 데이터에서 각 필드의 형식을 가져옵니다. |
| Business rules | 식에서 호출하는 프로젝트 비즈니스 규칙은 같은 조건으로 변환되며, 설정하는 열마다 `CASE` 하나가 만들어집니다. |
| Casts | 텍스트를 decimal 또는 long으로 변환하는 형 변환은 Spark와 정확히 같게 동작합니다. 숫자 앞뒤의 공백과 제어 문자는 제거되고, decimal은 자릿수에서 반올림(0.5 올림)되며, 숫자가 아닌 텍스트나 범위를 벗어난 값은 null이 됩니다. |
| Dates and times | 날짜 및 시간 형식은 Databend를 포함한 워크스페이스의 엔진에 맞게 작성되며, `window()`는 Spark가 정렬하는 방식 그대로 각 타임스탬프를 해당 텀블링 윈도에 배치합니다. |
| Iterator outputs | 출력 열이 실행 시점에만 알려지는 Table Iterator 또는 While Iterator는 Prophecy가 각 패스를 쌓는 방식과 같이, 모든 패스가 들어맞는 형식으로 각 열을 넓혀서 [테이블: 전체 유니온](/ko/reference/workflow-steps/tables/table-union-all/#열-일치)으로 각 패스의 행을 위치 기준으로 모읍니다. |
| Data Encoder/Decoder AES | 모든 엔진에서 실행됩니다. 키와, 젬이 지정하는 경우 초기화 벡터 및 추가 데이터는 사용자가 설정하는 워크플로 변수 `aes_key`, `aes_iv`, `aes_aad`에서 가져옵니다. |
| Data Masking hash | Spark의 `hash()`와 같은 값을 계산합니다. |
| Buffer, Simplify, Heat Map | Buffer는 Prophecy와 같은 수의 세그먼트로 둥근 모서리를 그리고, Simplify는 같은 꼭짓점을 제거하며, Heat Map은 젬의 해상도로 H3 육각형에 열을 합산하고 decimal 열은 decimal로 유지됩니다. |

### 서비스 및 제어

| 젬 | 변환 방식 |
| --- | --- |
| Pipeline | 이름이 지정된 파이프라인을 [Workflow Loop](/ko/reference/workflow-steps/workflow-control/workflow-loop/) 단계로 입력 행마다 한 번씩 실행합니다(입력이 없으면 한 번, 행이 없으면 실행하지 않음). 각 매개변수는 상수, 행의 열 또는 그에 대한 식으로 설정합니다. 앞선 실행이 실패해도 모든 실행이 계속 진행되며, 젬의 출력에는 Prophecy가 기록하는 것처럼 실행마다 상태, 메시지, 시간이 담긴 행이 하나씩 있습니다. |
| Schedules | Prophecy 작업 또는 SQL 파이프라인 일정은 변환된 워크플로에서 `Prophecy <name>`이라는 이름의 [예약된 이벤트](/ko/administration/scheduled-events/)가 되며, Prophecy에서 사용 중지되지 않았다면 사용 설정됩니다. 구성 재정의나 실행 조건 없이 변환된 파이프라인 하나를 실행하는 Spark 작업은 이런 방식으로 변환됩니다. |
| Script | Python 스크립트는 Python 단계에 들어갑니다. 스크립트가 `Config`에 설정한 값은 이후 단계가 읽는 워크플로 변수가 되며, Prophecy의 `Config`처럼 매 실행이 시작될 때 파이프라인의 값으로 재설정됩니다. |
| REST API, REST API Enrich | 입력 행마다 요청 하나를 보내는 [REST 요청](/ko/reference/workflow-steps/general/rest-request/) 단계이며, Prophecy처럼 오류 응답을 유지합니다. Enrich는 상태, 사유, 최종 URL도 읽습니다. 비동기 결과를 기다리는 요청은 응답이 완료되었다고 알릴 때까지 폴링합니다. |
| Stored Procedure | 인수를 전달하는 젬은 입력 행마다 한 번씩 [원격 실행: SQL](/ko/reference/workflow-steps/agent/agent-remote-execution-of-sql/#행마다-문-한-번-실행)로 프로시저를 호출하며, 각 인수는 해당 열에서 매개변수로 바인딩됩니다. 인수가 없는 젬은 에이전트를 통해 한 번 호출합니다. 변환된 단계에서 연결 또는 에이전트를 선택하십시오. |
| Email, Email Data | Cc, Bcc, Reply-To를 지원하고, 필드를 열에서 읽는 경우 행마다 메시지 하나를 보내는 [Notify Via Email](/ko/reference/workflow-steps/notifications/notify-via-email/) 단계입니다. |
| OpenAI, Bedrock, SageMaker Endpoint | 워크스페이스의 LLM 연결에서 [Text: NLP (AI)](/ko/reference/workflow-steps/text-documents/nlp-ai/) 단계로 변환됩니다. OpenAI 및 Bedrock 임베딩은 Embed 작업을 사용하며, 이를 위해 OpenAI 호환 또는 Azure OpenAI 연결이 필요합니다. Anthropic 연결은 거부됩니다. |
| Pinecone Lookup | 행마다 REST 요청을 보냅니다. |
| Data Quality Check, Deequ, Soda | 검사는 웨어하우스에서 실행되고 결과 테이블을 씁니다. Data Quality Check는 젬이 `minFailedChecks` 또는 `fail_pipeline` 사후 작업을 설정한 경우에만 실행을 중지하며, 그렇지 않으면 결과 테이블에 실패 항목이 나열됩니다. Deequ와 Soda는 실행을 중지하지 않습니다. 숫자 열에 대한 최소 또는 최대 길이 검사는 숫자를 텍스트로 보고 측정합니다. Soda 검사는 프로젝트의 YAML에서 변환되며, 누락, 잘못된 값, 유효한 값, 통계, 길이, 백분위수, 열 간 중복, 최신성, 실패한 행, 사용자 고유의 지표 쿼리를 포함합니다. |
| ToDo | 실행이 도달하면 원래 도구와 메시지를 알려 주는 오류를 발생시킵니다. |

### 암호화된 파일

암호화된 파일을 읽는 File Storage 젬은 [문서: 파일 암호 해독](/ko/reference/workflow-steps/document/encrypt-decrypt-file/) 단계로 변환되며, 가져오기가 읽기 전에 파일을 전용 폴더에 암호 해독하고 이후에 암호 해독된 사본을 제거합니다. 암호화된 파일을 쓰는 젬은 해당 폴더로 내보낸 다음 문서: 파일 암호화 단계로 파일을 암호화하여 제자리에 둡니다. AES 및 Blowfish 파일과 암호로 보호된 Excel 통합 문서가 지원됩니다.

내보내기 파일에는 키가 포함되지 않으므로 변환된 단계는 워크플로 변수에서 키를 읽습니다. AES 또는 Blowfish 키에는 `aes_key`, 통합 문서 암호에는 `xlsx_password`를 사용합니다. 워크플로를 실행하기 전에 변수를 설정하고, 이 파일 전용으로 사용할 키를 지정하십시오. 키와 암호 필드는 변수 참조만 허용하므로 키를 단계에 직접 입력하는 일이 없습니다.

## 예외 사항

변환된 워크플로가 자체적으로 재현하지 못하는 동작입니다. 변환 보고서는 해당 동작이 발생하는 위치마다 이를 알려 줍니다.

- **내보내기 파일에 포함되지 않은 코드 또는 데이터**: 코드가 내보내기 파일에 없는 Gem Builder 또는 기타 사용자 지정 젬과, 내보내기 파일에서 빠진 dbt 패키지의 매크로 호출은 누락된 항목을 알려 주는 단계가 됩니다. 파이프라인 코드와 dbt 패키지를 포함하여 프로젝트를 내보내거나 Python 또는 SQL 단계에서 로직을 다시 구성하십시오. Ab Initio Error Detection 및 MTime 젬은 적용하는 규칙이 내보내기 파일에 없으므로 입력을 그대로 통과시킵니다. 프로젝트 밖의 파일에서 읽는 Soda 검사와, 이전 스캔이나 다른 데이터 세트와 비교하거나 Soda가 이름을 지정한 형식을 테스트하는 Soda 검사는 결과 테이블에 행이 없으므로 이후 단계에서 계산하십시오.
- **파이프라인이 실행될 때만 알 수 있는 결과**: 응답을 평탄화하는 REST API 젬은 필드 이름이 선언되어 있지 않으면 전체 응답을 열 하나에 넣으며, 이는 실행해야만 알 수 있습니다. 필요한 필드는 이후 단계에서 추출하십시오. dbt가 컴파일하는 동안 웨어하우스를 쿼리하는 dbt 매크로는 이를 알려 주는 단계가 되므로, 쿼리를 그 반환 값으로 바꾸십시오. Spark StoredProcedure 젬은 실행되지만 OUT 값은 반환되지 않으며, 출력은 통과 열입니다. `input_file_name()`은 이름을 지정할 파일이 없는 테이블 또는 Delta 소스에서는 빈 문자열을 반환하며, 집계, 윈도 또는 입력이 여러 개인 젬 안의 `hash()` / `xxhash64()`는 웨어하우스에서 계산되므로 Spark와 다를 수 있습니다.
- **프로젝트를 변환할 때 단계에 기록되는 값**: 따옴표, 백슬래시 또는 중괄호가 들어 있는 매개변수 값, SQL 단계가 읽는 파이프라인 값, 구성을 통해 Delta 테이블 작업이 지정하는 데이터베이스는 고정 값으로 단계에 기록되므로 워크플로 변수를 변경해도 바뀌지 않습니다. 구성이 바뀌면 단계를 편집하십시오.
- **Scala 코드**: Scala 스크립트, Scala 식, Scala 사용자 정의 함수 또는 집계 함수는 이를 알려 주는 단계가 되므로 SQL 또는 Python으로 다시 작성하십시오.
- **Kafka Kerberos 로그인**: Kerberos(GSSAPI)로 로그인하는 Kafka 소스 또는 대상은 Kerberos 서비스 이름과 로그인 메커니즘 없이 변환되므로 PlaidCloud 연결에서 설정하십시오.
- **스트리밍**: 스트리밍 소스, 대상, 파이프라인은 실행 시점에 존재하는 데이터에 대한 배치 워크플로로 실행됩니다. 필요한 빈도로 실행되도록 워크플로를 예약하십시오.
- **작업 구성 요소**: Spark 작업은 파이프라인 하나와 일정이 변환되며, 그 밖의 구성 요소, 실행 조건, 구성 재정의는 변환되지 않습니다.
- **드문 호출**: 롤업 또는 윈도에서 호출하는 사용자 정의 집계 함수와, if, for, set 및 일반적인 필터를 넘어서는 Jinja를 사용하는 dbt 매크로는 해당 젬을 알려 주는 단계가 됩니다. Aggregate 젬에서 함수를 호출하거나 매크로를 인라인으로 작성하십시오.

## 관련 가이드

- [Savant 분석 마이그레이션](/ko/guides/workflows/migrate-savant-analyses/)
- [Alteryx 워크플로 마이그레이션](/ko/guides/workflows/migrate-alteryx-workflows/)
- [문서 계정 추가](/ko/guides/documents/adding-accounts/)
- [워크플로 변수 관리](/ko/guides/workflows/manage-workflow-variables/)
- [워크플로 실행](/ko/guides/workflows/run-a-workflow/)
