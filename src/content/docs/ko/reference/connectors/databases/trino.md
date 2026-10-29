---
title: Trino
description: PlaidCloud에서 Trino 분산 쿼리 엔진 연결을 설정하여 여러 데이터 소스에 걸친 페더레이션 쿼리를 실행합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/trino.md
---

**Trino**(이전 이름 PrestoSQL)는 데이터 레이크에 흔히 사용되는 분산 SQL 쿼리 엔진입니다. 이 커넥터를 사용하여 PlaidCloud 워크플로에서 Trino 배포를 쿼리할 수 있습니다. 인증은 HTTP 기본 인증 또는 JWT를 사용하며, 대상으로 지정한 카탈로그와 스키마에 따라 쿼리가 접근하는 기본 데이터 소스가 결정됩니다.

## 업스트림 문서
[Trino 문서](https://trino.io/docs/current/index.html).

## 설정

이 커넥터는 공급업체별 인증 흐름을 사용하며, 워크스페이스의 **연결** 화면에서 직접 구성합니다. 표시되는 구성 필드는 테넌트 관리자가 해당 통합을 위해 프로비저닝한 자격 증명에 따라 달라집니다.

최신 설정 세부 정보는 업스트림 [trino 문서](https://trino.io/docs/current/)를 참조하십시오.

이 커넥터를 테넌트에 설정하는 데 도움이 필요하면 계정 담당 팀에 문의하십시오. 커넥터별 자격 증명, 환경 URL, 필요한 사전 프로비저닝은 일반적으로 PlaidCloud 지원팀과 조율해야 합니다.
