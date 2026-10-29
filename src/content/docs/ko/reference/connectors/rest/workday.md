---
title: Workday REST 커넥터
description: PlaidCloud에서 Workday REST API 연결을 구성하여 HR, 재무, 계획 데이터를 워크플로에 통합합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday.md
---

## API 문서
[공급업체 API 레퍼런스](https://community.workday.com/sites/default/files/file-hosting/restapi/)에서 이 커넥터의 엔드포인트를 설명합니다.

## 구성

이 필드는 연결을 만들거나 편집할 때 표시됩니다. 필수 여부는 사용하도록 설정한 인증 옵션에 따라 달라집니다.

### 식별 정보

| 필드 | 유형 | 설명 |
|---|---|---|
| Name | 텍스트 | 이 연결의 표시 이름입니다. |
| Alias | 텍스트(여러 줄) | 연결에 대한 선택적 별칭 또는 메모입니다. |
| Is active | 토글 | 연결의 사용 여부입니다. 삭제하지 않고 일시 중지하려면 끕니다. |
| Db read only | 토글 | 연결을 읽기 전용 작업으로 제한합니다. |
| Access type | 선택 | 이 연결의 읽기 전용, 쓰기 전용 또는 읽기-쓰기 접근 수준입니다. |

### 기타

| 필드 | 유형 | 설명 |
|---|---|---|
| Oauth2 client id | 텍스트 | — |
| Oauth2 client secret | 텍스트 | 비밀 자격 증명이며 암호화되어 저장됩니다. |
| Workday url | 텍스트 | URL 엔드포인트입니다. |
| Oauth2 refresh token | 텍스트 | — |
