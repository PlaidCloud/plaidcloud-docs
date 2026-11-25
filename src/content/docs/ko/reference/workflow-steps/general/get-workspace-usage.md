---
title: Get Workspace Usage 단계
description: 워크스페이스 사용 현황을 활동, 멤버, 내용 또는 추세 형태로 프로젝트 테이블에 기록하여 도입 현황을 보고하거나 후속 단계에 활용합니다.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## 설명

워크스페이스 사용 현황을 프로젝트 테이블에 기록합니다. 시간에 따른 도입 추세를 추적하거나, 부서 또는 팀별 사용 현황을 보고하거나, 자체 대시보드를 구축하거나, 예약된 워크플로에서 활동 감소를 감지하는 데 사용하십시오. 수치는 [사용 현황 보고서](/ko/administration/access/usage-reports/)와 동일한 사용량 데이터를 기반으로 하며, 모든 데이터 세트는 모든 영역을 포함합니다.

**활동**과 **멤버**에는 멤버 식별 정보(사용자 ID, 사용자 이름, 이메일, 이름과 성, 보안 그룹)가 들어 있습니다. 대상 테이블은 일반 프로젝트 테이블이므로 프로젝트에 액세스할 수 있는 사람은 누구나 읽을 수 있습니다. 멤버 목록과 동일하게 취급하십시오. 테이블에 쓰는 실행은 매번 보안 로그에 기록됩니다.

## 구성

### 사용 데이터

**데이터 세트**는 각 행에 담기는 내용을 선택합니다. 그 아래의 설명 줄에는 선택한 데이터 세트의 행과 열이 표시됩니다.

| 데이터 세트 | 값 | 행 단위 | 식별 정보 포함 |
|---|---|---|---|
| **활동**(기본값) | `activity` | 일, 멤버, 작업, 항목 | 예 |
| **멤버** | `members` | 멤버 1명(활동이 없는 멤버 포함) | 예 |
| **내용** | `content` | 대시보드, 앱, 노트북(아무도 사용하지 않은 대시보드와 앱 포함) | 아니요 |
| **추세** | `trends` | 범위의 일, 주, 월 | 아니요 |

이 값은 API 또는 AI 어시스턴트를 통해 단계를 만들거나 편집할 때 단계에 저장되는 값입니다. 이 목록에 없는 데이터 세트로 저장된 단계는 실행할 때 실패하며 네 개의 데이터 세트 이름이 안내됩니다. 단계를 열어 **데이터 세트**를 선택하고 저장하십시오. 이전에 저장된 **멤버** 또는 **내용** 단계는 계속 실행되며 아래 열을 기록합니다. 하나의 영역으로 제한되어 있던 단계는 이제 모든 영역을 포함합니다.

### 열

날짜와 일은 UTC 자정의 타임스탬프로 기록됩니다.

#### 멤버 열

**활동**과 **멤버**에는 다음 열이 포함됩니다.

| 열 | 내용 |
|---|---|
| `user_id` | 멤버의 ID입니다. |
| `user_name` | 멤버의 사용자 이름입니다. |
| `email` | 멤버의 이메일 주소이며 소문자입니다. |
| `first_name` | 이름입니다. |
| `last_name` | 성입니다. |
| `is_active` | 멤버가 활성 상태이면 true, 비활성화되었으면 false입니다. |
| `groups` | 멤버의 보안 그룹이며 `; `로 구분됩니다. |

`groups`에는 최상위 그룹만 나열됩니다. 하위 그룹은 확장되지 않습니다.

#### 활동

