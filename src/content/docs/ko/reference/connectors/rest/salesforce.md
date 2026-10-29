---
title: Salesforce REST 커넥터
description: PlaidCloud에서 OAuth 2.0 클라이언트 자격 증명 흐름으로 Salesforce REST API 연결을 설정하고 테스트한 다음, Salesforce Query Object 단계로 CRM 개체를 프로젝트 테이블로 가져옵니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/salesforce.md
---

## API 문서

[Salesforce REST API 참조](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.html)에는 레코드 및 메타데이터 엔드포인트가 문서화되어 있고, [Bulk API 2.0 개발자 가이드](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/bulk_api_2_0.htm)에는 [Salesforce: 개체 쿼리](/ko/reference/workflow-steps/salesforce/query-salesforce-object/) 단계가 실행되는 기반인 쿼리 작업이 문서화되어 있습니다.

Salesforce 측 앱, Run As 사용자, 연결 만들기, 테스트까지의 전체 안내는 [Salesforce에 연결](/ko/guides/connections/salesforce/) 가이드를 따르십시오. 이 페이지는 그 가이드의 바탕이 되는 필드 참조입니다.

## 인증 방식

이 커넥터는 **OAuth 2.0 클라이언트 자격 증명**으로 로그인합니다. PlaidCloud는 앱의 컨슈머 키와 시크릿을 조직 자체의 토큰 엔드포인트에서 액세스 토큰으로 교환하고, 앱의 **Run As** 설정에 지정된 사용자로 API를 호출합니다. 대화형 로그인, 새로 고침 토큰, 관리할 인증서가 없습니다.

이 교환에는 실무에서 중요한 두 가지 속성이 있습니다.

- **토큰 하나로 전체 추출을 처리합니다.** PlaidCloud는 연결과 환경별로 액세스 토큰을 만료 직전까지 캐시하므로, 페이지를 나눈 대규모 읽기도 페이지마다 다시 인증하지 않습니다. 취소, IP 제한, 세션 정책 변경 등으로 Salesforce가 더 이상 인정하지 않는 토큰은 폐기되고 자동으로 한 번 교체됩니다.
- **요청은 Salesforce가 지정한 곳으로 갑니다.** 토큰 응답이 조직의 인스턴스를 알려 주며, 이후의 모든 호출은 입력한 호스트가 아니라 해당 인스턴스를 대상으로 이루어지므로, My Domain이나 인스턴스가 변경된 후에도 연결이 계속 동작합니다.

REST API 버전은 변동되지 않고 연결별로 고정되므로, 조직 업그레이드가 저장된 단계 내부의 응답 형태를 조용히 바꿀 수 없습니다. 새 연결은 현재 지원되는 버전을 사용하며, 연결 구성 API를 통해 연결을 다른 버전에 고정할 수 있습니다. 고정된 버전이 지원 종료에 도달하면 Salesforce가 HTTP 410으로 응답하고 PlaidCloud가 어떤 버전이 폐기되었는지 알려 줍니다.

## 구성

이 필드는 **Tools > Connections**에서 Salesforce 연결을 만들거나 편집할 때 나타납니다.

### 계정 설명

| 필드 | 유형 | 설명 |
|---|---|---|
| 계정 이름 | 텍스트 | 이 연결의 표시 이름입니다. |
| 메모 | 텍스트(여러 줄) | 연결에 대한 선택적 메모입니다. |

### 연결

| 필드 | 유형 | 설명 |
|---|---|---|
| 호스트 또는 IP 주소 | 텍스트 | 조직의 My Domain 호스트입니다. 운영 및 Developer Edition은 `mycompany.my.salesforce.com`, 샌드박스는 `mycompany--uat.sandbox.my.salesforce.com`입니다. 생략하면 PlaidCloud가 `https://`를 추가합니다. |

### 인증 자격 증명

