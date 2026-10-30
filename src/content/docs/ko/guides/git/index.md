---
title: PlaidCloud Git
description: 이슈, 풀 리퀘스트, 프로젝트 보드, 릴리스, 위키와 기본 제공되는 싱글 사인온으로 PlaidCloud 안에서 Git 리포지토리를 호스팅하고, 버전 관리하며, 협업합니다.
sidebar:
  label: 개요
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git은 워크스페이스에 내장된 프라이빗 Git 서비스입니다. 워크스페이스마다 자체 Git 서버가 제공되어 코드, 구성, 노트북 및 기타 버전 관리 파일을 저장할 수 있으며, 팀이 협업에 사용하는 이슈, 풀 리퀘스트, 프로젝트 보드도 함께 제공됩니다.

PlaidCloud 계정으로 로그인하므로 별도의 사용자 이름이나 암호를 설정할 필요가 없습니다. 워크스페이스에서 **Git**을 열면 이미 로그인된 상태입니다. 새 리포지토리는 기본적으로 비공개이며, 액세스 권한을 부여한 멤버에게만 표시됩니다.

## Git 관리

모든 멤버가 리포지토리를 만들 수 있지만, 리포지토리와 팀을 묶는 공유 공간인 **조직 만들기**에는 **Git Administration** 권한이 필요합니다. **ID**에서 보안 그룹에 해당 권한을 추가하거나 기본 제공되는 **Git Administration** 그룹에 멤버를 추가하여 권한을 부여합니다. 이 권한이 있는 그룹에 속한 사용자는 다음에 Git에 로그인할 때 Git 관리자가 됩니다. PlaidCloud 지원 담당자는 이 권한이 자동으로 부여됩니다.

새로 관리자 권한을 받은 사용자가 Git을 한 번도 열어 본 적이 없다면 관리자 액세스가 적용되려면 Git에 **두 번** 로그인해야 할 수 있습니다. 첫 번째 로그인에서 Git 계정이 만들어지고, 권한은 다음 로그인에서 적용됩니다.

## 이 섹션의 내용

- [리포지토리](/ko/guides/git/repositories/) — 리포지토리를 만든 다음 작업 내용을 복제하고, 커밋하고, 푸시합니다
- [이슈](/ko/guides/git/issues/) — 레이블, 마일스톤, 담당자로 작업, 버그, 아이디어를 추적합니다
- [풀 리퀘스트](/ko/guides/git/pull-requests/) — 브랜치에서 변경 사항을 제안하고 병합하기 전에 검토합니다
- [프로젝트 보드](/ko/guides/git/projects/) — 칸반 보드에서 이슈와 풀 리퀘스트를 정리합니다
- [릴리스 및 태그](/ko/guides/git/releases-and-tags/) — 리포지토리의 버전별 스냅샷을 표시하고 게시합니다
- [위키](/ko/guides/git/wikis/) — 코드 옆에 긴 형식의 문서를 보관합니다
- [패키지](/ko/guides/git/packages/) — 리포지토리 레지스트리에서 빌드 아티팩트를 게시하고 설치합니다
- [코드 검색](/ko/guides/git/searching-code/) — 리포지토리 전체에서 코드, 이슈, 풀 리퀘스트를 찾습니다

## 관련 항목

- [PlaidCloud Git에서 Panel 앱 배포](/ko/guides/panel-apps/deploy-from-git/) — 관리형 무자격 증명 연결로 리포지토리에서 바로 HoloViz Panel 앱을 서비스합니다
- [PlaidCloud Git에서 Dash 앱 배포](/ko/guides/dash-apps/deploy-from-git/) — 같은 방식으로 Plotly Dash 앱을 서비스합니다
- [액세스 관리](/ko/administration/access/) — 워크스페이스 멤버십과 보안 그룹이 리포지토리를 보고 편집할 수 있는 사용자를 결정하는 방식
