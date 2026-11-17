---
title: 파일 관리
description: CSV, Excel, Parquet 등 다양한 파일 형식으로 데이터를 가져오고 내보낼 수 있도록 PlaidCloud에서 파일 스토리지 계정을 관리합니다.
sidebar:
  label: 개요
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/index.md
---

PlaidCloud Documents에서는 데이터 및 워크플로와 함께 파일을 저장하고, 정리하고, 검색하고, 공유할 수 있습니다. 문서는 연결된 모든 스토리지 계정에서 가져올 수 있으며 워크플로에서 참조할 수 있습니다.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="S3, Google Cloud Storage, OneDrive 같은 연결된 스토리지 계정이 PlaidCloud Documents로 파일을 공급하고, Documents에서 파일을 저장, 정리, 검색, 공유합니다. 이후 워크플로 단계가 해당 파일을 참조하여 데이터를 가져오고 내보냅니다." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="dc-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">스토리지 계정</text>
  <rect x="16" y="40" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="60" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">S3</text>
  <rect x="16" y="82" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Cloud Storage</text>
  <rect x="16" y="124" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">OneDrive</text>
  <path d="M136 55 C186 55 206 92 246 96" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 97 L246 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 139 C186 139 206 108 246 104" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="248" y="70" width="180" height="64" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="338" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Documents</text>
  <text x="338" y="115" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">저장 · 정리 · 검색 · 공유</text>
  <path d="M428 102 L510 102" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="512" y="76" width="152" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="588" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">워크플로 단계</text>
  <text x="588" y="118" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">파일 가져오기 · 내보내기</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">파일은 연결된 모든 스토리지 계정에서 Documents로 들어오며, 여기에서 저장, 정리, 검색, 공유할 수 있습니다. 이후 워크플로 단계에서 참조하여 데이터를 가져오고 내보냅니다.</figcaption>
</figure>

## Documents 작업 공간

**Document**를 열면 왼쪽에 레일이 있고 그 옆에 선택한 페이지가 표시됩니다. 레일은 페이지를 **문서**(**개요**와 **찾아보기**)와 **계정**(**내 계정**과 **관리**)으로 묶어 보여 줍니다. 페이지를 열 수 없는 멤버에게는 해당 항목이 표시되지 않습니다. 페이지에는 맨 위에 제목이 있으며, 대개 짧은 부제목이 함께 표시되고, 작업은 그 옆의 헤더에 있습니다.

| 레일 항목 | 표시 내용 |
|---|---|
| **개요** | 계정 타일(**내 계정**을 여는 **계정**, **관리형 버킷**, **외부 서비스**, 그리고 소유한 계정이 사용 안 함 상태일 때 **조치 필요**로 태그되고 **관리**를 여는 **사용 안 함**), **고정된 항목** 파일, **서비스별 계정** 및 **사용 가능한 대상**입니다. 고정된 파일을 선택하면 파일이 선택된 상태로 해당 폴더에서 **찾아보기**가 열립니다. |
| **찾아보기** | 파일 탐색기입니다. 즐겨찾는 계정(최상위 폴더를 고정한 계정) 또는 워크스페이스의 기본 계정이 열리며, 페이지 헤더의 목록에서 다른 계정을 선택할 수 있습니다. [문서 계정 사용](/ko/guides/documents/using-document/)을 참조하십시오. |
| **내 계정** | 사용할 수 있는 모든 계정을 하나의 목록으로 보여 줍니다. 각 행의 **공유됨** 또는 **비공개** 표시는 계정이 나와 공유된 것인지 나만 사용하는 것인지 알려 줍니다. 행을 두 번 클릭하면 찾아볼 수 있습니다. |
| **관리** | 내가 소유한 계정이며, **이름**, **서비스**, **보안 유형**, **상태**, **설명**이 표시됩니다. 워크스페이스 관리자는 여기에서 모든 문서 계정을 보고 그 외에 관리할 수 있는 모든 계정을 관리할 수 있으며, 시스템 관리 계정은 거부되고 관리형 버킷 계정은 복제할 수 없습니다. |

레일에서 **내 계정** 옆에 개수가 표시됩니다. 개요에는 빠르게 시작할 수 있도록 **파일 찾아보기** 버튼과 **새 계정** 버튼이 있습니다.

### 관리의 행 작업

행의 **⋯** 메뉴를 열거나, 행을 마우스 오른쪽 버튼으로 클릭하거나, 도구 모음의 **작업** 메뉴를 사용하여 다음 작업을 할 수 있습니다.

- **열기**와 **편집**: 계정 페이지를 엽니다.
- **복제…**, **버전 기록**, **사용 위치…**: [사용 위치 및 다시 연결](/ko/guides/documents/account-management/document-account-used-by/)을 참조하십시오.
- **사용 가능한 대상**: **멤버**, **그룹**, **에이전트**, **소유자**가 있습니다. [문서 계정 액세스 제어](/ko/guides/documents/account-management/control-document-account-access/)를 참조하십시오.
- **사용** 또는 **사용 안 함**, 그리고 **삭제**.

### 계정 페이지

**새 계정**, **열기**, **편집**을 선택하면 계정이 페이지로 표시되며, 맨 위에 돌아갈 수 있는 **계정 관리**가 있습니다. 페이지에는 다음 카드가 있습니다.

- **일반**: 계정의 이름, 서비스, 버킷, 시작 경로입니다.
- **액세스**: 보안 모델과 계정을 사용 가능한 대상입니다. **멤버**, **그룹**, **에이전트**, **소유자**에는 각각 행 메뉴와 같은 선택기를 여는 **편집** 링크가 있습니다.
- **자격 증명**: 선택한 서비스에 대한 쓰기 전용 필드입니다. **Credentials saved** 메모는 자격 증명이 설정되어 있음을 나타내며, 저장된 값은 표시되지 않습니다. 저장된 값을 유지하려면 필드를 비워 두십시오. SFTP 계정에는 **연결 테스트**도 있습니다.
- **SSH**: SFTP 계정 전용 키 설정입니다.

헤더에는 **찾아보기**, **사용 위치**, 그리고 **복제**, **버전 기록**, **사용** 또는 **사용 안 함**, **삭제**가 있는 **작업** 메뉴가 있습니다. 저장하지 않은 변경 내용이 있는 채로 페이지를 벗어나면 PlaidCloud에서 변경 내용을 삭제할지 묻습니다.

예전 링크와 문서 화면의 북마크도 해당 페이지를 그대로 엽니다.
