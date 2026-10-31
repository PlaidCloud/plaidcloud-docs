---
title: OAuth 토큰
description: Jupyter 노트북, CLI 도구, 사용자 지정 애플리케이션 연결을 인증하기 위해 PlaidCloud API 접근용 OAuth 토큰을 설정합니다.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/oauth-setup.md
---

PlaidCloud는 표준 JSON-RPC 요청을 사용하므로, 해당 요청을 보낼 수 있는 모든 애플리케이션에서 사용할 수 있습니다.  요청은 OAuth 토큰으로 보호됩니다.


## OAuth 토큰 얻기

OAuth 토큰은 PlaidCloud 앱에서 생성합니다. 사용자에게 할당된 현재 OAuth 토큰 목록을 보거나 새 토큰을 생성하려면 `Analyze > Tools > Registered Systems`로 이동하십시오.

해당 화면에서 기존 토큰을 확인하거나 새 토큰을 만들 수 있습니다.

## OAuth PlaidCloud 구성 파일 다운로드
"Register a New System"을 선택하십시오.

양식을 작성하고, 목록에서 찾을 수 있도록 입력한 이름을 기록해 두십시오.

생성되면 톱니바퀴 아이콘을 클릭하여 등록된 시스템 레코드를 여십시오.  그러면 구성 파일 텍스트가 표시됩니다.  

참고: 맨 위의 드롭다운에서 이 연결에 사용할 프로젝트를 반드시 선택하십시오.  그러면 구성에 프로젝트 고유 식별자가 추가됩니다.

이 텍스트를 복사하여 시스템의 plaid.conf 파일에 붙여 넣으십시오.  이 파일은 .plaid 디렉터리에 두십시오.

## 로컬에 구성 파일 만들기
노트북 디렉터리보다 한 단계 위, 또는 명령줄을 사용할 위치보다 한 단계 위에 디렉터리를 만드십시오.  디렉터리 이름은 `.plaid`로 지정합니다.

`.plaid` 디렉터리 안에 `plaid.conf` 파일을 만들고 위에서 복사한 내용을 붙여 넣으십시오.  파일을 저장하면 이제 PlaidCloud 유틸리티와 rpc 메서드를 사용하여 연결할 수 있습니다.


## 고급 사용

`.plaid` 폴더는 사용하는 지점 가까이에 두는 것이 편리하지만, 상위 디렉터리 트리의 어느 곳에든 둘 수 있습니다.  초기화 과정은 `.plaid` 디렉터리를 찾을 때까지 디렉터리 트리를 위로 거슬러 올라갑니다.

같은 하위 디렉터리 구조에 함께 둘 수 없는 여러 작업이 접근해야 하는 경우에는 `.plaid` 디렉터리를 더 상위에 두면 유용할 수 있습니다.


## 선택적 경로 지정
로컬 Jupyter 노트북 설치본을 사용하거나 명령줄에서 작업하는 경우, 도우미 도구를 사용하여 데이터, Excel 파일 및 기타 데이터를 내보내고 로컬 데이터를 데이터프레임으로 읽어 들일 수 있습니다.  이렇게 하려면 paths.yaml 파일이 필요합니다.

`plaid.conf` 파일과 함께 `paths.yaml` 파일을 만드십시오.  `paths.yaml`은 `.plaid` 디렉터리 안에서 `plaid.conf` 파일과 같은 위치에 있어야 합니다.  이 파일에는 다음 경로 정보가 들어 있어야 합니다.

```yaml
paths:
 PROJECT_ROOT: '{WORKING_USER}/Documents'
 LOCAL_STORAGE: '{PROJECT_ROOT}/local_storage'
 DEBUG: '{PROJECT_ROOT}/local_storage'
 REPORTS: '{PROJECT_ROOT}/reports'
 
 create: []
 local: {}
```
