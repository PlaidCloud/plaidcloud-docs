---
title: Ramp REST 커넥터
description: PlaidCloud에서 Ramp REST API 연결을 설정하여 법인 카드 지출 및 경비 데이터를 워크플로에 통합합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/ramp.md
---

## API 문서
[공급업체 API 참조](https://docs.ramp.com/developer-api/v1)에서 이 커넥터의 엔드포인트를 다룹니다.

## 구성

이 필드는 연결을 만들거나 편집할 때 나타납니다. 필수 여부는 사용하도록 설정한 인증 옵션에 따라 달라집니다.

### 식별 정보

| 필드 | 유형 | 설명 |
|---|---|---|
| 이름 | 텍스트 | 이 연결의 표시 이름입니다. |
| 별칭 | 텍스트(여러 줄) | 연결에 대한 선택적 별칭 또는 메모입니다. |
| 활성 여부 | 토글 | 연결의 사용 여부입니다. 삭제하지 않고 일시 중지하려면 비활성화합니다. |
| DB 읽기 전용 | 토글 | 연결을 읽기 전용 작업으로 제한합니다. |
| 액세스 유형 | 선택 | 이 연결의 읽기 전용, 쓰기 전용 또는 읽기/쓰기 액세스 수준입니다. |

### 기타

| 필드 | 유형 | 설명 |
|---|---|---|
| OAuth2 클라이언트 ID | 텍스트 | — |
| OAuth2 클라이언트 시크릿 | 텍스트 | 비밀 자격 증명이며 암호화되어 저장됩니다. |
| Ramp 범위 | 텍스트 | — |
