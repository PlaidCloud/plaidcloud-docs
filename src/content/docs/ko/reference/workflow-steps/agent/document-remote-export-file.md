---
title: Document - Remote Export File 단계
description: PlaidCloud 워크플로에서 PlaidLink 에이전트를 통해 원격 시스템으로 파일을 내보내어 방화벽 뒤에서 파일을 안전하게 전송합니다.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-export-file.md
---

## 설명



PlaidLink 에이전트를 통해 PlaidCloud 문서 계정의 파일을 원격 파일 시스템에 기록합니다. 내부 공유 드라이브, 온프레미스 SFTP 서버, 특수 애플리케이션 디렉터리처럼 PlaidCloud에서 직접 접근할 수 없는 시스템에 보고서, 추출 결과 또는 처리된 파일을 전달할 때 유용합니다.

에이전트가 PlaidCloud에서 파일을 받아 구성된 로컬 대상에 기록합니다.


## 예제


먼저 “Agent to Use” 드롭다운에서 항목을 선택합니다. 다음으로 “File or Folder to Export”에서 파일 또는 폴더 경로를 찾아 선택합니다. 그런 다음 “Export Path Destination”에 위치를 입력합니다. 마지막으로 “Save and Run Step”을 선택합니다.

## 경로 안전성

내보내기 경로가 비어 있으면 `No destination path for the export; it would write into the agent's working directory.`와 함께 단계가 실패합니다. 여기에는 경로의 변수가 비어 있어 아무 값으로도 확인되지 않은 경로도 포함됩니다. `E:\` 또는 `\\nas\drop` 같은 드라이브나 공유 루트로 내보내는 것은 가능합니다.

**도착 시 아카이브 압축 해제**를 선택하면, 단계가 대상 폴더의 모든 아카이브를 풀고 삭제합니다. 따라서 파일 시스템 루트이거나 그 바로 아래 파일인 대상(`Refusing to unpack an export into the filesystem root <path>.`) 또는 PlaidLink 에이전트 자체 폴더(`Refusing to unpack an export into <path>, which contains the agent's working directory.`)는 거부합니다. 대신 전용 하위 폴더를 선택하십시오.

빈 경로 검사와 루트 검사는 이미 배포한 PlaidLink 에이전트에서도 작동합니다. 에이전트 자체 폴더를 거부하려면 업데이트된 PlaidLink 에이전트가 필요합니다.
