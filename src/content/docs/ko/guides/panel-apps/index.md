---
title: Panel 앱
description: PlaidCloud에서 대화형 HoloViz Panel 데이터 애플리케이션을 정적 브라우저 내 앱 또는 git 리포지토리에서 빌드한 서버 측 앱으로 빌드하고 배포합니다.
sidebar:
  label: Panel 앱
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/index.md
---

Panel 앱을 사용하면 매개변수화된 입력, 실시간 차트, 임베디드 데이터 테이블을 갖춘 대화형 [HoloViz Panel](https://panel.holoviz.org/) 애플리케이션을 PlaidCloud에서 바로 게시할 수 있습니다. **내 Panel 앱** 화면에서 관리하며, 이 화면에는 모든 앱이 런타임, 빌드 상태, URL과 함께 나열됩니다.

[Panel Studio](/ko/guides/panel-apps/studio/)에서 시작하십시오. **새 Studio 앱**을 선택하면 설정할 리포지토리 없이 PlaidCloud에서 빈 앱, 테이블, 뷰 또는 갤러리로 앱을 빌드할 수 있습니다. 맞춤 요구 사항이 있으면 **런타임** 열에 표시되는 다음 런타임 중 하나로 게시하십시오.

- **WASM** — 브라우저(Pyodide)에서 전체가 실행되는 정적 앱입니다. 문서 계정에서 미리 빌드된 HTML 파일을 게시합니다. 서버 프로세스가 없고 확장할 것도 없으며 즉시 제공됩니다.
- **서버** — git 리포지토리에서 빌드되어 서버 측에서 실행되는 앱입니다. 게시하면 PlaidCloud가 리포지토리를 컨테이너로 빌드하며, 컨테이너는 복제본 0개로 유휴 상태에 있다가 URL에 대한 첫 요청에 깨어나 (실시간 업데이트를 포함하여) 서비스하고 유휴 상태가 되면 다시 0으로 축소됩니다. Python 런타임, 서버 측 컴퓨팅 또는 브라우저에서 실행할 수 없는 라이브러리가 필요한 앱에 적합합니다.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 250" role="img" aria-label="두 가지 Panel 앱 런타임. WASM 앱은 서버 없이 브라우저에 바로 제공되는 미리 빌드된 HTML 파일입니다. 서버 앱은 git 리포지토리에서 컨테이너로 빌드되며, 복제본 0개로 유휴 상태에 있다가 첫 요청에 약 15초 만에 깨어나 서비스하고 유휴 상태가 되면 다시 0으로 축소됩니다." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pa-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="14" y="40" font-size="12" font-weight="700" fill="var(--sl-color-accent)">WASM</text>
  <rect x="70" y="24" width="150" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="49" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">미리 빌드된 HTML 파일</text>
  <path d="M220 45 L286 45" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="288" y="24" width="164" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="370" y="43" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">브라우저 · Pyodide</text>
  <text x="370" y="58" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">즉시 제공</text>
  <line x1="14" y1="96" x2="666" y2="96" stroke="var(--sl-color-gray-5)" stroke-dasharray="3 3" />
  <text x="14" y="146" font-size="12" font-weight="700" fill="var(--sl-color-accent)">서버</text>
  <rect x="70" y="128" width="96" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="118" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">git 리포지토리</text>
  <path d="M166 149 L186 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="188" y="128" width="110" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="243" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">컨테이너 빌드</text>
  <path d="M298 149 L318 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="320" y="128" width="120" height="42" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="380" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">유휴 · 복제본 0개</text>
  <text x="380" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">실행 중인 항목 없음</text>
  <path d="M440 149 L474 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <text x="457" y="140" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">첫 요청</text>
  <rect x="476" y="128" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="536" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">서비스 중</text>
  <text x="536" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">약 15초 후 깨어남</text>
  <path d="M536 170 C536 212 380 212 380 174" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#pa-arrow)" />
  <text x="458" y="206" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">유휴 상태가 되면 0으로 축소</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">두 가지 런타임: <strong>WASM</strong> 앱은 브라우저에 바로 제공되는 미리 빌드된 HTML 파일이고, <strong>서버</strong> 앱은 git에서 빌드되어 0으로 유휴 상태에 있다가 첫 요청(약 15초)에 깨어나 서비스하고 다시 0으로 축소됩니다.</figcaption>
</figure>

## 런타임 선택

| | WASM | 서버 |
|---|---|---|
| 소스 | 게시된 HTML 파일 | git 리포지토리(연결, 브랜치, 진입점) |
| 실행 위치 | 브라우저 | 서버 측, 0으로 축소 |
| 적합한 용도 | 가볍고 독립적인 대시보드 | 서버 컴퓨팅이나 전체 Python 라이브러리가 필요한 앱 |
| 콜드 스타트 | 없음 | 첫 요청에 앱이 시작됨(약 15초) |

## 다음 단계

- [Panel Studio](/ko/guides/panel-apps/studio/) — 설정할 리포지토리 없이 PlaidCloud에서 앱을 만들고, 편집하고, 미리 보고, 게시합니다.
- [PlaidCloud Git에서 Panel 앱 배포](/ko/guides/panel-apps/deploy-from-git/) — 자격 증명이 필요 없는 관리형 연결을 사용하여 리포지토리에서 제공되는 앱까지의 전체 과정입니다.
- [Weave로 Panel 앱 빌드](/ko/guides/panel-apps/build-with-weave/) — 앱을 설명하고 Weave가 제안하는 정확한 변경 사항을 승인합니다.
- [Panel 앱 만들기](/ko/guides/panel-apps/creating/) — 빈 앱, 테이블 또는 갤러리에서 Studio 앱을 시작하거나, git의 서버 앱 또는 파일의 WASM 앱을 게시합니다.
- [Panel 앱 키트](/ko/guides/panel-apps/app-kit/) — 필터, 주요 수치, 서버 페이징 데이터 그리드, 차트, 양식, 실행 버튼, 저장된 설정, 인쇄를 갖춘 PlaidCloud 모양의 앱을 라이트와 다크 테마로 빌드합니다.
- [Panel 앱용 Data API](/ko/guides/panel-apps/data-api/) — 서버에서 테이블을 필터링, 페이징, 집계 및 개수 확인합니다.
- [알림 및 다이제스트](/ko/guides/panel-apps/alerts-and-digests/) — 수치가 한도를 넘으면 푸시 알림, 이메일, Slack 또는 Teams 메시지를 받거나 예약된 요약을 받습니다.
- [앱 갤러리](/ko/guides/panel-apps/gallery/) — 앱을 템플릿으로 등록하고 등록된 앱으로 새 앱을 만듭니다.
- [프로젝트 브랜딩 및 앱 프로젝트](/ko/guides/panel-apps/branding/) — 프로젝트 앱의 색상과 로고를 설정하고 앱을 프로젝트에 할당합니다.
- [Panel 앱 사용](/ko/guides/panel-apps/using/) — 빌드 상태, 앱 열기, 편집, 제거에 대해 설명합니다.
- [Panel 앱 내부에서 AI 에이전트 빌드](/ko/get-started/tutorials/panel-ai-agent/) — 튜토리얼: AI 에이전트에 사용자 자신의 권한 범위로 제한된 REST API를 도구로 제공합니다.
