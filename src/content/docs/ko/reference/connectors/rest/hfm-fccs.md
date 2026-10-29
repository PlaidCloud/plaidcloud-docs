---
title: HFM / FCCS 커넥터
description: PlaidCloud에서 Oracle FCCS(Financial Consolidation and Close, EPM Cloud) 연결을 설정하여 POV 선택기로 임시 데이터 조각을 셀프 서비스로 가져오며, 선택적 캐싱과 예약된 반복 로드를 지원합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/hfm-fccs.md
---

PlaidCloud를 Oracle EPM Cloud의 일부인 Oracle **FCCS**(Financial Consolidation and Close)에 연결하면 재무 사용자가 HFM 팀에 요청 티켓을 올리지 않고도 데이터 조각을 셀프 서비스로 가져올 수 있습니다. [HFM/FCCS: 데이터 읽기(임시)](/ko/reference/workflow-steps/oracle-epm/hfm-fccs-read/) 단계는 실시간 쿼리처럼 느껴지지만, 내부적으로는 FCCS의 데이터 내보내기 작업 API에 대한 비동기 요청 → 폴링 → 가져오기입니다.

연결 종류는 연결 선택기에 **REST - HFM/FCCS**로 표시됩니다.

:::note[엔터티 차원의 범위 지정]
모든 POV(point of view)의 범위를 제한하십시오. 범위가 지정되지 않은 추출은 내보내기 작업이 실행되는 동안 FCCS 애플리케이션을 오랫동안 잠글 수 있습니다.
:::

## API 문서

이 커넥터는 Oracle EPM Cloud의 [REST API](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/index.html)를 사용합니다. 차원과 멤버를 찾는 애플리케이션 메타데이터 엔드포인트와, 그리드를 요청하고 폴링하고 가져오는 데이터 내보내기 작업 엔드포인트가 해당됩니다.

## 인증 방식

이 연결은 기존 EPM Cloud 포드에서 **서비스 계정을 사용한 HTTP Basic 인증**을 사용하며, OAuth나 토큰 흐름은 없습니다(OCI / Gen 2 베어러 토큰 포드는 범위에 포함되지 않습니다). **ID 도메인**을 설정하면 PlaidCloud는 로그인 이름을 `identitydomain.username`(도메인, 점, 사용자 이름 순)으로 구성합니다. ID 도메인을 비워 두었거나 사용자 이름에 이미 점이 포함되어 있으면 사용자 이름이 그대로 전송됩니다. 셀프 서비스 사용자가 가져올 애플리케이션과 POV 조각에 대한 읽기 권한이 있는 전용 통합 서비스 계정을 연결에 지정하십시오.

## 구성

| 필드 | 필수 | 설명 |
|---|---|---|
| 이름 | 예 | 이 연결의 표시 이름입니다. |
| EPM Cloud URL | 예 | EPM Cloud 포드/서비스 URL입니다(예: `https://planning-test-yourdomain.epm.us2.oraclecloud.com`). |
| ID 도메인 | 아니요 | EPM Cloud ID 도메인입니다. 설정하면 PlaidCloud가 로그인할 때 사용자 이름 앞에 `identitydomain.username` 형식으로 붙입니다. |
| 사용자 이름 | 예 | 통합 서비스 계정의 사용자 이름입니다. |
| 비밀번호 | 예 | 서비스 계정의 비밀번호입니다. 암호화되어 저장됩니다. |
| 기본 애플리케이션 | 아니요 | 단계의 POV 선택기에 미리 채울 기본 FCCS 애플리케이션입니다. 각 단계에서 재정의할 수 있습니다. |

## 연결로 할 수 있는 작업

- **임시 조각을 셀프 서비스로 가져오기.** 단계 양식에서 POV(애플리케이션과 FCCS 차원)를 구성하고 실행을 누르면 결과 테이블이 자동으로 만들어집니다. [HFM/FCCS: 데이터 읽기(임시)](/ko/reference/workflow-steps/oracle-epm/hfm-fccs-read/)를 참조하십시오.
- **티켓 생략.** 조각은 연결의 서비스 계정으로 실행되므로, 재무 사용자가 HFM 관리자를 기다리지 않고 직접 데이터를 가져옵니다.
- **반복 가져오기 캐싱.** 같은 POV와 기준 시점을 다시 요청하면 FCCS를 다시 호출하는 대신 이미 가져온 사본을 즉시 반환합니다.
- **엔터티별 조회 권한 관리.** 가져온 테이블은 **행 수준 보안을 적용할 준비**가 되어 있습니다. 관리자가 `Entity` 열에 행 액세스를 선언하면 셀프 서비스 사용자는 자신에게 권한이 있는 엔터티만 볼 수 있습니다. 이는 자동이 아니라 관리자의 통제 아래 관리됩니다. 단계 참조를 확인하십시오.
- **반복 로드 예약.** **대상 범위 지정**을 사용하면 임시 조각을 덮어쓰지 않고 병합하며 누적해서 늘어나는 영구 테이블로 승격할 수 있으므로, 같은 단계를 예약된 워크플로에 배치하면 야간 반복 로드가 됩니다.

## 메타데이터 검색

지원되는 FCCS 포드에서는 연결과 애플리케이션을 선택하면 단계 양식이 애플리케이션 메타데이터에서 각 차원의 멤버 목록을 실시간으로 검색하므로, POV 선택기가 선택할 수 있는 실제 멤버를 제공합니다(둘 중 하나가 바뀔 때마다 다시 검색합니다). 메타데이터 엔드포인트를 제공하지 않는 이전 포드에서는 검색 결과가 비어 있고 선택기는 수동 입력으로 전환됩니다. 멤버 이름을 직접 입력하며, 저장된 POV는 항상 그대로 다시 불러와집니다. 어느 쪽이든 가져오기는 동일하게 동작합니다.

## 알려진 제한 사항

| 제한 사항 | 의미 |
|---|---|
| 읽기 전용 | 이 커넥터는 FCCS에서 데이터를 추출합니다. 연결 데이터를 쓰거나, 연결 작업을 실행하거나, 다시 전기하지 않습니다. |
| 엔터티 차원의 범위 지정 | 범위가 지정되지 않은 추출(`Entity` 선택 없음)은 내보내기 작업이 실행되는 동안 FCCS 애플리케이션을 오랫동안 잠글 수 있습니다. 엔터티 선택을 제한된 범위로 유지하십시오. |
| 이전 포드에서는 수동 멤버 입력 | 포드가 메타데이터 엔드포인트를 제공하지 않는 경우 멤버 목록이 자동으로 채워지지 않으므로 멤버 이름을 직접 입력하십시오. |
| 행 수준 보안은 자동이 아니라 관리자가 관리 | 가져온 테이블은 행 액세스로 관리할 수 있지만, 관리자가 게시하고, `Entity` 열을 선언하고, 첫 관리 대상 쓰기를 승인하고, 조정해야 합니다. 그때까지는 테이블이 필터링되지 않습니다. |

## 관련 항목

- [HFM / FCCS에서 추출(가이드)](/ko/guides/connections/hfm-fccs/) — 연결을 만들고, POV를 구성하고, 실행하고, 캐시하고, 관리하고, 예약합니다.
- [HFM/FCCS: 데이터 읽기(임시)](/ko/reference/workflow-steps/oracle-epm/hfm-fccs-read/) — 단계 필드 참조입니다.
- [보안 그룹 및 할당 관리](/ko/administration/access/managing-security-groups-and-assignments/) — 행 액세스가 가져온 테이블을 관리하는 방식입니다.
- [연결 만들기 및 관리](/ko/guides/connections/create-connection/)
