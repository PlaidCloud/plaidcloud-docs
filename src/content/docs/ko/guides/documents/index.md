---
title: 파일 관리
description: PlaidCloud에서 CSV, Excel, Parquet 등 파일 형식으로 데이터를 가져오고 내보내기 위한 파일 저장소 계정을 관리합니다.
sidebar:
  label: 개요
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/index.md
---

PlaidCloud 문서는 데이터 및 워크플로와 함께 파일을 저장, 정리, 검색, 공유하는 기능입니다. 문서는 연결된 모든 저장소 계정에서 가져올 수 있으며 워크플로에서 참조할 수 있습니다.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="S3, Google Cloud Storage, OneDrive 같은 연결된 저장소 계정이 PlaidCloud 문서로 파일을 전달하고, 문서에서는 파일을 저장, 정리, 검색, 공유합니다. 이후 워크플로 단계가 해당 파일을 참조하여 데이터를 가져오고 내보냅니다." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="dc-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">저장소 계정</text>
  <rect x="16" y="40" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="60" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">S3</text>
  <rect x="16" y="82" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Cloud Storage</text>
  <rect x="16" y="124" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">OneDrive</text>
  <path d="M136 55 C186 55 206 92 246 96" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 97 L246 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 139 C186 139 206 108 246 104" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="248" y="70" width="180" height="64" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="338" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">문서</text>
  <text x="338" y="115" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">저장 · 정리 · 검색 · 공유</text>
  <path d="M428 102 L510 102" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="512" y="76" width="152" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="588" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">워크플로 단계</text>
  <text x="588" y="118" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">파일 가져오기 · 내보내기</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">파일은 연결된 모든 저장소 계정에서 문서로 들어오며, 문서에서 파일을 저장, 정리, 검색, 공유한 다음 워크플로 단계에서 참조하여 데이터를 가져오고 내보냅니다.</figcaption>
</figure>

## 문서 워크스페이스

**문서**는 왼쪽의 레일과 그 옆에서 선택한 페이지로 구성되어 열립니다. 레일은 페이지를 **문서**(**개요** 및 **찾아보기**)와 **계정**(**내 계정** 및 **관리**) 아래에 그룹화합니다. 페이지를 열 수 없는 멤버에게는 해당 항목이 표시되지 않습니다. 각 페이지의 맨 위에는 제목과 짧은 부제가 있으며, 작업은 그 옆의 머리글에 있습니다.

| 레일 항목 | 표시되는 내용 |
|---|---|
| **개요** | 계정 타일(**계정**, **공유됨**, **나만 비공개**, **관리형 버킷**, **외부 서비스**, 그리고 계정에 조치가 필요할 때 **사용 안 함**), **고정됨** 파일, **서비스별 계정**, **사용할 수 있는 사람**입니다. 고정된 파일을 선택하면 해당 파일이 선택된 상태로 그 폴더에서 **찾아보기**가 열립니다. |
| **찾아보기** | 파일 탐색기입니다. 즐겨찾는 계정(최상위 폴더를 고정한 계정) 또는 워크스페이스의 기본 계정이 열리며, 페이지 머리글의 목록에서 다른 계정을 선택할 수 있습니다. [문서 계정 사용](/ko/guides/documents/using-document/)을 참조하십시오. |
| **내 계정** | 사용할 수 있는 모든 계정을 하나의 목록으로 보여 줍니다. 각 행의 **공유됨** 또는 **비공개** 표시는 계정이 사용자와 공유된 것인지 사용자만의 것인지 알려 줍니다. 행을 두 번 클릭하면 해당 계정을 찾아봅니다. |
| **관리** | 소유한 계정이며 **이름**, **서비스**, **보안 유형**, **상태**, **설명**이 표시됩니다. 워크스페이스 관리자는 여기에서 모든 문서 계정을 볼 수 있으며 관리할 수 있는 모든 계정을 관리할 수 있습니다. 시스템 관리형 계정은 거부되며 관리형 버킷 계정은 복제할 수 없습니다. |

레일에는 **내 계정**과 **관리** 옆에 개수가 표시됩니다. 소유하지 않은 계정을 보유한 워크스페이스 관리자에게는 **관리**에 개수 대신 **관리자**가 표시됩니다. 개요에는 빠른 시작을 위한 **파일 찾아보기** 및 **새 계정** 버튼이 있습니다.

### 관리의 행 작업

행의 **⋯** 메뉴를 열거나, 행을 마우스 오른쪽 버튼으로 클릭하거나, 도구 모음의 **작업** 메뉴를 사용하면 다음을 이용할 수 있습니다.

- **열기** 및 **편집**: 계정 페이지를 엽니다.
- **복제…**, **버전 기록**, **사용 위치…**. [사용 위치 및 다시 지정](/ko/guides/documents/account-management/document-account-used-by/)을 참조하십시오.
- **사용할 수 있는 사람**: **멤버**, **그룹**, **에이전트**, **소유자**가 있습니다. [문서 계정 액세스 제어](/ko/guides/documents/account-management/control-document-account-access/)를 참조하십시오.
- **사용** 또는 **사용 안 함**, 그리고 **삭제**.

### 계정 페이지

**새 계정**, **열기**, **편집**은 계정을 페이지로 보여 주며, 맨 위의 **계정 관리**로 돌아갈 수 있습니다. 이 페이지에는 다음 카드가 있습니다.

- **일반**: 계정의 이름, 서비스, 버킷, 시작 경로입니다.
- **액세스**: 보안 모델과 계정을 사용할 수 있는 사람입니다. **멤버**, **그룹**, **에이전트**, **소유자**에는 각각 행 메뉴와 동일한 선택기를 여는 **편집** 링크가 있습니다.
- **자격 증명**: 선택한 서비스용 쓰기 전용 필드입니다. **자격 증명 저장됨** 메모는 자격 증명이 설정되었음을 나타내며, 저장된 값은 표시되지 않습니다. 저장된 내용을 유지하려면 필드를 비워 두십시오. SFTP 계정에는 **연결 테스트**도 있습니다.
- **SSH**: SFTP 계정 전용 키 설정입니다.

머리글에는 **찾아보기**, **사용 위치**, 그리고 **복제**, **버전 기록**, **사용** 또는 **사용 안 함**, **삭제**가 있는 **작업** 메뉴가 있습니다. 저장하지 않은 변경 사항이 있는 상태로 페이지를 벗어나면 PlaidCloud가 변경 사항을 취소할지 묻습니다.

문서 화면에 대한 이전 링크와 북마크는 계속해서 해당 페이지를 엽니다.
