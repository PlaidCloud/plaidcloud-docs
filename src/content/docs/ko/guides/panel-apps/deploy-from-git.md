---
title: PlaidCloud Git에서 Panel 앱 배포하기
description: HoloViz Panel 앱을 PlaidCloud에서 서비스하기 위한 전체 경로입니다. 코드를 PlaidCloud Git 리포지토리에 넣고, 자격 증명이 필요 없는 관리형 연결로 연결한 다음, 게시하여 라이브로 전환합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

내 컴퓨터에 있는 Panel 앱 코드를 라이브 URL로 만드는 전체 경로입니다. 워크스페이스에 내장된 관리형 Git 서비스인 **[PlaidCloud Git](/ko/guides/git/)** 을 소스로 사용합니다. PlaidCloud Git은 관리형이므로 앱을 배포하는 연결에는 **서버 URL, 사용자 이름, 토큰이 필요 없습니다**. PlaidCloud가 대신 인증합니다.

다음 다섯 단계로 진행합니다.

1. 최소한의 Panel 앱을 작성합니다.
2. 앱을 PlaidCloud Git 리포지토리에 넣습니다.
3. 관리형 PlaidCloud Git 연결을 만듭니다.
4. 리포지토리를 가리키는 서버 앱을 게시합니다.
5. 서비스 중인 앱을 열고, 시작되지 않으면 빌드 로그를 확인합니다.

각 단계에는 해당 부분을 더 자세히 다루는 안내 링크가 있으며, 이 페이지는 그 내용을 하나의 경로로 엮은 것입니다.

## 시작하기 전에

- 워크스페이스에서 **Git**을 열어 PlaidCloud Git에 접근할 수 있는지 확인합니다. 기본적으로 워크스페이스의 조직에는 **`apps`** 리포지토리(그리고 **`udfs`** 리포지토리)가 포함되어 있으며, Panel 앱을 두기에 적합합니다.
- 내 컴퓨터에서 코드를 푸시하려면 `git`이 로컬에 설치되어 있어야 합니다. Git 웹 UI에서 파일을 추가할 수도 있습니다.

## 1. 최소한의 Panel 앱 작성

앱에는 Panel 앱을 만들고 `.servable()`로 표시하는 Python 파일인 **진입점**이 필요합니다. 추가 패키지가 필요하면 리포지토리 루트나 진입점 옆에 **`requirements.txt`** 를 둘 수 있습니다(선택 사항).

```
apps/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

`app.py`를 만듭니다.

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello from PlaidCloud Git 👋\n\nServed straight from your workspace repository.").servable()
```

이것으로 완전한 앱입니다. PlaidCloud가 서비스하는 것은 `.servable()` 호출입니다. `panel`, `bokeh`와 PlaidCloud 클라이언트 라이브러리(`plaidcloud-rpc`, `plaidcloud-utilities`)는 미리 설치되어 있으므로 `requirements.txt`에는 *추가* 패키지만 나열하십시오. 더 풍부한 예제, 종속성, 라이트/다크 테마는 [Panel 앱 만들기](/ko/guides/panel-apps/creating/)를 참조하십시오.

## 2. 앱을 PlaidCloud Git 리포지토리에 넣기

