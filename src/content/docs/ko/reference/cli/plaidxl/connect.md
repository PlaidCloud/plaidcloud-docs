---
title: PlaidXL에 로그인
description: 이메일과 평소 사용하는 로그인 방식(SSO 및 2단계 인증 포함)으로 PlaidXL을 PlaidCloud 워크스페이스에 연결하고, 로그아웃하거나 워크스페이스를 전환합니다.
sidebar:
  label: 로그인
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL은 브라우저에서 PlaidCloud에 사용하는 것과 동일한 로그인 방식으로 사용자 본인으로 로그인합니다. 입력해야 하는 서버 주소도 없고 통합 문서에 저장되는 암호도 없습니다.

## 로그인

1. 작업 창을 엽니다. **PlaidCloud → Show Taskpane**을 선택합니다.
2. **Enter your email** 아래에 PlaidCloud에 사용하는 이메일 주소를 입력하고 **Sign In**을 클릭합니다.
3. 이메일이 여러 워크스페이스에 속해 있으면 **Select a tenant**에서 하나를 선택하고 **Sign In**을 클릭합니다. (PlaidXL에서 *테넌트*는 사용자의 PlaidCloud 워크스페이스를 의미합니다.) 워크스페이스가 하나뿐이면 PlaidXL이 자동으로 선택합니다.
4. Excel에서 팝업 창을 허용할지 묻습니다. 허용합니다.
5. 팝업에서 평소 사용하는 방식으로 로그인합니다.
   - **PlaidCloud 로그인** — 이메일, 암호 및 설정해 둔 2단계 인증 코드를 입력합니다.
   - **SSO(Single Sign-On)** — 이미 조직에 로그인되어 있다면 이 단계는 바로 통과합니다. 그렇지 않으면 조직의 로그인 페이지가 먼저 열립니다.
6. 팝업에 **Authenticated successfully**가 표시되면 저절로 닫히지 않은 경우 직접 닫습니다.

이제 작업 창에 **Connected to** 뒤에 워크스페이스 ID가, **as** 뒤에 사용자 이름이 표시되고 그 아래에 프로젝트가 나열됩니다. 계속해서 [테이블 및 차원 사용](/ko/reference/cli/plaidxl/retrieve/)을 진행합니다.

계정에 2단계 인증이나 SSO를 설정하려면 [멤버 인증](/ko/administration/access/member-authentication/)을 참조하십시오.

## 로그인 상태 유지

PlaidXL은 이 컴퓨터에서 로그인 상태를 유지하며 작업하는 동안 백그라운드에서 로그인을 갱신합니다. 이후 세션에서 작업 창을 열면 바로 프로젝트로 이동합니다. 로그인이 완전히 만료된 경우 PlaidXL이 이메일을 다시 요청합니다.

## 표시되는 항목

PlaidXL은 사용자의 권한으로 데이터를 읽습니다. PlaidCloud에서 열 수 있는 프로젝트와 그 안의 테이블 및 차원만 표시되며 그 외에는 표시되지 않습니다. 프로젝트나 테이블이 보이지 않으면 프로젝트 소유자에게 액세스 권한을 요청하십시오. 워크스페이스 멤버십의 작동 방식은 [조직과 워크스페이스 이해하기](/ko/administration/access/overview/organizations-and-workspaces-explained/)를 참조하십시오.

## 로그아웃 또는 워크스페이스 전환

작업 창 상단의 **Logout**을 클릭합니다. PlaidXL이 로그인 정보를 지우고 이메일 화면으로 돌아갑니다.

다른 워크스페이스에서 작업하려면 로그아웃한 다음 다시 로그인하고 **Select a tenant**에서 다른 워크스페이스를 선택합니다. PlaidXL은 열려 있는 모든 통합 문서에 대해 한 번에 하나의 워크스페이스만 사용합니다.

## 밝은 테마와 어두운 테마

작업 창은 Office 테마를 따릅니다. 밝은 테마나 어두운 테마로 고정하려면 작업 창 왼쪽 위의 해 또는 달 단추를 클릭합니다.

## 관련 항목

- [PlaidXL 설치](/ko/reference/cli/plaidxl/install/) — 추가 기능을 추가하고 작업 창 열기
- [문제 해결](/ko/reference/cli/plaidxl/troubleshooting/) — 로그인 팝업이 열리지 않거나 워크스페이스가 보이지 않을 때
- [워크스페이스 보기 및 관리](/ko/administration/access/overview/viewing-and-managing-workspaces/) — 사용자가 속한 워크스페이스
