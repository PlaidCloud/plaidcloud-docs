---
title: 모델링 학습 경로
description: PlaidCloud 모델링 프랙티셔너 및 엑스퍼트 랩에 앞서 읽어야 할 내용과 각 랩에서 요구하는 작업을 안내합니다.
sidebar:
  label: 모델링
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/modeling.md
---

모델링 트랙은 차원과 배부를 다룹니다. 계층을 만들고, 동인에 따라 비용을 배분하고, 결과가 일치함을 증명합니다. [파운데이션](/ko/guides/certification/foundations/) 경로부터 시작하십시오. 랩이 진행되는 방식은 [PlaidCloud 인증](/ko/guides/certification/)을 참조하십시오.

## 프랙티셔너

### 읽는 순서

1. [차원 시작하기](/ko/guides/dimensions/getting-started/)
2. [계층 관리](/ko/guides/projects/managing-hierarchies/)
3. [차원 계층 설계](/ko/get-started/tutorials/design-a-dimension/)
4. [배부 빠른 시작](/ko/guides/allocations/getting-started/allocations-quick-start/)
5. [Allocation Split 단계](/ko/reference/workflow-steps/allocation/allocation-split/)
6. [배부 모델 만들기](/ko/get-started/tutorials/build-an-allocation/)
7. [배부 결과](/ko/guides/allocations/results/allocation-results/)
8. [워크플로 로그 보기](/ko/guides/workflows/viewing-workflow-log/)

### 랩에서 요구하는 작업

랩의 이름은 *모델링: 공유 IT 비용 배분*입니다.

테이블에 각 부서와 그 상위 부서가 나열되어 있습니다. 기본 계층이 정확히 그 트리인 차원을 만듭니다. 그런 다음 랩의 워크플로에서 비용 풀을 부서의 인원수에 비례하여 부서에 배분하고, 부서마다 결과 행을 하나씩 만듭니다. 두 번째 드라이버 테이블도 있지만, 이 풀의 동인은 아닙니다.

랩은 워크플로가 실행되는지, 계층이 올바른지, 배분된 합계가 원천과 일치하는지, 그리고 각 부서가 올바른 금액을 받는지 검사합니다.

## 엑스퍼트

엑스퍼트 랩은 시간 제한이 있습니다. 시작한 시점부터 4시간이 주어집니다.

### 읽는 순서

1. [배부 구성](/ko/guides/allocations/setup/configure-an-allocation/)
2. [배부 문제 해결](/ko/guides/allocations/results/troubleshooting-allocations/)
3. [MCP 연결 AI 에이전트로 배부 추적](/ko/integrations/ai-coding-agents/tracing-allocations/)
4. [배부 결과](/ko/guides/allocations/results/allocation-results/)
5. [동인 가정 분석 해 보기](/ko/guides/allocations/results/driver-what-if/)
6. [계층 관리](/ko/guides/projects/managing-hierarchies/)

### 랩에서 요구하는 작업

랩의 이름은 *모델링 전문가: 배분 모델 수리*입니다.

2단계 배부 모델이 더 이상 원장과 일치하지 않고, 일부 부서는 분명히 잘못되어 있습니다. 원인을 추적하여 모델을 수정합니다. 각 단계는 자신의 풀을 정확히 배분하고, 부서별 합계는 올바르며 원장과 일치하고, 부서 차원에는 실제로 존재하는 부서만 있어야 합니다. 어떤 것도 일치시키기 위해 조정 행을 사용해서는 안 됩니다. 그런 다음 IT 비용을 인원수 대신 바닥 면적으로 배부했을 때 각 부서가 부담하게 될 금액을 보여 주는 단계를 추가합니다.

랩은 워크플로가 실행되는지, 계층이 올바른지, 각 단계와 부서별 합계가 원장과 일치하는지, 각 부서가 올바른 합계를 받는지, 그리고 바닥 면적 시나리오가 올바른지 검사합니다.
