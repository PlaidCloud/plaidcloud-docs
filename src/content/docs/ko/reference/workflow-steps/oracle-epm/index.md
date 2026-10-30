---
title: Oracle EPM (HFM / FCCS) 단계
description: HFM/FCCS 연결을 통해 Oracle FCCS의 임시 데이터 슬라이스를 셀프 서비스로 가져오는 워크플로 단계입니다. 관점을 구성하고 실행하면 결과가 테이블로 저장됩니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/index.md
---

[HFM/FCCS 연결](/ko/guides/connections/hfm-fccs/)을 통해 Oracle **FCCS**(Financial Consolidation and Close, EPM Cloud)에서 읽는 워크플로 단계입니다. 재무 담당자가 단계 양식에서 관점을 구성하고 실행하면 반환된 그리드가 프로젝트 테이블로 자동 저장됩니다. HFM 팀에 요청 티켓을 보낼 필요도, 연결 회계 지식도 필요하지 않습니다.

## 단계

- [HFM/FCCS: 데이터 읽기(임시)](/ko/reference/workflow-steps/oracle-epm/hfm-fccs-read/) — 관점 선택기로 데이터 슬라이스를 셀프 서비스로 가져옵니다. 반복 가져오기를 캐시하고, 행 수준 보안을 적용할 수 있으며, 예약된 반복 로드로 승격할 수 있습니다.

## 관련 항목

- [HFM / FCCS에서 추출(가이드)](/ko/guides/connections/hfm-fccs/)
- [HFM / FCCS 커넥터](/ko/reference/connectors/rest/hfm-fccs/)
