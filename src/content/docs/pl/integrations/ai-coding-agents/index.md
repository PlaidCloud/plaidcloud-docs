---
title: Agenci AI (MCP)
description: Połącz Claude, Cursor, GitHub Copilot, Gemini i innych agentów AI z Twoim tenantem PlaidCloud za pomocą serwera Model Context Protocol (MCP).
sidebar:
  label: Agenci AI (MCP)
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

PlaidCloud udostępnia wyselekcjonowany serwer [Model Context Protocol](https://modelcontextprotocol.io) (MCP) pod adresem `/mcp` w każdym obszarze roboczym. Agenci AI łączą się z nim tak samo jak z każdym innym serwerem MCP, a następnie wywołują narzędzia, aby odczytywać projekty, uruchamiać przepływy pracy, wykonywać zapytania do tabel, zarządzać wymiarami i nie tylko.

Strony w tej sekcji opisują, co udostępnia serwer, jak się uwierzytelnić oraz jak krok po kroku skonfigurować najpopularniejszych klientów AI. Architekturę, która za nimi stoi — nadzorowaną ścieżkę każdego żądania AI, sposób działania wyszukiwania kontekstu i uruchamianie własnego modelu — opisuje strona [Architektura AI i LLM](/pl/integrations/ai-architecture/).

## Co wyróżnia analizę AI w PlaidCloud

- **[Odpowiedzi, którym można zaufać](./honest-answers/)** — każda odpowiedź zawiera sygnał pewności i opisane prostym językiem zastrzeżenia, a PlaidCloud nigdy nie zmyśla liczb. Ta rzetelność pozwala działać na podstawie odpowiedzi AI bez ręcznego sprawdzania jej od nowa.
- **[Śledzenie alokacji](./tracing-allocations/)** — pytaj prostym językiem, *dlaczego* zmienił się zaalokowany wynik, co go zasila i co przyniosłaby hipotetyczna zmiana.
- **[Ścieżki analizy](./analysis-paths/)** — nadaj kluczowym tabelom przyjazne nazwy i ustaw domyślną, aby móc po prostu zapytać „dlaczego to wzrosło w zeszłym kwartale?”
- **[Definicje metryk](./metric-definitions/)** — ustal raz, jak obliczana jest dana liczba biznesowa, aby każda odpowiedź, która jej używa, była liczona tak samo.

## Połącz swojego asystenta

Najszybsza droga to przycisk **Połącz swoją AI** na pasku narzędzi w nagłówku PlaidCloud — wybierz klienta i postępuj zgodnie z wyświetlonymi krokami, wraz z adresem URL serwera MCP.

- [Pierwsze kroki](./getting-started/) — co udostępnia serwer MCP i jak się uwierzytelnić.
- [Microsoft 365 Copilot](/pl/integrations/microsoft-365-copilot/) — udostępnij PlaidCloud całemu zespołowi w Teams i Outlooku.
- Konfiguracja dla poszczególnych klientów: [Claude Code](./claude-code/), [Claude Desktop](./claude-desktop/), [Cursor](./cursor/), [GitHub Copilot](./copilot/), [Gemini](./gemini/), [ChatGPT](./chatgpt/), [Grok](./grok/).