| 열 | 내용 |
|---|---|
| `day` | 일입니다. |
| 멤버 열 | 위와 같습니다. |
| `member` | 멤버의 이름과 성이며, 둘 다 설정되어 있지 않으면 사용자 이름입니다. |
| `area` | `PlaidCloud app`, `Dashboards`, `Apps` 또는 `Notebooks`입니다. |
| `action` | `Opened app`, `Opened screen`, `Opened step`, `Saved step`, `Used palette action`, `Viewed dashboard`, `Used chart`, `Opened notebook` 또는 `Saved notebook`입니다. |
| `item_type` | `App area`, `Screen`, `Step`, `Palette action`, `Dashboard`, `Chart`, `App` 또는 `Notebook`입니다. |
| `item_id` | 항목의 ID입니다. 노트북의 경우 해당 경로입니다. |
| `item_name` | 항목의 이름입니다. 화면 또는 앱 영역은 `Members List`와 같이 풀어쓴 이름, 단계는 단계 유형, 대시보드·차트·앱은 해당 이름, 노트북은 해당 경로입니다. 이름을 찾을 수 없으면 항목의 ID입니다. |
| `events` | 멤버가 그날 해당 작업을 수행한 횟수입니다. |
| `source` | 영역의 키이며 [사용 현황 보고서](/ko/administration/access/usage-reports/) 내보내기에서 사용하는 이름과 같습니다. |
| `event` | 작업의 키이며 내보내기에서 사용하는 이름과 같습니다. |

`member`와 멤버 열은 작업을 수행한 주체에 따라 달라집니다.

- 어떤 멤버에도 연결할 수 없는 활동은 `member`가 `Unattributed`이고 멤버 열이 비어 있습니다.
- 이후에 삭제된 멤버는 `user_id`만 유지되며 `member`는 `Deleted user`입니다.
- 서비스 계정이나 에이전트와 같은 그 밖의 계정은 `user_id`만 유지되며 `member`는 해당 사용자 이름입니다.

`Used chart`는 5분 구간마다 멤버와 차트당 한 번씩 계산되므로 쿼리 수가 아니라 사용량을 나타냅니다.

#### 멤버

| 열 | 내용 |
|---|---|
| 멤버 열 | 위와 같습니다. |
| `member` | 멤버의 이름과 성이며, 둘 다 설정되어 있지 않으면 사용자 이름입니다. |
| `created` | 멤버가 워크스페이스에 추가된 날이며, 알 수 있는 경우에 한합니다. |
| `status` | 범위 내에서 멤버가 활동했으면 `Active`, 이전에는 PlaidCloud를 사용했지만 범위 내에서는 사용하지 않았으면 `Dormant`, 범위 종료 시점까지 기록된 사용이 없으면 `Never active`입니다. |
| `first_seen` | 범위와 관계없이 기록상 멤버가 PlaidCloud를 처음 사용한 날입니다. |
| `last_seen` | 범위 내에서 멤버가 마지막으로 활동한 날입니다. |
| `active_days` | 범위 내에서 활동이 있었던 일수입니다. |
| `events` | 범위 내 활동 이벤트 수입니다. |
| `active_minutes` | 범위 내 활동 시간(분)입니다. |
| `session_minutes` | 범위 내 세션 시간(분)입니다. |
| `app_open_minutes` | 범위 내에서 멤버가 패널 앱을 열어 둔 시간(분)입니다. Studio 미리 보기는 계산되지 않습니다. |

비활성화된 멤버를 포함하여 사용 기록이 삭제된 멤버를 제외한 모든 멤버에게 행이 있습니다. 서비스 계정과 에이전트는 나열되지 않습니다. 범위 내에 활동이 없는 멤버는 `last_seen`이 없으며 다른 활동 열은 비어 있거나 0입니다.

#### 내용

| 열 | 내용 |
|---|---|
| `type` | `Dashboard`, `App` 또는 `Notebook`입니다. |
| `item_id` | 대시보드 또는 앱의 ID이거나 노트북의 경로입니다. |
| `name` | 대시보드 또는 앱의 이름이거나 노트북의 경로입니다. 항목이 삭제되었거나 이름을 읽을 수 없으면 비어 있습니다. |
| `deleted` | 대시보드 또는 앱이 이후에 삭제되었으면 true입니다. |
| `unused` | 범위 내에서 아무도 사용하지 않은 대시보드 또는 앱이면 true입니다. |
| `users` | 범위 내에서 항목을 사용한 멤버 수입니다. |
| `opens` | 범위 내에서 항목을 연 횟수이며, 멤버에게 귀속할 수 없는 열기도 포함됩니다. |
| `last_used` | 범위 내에서 마지막으로 사용된 날입니다. 사용되지 않은 항목은 범위 종료 전에 마지막으로 열린 날이며, 없으면 비어 있습니다. |
| `app_open_minutes` | 범위 내에서 패널 앱이 열려 있던 시간(분)입니다. 대시보드, 노트북, Dash 앱 및 WASM 앱은 비어 있습니다. |

