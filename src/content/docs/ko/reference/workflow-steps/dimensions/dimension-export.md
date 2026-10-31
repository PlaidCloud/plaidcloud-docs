---
title: Dimension Export 단계
description: 워크플로 단계에서 PlaidCloud의 차원 데이터를 내보내 계층 구조를 파일로 저장하거나 다른 시스템으로 전송합니다.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-export.md
---

## 설명

차원을 평면 테이블 형태의 PlaidCloud 테이블로 펼칩니다. 멤버당 한 행이며, 상위 항목, 레벨, 값, 별칭, 속성에 대한 열이 있습니다. PlaidCloud의 계층 형식을 직접 읽을 수 없는 다운스트림 시스템에서 차원 구조를 쿼리하거나 조인하거나 입력으로 사용해야 할 때 이 단계를 사용하십시오.

일반적인 용도: 차원을 테이블로 내보낸 다음, 일반 내보내기 단계를 사용하여 외부 시스템(BI 도구, 보고 데이터베이스, 파일 전달)에 씁니다.

## 모든 계층 내보내기

**모든 계층**을 선택하면 모든 계층을 하나의 테이블로 가져옵니다. 결과에는 각 행이 속한 계층의 이름을 나타내는 `hierarchy` 열이 추가되며, 행은 기본 계층이 먼저 오고 그다음에 대체 계층이 알파벳순으로 정렬됩니다.
