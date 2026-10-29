---
title: Greenplum
description: PlaidCloud에서 Greenplum 데이터베이스 연결을 설정하여 Greenplum 데이터 웨어하우스에 쿼리하고 데이터를 가져오고 내보냅니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/greenplum.md
---

**Greenplum**은 PostgreSQL에서 파생된 대규모 병렬 분석 데이터베이스입니다(원래 Pivotal, 현재 VMware Tanzu). 이 커넥터를 사용하여 PlaidCloud 워크플로에서 Greenplum 테이블을 읽고 씁니다. 와이어 프로토콜이 PostgreSQL과 호환되므로 대부분의 PostgreSQL 도구 관련 고려 사항이 그대로 적용됩니다.

## 업스트림 문서
[Greenplum 문서](https://techdocs.broadcom.com/us/en/vmware-tanzu/data-solutions/tanzu-greenplum/7/greenplum-database/landing-index.html)

## 구성

연결을 만들거나 편집할 때 다음 필드가 나타납니다. 필수 여부는 사용하도록 설정한 인증 옵션에 따라 달라집니다.

### 식별 정보

| 필드 | 유형 | 설명 |
|---|---|---|
| 이름 | 텍스트 | 이 연결의 표시 이름입니다. |
| 별칭 | 텍스트(여러 줄) | 연결에 대한 선택 사항인 별칭 또는 메모입니다. |
| 활성 여부 | 토글 | 연결의 사용 여부입니다. 삭제하지 않고 일시 중지하려면 비활성화합니다. |
| DB 읽기 전용 | 토글 | 연결을 읽기 전용 작업으로 제한합니다. |
| 액세스 유형 | 선택 | 이 연결의 읽기 전용, 쓰기 전용 또는 읽기-쓰기 액세스 수준입니다. |

### 연결

| 필드 | 유형 | 설명 |
|---|---|---|
| DB 호스트 | 텍스트 | 데이터베이스 서버의 호스트 이름 또는 IP 주소입니다. |
| DB 포트 | 숫자 | 데이터베이스 연결의 포트 번호입니다. |
| DB 카탈로그 | 텍스트 | 연결할 데이터베이스, 카탈로그 또는 스키마입니다. |

### 인증

| 필드 | 유형 | 설명 |
|---|---|---|
| DB 사용자 | 텍스트 | 데이터베이스 인증에 사용하는 사용자 이름입니다. |
| SSO 사용 | 토글 | 사용자 이름/암호 대신 SSO(Single Sign-On)로 인증합니다. |
| DB 암호 | 암호 | 데이터베이스 인증에 사용하는 암호입니다. |

### SSL / TLS

| 필드 | 유형 | 설명 |
|---|---|---|
| SSL 사용 | 토글 | SSL/TLS로 연결을 암호화합니다. |
| SSL 모드 | 선택 | SSL 검증 모드입니다(예: disable, require, verify-ca, verify-full). |
| SSL 인증 클라이언트 인증서 | 텍스트(여러 줄) | 상호 TLS 인증에 사용하는 클라이언트 인증서(PEM)입니다. |
| SSL 인증 클라이언트 키 | 텍스트(여러 줄) | 상호 TLS 인증에 사용하는 클라이언트 개인 키(PEM)입니다. |
| SSL 인증 루트 인증서 | 텍스트(여러 줄) | 서버 인증서를 검증하는 데 사용하는 루트 CA 인증서(PEM)입니다. |
| SSL 인증 인증서 해지 | 텍스트(여러 줄) | 환경에서 사용하는 경우 인증서 해지 목록입니다. |

### SSH 터널

| 필드 | 유형 | 설명 |
|---|---|---|
| SSH 사용 | 토글 | SSH 배스천을 통해 연결을 터널링합니다. |
| SSH 호스트 | 텍스트 | SSH 배스천 호스트 이름입니다. |
| SSH 포트 | 숫자 | SSH 배스천 포트입니다(기본값 22). |
| SSH 사용자 | 텍스트 | SSH 배스천 사용자 이름입니다. |
| SSH 암호 | 암호 | SSH 배스천 암호입니다(암호 인증을 사용하는 경우). |
| SSH 인증서 사용 | 토글 | 암호 대신 개인 키로 SSH 배스천에 인증합니다. |
| SSH 개인 키 | 텍스트(여러 줄) | 배스천 인증에 사용하는 SSH 개인 키(PEM)입니다. |
| SSH 호스트 키 | 텍스트(여러 줄) | 배스천 핑거프린트 검증에 사용하는 예상 SSH 호스트 키입니다. |
