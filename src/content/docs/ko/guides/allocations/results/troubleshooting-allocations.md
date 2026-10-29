---
title: 배부 문제 해결
description: 일반적인 오류, 구성 문제, 결과 디버깅 기법을 포함하여 PlaidCloud 배부 문제를 해결합니다.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/troubleshooting-allocations.md
---

## 배부 단계가 저장되지 않는 이유

PlaidCloud는 배부 단계를 저장할 때 열 매핑을 검사합니다. 실행할 수 없는 매핑은 그 시점에 거부되며, 수정해야 할 항목을 나열하는 **저장할 수 없음** 알림이 표시되고 양식이 문제가 있는 탭으로 전환됩니다. 이전에는 이러한 단계가 아무 문제 없이 저장된 후 실행 도중 워크플로를 중단시켰으며, 이는 종종 몇 분 뒤에 발생했고 메시지에는 필드가 아니라 개수만 표시되었습니다.

**배부할 값 테이블**과 **드라이버 데이터 테이블**을 모두 선택하기 전에는 아무것도 검사하지 않습니다. 열 매핑은 이 두 테이블을 기반으로 만들어지므로 둘 다 설정하기 전에는 단계가 테이블 자체만 요구합니다.

### 배부 소스 맵

**"No columns specified for allocation."**
열을 하나 이상 선택하여 **역할**을 **배부할 값**으로 설정하십시오. 이 열에는 대상 전체에 분산될 값이 들어 있습니다.

**"Only numeric columns can be allocated, but ... is not numeric."**
**배부할 값**으로 표시된 열의 **유형**이 숫자가 아닙니다. 유형을 숫자 유형(Numeric, Currency, 정수, 큰 정수, 작은 정수(Small), 작은 정수(Tiny), Float, Double, Decimal, Serial, Big Serial) 중 하나로 변경하십시오.

**"Rename the `alloc_status` target column."**
배부는 결과 테이블에 자체 `alloc_status` 열을 기록하므로 같은 이름의 대상 열은 충돌합니다. 대상 열의 이름을 바꾸십시오.

### 드라이버 데이터 맵

**"No driver split value column found."**
드라이버 열 하나의 **역할**을 **분할 값**으로 설정하십시오. 이 열에는 배부가 나누는 기준이 되는 가중치 또는 백분율이 들어 있습니다.

**"The driver value column ... must be numeric."**
**분할 값** 열의 **유형**을 숫자 유형으로 변경하십시오.

**"No driver relation columns specified."**
드라이버 열을 하나 이상 선택하여 **역할**을 **소스 관계 (분모)** 값으로 설정하십시오. 이 설정이 드라이버 행을 소스 행과 연결합니다.

**"No allocation target columns are indicated."**
드라이버 열을 하나 이상 선택하여 **역할**을 **배부 대상 (분자)** 값으로 설정하십시오. 이 열은 배부의 대상이 되며 결과 테이블에 표시됩니다.

**"Driver relation columns do not exist in the source data."**
**소스 관계 (분모)** 역할로 표시된 열에 대해 **배부 소스 맵**에 이름이 같은 열이 없습니다. 이름을 일치하도록 바꾸거나 소스 맵에 해당 열을 추가하십시오.

**"Allocation value column ... is also used as a numerator or denominator column."**
소스 맵의 **배부할 값**과 드라이버 맵의 **소스 관계 (분모)** 또는 **배부 대상 (분자)** 역할에 같은 열 이름이 사용되었습니다. 배부되는 값이 그 값이 가는 곳을 설명하는 열과 구분되도록 둘 중 하나의 이름을 바꾸십시오.

### 차원을 사용한 분할 전용

**"Please select a hierarchy to use for the allocation dimension."**
**데이터 테이블 설정** 탭에서 **할당 차원 계층**을 선택하십시오. [배부 구성](/ko/guides/allocations/setup/configure-an-allocation/)을 참조하십시오.

## 좌초 비용


좌초 비용은....



## 비용 과다 배부


비용 과다 배부란 출력 비용이 더 많아지는 경우를 말합니다...



## 비용의 잘못된 배부


비용의 잘못된 배부는 다음과 같은 경우에 발생합니다...
