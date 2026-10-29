---
title: PlaidCloud Git 커넥터
description: 서버 URL이나 자격 증명을 구성하지 않고 Panel 앱, Dash 앱 또는 워크플로를 관리형 내장 Git 서비스인 PlaidCloud Git의 리포지토리에 연결합니다.
sidebar:
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/git/plaidcloud-git.md
---

**PlaidCloud Git**은 워크스페이스에 기본 제공되는 관리형 Git 서비스입니다. PlaidCloud Git 연결은 Panel 또는 Dash 배포나 워크플로가 사용자의 리포지토리 중 하나를 가리키도록 합니다. 관리형 서비스이므로 **서버 URL, 사용자 이름, 토큰이 필요하지 않습니다**. PlaidCloud가 호스트를 제공하고 사용자를 대신하여 인증합니다.

이러한 연결에서 앱을 제공하는 전체 과정은 [PlaidCloud Git에서 Panel 앱 배포](/ko/guides/panel-apps/deploy-from-git/) 또는 [PlaidCloud Git에서 Dash 앱 배포](/ko/guides/dash-apps/deploy-from-git/)를 참조하십시오. 리포지토리를 만들고 코드를 푸시하려면 [PlaidCloud Git 가이드](/ko/guides/git/)를 참조하십시오.

## 구성

**Tools > Connections**에서 **새 연결**을 클릭하고 **PlaidCloud Git**을 선택합니다. 이 양식에는 외부 Git 제공자가 표시하는 인증, SSL, SSH 섹션이 없습니다. 자격 증명은 플랫폼에서 가져오기 때문에, 연결의 식별 정보, 사용 방식, 리포지토리 대상만 남습니다.

### 식별 정보

| 필드 | 유형 | 설명 |
|---|---|---|
| 계정 이름 | 텍스트 | 이 연결의 표시 이름입니다. |
| 메모 | 텍스트 | 연결의 용도에 대한 선택적 메모입니다. |

### 리포지토리

| 필드 | 유형 | 설명 |
|---|---|---|
| 리포지토리 | 선택기 | 사용할 리포지토리입니다. **새로 고침**을 클릭하면 워크스페이스 리포지토리(예: `apps` 또는 `udfs`)가 나열되며, 그중 하나를 선택합니다. |
| 기본 브랜치 | 선택기 | 읽어 올 브랜치이며, 선택한 리포지토리의 브랜치 중에서 고릅니다. |
| 시작 경로 | 선택기 | 선택 사항입니다. 선택한 리포지토리를 탐색하여 폴더를 선택하면 모든 파일 조회가 하위 디렉터리로 한정됩니다. |

**사용법**(`Active` / `Read Only`)과 **보안 모델**(워크스페이스에서 누가 연결을 사용할 수 있는지)은 표준 연결 설정입니다. [연결 가이드](/ko/guides/connections/plaidcloud-git/)와 [연결 만들기 및 관리](/ko/guides/connections/create-connection/)를 참조하십시오.

## 일반적인 용도

- 워크스페이스의 `apps` 리포지토리에서 [HoloViz Panel 앱](/ko/guides/panel-apps/deploy-from-git/) 또는 [Plotly Dash 앱](/ko/guides/dash-apps/deploy-from-git/)을 제공합니다.
- PlaidCloud Git에 있는 사용자 정의 함수, 구성 또는 템플릿 파일을 소스로 사용합니다.

## 관련 항목

- [PlaidCloud Git 연결](/ko/guides/connections/plaidcloud-git/) — 사용법과 보안 모델을 포함해 연결을 만드는 작업 가이드
- [PlaidCloud Git에서 Panel 앱 배포](/ko/guides/panel-apps/deploy-from-git/) — 리포지토리에서 제공되는 앱까지의 전체 경로
- [PlaidCloud Git에서 Dash 앱 배포](/ko/guides/dash-apps/deploy-from-git/) — Plotly Dash 앱을 위한 동일한 경로
- [PlaidCloud Git 가이드](/ko/guides/git/) — 리포지토리, 이슈, 풀 리퀘스트 등
- [Git 리포지토리 연결](/ko/reference/connectors/git/) — 외부 Git 제공자(GitHub, GitLab 등)
