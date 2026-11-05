---
title: Get Workspace Usage 단계
description: 사용 현황 보고서의 워크스페이스 사용 합계를 일별 또는 월별로 프로젝트 테이블에 기록하여 도입 추이를 차트로 나타내거나 후속 단계에 전달합니다.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## 설명

워크스페이스 사용 현황 요약을 프로젝트 테이블에 기록합니다. 시간에 따른 도입 추이를 추적하거나, 사용 현황을 기반으로 자체 대시보드를 만들거나, 예약된 워크플로에서 활동 감소를 표시하는 데 사용하십시오. 수치는 [사용 현황 보고서](/ko/administration/access/usage-reports/)에 표시되는 것과 같습니다.

출력에는 합계만 포함됩니다. 멤버를 지칭하는 행은 없으며 노트북 경로는 `*`로 대체됩니다. 사용 기록이 삭제된 멤버는 제외됩니다.

## 구성

### 사용 데이터

**데이터 세트**는 각 행에 담기는 내용을 선택합니다.

| 데이터 세트 | 행 단위 | 열 |
|---|---|---|
| **항목별 일간** | 일, 영역, 이벤트, 대상 | `day`, `source`, `event`, `subject`, `events` |
| **항목별 월간** | 월, 영역, 이벤트, 대상 | `month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial` |
| **월간 합계**(기본값) | 월과 영역 | `month`, `source`, `active_users`, `coverage_start`, `partial` |

`partial`은 기록이 전체를 포함하지 않는 월에 대해 true이며, `coverage_start`는 수집이 시작된 날짜입니다.

**영역**은 행을 한 영역으로 제한합니다. **PlaidCloud 앱**, **대시보드**, **앱**, **앱 방문**, **노트북** 중에서 선택합니다. 모든 영역을 포함하려면 **모든 영역**으로 두십시오.

### 날짜 범위

**범위**는 읽을 날짜를 선택합니다.

- **최근 일수**(기본값 30)는 오늘을 포함하여 가장 최근 며칠을 읽습니다.
- **지난달**은 직전의 전체 달력 월을 읽습니다.
- **이번 달 누계**는 이번 달 1일부터 오늘까지 읽습니다.
- **날짜 사이**는 **시작 날짜**부터 **종료 날짜**까지 읽습니다. **종료 날짜**를 비워 두면 오늘까지 읽습니다.

일과 날짜는 UTC 기준입니다. **일**, **시작 날짜**, **종료 날짜**에는 숫자나 `YYYY-MM-DD` 날짜뿐 아니라 `{report_start}` 같은 [변수](/ko/guides/workflows/manage-workflow-variables/)도 사용할 수 있습니다. 시작은 종료보다 늦으면 안 됩니다.

### 사용 대상

**대상 테이블**이 결과를 받습니다. 이 단계는 테이블에 있던 내용을 대체하며, 행이 없는 경우에도 항상 데이터 세트의 열을 기록합니다.

## 경고

이러한 경우에도 단계는 실패하지 않습니다. 무슨 일이 있었는지 알려 주는 경고와 함께 끝나며 테이블은 여전히 기록됩니다.

- 워크스페이스에 아직 사용 현황 수집이 설정되지 않았습니다.
- 범위에 사용 기록이 없습니다.
- 범위가 보관된 기간보다 앞에서 시작하므로, 기록이 시작되는 지점에서 시작하도록 잘렸습니다. 일간 데이터는 180일, 월간 데이터는 25개월간 보관됩니다.

## 보안 로그

실행할 때마다 데이터 세트, 범위, 대상 테이블, 워크플로, 단계, 실행, 기록된 행 수를 기록하는 항목이 보안 로그에 기록됩니다.

## 관련 문서

- [일반 단계](/ko/reference/workflow-steps/general/)
- [사용 현황 보고서](/ko/administration/access/usage-reports/)
- [Get Workspace Members 단계](/ko/reference/workflow-steps/general/get-workspace-members/)
