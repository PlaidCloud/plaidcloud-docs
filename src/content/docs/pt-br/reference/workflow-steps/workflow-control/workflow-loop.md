---
title: Etapa Worklow Loop
description: Crie um loop em uma etapa de fluxo de trabalho do PlaidCloud para iterar sobre um conjunto de valores e repetir etapas para cada item da coleção.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/workflow-loop.md
---

## Descrição

Executa um fluxo de trabalho de destino uma vez por linha de um conjunto de dados, definindo os valores das colunas de cada linha como variáveis do projeto antes de cada iteração. Use esta etapa quando houver um processo parametrizado que precisa ser executado várias vezes com entradas diferentes — por exemplo, "executar o fechamento mensal para cada unidade de negócios desta tabela" ou "carregar este relatório para cada trimestre listado".

Cada iteração do loop enxerga as variáveis como se tivessem sido definidas manualmente; assim, o fluxo de trabalho chamado pode referenciá-las em expressões, filtros, caminhos de arquivo e nomes de tabela usando a sintaxe padrão `\{variable_name}`. O loop é sequencial por padrão; as iterações não são executadas em paralelo.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 690 170" role="img" aria-label="Um Worklow Loop sobre um conjunto de dados com as linhas Q1, Q2 e Q3. Os valores das colunas de cada linha viram variáveis do projeto e, em seguida, o fluxo de trabalho de destino é executado — uma passagem por linha, em sequência, não em paralelo." style="width:100%;max-width:690px;height:auto;">
  <defs><marker id="wl-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="50" width="120" height="74" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="74" y="44" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">conjunto de dados</text>
  <text x="74" y="76" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q1</text>
  <text x="74" y="96" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q2</text>
  <text x="74" y="116" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q3</text>
  <path d="M134 87 L178 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="180" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="250" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q1</text>
  <text x="250" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">passagem 1</text>
  <path d="M320 87 L360 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="362" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="432" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q2</text>
  <text x="432" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">passagem 2</text>
  <path d="M502 87 L542 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="544" y="63" width="138" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="613" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q3</text>
  <text x="613" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">passagem 3</text>
  <text x="408" y="142" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">sequencial — uma passagem por vez, não em paralelo</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">As colunas de cada linha viram variáveis do projeto e, em seguida, o fluxo de trabalho de destino é executado — uma passagem por linha, em sequência. Para um fan-out paralelo e isolado, use uma <a href="/pt-br/guides/workflows/create-a-macro/">Macro</a>.</figcaption>
</figure>



## Fluxo de trabalho a parar


Primeiro, selecione o projeto que contém o fluxo de trabalho que será executado em cada volta do loop no menu suspenso **Projeto**.



Em seguida, selecione o fluxo de trabalho específico a executar no menu suspenso **Fluxo de trabalho**.

## Se uma iteração falhar

Por padrão, o loop para na primeira iteração cujo fluxo de trabalho falha, e a etapa falha. Em **Tratamento de erros**, selecione **Continuar após uma iteração com falha** para executar todas as iterações mesmo quando uma falhar. Cada falha é mantida em **Status da execução do loop**, junto com o resultado de cada iteração, e a etapa termina com um aviso que informa quantas iterações falharam. Desmarcada, o loop para na primeira falha.

## Exemplos

Exemplos em breve
