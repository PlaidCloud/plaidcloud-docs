---
title: 명령줄
description: PlaidCloud 명령줄 인터페이스를 사용하여 작업을 자동화하고, 스크립트를 실행하고, 터미널에서 PlaidCloud 리소스를 다루는 방법을 설명합니다.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloud는 표준 JSON-RPC 요청을 사용하므로, 해당 요청을 보낼 수 있는 모든 애플리케이션에서 사용할 수 있습니다.


더 쉽게 사용할 수 있도록 연결과 API 실행 과정을 단순화하는 Python 패키지가 제공됩니다.


## 필수 설치

터미널에서 다음 명령을 실행하십시오.

```bash
pip install plaidcloud-rpc
```


## Simplerpc 객체를 사용하여 요청하기

`plaidcloud-rpc` 패키지로 요청하려면 `SimpleRPC` 객체를 사용하십시오.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC  
  
auth_token = "Your PlaidCloud Auth Token" # See Obtaining Token below  
endpoint_uri = "plaidcloud.com" # or plaidcloud.net  
rpc = SimpleRPC(auth_token, endpoint_uri)
```

`SimpleRPC` 객체를 만든 후에는 PlaidCloud에 RPC 요청을 보낼 수 있습니다. 다음 예제는 테이블의 메타데이터를 요청합니다.

```python
table = rpc.analyze.table.table(  
            project_id=project_id,  
            table_id=table_id  
        )
```

## 사용할 수 있는 API는 무엇입니까?

PlaidCloud의 거의 모든 측면을 제어하는 다양한 API를 사용할 수 있습니다. 대화형 API 참조는 PlaidCloud 워크스페이스마다 내부에서 제공됩니다. 워크스페이스를 열고 API 문서 메뉴로 이동하면 실시간 엔드포인트 카탈로그를 볼 수 있습니다.


## OAuth 토큰 얻기

OAuth 토큰을 얻는 방법과 자동 인증을 위해 시스템을 구성하는 방법은 [OAuth 설정](/ko/reference/cli/jupyter/oauth-setup/)을 참조하십시오.
