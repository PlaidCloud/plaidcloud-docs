---
title: Panel 앱 키트
description: plaidcloud_panel 키트로 PlaidCloud처럼 보이는 Panel 앱을 빌드합니다. App 셸, 명령 팔레트, FilterBar, KpiCard, DataGrid, Chart, Form, 실행 버튼, 저장된 설정, 인쇄 및 번역을 라이트 모드와 다크 모드에서 제공합니다.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

모든 서버 Panel 앱에는 `plaidcloud_panel` 키트가 설치되어 있습니다. 이 키트는 앱에 PlaidCloud의 모양, 즉 플랫폼의 나머지 부분과 동일한 색상, 글꼴, 간격을 라이트 모드와 다크 모드로 제공하며, 대부분의 앱에 필요한 화면(필터, 주요 수치, 대용량 데이터 그리드, 차트, 양식)을 위한 기성 구성 요소를 제공합니다. 앱은 [프로젝트의 브랜딩](/ko/guides/panel-apps/branding/)을 자동으로 가져옵니다.

```python
import plaidcloud_panel as pcp
```

키트를 가져오면 Plotly 및 Matplotlib 차트에도 PlaidCloud 스타일이 적용됩니다.

## 템플릿에서 시작하기

키트에는 동작하는 시작용 앱을 작성하는 명령이 포함되어 있습니다. 아무 폴더에서나 실행한 다음 테이블 및 열 이름을 편집하십시오.

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| 옵션 | 기능 |
|---|---|
| `--layout dashboard` | 사이드바의 필터, 주요 수치 두 개, 차트 하나. |
| `--layout explorer` | 사이드바의 필터, 행 개수, 행 테이블. |
| `--table` | 앱이 읽는 PlaidCloud 테이블. |
| `--filters` | 필터링할 열을 쉼표로 구분한 목록. 첫 번째 열이 차트를 구동합니다. |
| `--measure` | 합산할 숫자 열. |
| `--dir` | `app.py`와 `requirements.txt`를 쓸 위치. 기본값은 현재 폴더입니다. |

`app.py`가 이미 있으면 명령은 아무것도 쓰지 않고 중지됩니다. 두 파일을 리포지토리에 커밋하고 [앱을 게시](/ko/guides/panel-apps/creating/)하십시오.

## 예제 앱

이 앱은 판매 테이블을 지역과 연도로 필터링하고, 주요 수치 두 개, 차트, 일치하는 행의 페이징 그리드를 표시합니다. 그리드는 금액을 천 단위 구분 기호와 함께, 마진을 백분율로 표시합니다. 모든 구성 요소가 필터를 따릅니다.

```python
import panel as pn
import plaidcloud_panel as pcp
from bokeh.plotting import figure
from plaidcloud.utilities.panel_data import table

pn.extension("tabulator")

sales = table("sales")
bar = pcp.FilterBar(sales, "region", "year")


def by_region(t):
    df = t.aggregate(by=["region"], total=("amount", "sum"))
    regions = df["region"].astype(str).tolist()
    fig = figure(x_range=regions, height=320, toolbar_location=None)
    fig.vbar(x=regions, top=df["total"].astype(float).tolist(), width=0.8, color=pcp.series()[0])
    return fig


def grid(t):
    return pcp.DataGrid(t, key="id", totals={"amount": "sum"}, formats={"amount": "0,0", "margin": "0.0%"})


pcp.App(
    "Sales",
    sidebar=[bar],
    main=[
        pn.Row(
            pcp.KpiCard("Total amount", bar.table, "amount"),
            pcp.KpiCard("Orders", bar.table),
        ),
        pcp.Chart(pn.bind(by_region, bar.table), title="Amount by region"),
        pcp.Section("Orders", pn.bind(grid, bar.table)),
    ],
).servable()
```

