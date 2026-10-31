---
title: Dash 앱에서 데이터와 로그인한 사용자 읽기
description: Dash 앱을 앱을 보는 사람의 권한으로 PlaidCloud에 연결합니다. 프로젝트 데이터를 읽고, 보는 사람의 ID를 사용해 사용자별 동작과 행 수준 보안을 구현합니다.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/accessing-data.md
---

Dash 앱은 PlaidCloud 데이터를 읽을 수 있으며, 서버 Panel 앱과 마찬가지로 **앱을 보는 사람의 권한으로** 읽습니다. 누군가 앱을 열면 PlaidCloud는 플랫폼의 다른 부분에서 사용하는 것과 동일한 싱글 사인온으로 해당 사용자를 로그인시키며, 앱이 수행하는 모든 호출은 **그 사용자 본인의 권한**으로 실행됩니다. 공유 서비스 계정이 없으므로 앱은 보는 사람이 직접 볼 수 없는 데이터를 절대 볼 수 없습니다.

도우미 함수는 Dash 기본 이미지에 포함된 `plaidcloud_dash`에 있습니다.

```python
from plaidcloud_dash import current_user, get_connection
```

## PlaidCloud에 연결

Dash 콜백 내부에서 `get_connection()`을 호출하고, 읽으려는 데이터가 있는 프로젝트를 지정합니다.

```python
from plaidcloud_dash import get_connection

conn = get_connection(project_id="<your-project-id>")
```

필요한 설정은 이것이 전부입니다. 토큰, 사용자 이름 또는 비밀번호를 제공할 필요가 **없습니다**. `get_connection()`은 현재 세션의 액세스 토큰을 사용해 로그인한 사용자로 자동 인증합니다. 프로젝트 ID는 프로젝트의 URL이나 설정 페이지에서 확인할 수 있습니다.

> **콜백 내부에서 호출하십시오.** `get_connection()`은 현재 요청의 Flask 세션에서 사용자의 토큰을 읽는데, 이 세션은 콜백이 해당 사용자의 요청을 처리하는 동안에만 사용할 수 있습니다. 차단 호출을 백그라운드 스레드로 넘기는 경우 원시 스레드 풀은 세션을 전달하지 않으므로, 콜백 내부에서 토큰을 읽어 명시적으로 전달하십시오. 요청 밖에서(또는 인증이 비활성화된 상태에서) `get_connection()`을 호출하면 ID가 없는 연결을 조용히 반환하는 대신 `RuntimeError`가 발생합니다.

> **코드에서 프로젝트를 지정하십시오.** 게시 대화 상자에는 프로젝트 설정이 없습니다. Dash 앱은 서버 Panel 앱의 `PlaidConnection(project_id=...)`와 마찬가지로 `get_connection(project_id=...)`에서 지정한 프로젝트를 읽습니다. 자세한 내용은 [데이터와 로그인한 사용자 읽기](/ko/guides/panel-apps/accessing-data/)를 참조하십시오. 프로젝트 데이터를 전혀 다루지 않는 앱(예를 들어 `current_user()`만 호출하는 앱)에서는 `project_id` 없이 `get_connection()`만 호출해도 됩니다. 하지만 실제로 액세스할 수 있는 프로젝트 ID 없이 해당 연결에서 프로젝트 범위 작업을 호출하면 `Project Id has not been set` 오류가 발생합니다. (둘 이상의 프로젝트에서 읽으려면 프로젝트마다 연결을 여십시오.)

### 테이블 읽기

연결을 만든 후에는 이름으로 테이블을 pandas DataFrame에 가져올 수 있습니다.

```python
df = conn.get_dataframe("Sales Ledger")
```

연결이 곧 보는 사람이므로 이 호출은 보는 사람이 볼 수 있는 행만 반환하며, 프로젝트에 대한 액세스 권한이 전혀 없으면 권한 오류가 발생합니다.

