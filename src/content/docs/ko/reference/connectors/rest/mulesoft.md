---
title: MuleSoft REST 커넥터
description: PlaidCloud를 MuleSoft Anypoint 게이트웨이에 연결하고 API 정의를 첨부하여 워크플로 단계가 엔드포인트를 나열할 수 있도록 합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/mulesoft.md
---

MuleSoft Anypoint는 API 게이트웨이입니다. 조직이 그 뒤에 게시한 모든 서비스의 앞단에 위치하며, 주소는 배포마다 다릅니다. 따라서 하나의 서비스를 위해 만들어진 커넥터와 달리 MuleSoft 연결은 자체 엔드포인트를 알지 못하므로, API와 그 정의가 있는 위치를 직접 알려 주어야 합니다.

## API 문서

이 연결의 API 문서는 게이트웨이가 앞단에서 제공하는 서비스를 설명하는 문서입니다.

## 구성

MuleSoft는 [범용 REST 연결](/ko/reference/connectors/rest/generic-rest/)과 같은 양식을 사용하며, 탭 네 개, 필드, 동작이 모두 같습니다. 여기서는 다음 두 가지가 가장 중요합니다.

- **호스트 또는 IP 주소** — Anypoint 게이트웨이의 주소입니다. MuleSoft 주소는 배포마다 다르므로 기본값이 없습니다.
- **인증 유형** — 게이트웨이가 요구하는 `None`, `Basic`, `API Key`, `Bearer Token` 또는 `OAuth 2.0` 중 하나입니다. 사용자를 대신해 가정하는 값은 없습니다.

## 워크플로에서 엔드포인트 나열

게이트웨이에는 기본 제공 엔드포인트 목록이 없으므로, **API 정의**에서 API의 OpenAPI 3.x 또는 Swagger 2.0 정의를 연결에 첨부하십시오. 게시된 주소 또는 Document에 저장된 `.json` 또는 `.yaml` 파일 중 하나를 사용합니다. 필드는 [API 정의](/ko/reference/connectors/rest/generic-rest/#api-정의)를 참조하십시오.

그러면 이 연결을 사용하는 [REST Request 단계](/ko/guides/workflows/rest-request-step/)에서 **엔드포인트 소스**를 **연결의 API 정의에서**로 설정하고 **카탈로그 로드**를 선택하여, 각 경로를 직접 입력하는 대신 API의 엔드포인트 중에서 고를 수 있습니다.

## 관련 항목

- [범용 REST 연결](/ko/reference/connectors/rest/generic-rest/) — 이 양식의 전체 필드 참조입니다.
- [연결 만들기 및 관리](/ko/guides/connections/create-connection/)
- [REST Request 워크플로 단계](/ko/guides/workflows/rest-request-step/)