패턴은 모든 키트 앱에서 동일합니다. 테이블에 대해 `FilterBar`를 만든 다음 각 뷰를 `bar.table`에 바인딩합니다. `bar.table`(또는 위젯)에 바인딩되지 않은 뷰는 필터가 변경되어도 새로 고쳐지지 않습니다.

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)`는 앱 셸을 빌드합니다. 제목, 프로젝트 로고, 로그인한 사용자가 표시되는 헤더와 사이드바, 주 영역으로 구성됩니다. 결과에 `.servable()`을 호출하십시오.

- **탐색** — `nav=[("Overview", overview_page), ("Detail", detail_page)]`를 전달하면 사이드바 상단에 페이지 메뉴가 생깁니다. 각 페이지는 Panel 객체이거나 이를 반환하는 함수입니다. 함수는 페이지를 선택할 때 실행됩니다.
- **테마** — 앱은 라이트 테마로 열립니다. 다크 테마로 열려면 `theme="dark"`를 전달하거나 URL에 `?theme=dark`를 추가하십시오. `theme_toggle=True`(기본값)이면 헤더에 라이트/다크 전환 스위치가 표시됩니다.
- **브랜딩** — 앱은 세션이 시작될 때 프로젝트의 브랜드 색상과 로고를 읽습니다. 브랜딩이 없는 프로젝트는 PlaidCloud 기본값을 사용합니다.
- **명령 팔레트** — Ctrl-K(Mac에서는 Cmd-K)를 눌러 명령을 검색하고 실행합니다. `nav`의 모든 페이지가 페이지 이름으로 **이동**으로 나열되며, `commands={"Refresh data": refresh}`는 사용자 정의 항목을 추가합니다. 각 항목은 레이블과 인수가 없는 함수입니다. 항목을 선택하면 앱이 실행합니다.
- **첫 실행 둘러보기** — `tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]`는 짧은 단계별 소개를 표시하며, 각 단계는 제목과 한 줄 텍스트로 구성됩니다. 완료하거나 건너뛸 때까지 페이지 상단에 나타나며 이후에는 다시 표시되지 않습니다.
- **그 밖의 항목** — 다른 키워드 인수는 Panel의 `FastListTemplate`으로 전달됩니다.

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))`는 지정한 각 열마다 검색 가능한 다중 선택 상자를 하나씩 만들고 해당 열의 고유 값(최대 1,000개, 목록이 잘리면 알림 표시)을 나열합니다. 선택된 항목이 없으면 상자에 **모두**가 표시됩니다. 그 밖의 항목에는 열 이름으로 직접 만든 위젯을 전달하십시오.

- `bar.table`은 현재 선택으로 좁혀진 테이블입니다. 비어 있는 위젯은 데이터를 좁히지 않습니다.
- 선택 항목은 페이지 URL(`?region=EU`)에 저장되므로 필터링된 뷰를 링크로 공유할 수 있습니다.

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)`는 주요 수치 하나를 표시합니다. `fn`은 `sum`, `count`, `avg`, `min` 또는 `max`이며 서버가 전체 테이블에 대해 계산합니다. `column`이 없으면 행 개수를 표시합니다. 수치가 필터를 따르도록 소스로 `bar.table`을 전달하십시오.

`drill_to=grid`(`DataGrid`)를 전달하면 수치 아래에 **View rows** 버튼이 추가됩니다. 이 버튼을 선택하면 그리드가 카드 자체의 테이블을 가리켜, 그리드에 수치의 근거가 되는 행이 나열됩니다.

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})`는 어떤 크기의 데이터든 표시하는 테이블 뷰입니다. 현재 페이지만 브라우저로 전송되며, 페이징, 정렬, 합계 및 내보내기는 모두 서버에서 실행됩니다.

