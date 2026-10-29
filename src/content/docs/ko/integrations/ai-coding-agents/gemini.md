---
title: Google Gemini CLI
description: Google의 gemini-cli가 PlaidCloud의 MCP 도구를 호출하도록 구성합니다.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/gemini.md
---

Google의 [`gemini-cli`](https://github.com/google-gemini/gemini-cli)는 `~/.gemini/settings.json`(사용자 범위) 또는 프로젝트 루트의 `.gemini/settings.json`(프로젝트 범위)을 통해 MCP 서버를 지원합니다.

## 설정

1. PlaidCloud에 로그인한 브라우저에서 `https://<your-workspace>.plaid.cloud/mcp/setup/token`에 접속하여 전달자 토큰을 가져옵니다.

2. `~/.gemini/settings.json`을 편집합니다(없으면 만듭니다).

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "httpUrl": "https://<your-workspace>.plaid.cloud/mcp",
          "headers": {
            "Authorization": "Bearer eyJhbGc…"
          }
        }
      }
    }
    ```

3. `gemini`를 다시 시작합니다. 세션 안에서 `/mcp`를 실행하여 서버가 연결되었는지 확인하고 도구를 나열합니다.

## 사용법

Gemini에게 PlaidCloud 도구를 직접 사용하도록 요청하십시오.

- "plaidcloud를 사용해서 `Sales Forecasting` 프로젝트의 워크플로를 나열해 줘."
- "`customers` 테이블의 열과 가장 최근 스냅샷을 설명해 줘."

특정 도구를 호출하기 전에 입력 스키마를 확인하고 싶다면 `/tools` 명령으로 도구를 명시적으로 호출할 수도 있습니다.

## 토큰 새로 고침

토큰이 만료되면 `https://<your-workspace>.plaid.cloud/mcp/setup/token`을 다시 불러와서 `settings.json`의 `Authorization` 값을 업데이트하십시오. 변경 사항을 반영하려면 `gemini`를 다시 시작합니다.

## Gemini Code Assist (IDE)

VSCode/JetBrains의 Gemini Code Assist는 에이전트 설정 아래에서 동일한 `mcpServers` 구성을 받습니다. 스키마가 CLI 형식과 같으므로 IDE의 MCP 서버 설정 패널에 동일한 스니펫을 붙여 넣으십시오.
