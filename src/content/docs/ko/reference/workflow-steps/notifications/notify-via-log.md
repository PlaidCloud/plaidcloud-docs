---
title: Notify Via Log 단계
description: PlaidCloud 워크플로 단계에서 로그 항목을 기록하여 상태 메시지, 디버깅 정보, 감사 추적 이벤트를 남깁니다.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-log.md
---

## 설명


Analyze 워크플로 로그에 메시지를 기록합니다.



### 메시지 매개변수


로그에 기록할 메시지를 입력합니다. 그런 다음 다음 세 가지 심각도 수준 중 하나를 선택합니다.


* 정보
* 경고
* 오류

참고: 이 변환에서는 프로젝트 변수와 워크플로 변수를 모두 사용할 수 있습니다.


## 예제


이 예제에서 이 변환을 실행하면 로그에 **정보** 항목이 추가되며, 내용은 *Write a message to the workflow log. I believe you have my stapler, Demo.*입니다.
