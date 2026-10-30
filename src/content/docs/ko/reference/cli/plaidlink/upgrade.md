---
title: 업그레이드
description: PlaidLink 에이전트를 최신 버전으로 업그레이드하여 새로운 기능, 보안 패치 및 향상된 시스템 호환성을 이용합니다.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/upgrade.md
---

새 버전이 릴리스될 때 에이전트가 스스로 업데이트할 권한이 부족하거나 수동 업그레이드 절차를 원하는 경우에는 PlaidLink를 수동으로 업그레이드해야 할 수 있습니다.

## 에이전트 다운로드

[PlaidCloud.com](https://plaidcloud.com/)의 릴리스에서 **PlaidLink**를 확인합니다.

## 현재 에이전트 중지

Windows 검색 창에 **`Services`** 를 입력하고 서비스 관리자를 엽니다. 서비스 목록에서 **`PlaidCloud Agent`** 를 찾습니다.

**`PlaidCloud Agent`** 서비스를 마우스 오른쪽 단추로 클릭하고 *중지*를 선택합니다.  서비스가 정상적으로 중지되면 다음 단계로 진행합니다.

## 에이전트 압축 풀기

현재 설치된 에이전트의 위치로 이동합니다.

```bash
C:\Users\<Username here>\src\
```

더 이상 참조되지 않도록 현재 설치 폴더의 이름을 바꿉니다.  예: `Plaidlink_Old_12122022`

다운로드한 zip 파일의 압축을 이 위치에 풀어 설치합니다. 일반적으로 다음 위치를 사용합니다.

```bash
C:\Users\<Username here>\src\plaidlink
```

## 에이전트 시작

*서비스* 창으로 돌아갑니다.  **`PlaidCloud Agent`** 서비스를 마우스 오른쪽 단추로 클릭하고 *시작*을 선택합니다.

Windows 검색 창에 **`Services`** 를 입력하고 서비스 관리자를 엽니다. 서비스 목록에서 **`PlaidCloud Agent`** 를 찾습니다.

서비스를 마우스 오른쪽 단추로 클릭하고 **`Start`** 를 선택하여 에이전트를 시작합니다.  에이전트가 **`Running`** 상태로 표시되면 에이전트가 새 버전으로 다시 정상 작동하는 것입니다.
