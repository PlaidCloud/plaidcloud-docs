---
title: 머신러닝
description: scikit-learn 모델을 학습시키고 이를 사용해 테이블을 채점하는 워크플로 단계입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/machine-learning/index.md
---

임의의 테이블로 모델을 학습시키고, 모델 테이블로서 워크플로를 통해 전달한 다음, 이를 사용해 데이터 테이블을 채점합니다.

## 단계

- [ML: 모델 학습](/ko/reference/workflow-steps/machine-learning/ml-train/) — 소스 테이블로 scikit-learn 모델(분류 또는 회귀)을 학습시키고, 학습된 모델, 매개변수, 특성 목록, 학습 지표가 담긴 쿼리 가능한 모델 테이블을 기록합니다.
- [ML: 점수 산출](/ko/reference/workflow-steps/machine-learning/ml-score/) — 학습된 모델 테이블로 데이터 테이블을 채점하고 예측 열을 추가합니다.

Alteryx Assisted Modeling 파이프라인이 이 단계들로 변환되는 방식은 [Alteryx 워크플로 마이그레이션](/ko/guides/workflows/migrate-alteryx-workflows/#머신-러닝assisted-modeling-변환)을 참조하십시오.
