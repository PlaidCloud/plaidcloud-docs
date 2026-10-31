---
title: KI-Assistent
description: Nutzen Sie den integrierten PlaidCloud-KI-Assistenten, um Fragen zu stellen, Ausdrücke zu generieren und Ihre Projekte in natürlicher Sprache zu bedienen.
sidebar:
  label: KI-Assistent
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/ai-assistant/index.md
---

Der PlaidCloud-KI-Assistent ist das Chat-Erlebnis in der Anwendung, um Fragen zu Ihren Daten zu stellen, Workflow-Ausdrücke zu generieren und Vorgänge in natürlicher Sprache auszuführen. Er ist getrennt vom Bereich [KI-Agenten (MCP)](/de/integrations/ai-coding-agents/), der die Anbindung externer KI-Clients an Ihren Tenant behandelt.

Wie er im Hintergrund arbeitet – welches Modell antwortet, wie Retrieval eine Antwort fundiert und was den Zugriff regelt –, lesen Sie unter [KI- und LLM-Architektur](/de/integrations/ai-architecture/).

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 700 210" role="img" aria-label="Sie stellen dem KI-Assistenten eine Frage in natürlicher Sprache. Innerhalb des Projektbereichs ruft der Assistent die Daten und Metadaten des Projekts ab, um seine Antwort zu fundieren, und liefert dann eine Antwort. Unterhaltungen bleiben erhalten, jeweils mit dem Projekt, in dem sie begonnen wurden, außer älteren aus der Zeit, bevor Unterhaltungen zu einem Projekt gehörten; diese erscheinen im Verlauf jedes Projekts." style="width:100%;max-width:700px;height:auto;">
  <defs><marker id="ai-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="78" width="140" height="46" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="84" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Ihre Frage</text>
  <text x="84" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">natürliche Sprache</text>
  <path d="M154 101 L190 101" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="192" y="44" width="184" height="150" rx="12" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" stroke-dasharray="6 4" />
  <text x="204" y="38" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Projektbereich</text>
  <rect x="214" y="66" width="140" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="284" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">KI-Assistent</text>
  <rect x="214" y="140" width="140" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="284" y="158" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">Projektdaten + Metadaten</text>
  <text x="284" y="172" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">Tabellen · Workflows · Dimensionen</text>
  <path d="M284 140 L284 120" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ai-arrow)" />
  <text x="360" y="134" font-size="9" fill="var(--sl-color-gray-3)">Retrieval</text>
  <path d="M376 92 L520 92" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="522" y="66" width="150" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="597" y="90" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">fundierte Antwort</text>
  <text x="597" y="107" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">belegt mit Ihren Daten</text>
  <text x="284" y="205" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">Unterhaltungen bleiben erhalten</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Sie fragen in einfacher Sprache; innerhalb des Projektbereichs ruft der Assistent Ihre Daten und Metadaten ab, um seine Antwort zu fundieren. Unterhaltungen bleiben erhalten, jeweils mit dem Projekt, in dem sie begonnen wurden; ältere aus der Zeit, bevor Unterhaltungen zu einem Projekt gehörten, erscheinen im Verlauf jedes Projekts und sind mit (no project) gekennzeichnet. Den vollständigen Mechanismus beschreibt die <a href="/de/integrations/ai-architecture/">KI- und LLM-Architektur</a>.</figcaption>
</figure>

KI-Unterstützung gibt es auch direkt in einigen Workflow-Schritten – zum Beispiel beim [Generieren der Abfrage eines SQL-Extract-Schritts](/de/guides/ai-assistant/generate-sql-extract/) aus einer Beschreibung in einfacher Sprache.
