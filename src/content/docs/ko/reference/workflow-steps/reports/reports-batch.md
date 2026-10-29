---
title: Reports Batch 단계
description: PlaidCloud 워크플로 단계에서 배치 PDF 보고서를 생성하여, 서로 다른 데이터 입력을 가진 템플릿으로 여러 보고서를 만듭니다.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/reports-batch.md
---

## 설명



제어 테이블을 기반으로 하나의 RML 템플릿에서 여러 PDF 보고서를 렌더링합니다. 제어 테이블의 행마다 보고서가 하나씩 생성되며, 각 행의 열 값이 해당 보고서를 렌더링할 때 매개변수로 사용됩니다.

일반적인 용도는 고객 명세서(고객당 PDF 하나), 사업부별 재무제표(사업부당 PDF 하나), 청구서(주문당 PDF 하나)입니다. 일회성 보고서를 생성하려면 [Report Single](/ko/reference/workflow-steps/reports/report-single/) 단계를 비교해 보십시오.


## 템플릿이 읽는 이름

템플릿은 **보고서 데이터** 탭의 각 소스와 **배치 레코드 값 데이터 소스** 매핑의 각 대상 열을 이름으로 읽습니다. 상수 섹션은 없으며, 각 배치 행이 해당 보고서에 대한 템플릿의 값을 제공합니다. 새 소스의 이름은 `new_source`, `new_source_2` 등으로 지정되며 템플릿이 그대로 읽을 수 있습니다.


## 저장할 때 검사하는 항목

모든 소스 및 배치 열 이름은 지정되어 있고, 고유하며, 템플릿이 읽을 수 있어야 합니다. 이는 [Report Single](/ko/reference/workflow-steps/reports/report-single/) 단계와 같은 규칙이며, 상수 대신 배치 열에 적용됩니다. *Batch column name 'unit id' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*

배치 소스 테이블을 선택했지만 배치 매핑이 비어 있는 상태로 저장하면, 채우기를 실행한 것처럼 해당 테이블에서 매핑이 채워집니다.


## 빈 배치 테이블

배치 소스 테이블에 행이 없으면 단계는 배치 테이블을 명시한 경고와 함께 성공적으로 완료되며, 보고서는 생성되지 않습니다.


## 예제

아직 예제가 없습니다...
