---
title: SAP Profitability and Cost Management(PCM) 커넥터
description: PlaidCloud에서 SAP Profitability and Cost Management 연결을 구성하여 비용 배부 데이터를 워크플로에 통합합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/sap-pcm.md
---

## 업스트림 문서
[SAP PCM 레거시 문서](https://help.sap.com/docs/SAP_PROFITABILITY_AND_COST_MANAGEMENT).

## 구성

이 필드는 연결을 만들거나 편집할 때 나타납니다. 필수 여부는 사용하도록 설정한 인증 옵션에 따라 달라집니다.

### 식별

| 필드 | 유형 | 설명 |
|---|---|---|
| 이름 | 텍스트 | 이 연결의 표시 이름입니다. |
| 별칭 | 텍스트(여러 줄) | 연결에 대한 선택적 별칭 또는 메모입니다. |
| 활성 여부 | 토글 | 연결의 사용 여부입니다. 삭제하지 않고 일시 중지하려면 비활성화합니다. |
| DB 읽기 전용 | 토글 | 연결을 읽기 전용 작업으로 제한합니다. |
| 액세스 유형 | 선택 | 이 연결의 읽기 전용, 쓰기 전용 또는 읽기/쓰기 액세스 수준입니다. |

### 인증

| 필드 | 유형 | 설명 |
|---|---|---|
| DB 사용자 | 텍스트 | 데이터베이스 인증에 사용하는 사용자 이름입니다. |
| SSO 사용 | 토글 | 사용자 이름/비밀번호 대신 싱글 사인온으로 인증합니다. |
| DB 비밀번호 | 비밀번호 | 데이터베이스 인증에 사용하는 비밀번호입니다. |
