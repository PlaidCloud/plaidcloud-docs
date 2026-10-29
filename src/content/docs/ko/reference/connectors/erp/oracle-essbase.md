---
title: Oracle Essbase 커넥터
description: 서비스 계정으로 PlaidCloud를 Oracle Essbase 21c 또는 Oracle Analytics Cloud에 연결하여 워크플로에서 Essbase 큐브에 대한 실시간 MDX 쿼리를 실행합니다.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-essbase.md
---

## API 문서

이 커넥터는 [Oracle Essbase의 REST API](https://docs.oracle.com/en/database/other-databases/essbase/)와 통신합니다. Oracle이 Essbase 21c 및 Oracle Analytics Cloud(OAC)용으로 문서화한 `grid/mdx`, 애플리케이션, 데이터베이스, 아웃라인 엔드포인트와 동일합니다.

## 연결 대상

Oracle Essbase **21c 이상**과 Oracle Analytics Cloud(OAC) Essbase입니다. 이 버전들은 문서화된 REST API로 Essbase를 제공하며, PlaidCloud는 이 API를 호출합니다. REST 이전의 온프레미스 Essbase 릴리스는 **지원되지 않습니다**. 레거시 Java API나 그리드 클라이언트 경로는 없습니다.

연결을 만들면 [Essbase: 큐브 쿼리](/ko/reference/workflow-steps/essbase/essbase-query/) 단계가 큐브에 대해 실시간 MDX를 실행하여 결과 그리드를 테이블에 저장하고, [Essbase: 차원 읽기](/ko/reference/workflow-steps/essbase/essbase-dimension-read/) 단계가 차원 아웃라인을 PlaidCloud 차원으로 로드합니다.

## 인증 방식

연결은 HTTP 기본 인증으로 서비스 계정 사용자 이름과 비밀번호를 사용하여 인증합니다. 해당 계정의 Essbase 프로비저닝에 따라 볼 수 있고 쿼리할 수 있는 애플리케이션과 큐브가 결정되므로, 쿼리하려는 애플리케이션에만 읽기 액세스를 부여하고 그 이상은 부여하지 마십시오.

## 구성

| 필드 | 유형 | 설명 |
|---|---|---|
| 이름 | 텍스트 | 이 연결의 표시 이름입니다. |
| 기본 URL | 텍스트 | Essbase 서버의 오리진입니다. 예: `https://your-host:9001`. 오리진만 입력하고 뒤에 `/essbase/...` 경로를 붙이지 마십시오. |
| 기본 애플리케이션 | 텍스트 *(선택 사항)* | Essbase: 큐브 쿼리 단계 양식에서 이 애플리케이션을 미리 선택합니다. |
| 사용자 이름 | 텍스트 | HTTP 기본 인증에 사용하는 서비스 계정 사용자입니다. |
| 비밀번호 | 텍스트 | 서비스 계정의 비밀번호입니다. 암호화되어 저장됩니다. |
| SSL 확인 | 토글 | 기본적으로 켜져 있습니다. 자체 서명 인증서 등 확인할 수 없는 인증서를 사용하는 호스트에 대해서만 끄십시오. |

## 연결 테스트

연결 편집기에서 **연결 테스트**를 사용합니다. 테스트에 성공하면 Essbase 서버에 접속하여 서비스 계정이 볼 수 있는 애플리케이션을 나열하고 찾은 개수를 보고하므로, 쿼리를 만들기 전에 기본 URL과 자격 증명을 모두 확인할 수 있습니다.

## 관련 항목

- [Essbase: 큐브 쿼리](/ko/reference/workflow-steps/essbase/essbase-query/) — 큐브에 대해 실시간 MDX 쿼리를 실행하고 결과를 테이블에 저장합니다.
- [Essbase: 차원 읽기](/ko/reference/workflow-steps/essbase/essbase-dimension-read/) — 차원 아웃라인을 PlaidCloud 차원으로 로드합니다.
- [Oracle Essbase 단계](/ko/reference/workflow-steps/essbase/)
- [Oracle Essbase에 연결(가이드)](/ko/guides/connections/essbase/)
- [연결 만들기 및 관리](/ko/guides/connections/create-connection/)
