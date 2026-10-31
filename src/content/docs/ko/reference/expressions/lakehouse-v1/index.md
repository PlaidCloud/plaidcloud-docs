---
title: Lakehouse v1 식
description: Databend SQL 함수를 기반으로 하며 func. 접두사를 사용하는 SQLAlchemy 참조를 포함한 Lakehouse v1 식입니다.
sidebar:
  label: Lakehouse v1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/index.md
---

Lakehouse v1은 [Databend](https://databend.com/) SQL 엔진을 기반으로 합니다. 아래 각 함수에 대해 이 사이트는 PlaidCloud 방식의 구문과 예제를 제공합니다. 모든 예외 사례와 인수 변형을 포함한 정식 업스트림 참조는 **[Databend SQL 함수 참조](https://docs.databend.com/sql/sql-functions/)** 를 참조하십시오.

## 스칼라 함수

- [배열 함수](./00-array-functions) — 배열 연산을 수행합니다
- [비트 식 함수](./01-bitmap-functions) — 비트 연산과 조작을 수행합니다
- [조건 식 함수](./03-conditional-functions) — 조건 논리와 case 문을 구현합니다
- [컨텍스트 함수](./15-context-functions) — 현재 SQL 실행 컨텍스트에 대한 정보를 제공합니다
- [변환 함수](./02-conversion-functions) — 데이터 유형을 변환하고 값을 캐스트합니다
- [날짜 및 시간 함수](./05-datetime-functions) — 날짜와 시간을 조작하고 서식을 지정합니다
- [지리 공간 함수](./09-geo-functions) — 지리 공간 데이터를 처리하고 조작합니다
- [지오메트리 함수](./09-geometry-functions) — 지리 공간 지오메트리 데이터를 처리하고 조작합니다
- [간격 함수](./05-interval-functions) — 시간 간격을 만들고 조작합니다
- [맵 함수](./10-map-functions) — 맵 데이터 구조를 만들고 조작합니다
- [숫자 함수](./04-numeric-functions) — 계산과 숫자 연산을 수행합니다
- [검색 함수](./10-search-functions) — 식을 사용하여 값을 찾습니다
- [반정형 및 정형 데이터 함수](./10-semi-structured-functions) — JSON 및 기타 정형 데이터 형식을 다룹니다
- [문자열 함수](./06-string-functions) — 문자열을 조작하고 정규식 연산을 수행합니다

## 집계 함수

- [집계 함수](./07-aggregate-functions) — 합계, 평균, 개수 등의 요약을 계산합니다
- [윈도우 함수](./08-window-functions) — 지정한 행 범위에 대한 집계 계산을 제공합니다

## AI 함수

- [AI 함수](./11-ai-functions) — AI 및 머신러닝 기능을 활용합니다

## 전문 함수

- [해시 함수](./12-hash-functions) — 데이터 보안 및 비교를 위한 해시 값을 생성합니다
- [IP 주소 함수](./14-ip-address-functions) — IP 주소 데이터를 조작하고 분석합니다
- [UUID 함수](./13-uuid-functions) — UUID를 생성하고 조작합니다

## 시스템 및 테이블 함수

- [시퀀스 함수](./18-sequence-functions) — 순차 값을 생성합니다
- [시스템 함수](./16-system-functions) — 시스템 수준 정보에 액세스하고 제어 작업을 수행합니다
- [테이블 함수](./17-table-functions) — 표 형식으로 결과를 반환합니다

## 기타 함수

- [딕셔너리 함수](./19-dictionary-functions) — 딕셔너리 데이터 구조를 다룹니다
- [기타 함수](./20-other-functions) — 여러 기타 함수 모음
- [테스트 함수](./19-test-functions) — 테스트 목적으로 사용하는 함수
