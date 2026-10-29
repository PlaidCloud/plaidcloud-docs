---
title: PlaidCloud Git에서 Dash 앱 배포
description: PlaidCloud에서 Plotly Dash 앱을 서비스하는 전체 과정입니다. 코드를 PlaidCloud Git 리포지토리에 넣고, 자격 증명이 필요 없는 관리형 연결로 연결한 다음 라이브로 게시합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/deploy-from-git.md
---

이 문서는 워크스페이스에 내장된 관리형 Git 서비스인 **[PlaidCloud Git](/ko/guides/git/)** 을 소스로 사용하여, 내 컴퓨터의 Dash 앱 코드에서 라이브 URL까지 이르는 전체 과정을 설명합니다. PlaidCloud Git은 관리형이므로 앱을 배포하는 연결에 **서버 URL, 사용자 이름, 토큰이 필요 없으며** PlaidCloud가 사용자를 대신해 인증합니다.

다섯 단계로 진행합니다.

1. 최소한의 Dash 앱을 작성합니다.
2. PlaidCloud Git 리포지토리에 넣습니다.
3. 관리형 PlaidCloud Git 연결을 만듭니다.
4. 리포지토리를 가리키는 Dash 앱을 게시합니다.
5. 서비스 중인 앱을 열고, 시작되지 않으면 빌드 로그를 확인합니다.

이 안내는 [PlaidCloud Git에서 Panel 앱 배포](/ko/guides/panel-apps/deploy-from-git/)와 거의 동일합니다. 두 앱 모두 Git에서 빌드되어 같은 방식으로 서비스되는 서버 측 Python 앱입니다. 차이점은 앱 코드 자체와 게시 대화 상자의 필드 하나뿐입니다.

## 시작하기 전에

- 워크스페이스에서 **Git**을 열어 PlaidCloud Git에 접속할 수 있는지 확인합니다. 기본적으로 워크스페이스의 조직에는 **`apps`** 리포지토리가 포함되어 있으며, Dash 앱에도 적합한 위치입니다.
- 내 컴퓨터에서 코드를 푸시하려면 로컬에 `git`을 설치하십시오(Git 웹 UI에서 파일을 추가할 수도 있습니다).

## 1. 최소한의 Dash 앱 작성

앱에는 Dash 앱을 만들고 Flask 서버를 노출하는 Python 파일인 **진입점**이 필요합니다. 추가 패키지가 있다면 리포지토리 루트 또는 진입점 옆에 **`requirements.txt`** 를 선택적으로 둘 수 있습니다.

```
apps/
├── app.py            # entry point — exposes `server`
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

`app.py`를 만듭니다.

```python
import plaidcloud_dash as pcd
from dash import Dash, Input, Output, html

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you

app.layout = html.Div(
    [
        html.H1("Hello from PlaidCloud Git"),
        html.P(id="whoami"),
        html.Button("Who am I?", id="whoami-btn", n_clicks=0),
    ]
)


@app.callback(Output("whoami", "children"), Input("whoami-btn", "n_clicks"))
def _whoami(n_clicks):
    if not n_clicks:
        return ""
    return f"Signed in as {pcd.current_user()!r}"


if __name__ == "__main__":
    app.run(debug=True)
```

이것으로 완전한 앱이 됩니다. `dash`, `plotly`, `dash-mantine-components`, `dash-ag-grid`와 PlaidCloud 클라이언트 라이브러리(`plaidcloud-rpc`, `plaidcloud-utilities`)는 미리 설치되어 있으므로 `requirements.txt`에는 *추가* 패키지만 나열하십시오. `Dash(__name__)`에 `requests_pathname_prefix` 또는 `url_base_pathname`을 전달하지 마십시오. 플랫폼이 `DASH_URL_BASE_PATHNAME`을 통해 URL 접두사를 자동으로 설정하며, 둘 다 설정하면 시작 시 구성 오류가 발생합니다. 전체 앱 규약과 데이터 액세스 도우미는 [앱 규약](/ko/guides/dash-apps/#앱-규약)과 [Dash 앱에서 데이터와 로그인한 사용자 읽기](/ko/guides/dash-apps/accessing-data/)를 참조하십시오.

## 2. PlaidCloud Git 리포지토리에 앱 넣기

워크스페이스의 기존 **`apps`** 리포지토리를 사용하거나 [새로 만드십시오](/ko/guides/git/repositories/#리포지토리-만들기). 그런 다음 코드를 리포지토리에 넣습니다.

PlaidCloud를 통해 로그인하므로 Git 계정에는 별도의 비밀번호가 없습니다. 리포지토리 **읽기** 및 **쓰기** 범위를 가진 [개인 액세스 토큰을 생성](/ko/guides/git/repositories/#개인-액세스-토큰-생성)한 다음(**아바타 → 설정 → 애플리케이션**), Git이 묻을 때 이 토큰을 비밀번호로 사용하십시오. 리포지토리의 **코드** 버튼에서 **HTTPS** 복제 URL을 복사한 다음 다음과 같이 실행합니다.

```bash
git clone https://<your-git-host>/<org>/apps.git
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

리포지토리 경로 `<org>/apps`를 기록해 두십시오. 여기서 `<org>`는 워크스페이스의 조직 이름입니다. 이 경로는 다음 단계에서 입력합니다. 복제, 커밋, 푸시에 관한 자세한 내용은 [리포지토리](/ko/guides/git/repositories/)에 있습니다.

