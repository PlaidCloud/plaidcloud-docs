---
title: 명령줄
description: PlaidCloud 명령줄 인터페이스를 사용하여 작업을 자동화하고, 스크립트를 실행하고, 터미널에서 PlaidCloud 리소스를 다루는 방법을 설명합니다.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloud에는 HTTP 요청을 보낼 수 있는 모든 애플리케이션에서 사용할 수 있는 REST API가 있습니다. 더 쉽게 사용할 수 있도록 `plaidcloud-rpc` Python 패키지가 연결 및 요청 세부 정보를 대신 처리합니다.

:::caution[JSON-RPC는 더 이상 사용되지 않음]
JSON-RPC는 더 이상 사용되지 않으며 향후 릴리스에서 제거됩니다. 호출을 REST API로 보내는 `plaidcloud-rpc` 1.25.0 이상을 사용하고, 새 통합은 REST API를 기준으로 작성하십시오. [JSON-RPC는 더 이상 사용되지 않음](#json-rpc는-더-이상-사용되지-않음)을 참조하십시오.
:::


## 필수 설치

터미널에서 다음 명령을 실행하십시오.

```bash
pip install "plaidcloud-rpc>=1.25.0"
```


## SimpleRPC 객체를 사용하여 요청하기

`plaidcloud-rpc` 패키지로 요청하려면 `SimpleRPC` 객체를 사용하십시오.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC

auth_token = "Your PlaidCloud OAuth token"  # See Obtaining an OAuth Token below
endpoint_uri = "https://<your-workspace>.plaid.cloud/json-rpc/"
rpc = SimpleRPC(auth_token, endpoint_uri)
```

`SimpleRPC` 객체를 인스턴스화한 후에는 PlaidCloud에 요청을 보낼 수 있습니다. 이 예제는 테이블의 메타데이터를 요청합니다.

```python
table = rpc.analyze.table.table(
            project_id=project_id,
            table_id=table_id
        )
```

`SimpleRPC`는 각 호출을 동일한 토큰으로 워크스페이스 호스트의 `/rest/v1/`에 있는 REST API로 보냅니다. REST API가 아직 지원하지 않는 호출이나 아직 이전 릴리스를 사용하는 워크스페이스에 대한 호출은 대신 JSON-RPC를 사용하므로, 어느 경우에도 같은 코드가 작동합니다. 호출이 실패하면 두 경우 모두 `RPCError`가 발생합니다.


## REST API 직접 호출하기

`call_rest`는 `SimpleRPC`와 동일한 토큰, TLS 설정, 재시도로 REST API의 모든 엔드포인트에 요청을 보냅니다. HTTP 메서드와 `/rest/v1/` 아래의 경로를 지정하고, 필요에 따라 쿼리 문자열용 `params`와 JSON 요청 본문용 `body`를 지정합니다.

```python
dimensions = rpc.call_rest(
    'GET',
    'analyze/dimension/dimensions',
    params={'project_id': project_id},
)
```

디코딩된 JSON 응답을 반환하며, 응답에 본문이 없으면 `None`을 반환합니다. 성공이 아닌 응답은 HTTP 상태를 `code`로 하는 `RPCError`를 발생시킵니다.


## JSON-RPC는 더 이상 사용되지 않음

JSON-RPC는 더 이상 사용되지 않으며 향후 릴리스에서 제거됩니다. 1.25.0 이전 버전의 `plaidcloud-rpc`는 모든 호출을 JSON-RPC로 보내므로 JSON-RPC가 제거되면 작동하지 않습니다. 1.25.0 이상으로 업그레이드하십시오. `SimpleRPC` 코드는 변경할 필요가 없습니다. 새 통합은 REST API를 기준으로 작성하십시오.


## 사용할 수 있는 API는 무엇입니까?

PlaidCloud의 거의 모든 측면을 제어하는 다양한 API를 사용할 수 있습니다. 대화형 API 참조는 PlaidCloud 워크스페이스마다 내부에서 제공됩니다. 워크스페이스를 열고 API 문서 메뉴로 이동하면 실시간 엔드포인트 카탈로그를 볼 수 있습니다.


## OAuth 토큰 얻기

OAuth 토큰을 얻는 방법과 자동 인증을 위해 시스템을 구성하는 방법은 [OAuth 설정](/ko/reference/cli/jupyter/oauth-setup/)을 참조하십시오.