- **페이징** — 페이지당 200, 500 또는 1,000행이며 이전 및 다음 버튼과 행 카운터가 있습니다.
- **정렬** — 열 머리글을 클릭합니다. 정렬은 보이는 페이지뿐 아니라 전체 테이블에 적용됩니다.
- **합계** — `totals`는 열을 `sum`, `count`, `avg`, `min` 또는 `max`에 매핑합니다. 서버가 일치하는 모든 행에 대해 각각을 계산하고 결과를 그리드의 마지막 행으로 고정합니다.
- **내보내기** — **CSV** 및 **XLSX** 버튼은 일치하는 모든 행을 현재 정렬 순서로 최대 `export_cap`행(기본값 100,000)까지 다운로드합니다. 테이블이 더 크면 필터를 좁히라는 알림이 표시됩니다. `=`, `+`, `-` 또는 `@`로 시작하는 텍스트 셀에는 스프레드시트가 텍스트로 읽도록 앞에 작은따옴표가 붙습니다.
- **숫자 형식** — `formats={"margin": "0.0%", "amount": "0,0"}`는 [numbro](https://numbrojs.com/format.html) 형식 문자열을 사용하여 열별 표시 형식을 설정합니다. `%` 형식은 100을 곱합니다. 합계 행도 동일한 형식을 사용합니다. 형식이 없는 부동 소수점 열은 천 단위 구분 기호와 함께 최대 소수점 두 자리까지 표시됩니다. **복사**, **CSV** 및 **XLSX**는 원시 값을 유지합니다.
- **키** — `key`는 행을 고유하게 식별하는 열 또는 열 목록입니다. 항상 전달하십시오. [안정적인 페이징](/ko/guides/panel-apps/data-api/#안정적인-페이징)을 참조하십시오.

- **그룹화 기준** — `group_by=["region"]`은 그룹당 하나의 행을 표시하며, `totals` 측정값과 `rows` 개수는 모두 서버가 계산하고, 일치하는 모든 행에 대한 **합계** 행이 표시됩니다. `groupable=["region", "year"]`를 전달하면 보는 사람이 열을 선택할 수 있는 **그룹화 기준** 선택기가 추가됩니다. 그리드는 최대 1,000개 그룹을 표시하며 목록이 잘리면 알려 줍니다. 그룹 행에는 **열기** 링크가 없습니다.
- **조건부 서식** — `rules`는 값에 따라 셀에 색을 지정합니다. 각 규칙은 `column`, `op`(`>`, `>=`, `<`, `<=`, `==`, `!=` 또는 `between`), `value`(`between`의 경우 `[low, high]`) 및 `token`(`success`, `warning`, `error` 또는 `info`)을 지정합니다. 예: `{"column": "margin", "op": "<", "value": 0, "token": "error"}`. 합계 행에는 색이 지정되지 않습니다.
- **복사** — **복사** 버튼은 표시된 열과 합계 행을 포함한 현재 페이지를 Excel에 붙여 넣을 수 있는 탭으로 구분된 텍스트로 클립보드에 넣습니다.
- **Open in PlaidCloud** — 소스가 PlaidCloud 테이블이면 **Open in PlaidCloud** 링크가 해당 테이블을 엽니다.
- **저장된 열 레이아웃** — `layout_key="orders"`는 열을 선택하고 순서를 정하며 일부를 고정하기 위한 **열** 및 **Pinned** 선택기를 추가합니다. 각 보는 사람의 선택은 해당 이름으로 저장되며 다음에 앱을 열 때 복원됩니다.
- **행 링크** — `row_link`는 행을 사전으로 받아 웹 주소를 반환하거나, 링크가 없으면 `None`을 반환하는 함수입니다. 그리드는 링크가 있는 각 행에 링크가 포함된 **열기** 열을 추가합니다. `http` 및 `https` 주소와 같은 사이트의 경로만 링크됩니다.
- **새로 고침** — `grid.refresh()`는 동일한 소스를 다시 쿼리하고 페이지, 정렬 및 그룹화를 유지합니다. [실행](#실행-버튼-및-최신-상태)이 테이블 쓰기를 마친 후 호출하십시오.

`source`는 테이블 이름 또는 [Data API](/ko/guides/panel-apps/data-api/)의 테이블입니다. 그리드를 다시 필터링하려면 `grid.source`를 필터링된 테이블로 설정하거나 예제처럼 `bar.table`에서 새 그리드를 빌드하십시오.

그리드에는 보는 사람의 행 수준 보안이 적용됩니다. 그리드는 보는 사람 본인의 연결을 통해 읽습니다.

## Chart

`pcp.Chart(obj, title=None, height=320)`는 제목이 있는 카드에 차트를 넣습니다. `obj`는 Bokeh figure, hvPlot 또는 HoloViews 플롯, Plotly figure, Matplotlib figure 또는 이 중 하나를 반환하는 `pn.bind(...)`일 수 있습니다. Bokeh figure의 숫자 축에는 천 단위 구분 기호가 표시되어 800000이 800,000으로 읽힙니다.

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")`는 입력 위젯을 제출 버튼이 있는 하나의 양식으로 배치합니다. `form.values()`는 이름이 있는 모든 위젯에 대해 `{widget.name: widget.value}`를 반환하며, 버튼을 클릭하면 `on_submit`이 해당 사전을 받습니다.

## Section, Card, Tabs 및 Loading

| 구성 요소 | 용도 |
|---|---|
| `pcp.Section(title, *objects)` | 페이지 배경 위에 바로 놓이는 제목이 있는 그룹. |
| `pcp.Card(title, *objects)` | 도드라진 면 위의 제목이 있는 그룹. |
| `pcp.Tabs(Overview=obj, Detail=obj)` | 탭을 선택할 때 탭의 콘텐츠를 로드하는 탭. 활성 탭에는 브랜드 색상이 적용됩니다. |
| `pcp.Loading(height=200)` | 데이터를 로드하는 동안 표시하는 반짝이는 자리 표시자. |

## StatusBanner

`pcp.StatusBanner(message, kind="info")`는 인라인 알림을 표시합니다. `kind`는 `error`, `warning`, `success` 또는 `info`입니다.

## 실행 버튼 및 최신 상태

`pcp.run_workflow_button(workflow_id, label=None)`은 앱을 연 사람의 권한으로 PlaidCloud 워크플로를 실행하는 버튼을 추가하며, **Running…**, 이어서 **완료** 또는 **실패**를 표시합니다. 실패하면 실패한 단계의 이름을 최대 다섯 개까지 알려 줍니다. `project_id`를 전달하지 않으면 워크플로는 앱의 프로젝트에 속합니다.

`pcp.RunButton(label, start, status)`은 모든 작업에 대해 동일하게 동작합니다. `start`는 작업을 시작하고 실행 ID를 반환하며, `status(run_id)`는 `"running"`, `"succeeded"` 또는 `"failed"`를 반환하거나, 이유를 표시하려면 `("failed", reason)`을 반환합니다. 둘 다 REST API 호출 같은 일반 함수입니다. 버튼의 `runs` 값은 실행이 성공할 때마다 1씩 증가하므로, 이후에 새로 고쳐야 하는 뷰는 이 값에 바인딩합니다.

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)`는 테이블이 마지막으로 기록된 시점을 **Updated 5 min ago**로 표시합니다. 페이지가 열려 있는 동안 경과 시간이 갱신됩니다. 더 오래된 데이터를 경고로 표시하려면 `stale_after=datetime.timedelta(hours=24)`를 전달하고, 실행 후에는 `.refresh()`를 호출하십시오. 날짜를 알 수 없는 테이블은 **Last update unknown**으로 표시되며 이는 오류가 아닙니다. `pcp.Freshness(fetch)`는 모든 소스에 대해 동일하게 동작하며, `fetch`는 데이터가 마지막으로 변경된 시점을 반환합니다.

## 저장된 설정

`pcp.user_state`는 방문 사이에 각 사람의 선택을 기억하므로 앱이 그 사람이 나갔을 때의 상태로 열립니다.

- `pcp.user_state.persist(widget, "region")`는 저장된 값을 위젯에 복원하고 변경될 때마다 저장합니다. 위젯이 더 이상 제공하지 않는 저장된 값은 무시됩니다.
- `nav`에서 선택한 페이지는 자동으로 저장됩니다.
- `pcp.user_state.persist(widget, "filters.region")`처럼 `filters.`로 시작하는 키는 필터 선택을 보관합니다. PlaidCloud는 읽을 때마다 이를 해당 사람의 현재 행 액세스에 맞게 정리하므로, 저장된 필터가 더 이상 볼 수 없는 값을 되살리지 않습니다.
- `pcp.user_state.get(key, default)`와 `pcp.user_state.set(key, value)`는 그 밖의 작은 값을 저장합니다.

저장된 설정은 한 앱에서 한 사람에게 속하며 최대 8KB입니다. 설정은 사람 사이에 공유되지 않습니다. 설정을 저장할 때 PlaidCloud에 연결할 수 없으면 앱은 세션이 끝날 때까지 설정을 유지합니다.

## 인쇄 및 PDF로 저장

`pcp.PrintButton()`은 브라우저의 인쇄 대화 상자를 열며, 대상으로 **PDF로 저장**을 선택할 수 있습니다. 페이지는 사이드바와 컨트롤이 숨겨지고 프로젝트의 브랜드가 적용된 상태로 인쇄됩니다. 각 `DataGrid`는 현재 페이지 전체를 최대 1,000행까지 인쇄하며 합계 행이 마지막에 옵니다. 다크 앱은 라이트 팔레트로 인쇄됩니다.

## 언어

버튼, 알림, 명령 팔레트, 둘러보기, 실행 및 최신 상태 메시지, 그리드 바닥글 등 키트 자체의 텍스트는 영어, 독일어 또는 프랑스어로 표시됩니다. 언어는 페이지 주소의 `?lang=de` 또는 `?lang=fr`이며, 지정하지 않으면 브라우저의 언어를 따릅니다. 숫자는 해당 언어의 구분 기호를 사용합니다. 데이터, 열 이름 및 직접 작성한 레이블은 번역되지 않습니다.

## 성능 예산

첫 페인트에 3,000ms보다 오래 걸리거나 2,000ms보다 느린 쿼리를 실행하는 페이지 로드는 초과한 항목을 지정하는 경고를 앱 로그에 기록합니다. 동일한 수치가 [Panel Studio](/ko/guides/panel-apps/studio/#인사이트)의 **인사이트** 탭에도 표시됩니다. 앱에 다른 한도를 설정하려면 다음 환경 변수를 설정하십시오.

| 변수 | 기본값 | 설정 내용 |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | 첫 페인트까지의 밀리초. |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | 쿼리 하나의 밀리초. |

정수가 아닌 값은 무시되며 기본값이 적용됩니다.

## 직접 만드는 차트의 색상

`pcp.series()`는 PlaidCloud 차트 팔레트를 순서대로 색상 목록으로 반환합니다. 직접 그리는 차트가 예제의 막대 차트처럼 키트 자체의 구성 요소와 일치하도록 이를 사용하십시오.

## 다음 단계

- [Data API](/ko/guides/panel-apps/data-api/) — 앱에서 PlaidCloud 테이블을 필터링, 페이징, 개수 계산 및 집계합니다.
- [알림 및 다이제스트](/ko/guides/panel-apps/alerts-and-digests/) — 앱에서 KPI 알림과 예약된 요약을 보냅니다.
- [프로젝트 브랜딩](/ko/guides/panel-apps/branding/) — 프로젝트의 모든 앱에 대해 색상과 로고를 한 번에 설정합니다.
