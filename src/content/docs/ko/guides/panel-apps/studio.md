---
title: Panel Studio
description: PlaidCloud를 떠나지 않고 Panel 앱을 만들고, 편집하고, 미리 보고, 게시합니다. 이후 이전 버전을 복원하고, 앱의 사용량과 속도를 확인하고, 알림 및 다이제스트를 설정하고, 갤러리에 등록하고, 홈에 고정합니다.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio는 PlaidCloud 안에서 Panel 앱을 편집하는 편집기입니다. 앱의 파일을 편집기 옆에 표시하고, 열어 볼 수 있는 비공개 미리 보기를 빌드하며, 준비가 되면 앱을 게시합니다. 시작하는 데 git 리포지토리가 필요하지 않습니다.

## Panel Studio 열기

- 프로젝트의 **홈** 보드에서 Panel 앱의 **Open in Studio**를 선택합니다.
- **내 Panel 앱**에서 앱 행의 **Open in Studio**를 선택합니다.

새 앱을 시작하려면 두 곳 중 어디에서든 **Create app**을 선택합니다.

## 앱 만들기

**Create app** 대화 상자에서는 다섯 가지 중 하나로 시작할 수 있습니다.

| 시작 기준 | 얻는 것 |
|---|---|
| **비어 있음** | `app.py`와 `requirements.txt`가 있는 최소한의 앱. |
| **테이블** | 선택한 테이블을 기반으로 빌드된 앱. |
| **뷰** | 프로젝트 뷰를 기반으로 빌드된 동일한 앱. |
| **템플릿** | [Panel 앱 키트](/ko/guides/panel-apps/app-kit/#템플릿에서-시작하기)의 기성 앱. |
| **갤러리에서** | 워크스페이스가 [앱 갤러리](/ko/guides/panel-apps/gallery/)에 등록한 앱의 사본. |

앱 이름을 지정하고 **프로젝트**를 선택한 다음 **만들기**를 선택합니다. Studio가 왼쪽에 파일이 나열된 새 앱을 엽니다.

## 편집

목록에서 파일을 선택하면 편집기에서 편집할 수 있습니다. Python 종속성은 `requirements.txt`에 한 줄에 패키지 하나씩 나열하십시오. 이 종속성은 앱을 빌드할 때 설치됩니다.

**Ask Weave**를 선택하면 Weave가 앱을 대신 작성하거나 변경합니다. [Weave로 Panel 앱 빌드하기](/ko/guides/panel-apps/build-with-weave/)를 참조하십시오.

## 저장, 미리 보기 및 게시

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="저장하면 본인만 볼 수 있는 초안이 유지됩니다. 미리 보기는 편집기용으로 초안의 비공개 사본을 빌드합니다. 게시는 확인 후 라이브 앱을 교체합니다." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">저장</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">초안만</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">미리 보기</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">편집자만</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">게시</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">라이브 앱</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">편집 내용은 게시할 때만 보는 사람에게 전달됩니다.</figcaption>
</figure>

### 저장

**저장**은 변경 사항을 초안으로 저장합니다. 라이브 앱은 변경되지 않으며 다른 사람은 초안을 볼 수 없습니다.

### 미리 보기

**미리 보기**는 저장된 초안을 비공개 사본으로 빌드하여 엽니다. 앱의 편집자만 미리 보기를 열 수 있습니다.

- 미리 보기는 저장 없이 24시간이 지나면 제거됩니다.
- 워크스페이스에는 한 번에 최대 10개의 미리 보기를 둘 수 있습니다.
- 최신 편집 내용을 보려면 다시 저장하고 **미리 보기**를 선택합니다.

### 게시

**게시**는 라이브 앱을 저장된 초안으로 교체합니다. 앱 프로젝트에 대한 편집 권한이 필요하며, Studio가 먼저 확인을 요청합니다.

앱을 연 이후에 다른 사람이 변경 사항을 게시했다면 Studio는 그 사람의 작업을 덮어쓰는 대신 충돌을 알려 줍니다. 앱을 다시 로드하고, 편집 내용을 옮긴 다음 다시 게시하십시오.

## 빌드 상태 및 오류

**빌드** 탭에는 최신 빌드의 상태가 표시되며 빌드가 진행되는 동안 업데이트됩니다. 빌드가 실패하면 탭에 각 오류가 파일 및 줄 번호와 함께 나열되므로 해당 줄로 바로 이동할 수 있습니다. `requirements.txt`의 종속성 문제에는 해결 방법에 대한 힌트가 함께 제공됩니다.

오류와 경고는 편집기의 해당 줄에도 표시되므로 문제를 그 위치에서 볼 수 있습니다.

앱을 게시한 후 각 상태의 의미는 [Panel 앱 사용하기](/ko/guides/panel-apps/using/#빌드-상태서버-앱)를 참조하십시오.

## 기록 및 복원

**기록** 탭에는 앱의 게시된 모든 버전이 최신순으로 빌드 상태와 함께 나열됩니다. 이전 버전을 보려면 **더 로드**를 선택합니다.

이전 버전으로 돌아가려면 해당 버전에서 **복원**을 선택하고 확인합니다. 복원된 버전이 라이브 앱이 되어 다시 빌드됩니다. 저장하지 않은 초안은 사라지지 않습니다. 초안에 그대로 남아 있다가 다음에 게시할 때 복원된 버전 위에 적용되어 라이브로 전환됩니다. 앱이 이미 해당 버전과 일치하면 Studio가 그렇게 알려 주고 아무것도 변경하지 않습니다. 복원하는 동안 다른 사람이 게시했다면 Studio는 아무것도 복원하지 않고 다시 시도하라고 요청합니다.

## 인사이트

**인사이트** 탭에는 사람들이 앱을 사용하는 방식과 앱의 응답 속도가 표시됩니다. 최근 7일, 14일 또는 30일을 선택합니다.

| 섹션 | 표시 내용 |
|---|---|
| **Views per day** | 하루에 앱이 열린 횟수. |
| **Page load** | 해당 기간의 페이지 로드에서 구한 로드 시간의 중앙값과 로드의 95퍼센트가 넘어서는 시간. |
| **Slowest queries** | 가장 오래 걸린 쿼리와 실행 빈도, 그리고 중앙값, 느린 쪽 값, 가장 느린 시간. |
| **오류** | 해당 기간에 잘못된 사항을 오류 종류와 앱에서 발생한 위치별로 표시. |

기간에 Insights가 읽을 수 있는 것보다 많은 활동이 있으면 수치가 일부라고 알려 줍니다. 페이지 로드가 앱의 [성능 예산](/ko/guides/panel-apps/app-kit/#성능-예산)을 초과하면 Insights가 초과한 횟수와 느렸던 쿼리를 경고합니다. Insights는 쿼리가 반환한 데이터나 앱을 연 사람의 이름을 절대 표시하지 않습니다.

두 탭 모두 앱이 프로젝트에 할당되어 있어야 합니다. 할당되지 않은 앱에는 할당하라는 메시지가 표시됩니다.

## 알림 및 다이제스트

**Alerts & Digests**를 선택하면 앱 데이터의 수치를 감시하다가 한도를 넘으면 알려 주거나 일정에 따라 요약을 보내는 알림을 설정할 수 있습니다. [알림 및 다이제스트](/ko/guides/panel-apps/alerts-and-digests/)를 참조하십시오.

## 갤러리에 앱 등록하기

**Gallery…** 를 선택하면 프로젝트를 볼 수 있는 누구나 자신의 앱을 만들 수 있는 템플릿으로 앱을 등록하거나 갤러리에서 제거할 수 있습니다. [앱 갤러리](/ko/guides/panel-apps/gallery/)를 참조하십시오.

## 홈에 고정

**Pin to Home**을 선택하면 프로젝트의 **홈** 보드에 앱이 추가되고, **Unpin from Home**을 선택하면 제거됩니다.

## 앱 삭제

Panel 앱을 삭제하면 먼저 확인을 요청합니다. **내 Panel 앱**에서 앱 행의 **빼기** 아이콘을 사용합니다. 게시 취소도 확인을 요청합니다.

## 다음 단계

- [Weave로 Panel 앱 빌드하기](/ko/guides/panel-apps/build-with-weave/) — 앱을 설명하고 정확한 변경 사항을 승인합니다.
- [Panel 앱 키트](/ko/guides/panel-apps/app-kit/) — Studio의 테이블, 뷰 및 템플릿 시작에서 사용하는 구성 요소.
- [알림 및 다이제스트](/ko/guides/panel-apps/alerts-and-digests/) — 수치가 한도를 넘거나 일정에 따라 사람들에게 알립니다.
- [앱 갤러리](/ko/guides/panel-apps/gallery/) — 다른 사람의 시작점으로 앱을 공유합니다.
- [Panel 앱 사용하기](/ko/guides/panel-apps/using/) — 게시 후의 로그, 사용량 및 다시 빌드.
