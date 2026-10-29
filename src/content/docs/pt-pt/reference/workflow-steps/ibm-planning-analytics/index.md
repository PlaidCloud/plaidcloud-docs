---
title: Passos do IBM TM1 / Planning Analytics
description: Passos de fluxo de trabalho que leem de um servidor IBM TM1 / Planning Analytics através da sua ligação TM1 — dados de cubos por vista guardada ou MDX, e hierarquias de dimensões — diretamente na nuvem ou através de um agente PlaidLink local.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/index.md
---

Passos de fluxo de trabalho que leem do IBM **TM1 / Planning Analytics** através da sua [ligação TM1](/pt-pt/guides/connections/tm1/): dados de cubos por vista guardada ou MDX, com um corte opcional por ponto de vista, e hierarquias de dimensões carregadas numa dimensão do PlaidCloud. Aceda ao TM1 diretamente na nuvem ou, para um servidor acessível apenas a partir da sua própria rede, através de um agente PlaidLink local.

## Passos

- [TM1: Consultar cubo](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — lê um cubo por vista guardada ou MDX, com um corte por ponto de vista e uma pré-visualização antes de guardar. Diretamente na nuvem.
- [TM1: Consultar cubo (agente)](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — o equivalente local de TM1: Consultar cubo, enviado através de um agente PlaidLink instalado.
- [TM1: Ler dimensão](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — carrega uma hierarquia do TM1 numa dimensão do PlaidCloud. Diretamente na nuvem.

## Relacionados

- [Ligar ao TM1 (guia)](/pt-pt/guides/connections/tm1/)
- [Conector TM1](/pt-pt/reference/connectors/rest/tm1/)
