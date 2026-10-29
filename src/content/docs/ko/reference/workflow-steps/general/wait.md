---
title: 대기
description: PlaidCloud 워크플로 단계에 시간 지연을 추가하여 다음 단계로 진행하기 전에 지정한 시간 동안 실행을 일시 중지합니다.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/wait.md
---

## 설명


대기 변환은 지정한 시간 동안 처리를 일시 중지하는 데 사용합니다. 다른 시스템의 I/O 작업을 기다리거나 개발 중에 워크플로를 디버깅할 때 특히 유용합니다.



## 기간 매개변수


**소요 시간** 스피너를 사용하여 0 이상의 정수 값을 지정합니다.



다음으로 드롭다운 메뉴에서 시간 단위를 지정합니다. 선택할 수 있는 단위는 다음과 같습니다.


* 초
* 분
* 시간

## 시간 또는 파일 대기

**기타 대기** 섹션에는 다음 필드가 있습니다. 단계는 소요 시간이 지난 후 이 순서대로 대기합니다.

* **밀리초**(`milliseconds`) — 소요 시간에 더해 추가로 대기하는 밀리초입니다.
* **하루 중 시각까지**(`until_time`) — 이어서 시계가 이 시각(UTC, `HH:MM:SS` 형식)을 다음에 가리킬 때까지 대기합니다.
* **파일 대기**(`file`) — 이어서 이 Document 파일 `{account, path}`이 변경될 때까지 대기합니다. **파일 변경**(`file_event`)은 대기할 변경 유형으로, `modified`(기본값), `created`, `deleted` 중 하나입니다. 단계는 **파일 확인 간격(초)**(`poll_seconds`, 기본값 5)마다 파일을 확인하며, **파일 최대 대기 시간(초)**(`max_wait_seconds`, 기본값 3600, 최대 하루)까지 기다린 후 경고와 함께 완료되고 워크플로는 계속됩니다. `created`를 기다리는데 파일이 이미 있으면 대기가 즉시 끝나고, `modified` 또는 `deleted`를 기다리는데 파일이 없으면 기다리지 않고 경로를 알려 주는 경고와 함께 완료됩니다.
