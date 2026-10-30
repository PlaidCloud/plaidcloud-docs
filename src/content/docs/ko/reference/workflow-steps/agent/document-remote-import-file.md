---
title: Document - Remote Import File 단계
description: PlaidCloud 워크플로에서 PlaidLink 에이전트를 통해 원격 시스템에서 파일을 가져와 방화벽 뒤의 파일을 안전하게 가져옵니다.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-import-file.md
---

## 설명



PlaidLink 에이전트를 통해 원격 파일 시스템에서 파일을 가져와 PlaidCloud 문서 계정에 저장합니다. 원본 파일이 내부 파일 공유, 온프레미스 서버 또는 방화벽 뒤에 있을 때 사용합니다.

에이전트가 파일을 로컬에서 읽어 PlaidCloud로 스트리밍하며, 이후 워크플로 단계에서 이를 처리할 수 있습니다.


## 예제


먼저 “Agent to Use” 드롭다운에서 항목을 선택합니다. 다음으로 “File or Folder Path for Import”에 파일 또는 폴더 경로를 입력합니다. 그런 다음 “Folder Destination”에 대상 폴더를 입력합니다. 필요하면 파일이 도착할 때 압축하도록 **압축**을 선택합니다: Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO 또는 Deflate (zlib). 마지막으로 “Save and Run Step”을 선택합니다.

## 없는 원본 파일 또는 폴더

원격 공유의 해당 경로에 아무것도 없으면 오류 대신 `No file or folder found at <path>; nothing imported.` 경고와 함께 단계가 완료됩니다. 워크플로는 다음 단계로 계속되며, 없는 원본에 대해서는 단계의 재시도 및 오류 발생 시 설정(단계로 이동 또는 계속)이 실행되지 않습니다. 이는 이미 배포한 PlaidLink 에이전트에서도 작동합니다.

경로가 비어 있으면 `No path to import from; nothing imported.` 경고와 함께 동일하게 완료됩니다. 여기에는 `{folder}/archive`처럼 폴더가 변수여서 이번 실행에서 아무 값으로도 확인되지 않은 경로도 포함됩니다.

파일 시스템 루트이거나 PlaidLink 에이전트 작업 디렉터리의 상위 폴더인 경로(`/`, `C:\`, `\\server\share` 같은 공유 루트 또는 `..`)는 아무것도 업로드하기 전에 단계가 실패하며, `Refusing to import from the filesystem root <path>.` 또는 `Refusing to import from <path>, which contains the agent's working directory.`가 표시됩니다. 루트와 `..`는 이미 배포한 PlaidLink 에이전트에서도 거부되며, 업데이트된 에이전트는 자체 파일 시스템을 기준으로 판단하여 작업 디렉터리를 포함하는 다른 모든 폴더도 거부합니다.

그 밖의 실패는 여전히 단계를 실패 처리합니다. 권한 거부, PlaidCloud로의 업로드 실패, 그리고 업데이트된 PlaidLink 에이전트에서는 서버 또는 공유에 접근할 수 없는 경우가 이에 해당합니다.

아무것도 가져오지 않으므로 이전 실행의 문서는 그대로 남아 있습니다. 이번 기간의 파일이 도착했을 때만 후속 단계를 실행하려면 다음 중 하나를 수행하십시오.

- 후속 단계에 **file exists in Document** [단계 조건](/ko/guides/workflows/step-conditions/#문서-경로-조건)을 추가하고, Document 경로를 파일 이름에 기간이 포함된 경로처럼 기간별 경로로 설정합니다.
- 워크플로가 사용한 뒤 가져온 문서를 삭제하여, 없는 원본이 오래된 파일을 남겨 두지 않도록 합니다.
