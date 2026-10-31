---
title: Document - Remote Rename File 단계
description: PlaidCloud 워크플로에서 PlaidLink 에이전트를 통해 원격 시스템의 파일 이름을 바꾸어 방화벽 뒤의 파일을 안전하게 관리합니다.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-rename-file.md
---

## 설명



PlaidLink 에이전트를 통해 원격 파일 시스템의 파일 이름을 바꾸거나 이동합니다. 전적으로 온프레미스 쪽에서 작동하며 PlaidCloud와 주고받는 데이터는 없습니다.

일반적인 패턴: 원격 가져오기 단계가 성공한 후 원본 파일 이름을 바꿔 '처리됨'으로 표시하면, 같은 워크플로가 다음 실행에서 이를 다시 가져오지 않습니다.


## 예제


먼저 “Agent to Use” 드롭다운에서 항목을 선택합니다. 



다음으로 “Source Path”와 “Destination Path”를 입력합니다. 



마지막으로 “Save and Run Step”을 선택합니다.

## 없는 원본

업데이트된 PlaidLink 에이전트에서는 원격 시스템에 존재하지 않는 원본이 있으면 오류 대신 `No file or folder found at <path>; nothing renamed` 경고와 함께 단계가 완료되고 워크플로가 계속됩니다. 업데이트되지 않은 에이전트는 여전히 단계를 실패 처리합니다.

원본 경로가 비어 있으면 `No path to rename from; nothing renamed.` 경고와 함께 단계가 완료됩니다. 경로의 폴더가 변수여서 이번 실행에서 아무 값으로도 확인되지 않은 경우도 마찬가지입니다.

파일 시스템 루트이거나 PlaidLink 에이전트 작업 디렉터리의 상위 폴더인 원본(`/`, `C:\`, `\\server\share` 같은 공유 루트 또는 `..`)은 `Refusing to rename from the filesystem root <path>.` 또는 `Refusing to rename from <path>, which contains the agent's working directory.`와 함께 단계가 실패합니다. 대상 경로가 비어 있으면 `No destination path for the rename; it would write into the agent's working directory.`와 함께 단계가 실패합니다. `E:\` 또는 `\\nas\drop` 같은 드라이브나 공유 루트로 이름을 바꾸는 것은 가능합니다. 루트와 `..`는 이미 배포한 PlaidLink 에이전트에서도 거부되며, 업데이트된 에이전트는 자체 파일 시스템을 기준으로 판단하여 작업 디렉터리를 포함하는 다른 모든 폴더도 거부합니다.
