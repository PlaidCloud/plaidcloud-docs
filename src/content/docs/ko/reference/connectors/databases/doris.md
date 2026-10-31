---
title: Apache Doris
description: PlaidCloud에서 Apache Doris 데이터베이스 연결을 구성하여 대규모 데이터 세트에 대해 실시간 분석 쿼리를 실행합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/doris.md
---

**Apache Doris**는 StarRocks가 포크된 고성능 MPP 분석 데이터베이스입니다. 이 커넥터를 사용하여 PlaidCloud 워크플로에서 Doris 배포를 쿼리합니다. 연결은 MySQL 와이어 프로토콜과 표준 사용자 이름/암호 인증을 사용합니다.

## 업스트림 문서
[Apache Doris 문서](https://doris.apache.org/docs/4.x/gettingStarted/what-is-apache-doris)

[Apache Doris 프로젝트 홈페이지](https://doris.apache.org/)

## 설정

이 커넥터는 공급업체별 인증 흐름을 사용하며 워크스페이스의 **연결** 화면에서 직접 구성합니다. 표시되는 구성 필드는 테넌트 관리자가 해당 통합에 대해 프로비저닝한 자격 증명에 따라 달라집니다.

최신 설정 세부 정보는 업스트림 [doris 문서](https://doris.apache.org/docs/)를 참조하십시오.

테넌트에 이 커넥터를 설정하는 데 도움이 필요하면 계정 팀에 문의하십시오. 커넥터별 자격 증명, 환경 URL 및 필요한 사전 프로비저닝은 일반적으로 PlaidCloud 지원팀과 조율해야 합니다.
