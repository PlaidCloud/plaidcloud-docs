---
title: Dash 앱
description: PlaidCloud에서 서버 측 Plotly Dash 데이터 애플리케이션을 빌드하고 배포합니다. Git 리포지토리에서 게시하며 사용자별 인증과 제로 스케일링을 지원하고, 서버 Panel 앱과 동등한 기능을 제공합니다.
sidebar:
  label: Dash 앱
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/index.md
---

Dash 앱을 사용하면 콜백, 차트, 데이터 그리드(`dash-ag-grid`, `dash-mantine-components`)를 갖춘 대화형 [Plotly Dash](https://dash.plotly.com/) 애플리케이션을 PlaidCloud에서 바로 게시할 수 있습니다. **내 Panel 앱** 화면에서 Panel 앱과 함께 관리하며, 각 행에 런타임, 빌드 상태, URL이 표시됩니다.

## Dash의 위치

Dash 앱은 **서버 Panel 앱**과 똑같이 호스팅됩니다. PlaidCloud가 Git 리포지토리의 브랜치를 가리키면 코드를 컨테이너로 빌드하고, 컨테이너는 복제본 0개로 유휴 상태에 있다가 첫 번째 요청에서 깨어나 서비스하며, 유휴 상태가 되면 다시 0으로 축소됩니다. Dash용 별도의 "WASM" 런타임은 없으며 모든 Dash 앱은 서버 앱입니다.

앱을 HoloViz Panel이 아닌 Plotly Dash로 작성한 경우에 Dash 앱을 선택하십시오. 예를 들어 기존 Dash 코드베이스가 있거나, Dash의 콜백 모델과 `dash-ag-grid` / `dash-mantine-components` 생태계를 선호하는 팀이 해당합니다. 처음 시작하며 특별한 선호가 없다면 대안인 [Panel 앱](/ko/guides/panel-apps/)을 참조하십시오.

서버 Panel 앱이 제공받는 모든 기능을 Dash 앱도 제공받습니다.

- **사용자별 ID.** 각 사용자는 플랫폼의 싱글 사인온으로 로그인하며, 앱이 데이터를 읽기 위해 수행하는 모든 호출은 *그 사용자*의 권한으로 실행됩니다. [데이터와 로그인한 사용자 읽기](/ko/guides/panel-apps/accessing-data/)와 동일한 모델을 Dash 자체 도우미 API로 사용합니다. [Dash 앱에서 데이터와 로그인한 사용자 읽기](/ko/guides/dash-apps/accessing-data/)를 참조하십시오.
- **제로 스케일링.** 앱은 설정된 유휴 시간이 지나면 복제본 0개로 유휴 상태가 되고 다음 요청에서 깨어나며, 콜드 스타트 중에는 짧은 PlaidCloud 로딩 화면이 표시됩니다. [Dash 앱 사용](/ko/guides/dash-apps/using/#dash-앱-열기)을 참조하십시오.
- **자동 다시 빌드.** 연결된 브랜치에 푸시할 때마다 앱이 다시 빌드되고 재배포됩니다.
- **런타임 및 빌드 로그.** 각 줄에는 해당 줄을 생성한 세션의 사용자가 태그로 표시됩니다.

Dash 앱에는 다음 두 가지가 **없으며**, 둘 다 의도된 설계이고 Panel 앱에도 없는 기능입니다.

- **디자인/테마 설정 없음.** Panel 게시 대화 상자의 **디자인** 옵션(FAST 또는 기본값)은 Panel 전용입니다. Dash 앱은 선택한 구성 요소(`dash-mantine-components`, 사용자 지정 CSS 등)를 통해 스타일을 전적으로 지정하므로 게시 양식에는 이에 해당하는 필드가 없습니다.
- **앱별 액세스 목록 없음.** 액세스는 워크스페이스의 SSO 게이트로 제어됩니다. 테넌트에 로그인한 사용자는 누구나 앱을 열 수 있으며(**공개 액세스 허용**을 사용하면 누구나 열 수 있습니다), 두 앱 유형 모두 앱별 ACL 계층은 따로 없습니다.

## 앱 규약

Dash 앱의 진입 파일 이름은 `app.py`여야 하고 `server`를 노출해야 합니다. 규약은 이것이 전부입니다.

```python
from dash import Dash

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you
```

- **파일 이름을 `app.py`로 지정하십시오.** PlaidCloud의 런처는 앱을 `app` 모듈로 가져와 `server` 객체를 읽으므로, **진입점**에 설정한 경로(리포지토리 루트 또는 하위 폴더)와 관계없이 해당 경로의 파일 이름은 `app.py`여야 합니다.
- **모듈 수준에서 `server = app.server`를 노출하십시오.** 플랫폼이 가져오는 객체가 이것입니다.
- **로그인을 직접 연결할 필요가 없습니다.** 플랫폼이 모든 요청을 사용자별 싱글 사인온 뒤에 자동으로 두므로, ID를 얻기 위해 `init_auth`를 호출하거나 `plaidcloud_dash`를 가져올 필요가 없습니다. (`plaidcloud_dash.init_auth(server, url_base_pathname=os.environ["DASH_URL_BASE_PATHNAME"])`를 *호출하는* 기존 앱도 그대로 작동합니다. 이 호출은 멱등성이 있어 플랫폼 자체 연결과 공존합니다.)
- **`Dash(__name__)`에 `requests_pathname_prefix` 또는 `url_base_pathname`을 설정하지 마십시오.** 모든 Dash 앱은 필수 URL 접두사(`/serve/<slug>/`) 아래에서 서비스되며, 플랫폼이 Dash 자체의 기본 구성 변수인 `DASH_URL_BASE_PATHNAME` 환경 변수를 통해 이를 설정합니다. 이 변수는 모든 생성자 인수보다 먼저 읽힙니다. 접두사를 명시적으로도 전달하면 Dash 자체 구성과 충돌하여 앱이 시작되지 않습니다.
- **`Entry Point`는 하위 폴더를 가리킬 수 있습니다.** 앱을 시작하기 전에 호스트가 컨테이너의 작업 디렉터리를 진입 파일이 있는 폴더로 설정하므로, 같은 폴더의 형제 가져오기(`import data`)와 앱의 상대 파일 경로는 그 폴더 안에서 `python app.py`를 실행한 것과 똑같이 해당 폴더를 기준으로 확인됩니다.
- **가져오기 시점에 데이터를 읽지 마십시오.** PlaidCloud 읽기는 모듈 범위가 아닌 콜백 내부에서 수행하십시오. [Dash 앱에서 데이터와 로그인한 사용자 읽기](/ko/guides/dash-apps/accessing-data/)를 참조하십시오. 앱의 모듈은 컨테이너가 시작될 때, 즉 아무도 로그인하기 전에 한 번 실행되므로 그 시점의 연결이나 테이블 읽기는 대신 동작할 사용자가 없어 부팅 시 앱이 실패합니다.

PlaidCloud는 앱을 **스레드 방식의 gunicorn** 아래에서 실행하므로 하나의 프로세스에서 동시 접속 사용자를 처리합니다. 둘 이상의 사용자가 동시에 앱을 사용하도록 지원하기 위해 추가로 할 일은 없습니다.

## Panel과 Dash 중 선택

| | Panel 앱 | Dash 앱 |
|---|---|---|
| 프레임워크 | HoloViz Panel | Plotly Dash |
| 런타임 | WASM(브라우저 내) 또는 서버 | 서버만 |
| ID 모델 | 사용자별 SSO(서버 앱) | 사용자별 SSO |
| 제로 스케일링 | 서버 앱만 | 예 |
| 디자인/테마 설정 | 예(FAST / 기본값) | 아니요 — 자체 구성 요소로 스타일 지정 |
| 앱별 액세스 목록 | 아니요 — 워크스페이스 SSO 게이트 | 아니요 — 워크스페이스 SSO 게이트 |

## 다음 단계

- [PlaidCloud Git에서 Dash 앱 배포](/ko/guides/dash-apps/deploy-from-git/) — 자격 증명이 필요 없는 관리형 연결을 사용하여 리포지토리에서 서비스 중인 앱까지 이르는 전체 과정입니다.
- [Dash 앱에서 데이터와 로그인한 사용자 읽기](/ko/guides/dash-apps/accessing-data/) — 앱을 보는 사람의 권한으로 PlaidCloud 데이터를 쿼리합니다.
- [Dash 앱 사용](/ko/guides/dash-apps/using/) — 빌드 상태, 앱 열기, 로그, 앱 제거를 설명합니다.
