---
title: Kafka 내보내기
description: PlaidCloud 테이블의 각 행을 Apache Kafka 토픽에 메시지로 전송합니다.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-kafka.md
---

## 설명

프로젝트 테이블의 각 행을 Apache Kafka 토픽에 메시지 하나로 전송합니다. 전송된 메시지는 되돌릴 수 없으므로 단계를 다시 실행하면 행이 다시 전송됩니다. 이 단계는 [Apache Kafka 연결](/ko/reference/connectors/databases/apache-kafka/)을 통해 Kafka에 접속합니다.

## 소스 및 대상

| 설정 | 필수 | 기능 |
| --- | --- | --- |
| 소스 테이블 | 예 | 전송할 테이블입니다. |
| Kafka 연결 | 예 | 전송에 사용할 연결입니다. |
| 토픽 | 예 | 모든 행을 전송할 토픽입니다. |

## 메시지

| 설정 | 기능 |
| --- | --- |
| 키 열 | 값이 메시지 키가 되는 열입니다. 비워 두면 키 없이 메시지를 전송합니다. |
| 값 열 | 메시지 값을 구성하는 열이며 쉼표로 구분합니다. 비워 두면 모든 열을 전송합니다. |
| 파티션 열 | 각 메시지의 파티션을 지정하는 정수 열입니다. 비워 두면 Kafka가 선택합니다. |
| 값 형식 | **JSON**, **텍스트** 또는 **Avro**입니다. |
| Avro 스키마(JSON) | 메시지 값의 Avro 스키마입니다. 형식이 **Avro**이면 필수입니다. |

## 전송

| 설정 | 기본값 | 기능 |
| --- | --- | --- |
| 전송 대기 시간(초) | `60` | 모든 메시지를 Kafka가 확인할 때까지 단계가 마지막에 기다리는 시간입니다. |
| 제한 시간(초) | `10800` | 전송이 실행될 수 있는 최대 시간입니다. |
| 추가 프로듀서 설정(JSON) | — | `{"compression.type": "gzip"}`와 같이 JSON 개체로 지정하는 추가 Kafka 프로듀서 설정입니다. PlaidCloud가 허용하는 설정만 허용됩니다. |

## 관련 항목

- [Kafka 가져오기](/ko/reference/workflow-steps/import/import-kafka/)
- [Apache Kafka 연결](/ko/reference/connectors/databases/apache-kafka/)
