---
title: Apache Kafka
description: PlaidCloud에서 Apache Kafka 연결을 설정하여 토픽 메시지를 테이블로 읽어 오고 테이블 행을 메시지로 전송합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/apache-kafka.md
---

**Apache Kafka**는 분산 이벤트 스트리밍 플랫폼입니다. 이 연결을 [Kafka 가져오기](/ko/reference/workflow-steps/import/import-kafka/) 단계와 함께 사용하면 토픽의 메시지를 테이블로 읽어 올 수 있고, [Kafka 내보내기](/ko/reference/workflow-steps/export/export-kafka/) 단계와 함께 사용하면 테이블의 각 행을 메시지로 전송할 수 있습니다. 연결을 만들려면 연결 유형으로 **Apache Kafka**를 선택합니다.

## 업스트림 문서
[Apache Kafka 문서](https://kafka.apache.org/documentation/)

## 구성

### Kafka 연결

| 필드 | 필수 | 설명 |
|---|---|---|
| 브로커 | 예 | 연결할 브로커를 쉼표로 구분하여 입력합니다(예: `broker1:9092,broker2:9092`). |
| 보안 프로토콜 | 아니요 | `PLAINTEXT`(기본값), `SSL`, `SASL_PLAINTEXT` 또는 `SASL_SSL`입니다. |
| 세션 제한 시간(ms) | 아니요 | 브로커가 PlaidCloud로부터 응답이 없는 상태로 대기하다가 컨슈머 그룹에서 제외하기까지의 시간입니다. 최소 1000입니다. |

### SASL 자격 증명

보안 프로토콜이 `SASL_PLAINTEXT` 또는 `SASL_SSL`일 때 사용합니다.

| 필드 | 설명 |
|---|---|
| SASL 메커니즘 | `PLAIN`(기본값), `SCRAM-SHA-256`, `SCRAM-SHA-512` 또는 `OAUTHBEARER`입니다. Kerberos(`GSSAPI`)는 사용할 수 없습니다. |
| 사용자 | `PLAIN` 및 `SCRAM`에서 연결에 사용할 사용자입니다. |
| 암호 | `PLAIN` 및 `SCRAM`에서 사용하는 사용자의 암호입니다(쓰기 전용). |

### OAuth(OAUTHBEARER)

SASL 메커니즘이 `OAUTHBEARER`일 때 사용합니다. PlaidCloud는 OAuth 클라이언트 자격 증명 부여 방식으로 ID 공급자에서 토큰을 가져오며, 토큰이 만료되면 새 토큰을 가져옵니다.

| 필드 | 설명 |
|---|---|
| 토큰 엔드포인트 URL | ID 공급자의 토큰 엔드포인트입니다. 공용 인터넷상의 `https` 주소여야 합니다. |
| 클라이언트 ID | 토큰을 요청할 클라이언트입니다. 필수입니다. |
| 클라이언트 시크릿 | 클라이언트의 시크릿입니다(쓰기 전용). 필수입니다. |
| 범위 | 공급자가 필요로 하는 경우 요청할 범위입니다. |
| SASL 확장 | 토큰과 함께 전송되는 선택 사항인 `key=value` 쌍으로, 쉼표로 구분합니다. 예를 들어 Confluent Cloud에서 요구하는 `logicalCluster` 및 `identityPoolId`가 있습니다. |

### TLS

| 필드 | 설명 |
|---|---|
| CA 인증서(PEM) | 브로커 인증서를 서명한 인증 기관입니다. 공용 인증 기관이 아닌 경우에 사용합니다. 편집 시 비워 두면 저장된 인증서가 유지됩니다. |
