---
title: Calculate PCM Model 단계
description: PlaidCloud 워크플로 단계에서 SAP PCM 모델 계산을 트리거하여 수익성 및 원가 배부 처리 작업을 실행합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/calculate-pcm-model.md
---

## 설명



SAP Profitability and Cost Management(PCM) 모델의 계산 엔진을 트리거합니다. 워크플로에서 업스트림 데이터 로드가 모델의 입력(할당, 드라이버, 소스 데이터)을 채운 후 원가 계산을 실행하려면 이 단계를 사용하십시오.

계산은 PCM 서버 측에서 비동기로 수행됩니다. 장시간 실행되는 계산을 중단해야 한다면 [Stop PCM Model Calculation](/ko/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation/) 단계와 함께 사용하십시오.


## 당사의 자격


PlaidCloud는 공식 SAP 파트너이며 SAP PCM 모델 설계 및 구현과 관련된 서비스의 우선 공급업체입니다.







## 예제


드롭다운에서 사용할 에이전트를 선택하고, “모델 이름” 필드에 모델 이름을 입력하고, (필요한 경우) “Wait for Calculation to Complete” 체크박스를 선택한 다음 “Save and Run Step”을 클릭합니다.