> **여기서 사용하는 토큰은 *사용자*가 코드를 푸시하는 용도일 뿐입니다.** 다음에 만들 연결은 관리형이며 토큰이 필요 없습니다. 둘을 혼동하지 마십시오.

## 3. 관리형 PlaidCloud Git 연결 만들기

**연결**은 Dash 배포에 코드가 있는 위치를 알려 줍니다. PlaidCloud Git의 연결은 *관리형*이므로 PlaidCloud가 호스트와 자격 증명을 제공하며, 사용자는 리포지토리 대상만 입력합니다. 이는 서버 Panel 앱이 사용하는 것과 같은 연결 유형입니다.

1. **도구 > 연결**을 열고 **새 연결**을 클릭한 다음 **PlaidCloud Git**을 선택합니다.
2. 연결에 **계정 이름**을 지정합니다(예: `Apps Repo`).
3. **Repository Path**를 `<org>/apps`(2단계에서 기록한 경로)로 설정하고 **기본 브랜치**를 `main`으로 설정합니다. 앱이 하위 디렉터리에 있는 경우가 아니면 **시작 경로**는 비워 둡니다.
4. **만들기**를 클릭합니다.

서버 URL, 사용자, 비밀번호 또는 SSL/SSH 필드는 없습니다. PlaidCloud Git은 관리형이므로 플랫폼이 호스트와 인증을 처리합니다. 연결의 **사용법**과 **보안 모델**(워크스페이스에서 연결을 사용할 수 있는 대상)을 포함한 전체 양식은 [PlaidCloud Git 연결](/ko/guides/connections/plaidcloud-git/)을 참조하십시오.

## 4. Dash 앱 게시

이제 Dash 배포가 해당 연결을 가리키도록 합니다.

1. **내 Panel 앱**을 열고 **새 Dash 앱**을 클릭합니다.
2. **디렉터리 설정**에서 **앱 이름**과 **URL 슬러그**를 설정합니다. 슬러그는 앱의 URL이자 내부 이름이므로 소문자, 숫자, 하이픈만 사용하고 문자로 시작하며 40자 이하로 지정하십시오(예: `hello-dash`). 선택 사항인 **메모**에는 앱에 대한 설명을 적습니다.
3. **Git 연결 및 게시 감시기**에서 다음을 설정합니다.
   - **Git 연결** — 3단계에서 만든 PlaidCloud Git 연결입니다.
   - **브랜치** — `main`입니다. 이 브랜치에 푸시하면 앱이 자동으로 다시 빌드되고 재배포됩니다.
   - **진입점** — `app.py`입니다.
4. **런타임**에서 **CPU**, **메모리**, **유휴 시간(분)** 창을 선택합니다. 로그인 없이 앱에 접근할 수 있어야 하는 경우에만 **공개 액세스 허용**을 선택합니다. **디자인** 설정은 없습니다. 이는 Panel 전용 옵션입니다.
5. **고급 (임베디드 서비스)** — 선택 사항입니다. 앱을 다른 사이트에 임베드하는 경우가 아니면 비워 둡니다.
6. **게시**를 클릭합니다.

## 5. 앱 열기, 시작되지 않으면 로그 확인

게시하면 앱이 **빌드**됩니다. PlaidCloud가 브랜치를 복제하고 `requirements.txt`를 설치한 다음 `platform-dash-base` 이미지로 컨테이너 이미지를 빌드합니다. 앱의 **상태**는 **내 Panel 앱** 목록에 표시되며 자동으로 업데이트됩니다.

- 상태가 **준비됨**이 되면 `https://<your-tenant-host>/serve/<slug>/`에서 앱을 엽니다. 유휴 상태 이후 첫 번째 요청은 앱을 기동시키며, 그동안 짧은 PlaidCloud 로딩 화면이 표시됩니다.
- 빌드가 실패하면 앱을 열고 **빌드** 로그를 확인하십시오. 누락된 종속성이나 가져오기 오류가 여기에 표시됩니다. 각 상태의 의미, 로그를 읽는 방법, 다시 빌드를 트리거하는 방법은 [Dash 앱 사용](/ko/guides/dash-apps/using/)을 참조하십시오.

이후에는 **연결된 브랜치에 푸시할 때마다 앱이 자동으로 다시 빌드되고 재배포됩니다**. `app.py`를 수정하고 `git push`하면 변경 사항이 라이브로 반영됩니다. (앱이 **잠겨** 있으면 잠금을 해제할 때까지 푸시가 건너뛰어집니다. [Dash 앱 사용](/ko/guides/dash-apps/using/#앱-잠그기)을 참조하십시오.)

## 다음 단계

- [Dash 앱에서 데이터와 로그인한 사용자 읽기](/ko/guides/dash-apps/accessing-data/) — 앱을 보는 사람의 권한으로 PlaidCloud 데이터를 쿼리합니다.
- [Dash 앱 사용](/ko/guides/dash-apps/using/) — 빌드 상태, 로그, 잠금, 앱 제거를 설명합니다.
- [PlaidCloud Git 연결](/ko/guides/connections/plaidcloud-git/) — 전체 연결 양식, 사용법, 보안 모델을 설명합니다.
- [리포지토리](/ko/guides/git/repositories/) — PlaidCloud Git의 브랜치, 토큰, 협업을 설명합니다.
