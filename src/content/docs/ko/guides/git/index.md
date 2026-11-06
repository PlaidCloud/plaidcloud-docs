---
title: PlaidCloud Git
description: PlaidCloud 안에서 Git 리포지토리를 호스팅하고, 버전을 관리하고, 협업합니다. 이슈, 풀 리퀘스트, 프로젝트 보드, 릴리스, 위키를 제공하며 싱글 사인온이 기본으로 내장되어 있습니다.
sidebar:
  label: 개요
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git은 워크스페이스에 내장된 비공개 Git 서비스입니다. 각 워크스페이스에는 코드, 구성, 노트북, 그 밖의 버전 관리 파일을 저장하는 전용 Git 서버가 제공되며, 팀이 이를 협업에 활용할 수 있는 이슈, 풀 리퀘스트, 프로젝트 보드도 함께 제공됩니다.

PlaidCloud 계정으로 로그인하므로 별도의 사용자 이름이나 비밀번호를 설정할 필요가 없습니다. 새 리포지토리는 기본적으로 비공개이며, 액세스 권한을 부여한 멤버에게만 표시됩니다.

## Git 열기

워크스페이스의 앱 목록에서 **Git**을 선택합니다. **Git** 탭이 열리고 워크스페이스의 호스트, 내 역할, **Repositories** 목록이 표시됩니다. **View all in Git**을 사용하면 Git 웹 인터페이스로 이동하고, **Manage who can push**(그룹을 관리할 수 있는 경우)를 사용하면 그룹 관리가 열리며, 새로 고침 버튼은 목록을 다시 불러옵니다. PlaidCloud로 돌아오려면 **← Back to** your workspace in Git을 사용하십시오.

역할 표시기에는 내 수준이 **Administrator**, **Contributor**, **뷰어** 중 하나로 표시되고, 그 수준에서 할 수 있는 일에 대한 설명이 함께 나타납니다. 각 리포지토리 행에는 이름, 설명(있는 경우), 날짜가 포함된 **업데이트됨**, 복사 버튼이 있는 읽기 전용 클론 필드, 그리고 Git에서 리포지토리를 여는 **열기**가 표시됩니다. 비공개로 만든 리포지토리는 이 목록이 아니라 Git에서 직접 확인할 수 있습니다.

워크스페이스에 Git이 설정되어 있지 않거나 Git에 연결할 수 없으면 **Git** 탭에 이유와 함께 **Git을 사용할 수 없음**이 표시되며, **다시 시도**를 선택하면 다시 확인합니다.

## 리포지토리 클론하기

해당 행에서 리포지토리의 클론 주소를 복사합니다. 처음 복사하면 아래 단계가 담긴 **Set up Git on your computer** 카드가 나타납니다. **닫기**를 선택하면 카드가 숨겨지며, 머리글의 **How to clone**을 선택하면 다시 표시됩니다.

1. 컴퓨터에 Git이 설치되어 있어야 합니다.
2. **설정 → 애플리케이션**에서 **write:repository** 권한이 있는 토큰을 만듭니다. 카드에 해당 페이지로 가는 링크가 있습니다.
3. 표시된 두 개의 `git config --global user.name` 및 `user.email` 명령으로 Git에 내가 누구인지 알려 줍니다. 이 명령에는 이미 내 이름과 이메일이 들어 있습니다.
4. 표시된 `git clone` 명령으로 리포지토리를 클론합니다. Git이 비밀번호를 물으면 PlaidCloud 비밀번호가 아니라 해당 토큰을 붙여 넣습니다.

각 명령에는 고유한 복사 버튼이 있습니다. 전체 과정은 [리포지토리](/ko/guides/git/repositories/)를 참조하십시오. 복사하려면 푸시 액세스와 활성화된 Git 계정이 필요합니다. 복사 버튼이 비활성화되어 있으면 아무 리포지토리나 한 번 열어 계정을 활성화하거나, **뷰어**인 경우 아래 설명대로 푸시 액세스를 요청하십시오.

## 액세스 수준

Git에 액세스할 수 있는 모든 사용자는 워크스페이스의 공유 리포지토리를 읽을 수 있습니다. 푸시할 수 있는 수준은 두 가지가 더 있습니다.

