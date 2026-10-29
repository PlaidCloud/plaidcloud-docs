---
title: Tableau 연결
description: 개인 액세스 토큰을 사용하여 PlaidCloud를 Tableau Server 또는 Tableau Cloud에 연결하면 워크플로가 데이터 소스를 게시할 수 있습니다.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/collaboration/tableau.md
---

Tableau 연결에는 Tableau Server 또는 Tableau Cloud 사이트의 주소와 개인 액세스 토큰이 저장됩니다. [Publish to Tableau](/ko/reference/workflow-steps/export/export-to-tableau/) 단계는 이 연결을 사용하여 `.hyper` 추출을 데이터 소스로 게시합니다.

## 시작하기 전에

Tableau에서 게시를 수행할 계정의 개인 액세스 토큰을 만듭니다. **My Account Settings**를 선택한 다음 **Personal Access Tokens**를 선택합니다. Tableau에서 토큰 시크릿을 표시할 때 복사해 두십시오. Tableau는 이를 다시 표시하지 않습니다. 이 계정에는 게시할 프로젝트에 데이터 소스를 게시할 권한이 있어야 합니다.

## 연결 만들기

1. **Analyze**를 열고 **Tools → 외부 데이터 연결**을 선택한 다음 **+ 새 연결 → Tableau**를 선택합니다.
2. 연결의 이름과 설명을 입력합니다.
3. 연결 설정을 입력합니다.

| 필드 | 입력할 내용 |
| --- | --- |
| **서버 URL** | 서버 또는 Tableau Cloud 포드의 주소입니다(예: `https://prod-useast-a.online.tableau.com`). 호스트만 입력하면 `https`로 간주되며 `http` 주소는 거부됩니다. |
| **사이트** | 사이트의 콘텐츠 URL로, 브라우저 주소에서 `#/site/` 뒤에 오는 부분입니다. 기본 사이트는 비워 둡니다. |
| **개인 액세스 토큰 이름** | Tableau에서 토큰에 지정한 이름입니다. |
| **개인 액세스 토큰 시크릿** | 토큰 시크릿입니다. 암호화되어 저장되며 연결을 다시 열면 비어 있는 것으로 표시됩니다. 저장된 시크릿을 유지하려면 비워 둡니다. |

4. **만들기**를 선택합니다.

서버는 인터넷에서 접근할 수 있어야 합니다. PlaidCloud는 사설 네트워크에 있는 Tableau 서버에는 연결하지 않습니다.

## 관련 항목

- [Publish to Tableau](/ko/reference/workflow-steps/export/export-to-tableau/) 단계
- [Tableau Hyper Export](/ko/reference/workflow-steps/export/export-hyper/) 단계
