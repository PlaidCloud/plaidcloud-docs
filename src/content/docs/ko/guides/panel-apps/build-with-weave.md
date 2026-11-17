---
title: Weave로 Panel 앱 빌드하기
description: 원하는 앱을 설명하면 Weave가 Panel Studio에서 작성하며, 저장되기 전에 정확한 변경 사항을 승인합니다.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/build-with-weave.md
---

Weave는 Panel 앱을 대신 작성하고 변경할 수 있습니다. [Panel Studio](/ko/guides/panel-apps/studio/)에서 열어 둔 앱에 대해 작업하며, 승인하기 전에는 Weave가 제안한 어떤 것도 앱을 변경하지 않습니다.

## Weave에 요청하기

1. Panel Studio에서 앱을 엽니다.
2. **Weave에 문의**를 선택합니다. [Weave 도크](/ko/guides/ai-assistant/weave-dock/)가 앱의 대화로 열립니다.
3. 원하는 내용을 설명합니다. 예: "지역 필터와 월별 매출 차트를 추가해 줘."

Weave는 작업 중인 앱의 파일, 빌드 상태와 빌드 오류, 앱의 기반이 되는 테이블 또는 뷰를 이미 알고 있습니다. 대화에 코드나 오류를 붙여 넣을 필요가 없습니다. 빌드가 실패하면 빌드 상태에서 **Ask Weave about this error**를 선택하십시오. 오류가 입력 상자에 들어간 상태로 도크가 열리므로 바로 보낼 수 있습니다.

Weave는 프로젝트에 속한 앱에서 작동합니다. 프로젝트에 속하지 않은 앱에서는 Panel Studio에 *Assign this app to a project to use Weave.* 라는 메시지가 표시됩니다.

## 변경 사항 승인하기

Weave가 앱의 코드를 변경하려고 하면 추가하고 제거하는 모든 줄을 파일별로 보여 주는 전체 차이점이 포함된 승인 카드를 표시합니다.

1. 차이점을 읽습니다.
2. 변경 사항을 앱의 초안에 저장하려면 **승인**을, 취소하려면 **거부**를 선택합니다.

승인하면 초안이 저장됩니다. 게시되지는 않습니다. 결과를 미리 본 다음 만족스러우면 [게시](/ko/guides/panel-apps/studio/#게시)하십시오.

### 승인은 웹에서만 가능합니다

코드 변경은 웹의 PlaidCloud에서만 승인할 수 있습니다. PlaidCloud 모바일 앱에서는 제안된 코드 변경을 거부할 수는 있지만 승인할 수는 없습니다. 그 밖의 Weave 변경은 휴대폰에서도 승인할 수 있습니다. [모바일에서 Weave 사용하기](/ko/guides/mobile-app/weave-on-mobile/)를 참조하십시오.

## 다음 단계

- [Panel Studio](/ko/guides/panel-apps/studio/) — 저장, 미리 보기 및 게시.
- [Panel 앱 키트](/ko/guides/panel-apps/app-kit/) — Weave가 빌드에 사용하는 구성 요소.
