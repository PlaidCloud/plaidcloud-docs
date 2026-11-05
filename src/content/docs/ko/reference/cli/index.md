---
title: CLI 도구
description: PlaidCloud 명령줄 도구인 PlaidLink 에이전트, PlaidXL Excel 추가 기능, 노트북 연동용 Jupyter CLI에 대한 참조입니다.
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

PlaidCloud는 웹 UI 밖에서 워크스페이스를 사용할 수 있도록 세 가지 명령줄 및 로컬 도구를 제공합니다.

## PlaidLink

[PlaidLink](/ko/reference/cli/plaidlink/)는 네트워크 내부에서 실행되는 에이전트로, PlaidCloud 워크플로를 방화벽으로 보호되는 리소스(PlaidCloud가 직접 접근할 수 없는 데이터베이스, 파일 공유 및 기타 시스템)와 연결합니다. Windows 서비스, Unix/Linux/Mac 데몬, 컨테이너 또는 Kubernetes 파드로 설치할 수 있습니다.

- [설치](/ko/reference/cli/plaidlink/install/)
- [구성](/ko/reference/cli/plaidlink/configure/)
- [에이전트](/ko/reference/cli/plaidlink/agents/)
- [업그레이드](/ko/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/ko/reference/cli/plaidxl/)은 Microsoft Excel용 PlaidCloud 추가 기능입니다. 프로젝트 테이블과 차원을 워크시트로 가져오고, 필요할 때 새로 고치며, PlaidCloud 데이터에서 집계 값과 관리되는 지표를 계산하는 `PLAIDXL` 수식을 추가하고, 계획한 값을 다시 기록합니다.

- [설치](/ko/reference/cli/plaidxl/install/)
- [로그인](/ko/reference/cli/plaidxl/connect/)
- [테이블과 차원 작업](/ko/reference/cli/plaidxl/retrieve/)
- [사용자 지정 함수](/ko/reference/cli/plaidxl/functions/)
- [보고서 작성](/ko/reference/cli/plaidxl/build-a-report/)
- [드릴, 멤버 선택, 숫자 설명](/ko/reference/cli/plaidxl/drill/)
- [PlaidCloud에 값 입력](/ko/reference/cli/plaidxl/write-values/)
- [Excel에서 Weave에 문의](/ko/reference/cli/plaidxl/weave/)
- [PlaidCloud 리본](/ko/reference/cli/plaidxl/ribbon/)
- [문제 해결](/ko/reference/cli/plaidxl/troubleshooting/)

## Jupyter CLI

[Jupyter CLI](/ko/reference/cli/jupyter/)를 사용하면 데이터 과학자가 PlaidCloud 인식 CLI와 Python 도우미로 Jupyter 노트북에서 PlaidCloud 프로젝트 데이터를 다룰 수 있습니다.

- [명령줄](/ko/reference/cli/jupyter/command-line/)
- [Jupyter 노트북](/ko/reference/cli/jupyter/jupyter-notebook/)
- [OAuth 설정](/ko/reference/cli/jupyter/oauth-setup/)
