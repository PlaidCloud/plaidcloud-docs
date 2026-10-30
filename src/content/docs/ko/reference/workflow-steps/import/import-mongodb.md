---
title: MongoDB 가져오기
description: MongoDB 컬렉션 또는 집계 파이프라인의 결과를 워크플로 단계로 PlaidCloud 테이블에 읽어 옵니다.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-mongodb.md
---

## 설명

MongoDB 컬렉션의 문서를 문서당 한 행씩 프로젝트 테이블로 읽습니다. 필요한 문서만 읽으려면 필터를 사용하고, 문서를 가져오기 전에 MongoDB에서 재구성하려면 집계 파이프라인을 사용하십시오. 이 단계는 [MongoDB 연결](/ko/reference/connectors/databases/mongodb/)을 통해 MongoDB에 접근합니다.

## 소스 및 대상

| 설정 | 필수 | 기능 |
| --- | --- | --- |
| MongoDB 연결 | 예 | 데이터를 읽을 연결입니다. |
| 데이터베이스 | 아니요 | 읽을 데이터베이스입니다. 비워 두면 연결의 **기본 데이터베이스**를 사용합니다. |
| 컬렉션 | 예 | 읽을 컬렉션입니다. |
| 대상 테이블 | 예 | 문서를 저장할 테이블입니다. 뷰가 아니라 테이블이어야 합니다. |

## 쿼리

| 설정 | 기능 |
| --- | --- |
| 필터(JSON) | `{"status": "open"}`과 같이 JSON 객체로 지정하는 MongoDB 쿼리 필터입니다. 일치하는 문서만 읽습니다. |
| 집계 파이프라인(JSON) | `[{"$match": {"status": "open"}}]`과 같이 JSON 배열로 지정하는 집계 파이프라인입니다. 설정하면 컬렉션을 필터링하는 대신 집계합니다. `$out` 또는 `$merge` 단계가 있는 파이프라인은 MongoDB에 쓰게 되므로 거부됩니다. |
| 행 제한(0 = 전체) | 읽을 최대 문서 수입니다. `0`이면 모든 문서를 읽습니다. |
| 시간 제한(초) | MongoDB가 읽기를 중단하기 전까지 소요할 수 있는 시간입니다. |
| 열 결정에 사용할 문서 수 | 단계에 열을 선언하지 않은 경우, 처음부터 몇 개의 문서로 열과 열 유형을 결정할지 지정합니다. 문서가 가진 각 최상위 필드가 열이 됩니다. 기본값은 1000입니다. |

필터와 파이프라인에는 `{"region": "{region}"}`처럼 `{name}` 형식으로 쓴 워크플로 변수를 사용할 수 있습니다. 각 변수의 값은 단일 JSON 문자열 또는 숫자로 삽입되므로, 변수로 쿼리에 키나 연산자를 추가할 수 없습니다. 정의되지 않은 변수가 있으면 해당 변수 이름을 명시한 오류와 함께 단계가 중지됩니다.

## 열 매핑

매핑 탭에서 각 문서 필드를 대상 테이블의 열에 매핑하십시오. 열은 이름이 같은 문서 필드를 읽습니다. 존재하지 않는 컬렉션은 경고와 함께 완료되며 대상 테이블은 비어 있게 됩니다.

## 관련 항목

- [MongoDB 내보내기](/ko/reference/workflow-steps/export/export-mongodb/)
- [MongoDB 연결](/ko/reference/connectors/databases/mongodb/)
