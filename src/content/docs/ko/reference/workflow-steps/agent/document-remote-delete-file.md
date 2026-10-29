---
title: Document - Remote Delete File 단계
description: PlaidCloud 워크플로에서 PlaidLink 에이전트를 통해 원격 시스템의 파일을 삭제하여 방화벽 뒤의 파일을 안전하게 관리합니다.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-delete-file.md
---

## 설명



PlaidLink 에이전트를 통해 접근하는 방화벽 뒤 파일 시스템의 파일을 삭제합니다. 에이전트가 온프레미스 파일 시스템에서 로컬로 삭제를 수행합니다.

온프레미스 내보내기 작업 후 정리하거나, 처리가 끝난 원본 파일을 제거해야 하는 파일 기반 연동의 일부로 사용합니다.


## 예제


먼저 “Agent to Use” 드롭다운에서 항목을 선택합니다. 다음으로 “File or Folder Path for Delete”에 파일 또는 폴더 경로를 입력합니다. 마지막으로 “Save and Run Step”을 선택합니다.

## 없는 경로

업데이트된 PlaidLink 에이전트에서는 원격 시스템에 존재하지 않는 경로가 있으면 오류 대신 `Nothing to delete at <path>` 경고와 함께 단계가 완료되고 워크플로가 계속됩니다. 업데이트되지 않은 에이전트는 여전히 단계를 실패 처리합니다.

경로가 비어 있으면 `No path to delete; nothing deleted.` 경고와 함께 단계가 완료되며 아무것도 삭제하지 않습니다. 여기에는 `{folder}/archive`처럼 폴더가 변수여서 이번 실행에서 아무 값으로도 확인되지 않은 경로도 포함됩니다.

파일 시스템 루트이거나 PlaidLink 에이전트 작업 디렉터리의 상위 폴더인 경로(`/`, `C:\`, `\\server\share` 같은 공유 루트 또는 `..`)는 아무것도 삭제하기 전에 단계가 실패하며, `Refusing to delete the filesystem root <path>.` 또는 `Refusing to delete <path>, which contains the agent's working directory.`가 표시됩니다. 루트와 `..`는 이미 배포한 PlaidLink 에이전트에서도 거부되며, 업데이트된 에이전트는 자체 파일 시스템을 기준으로 판단하여 작업 디렉터리를 포함하는 다른 모든 폴더도 거부합니다.
