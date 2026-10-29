---
title: Panel 앱용 Data API
description: panel_data로 Panel 앱에서 PlaidCloud 테이블을 읽습니다. 로그인한 보는 사람의 권한으로 서버에서 필터링, 페이징, 개수 계산 및 집계를 수행하며 행 수준 보안이 적용됩니다.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/data-api.md
---

`plaidcloud.utilities.panel_data`는 서버 Panel 앱이 전체 테이블을 앱에 로드하지 않고 테이블을 읽는 방법입니다. 원하는 것, 즉 일부 필터와 일치하는 행, 그중 한 페이지, 개수, 그룹별 합계를 설명하면 PlaidCloud의 데이터베이스가 작업을 수행합니다. 결과만 앱으로 돌아옵니다.

모든 요청은 앱을 보는 사람의 권한으로 실행되므로, 그 사람의 프로젝트 권한과 [행 수준 보안](/ko/guides/panel-apps/accessing-data/)이 반환되는 모든 항목에 적용됩니다.

```python
from plaidcloud.utilities.panel_data import table

sales = table("sales")
```

`table(name)`은 앱의 프로젝트에 있는 테이블을 엽니다. 이 프로젝트는 앱이 게시될 때 [할당된](/ko/guides/panel-apps/branding/#앱을-프로젝트에-할당하기) 프로젝트입니다. 다른 프로젝트의 테이블을 읽으려면 `table("sales", project="Finance")`처럼 프로젝트를 전달하십시오. 프로젝트는 ID, 이름 또는 경로일 수 있습니다.

테이블 핸들은 절대 변하지 않습니다. `filter`는 새 핸들을 반환하므로 필터링되지 않은 핸들을 유지하면서 여기서 여러 뷰를 파생할 수 있습니다.

## 필터

```python
emea = sales.filter(region="EMEA", year=[2025, 2026])
```

각 키워드는 열 이름입니다. 단일 값은 그 값과 같은 행과 일치합니다. 리스트, 튜플 또는 세트는 구성원 중 하나와 같은 행과 일치합니다. 여러 키워드는 AND로 결합되며, 결과에 `filter`를 다시 호출하면 조건이 추가됩니다.

`None`, 빈 문자열 또는 빈 리스트 값은 해당 열을 필터링하지 않은 상태로 둡니다. 그래서 비어 있는 필터 위젯이 데이터를 그대로 두며, `sales.filter(**widget_values)`는 먼저 빈 값을 확인하지 않아도 작동합니다.

존재하지 않는 열을 지정하면 테이블과 열 이름을 알려 주는 오류가 발생합니다.

## 페이지

```python
rows = emea.page(1, 200, sort=["-amount"], key="id")
```

`page(n, size, sort, key)`는 `size`행으로 구성된 `n`번째 페이지(1부터 시작)를 pandas 데이터프레임으로 반환합니다.

- `sort`는 열 이름의 리스트입니다. 내림차순으로 정렬하려면 이름 앞에 `-`를 붙입니다(`["region", "-amount"]`).
- `key`는 테이블의 고유 열 또는 고유 열 리스트입니다. 항상 전달하십시오.

### 안정적인 페이징

페이징은 정렬된 행 목록의 조각을 가져옵니다. 각 요청은 별도의 쿼리입니다. 두 행이 정렬 열에서 동률이면 데이터베이스가 다음 요청에서 순서를 다르게 반환할 수 있으므로, 행이 두 조각에 나타나거나 어느 조각에도 나타나지 않을 수 있습니다. `key`가 이 틈을 메웁니다. PlaidCloud가 정렬 열 뒤에 이를 추가하므로 순서가 항상 완전하며 모든 행이 정확히 하나의 조각에 속합니다.

`key`가 없으면 페이징은 모든 열로 정렬하는 방식으로 대체됩니다. 열이 많은 테이블에서는 느리며 두 행이 동일하면 여전히 불안정합니다. 페이징할 때마다 고유 키를 전달하십시오. 같은 이유로 [`DataGrid`](/ko/guides/panel-apps/app-kit/#datagrid)에도 전달하십시오.

## 개수

```python
total_rows = emea.count()
```

필터와 일치하는 행의 개수를 정수로 반환합니다.

## 집계

```python
by_region = sales.aggregate(by=["region"], total=("amount", "sum"), orders=("id", "count"))
grand_total = emea.aggregate(total=("amount", "sum"))
```

`aggregate(by=(), limit=1000, **measures)`는 `by` 열로 정렬된 그룹당 하나의 행이 있는 데이터프레임을 반환합니다. 각 측정값은 `name=(column, function)`이며, 함수는 `sum`, `count`, `avg`, `min` 또는 `max`입니다. 측정값이 하나 이상 필요합니다.

`by`가 없으면 필터링된 행에 대한 합계가 한 행으로 반환됩니다. `limit`은 반환되는 그룹 수를 제한합니다.

Decimal 열은 문자열로 도착할 수 있습니다. 차트를 그리거나 서식을 지정하기 전에 `float(...)` 또는 `astype(float)`으로 변환하십시오.

## 종합하기

```python
import panel as pn
import plaidcloud_panel as pcp
from plaidcloud.utilities.panel_data import table

pn.extension("tabulator")

orders = table("orders")
bar = pcp.FilterBar(orders, "status")

pcp.App(
    "Orders",
    sidebar=[bar],
    main=[
        pcp.KpiCard("Open value", bar.table, "amount"),
        pn.bind(lambda t: pcp.DataGrid(t, key="order_id"), bar.table),
    ],
).servable()
```

`FilterBar`, `KpiCard`, `DataGrid`는 모두 이러한 테이블 핸들을 받으므로 대부분의 앱은 `page`, `count` 또는 `aggregate`를 직접 호출하지 않습니다. 직접 뷰를 만들 때 사용하십시오. [Panel 앱 키트](/ko/guides/panel-apps/app-kit/)를 참조하십시오.

## 관련 항목

- [데이터 읽기 및 로그인한 사용자](/ko/guides/panel-apps/accessing-data/) — 보는 사람으로 연결하는 방법과 `PlaidConnection`을 직접 사용해야 하는 경우.
