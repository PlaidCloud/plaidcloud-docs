---
title: AI Assistant
description: Use the built-in PlaidCloud AI Assistant to ask questions, generate expressions, and operate on your projects in natural language.
sidebar:
  label: AI Assistant
  order: 14
---

The PlaidCloud AI Assistant is the in-app chat experience for asking questions about your data, generating workflow expressions, and performing operations in natural language. It is separate from the [AI Agents (MCP)](/integrations/ai-coding-agents/) area, which covers connecting external AI clients to your tenant.

To see how it works underneath — which model answers, how retrieval grounds an answer, and what
governs access — read [AI and LLM Architecture](/integrations/ai-architecture/).

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 700 210" role="img" aria-label="You ask the AI Assistant a question in natural language. Within the project scope, the assistant retrieves the project's data and metadata to ground its response, then returns an answer. Conversations persist and are isolated per project." style="width:100%;max-width:700px;height:auto;">
  <defs><marker id="ai-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="78" width="140" height="46" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="84" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">your question</text>
  <text x="84" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">natural language</text>
  <path d="M154 101 L190 101" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="192" y="44" width="184" height="150" rx="12" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" stroke-dasharray="6 4" />
  <text x="204" y="38" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Project scope</text>
  <rect x="214" y="66" width="140" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="284" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">AI Assistant</text>
  <rect x="214" y="140" width="140" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="284" y="158" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">project data + metadata</text>
  <text x="284" y="172" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">tables · workflows · dimensions</text>
  <path d="M284 140 L284 120" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ai-arrow)" />
  <text x="360" y="134" font-size="9" fill="var(--sl-color-gray-3)">retrieval</text>
  <path d="M376 92 L520 92" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="522" y="66" width="150" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="597" y="90" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">grounded answer</text>
  <text x="597" y="107" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">cites your data</text>
  <text x="284" y="205" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">conversations persist, isolated per project</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">You ask in plain language; within the project scope the assistant retrieves your data and metadata to ground its answer. Conversations persist and are isolated per project. For the full mechanism, see <a href="/integrations/ai-architecture/">AI and LLM Architecture</a>.</figcaption>
</figure>

AI assistance also appears directly in some workflow steps — for example, [generating a SQL Extract step's query](/guides/ai-assistant/generate-sql-extract/) from a plain-language description.
