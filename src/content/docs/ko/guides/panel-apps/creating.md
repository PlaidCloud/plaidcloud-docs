---
title: Panel 앱 만들기
description: Panel Studio에서 빈 앱, 테이블, 뷰 또는 갤러리로 Panel 앱을 만들거나, 맞춤 요구 사항을 위해 git의 서버 앱 또는 정적 WASM 앱을 게시합니다.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

Panel Studio로 시작하십시오. 리포지토리나 별도 설정이 필요 없습니다. PlaidCloud에서 앱을 빌드하고 미리 본 다음 준비가 되면 게시합니다. Studio가 맞지 않을 때만 맞춤 런타임을 선택하십시오.

## Studio 앱 만들기

**내 Panel 앱**을 엽니다. **새 Studio 앱**은 도구 모음의 첫 번째 버튼입니다. 프로젝트의 **홈** 탭에 있는 **패널 앱** 상자에서 **새 Studio 앱**을 선택하거나 [테이블에서 시작](#테이블에서-시작)할 수도 있습니다.

1. **새 Studio 앱**을 선택합니다.
2. **이름**을 입력합니다. **URL 슬러그**는 이름에서 자동으로 채워집니다.
3. 앱을 소유할 **프로젝트**를 선택합니다. 프로젝트에 대한 편집 액세스 권한이 필요합니다.
4. **시작 기준**에서 앱을 시작할 방식을 선택합니다.

   | 시작 기준 | 결과 |
   |---|---|
   | **빈 앱** | `app.py`와 `requirements.txt`가 있는 최소 앱입니다. |
   | **테이블에서** | 선택한 테이블을 기반으로 빌드된 앱입니다. |
   | **뷰에서** | 프로젝트 뷰를 기반으로 빌드된 동일한 앱입니다. |
   | **다른 Studio 앱에서** | 내 Studio 앱 중 하나의 복사본입니다. |
   | **갤러리에서** | 워크스페이스에서 [갤러리에 등록한](#갤러리에서-시작) 앱의 복사본입니다. |

5. **만들기**를 선택합니다. Studio에서 새 앱이 열립니다. 테이블이나 뷰의 경우 첫 페이지를 빌드하는 Weave 프롬프트가 전송할 수 있도록 준비되어 있습니다.

앱을 편집, 미리 보기 및 게시하려면 [Panel Studio](/ko/guides/panel-apps/studio/)를 참조하십시오.

### 테이블에서 시작

프로젝트의 **테이블** 탭에서 시작할 수도 있습니다. 테이블 또는 뷰를 하나 선택한 다음 **새로 만들기** 메뉴 또는 마우스 오른쪽 버튼 메뉴에서 **Panel 앱 만들기**을 선택합니다. 프로젝트와 테이블이 이미 선택된 상태로 **새 Studio 앱** 대화 상자가 열립니다. 이 명령은 프로젝트에 대한 편집 액세스 권한이 있고 프로젝트가 읽기 전용이 아닐 때 사용할 수 있습니다.

### 갤러리에서 시작

**내 Panel 앱** 도구 모음에서 **갤러리**를 선택하여 워크스페이스에 등록된 앱을 둘러보고, **이것으로 앱 만들기…** 옵션을 선택하여 나만의 복사본을 만듭니다. 또는 **새 Studio 앱** 대화 상자에서 **갤러리에서**를 선택합니다. 내 앱을 등록하는 방법을 포함하여 [앱 갤러리](/ko/guides/panel-apps/gallery/)를 참조하십시오.

## 기타 런타임

Studio 앱은 대부분의 대시보드와 도구를 다룹니다. 맞춤 요구 사항이 있으면 **내 Panel 앱** 도구 모음에서 다른 [런타임](/ko/guides/panel-apps/) 중 하나로 게시하십시오.

- **WASM 앱 추가** — 파일에서 브라우저 내 정적 앱을 게시합니다.
- **새 서버 앱** — 직접 관리하는 git 리포지토리에서 앱을 빌드하고 실행합니다. 예를 들어 기존 코드나 자체 빌드 프로세스를 재사용할 때 사용합니다.
- **새 Dash 앱** — Plotly Dash 앱을 게시합니다. [Dash 앱](/ko/guides/dash-apps/)을 참조하십시오.

## 서버 앱 만들기

서버 앱은 git 리포지토리에서 빌드되며 `https://<your-tenant-host>/serve/<slug>/`에서 제공됩니다. PlaidCloud가 리포지토리의 브랜치를 가리키도록 지정하면 코드를 컨테이너로 빌드하고 `panel serve`를 실행하며, 해당 브랜치에 푸시할 때마다 자동으로 다시 빌드합니다.

### 앱 리포지토리 준비

리포지토리에는 두 가지가 필요합니다. 하나는 **진입점**, 즉 Panel 앱을 빌드하고 `.servable()`로 표시하는 Python 파일이며, 다른 하나는 선택 사항으로 리포지토리 루트 또는 진입점 옆에 둘 수 있는 추가 패키지를 나열한 **`requirements.txt`** 입니다.

```
my-panel-app/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

#### Hello World

`app.py`를 만듭니다.

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello, PlaidCloud 👋\n\nYour first server-side Panel app is running.").servable()
```

이것으로 완전한 앱이 됩니다. PlaidCloud가 제공하는 것은 `.servable()` 호출입니다. 렌더링하려는 모든 항목은 (직접 또는 servable 레이아웃 안에 있음으로써) servable로 표시되어야 합니다.

#### 조금 더 풍부한 예제

Panel 앱은 대화형입니다. 이 예제는 테이블을 실시간으로 업데이트하는 슬라이더를 추가합니다.

```python
import pandas as pd
import panel as pn

pn.extension()

multiplier = pn.widgets.IntSlider(name="Multiplier", start=1, end=10, value=3)

@pn.depends(multiplier)
def times_table(m):
    df = pd.DataFrame({"n": range(1, 6)})
    df["result"] = df["n"] * m
    return pn.pane.DataFrame(df, index=False)

pn.Column(
    "# Times Table",
    multiplier,
    times_table,
).servable()
```

#### 종속성 추가

이 두 번째 예제는 기본 이미지에 포함되지 않은 `pandas`를 가져오므로 `requirements.txt`를 추가하십시오(리포지토리 루트 또는 진입점 옆).

```text
pandas
```

PlaidCloud는 이미지를 빌드할 때 `pip`로 이러한 패키지를 설치합니다. `plotly`, `holoviews`, `hvplot` 같은 일반적인 시각화 라이브러리도 기본 이미지에 없으므로 앱이 가져오는 라이브러리는 여기에 나열하십시오.

> **플랫폼이 제공하는 것과 기대하는 것.** 앱을 작성할 때 다음 가정을 염두에 두십시오.
>
> - **`panel`과 `bokeh`는 사전 설치되어 있습니다.** 플랫폼 기본 이미지가 제공합니다. `requirements.txt`에 나열하지 말고, 이전 버전의 Panel로 고정하지 마십시오. 실시간 업데이트 재연결은 최신 버전에 의존합니다.
> - **PlaidCloud 클라이언트 라이브러리(`plaidcloud-rpc`, `plaidcloud-utilities`)는 사전 설치되어 있습니다.** `plaidcloud.rpc` 또는 `plaidcloud.utilities`를 직접 가져오고 `requirements.txt`에 나열하지 마십시오.
> - **`requirements.txt`는 리포지토리 루트 또는 진입점 옆에 둘 수 있습니다.** 공유(모노레포) 리포지토리에서는 각 앱의 종속성을 해당 앱의 폴더에 두십시오. 루트 수준 파일이 있으면 그것도 설치되므로 공유 종속성은 루트에, 앱별 종속성은 앱 옆에 두십시오.
> - **앱은 읽기 전용 파일 시스템에서 루트가 아닌 사용자로 실행됩니다.** `/tmp`만 쓸 수 있으므로 임시 파일은 그곳에 쓰십시오(대부분의 라이브러리는 이미 `$TMPDIR`을 따릅니다).
> - **포트, URL 접두사, 호스트를 하드코딩하지 마십시오.** PlaidCloud가 배포 시점에 할당하고 주입하므로 `.servable()`만 호출하면 됩니다.

PlaidCloud 모양과 기성 필터, 그리드, 차트를 사용하려면 [Panel 앱 키트](/ko/guides/panel-apps/app-kit/)로 앱을 빌드하십시오.

### 테마 설정: 라이트, 다크 또는 전환

서버 앱은 기본적으로 PlaidCloud의 현대적인 **Fast** 디자인으로 렌더링됩니다. 플랫폼 전체에 적용되는 깔끔한 Fluent 스타일의 모양입니다. 게시 대화 상자에서 **디자인**은 이 플랫폼 계층을 제어합니다.

- **FAST** — PlaidCloud 기본값입니다. 새 앱과 Fast 템플릿으로 빌드한 앱에 사용하십시오.
- **기본값** — Panel의 기본 스타일입니다. 기존 앱의 CSS나 시각 요소가 FAST에서 깨질 때 사용하십시오.

앱 코드에서 제어하는 것은 **테마**, 즉 라이트, 다크 또는 보는 사람이 전환할 수 있는 스위치입니다.

테마는 제공하는 **템플릿**의 속성입니다. Fast 템플릿인 `FastListTemplate`(단일 열)과 `FastGridTemplate`(반응형 그리드)은 이를 위해 두 가지 설정을 받습니다.

- **`theme`** — 라이트는 `"default"`, 다크는 `"dark"`입니다. 이 값을 설정하면 보는 사람이 URL에 `?theme=dark`를 추가해도 앱이 해당 테마로 고정됩니다.
- **`theme_toggle`** — `True`이면 헤더에 라이트/다크 스위치가 표시되고 `False`이면 숨겨집니다. 기본값은 `True`입니다. 스위치를 숨기는 것만으로는 테마가 고정되지 않습니다. 위의 `theme`으로 고정하십시오. 고정한 후에는 보는 사람에게 아무것도 바꾸지 못하는 스위치가 보이지 않도록 `theme_toggle=False`로 설정하십시오.

앱에 맞는 패턴을 선택하십시오.

**라이트 전용** — 보통 밝은 배경에 맞게 직접 스타일을 지정하는 밀도 높은 보고서와 재무 테이블에 가장 적합합니다.

```python
import panel as pn

pn.extension("tabulator")

pn.template.FastListTemplate(
    title="Sales Dashboard",
    theme="default",      # light
    theme_toggle=False,   # hide the switch
    main=[...],
).servable()
```

**다크 전용:**

```python
pn.template.FastListTemplate(
    title="Ops Monitor",
    theme="dark",
    theme_toggle=False,
    main=[...],
).servable()
```

**보는 사람이 선택** — 기본값은 라이트이며 헤더에 스위치가 있습니다. 전환을 따르도록 `theme`을 생략하십시오.

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **다크를 허용한다면 테이블이 다크 테마를 인식하도록 만드십시오.** 라이트 테이블 테마(`theme="bootstrap"`)로 고정된 `Tabulator`나 `background: #fff`처럼 밝은 색을 하드코딩한 사용자 지정 CSS는 어두운 페이지에서 읽을 수 없는 흰색 블록으로 렌더링됩니다. `pn.widgets.Tabulator(..., theme="fast")`처럼 앱을 따르는 테이블 테마를 사용하고 밝은 색을 하드코딩하지 마십시오. 보고서가 라이트에 맞게 많이 직접 스타일링되어 있다면 대신 라이트로 고정하십시오(위의 첫 번째 패턴).

템플릿이 없는 일반 앱인 `pn.Column(...).servable()`은 Panel 기본값을 따르며 이 설정의 영향을 받지 않습니다. 명시적으로 제어하려면 템플릿을 사용하십시오.

리포지토리는 PlaidCloud의 **Git 연결**을 통해 접근할 수 있어야 합니다. 코드가 [PlaidCloud Git](/ko/guides/git/)에 있다면 **Tools > Connections**에서 관리형 **PlaidCloud Git** 연결을 만드십시오. 서버 URL이나 자격 증명이 필요하지 않습니다. 빈 리포지토리에서 제공되는 앱까지의 전체 과정은 [PlaidCloud Git에서 Panel 앱 배포](/ko/guides/panel-apps/deploy-from-git/)를 참조하십시오.

### 앱 게시

1. **새 서버 앱**을 클릭하여 **서버 Panel 앱 게시** 대화 상자를 엽니다. 설정은 섹션별로 묶여 있습니다.
2. **디렉터리 설정**에서:
   - **앱 이름** — 목록에 표시되는 이름입니다.
   - **URL 슬러그** — 앱의 URL이자 내부 이름이므로 유효한 DNS 레이블이어야 합니다. 소문자, 숫자, 하이픈을 사용하고 문자로 시작하며 40자 이하여야 합니다(예: `sales-dashboard`). 대화 상자는 게시하기 전에 이를 확인합니다.
   - **메모** — 선택 사항인 설명입니다.
   - **프로젝트** — 앱을 소유하는 프로젝트입니다. 앱의 [브랜딩](/ko/guides/panel-apps/branding/)을 제공하며 앱 테이블의 기본 프로젝트가 됩니다. 게시 후에는 여기서 변경할 수 없으며 [할당](/ko/guides/panel-apps/branding/#기존-앱의-경우)을 사용하십시오.
3. **Git 연결 및 게시 감시기**에서:
   - **Git 연결** — 앱의 리포지토리를 보관하는 연결입니다.
   - **브랜치** — 빌드할 브랜치입니다. 이 브랜치에 푸시하면 앱이 자동으로 다시 빌드되고 재배포됩니다.
   - **진입점** — Panel이 제공해야 하는 `.py` 파일입니다(`app.py`).
4. **런타임**에서:
   - 앱 컨테이너가 요청할 **CPU**와 **메모리**.

     > 리소스(CPU/메모리)를 줄이면 앱이 더 빠르게 스케줄되고 콜드 스타트됩니다.

   - **디자인** — PlaidCloud의 현대적인 디자인은 **FAST**를, 앱의 CSS가 Panel 기본 스타일을 기대한다면 **기본값**을 선택합니다.
   - **유휴 시간(분)** — 트래픽이 없는 상태에서 앱이 0으로 축소되기 전까지 웜 상태로 유지되는 시간입니다. 기본값은 5분입니다.
   - **공개 액세스 허용** — 인증되지 않은 액세스를 허용하려면 선택합니다. 선택하지 않으면 보는 사람이 테넌트에 로그인해야 합니다.
5. **고급 (임베디드 서비스)** 섹션은 선택 사항입니다. 기본적으로 앱은 PlaidCloud 테넌트에서만 제공됩니다. 다른 사이트에 임베드하려면 **도메인 추가**를 클릭하고 앱을 로드할 수 있는 각 도메인을 한 행에 하나씩 입력하십시오. 스키마나 경로 없이 호스트만 입력합니다(예: `example.com` 또는 `app.example.com:8443`). 앱을 다른 곳에 임베드하는 경우가 아니면 목록을 비워 두십시오.
6. **게시**를 클릭합니다.

게시하면 앱이 **빌드**됩니다. **상태**가 목록에 표시되며 자동으로 업데이트됩니다. 각 상태의 의미, 앱이 준비된 후 여는 방법, 게시를 취소하지 않고 다시 빌드를 트리거하는 방법은 [Panel 앱 사용](/ko/guides/panel-apps/using/)을 참조하십시오.

> 앱의 URL은 빌드 상태가 **준비됨**이 된 후에만 작동하며, 유휴 상태 이후의 첫 요청은 앱을 시작하는 데 약 15초가 걸립니다.

### 고급: 로컬에서 PlaidCloud와 동일하게 구성

기술 사용자는 PlaidCloud가 사용하는 것과 같은 입력으로 앱을 빌드하고 테스트할 수 있습니다. 게시하거나 **다시 빌드**를 클릭하기 전에 할 수 있는 가장 가까운 로컬 검사입니다.

PlaidCloud는 선택한 git 브랜치에서 이 생성된 Dockerfile로 빌드합니다. 로컬에서도 같은 내용을 `Dockerfile.plaidcloud-panel`로 사용하십시오.

```dockerfile
FROM us-docker.pkg.dev/plaidcloud-build/panel-base/platform-panel-base:0.5.1
USER root
COPY . /app
RUN if [ -f /app/requirements.txt ]; then pip install --no-cache-dir -r /app/requirements.txt; fi
# If your entry point is in a subfolder, PlaidCloud also installs that folder's requirements.txt,
# after the root one (so a per-app pin wins). Replace <app-folder> with your entry point's folder,
# or drop this line if your app is at the repository root.
RUN if [ -f "/app/<app-folder>/requirements.txt" ]; then pip install --no-cache-dir -r "/app/<app-folder>/requirements.txt"; fi
USER 10001
```

서버 빌드와 일치시키려면:

1. **브랜치**에서 선택한 것과 같은 브랜치를 체크아웃합니다.
2. `COPY . /app`이 PlaidCloud와 일치하도록 리포지토리 루트에서 빌드를 실행합니다.
3. 선택적 종속성은 `requirements.txt`에 넣습니다. 리포지토리 루트 또는 진입점 옆에 둘 수 있습니다. 둘 다 설치되며 앱 폴더의 파일이 마지막에 설치됩니다(앱별 고정이 우선하도록).
4. **진입점**에서 선택한 것과 같은 진입점 경로를 사용합니다.

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

배포된 이미지는 기본 이미지의 진입점을 재정의하지 않습니다. PlaidCloud가 주입하는 환경 변수로 `panel serve`를 실행합니다. 같은 런타임 계약으로 빌드된 이미지를 테스트하십시오.

```sh
docker run --rm \
  --cpus 0.5 \
  --memory 512m \
  -p 5006:5006 \
  -e APP_PATH=/app/app.py \
  -e PANEL_PREFIX=/serve/local \
  -e PANEL_PORT=5006 \
  -e PANEL_ORIGIN=localhost:5006 \
  -e PANEL_KEEP_ALIVE_MS=25000 \
  -e PLAID_PANEL_DESIGN=fast \
  local-panel-app:plaidcloud
```

`http://localhost:5006/serve/local/`을 엽니다.

테스트할 때는 게시 대화 상자의 설정과 일치시키십시오.

- **진입점**은 `APP_PATH=/app/<entry-point>`에 대응합니다.
- **CPU**와 **메모리**는 Docker의 `--cpus` 및 `--memory` 제한에 대응합니다.
- **디자인: FAST**는 `PLAID_PANEL_DESIGN=fast`에 대응합니다.
- **디자인: 기본값**은 `PLAID_PANEL_DESIGN`을 생략한다는 뜻입니다.
- **유휴 시간(분)** 설정은 배포 환경의 축소 시간에 대응합니다. 로컬 Docker에서는 적용되지 않지만 앱은 여전히 같은 Panel 웹소켓 keepalive 및 세션 정리 설정을 사용합니다.
- **임베디드 서비스** 도메인은 `PANEL_ORIGIN`에 대응합니다. 호스트를 둘 이상 테스트해야 하면 공백으로 구분한 목록을 사용하십시오.

컨테이너가 필요하지 않다면 로컬 Python 환경에서 서비스 계층을 테스트할 수도 있습니다. 같은 `requirements.txt`를 설치하고 플랫폼 환경 변수를 설정한 다음 배포된 이미지가 사용하는 것과 같은 플래그로 `panel serve`를 실행합니다.

```sh
export APP_PATH=app.py
export PANEL_PREFIX=/serve/local
export PANEL_PORT=5006
export PANEL_ORIGIN=localhost:5006
export PANEL_KEEP_ALIVE_MS=25000
export PLAID_PANEL_DESIGN=fast

panel serve "$APP_PATH" \
  --address 0.0.0.0 \
  --port "$PANEL_PORT" \
  --prefix "$PANEL_PREFIX" \
  --allow-websocket-origin "$PANEL_ORIGIN" \
  --num-procs 1 \
  --keep-alive "$PANEL_KEEP_ALIVE_MS" \
  --unused-session-lifetime 15000 \
  --index "$(basename "$APP_PATH" .py)"
```

`http://localhost:5006/serve/local/`을 엽니다.

배포된 기본 모양과 일치시키려면 `PLAID_PANEL_DESIGN=fast`를 사용하십시오. 게시 대화 상자의 **기본값** 디자인 옵션을 테스트하려면 `PLAID_PANEL_DESIGN`을 설정하지 않고 같은 명령을 실행하십시오. `PANEL_PREFIX`, `PANEL_ORIGIN`, `--keep-alive`, `--unused-session-lifetime`은 그대로 두십시오. 이들은 배포된 런타임 계약의 일부입니다.

## WASM 앱 만들기

WASM 앱은 미리 빌드된 HTML 파일로 브라우저에서 실행됩니다.

1. **WASM 앱 추가**를 클릭하여 **서버리스 Panel 앱 게시** 대화 상자를 엽니다.
2. **앱 이름**과 **버전**을 입력합니다.
3. **앱 HTML 위치**를 선택합니다. 문서 계정에 있는 HTML 파일입니다.
4. **앱 URL 슬러그**와 선택 사항인 **메모**를 입력합니다.
5. **게시**를 클릭합니다. WASM 앱에는 빌드 단계가 없으며 즉시 제공됩니다.
