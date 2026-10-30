---
title: Oracle Essbase 단계
description: Essbase 연결을 통해 Oracle Essbase 큐브에서 읽는 워크플로 단계로, 실시간 MDX 쿼리와 PlaidCloud 차원으로 로드되는 차원 아웃라인을 클라우드 직접 방식으로 제공합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/index.md
---

[Oracle Essbase 연결](/ko/guides/connections/essbase/)을 통해 Oracle **Essbase**에서 읽는 워크플로 단계로, 실시간 MDX 쿼리로 가져오는 큐브 데이터와 PlaidCloud 차원으로 로드되는 차원 아웃라인을 다룹니다. Essbase는 REST API를 통해 **클라우드 직접** 방식으로 접근하며, 이 단계에는 온프레미스 에이전트 경로가 없습니다.

## 단계

- [Essbase: 큐브 쿼리](/ko/reference/workflow-steps/essbase/essbase-query/) — 큐브에 대해 실시간 MDX 쿼리를 실행하고 결과 그리드를 테이블로 저장합니다. 클라우드 직접 방식입니다.
- [Essbase: 차원 읽기](/ko/reference/workflow-steps/essbase/essbase-dimension-read/) — Essbase 차원 아웃라인을 PlaidCloud 차원으로 로드합니다. 클라우드 직접 방식입니다.

## 관련 항목

- [Oracle Essbase에 연결(가이드)](/ko/guides/connections/essbase/)
- [Oracle Essbase 커넥터](/ko/reference/connectors/erp/oracle-essbase/)
