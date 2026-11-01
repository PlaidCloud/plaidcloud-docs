---
title: PlaidXL에 로그인
description: 이메일과 평소 사용하는 로그인 방식(싱글 사인온 및 2단계 인증 포함)으로 PlaidXL을 PlaidCloud 워크스페이스에 연결하고, 로그아웃하거나 워크스페이스를 전환합니다.
sidebar:
  label: 로그인
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL은 브라우저에서 PlaidCloud에 사용하는 것과 동일한 로그인으로 사용자 본인으로 로그인합니다. 입력해야 하는 서버 주소가 없으며 통합 문서에 저장되는 비밀번호도 없습니다.

## 로그인

1. 작업 창을 엽니다. **PlaidCloud → Open PlaidXL**.
2. **Enter your email**에 PlaidCloud에 사용하는 이메일 주소를 입력하고 **Sign In**을 클릭합니다. PlaidXL은 다음에 사용할 수 있도록 주소를 기억합니다.
3. 이메일이 둘 이상의 워크스페이스에 속해 있다면 **Select a workspace**에서 하나를 선택하고 **Sign In**을 클릭합니다. PlaidXL은 선택한 항목을 기억합니다. 하나의 워크스페이스에 속해 있다면 PlaidXL이 자동으로 선택합니다. 이메일에 연결된 워크스페이스가 없으면 창에 그렇게 표시되므로 주소를 확인하고 다시 시도하십시오.
4. Excel에서 팝업 창을 허용할지 묻습니다. 허용합니다.
5. 팝업에서 평소 사용하는 방식으로 로그인합니다.
   - **PlaidCloud 로그인** — 이메일, 비밀번호, 그리고 설정해 둔 2단계 인증 코드.
   - **싱글 사인온** — 이미 조직에 로그인되어 있다면 이 단계는 바로 통과됩니다. 그렇지 않으면 조직의 로그인 페이지가 먼저 열립니다.
6. 팝업에 **Authenticated successfully**가 표시되면, 저절로 닫히지 않은 경우 직접 닫습니다.

이제 작업 창 머리글에 워크스페이스와 통합 문서에 연결된 프로젝트가 표시되며, 그 옆에 계정 메뉴가 있습니다. [테이블 및 차원 작업](/ko/reference/cli/plaidxl/retrieve/)으로 계속 진행하십시오.

계정에 2단계 인증 또는 싱글 사인온을 설정하려면 [멤버 인증](/ko/administration/access/member-authentication/)을 참조하십시오.

## 로그인 상태 유지

PlaidXL은 이 컴퓨터에서 로그인 상태를 유지하고 작업하는 동안 백그라운드에서 로그인을 갱신합니다. 이후 세션에서 작업 창을 열면 바로 프로젝트 목록으로 이동합니다. 로그인이 완전히 만료되었다면 PlaidXL이 이메일을 다시 묻습니다. 로그인을 갱신하는 중에 발생하는 짧은 네트워크 문제로는 로그아웃되지 않으며, PlaidXL이 다시 시도합니다.

## 볼 수 있는 항목

PlaidXL은 사용자의 권한으로 읽습니다. PlaidCloud에서 열 수 있는 프로젝트와 그 안의 테이블 및 차원만 표시되며 그 외에는 표시되지 않습니다. 프로젝트나 테이블이 보이지 않으면 프로젝트 소유자에게 액세스를 요청하십시오. 워크스페이스 멤버십이 작동하는 방식은 [조직과 워크스페이스 이해하기](/ko/administration/access/overview/organizations-and-workspaces-explained/)를 참조하십시오.

## 로그아웃 또는 워크스페이스 전환

작업 창 오른쪽 위의 계정 메뉴(점 세 개)를 클릭합니다. 이름과 워크스페이스가 표시되며 두 가지 명령이 있습니다.

- **Log out**은 로그인을 지우고 이메일 화면으로 돌아갑니다.
- **Switch workspace**는 로그아웃하고 이메일 화면으로 돌아가므로, **Select a workspace**에서 다른 워크스페이스를 선택할 수 있습니다.

로그인은 열려 있는 모든 통합 문서가 공유하지만, 각 통합 문서는 자체 프로젝트를 유지합니다. 통합 문서의 프로젝트는 워크스페이스에 속하므로, 전환한 후에는 이전 워크스페이스의 프로젝트에 연결된 통합 문서에는 프로젝트를 선택하기 전까지 프로젝트가 없습니다. [프로젝트는 통합 문서에 속합니다](/ko/reference/cli/plaidxl/retrieve/#프로젝트는-통합-문서에-속합니다)를 참조하십시오.

## 밝은 테마와 어두운 테마

작업 창은 Office 테마를 따르며 테마를 변경하면 함께 바뀝니다.

## 키보드와 스크린 리더

프로젝트, 테이블, 차원 목록의 행은 키보드 포커스를 받으며 **Enter**와 **공백** 키에 반응합니다. 선택된 행은 스크린 리더가 안내하며, 선택 상태와 경고 상태에는 색상뿐 아니라 아이콘도 표시됩니다.

## 관련 항목

- [PlaidXL 설치](/ko/reference/cli/plaidxl/install/) — 추가 기능을 설치하고 작업 창 열기
- [문제 해결](/ko/reference/cli/plaidxl/troubleshooting/) — 로그인 팝업이 열리지 않거나 워크스페이스가 보이지 않을 때
- [워크스페이스 보기 및 관리](/ko/administration/access/overview/viewing-and-managing-workspaces/) — 속해 있는 워크스페이스
