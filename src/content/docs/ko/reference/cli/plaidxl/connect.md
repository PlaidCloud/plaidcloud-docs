---
title: PlaidXL에 로그인
description: 이메일과 평소 사용하는 로그인 방식(SSO 및 2단계 인증 포함)으로 PlaidXL을 PlaidCloud 워크스페이스에 연결하고, 로그아웃하거나 워크스페이스를 전환합니다.
sidebar:
  label: 로그인
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL은 브라우저에서 PlaidCloud에 사용하는 것과 동일한 로그인으로 사용자 본인 자격으로 로그인합니다. 입력해야 할 서버 주소도 없고, 통합 문서에 저장되는 비밀번호도 없습니다.

## 로그인

1. 작업 창을 엽니다. **PlaidCloud → Open PlaidXL**을 클릭하거나, **연결** 그룹에서 **계정**을 클릭합니다.
2. **Enter your email** 아래에 PlaidCloud에 사용하는 이메일 주소를 입력하고 **로그인**을 클릭합니다. PlaidXL이 다음에 사용할 수 있도록 주소를 기억합니다.
3. 이메일이 둘 이상의 워크스페이스에 속해 있다면 **Select a workspace**에서 하나를 선택하고 **로그인**을 클릭합니다. PlaidXL이 선택을 기억합니다. 하나의 워크스페이스에만 속해 있으면 PlaidXL이 자동으로 선택합니다. 이메일에 연결된 워크스페이스가 없으면 창에 해당 안내가 표시됩니다. 주소를 확인하고 다시 시도하십시오.
4. Excel이 팝업 창을 허용할지 묻습니다. 허용합니다.
5. 팝업에서 평소 방식으로 로그인합니다.
   - **PlaidCloud sign-in** — 이메일, 비밀번호, 그리고 설정해 둔 2단계 인증 코드입니다.
   - **Single sign-on** — 이미 조직에 로그인되어 있다면 이 단계는 바로 통과됩니다. 그렇지 않으면 먼저 조직의 로그인 페이지가 열립니다.
6. 팝업에 **Authenticated successfully**가 표시되면 스스로 닫히지 않은 경우 닫습니다.

이제 작업 창 머리글에 워크스페이스와 통합 문서에 연결된 프로젝트가 표시되고, 그 옆에 계정 메뉴가 나타납니다. [테이블과 차원 작업](/ko/reference/cli/plaidxl/retrieve/)으로 계속 진행하십시오.

계정에 2단계 인증이나 SSO를 설정하려면 [멤버 인증](/ko/administration/access/member-authentication/)을 참조하십시오.

### Office 계정으로 로그인

Microsoft Entra ID의 업무용 계정으로 Office에 로그인되어 있고 PlaidXL에 저장된 로그인이 없으면, PlaidXL이 해당 계정에서 워크스페이스를 찾으므로 이메일을 입력하지 않아도 됩니다.

- **워크스페이스가 하나인 경우** — PlaidXL이 해당 워크스페이스로 로그인을 시작합니다. Excel이 요청하면 팝업을 허용하십시오. SSO를 사용하면 바로 통과됩니다. 웹용 Excel에서는 먼저 **Continue as** 다음의 계정을 클릭합니다.
- **워크스페이스가 여러 개인 경우** — **Select a workspace**에서 하나를 선택합니다. 통합 문서에서 마지막으로 사용한 워크스페이스가 이미 선택되어 있습니다.
- **워크스페이스가 없는 경우** — 주소가 미리 입력된 이메일 화면이 열립니다.

Office 계정과 다른 이메일로 로그인하면 PlaidXL이 어느 계정인지 알려 줍니다. **Log out** 후에는 PlaidXL이 사용자가 직접 로그인하기를 기다립니다.

### 로그인하기 전의 명령

로그인하기 전에도 리본에서 PlaidXL 명령을 클릭할 수 있습니다. PlaidXL이 작업 창을 열어 로그인하거나 프로젝트를 선택하도록 안내한 다음, 시작한 셀에서 해당 명령을 실행합니다.

## 로그인 상태 유지

PlaidXL은 이 컴퓨터에서 로그인 상태를 유지하고, 작업하는 동안 백그라운드에서 로그인을 갱신합니다. 이후 세션에서 작업 창을 열면 바로 프로젝트로 이동합니다. 로그인이 완전히 만료되었다면 PlaidXL이 이메일을 다시 요청합니다. 로그인을 갱신하는 중에 일시적인 네트워크 문제가 생겨도 로그아웃되지 않으며 PlaidXL이 다시 시도합니다.

## 볼 수 있는 항목

PlaidXL은 사용자의 권한으로 읽습니다. PlaidCloud에서 열 수 있는 프로젝트와 그 안의 테이블 및 차원만 표시되며 그 이상은 표시되지 않습니다. 프로젝트나 테이블이 보이지 않으면 프로젝트 소유자에게 액세스를 요청하십시오. 워크스페이스 멤버십의 작동 방식은 [조직과 워크스페이스 이해](/ko/administration/access/overview/organizations-and-workspaces-explained/)를 참조하십시오.

## 로그아웃 또는 워크스페이스 전환

작업 창 오른쪽 위의 계정 메뉴(점 세 개)를 클릭합니다. 이름과 워크스페이스가 표시되며 세 가지 명령이 있습니다.

- **Keyboard shortcuts**는 PlaidXL 단축키를 나열하며 변경할 수 있습니다. [키보드 단축키](/ko/reference/cli/plaidxl/ribbon/#키보드-단축키)를 참조하십시오.
- **Switch workspace**는 로그아웃하고 이메일 화면으로 돌아가므로 **Select a workspace**에서 다른 워크스페이스를 선택할 수 있습니다.
- **Log out**은 로그인을 지우고 이메일 화면으로 돌아갑니다.

로그인은 열려 있는 모든 통합 문서에서 공유되지만, 각 통합 문서는 자체 프로젝트를 유지합니다. 통합 문서의 프로젝트는 하나의 워크스페이스에 속하므로, 전환한 뒤에는 이전 워크스페이스의 프로젝트에 연결된 통합 문서에 프로젝트를 다시 선택하기 전까지 프로젝트가 없습니다. [프로젝트는 통합 문서에 속합니다](/ko/reference/cli/plaidxl/retrieve/#프로젝트는-통합-문서에-속합니다)를 참조하십시오.

## 밝은 테마와 어두운 테마

작업 창은 Office 테마를 따르며, 테마를 변경하면 함께 바뀝니다.

## 키보드와 화면 읽기 프로그램

프로젝트, 테이블, 차원 목록의 행은 키보드 포커스를 받고 **Enter**와 **Space**에 반응합니다. 선택한 행은 화면 읽기 프로그램이 읽어 주며, 선택 상태와 경고 상태는 색상뿐 아니라 아이콘으로도 표시됩니다.

## 관련 항목

- [PlaidXL 설치](/ko/reference/cli/plaidxl/install/) — 추가 기능을 추가하고 작업 창을 엽니다
- [문제 해결](/ko/reference/cli/plaidxl/troubleshooting/) — 로그인 팝업이 열리지 않거나 워크스페이스가 보이지 않을 때
- [워크스페이스 보기 및 관리](/ko/administration/access/overview/viewing-and-managing-workspaces/) — 속해 있는 워크스페이스