| 역할 | 할 수 있는 작업 | 부여 방법 |
|---|---|---|
| **뷰어** | 공유 리포지토리를 보고 클론합니다. | 모든 멤버에게 기본으로 부여됩니다. |
| **Contributor** | 읽기 수준의 모든 작업을 할 수 있고, [Panel](/ko/guides/panel-apps/deploy-from-git/) 및 [Dash](/ko/guides/dash-apps/deploy-from-git/) 앱 코드가 있는 `apps` 리포지토리에 푸시할 수 있습니다. | **Git Contributors** 보안 그룹입니다. |
| **Administrator** | Contributor의 모든 작업을 할 수 있고, `udfs`를 포함한 모든 리포지토리에 푸시하며 조직을 만들 수 있습니다. | **Git Administration** 보안 그룹입니다. |

사용자 정의 함수는 이를 호출하는 워크플로의 ID로 실행되므로 `udfs` 리포지토리는 관리자만 사용할 수 있습니다.

**뷰어**인 경우 **Git** 탭에 **Git Contributors**에 추가해 달라고 요청할 수 있는 워크스페이스 관리자가 최대 세 명까지 표시됩니다.

## 앱과 UDF에서 Git 사용하기

Panel 또는 Dash 앱 창에는 리포지토리, 브랜치, 빌드 상태를 보여 주는 **Repository** 섹션이 있으며, 푸시할 수 있는 멤버에게는 **Edit in browser**와 **Copy clone URL**이 표시됩니다. Git 기반 UDF의 도구 모음에는 Git에서 해당 브랜치의 리포지토리를 여는 **열기**가 있고, 관리자에게는 **Edit in browser**가 표시됩니다.

## Git 액세스 권한 부여하기

워크스페이스 관리자는 **ID**에서 멤버를 보안 그룹에 추가하거나 직접 만든 그룹에 권한을 추가하여 액세스 권한을 부여합니다.

1. 앱 코드를 푸시할 수 있게 하려면 멤버를 **Git Contributors**에 추가하고, Git 관리자로 지정하려면 **Git Administration**에 추가합니다.
2. 모든 신규 멤버에게 앱 코드 푸시 권한을 부여하려면 **Git Contributors**를 기본 그룹에 추가합니다. **Git Administration**은 기본 그룹으로 지정할 수 없습니다.
3. 멤버가 할 수 있는 작업을 확인하려면 해당 멤버를 열고 **Git** 탭을 선택합니다. 멤버의 Git 사용자 이름, 수준, 그리고 그 수준을 부여하는 그룹이 표시됩니다.

변경 사항은 멤버가 다음에 Git에 로그인하거나 **Git** 탭을 열 때 적용됩니다. PlaidCloud 지원 담당자에게는 Administrator 액세스가 자동으로 부여됩니다.

## 이 섹션의 내용

- [리포지토리](/ko/guides/git/repositories/) — 리포지토리를 만든 다음 작업을 클론, 커밋, 푸시합니다.
- [이슈](/ko/guides/git/issues/) — 레이블, 마일스톤, 담당자로 작업, 버그, 아이디어를 추적합니다.
- [풀 리퀘스트](/ko/guides/git/pull-requests/) — 브랜치에서 변경 사항을 제안하고 병합하기 전에 검토합니다.
- [프로젝트 보드](/ko/guides/git/projects/) — 이슈와 풀 리퀘스트를 칸반 보드에서 정리합니다.
- [릴리스와 태그](/ko/guides/git/releases-and-tags/) — 리포지토리의 버전 스냅샷을 표시하고 게시합니다.
- [위키](/ko/guides/git/wikis/) — 긴 형식의 문서를 코드 옆에 보관합니다.
- [패키지](/ko/guides/git/packages/) — 리포지토리 레지스트리에서 빌드 아티팩트를 게시하고 설치합니다.
- [코드 검색](/ko/guides/git/searching-code/) — 리포지토리 전체에서 코드, 이슈, 풀 리퀘스트를 찾습니다.

## 관련 문서

- [PlaidCloud Git에서 Panel 앱 배포하기](/ko/guides/panel-apps/deploy-from-git/) — 자격 증명이 필요 없는 관리형 연결로 HoloViz Panel 앱을 리포지토리에서 바로 서비스합니다.
- [PlaidCloud Git에서 Dash 앱 배포하기](/ko/guides/dash-apps/deploy-from-git/) — Plotly Dash 앱을 같은 방식으로 서비스합니다.
- [액세스 관리](/ko/administration/access/) — 워크스페이스 멤버십과 보안 그룹이 리포지토리를 보고 편집할 수 있는 사용자를 어떻게 결정하는지 설명합니다.
