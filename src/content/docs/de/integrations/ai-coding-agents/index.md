---
title: KI-Agents (MCP)
description: Verbinden Sie Claude, Cursor, GitHub Copilot, Gemini und andere KI-Agents über den MCP-Server (Model Context Protocol) mit Ihrem PlaidCloud-Mandanten.
sidebar:
  label: KI-Agents (MCP)
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

PlaidCloud stellt in jedem Workspace unter `/mcp` einen kuratierten [Model-Context-Protocol](https://modelcontextprotocol.io)-Server (MCP) bereit. KI-Agents verbinden sich damit genauso wie mit jedem anderen MCP-Server und rufen dann die Werkzeuge auf, um Projekte zu lesen, Workflows auszuführen, Tabellen abzufragen, Dimensionen zu verwalten und mehr.

Die Seiten in diesem Abschnitt behandeln, was der Server bereitstellt, wie Sie sich authentifizieren und wie Sie die gängigsten KI-Clients Schritt für Schritt einrichten. Die dahinterliegende Architektur – der kontrollierte Weg jeder KI-Anfrage, die Funktionsweise der Abfrage und wie Sie ein eigenes Modell betreiben – finden Sie unter [KI- und LLM-Architektur](/de/integrations/ai-architecture/).

## Was die KI-Analyse von PlaidCloud auszeichnet

- **[Antworten, denen Sie vertrauen können](./honest-answers/)** – jede Antwort trägt ein Konfidenzsignal und verständliche Hinweise, und PlaidCloud erfindet nie eine Zahl. Diese Ehrlichkeit ermöglicht es Ihnen, auf eine KI-Antwort zu handeln, ohne sie von Hand erneut zu prüfen.
- **[Umlagen nachvollziehen](./tracing-allocations/)** – fragen Sie in einfacher Sprache, *warum* sich ein umgelegtes Ergebnis geändert hat, was es speist und was eine hypothetische Änderung bewirken würde.
- **[Analysepfade](./analysis-paths/)** – geben Sie Ihren wichtigsten Tabellen sprechende Namen und einen Standard, damit Sie einfach fragen können „warum ist das im letzten Quartal gestiegen?“
- **[Dashboards erstellen](./build-dashboards/)** – bitten Sie über dieselbe PlaidCloud-Verbindung um Diagramme und Dashboards auf Ihren veröffentlichten Tabellen und Ansichten.
- **[Kennzahldefinitionen](./metric-definitions/)** – legen Sie einmal fest, wie eine Geschäftszahl berechnet wird, damit jede Antwort, die sie verwendet, auf dieselbe Weise berechnet wird.

## Ihren Assistenten verbinden

Der schnellste Weg ist der Eintrag **Ihre KI verbinden** im Avatar-Menü (Benutzermenü) von PlaidCloud – wählen Sie Ihren Client und folgen Sie den angezeigten Schritten, einschließlich der MCP-Server-URL.

- [Erste Schritte](./getting-started/) – was der MCP-Server bereitstellt und wie Sie sich authentifizieren.
- [Microsoft 365 Copilot](/de/integrations/microsoft-365-copilot/) – bringen Sie PlaidCloud in Teams und Outlook zu Ihrem ganzen Team.
- Einrichtung pro Client: [Claude Code](./claude-code/), [Claude Desktop](./claude-desktop/), [Cursor](./cursor/), [GitHub Copilot](./copilot/), [Gemini](./gemini/), [ChatGPT](./chatgpt/), [Grok](./grok/).
