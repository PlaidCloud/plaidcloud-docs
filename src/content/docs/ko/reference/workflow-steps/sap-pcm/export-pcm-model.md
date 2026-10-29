---
title: Calculate and Export PCM Model 단계
description: PlaidLink 에이전트를 통해 PCM 모델 계산을 실행하고 결과를 데이터베이스 또는 구분 기호로 분리된 파일로 내보냅니다.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/export-pcm-model.md
---

## 설명

PCM 설치 환경에 접근할 수 있는 [PlaidLink 에이전트](/ko/reference/workflow-steps/agent/)를 통해 SAP PCM 모델을 계산하고 결과를 한 번에 내보냅니다. [Calculate PCM Model](/ko/reference/workflow-steps/sap-pcm/calculate-pcm-model/) 단계는 계산만 실행하지만, 이 단계는 출력도 함께 이동합니다.

## 구성

### 사용할 에이전트

PCM 설치 환경에 접근하는 PlaidLink 에이전트입니다.

### 모델 정보

- **모델 이름** — 계산할 PCM 모델입니다.
- **내보내기 사양 경로** — 내보낼 대상을 설명하는 PCM 내보내기 사양입니다.

### 내보내기 출력 대상

데이터베이스 대상, 파일 대상 또는 둘 다 선택합니다.

**데이터베이스로** — 기본적으로 켜져 있으며, 내보내기는 사양에 구성된 데이터베이스 대상을 통해 기록합니다.

**파일로** — 기본적으로 꺼져 있습니다. 켜면 다음 옵션을 사용할 수 있습니다.

- **파일 경로** — 에이전트가 파일을 기록할 위치입니다.
- **별칭** — 내보내기에 기록되는 별칭입니다. 기본값은 `DEFAULT ALIAS`입니다.
- **정밀도** — 내보내는 값의 소수 자릿수입니다. 기본값은 0입니다.
- **구분 기호** — 쉼표, 탭, 파이프, 세미콜론, 공백, `@`, `~` 또는 `:`입니다. 기본값은 탭입니다.
- **추가** — 기본적으로 꺼져 있으므로 실행할 때마다 파일을 교체합니다. 실행 결과를 누적하려면 켜십시오.
- **규칙 포함** — 기본적으로 꺼져 있습니다. 값과 함께 모델의 규칙도 내보내려면 켜십시오.
- **유니코드** — 기본적으로 꺼져 있습니다. 내보내는 데이터에 기본 인코딩 범위를 벗어나는 문자가 포함된 경우 켜십시오.

## 관련 항목

- [SAP-PCM 단계](/ko/reference/workflow-steps/sap-pcm/)
- [Calculate PCM Model](/ko/reference/workflow-steps/sap-pcm/calculate-pcm-model/) 단계
- [Run SAP PCM Hyper Loader](/ko/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader/) 단계
