---
title: MongoDB 내보내기
description: PlaidCloud 테이블을 MongoDB 컬렉션에 삽입, 교체, 업데이트 또는 업서트한 문서로 기록합니다.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-mongodb.md
---

## 설명

프로젝트 테이블의 각 행을 문서로 MongoDB 컬렉션에 기록합니다. 컬렉션이 없으면 만들어집니다. 이 단계는 [MongoDB 연결](/ko/reference/connectors/databases/mongodb/)을 통해 MongoDB에 접속합니다.

## 소스 및 대상

| 설정 | 필수 | 기능 |
| --- | --- | --- |
| 소스 테이블 | 예 | 기록할 테이블입니다. |
| MongoDB 연결 | 예 | 기록에 사용할 연결입니다. |
| 데이터베이스 | 아니요 | 기록할 데이터베이스입니다. 비워 두면 연결의 **기본 데이터베이스**를 사용합니다. |
| 컬렉션 | 예 | 기록할 컬렉션입니다. |

## 쓰기 옵션

| 설정 | 기능 |
| --- | --- |
| 쓰기 모드 | **행마다 문서 삽입**(기본값), **일치하는 문서 교체**, **일치하는 문서의 필드 업데이트**, **일치하는 문서를 교체하거나 삽입** 또는 **일치하는 문서의 필드를 업데이트하거나 삽입**입니다. |
| 일치 열 | 문서를 식별하는 열이며 쉼표로 구분합니다. 삽입을 제외한 모든 모드에서 필수입니다. |
| 쓰기 전에 컬렉션의 모든 문서 삭제 | 컬렉션을 먼저 비워 이번 실행의 행만 남도록 합니다. |
| 첫 번째 쓰기 실패 시 중지 | MongoDB가 거부한 첫 번째 문서에서 중지합니다. 선택을 해제하면 나머지를 계속 진행합니다. |
| 쓰기가 저널에 반영될 때까지 대기 | MongoDB가 각 배치를 저널에 기록할 때까지 기다립니다. |
| Write Concern | 비워 두면 연결의 값을 사용하며, 서버 수 또는 `majority`를 지정할 수 있습니다. |
| 요청당 문서 수 | 각 요청으로 전송하는 문서 수입니다. |

삽입은 단계를 실행할 때마다 문서를 다시 추가합니다. 교체 또는 업데이트 모드는 단계를 몇 번 실행해도 컬렉션이 동일하게 유지되므로, 워크플로가 같은 행에 대해 두 번 실행될 수 있는 경우에는 이들 중 하나를 사용하십시오.

## 관련 항목

- [MongoDB 가져오기](/ko/reference/workflow-steps/import/import-mongodb/)
- [MongoDB 연결](/ko/reference/connectors/databases/mongodb/)
