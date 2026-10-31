---
title: Assistant IA
description: Utilisez l'assistant IA intégré de PlaidCloud pour poser des questions, générer des expressions et agir sur vos projets en langage courant.
sidebar:
  label: Assistant IA
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/ai-assistant/index.md
---

L'assistant IA de PlaidCloud est l'expérience de chat intégrée à l'application pour poser des questions sur vos données, générer des expressions de workflow et effectuer des opérations en langage courant. Il est distinct de l'espace [Agents IA (MCP)](/fr/integrations/ai-coding-agents/), qui explique comment connecter des clients IA externes à votre tenant.

Pour comprendre son fonctionnement sous-jacent — quel modèle répond, comment la recherche d'information ancre une réponse, et ce
qui régit l'accès — lisez [Architecture IA et LLM](/fr/integrations/ai-architecture/).

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 700 210" role="img" aria-label="Vous posez une question à l'assistant IA en langage courant. Dans le périmètre du projet, l'assistant récupère les données et métadonnées du projet pour ancrer sa réponse, puis renvoie une réponse. Les conversations sont conservées, chacune avec le projet dans lequel elle a été commencée, à l'exception des plus anciennes, antérieures à l'appartenance des conversations à un projet, qui apparaissent dans l'historique de chaque projet." style="width:100%;max-width:700px;height:auto;">
  <defs><marker id="ai-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="78" width="140" height="46" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="84" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">votre question</text>
  <text x="84" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">langage courant</text>
  <path d="M154 101 L190 101" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="192" y="44" width="184" height="150" rx="12" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" stroke-dasharray="6 4" />
  <text x="204" y="38" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Périmètre du projet</text>
  <rect x="214" y="66" width="140" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="284" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">Assistant IA</text>
  <rect x="214" y="140" width="140" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="284" y="158" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">données + métadonnées du projet</text>
  <text x="284" y="172" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">tables · workflows · dimensions</text>
  <path d="M284 140 L284 120" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ai-arrow)" />
  <text x="360" y="134" font-size="9" fill="var(--sl-color-gray-3)">récupération</text>
  <path d="M376 92 L520 92" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="522" y="66" width="150" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="597" y="90" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">réponse ancrée</text>
  <text x="597" y="107" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">cite vos données</text>
  <text x="284" y="205" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">les conversations sont conservées</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Vous posez votre question en langage courant ; dans le périmètre du projet, l'assistant récupère vos données et métadonnées pour ancrer sa réponse. Les conversations sont conservées, chacune avec le projet dans lequel elle a été commencée ; les plus anciennes, antérieures à l'appartenance des conversations à un projet, apparaissent dans l'historique de chaque projet, marquées (aucun projet). Pour le mécanisme complet, consultez <a href="/fr/integrations/ai-architecture/">Architecture IA et LLM</a>.</figcaption>
</figure>

L'assistance IA apparaît aussi directement dans certaines étapes de workflow — par exemple, [la génération de la requête d'une étape SQL Extract](/fr/guides/ai-assistant/generate-sql-extract/) à partir d'une description en langage courant.
