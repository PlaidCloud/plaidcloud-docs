---
title: KI-Agenten (MCP)
description: Verbinden Sie Claude, Cursor, GitHub Copilot, Gemini und andere KI-Agenten über den MCP-Server (Model Context Protocol) mit Ihrem PlaidCloud-Tenant.
sidebar:
  label: KI-Agenten (MCP)
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

PlaidCloud stellt in jedem Workspace unter `/mcp` einen kuratierten [Model-Context-Protocol](https://modelcontextprotocol.io)-Server (MCP) bereit. KI-Agenten verbinden sich damit wie mit jedem anderen MCP-Server und rufen dann die Tools auf, um Projekte zu lesen, Workflows auszuführen, Tabellen abzufragen, Dimensionen zu verwalten und mehr.

Die Seiten in diesem Abschnitt behandeln, was der Server bereitstellt, wie die Authentifizierung funktioniert und wie Sie die gängigsten KI-Clients Schritt für Schritt einrichten. Zur dahinterliegenden Architektur – dem kontrollierten Weg jeder KI-Anfrage, der Funktionsweise des Retrievals und dem Betrieb eines eigenen Modells – siehe [KI- und LLM-Architektur](/de/integrations/ai-architecture/).

## Was die KI-Analyse von PlaidCloud auszeichnet

- **[Antworten, denen Sie vertrauen können](./honest-answers/)** – jede Antwort enthält ein Konfidenzsignal und Hinweise in verständlicher Sprache, und PlaidCloud erfindet nie eine Zahl. Diese Ehrlichkeit ermöglicht es Ihnen, auf eine KI-Antwort zu reagieren, ohne sie von Hand nachzuprüfen.
- **[Umlagen nachverfolgen](./tracing-allocations/)** – fragen Sie in verständlicher Sprache, *warum* sich ein umgelegtes Ergebnis geändert hat, was darin einfließt und was eine hypothetische Änderung bewirken würde.
- **[Analysepfade](./analysis-paths/)** – geben Sie Ihren wichtigsten Tabellen sprechende Namen und einen Standard, damit Sie einfach fragen können: „Warum ist das im letzten Quartal gestiegen?“
- **[Dashboards erstellen](./build-dashboards/)** – lassen Sie sich Diagramme und Dashboards über Ihre veröffentlichten Tabellen und Ansichten erstellen, über dieselbe PlaidCloud-Verbindung.
- **[Kennzahldefinitionen](./metric-definitions/)** – legen Sie einmal fest, wie eine Geschäftszahl berechnet wird, damit jede Antwort, die sie verwendet, auf dieselbe Weise berechnet wird.

## Ihren Assistenten verbinden

Am schnellsten geht es mit der Schaltfläche **Ihre KI verbinden** in der Kopfleiste von PlaidCloud – wählen Sie Ihren Client und folgen Sie den angezeigten Schritten, einschließlich der MCP-Server-URL.

- [Erste Schritte](./getting-started/) – was der MCP-Server bereitstellt und wie Sie sich authentifizieren.
- [Microsoft 365 Copilot](/de/integrations/microsoft-365-copilot/) – stellen Sie PlaidCloud Ihrem gesamten Team in Teams und Outlook bereit.
- Einrichtung pro Client: [Claude Code](./claude-code/), [Claude Desktop](./claude-desktop/), [Cursor](./cursor/), [GitHub Copilot](./copilot/), [Gemini](./gemini/), [ChatGPT](./chatgpt/), [Grok](./grok/).
