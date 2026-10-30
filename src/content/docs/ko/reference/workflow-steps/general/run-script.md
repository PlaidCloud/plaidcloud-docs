---
title: 앱 작업 실행
description: 워크플로에서 등록된 애플리케이션 작업을 호출하며, 필요하면 문서 경로와 매개변수를 전달합니다.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/run-script.md
---

## 설명

워크플로 안에서 등록된 애플리케이션 작업을 호출합니다. 데이터 변환이 아닌 플랫폼 작업, 즉 앱이 자동화를 위해 노출하는 작업을 트리거할 때 사용합니다.

## 구성

### 실행할 애플리케이션 작업

호출할 작업입니다.

### 파일 경로

파일을 받는 작업의 경우:

- **문서 디렉터리** — 전달할 문서 계정과 경로입니다.
- **파일 매개변수 이름** — 작업이 경로를 받을 것으로 기대하는 매개변수입니다. 기본값은 `document_path`이며, 작업이 다른 이름을 사용하는 경우에만 변경하십시오.

### 선택적 매개변수

파일 경로와 함께 작업에 전달되는 이름/값 쌍입니다.

## 관련 항목

- [일반 단계](/ko/reference/workflow-steps/general/)
- [User Defined Transform 단계](/ko/reference/workflow-steps/general/user-defined-transform/)
- [Run Remote Python 단계](/ko/reference/workflow-steps/general/run-remote-python/)