노트북 경로마다 고유한 행이 있습니다. 행은 사용된 항목이 먼저 나열되며 사용자 수가 많은 순서이고, 그다음에 아무도 사용하지 않은 대시보드와 앱이 나옵니다. 이들은 게시된 대시보드와 범위가 시작될 때 이미 존재하던 앱입니다. 범위가 보관된 일별 데이터 안에서 시작하고, 그 시점에 해당 종류의 항목 사용량이 수집되고 있었으며, 이름을 읽을 수 있는 경우에만 나열됩니다. 앱의 Studio 미리 보기는 제외됩니다.

#### 추세

| 열 | 내용 |
|---|---|
| `period` | `Day`, `Week` 또는 `Month`입니다. |
| `period_start` | 기간의 첫째 날입니다. 주는 월요일에 시작합니다. |
| `active_members` | 범위 내에서 해당 기간에 활동한 멤버 수입니다. |
| `events` | 해당 기간의 활동 이벤트 수입니다. |
| `active_minutes` | 해당 기간의 활동 시간(분)입니다. |
| `session_minutes` | 해당 기간의 세션 시간(분)입니다. |
| `active_members_7d` | `Day` 행에서 해당 일로 끝나는 7일 동안 활동한 멤버 수입니다. |
| `active_members_28d` | `Day` 행에서 해당 일로 끝나는 28일 동안 활동한 멤버 수입니다. |
| `stickiness` | `Day` 행에서 `active_members`를 `active_members_28d`로 나눈 값입니다. |
| `complete` | 오늘, 오늘이 포함된 주 또는 월, 범위에 의해 잘린 주 또는 월에 대해 false입니다. |

보관된 일별 데이터가 시작되는 시점부터 범위의 모든 날에는 사용 기록이 없더라도 행이 있으며, 그 날들이 속한 모든 주와 월에도 행이 있습니다. `active_members_7d`, `active_members_28d`, `stickiness`는 `Week` 및 `Month` 행에서 비어 있으며, 7일 또는 28일이 보관된 일별 데이터보다 이전에 걸치는 `Day` 행에서도 비어 있습니다. 보관된 일별 데이터보다 이전에 시작하고 범위에 완전히 포함되는 월은 월별 요약에서 가져옵니다. 이 경우 `active_members`는 있지만 이벤트와 시간(분)은 비어 있으며, `complete`는 요약이 해당 월 전체를 포함했는지 나타냅니다.

### 예: 부서별 활동 시간

**활동**과 **멤버**에는 멤버의 `email`이 소문자로 들어 있으므로, 인사 또는 조직 마스터 테이블과 같은 자체 테이블에 조인하여 부서별로 보고할 수 있습니다.

1. **데이터 세트**를 **멤버**로 설정하고 `usage_members`와 같은 대상 테이블을 지정하여 **Get Workspace Usage** 단계를 추가합니다.
2. 소문자 `email` 열이 일치하는 곳에서 `usage_members`를 조직 테이블에 조인하는 **테이블: 내부 조인** 단계를 추가합니다. 조직 테이블에서는 부서를, `usage_members`에서는 `active_minutes`와 `events` 열을 유지합니다.
3. 같은 단계에서 부서별로 집계하고 `active_minutes`를 합산합니다.

결과는 부서별 활동 시간입니다. 조직 테이블에 없는 멤버는 내부 조인에서 제외되므로 이들을 확인하려면 왼쪽 조인을 사용하십시오. **활동**에 대해 두 번째 단계를 사용하여 같은 방식으로 반복하고 부서와 `item_name`별로 `events`를 합산하면 어느 부서가 어떤 대시보드와 앱을 사용하는지 보고할 수 있습니다.

