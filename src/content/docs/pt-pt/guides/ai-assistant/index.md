---
title: AI Assistant
description: Use o AI Assistant integrado do PlaidCloud para fazer perguntas, gerar expressões e operar nos seus projetos em linguagem natural.
sidebar:
  label: AI Assistant
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/ai-assistant/index.md
---

O AI Assistant do PlaidCloud é a experiência de chat integrada na aplicação para fazer perguntas sobre os seus dados, gerar expressões de fluxos de trabalho e executar operações em linguagem natural. É distinto da área [Agentes de IA (MCP)](/pt-pt/integrations/ai-coding-agents/), que trata da ligação de clientes de IA externos ao seu tenant.

Para ver como funciona por baixo — que modelo responde, como a obtenção de informação fundamenta uma resposta e o que
rege o acesso — leia [Arquitetura de IA e LLM](/pt-pt/integrations/ai-architecture/).

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 700 210" role="img" aria-label="Faz uma pergunta ao AI Assistant em linguagem natural. Dentro do âmbito do projeto, o assistente obtém os dados e metadados do projeto para fundamentar a resposta e depois devolve uma resposta. As conversas persistem, cada uma com o projeto em que foi iniciada, exceto as mais antigas, anteriores ao momento em que as conversas passaram a pertencer a um projeto, que aparecem no histórico de todos os projetos." style="width:100%;max-width:700px;height:auto;">
  <defs><marker id="ai-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="78" width="140" height="46" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="84" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">a sua pergunta</text>
  <text x="84" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">linguagem natural</text>
  <path d="M154 101 L190 101" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="192" y="44" width="184" height="150" rx="12" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" stroke-dasharray="6 4" />
  <text x="204" y="38" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Âmbito do projeto</text>
  <rect x="214" y="66" width="140" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="284" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">AI Assistant</text>
  <rect x="214" y="140" width="140" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="284" y="158" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">dados + metadados do projeto</text>
  <text x="284" y="172" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">tabelas · fluxos de trabalho · dimensões</text>
  <path d="M284 140 L284 120" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ai-arrow)" />
  <text x="360" y="134" font-size="9" fill="var(--sl-color-gray-3)">obtenção</text>
  <path d="M376 92 L520 92" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="522" y="66" width="150" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="597" y="90" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">resposta fundamentada</text>
  <text x="597" y="107" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">cita os seus dados</text>
  <text x="284" y="205" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">as conversas persistem</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Pergunta em linguagem corrente; dentro do âmbito do projeto, o assistente obtém os seus dados e metadados para fundamentar a resposta. As conversas persistem, cada uma com o projeto em que foi iniciada; as mais antigas, anteriores ao momento em que as conversas passaram a pertencer a um projeto, aparecem no histórico de todos os projetos, marcadas com (no project). Para o mecanismo completo, consulte <a href="/pt-pt/integrations/ai-architecture/">Arquitetura de IA e LLM</a>.</figcaption>
</figure>

A assistência de IA também aparece diretamente em alguns passos de fluxos de trabalho — por exemplo, [gerar a consulta de um passo Extrair SQL](/pt-pt/guides/ai-assistant/generate-sql-extract/) a partir de uma descrição em linguagem corrente.
