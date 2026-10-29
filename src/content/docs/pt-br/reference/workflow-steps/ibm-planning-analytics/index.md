---
title: Etapas do IBM TM1 / Planning Analytics
description: Etapas de fluxo de trabalho que leem de um servidor IBM TM1 / Planning Analytics por meio da sua conexão TM1 — dados de cubo por visão salva ou MDX e hierarquias de dimensão — diretamente da nuvem ou por um agente PlaidLink local.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/index.md
---

Etapas de fluxo de trabalho que leem do IBM **TM1 / Planning Analytics** por meio da sua [conexão TM1](/pt-br/guides/connections/tm1/): dados de cubo por visão salva ou MDX, com um recorte opcional por ponto de vista, e hierarquias de dimensão carregadas em uma dimensão do PlaidCloud. Acesse o TM1 diretamente da nuvem ou, para um servidor acessível apenas de dentro da sua própria rede, por um agente PlaidLink local.

## Etapas

- [TM1: Consultar cubo](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — lê um cubo por visão salva ou MDX, com um recorte por ponto de vista e uma pré-visualização antes de salvar. Direto da nuvem.
- [TM1: Consultar cubo (agente)](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — o equivalente local de TM1: Consultar cubo, despachado por um agente PlaidLink instalado.
- [TM1: Ler dimensão](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — carrega uma hierarquia do TM1 em uma dimensão do PlaidCloud. Direto da nuvem.

## Relacionados

- [Conectar ao TM1 (guia)](/pt-br/guides/connections/tm1/)
- [Conector TM1](/pt-br/reference/connectors/rest/tm1/)
