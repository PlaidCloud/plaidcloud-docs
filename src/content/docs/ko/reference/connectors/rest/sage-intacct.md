---
title: Sage Intacct REST 커넥터
description: PlaidCloud에서 Sage Intacct REST API 연결을 설정하여 재무 및 회계 데이터를 워크플로에 통합합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/sage-intacct.md
---

## API 문서

Sage Intacct REST API 문서는 [Sage 개발자 사이트](https://developer.sage.com/intacct/docs/1/sage-intacct-rest-api/get-started/quick-start)에서 확인할 수 있습니다.


## 보안 요구 사항

PlaidCloud는 REST 연결 계열에 전용 **Intacct** 연결을 제공합니다(**REST - Intacct**로 표시). 이 연결은 Intacct REST API에 대해 OAuth2 클라이언트 자격 증명으로 인증합니다. Sage Intacct **Web Services** 발신자 ID/발신자 비밀번호 쌍을 연결의 **클라이언트 ID**와 **클라이언트 시크릿**으로 입력하고, 웹 서비스 사용자 이름과 회사 ID도 입력합니다. 발신자 자격 증명은 Sage 지원팀이 회사에 대해 활성화해야 하며, 웹 서비스 사용자에게는 커넥터가 읽을 모든 Intacct 개체에 대한 권한이 있어야 합니다.

클라이언트 ID와 클라이언트 시크릿은 비밀로 취급하십시오. PlaidCloud의 **자격 증명** 영역을 통해서만 저장하고 연결에서 참조하십시오.


## 자격 증명 얻기

1. Sage Intacct **Company Setup** 영역을 엽니다
2. Sage에서 제공한 발신자 ID에 대해 Web Services를 사용 설정합니다
3. PlaidCloud용 Web Services 사용자를 만들거나 선택합니다
4. 쿼리하려는 모든 개체에 대한 권한을 사용자에게 부여합니다
5. 회사 ID, 웹 서비스 사용자 이름, 발신자 ID, 발신자 비밀번호를 기록해 둡니다


## Sage Intacct 커넥터 만들기

1. **Tools > Connections**로 이동하여 `Add Connection`을 클릭합니다
2. **REST** 아래에서 **Intacct**를 선택합니다(**REST - Intacct**로 표시)
3. 다음을 입력합니다.
    * **연결 이름** — 워크플로 단계에 표시되는 친숙한 이름
    * **클라이언트 ID** — Intacct 발신자 ID
    * **클라이언트 시크릿** — Intacct 발신자 비밀번호
    * **웹 서비스 사용자 이름** — 웹 서비스 사용자 로그인
    * **회사 ID** — 연결하려는 Intacct 회사
4. `Test`를 클릭하여 자격 증명을 검증합니다
5. `Save`를 클릭합니다


## 워크플로 단계에서 사용

동일한 연결로 Intacct에서 읽기와 전기를 모두 수행합니다. 다음에서 선택할 수 있습니다.

* [Import Sage AP 단계](../../../workflow-steps/sage-intacct/import-sage-ap/) — AP 청구서 헤더
* [Import Sage AP Lines 단계](../../../workflow-steps/sage-intacct/import-sage-ap-lines/) — AP 청구서 라인 상세
* [Import Sage Intacct Query 단계](../../../workflow-steps/sage-intacct/import-intacct-query/) — 모든 Intacct 개체에 대한 일반 쿼리
* [Import Intacct Entity 단계](../../../workflow-steps/sage-intacct/import-intacct-entity/) — 총계정원장 상세, 잔액, 항목, 차원 마스터를 자동 페이지 나누기로 가져옵니다
* [Intacct: 분개 전표 전기 단계](../../../workflow-steps/sage-intacct/export-to-sage/) — 분개 항목 전기
