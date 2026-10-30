---
title: 배부 단계
description: 차원에 걸쳐 값을 배부하는 워크플로 단계(분할, 규칙, 규칙 기반 태깅)로, 비용 배부, 차지백, 이전 가격 책정에 사용합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/allocation/index.md
---

비용 배부, 차지백, 이전 가격 책정 및 유사한 값 분배 문제를 위한 워크플로 단계입니다. 각 단계는 드라이버 데이터와 방법을 사용하여 소스 행 집합의 값을 대상 집합으로 분배합니다.

## 단계

- [Allocation Rules 단계](/ko/reference/workflow-steps/allocation/allocation-rules/) — 명시적 조건으로 배부 규칙을 정의하고 적용합니다.
- [Allocation Split 단계](/ko/reference/workflow-steps/allocation/allocation-split/) — 드라이버 테이블을 사용하여 소스 값을 대상에 나눕니다.
- [규칙 기반 태깅](/ko/reference/workflow-steps/allocation/rule-based-tagging/) — 배부하기 전에 차원의 속성으로 행에 태그를 지정합니다.

## 관련 항목

- [배부(가이드)](/ko/guides/allocations/) — 배부 문제를 위한 개념과 엔드투엔드 워크플로.
- [차원(가이드)](/ko/guides/dimensions/) — 배부가 값을 분배하는 대상 계층을 설정합니다.
