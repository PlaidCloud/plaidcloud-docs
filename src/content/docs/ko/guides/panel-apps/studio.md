---
title: Panel Studio
description: PlaidCloud를 벗어나지 않고 Panel 앱을 만들고, 편집하고, 미리 보고, 게시합니다. 이전 버전 복원, 앱의 사용 현황과 속도 확인, 알림 및 요약 설정, 갤러리 등록, 홈에 고정도 할 수 있습니다.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio는 PlaidCloud 안에서 Panel 앱을 편집하는 편집기입니다. 앱의 파일을 편집기 옆에 표시하고, 열어 볼 수 있는 비공개 미리 보기를 빌드하며, 준비가 되면 앱을 게시합니다. 시작하는 데 Git 리포지토리는 필요하지 않습니다.

## Panel Studio 열기

- 프로젝트의 **홈** 보드에서 Panel 앱의 **Studio에서 열기**를 선택합니다.
- **내 Panel 앱**에서 앱 행의 **Studio**를 선택합니다.

새 앱을 시작하려면 **새 Studio 앱**을 선택합니다. 이 버튼은 **내 Panel 앱** 도구 모음의 첫 번째 버튼이며, 프로젝트의 **홈** 탭에 있는 **Panel 앱** 상자에도 있습니다. 테이블을 기반으로 앱을 만들려면 프로젝트의 **테이블** 탭에서 해당 테이블을 선택한 다음 **Panel 앱 만들기**를 선택합니다.

## 앱 만들기

**새 Studio 앱** 대화 상자에서는 다음 다섯 가지 중 하나로 시작할 수 있습니다.

| 시작 기준 | 결과 |
|---|---|
| **빈 앱** | `app.py`와 `requirements.txt`가 있는 최소한의 앱입니다. |
| **테이블에서** | 선택한 테이블을 기반으로 한 앱입니다. |
| **뷰에서** | 프로젝트 뷰를 기반으로 한 같은 형태의 앱입니다. |
| **다른 Studio 앱에서** | 내 Studio 앱 중 하나의 복사본입니다. |
| **갤러리에서** | 워크스페이스에서 [앱 갤러리](/ko/guides/panel-apps/gallery/)에 등록한 앱의 복사본입니다. |

앱 이름을 정하고 **프로젝트**를 선택한 다음 **만들기**를 선택합니다. Studio가 새 앱을 열고 왼쪽에 파일을 표시합니다. 테이블이나 뷰에서 시작한 경우 앱의 첫 페이지를 만들기 위한 Weave 프롬프트가 전송할 수 있는 상태로 준비됩니다. [Panel 앱 만들기](/ko/guides/panel-apps/creating/)를 참조하십시오.

## 앱이 저장되는 위치

Studio 앱은 워크스페이스의 [PlaidCloud Git](/ko/guides/git/)에 있는 `apps` 리포지토리 안에서 앱 이름을 딴 폴더(`<app-slug>/`)로 저장되며, 이는 다른 Panel 앱이 있는 리포지토리와 같습니다. Studio는 앱을 위한 별도의 리포지토리를 만들지 않으므로 `apps`에서 다른 앱과 함께 소스를 찾고 편집할 수 있습니다.

- **초안 브랜치.** 아직 게시하지 않은 작업은 `studio-<app-slug>`라는 브랜치에 보관됩니다. **게시**는 해당 브랜치의 앱 폴더를 메인 브랜치로 복사합니다.
- **다시 빌드.** `apps`에 푸시하면 해당 앱의 폴더 또는 리포지토리 루트의 `requirements.txt`가 변경된 경우에만 앱이 다시 빌드됩니다.
- **기존 앱.** 별도의 리포지토리에 있던 Studio 앱은 자동으로 해당 폴더로 이동됩니다. 이전 리포지토리는 보관 처리되어 읽기 전용으로 남으며 삭제되지 않습니다.

## 편집

목록에서 파일을 선택하면 편집기에서 편집할 수 있습니다. Python 종속성은 `requirements.txt`에 한 줄에 패키지 하나씩 나열하십시오. 이 패키지는 앱을 빌드할 때 설치됩니다.

**Weave에 문의**를 선택하면 Weave가 앱을 대신 작성하거나 변경합니다. [Weave로 Panel 앱 만들기](/ko/guides/panel-apps/build-with-weave/)를 참조하십시오.

## 저장, 미리 보기, 게시

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="저장하면 나만 볼 수 있는 초안이 유지됩니다. 미리 보기는 편집기용으로 초안의 비공개 사본을 빌드합니다. 게시는 확인 후 라이브 앱을 대체합니다." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">저장</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">초안만</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">미리 보기</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">편집기에서만</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">게시</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">라이브 앱</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">편집 내용은 게시해야 비로소 보는 사람에게 반영됩니다.</figcaption>
</figure>

### 저장

**저장**은 변경 사항을 초안으로 저장합니다. 라이브 앱은 변경되지 않으며 다른 사람은 초안을 볼 수 없습니다.

### 미리 보기

**미리 보기**는 저장된 초안을 비공개 사본으로 빌드하여 엽니다. 앱의 편집자만 미리 보기를 열 수 있습니다.

- 미리 보기는 저장 없이 24시간이 지나면 제거됩니다.
- 워크스페이스에서는 미리 보기를 동시에 최대 10개까지 둘 수 있습니다.
- 최신 편집 내용을 보려면 다시 저장한 다음 **미리 보기**를 선택합니다.

### 게시

**게시**는 라이브 앱을 저장된 초안으로 대체합니다. 앱이 속한 프로젝트의 편집 권한이 필요하며, Studio가 먼저 확인을 요청합니다.

