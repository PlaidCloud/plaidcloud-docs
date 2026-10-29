---
title: CLI 도구
description: PlaidCloud 명령줄 도구에 대한 참조입니다. PlaidLink 에이전트, PlaidXL Excel 추가 기능, 노트북 연동을 위한 Jupyter CLI를 다룹니다.
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

PlaidCloud는 웹 UI 밖에서 워크스페이스를 다루기 위한 세 가지 명령줄 및 로컬 도구를 제공합니다.

## PlaidLink

[PlaidLink](/ko/reference/cli/plaidlink/)는 네트워크 내부에서 실행되어 PlaidCloud 워크플로를 방화벽으로 보호되는 리소스(PlaidCloud가 직접 접근할 수 없는 데이터베이스, 파일 공유 및 기타 시스템)와 연결하는 에이전트입니다. Windows 서비스, Unix/Linux/Mac 데몬, 컨테이너 또는 Kubernetes 파드로 설치합니다.

- [설치](/ko/reference/cli/plaidlink/install/)
- [구성](/ko/reference/cli/plaidlink/configure/)
- [에이전트](/ko/reference/cli/plaidlink/agents/)
- [업그레이드](/ko/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/ko/reference/cli/plaidxl/)은 Microsoft Excel용 PlaidCloud 추가 기능입니다. 프로젝트 테이블과 차원을 워크시트로 가져오고, 필요할 때 새로 고치며, PlaidCloud 데이터로 롤업 값을 계산하는 `PLAIDXL` 수식을 추가합니다.

- [설치](/ko/reference/cli/plaidxl/install/)
- [로그인](/ko/reference/cli/plaidxl/connect/)
- [테이블 및 차원 다루기](/ko/reference/cli/plaidxl/retrieve/)
- [사용자 지정 함수](/ko/reference/cli/plaidxl/functions/)
- [사용자 지정 함수로 보고서 작성](/ko/reference/cli/plaidxl/build-a-report/)
- [PlaidCloud 리본](/ko/reference/cli/plaidxl/ribbon/)
- [문제 해결](/ko/reference/cli/plaidxl/troubleshooting/)

## Jupyter CLI

[Jupyter CLI](/ko/reference/cli/jupyter/)를 사용하면 데이터 과학자가 PlaidCloud 인식 CLI와 Python 도우미를 통해 Jupyter 노트북에서 PlaidCloud 프로젝트 데이터를 다룰 수 있습니다.

- [명령줄](/ko/reference/cli/jupyter/command-line/)
- [Jupyter 노트북](/ko/reference/cli/jupyter/jupyter-notebook/)
- [OAuth 설정](/ko/reference/cli/jupyter/oauth-setup/)
