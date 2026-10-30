---
title: Notify via Microsoft Teams 단계
description: PlaidCloud 워크플로 단계에서 Microsoft Teams 알림을 보내 채널이나 사용자에게 워크플로 이벤트와 상태를 알립니다.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-microsoft-teams.md
---

워크플로에서 Microsoft Teams 알림을 추가하는 일은 두 부분으로 이루어집니다. 두 부분은 다음과 같습니다.


1. Microsoft Teams 외부 연결 만들기
2. 워크플로에 Microsoft Teams 알림 단계 추가

## 워크플로에 Microsoft Teams 알림 단계 추가


워크플로에 Microsoft Teams 알림 단계를 추가하는 방법은 다른 단계를 추가하는 것과 같습니다. 단계를 추가한 후 단계 구성을 열고 양식을 작성한 다음 저장합니다. 이제 Microsoft Teams 알림을 테스트할 수 있습니다.



## Microsoft Teams 메시지 서식 지정


Teams에는 이미지 추가, 사용자 멘션 등 다양한 서식 옵션이 있습니다. 자세한 내용은 [Teams 메시지 텍스트 서식](https://support.microsoft.com/en-us/office/use-markdown-formatting-in-teams-4d10bd65-55e2-4b2d-a1f3-2bebdcd2c772) 문서를 참조하십시오.



## Microsoft Teams 외부 연결 만들기


PlaidCloud가 사용자를 대신하여 Microsoft Teams 알림을 보낼 수 있도록 하는 일회성 설정입니다. Microsoft Teams에서는 웹훅 앱(인터넷을 통해 알림을 보내는 일반적인 방법)을 만들 수 있습니다. Microsoft Teams에서 웹훅 앱을 만든 후, 제공된 자격 증명을 PlaidCloud에 추가하여 사용할 수 있게 합니다.



### Microsoft Teams 웹훅 앱 만들기


이 단계는 Microsoft Teams 관리자가 수행해야 합니다. [수신 웹훅 만들기(Microsoft Teams 문서)](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook#create-incoming-webhook-1)에 설명된 단계를 따르십시오.



### PlaidCloud 외부 연결 설정


이 단계는 외부 데이터 연결을 만들 권한이 있는 PlaidCloud 워크스페이스 관리자가 수행해야 합니다. 연결을 만들려면 다음 단계를 따르십시오.


1. `Analyze > Tools > External Data Connections`로 이동합니다
2. `+ New Connection` 선택 항목에서 Microsoft Teams Webhook을 선택합니다
3. 이름, 설명을 입력하고 위에서 웹훅을 만들 때 생성된 웹훅 URL을 붙여 넣습니다. 여기에 입력한 이름이 워크플로 단계에서 선택 항목으로 표시되므로 가능하면 알아보기 쉬운 이름을 사용하십시오. URL을 가진 사람은 누구나 채널에 게시할 수 있으므로 **웹훅 URL** 필드는 붙여 넣을 때 값을 가리고 연결을 다시 열면 비어 있는 것으로 표시됩니다. 저장된 URL을 유지하려면 비워 두십시오.
4. `+ Create` 버튼을 선택합니다


## 예제

아직 예제가 없습니다...
