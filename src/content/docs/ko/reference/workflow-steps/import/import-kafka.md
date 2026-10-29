---
title: Kafka 가져오기
description: Apache Kafka 토픽의 메시지를 두 오프셋 사이에서 읽어 메시지당 한 행씩 PlaidCloud 테이블로 가져옵니다.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-kafka.md
---

## 설명

하나 이상의 Apache Kafka 토픽의 메시지를 메시지당 한 행씩 프로젝트 테이블로 읽습니다. 이 단계는 시작 오프셋부터 종료 오프셋까지 고정된 범위를 읽으며, `latest`는 단계가 시작될 때 각 파티션의 끝을 의미합니다. 단계가 실행되는 동안 도착하는 메시지는 읽지 않습니다. 이 단계는 [Apache Kafka 연결](/ko/reference/connectors/databases/apache-kafka/)을 통해 Kafka에 접근합니다.

## 소스 및 대상

| 설정 | 필수 | 기능 |
| --- | --- | --- |
| Kafka 연결 | 예 | 데이터를 읽을 연결입니다. |
| 토픽 | 둘 중 하나 | 읽을 토픽이며, 한 줄에 하나씩 입력합니다. |
| 토픽 패턴 | 둘 중 하나 | 읽을 토픽을 선택하는 정규식이며, **토픽** 대신 사용합니다. |
| 대상 테이블 | 예 | 메시지를 저장할 테이블입니다. |

## 메시지 범위

| 설정 | 기본값 | 기능 |
| --- | --- | --- |
| 시작 오프셋 | `earliest` | `earliest`, `latest`, 또는 `{"orders": {"0": 1200, "1": 980}}`와 같이 파티션마다 오프셋을 지정하는 JSON입니다. JSON에서 `-2`는 earliest를, `-1`은 latest를 의미합니다. |
| 종료 오프셋 | `latest` | `latest` 또는 시작 오프셋과 같은 형식의 JSON입니다. |
| 메시지 제한(0 = 전체) | `0` | 읽을 최대 메시지 수입니다. `0`이면 범위 내 모든 메시지를 읽습니다. |
| 유휴 시간 제한(초) | `10` | 새 메시지 없이 이 시간(초)이 지나면 읽기를 종료합니다. |
| 시간 제한(초) | `10800` | 읽기를 실행할 수 있는 최대 시간입니다. |

오프셋에는 `{name}` 형식으로 쓴 워크플로 변수를 사용할 수 있습니다.

## 메시지 값

| 설정 | 기능 |
| --- | --- |
| 값 형식 | **JSON**, **텍스트** 또는 **Avro**입니다. |
| Avro 스키마(JSON) | 메시지 값의 Avro 스키마입니다. 형식이 **Avro**이면 필수입니다. |
| 추가 컨슈머 설정(JSON) | `{"fetch.min.bytes": 1}`와 같이 JSON 객체로 지정하는 추가 Kafka 컨슈머 설정입니다. PlaidCloud에서 허용하는 설정만 사용할 수 있습니다. |

## 열 매핑

매핑 탭에서 열을 하나 이상 매핑하십시오. 열은 메시지의 부분인 `key`, `value`, `topic`, `partition`, `offset`, `timestamp`, `timestamp_type`, `headers` 중 하나를 읽거나, 구문 분석된 값의 필드를 경로로 읽습니다. 이 단계에는 **소스 검사**가 없으므로 열을 직접 입력하십시오.

## 관련 항목

- [Kafka 내보내기](/ko/reference/workflow-steps/export/export-kafka/)
- [Apache Kafka 연결](/ko/reference/connectors/databases/apache-kafka/)
