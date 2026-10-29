---
title: MongoDB
description: PlaidCloud에서 MongoDB 연결을 설정하여 컬렉션을 테이블로 읽고 테이블을 문서로 다시 씁니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/mongodb.md
---

**MongoDB**는 문서 데이터베이스입니다. 이 연결을 [MongoDB 가져오기](/ko/reference/workflow-steps/import/import-mongodb/) 단계와 함께 사용하면 컬렉션 또는 집계 파이프라인의 결과를 테이블로 읽을 수 있고, [MongoDB 내보내기](/ko/reference/workflow-steps/export/export-mongodb/) 단계와 함께 사용하면 테이블을 문서로 다시 쓸 수 있습니다. 연결을 만들려면 연결 유형으로 **MongoDB**를 선택합니다.

## 업스트림 문서
[MongoDB 문서](https://www.mongodb.com/docs/).

## 구성

### MongoDB 연결

| 필드 | 필수 | 설명 |
|---|---|---|
| 호스트 | 예 | 서버의 호스트 이름입니다. |
| SRV 주소 사용(mongodb+srv://, 포트 없음) | 아니요 | MongoDB Atlas처럼 DNS 시드 목록을 통해 연결합니다. 포트는 사용되지 않습니다. |
| 포트 | 아니요 | 서버의 포트입니다. 기본값은 `27017`입니다. |
| 기본 데이터베이스 | 아니요 | 단계에서 데이터베이스를 지정하지 않을 때 사용하는 데이터베이스입니다. |

### 인증 자격 증명

| 필드 | 설명 |
|---|---|
| 사용자 | 연결에 사용할 사용자입니다. |
| 비밀번호 | 사용자의 비밀번호입니다(쓰기 전용). |

### 옵션

| 필드 | 설명 |
|---|---|
| 연결 옵션 | `authSource=admin&tls=true`처럼 `&`로 연결한 MongoDB URI 옵션입니다. PlaidCloud에서 허용하는 옵션만 사용할 수 있습니다. 편집할 때 비워 두면 저장된 옵션이 유지됩니다. |

### TLS

| 필드 | 설명 |
|---|---|
| CA 인증서(PEM) | 서버 인증서에 서명한 인증 기관이며, 공인 기관이 아닌 경우에 사용합니다. 편집할 때 비워 두면 저장된 인증서가 유지됩니다. |