앱을 연 이후에 다른 사람이 변경 사항을 게시한 경우 Studio는 그 사람의 작업을 덮어쓰지 않고 충돌을 알립니다. 앱을 다시 로드하고 내 편집 내용을 옮긴 다음 다시 게시하십시오.

## 빌드 상태와 오류

**빌드** 탭에는 최신 빌드의 상태가 표시되며 빌드가 진행되는 동안 업데이트됩니다. 빌드에 실패하면 이 탭에 각 오류가 파일과 줄 번호와 함께 나열되므로 해당 줄로 바로 이동할 수 있습니다. `requirements.txt`의 종속성 문제에는 해결 방법에 대한 힌트가 함께 표시됩니다.

오류와 경고는 편집기의 해당 줄에도 표시되므로 문제가 있는 위치에서 바로 확인할 수 있습니다.

앱을 게시한 후 각 상태가 의미하는 바는 [Panel 앱 사용](/ko/guides/panel-apps/using/#빌드-상태서버-앱)을 참조하십시오.

## 기록 및 복원

**기록** 탭에는 앱의 게시된 모든 버전이 빌드 상태와 함께 최신순으로 나열됩니다. 이전 버전을 보려면 **더 로드**를 선택합니다.

이전 버전으로 되돌리려면 해당 버전에서 **복원**을 선택하고 확인합니다. 복원된 버전이 라이브 앱이 되고 다시 빌드됩니다. 저장하지 않은 초안은 사라지지 않고 초안에 그대로 남아 있다가 다음에 게시할 때 복원된 버전 위에 반영되어 라이브가 됩니다. 앱이 이미 해당 버전과 일치하면 Studio가 그 사실을 알리고 아무것도 변경하지 않습니다. 복원하는 동안 다른 사람이 게시한 경우 Studio는 아무것도 복원하지 않고 다시 시도하도록 안내합니다.

## 인사이트

**인사이트** 탭에는 사람들이 앱을 어떻게 사용하는지와 앱의 응답 속도가 표시됩니다. 지난 7일, 14일, 30일 중에서 선택합니다.

| 섹션 | 표시 내용 |
|---|---|
| **일별 조회수** | 매일 앱이 열린 횟수입니다. |
| **페이지 로드** | 해당 기간의 페이지 로드를 기준으로 한 로드 시간의 중앙값과, 로드의 95퍼센트가 그보다 빨랐던 시간입니다. |
| **가장 느린 쿼리** | 가장 오래 걸린 쿼리이며, 실행 횟수와 중앙값, 느린 쪽 값, 가장 느린 시간이 함께 표시됩니다. |
| **오류** | 해당 기간에 발생한 문제를 오류 종류와 앱에서 발생한 위치별로 보여 줍니다. |

기간 내 활동량이 인사이트가 읽을 수 있는 범위를 넘으면 수치가 일부만 반영되었다고 알려 줍니다. 페이지 로드가 앱의 [성능 예산](/ko/guides/panel-apps/app-kit/#성능-예산)을 초과하면 인사이트가 초과한 건수와 느렸던 쿼리를 경고로 알려 줍니다. 인사이트는 쿼리가 반환한 데이터나 앱을 연 사람의 이름을 표시하지 않습니다.

**기록** 및 **인사이트** 탭을 사용하려면 앱이 프로젝트에 할당되어 있어야 하며, 할당되지 않은 앱에는 할당하라는 안내가 표시됩니다.

## 알림 및 요약

**알림 및 요약**을 선택하면 앱 데이터의 수치를 감시하다가 한도를 넘으면 알려 주거나 일정에 따라 요약을 보내는 알림을 설정할 수 있습니다. [알림 및 요약](/ko/guides/panel-apps/alerts-and-digests/)을 참조하십시오.

## 갤러리에 앱 등록

Studio에서 **갤러리…** 를 선택합니다. **갤러리에 등록**을 선택하면 해당 프로젝트를 볼 수 있는 모든 사용자가 그 앱으로 자신의 앱을 만들 수 있는 템플릿으로 등록되고, **갤러리에서 제외**를 선택하면 등록이 제거됩니다. 이 버튼은 프로젝트에 속한 앱에서 사용할 수 있으며 프로젝트에 대한 편집 권한이 필요합니다. [앱 갤러리](/ko/guides/panel-apps/gallery/)를 참조하십시오.

## 홈에 고정

**홈에 고정**을 선택하면 앱이 프로젝트의 **홈** 보드에 추가되고, **홈에서 고정 해제**를 선택하면 제거됩니다.

## 앱 삭제

Panel 앱을 삭제하기 전에 먼저 확인을 요청합니다. **내 Panel 앱**에서 앱 행의 **빼기** 아이콘을 사용합니다. 게시 취소도 확인을 요청합니다.

## 다음 단계

- [Weave로 Panel 앱 만들기](/ko/guides/panel-apps/build-with-weave/) — 앱을 설명하고 정확한 변경 내용을 승인합니다.
- [Panel 앱 키트](/ko/guides/panel-apps/app-kit/) — Studio의 테이블 및 뷰 시작 옵션이 사용하는 구성 요소입니다.
- [알림 및 요약](/ko/guides/panel-apps/alerts-and-digests/) — 수치가 한도를 넘거나 일정에 따라 사람들에게 알립니다.
- [앱 갤러리](/ko/guides/panel-apps/gallery/) — 다른 사람이 시작점으로 쓸 수 있도록 앱을 공유합니다.
- [Panel 앱 사용](/ko/guides/panel-apps/using/) — 게시 후의 로그, 사용 현황, 다시 빌드입니다.