| 필드 | 유형 | 설명 |
|---|---|---|
| 클라이언트 ID | 텍스트 | 앱의 컨슈머 키입니다. |
| 클라이언트 시크릿 | 비밀번호 | 앱의 컨슈머 시크릿입니다. 암호화되어 저장됩니다. 변경하려면 새 값을 입력하고, 저장된 값을 유지하려면 비워 두십시오. |

### 사용법 및 보안

| 필드 | 유형 | 설명 |
|---|---|---|
| 활성(액세스 허용) | 토글 | 연결을 사용할 수 있는지 여부입니다. 연결을 삭제하지 않고 액세스를 일시 중지하려면 선택을 해제하십시오. |
| 보안 모델 | 선택 | 연결을 사용할 수 있는 대상으로, 소유자만, 특정 멤버, 특정 보안 그룹 또는 모든 워크스페이스 멤버입니다. |

각 연결은 환경마다 이 값 집합을 하나씩 보유하므로, 하나의 연결이 개발 환경에서는 샌드박스를, 운영 환경에서는 운영 조직을 가리킬 수 있습니다. 자격 증명은 환경별로 테스트하고 설정하십시오.

## 연결 테스트

**연결 테스트**는 실제 토큰 교환을 수행하고 자격 증명이 어떤 대상으로 인증되는지 보고합니다.

| 보고 항목 | 중요한 이유 |
|---|---|
| 조직 ID | 자격 증명이 어느 조직에 도달하는지 확인합니다. 샌드박스 자격 증명이 운영 환경에 저장된 경우를 가장 빠르게 찾아낼 수 있습니다. |
| API 버전 | 이 조직이 지원하는 가장 높은 버전입니다. 읽기는 이 버전이 아니라 연결에 고정된 버전(`salesforce_api_version`을 설정하지 않았다면 `v61.0`)에서 실행됩니다. |
| Run As 사용자 | 이 연결이 반환하는 모든 행과 필드가 범위로 한정되는 사용자입니다. 추출의 행 수를 신뢰하기 전에 이를 확인하십시오. |

테스트가 실패하면 원인이 표시됩니다. 인증 실패는 HTTP 상태를 보고하고 클라이언트 ID와 시크릿을 다시 입력하도록 안내합니다. 클라이언트 시크릿은 저장한 후에는 다시 읽을 수 없기 때문입니다.

## 알려진 제한 사항

- **Run As 사용자는 두 가지 다른 방식으로 모든 읽기의 범위를 정합니다.** 해당 사용자가 볼 수 없는 행은 오류나 건수 없이 그냥 누락됩니다. 해당 사용자가 읽을 수 없는 필드가 있으면 쿼리 전체가 실패합니다. 둘 다 [Run As 사용자가 모든 것의 범위를 정합니다](/ko/guides/connections/salesforce/#run-as-사용자가-모든-것의-범위를-결정합니다)에서 다룹니다.
- **읽기 전용입니다.** 이 커넥터는 데이터를 추출하며 레코드를 Salesforce에 다시 쓰지 않습니다.
- **일부 필드 유형은 추출할 수 없습니다.** 복합 주소 및 지리 위치 필드, `base64` 블롭, `encryptedstring`, `anyType`이 해당됩니다. 단계의 필드 선택기가 각각 표시하고 이유를 알려 줍니다. [단계가 거부하는 필드](/ko/reference/workflow-steps/salesforce/query-salesforce-object/#단계가-거부하는-필드)를 참조하십시오.
- **추출은 동기화가 아닙니다.** Salesforce에서 삭제된 레코드는 대상 테이블에 그대로 남아 있습니다.

## 관련 항목

- [Salesforce에 연결](/ko/guides/connections/salesforce/) — 단계별 안내
- [Salesforce: 개체 쿼리](/ko/reference/workflow-steps/salesforce/query-salesforce-object/)
- [연결 만들기 및 관리](/ko/guides/connections/create-connection/)