### 날짜 범위

**범위**는 읽을 일자를 선택합니다.

| 범위 | 값 | 읽는 기간 |
|---|---|---|
| **최근 일수**(기본값 30) | `last_days` | 오늘을 포함한 최근 일수입니다. |
| **이전 달** | `previous_month` | 마지막으로 완료된 달력 월입니다. |
| **이번 달 누계** | `month_to_date` | 이번 달 1일부터 오늘까지입니다. |
| **날짜 사이** | `dates` | **시작 날짜**부터 **종료 날짜**까지입니다. 오늘까지 읽으려면 **종료 날짜**를 비워 두십시오. |

일수와 날짜는 UTC입니다. **일**에는 정수를 입력합니다. **시작 날짜**와 **종료 날짜**에는 `YYYY-MM-DD` 날짜 또는 `{report_start}`와 같은 [변수](/ko/guides/workflows/manage-workflow-variables/)를 사용할 수 있습니다. 시작은 종료보다 늦어서는 안 됩니다.

일별 데이터는 180일 동안, 월별 요약은 25개월 동안 보관됩니다.

### 사용 대상

**대상 테이블**이 결과를 받습니다. 이 단계는 테이블에 있던 내용을 대체하며, 행이 없는 경우에도 항상 데이터 세트의 열을 기록합니다.

## 경고

이러한 경우에는 단계가 실패하지 않습니다. 경고와 함께 완료되며 테이블은 데이터 세트의 열과 함께 그대로 대체됩니다.

| 경고 | 의미 |
|---|---|
| "Usage data is not available yet: the usage database has not been set up on this workspace." | 워크스페이스에 대해 사용 현황 수집이 아직 설정되지 않았습니다. |
| "Usage data is not available right now: the usage database could not be reached." | 사용량 데이터를 읽을 수 없었습니다. 나중에 단계를 다시 실행하십시오. |
| "No usage from *start* to *end*." | 범위 내에 사용 기록이 없었습니다. |
| "Usage before *date* isn't kept, so the range was clipped to start there." | 범위가 보관된 일별 데이터보다 이전에 시작하므로 활동이 *date*부터 집계됩니다. **추세**에는 그 이전의 전체 월이 월별 요약에서 여전히 포함됩니다. |
| "This took too long to compute: narrow the date range." | 읽기 시간이 초과되어 테이블에 행이 없습니다. 더 짧은 범위를 선택하십시오. |
| "Some names are unavailable right now, so those items are named by their id." | **활동**에만 해당합니다. 일부 대시보드, 차트 또는 앱 이름을 읽을 수 없어 `item_name`에 ID가 들어갑니다. |
| "Members could not be read right now, so they are named by their id." | **활동**에만 해당합니다. 멤버 목록을 읽을 수 없어 `member`에 멤버의 ID가 들어가며, 멤버 열 중 `user_id`만 채워집니다. |
| "Names are unavailable right now, so items nobody used are not listed." | **내용**에만 해당합니다. 대시보드 또는 앱 이름을 읽을 수 없어 사용된 항목만 나열됩니다. |
| "Activity before *date* isn't kept, so items nobody used in this range can't be listed." | **내용**에만 해당합니다. 범위가 보관된 일별 데이터보다 이전에 시작하므로 사용된 항목만 나열됩니다. |

멤버 목록을 읽을 수 없으면 **멤버**는 대신 실패하며 대상 테이블은 그대로 유지됩니다.

## 보안 로그

테이블에 쓰는 실행은 매번 데이터 세트, 범위, 대상 테이블과 해당 프로젝트, 워크플로, 단계, 실행, 기록된 행 수를 담은 항목이 보안 로그에 기록되며, **활동**과 **멤버**의 경우 행에 멤버 식별 정보가 들어 있다는 내용도 함께 기록됩니다.

## 관련 항목

- [일반 단계](/ko/reference/workflow-steps/general/)
- [사용 현황 보고서](/ko/administration/access/usage-reports/)
- [Get Workspace Members](/ko/reference/workflow-steps/general/get-workspace-members/)
