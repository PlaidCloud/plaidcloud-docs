---
title: IBM TM1 / Planning Analytics 단계
description: TM1 연결을 통해 IBM TM1 / Planning Analytics 서버에서 읽는 워크플로 단계입니다. 저장된 뷰 또는 MDX로 큐브 데이터를, 차원 계층을 읽으며 클라우드 직접 방식 또는 온프레미스 PlaidLink 에이전트를 통해 연결합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/index.md
---

[TM1 연결](/ko/guides/connections/tm1/)을 통해 IBM **TM1 / Planning Analytics**에서 읽는 워크플로 단계입니다. 선택적 관점 슬라이스를 사용하여 저장된 뷰 또는 MDX로 큐브 데이터를 읽고, 차원 계층을 PlaidCloud 차원으로 로드합니다. TM1에는 클라우드에서 직접 연결하거나, 사용자의 네트워크 내부에서만 접근할 수 있는 서버라면 온프레미스 PlaidLink 에이전트를 통해 연결합니다.

## 단계

- [TM1: 큐브 쿼리](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — 관점 슬라이스와 저장 전 미리 보기를 사용하여 저장된 뷰 또는 MDX로 큐브를 읽습니다. 클라우드 직접 방식입니다.
- [TM1: 큐브 쿼리(에이전트)](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — TM1: 큐브 쿼리의 온프레미스 대응 단계로, 설치된 PlaidLink 에이전트를 통해 전달됩니다.
- [TM1: 차원 읽기](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — TM1 계층을 PlaidCloud 차원으로 로드합니다. 클라우드 직접 방식입니다.

## 관련 항목

- [TM1 연결(가이드)](/ko/guides/connections/tm1/)
- [TM1 커넥터](/ko/reference/connectors/rest/tm1/)
