---
title: 배부 빠른 시작
description: 원천, 동인, 대상 매핑을 단계별로 안내하는 이 가이드로 PlaidCloud에서 기본 비용 배부를 빠르게 설정하십시오.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/allocations-quick-start.md
---

이 안내에서는 원시 비용 데이터에서 시작하여 약 30분 안에 작동하는 배부 모델을 만드는 과정을 다룹니다.

## 준비 사항

- 테이블이 두 개 이상 있는 프로젝트:
  - **배부할 값** — 분배하려는 비용(또는 수익이나 수량)입니다. 원천 단위마다 한 행이며, 금액을 담은 열이 하나 있어야 합니다.
  - **동인 데이터** — 분배의 기준입니다. 인원 수, 면적, 거래 건수, 매출 등 배부의 *기준*으로 삼으려는 모든 값이 해당됩니다.
- 원천과 대상을 연결하는 차원(비용 센터, 부서, 제품 등 모델에 맞는 분류 체계).

아직 이러한 항목이 모두 준비되지 않았다면 [테이블 및 뷰](/ko/guides/data/)와 [차원](/ko/guides/dimensions/) 가이드에서 입력 데이터를 로드하는 방법을 확인하십시오.

## 단계

1. 배부할 값 테이블과 동인 테이블이 있는 **프로젝트를 엽니다**.
2. **새 워크플로를 만듭니다.** 배부는 항상 워크플로 안에서 실행되며, 워크플로 밖에서 테이블에 직접 작동하지 않습니다.
3. **배부 단계를 추가합니다.** 워크플로 안에서 **배부** 범주의 단계를 추가합니다. 동인 기반의 간단한 분배에는 **Allocation Rules**로 시작하는 것이 가장 일반적입니다.
4. **원천을 구성합니다.** 단계가 배부할 값 테이블을 가리키도록 하고 배부할 금액이 있는 열을 선택합니다.
5. **동인을 구성합니다.** 단계가 동인 테이블을 가리키도록 하고 동인 값이 있는 열을 선택합니다.
6. **차원을 매핑합니다.** 각 테이블에서 차원 멤버를 나타내는 열을 지정합니다. 배부 단계는 이 열을 사용하여 원천 행을 동인 행과 매칭합니다.
7. **단계를 실행합니다.** 출력은 분배된 금액마다 한 행이 있는 새 테이블입니다.
8. **결과를 검사합니다.** 합계가 예상과 일치하는지 확인합니다. 배부된 금액의 합계는 원천 금액의 합계와 같아야 합니다(반올림 허용 오차 내).

## 일반적인 후속 작업

- **재귀적 분배** — 대상 자체에 추가 배부를 위한 동인이 포함된 경우 [재귀 배부](/ko/guides/allocations/setup/recursive-allocations/)를 참조하십시오.
- **배부를 위한 행 태깅** — *어떤* 행이 어떤 대상으로 배부될지 결정하려면 [규칙 기반 태깅](/ko/guides/allocations/getting-started/rule-based-tagging/)을 참조하십시오.
- **예상치 못한 결과 조사** — 합계가 일치하지 않거나 특정 행이 잘못된 것처럼 보이면 [배부 문제 해결](/ko/guides/allocations/results/troubleshooting-allocations/)을 참조하십시오.

## 다음 단계

- [배부는 왜 유용한가요?](/ko/guides/allocations/getting-started/why-are-allocations-useful/) — 사용 시기
- [배부 구성](/ko/guides/allocations/setup/configure-an-allocation/) — 더 자세한 구성 참조
- [배부 단계 유형](/ko/reference/workflow-steps/allocation/) — 배부 범주의 모든 워크플로 단계
