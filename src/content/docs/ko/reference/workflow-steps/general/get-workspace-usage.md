---
title: Get Workspace Usage 단계
description: 사용 현황 보고서의 워크스페이스 사용량 합계를 일별 또는 월별로 프로젝트 테이블에 기록하여 도입률을 차트로 표시하거나 후속 단계에 활용합니다.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## 설명

워크스페이스 사용 현황 요약을 프로젝트 테이블에 기록합니다. 시간에 따른 도입률을 추적하거나, 사용 현황에 대한 자체 대시보드를 만들거나, 예약된 워크플로에서 활동 감소를 감지할 때 사용하십시오. 수치는 [사용 현황 보고서](/ko/administration/access/usage-reports/)에 표시되는 것과 동일합니다.

출력에는 합계만 포함됩니다. 멤버 이름이 나오는 행은 없으며 노트북 경로는 `*`로 대체됩니다. 사용 기록이 삭제된 멤버는 제외됩니다.

## 구성

### 사용 현황 데이터

**데이터 세트**는 각 행에 담길 내용을 선택합니다.

| 데이터 세트 | 행 단위 | 열 |
|---|---|---|
| **항목별 일별** | 일, 영역, 이벤트, 대상 | `day`, `source`, `event`, `subject`, `events` |
| **항목별 월별** | 월, 영역, 이벤트, 대상 | `month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial` |
| **월별 합계**(기본값) | 월, 영역 | `month`, `source`, `active_users`, `coverage_start`, `partial` |

`partial`은 기록이 전체를 포함하지 않는 월에 대해 true이며, `coverage_start`는 수집이 시작된 날짜입니다.

**영역**은 행을 하나의 영역으로 제한합니다. **PlaidCloud 앱**, **대시보드**, **앱**, **앱 방문**, **노트북** 중에서 선택합니다. 모든 영역을 포함하려면 **전체 영역**으로 두십시오.

### 날짜 범위

**범위**는 읽을 일자를 선택합니다.

- **최근 일수**(기본값 30)는 오늘을 포함하여 가장 최근 일자를 읽습니다.
- **지난달**은 직전의 전체 달력 월을 읽습니다.
- **이번 달 누계**는 이번 달 1일부터 오늘까지 읽습니다.
- **날짜 사이**는 **시작 날짜**부터 **종료 날짜**까지 읽습니다. 오늘까지 읽으려면 **종료 날짜**를 비워 두십시오.

일자와 날짜는 UTC 기준입니다. **일**, **시작 날짜**, **종료 날짜**에는 숫자나 `YYYY-MM-DD` 날짜뿐 아니라 `{report_start}` 같은 [변수](/ko/guides/workflows/manage-workflow-variables/)도 사용할 수 있습니다. 시작일은 종료일보다 늦을 수 없습니다.

### 사용 현황 대상

**대상 테이블**이 결과를 받습니다. 이 단계는 테이블에 있던 내용을 대체하며, 행이 없을 때도 항상 데이터 세트의 열을 기록합니다.

## 경고

다음은 단계를 실패시키지 않습니다. 단계는 일어난 일을 알리는 경고와 함께 완료되며 테이블도 계속 기록합니다.

- 워크스페이스에 사용 현황 수집이 아직 설정되지 않았습니다.
- 해당 범위에 사용 기록이 없었습니다.
- 범위가 보관된 기간보다 앞서 시작하므로 기록이 시작되는 시점부터 시작하도록 잘렸습니다. 일별 데이터는 180일간, 월별 데이터는 25개월간 보관됩니다.

## 보안 로그

실행할 때마다 데이터 세트, 범위, 대상 테이블, 워크플로, 단계, 실행, 기록된 행 수를 기록한 항목이 보안 로그에 남습니다.

## 관련 항목

- [일반 단계](/ko/reference/workflow-steps/general/)
- [사용 현황 보고서](/ko/administration/access/usage-reports/)
- [Get Workspace Members 단계](/ko/reference/workflow-steps/general/get-workspace-members/)
