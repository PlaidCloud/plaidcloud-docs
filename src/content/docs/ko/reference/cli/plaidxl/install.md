---
title: PlaidXL 설치
description: Windows 또는 Mac의 Excel에 PlaidXL 추가 기능을 추가하고 PlaidCloud 리본 탭을 찾아 PlaidXL 작업 창을 엽니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

PlaidXL은 통합 문서마다가 아니라 컴퓨터당 한 번만 설치합니다. 설치 후에는 열어 보는 모든 통합 문서의 Excel 리본에 **PlaidCloud** 탭이 표시됩니다.

## 시작하기 전에

- Windows 또는 Mac에서 Microsoft 365용 Excel 또는 Excel 2021 이상을 사용하십시오.
- 조직에서 Office 추가 기능을 중앙에서 관리하는 경우 Microsoft 365 관리자가 PlaidXL을 대신 배포해야 할 수 있습니다. 직접 추가 기능을 설치할 수 없다면 관리자에게 **PlaidCloud** 추가 기능을 추가해 달라고 요청하십시오.

## Windows에서 설치

1. Excel에서 **삽입 → 추가 기능**을 엽니다(일부 버전에서는 **홈 → 추가 기능**).
2. 추가 기능 검색 상자에 `PlaidCloud`를 입력합니다.
3. **PlaidCloud** 추가 기능을 선택하고 **추가**를 클릭합니다.

## Mac에서 설치

1. Excel for Mac에서 **삽입 → 추가 기능**을 엽니다. 이전 버전에서는 메뉴가 **삽입 → 스토어**입니다.
2. 추가 기능 검색 상자에 `PlaidCloud`를 입력합니다.
3. **PlaidCloud** 추가 기능을 선택하고 **추가**를 클릭합니다.

## 작업 창 열기

1. 리본에서 **PlaidCloud** 탭을 클릭합니다.
2. **PlaidXL Controls** 그룹에서 **Show Taskpane**을 클릭합니다.

PlaidXL 작업 창이 창 오른쪽에 열리고 로그인을 요청합니다. 계속해서 [로그인](/ko/reference/cli/plaidxl/connect/)을 진행합니다.

작업 창은 세션 간에 로그인 상태를 유지하므로 보통 한 번 로그인한 후에는 필요할 때 작업 창만 열면 됩니다.

## PlaidXL이 표시되지 않는 경우

- 모든 Excel 창을 닫고 Excel을 다시 엽니다. 추가 기능은 Excel을 다시 시작해야 리본에 표시되는 경우가 많습니다.
- **삽입 → 내 추가 기능**(Windows) 또는 **삽입 → 추가 기능 → 내 추가 기능**(Mac)에서 **PlaidCloud**를 선택합니다.
- 조직에서 스토어의 추가 기능을 차단하는 경우 Microsoft 365 관리자에게 배포를 요청하십시오.

더 많은 해결 방법은 [문제 해결](/ko/reference/cli/plaidxl/troubleshooting/) 페이지에 있습니다.

## 관련 항목

- [로그인](/ko/reference/cli/plaidxl/connect/) — 추가 기능을 워크스페이스에 연결
- [PlaidCloud 리본](/ko/reference/cli/plaidxl/ribbon/) — **PlaidCloud** 탭의 모든 명령
