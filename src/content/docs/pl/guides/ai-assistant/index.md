---
title: Asystent AI
description: Korzystaj z wbudowanego asystenta AI PlaidCloud, aby zadawać pytania, generować wyrażenia i wykonywać operacje na projektach w języku naturalnym.
sidebar:
  label: Asystent AI
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/ai-assistant/index.md
---

Asystent AI PlaidCloud to czat w aplikacji, w którym zadajesz pytania o swoje dane, generujesz wyrażenia przepływów pracy i wykonujesz operacje w języku naturalnym. Jest oddzielony od obszaru [Agenci AI (MCP)](/pl/integrations/ai-coding-agents/), który dotyczy łączenia zewnętrznych klientów AI z Twoim tenantem.

Aby zobaczyć, jak działa to pod spodem — który model odpowiada, jak wyszukiwanie uziemia odpowiedź i co reguluje dostęp — przeczytaj [Architektura AI i LLM](/pl/integrations/ai-architecture/).

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 700 210" role="img" aria-label="Zadajesz asystentowi AI pytanie w języku naturalnym. W zakresie projektu asystent pobiera dane i metadane projektu, aby uziemić swoją odpowiedź, a następnie zwraca odpowiedź. Konwersacje są zachowywane, każda wraz z projektem, w którym została rozpoczęta, z wyjątkiem starszych z czasów, gdy konwersacje nie należały do projektu, które są widoczne w historii każdego projektu." style="width:100%;max-width:700px;height:auto;">
  <defs><marker id="ai-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="78" width="140" height="46" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="84" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Twoje pytanie</text>
  <text x="84" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">język naturalny</text>
  <path d="M154 101 L190 101" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="192" y="44" width="184" height="150" rx="12" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" stroke-dasharray="6 4" />
  <text x="204" y="38" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Zakres projektu</text>
  <rect x="214" y="66" width="140" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="284" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">Asystent AI</text>
  <rect x="214" y="140" width="140" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="284" y="158" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">dane i metadane projektu</text>
  <text x="284" y="172" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">tabele · przepływy pracy · wymiary</text>
  <path d="M284 140 L284 120" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ai-arrow)" />
  <text x="360" y="134" font-size="9" fill="var(--sl-color-gray-3)">wyszukiwanie</text>
  <path d="M376 92 L520 92" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="522" y="66" width="150" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="597" y="90" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">uziemiona odpowiedź</text>
  <text x="597" y="107" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">powołuje się na Twoje dane</text>
  <text x="284" y="205" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">konwersacje są zachowywane</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Pytasz zwykłym językiem; w zakresie projektu asystent pobiera Twoje dane i metadane, aby uziemić swoją odpowiedź. Konwersacje są zachowywane, każda wraz z projektem, w którym została rozpoczęta; starsze z czasów, gdy konwersacje nie należały do projektu, są widoczne w historii każdego projektu i oznaczone jako (brak projektu). Pełny mechanizm opisano w <a href="/pl/integrations/ai-architecture/">Architektura AI i LLM</a>.</figcaption>
</figure>

Pomoc AI pojawia się także bezpośrednio w niektórych krokach przepływu pracy — na przykład [generowanie zapytania kroku SQL Extract](/pl/guides/ai-assistant/generate-sql-extract/) na podstawie opisu w zwykłym języku.