워크스페이스의 기존 **`apps`** 리포지토리를 사용하거나 [새 리포지토리를 만듭니다](/ko/guides/git/repositories/#리포지토리-만들기). 그런 다음 코드를 리포지토리에 넣습니다.

PlaidCloud를 통해 로그인하므로 Git 계정에는 별도의 비밀번호가 없습니다. **write:repository** 권한이 있는 [개인 액세스 토큰을 생성](/ko/guides/git/repositories/#개인-액세스-토큰-생성)하고(**내 아바타 → 설정 → 애플리케이션**), Git이 비밀번호를 요청할 때 그 토큰을 입력하십시오. `apps`에 푸시하려면 **Contributor** 액세스가 필요합니다. **Git** 탭에 읽기 액세스만 있다고 표시되면 워크스페이스 관리자에게 **Git Contributors**에 추가해 달라고 요청하십시오. **Git** 탭에서 리포지토리의 **Copy clone URL**을 선택한 다음 다음을 실행합니다.

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

리포지토리 경로 `<org>/apps`를 기록해 두십시오. 여기서 `<org>`는 워크스페이스의 조직 이름입니다. 이 경로는 다음 단계에서 입력합니다. 클론, 커밋, 푸시에 대한 자세한 내용은 [리포지토리](/ko/guides/git/repositories/)를 참조하십시오.

> **여기서 사용하는 토큰은 *사용자가* 코드를 푸시할 때만 쓰입니다.** 다음에 만들 연결은 관리형이므로 토큰이 필요 없습니다. 두 가지를 혼동하지 마십시오.

## 3. 관리형 PlaidCloud Git 연결 만들기

**연결**은 Panel 배포가 코드를 가져올 위치를 알려 줍니다. PlaidCloud Git의 연결은 *관리형*입니다. PlaidCloud가 호스트와 자격 증명을 제공하므로 리포지토리 대상만 입력하면 됩니다.

1. **Tools > Connections**를 열고 **새 연결**을 클릭한 다음 **PlaidCloud Git**을 선택합니다.
2. 연결에 **계정 이름**을 지정합니다(예: `Apps Repo`).
3. **Repository Path**를 2단계에서 기록해 둔 경로인 `<org>/apps`로 설정하고 **기본 브랜치**를 `main`으로 설정합니다. 앱이 하위 디렉터리에 있지 않다면 **시작 경로**는 비워 둡니다.
4. **만들기**를 클릭합니다.

서버 URL, 사용자, 비밀번호, SSL/SSH 필드는 없습니다. PlaidCloud Git은 관리형이므로 플랫폼이 호스트와 인증을 처리합니다. 연결의 **사용법**과 **보안 모델**(워크스페이스에서 누가 사용할 수 있는지)을 포함한 전체 양식은 [PlaidCloud Git 연결](/ko/guides/connections/plaidcloud-git/)을 참조하십시오.

> **이전 워크스페이스 빌드를 사용 중인가요?** 양식에 서버 URL이나 자격 증명 필드가 아직 표시되더라도 비워 두면 됩니다. 어느 경우든 플랫폼이 대신 인증합니다.

## 4. 서버 앱 게시

이제 서버 배포가 그 연결을 가리키도록 설정합니다.

1. **내 Panel 앱**을 열고 **새 서버 앱**을 클릭합니다.
2. **디렉터리 설정**에서 **앱 이름**과 **URL 슬러그**를 설정합니다. 슬러그는 앱의 URL이자 내부 이름이므로 소문자, 숫자, 하이픈을 사용하고 문자로 시작하며 40자 이하로 지정합니다(예: `hello-panel`).
3. **Git 연결 및 게시 감시기**에서 다음을 설정합니다.
   - **Git 연결** — 3단계에서 만든 PlaidCloud Git 연결입니다.
   - **브랜치** — `main`입니다. 이 브랜치에 푸시하면 앱이 자동으로 다시 빌드되고 재배포됩니다.
   - **진입점** — `app.py`입니다.
4. **런타임**에서 **CPU**, **메모리**, **디자인**(PlaidCloud의 최신 디자인을 사용하려면 **FAST**), **유휴 시간(분)** 창을 선택합니다. 로그인 없이 앱에 접근할 수 있어야 하는 경우에만 **공개 액세스 허용**을 선택합니다.
5. **게시**를 클릭합니다.

이 대화 상자의 모든 필드는 [Panel 앱 만들기](/ko/guides/panel-apps/creating/#앱-게시)에 설명되어 있습니다.

## 5. 앱 열기 및 시작되지 않을 때 로그 확인

게시하면 앱이 **빌드**됩니다. PlaidCloud가 브랜치를 클론하고, `requirements.txt`(리포지토리 루트와 앱 폴더에 있는 경우 둘 다)를 설치하고, 컨테이너 이미지를 빌드합니다. **상태**는 **내 Panel 앱** 목록에 표시되며 자동으로 업데이트됩니다.

- 상태가 **준비됨**이 되면 `https://<your-tenant-host>/serve/<slug>/`에서 앱을 엽니다. 유휴 상태 이후의 첫 요청이 앱을 시작시키며, 약 15초가 걸립니다.
- 빌드에 실패하면 앱을 열고 **빌드** 로그를 확인하십시오. 누락된 종속성이나 가져오기 오류가 여기에 나타납니다. 각 상태의 의미, 로그를 읽는 방법, 다시 빌드하는 방법은 [Panel 앱 사용](/ko/guides/panel-apps/using/)을 참조하십시오.

이후에는 **연결된 브랜치에 푸시할 때마다 앱이 자동으로 다시 빌드되고 재배포됩니다**. `app.py`를 편집하고 `git push`하면 변경 사항이 라이브로 반영됩니다. (단, 앱이 **잠겨** 있으면 잠금을 해제할 때까지 푸시가 건너뛰어집니다. [앱 잠금](/ko/guides/panel-apps/using/#앱-잠그기)을 참조하십시오.)

## 다음 단계

- [Panel 앱 만들기](/ko/guides/panel-apps/creating/) — 더 풍부한 예제, 종속성, 라이트/다크 테마를 다룹니다
- [PlaidCloud Git 연결](/ko/guides/connections/plaidcloud-git/) — 전체 연결 양식, 사용법, 보안 모델을 다룹니다
- [데이터와 로그인한 사용자 읽기](/ko/guides/panel-apps/accessing-data/) — 앱을 보는 사람의 권한으로 PlaidCloud 데이터를 쿼리합니다
- [리포지토리](/ko/guides/git/repositories/) — PlaidCloud Git의 브랜치, 토큰, 협업을 다룹니다
