---
title: Cursor
description: Cursor IDE에서 내장 MCP 지원을 통해 PlaidCloud의 MCP 도구를 호출하도록 구성합니다.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/cursor.md
---

[Cursor](https://cursor.com)는 `mcp.json` 구성 파일을 통해 MCP 서버를 지원합니다. 형식이 Claude Code의 `.mcp.json`과 같으므로 동일한 전달자 토큰 스니펫이 둘 다에서 작동합니다.

PlaidCloud 헤더 도구 모음의 **AI 연결** 창에는 OAuth 로그인을 통해 서버를 추가하는 원클릭 링크인 **Cursor에 설치**가 있으며, 구성 파일은 필요하지 않습니다. 먼저 이를 시도하십시오. 아래의 전달자 토큰 구성은 이 페이지에서 전체를 설명하는 설정이며, 원클릭 링크로 서버가 추가되지 않거나 Cursor가 설치되어 있지 않을 때의 대체 방법입니다.

## 설정

1. PlaidCloud에 로그인한 브라우저에서 `https://<your-workspace>.plaid.cloud/mcp/setup/token`에 접속하여 전달자 토큰을 가져옵니다.

2. Cursor의 MCP 구성을 엽니다.
   - **프로젝트 범위**: 프로젝트 루트에 `.cursor/mcp.json`을 만듭니다.
   - **사용자 범위(모든 프로젝트)**: 홈 디렉터리에 `~/.cursor/mcp.json`을 만듭니다.

3. PlaidCloud 서버를 추가합니다.

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "url": "https://<your-workspace>.plaid.cloud/mcp",
          "headers": {
            "Authorization": "Bearer eyJhbGc…"
          }
        }
      }
    }
    ```

4. Cursor의 **Settings → MCP**를 열어 서버가 연결되었는지 확인합니다. 오류가 표시되면 [문제 해결](../troubleshooting/)을 참조하십시오.

## 도구 사용

Cursor의 Composer 또는 채팅 패널에서 일반 언어로 에이전트에게 요청하면("프로젝트 `Q4 Forecast`의 구조를 설명해 줘") 적절한 `plaidcloud_*` 도구를 선택합니다. 도구 호출과 응답이 인라인으로 표시되며, 변경 작업은 승인하기 전에 검토하십시오.

## 토큰 새로 고침

토큰이 만료되면 `https://<your-workspace>.plaid.cloud/mcp/setup/token`을 다시 불러와서 새 값을 `mcp.json`에 붙여 넣으십시오. Cursor는 전체 재시작 없이 변경 사항을 반영합니다. 필요하면 **Settings → MCP**에서 서버를 껐다가 다시 켜십시오.

## 여러 테넌트

다른 이름으로 항목을 반복합니다.

```json
{
  "mcpServers": {
    "plaidcloud-prod": { "url": "https://prod.plaid.cloud/mcp", "headers": { "Authorization": "Bearer …" } },
    "plaidcloud-dev":  { "url": "https://dev.plaid.cloud/mcp",  "headers": { "Authorization": "Bearer …" } }
  }
}
```
