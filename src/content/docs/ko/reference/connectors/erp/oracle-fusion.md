---
title: Oracle Fusion 커넥터
description: OAuth2 자격 증명으로 PlaidCloud에 Oracle Fusion Cloud 연결을 설정하여 OData/BIP로 총계정원장 잔액과 분개 배치를 가져오고 FBDI로 분개를 전기합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-fusion.md
---

## API 문서

Oracle Fusion Cloud의 [REST API(OData)](https://docs.oracle.com/en/cloud/saas/financials/)와 [BI Publisher(BIP) 및 파일 기반 데이터 가져오기(FBDI)](https://docs.oracle.com/en/cloud/saas/applications-common/) 참조 문서에 이 커넥터가 사용하는 엔드포인트와 대량 추출/로드 경로가 설명되어 있습니다.

## 인증 방식

연결은 전용 API 사용자에 대해 OAuth2 클라이언트 자격 증명(또는 Fusion Cloud 보안 설정에서 통합 사용자에게 발급하는 기본 인증 API 자격 증명)으로 인증합니다. API 사용자의 역할에 따라 읽을 수 있는 총계정원장 엔터티와 전기할 수 있는 FBDI/GL Interface 기능이 모두 결정됩니다.

## 구성

| 필드 | 유형 | 설명 |
|---|---|---|
| 이름 | 텍스트 | 이 연결의 표시 이름입니다. |
| 인스턴스 URL | 텍스트 | Fusion Cloud 인스턴스 URL입니다. 예: `https://yourorg.fa.us2.oraclecloud.com`. |
| 클라이언트 ID | 텍스트 | API 사용자의 OAuth2 클라이언트 ID입니다(기본 인증의 경우 사용자 이름). |
| 클라이언트 시크릿 | 텍스트 | API 사용자의 OAuth2 클라이언트 시크릿입니다(기본 인증의 경우 비밀번호). 암호화되어 저장됩니다. |

## 가져올 수 있는 엔터티

가져오기 단계는 두 가지이며 가져오는 규모가 다릅니다. 둘 다 `gl_balances`와 `journal_batches`를 대상으로 합니다.

- **Import Fusion Entity** 단계 — 일상적이고 제한된 규모의 가져오기를 위한 직접 OData/BIP 호출입니다.
- **Import Fusion Bulk Extract** 단계 — 대규모 추출을 위한 비동기 FBDI/BIP 내보내기 작업입니다.

두 단계 모두 날짜, 회계 기간, 숫자 잔액/금액 필드에 대한 범위 필터(`ge`/`le`)와 원장이나 통화 같은 불연속 필드에 대한 동등 필터를 지원합니다. 전체 필드 참조는 [Import Fusion Entity](/ko/reference/workflow-steps/oracle-fusion/import-fusion-entity/) 단계와 [Import Fusion Bulk Extract](/ko/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) 단계를 참조하십시오.

## 분개 항목 전기

**Oracle Fusion: Post Journal Entry** 단계는 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 총계정원장 분개 배치를 전기합니다. 배치를 FBDI 파일로 Oracle의 GL_INTERFACE 스테이징 테이블에 쓰고, Journal Import Launcher ESS 작업을 제출한 뒤 최종 상태가 될 때까지 폴링하며, 배치가 전기되었다고 보고하기 전에 확인합니다. 수정은 원본을 편집하지 않고 차변/대변을 맞바꾼 새 역분개를 전기합니다. 필드 참조는 [Oracle Fusion: Post Journal Entry](/ko/reference/workflow-steps/oracle-fusion/oracle-fusion-post/)를, 전체 전기 안내는 [Oracle Fusion에 연결](/ko/guides/connections/oracle-fusion/)을 참조하십시오.

## 알려진 제한 사항

| 제한 사항 | 의미 |
|---|---|
| ESS 작업 지연 | Journal Import Launcher는 동기 호출이 아니라 예약된 작업으로 실행되므로, 전기 실행은 직접 API 쓰기보다 훨씬 오래 걸립니다. |
| 대량 추출 지연 | `import_fusion_bulk_extract`는 FBDI/BIP 내보내기 작업을 기다리므로, `import_fusion_entity`의 직접 경로로는 처리하기에 너무 큰 가져오기에만 사용하십시오. |

## 관련 항목

- [Oracle Fusion에 연결(가이드)](/ko/guides/connections/oracle-fusion/) — 연결 만들기, 테스트, 엔터티 가져오기, 분개 전기를 단계별로 안내합니다.
- [Import Fusion Entity](/ko/reference/workflow-steps/oracle-fusion/import-fusion-entity/)
- [Import Fusion Bulk Extract](/ko/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/)
- [Oracle Fusion: Post Journal Entry](/ko/reference/workflow-steps/oracle-fusion/oracle-fusion-post/)
- [ERP 전기 이력 검토](/ko/guides/connections/erp-post-history/)