> **SQL을 직접 작성하지 말고 이름으로 테이블을 읽으십시오.** 관리자가 [행 액세스](/ko/administration/access/managing-security-groups-and-assignments/#행-액세스와-직접-작성한-쿼리)를 켠 프로젝트에서 이름으로 읽으면 각 사용자의 행 권한이 적용되지만, 앱이 직접 구성한 쿼리는 프로젝트 아키텍트가 아닌 모든 사용자에 대해 거부됩니다. 권한을 적용할 단일 테이블이 없기 때문입니다. 이름으로 읽으면 어느 쪽이든 앱이 계속 작동합니다.

## 가져오기 시점이나 프로세스 범위가 아닌 콜백에서 읽기

하나의 프로세스가 모든 사용자에게 서비스를 제공합니다. 데이터 격리를 올바르게 구현하려면 두 가지 규칙을 지켜야 합니다.

- **모듈 범위(가져오기 시점)에서 연결을 열거나 테이블을 읽지 마십시오.** `app.py`와 이 파일이 가져오는 모든 모듈은 컨테이너가 시작될 때, 즉 누구도 로그인하기 전에 **한 번** 실행됩니다. 여기에서 `get_connection()` 또는 `PlaidConnection()`을 호출하면 인증할 사용자가 없어 부팅 시 앱이 실패합니다(이는 "앱이 시작되지 않음" 크래시 루프의 가장 흔한 원인입니다). 모든 읽기는 사용자의 요청과 세션 토큰이 존재하는 콜백 내부에서 수행하십시오.

- **사용자별 결과를 모듈 또는 프로세스 범위에 캐시하지 마십시오.** 스레드 방식의 gunicorn 워커는 동시에 접속한 모든 사용자에 걸쳐 하나의 Python 프로세스를 공유하므로, 모듈 수준 변수, 전역 딕셔너리 또는 `lru_cache`에 저장한 DataFrame은 *다른 모든* 사용자에게 보입니다. 즉 한 사람의 행이 다른 사람의 화면에 노출됩니다. 사용자별 데이터는 콜백 내부에서 계산하고 콜백이 반환되면 범위를 벗어나도록 두십시오.

  ```python
  # WRONG — a module/process-global cache is shared across all viewers
  _CACHE = {}

  @app.callback(...)
  def _load(n):
      viewer = current_user()
      if viewer not in _CACHE:                      # still process-global; leaks under load
          _CACHE[viewer] = get_connection(project_id="…").get_dataframe("Sales")
      return _CACHE[viewer].to_dict("records")

  # RIGHT — read inside the callback, no shared state
  @app.callback(...)
  def _load(n):
      conn = get_connection(project_id="…")          # this viewer, this request
      return conn.get_dataframe("Sales").to_dict("records")
  ```

### 공유 참조 데이터

여러 사용자가 조회 테이블이나 제품 목록처럼 *동일한* 참조 데이터를 실제로 필요로 한다면, 프로세스 수준 캐시로 공유하려 하지 마십시오. 대신 PlaidCloud의 일반적인 [행 액세스 / 프로젝트 권한](/ko/administration/access/managing-security-groups-and-assignments/)을 통해 앱 사용자에게 해당 테이블을 부여하고, 각 사용자가 자신의 `get_connection()`으로 읽도록 하십시오. 모든 사용자가 동일한 액세스 권한을 부여받았기 때문에 동일한 참조 행을 얻는 것이며, 한 사용자의 읽기 결과를 다른 사용자에게 재사용하기 때문이 아닙니다.

## 보는 사람 식별

개인화된 인사말, 탭 숨기기, 행 수준 보안처럼 **누가 보고 있는지**에 맞게 앱이 표시하는 내용을 조정하려면 `current_user()`를 호출하십시오.

```python
from plaidcloud_dash import current_user

viewer = current_user()  # the viewer's identifier
```

`current_user()`는 로그인한 사용자의 식별자를 반환합니다. 사용자 이름을 우선 사용하고, 사용자 이름 클레임이 없으면 이메일, 그다음 계정 ID 순으로 대체하며, 검증된 로그인 정보에서 가져오므로 해당 사용자의 ID로 신뢰할 수 있습니다. 이 함수는 예외를 발생시키지 않으며, 인증이 비활성화된 상태나 요청 밖에서 호출하면 빈 문자열을 반환합니다.

### 행 수준 보안

두 가지를 결합하십시오. 보는 사람을 확인한 다음 모든 쿼리를 해당 사용자로 필터링합니다. 예를 들어 각 지역 관리자에게 자신의 지역만 표시하려면 다음과 같이 합니다.

```python
from dash import Input, Output
from plaidcloud_dash import current_user, get_connection


@app.callback(Output("sales-table", "children"), Input("load-btn", "n_clicks"))
def _load_my_region(n_clicks):
    viewer = current_user()
    conn = get_connection(project_id="<your-project-id>")

    sales = conn.get_dataframe("Regional Sales")
    mine = sales[sales["manager_email"] == viewer]

    return mine.to_dict("records")
```

연결이 이미 사용자의 프로젝트 권한을 적용하므로 이 필터링은 사용자가 볼 수 있는 범위 위에 *추가로* 결과를 다듬는 것이며, PlaidCloud 자체 액세스 제어를 대체하지 않습니다.

## 공개 앱

**공개 액세스 허용**을 선택하고 게시한 경우 앱은 로그인 없이 제공되므로 대신 동작할 사용자가 없습니다. `current_user()`는 빈 문자열을 반환하고 `get_connection()`은 인증에 사용할 세션 토큰이 없어 예외를 발생시킵니다. 공개 앱에서는 누구에게나 안전한 데이터만 사용하거나, 공개 액세스를 끄고 사용자가 로그인하도록 하여 위에서 설명한 사용자별 모델이 적용되게 하십시오.
