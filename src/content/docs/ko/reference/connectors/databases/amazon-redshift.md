---
title: Amazon Redshift
description: PlaidCloud에서 Amazon Redshift 데이터베이스 연결을 설정하여 Redshift 웨어하우스의 데이터를 쿼리, 가져오기, 내보내기합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/amazon-redshift.md
---

**Amazon Redshift**는 대규모 데이터 세트에 대한 분석 워크로드를 위해 설계된 AWS의 관리형 클라우드 데이터 웨어하우스입니다. 이 커넥터를 사용하면 PlaidCloud 워크플로에서 Redshift 테이블을 읽고 쓸 수 있습니다. 커넥터는 PostgreSQL 와이어 프로토콜을 사용하며, 인증에는 표준 데이터베이스 자격 증명 또는 IAM 기반 임시 자격 증명을 사용합니다.

## 업스트림 문서
가이드와 참조 자료는 [Amazon Redshift 문서](https://docs.aws.amazon.com/redshift/)를 참조하십시오.

## 구성

이 필드는 연결을 만들거나 편집할 때 표시됩니다. 필수 여부는 사용하도록 설정한 인증 옵션에 따라 달라집니다.

### 식별

| 필드 | 유형 | 설명 |
|---|---|---|
| Name | 텍스트 | 이 연결의 표시 이름입니다. |
| Alias | 텍스트(여러 줄) | 연결에 대한 선택적 별칭 또는 메모입니다. |
| Is active | 토글 | 연결의 사용 여부입니다. 삭제하지 않고 일시 중지하려면 사용 안 함으로 설정합니다. |
| Db read only | 토글 | 연결을 읽기 전용 작업으로 제한합니다. |
| Access type | 선택 | 이 연결의 읽기 전용, 쓰기 전용 또는 읽기-쓰기 액세스 수준입니다. |

### 연결

| 필드 | 유형 | 설명 |
|---|---|---|
| Db host | 텍스트 | 데이터베이스 서버의 호스트 이름 또는 IP 주소입니다. |
| Db port | 숫자 | 데이터베이스 연결의 포트 번호입니다. |
| Db catalog | 텍스트 | 연결할 데이터베이스, 카탈로그 또는 스키마입니다. |

### 인증

| 필드 | 유형 | 설명 |
|---|---|---|
| Db user | 텍스트 | 데이터베이스 인증에 사용할 사용자 이름입니다. |
| Use sso | 토글 | 사용자 이름/비밀번호 대신 싱글 사인온으로 인증합니다. |
| Db password | 비밀번호 | 데이터베이스 인증에 사용할 비밀번호입니다. |

### SSL / TLS

| 필드 | 유형 | 설명 |
|---|---|---|
| Use ssl | 토글 | SSL/TLS로 연결을 암호화합니다. |
| Ssl mode | 선택 | SSL 확인 모드입니다(예: disable, require, verify-ca, verify-full). |
| Ssl auth client cert | 텍스트(여러 줄) | 상호 TLS 인증에 사용하는 클라이언트 인증서(PEM)입니다. |
| Ssl auth client key | 텍스트(여러 줄) | 상호 TLS 인증에 사용하는 클라이언트 개인 키(PEM)입니다. |
| Ssl auth root cert | 텍스트(여러 줄) | 서버 인증서를 확인하는 데 사용하는 루트 CA 인증서(PEM)입니다. |
| Ssl auth cert revoke | 텍스트(여러 줄) | 사용 환경에서 인증서 해지 목록을 사용하는 경우 해당 목록입니다. |

### SSH 터널

| 필드 | 유형 | 설명 |
|---|---|---|
| Use ssh | 토글 | SSH 배스천을 통해 연결을 터널링합니다. |
| Ssh host | 텍스트 | SSH 배스천 호스트 이름입니다. |
| Ssh port | 숫자 | SSH 배스천 포트입니다(기본값 22). |
| Ssh user | 텍스트 | SSH 배스천 사용자 이름입니다. |
| Ssh password | 비밀번호 | SSH 배스천 비밀번호입니다(비밀번호 인증을 사용하는 경우). |
| Use ssh cert | 토글 | 비밀번호 대신 개인 키로 SSH 배스천에 인증합니다. |
| Ssh private key | 텍스트(여러 줄) | 배스천 인증에 사용하는 SSH 개인 키(PEM)입니다. |
| Ssh host key | 텍스트(여러 줄) | 배스천 지문 확인에 사용하는 예상 SSH 호스트 키입니다. |
