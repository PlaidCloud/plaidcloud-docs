---
title: Lakehouse v2 식
description: SQLAlchemy 참조와 함께 제공되는 StarRocks 4.1 SQL 함수 기반의 Lakehouse v2 식입니다.
sidebar:
  label: Lakehouse v2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/index.md
---

Lakehouse v2는 [StarRocks](https://www.starrocks.io/) 4.1을 기반으로 합니다. 아래 각 함수에 대해 이 사이트는 PlaidCloud에 맞춘 구문과 예제를 제공합니다. 모든 예외 상황과 인수 변형을 포함한 공식 업스트림 참조는 **[StarRocks SQL 함수 참조](https://docs.starrocks.io/docs/sql-reference/sql-functions/)** 를 확인하십시오.

## 집계 함수

- [집계 함수](./01-aggregate-functions) — 합계, 평균, 개수 등의 요약 값을 계산합니다.
- [백분위수 함수](./15-percentile-functions) — 백분위수 값을 계산하고 백분위수 상태를 관리합니다.

## 스칼라 함수

- [배열 함수](./02-array-functions) — 배열 연산을 수행합니다.
- [바이너리 함수](./03-binary-functions) — 바이너리와 문자열 형식 간에 변환합니다.
- [비트 함수](./04-bit-functions) — 비트 단위 연산을 수행합니다.
- [비트맵 함수](./05-bitmap-functions) — 비트맵 연산과 조작을 수행합니다.
- [조건 함수](./06-condition-functions) — 조건 논리와 CASE 문을 구현합니다.
- [암호화 함수](./07-cryptographic-functions) — 데이터를 암호화, 복호화, 해시합니다.
- [날짜 및 시간 함수](./08-date-time-functions) — 날짜와 시간을 조작하고 서식을 지정합니다.
- [딕셔너리 함수](./09-dictionary-functions) — 딕셔너리 테이블에서 값을 조회합니다.
- [해시 함수](./10-hash-functions) — MurmurHash와 xxHash로 해시 값을 생성합니다.
- [JSON 함수](./11-json-functions) — JSON 데이터를 생성, 쿼리, 조작합니다.
- [맵 함수](./12-map-functions) — 맵 데이터 구조를 생성하고 조작합니다.
- [수학 함수](./13-math-functions) — 계산과 숫자 연산을 수행합니다.
- [패턴 일치 함수](./14-pattern-matching-functions) — LIKE와 정규식으로 문자열을 일치시킵니다.
- [스칼라 함수(HLL)](./16-scalar-functions) — HyperLogLog 카디널리티 추정 함수입니다.
- [공간 함수](./17-spatial-functions) — 지리 공간 데이터를 처리하고 조작합니다.
- [문자열 함수](./18-string-functions) — 문자열을 조작하고 텍스트 연산을 수행합니다.
- [구조체 함수](./19-struct-functions) — 구조체 데이터 형식을 생성하고 사용합니다.
- [Variant 함수](./22-variant-functions) — VARIANT 데이터 형식을 쿼리하고 검사합니다.

## 테이블 함수

- [테이블 함수](./20-table-functions) — 결과를 표 형식으로 반환합니다.

## 유틸리티 및 메타 함수

- [유틸리티 함수](./21-utility-functions) — 시스템 정보와 세션 유틸리티에 액세스합니다.
- [메타 함수](./23-meta-functions) — 구체화된 뷰, 메모리, 진단 정보를 검사합니다.

## Lakehouse 관리

- [Lakehouse 관리](./lakehouse-management/) — 쿼리를 실행하고, 카탈로그를 탐색하고, 창고를 관리하고, 컴퓨팅을 모니터링합니다.
