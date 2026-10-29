---
title: Notify via Slack 단계
description: PlaidCloud 워크플로 단계에서 Slack 알림을 보내 채널이나 사용자에게 워크플로 이벤트, 오류, 상태를 알립니다.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-slack.md
---

워크플로에서 Slack 알림을 추가하는 일은 두 부분으로 이루어집니다. 두 부분은 다음과 같습니다.


1. Slack Webhook 외부 연결 만들기
2. 워크플로에 Slack 알림 단계 추가

## 워크플로에 Slack 알림 단계 추가


워크플로에 Slack 알림 단계를 추가하는 방법은 다른 단계를 추가하는 것과 같습니다. 단계를 추가한 후 단계 구성을 열고 양식을 작성한 다음 저장합니다. 이제 Slack 알림을 테스트할 수 있습니다.



## 파일 첨부

**업로드할 파일**에서 문서를 선택하면 해당 문서가 메시지를 설명 댓글로 하여 채널로 전송됩니다. 웹훅은 파일을 전달할 수 없으므로 첨부 파일은 Slack 연결의 봇 토큰을 통해 전송됩니다.

- 연결에 **봇 토큰**을 추가합니다. `files:write` 범위를 가진 Slack 앱의 `xoxb-` 토큰이며, 앱이 채널에 초대되어 있어야 합니다.
- 단계에는 채널 이름이 아니라 `C0123ABCD`와 같은 **채널 ID**를 입력합니다. Slack의 파일 업로드는 ID만 받으며, ID가 없으면 단계가 실패합니다. ID를 찾으려면 Slack에서 채널 세부 정보를 열고 맨 아래로 스크롤합니다.
- 문서를 찾을 수 없으면 메시지는 첨부 파일 없이 웹훅으로 전송되며, 단계는 문서 경로와 함께 경고를 표시합니다.

## Slack 메시지 서식 지정


Slack에는 이미지 추가, 사용자 멘션 등 다양한 서식 옵션이 있습니다. 자세한 내용은 [Slack 텍스트 서식](https://api.slack.com/reference/surfaces/formatting) 문서를 참조하십시오.



## Slack Webhook 외부 연결 만들기


PlaidCloud가 사용자를 대신하여 Slack 알림을 보낼 수 있도록 하는 일회성 설정입니다. Slack에서는 웹훅 앱(인터넷을 통해 알림을 보내는 일반적인 방법)을 만들 수 있습니다. Slack에서 웹훅 앱을 만든 후, 제공된 자격 증명을 PlaidCloud에 추가하여 사용할 수 있게 합니다.



### Slack 웹훅 앱 만들기


이 단계는 Slack 관리자가 수행해야 합니다. Slack 웹훅 앱을 만들려면 다음 단계를 따르십시오.


1. Slack에서 워크스페이스 제어 메뉴를 열고 `Settings & administration > Manage Apps`를 선택합니다
2. 앱 카테고리 목록에서 `Custom Integrations`를 선택합니다
3. 앱 목록에서 `Incoming Webhooks`를 선택합니다
4. `Add to Slack` 버튼을 선택합니다
5. 다음 화면에서 메시지를 게시할 Slack 채널을 선택하고 계속합니다. 이 채널이 기본으로 사용되지만, 특정 개인에게 DM을 보내는 것을 포함하여 각 알림에서 재정의할 수 있습니다.
6. 표시된 웹훅 URL을 복사합니다. 나중에 사용하므로 안전한 곳에 보관하십시오. 다음과 같은 형태입니다. `https://hooks.slack.com/services/T04QZ1435/G02TGBFTOP8/K9GZrR2ThdJz1uSiL9YeZxoR`
7. 저장하기 전에 모양, 이름, 이모지를 사용자 지정할 수 있습니다. 이러한 사용자 지정은 기본값일 뿐이며 PlaidCloud 워크플로 내의 각 알림 단계에서 재정의할 수 있습니다.

### PlaidCloud 외부 연결 설정


이 단계는 외부 데이터 연결을 만들 권한이 있는 PlaidCloud 워크스페이스 관리자가 수행해야 합니다. 연결을 만들려면 다음 단계를 따르십시오.


1. `Analyze > Tools > External Data Connections`로 이동합니다
2. `+ New Connection` 선택 항목에서 Slack Webhook을 선택합니다
3. 이름, 설명을 입력하고 위 6단계에서 제공된 웹훅 URL을 붙여 넣습니다. 여기에 입력한 이름이 워크플로 단계에서 선택 항목으로 표시되므로 가능하면 알아보기 쉬운 이름을 사용하십시오. URL을 가진 사람은 누구나 채널에 게시할 수 있으므로 **웹훅 URL** 필드는 붙여 넣을 때 값을 가리고 연결을 다시 열면 비어 있는 것으로 표시됩니다. 저장된 URL을 유지하려면 비워 두십시오.
4. 첨부 파일을 보내려면 Slack 앱의 봇 토큰도 **봇 토큰(파일 업로드용)** 필드에 붙여 넣습니다. 연결에는 웹훅 URL, 봇 토큰 또는 둘 다 담을 수 있습니다. 봇 토큰은 웹훅 URL과 마찬가지로 가려지며 연결을 다시 열면 비어 있는 것으로 표시됩니다.
5. `+ Create` 버튼을 선택합니다


## 예제

아직 예제가 없습니다...
