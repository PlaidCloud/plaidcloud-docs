---
title: Asistente de IA
description: Use el asistente de IA integrado de PlaidCloud para hacer preguntas, generar expresiones y operar sobre sus proyectos en lenguaje natural.
sidebar:
  label: Asistente de IA
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/ai-assistant/index.md
---

El asistente de IA de PlaidCloud es la experiencia de chat integrada en la aplicación para hacer preguntas sobre sus datos, generar expresiones de flujos de trabajo y realizar operaciones en lenguaje natural. Es independiente del área de [agentes de IA (MCP)](/es/integrations/ai-coding-agents/), que trata de conectar clientes de IA externos a su inquilino.

Para ver cómo funciona por dentro (qué modelo responde, cómo la recuperación de información fundamenta una respuesta y qué rige el acceso), lea [Arquitectura de IA y LLM](/es/integrations/ai-architecture/).

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 700 210" role="img" aria-label="Usted hace una pregunta al asistente de IA en lenguaje natural. Dentro del ámbito del proyecto, el asistente recupera los datos y metadatos del proyecto para fundamentar su respuesta y luego devuelve una respuesta. Las conversaciones persisten, cada una con el proyecto en el que se inició, salvo las más antiguas, anteriores a que las conversaciones pertenecieran a un proyecto, que aparecen en el historial de todos los proyectos." style="width:100%;max-width:700px;height:auto;">
  <defs><marker id="ai-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="78" width="140" height="46" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="84" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">su pregunta</text>
  <text x="84" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">lenguaje natural</text>
  <path d="M154 101 L190 101" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="192" y="44" width="184" height="150" rx="12" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" stroke-dasharray="6 4" />
  <text x="204" y="38" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Ámbito del proyecto</text>
  <rect x="214" y="66" width="140" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="284" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">Asistente de IA</text>
  <rect x="214" y="140" width="140" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="284" y="158" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">datos + metadatos del proyecto</text>
  <text x="284" y="172" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">tablas · flujos de trabajo · dimensiones</text>
  <path d="M284 140 L284 120" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ai-arrow)" />
  <text x="360" y="134" font-size="9" fill="var(--sl-color-gray-3)">recuperación</text>
  <path d="M376 92 L520 92" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="522" y="66" width="150" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="597" y="90" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">respuesta fundamentada</text>
  <text x="597" y="107" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">cita sus datos</text>
  <text x="284" y="205" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">las conversaciones persisten</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Usted pregunta en lenguaje natural; dentro del ámbito del proyecto, el asistente recupera sus datos y metadatos para fundamentar su respuesta. Las conversaciones persisten, cada una con el proyecto en el que se inició; las más antiguas, anteriores a que las conversaciones pertenecieran a un proyecto, aparecen en el historial de todos los proyectos, marcadas como (sin proyecto). Para conocer el mecanismo completo, consulte <a href="/es/integrations/ai-architecture/">Arquitectura de IA y LLM</a>.</figcaption>
</figure>

La asistencia de IA también aparece directamente en algunos pasos de flujos de trabajo; por ejemplo, [generar la consulta de un paso SQL Extract](/es/guides/ai-assistant/generate-sql-extract/) a partir de una descripción en lenguaje natural.
