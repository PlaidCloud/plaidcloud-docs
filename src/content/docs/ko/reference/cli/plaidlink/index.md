---
title: PlaidLink
description: 방화벽 뒤에 있는 시스템에 안전하게 액세스할 수 있도록 PlaidLink 에이전트를 설치하고 구성하여 원격 쿼리와 파일 전송을 수행합니다.
sidebar:
  label: PlaidLink
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/index.md
---

PlaidLink는 방화벽으로 보호되어 있거나 기타 제한 사항 때문에 PlaidCloud에서 직접 연결하기 어려운 고객 시스템 및 프로세스에 간접적으로 액세스할 수 있게 해 줍니다. 격리된 영역 안에 설치된 PlaidCloud 에이전트를 통해 PlaidCloud는 쿼리 실행, 파일 다운로드 또는 업로드, 센서 조건 확인, SAP 연동 등 다양한 작업을 에이전트에 요청할 수 있습니다.

에이전트가 PlaidCloud에 먼저 접속하고 표준 HTTPS 네트워크 프로토콜로 통신하므로 대개 최소한의 설정만으로 동작합니다. 또한 에이전트를 권한 없는 사용자로 실행하여 제한된 환경에서 액세스 권한을 제어할 수 있습니다.

## 주제

- [설치](/ko/reference/cli/plaidlink/install/) — Windows, Linux, macOS 또는 컨테이너에서 PlaidLink 실행하기
- [구성](/ko/reference/cli/plaidlink/configure/) — 연결 설정, 자격 증명 및 런타임 옵션
- [에이전트](/ko/reference/cli/plaidlink/agents/) — 여러 에이전트와 해당 기능 관리하기
- [업그레이드](/ko/reference/cli/plaidlink/upgrade/) — 최신 PlaidLink 빌드로 이동하기
