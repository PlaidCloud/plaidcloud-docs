---
title: PlaidCloud Git에서 Panel 앱 배포
description: PlaidCloud에서 HoloViz Panel 앱을 제공하는 전체 과정입니다. 코드를 PlaidCloud Git 리포지토리에 올리고, 자격 증명이 필요 없는 관리형 연결로 연결한 다음 라이브로 게시합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

이 문서는 컴퓨터에 있는 Panel 앱 코드를 라이브 URL로 만드는 전체 과정을 설명하며, 워크스페이스에 내장된 관리형 Git 서비스인 **[PlaidCloud Git](/ko/guides/git/)** 을 소스로 사용합니다. PlaidCloud Git은 관리형이므로 앱을 배포하는 연결에 **서버 URL, 사용자 이름, 토큰이 필요하지 않습니다**. PlaidCloud가 사용자를 대신해 인증합니다.

다섯 단계로 진행합니다.

1. 최소한의 Panel 앱을 작성합니다.
2. PlaidCloud Git 리포지토리에 올립니다.
3. 관리형 PlaidCloud Git 연결을 만듭니다.
4. 리포지토리를 가리키는 서버 앱을 게시합니다.
5. 제공되는 앱을 열고, 시작되지 않으면 빌드 로그를 확인합니다.

각 단계는 해당 부분을 자세히 다루는 가이드로 연결되며, 이 문서는 이를 하나의 경로로 엮은 것입니다.

## 시작하기 전에

- 워크스페이스에서 **Git**을 열어 PlaidCloud Git에 접근할 수 있는지 확인합니다. 기본적으로 워크스페이스의 조직에는 **`apps`** 리포지토리(그리고 **`udfs`** 리포지토리)가 있으며, Panel 앱을 두기에 가장 알맞은 위치입니다.
- 컴퓨터에서 코드를 푸시하려면 `git`이 로컬에 설치되어 있어야 합니다(Git 웹 UI에서 파일을 추가할 수도 있습니다).

## 1. 최소한의 Panel 앱 작성

앱에는 Panel 앱을 빌드하고 `.servable()`로 표시하는 Python 파일인 **진입점**이 필요하며, 추가 패키지가 있으면 리포지토리 루트나 진입점 옆에 **`requirements.txt`** 를 선택적으로 둘 수 있습니다.

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

이것으로 완전한 앱입니다. PlaidCloud가 제공하는 것은 `.servable()` 호출입니다. `panel`, `bokeh`, PlaidCloud 클라이언트 라이브러리(`plaidcloud-rpc`, `plaidcloud-utilities`)는 미리 설치되어 있으므로 `requirements.txt`에는 *추가* 패키지만 나열하십시오. 더 풍부한 예제, 종속성, 밝은 테마와 어두운 테마 설정은 [Panel 앱 만들기](/ko/guides/panel-apps/creating/)를 참조하십시오.

## 2. PlaidCloud Git 리포지토리에 앱 올리기

