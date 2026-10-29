---
title: Grok
description: xAI의 Grok을 사용자 지정 커넥터를 통해 PlaidCloud의 MCP 서버에 연결합니다.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/grok.md
---

[Grok](https://grok.com)은 grok.com에서 구성하는 사용자 지정 커넥터를 통해 MCP 서버를 지원합니다.

## 설정

1. [grok.com/connectors](https://grok.com/connectors)로 이동하여 **New Connector → Custom**을 클릭합니다.
2. MCP 서버 URL을 붙여 넣습니다. `https://<your-workspace>.plaid.cloud/mcp`.
3. Grok이 PlaidCloud로 리디렉션하면 로그인을 완료합니다. 요청한 애플리케이션과 자격 증명을 보낼 리디렉션 URI가 표시되는 **Application Access Request** 페이지가 나타납니다. 승인하기 전에 두 항목이 Grok과 일치하는지 확인하십시오.

## 회사 요금제

Business 및 Enterprise 워크스페이스에서는 팀 관리자가 커넥터 설정을 담당합니다. 워크스페이스 관리자가 grok.com/connectors에서 커넥터를 프로비저닝하면 멤버가 각자의 계정을 해당 커넥터에 연결합니다.

## 액세스 새로 고침

Grok에서 연결에 재인증이 필요하다고 알려 오면 로그인 단계를 다시 수행하십시오. 커넥터는 URL을 그대로 유지하므로 처음부터 다시 추가할 필요가 없습니다.
