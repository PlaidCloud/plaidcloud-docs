---
title: AI 에이전트(MCP)
description: Model Context Protocol(MCP) 서버를 통해 Claude, Cursor, GitHub Copilot, Gemini 및 기타 AI 에이전트를 PlaidCloud 테넌트에 연결합니다.
sidebar:
  label: AI 에이전트(MCP)
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

PlaidCloud는 모든 워크스페이스의 `/mcp`에서 선별된 [Model Context Protocol](https://modelcontextprotocol.io)(MCP) 서버를 제공합니다. AI 에이전트는 다른 MCP 서버에 연결하는 것과 같은 방식으로 이 서버에 연결한 다음, 도구를 호출하여 프로젝트를 읽고, 워크플로를 실행하고, 테이블을 쿼리하고, 차원을 관리하는 등의 작업을 수행합니다.

이 섹션의 페이지에서는 서버가 제공하는 기능, 인증 방법, 가장 일반적인 AI 클라이언트의 단계별 설정 방법을 다룹니다. 이 기능의 기반 아키텍처, 즉 모든 AI 요청이 거치는 관리형 경로, 검색 방식, 자체 모델을 실행하는 방법은 [AI 및 LLM 아키텍처](/ko/integrations/ai-architecture/)를 참조하십시오.

## PlaidCloud의 AI 분석이 다른 이유

- **[신뢰할 수 있는 답변](./honest-answers/)** — 모든 답변에는 신뢰도 신호와 쉬운 말로 된 주의 사항이 함께 제공되며, PlaidCloud는 숫자를 절대 지어내지 않습니다. 이러한 정직성 덕분에 AI 답변을 직접 다시 확인하지 않고도 그에 따라 행동할 수 있습니다.
- **[배부 추적](./tracing-allocations/)** — 배부 결과가 *왜* 바뀌었는지, 무엇이 그 결과에 영향을 주는지, 가상의 변경이 어떤 영향을 미치는지 쉬운 말로 물어볼 수 있습니다.
- **[분석 경로](./analysis-paths/)** — 주요 테이블에 알기 쉬운 이름과 기본값을 지정하면 "지난 분기에 왜 올랐나요?"처럼 바로 질문할 수 있습니다.
- **[대시보드 만들기](./build-dashboards/)** — 같은 PlaidCloud 연결을 통해 게시된 테이블과 뷰를 기반으로 차트와 대시보드를 요청할 수 있습니다.
- **[지표 정의](./metric-definitions/)** — 비즈니스 수치를 계산하는 방법을 한 번만 합의해 두면, 그 수치를 사용하는 모든 답변이 같은 방식으로 계산됩니다.

## 어시스턴트 연결

가장 빠른 방법은 PlaidCloud 자체 헤더 도구 모음에 있는 **AI 연결** 버튼을 사용하는 것입니다. 사용하는 클라이언트를 선택하고 표시되는 단계(MCP 서버 URL 포함)를 따르십시오.

- [시작하기](./getting-started/) — MCP 서버가 제공하는 기능과 인증 방법.
- [Microsoft 365 Copilot](/ko/integrations/microsoft-365-copilot/) — Teams와 Outlook에서 팀 전체가 PlaidCloud를 사용할 수 있습니다.
- 클라이언트별 설정: [Claude Code](./claude-code/), [Claude Desktop](./claude-desktop/), [Cursor](./cursor/), [GitHub Copilot](./copilot/), [Gemini](./gemini/), [ChatGPT](./chatgpt/), [Grok](./grok/).
