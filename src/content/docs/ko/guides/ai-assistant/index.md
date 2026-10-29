---
title: AI Assistant
description: PlaidCloud에 기본 제공되는 AI Assistant를 사용해 질문하고, 식을 생성하고, 자연어로 프로젝트를 조작합니다.
sidebar:
  label: AI Assistant
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/ai-assistant/index.md
---

PlaidCloud AI Assistant는 데이터에 대해 질문하고, 워크플로 식을 생성하고, 자연어로 작업을 수행하는 앱 내 채팅 환경입니다. 외부 AI 클라이언트를 테넌트에 연결하는 방법을 다루는 [AI 에이전트(MCP)](/ko/integrations/ai-coding-agents/) 영역과는 별개입니다.

내부적으로 어떻게 동작하는지, 즉 어떤 모델이 답변하는지, 검색이 답변을 어떻게 뒷받침하는지, 무엇이 접근을 제어하는지는 [AI 및 LLM 아키텍처](/ko/integrations/ai-architecture/)에서 확인하십시오.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 700 210" role="img" aria-label="사용자가 자연어로 AI Assistant에 질문합니다. 프로젝트 범위 안에서 어시스턴트가 프로젝트의 데이터와 메타데이터를 검색해 응답을 뒷받침한 다음 답변을 반환합니다. 대화는 유지되며 각 대화는 시작된 프로젝트와 함께 저장됩니다. 단, 대화가 프로젝트에 속하기 전의 이전 대화는 모든 프로젝트의 기록에 표시됩니다." style="width:100%;max-width:700px;height:auto;">
  <defs><marker id="ai-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="78" width="140" height="46" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="84" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">사용자 질문</text>
  <text x="84" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">자연어</text>
  <path d="M154 101 L190 101" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="192" y="44" width="184" height="150" rx="12" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" stroke-dasharray="6 4" />
  <text x="204" y="38" font-size="12" font-weight="700" fill="var(--sl-color-accent)">프로젝트 범위</text>
  <rect x="214" y="66" width="140" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="284" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">AI Assistant</text>
  <rect x="214" y="140" width="140" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="284" y="158" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">프로젝트 데이터 + 메타데이터</text>
  <text x="284" y="172" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">테이블 · 워크플로 · 차원</text>
  <path d="M284 140 L284 120" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ai-arrow)" />
  <text x="360" y="134" font-size="9" fill="var(--sl-color-gray-3)">검색</text>
  <path d="M376 92 L520 92" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="522" y="66" width="150" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="597" y="90" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">근거 기반 답변</text>
  <text x="597" y="107" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">사용자 데이터를 인용</text>
  <text x="284" y="205" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">대화 유지</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">일반 언어로 질문하면, 어시스턴트가 프로젝트 범위 안에서 데이터와 메타데이터를 검색해 답변의 근거로 삼습니다. 대화는 유지되며 각 대화는 시작된 프로젝트와 함께 저장됩니다. 대화가 프로젝트에 속하기 전의 이전 대화는 모든 프로젝트의 기록에 (프로젝트 없음)으로 표시됩니다. 전체 메커니즘은 <a href="/ko/integrations/ai-architecture/">AI 및 LLM 아키텍처</a>를 참조하십시오.</figcaption>
</figure>

AI 지원은 일부 워크플로 단계에서도 직접 제공됩니다. 예를 들어 일반 언어 설명으로 [SQL 추출 단계의 쿼리를 생성](/ko/guides/ai-assistant/generate-sql-extract/)할 수 있습니다.
