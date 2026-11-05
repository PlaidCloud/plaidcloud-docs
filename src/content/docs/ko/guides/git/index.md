---
title: PlaidCloud Git
description: PlaidCloud 안에서 Git 리포지토리를 호스팅하고 버전 관리하며 협업합니다. 이슈, 풀 리퀘스트, 프로젝트 보드, 릴리스, 위키를 제공하며 싱글 사인온이 기본으로 내장되어 있습니다.
sidebar:
  label: 개요
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git은 워크스페이스에 내장된 비공개 Git 서비스입니다. 각 워크스페이스에는 코드, 구성, 노트북 및 기타 버전 관리 파일을 저장하는 전용 Git 서버가 있으며, 팀이 이를 두고 협업하는 데 사용하는 이슈, 풀 리퀘스트, 프로젝트 보드도 함께 제공됩니다.

PlaidCloud 계정으로 로그인하므로 별도의 사용자 이름이나 비밀번호를 설정할 필요가 없습니다. 새 리포지토리는 기본적으로 비공개이며, 액세스 권한을 부여한 멤버에게만 표시됩니다.

## Git 열기

워크스페이스의 앱 목록에서 **Git**을 선택합니다. **Git** 탭에는 워크스페이스의 리포지토리가 이름, 설명, 기본 브랜치, 마지막 업데이트 시점과 함께 표시되며, 맨 위의 한 줄에 수행할 수 있는 작업이 안내됩니다. 리포지토리를 선택하면 열리고, **View all in Git**을 선택하면 Git 웹 인터페이스로 이동합니다. PlaidCloud로 돌아가려면 Git에서 워크스페이스의 **← Back to**를 사용합니다.

리포지토리를 클론하려면 해당 행에서 **Copy clone URL**을 선택합니다. 처음에는 필요한 사항을 알려 주는 힌트가 표시됩니다.

1. 컴퓨터에 Git이 설치되어 있어야 합니다.
2. Git의 **설정 → 애플리케이션**에서 **write:repository** 권한이 있는 액세스 토큰을 만듭니다. 힌트에 해당 페이지로 이동하는 링크가 있습니다.
3. Git이 비밀번호를 요청하면 PlaidCloud 비밀번호가 아니라 토큰을 붙여 넣습니다.
4. 표시된 `git config --global user.name` 및 `user.email` 명령 두 개를 실행합니다. 이 명령에는 이미 내 이름과 이메일이 들어 있습니다.

전체 안내는 [리포지토리](/ko/guides/git/repositories/)를 참조하십시오. 클론 URL을 복사할 수 없다면 읽기 액세스만 있는 것입니다. 아래를 참조하십시오.

## 액세스 수준

Git 액세스 권한이 있는 모든 멤버는 워크스페이스의 공유 리포지토리를 읽을 수 있습니다. 푸시할 수 있는 수준은 두 가지가 더 있습니다.

| 수준 | 할 수 있는 작업 | 부여 주체 |
|---|---|---|
| **읽기** | 공유 리포지토리를 보고 클론합니다. | 모든 멤버에게 기본으로 부여됩니다. |
| **Contributor** | 읽기의 모든 작업과 함께, [Panel](/ko/guides/panel-apps/deploy-from-git/) 및 [Dash](/ko/guides/dash-apps/deploy-from-git/) 앱 코드가 있는 `apps` 리포지토리에 푸시합니다. | **Git Contributors** 보안 그룹입니다. |
| **관리자** | Contributor의 모든 작업과 함께, `udfs`를 포함한 모든 리포지토리에 푸시하고 조직을 만듭니다. | **Git Administration** 보안 그룹입니다. |

`udfs` 리포지토리는 사용자 정의 함수가 이를 호출하는 워크플로의 ID로 실행되기 때문에 관리자만 사용할 수 있습니다.

읽기 액세스만 있는 경우 **Git** 탭에 **Git Contributors**에 추가해 달라고 요청할 수 있는 워크스페이스 관리자가 최대 세 명까지 표시됩니다.

## 앱 및 UDF에서 Git 사용

Panel 또는 Dash 앱 창에는 리포지토리, 브랜치, 빌드 상태를 보여 주는 **리포지토리** 섹션이 있으며, 푸시할 수 있는 멤버에게는 **Edit in browser**와 **Copy clone URL**이 표시됩니다. Git 기반 UDF의 도구 모음에는 **Open**이 있어 해당 브랜치의 리포지토리를 Git에서 열고, 관리자에게는 **Edit in browser**도 있습니다.

## Git 액세스 권한 부여

워크스페이스 관리자는 **ID**에서 멤버를 보안 그룹에 추가하거나 직접 만든 그룹에 권한을 추가하는 방식으로 액세스 권한을 부여합니다.

1. 앱 코드를 푸시할 수 있게 하려면 멤버를 **Git Contributors**에 추가하고, Git 관리자로 지정하려면 **Git Administration**에 추가합니다.
2. 모든 신규 멤버에게 앱 코드 푸시 권한을 주려면 **Git Contributors**를 기본 그룹에 추가합니다. **Git Administration**은 기본 그룹으로 지정할 수 없습니다.
3. 멤버가 할 수 있는 작업을 확인하려면 해당 멤버를 열고 **Git** 탭을 선택합니다. 멤버의 Git 사용자 이름, 수준, 그 수준을 부여하는 그룹이 표시됩니다.

변경 사항은 멤버가 다음에 Git에 로그인하거나 **Git** 탭을 열 때 적용됩니다. PlaidCloud 지원 담당자는 자동으로 관리자 액세스 권한을 갖습니다.

## 이 섹션의 내용

- [리포지토리](/ko/guides/git/repositories/) — 리포지토리를 만든 다음 작업을 클론, 커밋, 푸시합니다
- [이슈](/ko/guides/git/issues/) — 레이블, 마일스톤, 담당자로 작업, 버그, 아이디어를 추적합니다
- [풀 리퀘스트](/ko/guides/git/pull-requests/) — 브랜치에서 변경 사항을 제안하고 병합하기 전에 검토합니다
- [프로젝트 보드](/ko/guides/git/projects/) — 칸반 보드에서 이슈와 풀 리퀘스트를 정리합니다
- [릴리스 및 태그](/ko/guides/git/releases-and-tags/) — 리포지토리의 버전별 스냅샷을 표시하고 게시합니다
- [위키](/ko/guides/git/wikis/) — 긴 분량의 문서를 코드 옆에 보관합니다
- [패키지](/ko/guides/git/packages/) — 리포지토리 레지스트리에서 빌드 아티팩트를 게시하고 설치합니다
- [코드 검색](/ko/guides/git/searching-code/) — 리포지토리 전반에서 코드, 이슈, 풀 리퀘스트를 찾습니다

## 관련 항목

- [PlaidCloud Git에서 Panel 앱 배포하기](/ko/guides/panel-apps/deploy-from-git/) — 자격 증명이 필요 없는 관리형 연결로 HoloViz Panel 앱을 리포지토리에서 바로 서비스합니다
- [PlaidCloud Git에서 Dash 앱 배포하기](/ko/guides/dash-apps/deploy-from-git/) — Plotly Dash 앱을 같은 방식으로 서비스합니다
- [액세스 관리](/ko/administration/access/) — 워크스페이스 멤버십과 보안 그룹이 리포지토리를 볼 수 있는 사람과 편집할 수 있는 사람을 어떻게 결정하는지 설명합니다