워크스페이스에 이미 있는 **`apps`** 리포지토리를 사용하거나 [새로 만드십시오](/ko/guides/git/repositories/#리포지토리-만들기). 그런 다음 코드를 그 안에 넣습니다. [Panel Studio](/ko/guides/panel-apps/studio/#앱이-저장되는-위치)에서 만든 앱은 이미 `apps` 안의 폴더이므로 직접 올린 앱 옆에서 찾을 수 있습니다.

PlaidCloud를 통해 로그인하므로 Git 계정에는 별도의 비밀번호가 없습니다. **write:repository** 권한이 있는 [개인 액세스 토큰을 생성](/ko/guides/git/repositories/#개인용-액세스-토큰-생성)(**아바타 → Settings → Applications**)하고 Git이 비밀번호를 요청할 때 이를 사용하십시오. `apps`에 푸시하려면 **Contributor** 액세스가 필요합니다. **Git** 탭에 **뷰어**로 표시되면 워크스페이스 관리자에게 **Git Contributors**에 추가해 달라고 요청하십시오. **Git** 탭에서 리포지토리 복제 주소 옆의 복사 버튼을 사용한 다음 다음을 실행합니다.

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

리포지토리 경로인 `<org>/apps`를 기록해 두십시오. 여기서 `<org>`는 워크스페이스의 조직 이름입니다. 다음 단계에서 이 경로를 입력합니다. 전체 복제, 커밋, 푸시 방법은 [리포지토리](/ko/guides/git/repositories/)에 있습니다.

> **여기서 토큰은 *사용자*가 코드를 푸시하는 용도로만 쓰입니다.** 다음에 만드는 연결은 관리형이며 토큰이 필요 없으므로 둘을 혼동하지 마십시오.

## 3. 관리형 PlaidCloud Git 연결 만들기

**연결**은 Panel 배포에 코드가 어디에 있는지 알려 줍니다. PlaidCloud Git의 연결은 *관리형*이므로 PlaidCloud가 호스트와 자격 증명을 제공하며, 사용자는 리포지토리 대상만 입력합니다.

1. **Tools > 연결**을 열고 **새 연결**을 클릭한 다음 **PlaidCloud Git**을 선택합니다.
2. 연결에 **계정 이름**을 지정합니다(예: `Apps Repo`).
3. **리포지토리 경로**를 `<org>/apps`(2단계에서 기록해 둔 경로)로, **기본 브랜치**를 `main`으로 설정합니다. 앱이 하위 디렉터리에 있지 않다면 **시작 경로**는 비워 둡니다.
4. **만들기**를 클릭합니다.

서버 URL, 사용자, 비밀번호, SSL/SSH 필드가 없습니다. PlaidCloud Git은 관리형이므로 플랫폼이 호스트와 인증을 처리합니다. 연결의 **사용법**과 **보안 모델**(워크스페이스에서 누가 사용할 수 있는지)을 포함한 전체 양식은 [PlaidCloud Git 연결](/ko/guides/connections/plaidcloud-git/)을 참조하십시오.

> **이전 워크스페이스 빌드를 사용 중이신가요?** 양식에 여전히 서버 URL이나 자격 증명 필드가 표시되면 비워 두십시오. 어느 쪽이든 플랫폼이 사용자를 대신해 인증합니다.

## 4. 서버 앱 게시

이제 서버 배포가 해당 연결을 가리키도록 설정합니다.

1. **내 Panel 앱**을 열고 **새 서버 앱**을 클릭합니다.
2. **디렉터리 설정**에서 **앱 이름**과 **URL 슬러그**를 설정합니다. 슬러그는 앱의 URL이자 내부 이름이므로 소문자, 숫자, 하이픈을 사용하고 문자로 시작하며 40자 이하여야 합니다(예: `hello-panel`).
3. **Git 연결 및 게시 감시기**에서 다음을 설정합니다.
   - **Git 연결** — 3단계에서 만든 PlaidCloud Git 연결입니다.
   - **브랜치** — `main`입니다. 이 브랜치로 푸시하면 앱이 자동으로 다시 빌드되고 다시 배포됩니다.
   - **진입점** — `app.py`입니다.
4. **런타임**에서 **CPU**, **메모리**, **디자인**(PlaidCloud의 현대적인 모양을 쓰려면 **FAST**), **Idle** 시간을 선택합니다. 로그인하지 않고도 앱에 접근할 수 있어야 하는 경우에만 **공개 액세스 허용**을 선택합니다.
5. **게시**를 클릭합니다.

이 대화 상자의 모든 필드는 [Panel 앱 만들기](/ko/guides/panel-apps/creating/#앱-게시)에 설명되어 있습니다.

## 5. 앱 열기, 시작되지 않으면 로그 확인

게시하면 앱이 **빌드**됩니다. PlaidCloud가 브랜치를 복제하고, `requirements.txt`(있으면 리포지토리 루트와 앱 폴더의 것)를 설치하고, 컨테이너 이미지를 빌드합니다. 앱의 **상태**는 **내 Panel 앱** 목록에 표시되며 자동으로 업데이트됩니다.

- 상태가 **준비됨**이면 `https://<your-tenant-host>/serve/<slug>/`에서 앱을 엽니다. 유휴 상태 이후 첫 요청은 앱을 깨우는 데 시간(약 15초)이 걸립니다.
- 빌드가 실패하면 앱을 열고 **빌드** 로그를 확인하십시오. 누락된 종속성이나 가져오기 오류가 여기에 표시됩니다. 각 상태의 의미, 로그를 읽는 방법, 다시 빌드를 시작하는 방법은 [Panel 앱 사용](/ko/guides/panel-apps/using/)을 참조하십시오.

이후에는 **연결된 브랜치로 푸시할 때마다 앱이 자동으로 다시 빌드되고 다시 배포됩니다.** `app.py`를 편집하고 `git push`하면 변경 사항이 라이브가 됩니다. (앱이 **잠겨** 있지 않은 경우에 한합니다. 잠긴 경우에는 [앱 잠금](/ko/guides/panel-apps/using/#앱-잠금)을 참조하십시오. 잠금을 해제할 때까지 푸시는 건너뜁니다.)

## 다음 단계

- [Panel 앱 만들기](/ko/guides/panel-apps/creating/) — 더 풍부한 예제, 종속성, 밝은 테마와 어두운 테마 설정
- [PlaidCloud Git 연결](/ko/guides/connections/plaidcloud-git/) — 전체 연결 양식, 사용법, 보안 모델
- [데이터 및 로그인한 사용자 읽기](/ko/guides/panel-apps/accessing-data/) — 앱을 보는 사람의 권한으로 PlaidCloud 데이터를 쿼리합니다
- [리포지토리](/ko/guides/git/repositories/) — PlaidCloud Git의 브랜치, 토큰, 협업
