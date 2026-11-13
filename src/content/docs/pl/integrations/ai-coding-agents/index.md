---
title: Agenci AI (MCP)
description: Połącz Claude, Cursor, GitHub Copilot, Gemini i innych agentów AI z dzierżawą PlaidCloud za pomocą serwera Model Context Protocol (MCP).
sidebar:
  label: Agenci AI (MCP)
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

PlaidCloud udostępnia wyselekcjonowany serwer [Model Context Protocol](https://modelcontextprotocol.io) (MCP) pod adresem `/mcp` w każdym obszarze roboczym. Agenci AI łączą się z nim tak samo jak z każdym innym serwerem MCP, a następnie wywołują narzędzia, aby odczytywać projekty, uruchamiać przepływy pracy, wykonywać zapytania do tabel, zarządzać wymiarami i nie tylko.

Strony w tej sekcji opisują, co udostępnia serwer, jak się uwierzytelniać oraz jak krok po kroku skonfigurować najpopularniejszych klientów AI. Architekturę, która za tym stoi — kontrolowaną ścieżkę każdego żądania AI, sposób działania wyszukiwania i uruchamianie własnego modelu — opisano w [Architekturze AI i LLM](/pl/integrations/ai-architecture/).

## Czym wyróżnia się analiza AI w PlaidCloud

- **[Odpowiedzi, którym można zaufać](./honest-answers/)** — każda odpowiedź zawiera sygnał pewności i zastrzeżenia w prostym języku, a PlaidCloud nigdy nie zmyśla liczb. Dzięki tej rzetelności można działać na podstawie odpowiedzi AI bez ręcznego sprawdzania.
- **[Śledzenie alokacji](./tracing-allocations/)** — pytaj prostym językiem, *dlaczego* zmienił się zaalokowany wynik, co go zasila i jaki skutek miałaby hipotetyczna zmiana.
- **[Ścieżki analizy](./analysis-paths/)** — nadaj kluczowym tabelom przyjazne nazwy i domyślną, aby wystarczyło zapytać „dlaczego to wzrosło w ostatnim kwartale?”
- **[Budowanie pulpitów](./build-dashboards/)** — poproś o wykresy i pulpity na podstawie opublikowanych tabel i widoków, przez to samo połączenie z PlaidCloud.
- **[Definicje metryk](./metric-definitions/)** — ustal raz, jak oblicza się liczbę biznesową, aby każda odpowiedź, która jej używa, była obliczana tak samo.

## Połącz swojego asystenta

Najszybszą drogą jest pozycja **Połącz swoją AI** w menu awatara (użytkownika) PlaidCloud — wybierz swojego klienta i postępuj zgodnie z pokazanymi krokami, w tym z adresem URL serwera MCP.

- [Pierwsze kroki](./getting-started/) — co udostępnia serwer MCP i jak się uwierzytelniać.
- [Microsoft 365 Copilot](/pl/integrations/microsoft-365-copilot/) — udostępnij PlaidCloud całemu zespołowi w Teams i Outlooku.
- Konfiguracja dla poszczególnych klientów: [Claude Code](./claude-code/), [Claude Desktop](./claude-desktop/), [Cursor](./cursor/), [GitHub Copilot](./copilot/), [Gemini](./gemini/), [ChatGPT](./chatgpt/), [Grok](./grok/).
