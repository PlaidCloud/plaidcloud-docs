---
title: PlaidXL 문제 해결
description: 리본에 추가 기능이 보이지 않음, 로그인 팝업이 열리지 않음, 워크스페이스나 프로젝트가 보이지 않음, 테이블이 빨간색으로 표시됨, 가져오기가 느림, PlaidXL 수식 오류 등 PlaidXL의 일반적인 문제 해결 방법입니다.
sidebar:
  label: 문제 해결
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## 리본에 PlaidCloud 탭이 없음

- 모든 Excel 창을 닫고 Excel을 다시 엽니다. 새로 설치한 추가 기능은 다시 시작한 후에야 표시되는 경우가 많습니다.
- **삽입 → 내 추가 기능**을 열고 **PlaidCloud**를 선택합니다.
- Microsoft 365용 데스크톱 Excel 또는 Excel 2021 이상을 사용하고 있는지 확인합니다. [PlaidXL 설치](/ko/reference/cli/plaidxl/install/)를 참조하십시오.
- 조직에서 추가 기능을 관리하는 경우 Microsoft 365 관리자에게 **PlaidCloud** 추가 기능이 사용자에게 배포되었는지 문의하십시오.

## 로그인 팝업이 열리지 않음

**Sign In**을 클릭하면 Excel에서 팝업 창을 표시할지 묻습니다. 허용합니다. 메시지를 닫았다면 **Sign In**을 다시 클릭합니다.

팝업은 열리지만 로그인을 완료할 수 없다면 같은 이메일로 브라우저에서 PlaidCloud에 로그인해 보십시오. 암호가 만료되었거나 더 이상 가지고 있지 않은 2단계 인증 기기와 같은 문제는 먼저 PlaidCloud에서 해결해야 합니다. [멤버 인증](/ko/administration/access/member-authentication/)을 참조하십시오.

## 워크스페이스가 목록에 없음

**Select a tenant**에는 이메일 주소가 속한 워크스페이스가 나열됩니다. 하나가 없다면 해당 워크스페이스에 사용하는 이메일과 같은 이메일을 입력했는지 확인한 다음 워크스페이스 관리자에게 멤버인지 확인해 달라고 요청하십시오. [워크스페이스 멤버 관리](/ko/administration/access/overview/managing-workspace-members/)를 참조하십시오.

속한 다른 워크스페이스로 이동하려면 **Logout**을 클릭한 다음 다시 로그인합니다.

## 프로젝트, 테이블 또는 차원이 보이지 않음

PlaidXL에는 계정이 PlaidCloud에서 볼 수 있는 항목이 표시됩니다. 프로젝트가 보이지 않으면 프로젝트 소유자에게 액세스 권한을 요청하십시오. 테이블이 보이지 않으면 선택한 프로젝트에 테이블이 있고 데이터가 로드되었는지 확인하십시오. 한 번도 기록된 적이 없는 테이블은 선택할 때 **Unable to get table metadata**가 표시됩니다.

프로젝트, 테이블, 차원 목록의 폴더는 접힌 상태로 시작합니다. 폴더 안의 항목을 찾으려면 목록 위쪽의 필터 상자에 이름의 일부를 입력하십시오.

## 테이블이 빨간색으로 표시됨

테이블의 행 또는 열이 Excel 워크시트에 담을 수 있는 수를 초과합니다. 크기가 맞을 때까지 **고급**을 선택하여 행을 필터링하고 필요하지 않은 열의 선택을 해제합니다. [빨간색으로 표시되는 테이블](/ko/reference/cli/plaidxl/retrieve/#빨간색으로-표시되는-테이블)을 참조하십시오.

## 가져오기가 느림

Excel은 열이 많은 테이블에서 가장 느립니다. 필요하지 않은 열의 확인란을 선택 해제하고 **고급**으로 행을 필터링하십시오. 작업에 사용하는 데이터만 가져오면 더 빠르고 통합 문서도 작아집니다.

## 수식에 오류가 표시됨

| 표시되는 내용 | 확인할 사항 |
|---|---|
| `#SPILL!` | 결과에 필요한 셀에 다른 내용이 있습니다. 수식 아래나 옆의 셀을 비우십시오. |
| `#NAME?` | Excel이 함수를 인식하지 못합니다. PlaidXL이 설치되어 있는지(리본에 **PlaidCloud** 탭이 있는지) 확인하고 [함수 목록](/ko/reference/cli/plaidxl/functions/)에서 철자를 확인하십시오. |
| `PLAIDXL` 함수의 오류 | 로그인되어 있고 올바른 프로젝트가 선택되어 있는지 확인한 다음 모든 테이블, 열, 차원, 노드 이름을 PlaidCloud와 비교하십시오. 이름은 정확히 일치해야 합니다. |
| `CELL`이 필터 열을 찾을 수 없다고 보고함 | `DIMENSION_REPR`의 첫 번째 인수는 차원이 아니라 테이블의 열입니다. 테이블의 열 이름을 정확히 사용하십시오. [값](/ko/reference/cli/plaidxl/functions/#값)을 참조하십시오. |
| `CELL`이 0 또는 예상치 못한 합계를 반환함 | 노드 이름을 차원과 비교하십시오. 존재하지 않는 노드는 아무것도 롤업하지 않고 0을 반환합니다. 노드는 해당 차원에 연결된 열에서만 롤업되며, 다른 열에서는 값과 정확히 일치해야 합니다. |
| 데이터나 프로젝트를 변경해도 값이 바뀌지 않음 | 전체 다시 계산을 강제로 실행하십시오. Windows에서는 **Ctrl+Alt+F9**를 누릅니다. |
| `MEASURE_TYPE`이 오류를 반환함 | 소문자로 된 `sum`, `mean`, `median`, `min`, `max`, `std`, `var` 중 하나를 사용하십시오. |

## 수식이 다른 프로젝트의 데이터를 반환함

PlaidXL 함수는 작업 창에서 선택한 프로젝트에서 데이터를 읽으며, 이 선택은 열려 있는 모든 통합 문서에서 공유됩니다. 보고서를 작성한 대상 프로젝트를 선택한 다음 전체 다시 계산을 강제로 실행하십시오. **기본값으로 설정**은 프로젝트를 통합 문서에 저장하므로 해당 통합 문서에서 작업 창을 열 때 프로젝트가 선택되어 있습니다. [기본 프로젝트 설정](/ko/reference/cli/plaidxl/retrieve/#기본-프로젝트-설정)을 참조하십시오.

## 관련 항목

- [PlaidXL 설치](/ko/reference/cli/plaidxl/install/)
- [PlaidXL에 로그인](/ko/reference/cli/plaidxl/connect/)
- [도움말 얻기](/ko/guides/support/getting-help/) — 지원 티켓 열기
