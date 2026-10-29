---
title: 데이터 읽기 및 로그인한 사용자
description: 서버 측 Panel 앱을 앱을 보는 사람의 권한으로 PlaidCloud에 연결하여 프로젝트 데이터를 읽고, 사용자별 동작과 행 수준 보안에 보는 사람의 ID를 사용합니다.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/accessing-data.md
---

서버 Panel 앱은 PlaidCloud 데이터를 읽을 수 있으며, 이때 **앱을 보는 사람의 권한으로** 읽습니다. 누군가 앱을 열면 PlaidCloud가 플랫폼의 나머지 부분에서 사용하는 것과 동일한 싱글 사인온으로 그 사람을 로그인시키고, 앱이 수행하는 모든 호출은 **보는 사람 본인의 권한**으로 실행됩니다. 공유 서비스 계정은 없으며, 앱은 보는 사람이 직접 볼 수 없는 데이터를 절대 볼 수 없습니다.

이는 **서버** 앱에만 적용됩니다. WASM 앱은 전적으로 브라우저에서 실행되며 서버 측 연결이 없습니다.

## PlaidCloud에 연결하기

읽으려는 데이터가 있는 프로젝트를 지정하여 `PlaidConnection`을 사용합니다.

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection(project_id="<your-project-id>")
```

설정은 이것이 전부입니다. 토큰, 사용자 이름 또는 비밀번호를 제공할 필요가 **없습니다**. 연결은 로그인한 사용자로 자동 인증됩니다. 프로젝트의 ID는 프로젝트의 URL이나 설정 페이지에서 확인할 수 있습니다.

> **프로젝트를 지정하십시오.** **프로젝트** 선택기에서 프로젝트를 지정하여 게시한 앱은 기본적으로 해당 프로젝트를 읽으며, [Data API](/ko/guides/panel-apps/data-api/)는 `table("name")`에 해당 프로젝트를 사용합니다. 프로젝트가 없는 앱의 경우 위와 같이 `PlaidConnection`에 `project_id`를 전달하십시오. 인수 없는 `PlaidConnection()`에는 읽을 프로젝트가 없습니다.

### 테이블 읽기

연결을 사용하여 이름으로 테이블을 pandas DataFrame으로 가져옵니다.

```python
df = conn.get_dataframe("Sales Ledger")
```

연결이 곧 보는 사람이므로 보는 사람이 볼 수 있는 행만 반환되며, 프로젝트에 대한 액세스 권한이 전혀 없으면 권한 오류가 발생합니다.

> **SQL을 작성하지 말고 이름으로 테이블을 읽으십시오.** 관리자가 [행 액세스](/ko/administration/access/managing-security-groups-and-assignments/#행-액세스와-직접-작성한-쿼리)를 켠 프로젝트에서는 이름으로 읽으면 각 보는 사람의 행 권한이 적용되지만, 앱이 직접 작성한 쿼리는 프로젝트 아키텍트가 아닌 사용자에게는 거부됩니다. 권한이 필터링할 단일 테이블이 없기 때문입니다. 이름으로 읽으면 어느 경우든 앱이 계속 작동합니다.

## 보는 사람 식별하기

개인화된 인사말, 탭 숨기기, 행 수준 보안처럼 **누가 보고 있는지**에 맞게 앱이 표시하는 내용을 조정하려면 Panel에서 로그인한 사용자를 읽습니다.

```python
import panel as pn

viewer = pn.state.user          # the viewer's email address
token  = pn.state.access_token  # their JWT, if you need claims or group membership
```

`pn.state.user`는 검증된 로그인에서 가져온 보는 사람의 이메일이므로 신원으로 신뢰할 수 있습니다. `pn.state.access_token`은 원시 액세스 토큰이며, 더 세밀한 규칙을 위해 그룹 또는 역할 클레임을 디코딩해야 할 때 유용합니다.

### 행 수준 보안

두 가지를 결합합니다. 보는 사람을 읽은 다음 모든 쿼리를 그 사람으로 필터링합니다. 예를 들어 각 지역 관리자에게 자신의 지역만 표시하려면 다음과 같이 합니다.

```python
import panel as pn
from plaidcloud.utilities.connect import PlaidConnection

pn.extension()

viewer = pn.state.user
conn = PlaidConnection(project_id="<your-project-id>")

sales = conn.get_dataframe("Regional Sales")
mine = sales[sales["manager_email"] == viewer]

pn.Column(
    f"# Sales for {viewer}",
    pn.pane.DataFrame(mine, index=False),
).servable()
```

연결이 이미 보는 사람의 프로젝트 권한을 적용하므로 이 필터링은 볼 수 있는 항목 위에 *추가로* 가공하는 것이며, PlaidCloud 자체 액세스 제어를 대체하지 않습니다.

> **앱의 주 흐름에서 데이터를 호출하십시오.** 로그인한 사용자는 앱 코드가 해당 세션에 대해 실행되는 동안(`.servable()` 작업이 수행되는 곳) 사용할 수 있습니다. 차단 호출을 백그라운드 스레드로 넘기는 경우 `asyncio.to_thread`를 사용하십시오. 원시 스레드 풀은 세션의 ID를 전달하지 않으며, 연결은 잘못된 데이터를 읽는 대신 오류를 발생시킵니다.

## 공개 앱

**공개 액세스 허용**을 선택하여 게시하면 앱이 로그인 없이 제공되므로 대신 동작할 보는 사람이 없습니다. `pn.state.user`는 비어 있고 `PlaidConnection()`은 인증할 대상이 없습니다. 공개 앱에는 누구에게나 안전한 데이터만 사용하거나, 공개 액세스를 끄고 보는 사람이 로그인하여 위의 사용자별 모델이 적용되도록 하십시오.
