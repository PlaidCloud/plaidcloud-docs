---
title: Stop PCM Model Calculation 단계
description: PlaidCloud 워크플로 단계에서 실행 중인 SAP PCM 모델 계산을 중지하여 오류나 문제가 감지되었을 때 처리를 중단합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation.md
---

## 설명



진행 중인 SAP PCM 모델 계산을 중단합니다. 계산이 너무 오래 걸리거나, 잘못된 입력 데이터로 시작되었거나, 우선순위가 더 높은 작업을 위해 서버 리소스를 확보해야 할 때 유용합니다.

현재 실행 중인 계산이 없으면 이 단계는 워크플로 로그에 경고를 기록하고 계속 진행합니다.


## 당사의 자격


PlaidCloud는 SAP 공식 파트너이며, SAP PCM 모델 설계 및 구현 관련 서비스의 우선 공급업체입니다.




## 예제


드롭다운에서 사용할 에이전트를 선택하고 “Model Name”을 입력한 다음 “Wait for Copy to Complete” 확인란을 선택하고 “저장 및 실행”을 클릭합니다.
