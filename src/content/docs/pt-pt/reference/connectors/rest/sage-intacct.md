---
title: Conector REST Sage Intacct
description: Configure uma ligação à API REST do Sage Intacct no PlaidCloud para integrar dados financeiros e contabilísticos nos seus fluxos de trabalho.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/sage-intacct.md
---

## Documentação da API

A documentação da API REST do Sage Intacct está disponível no [site Sage Developer](https://developer.sage.com/intacct/docs/1/sage-intacct-rest-api/get-started/quick-start).


## Requisitos de segurança

O PlaidCloud disponibiliza uma ligação **Intacct** dedicada na família de ligações REST (listada como **REST - Intacct**). Autentica-se com credenciais de cliente OAuth2 na API REST do Intacct: o par Sender ID/Sender password dos **Web Services** do Sage Intacct é introduzido como **ID do cliente** e **Segredo do cliente** da ligação, a que se juntam um Nome de utilizador do utilizador de serviço Web e um ID da empresa. As credenciais de remetente têm de ser ativadas para a sua empresa pelo suporte da Sage; o utilizador de Web Services tem de ter permissões para todos os objetos Intacct que o conector vai ler.

Trate o ID do cliente e o Segredo do cliente como segredos — guarde-os apenas através da área **Credentials** do PlaidCloud e faça referência a eles a partir da ligação.


## Obter as credenciais

1. Abra a área **Company Setup** do Sage Intacct
2. Ative os Web Services para o Sender ID fornecido pela Sage
3. Crie ou selecione um utilizador de Web Services para o PlaidCloud
4. Conceda ao utilizador permissões sobre todos os objetos que pretende consultar
5. Registe o ID da empresa, o Nome de utilizador do utilizador de serviço Web, o Sender ID e a Sender password


## Criar o conector Sage Intacct

1. Aceda a **Tools > Connections** e clique em `Add Connection`
2. Em **REST**, selecione **Intacct** (listado como **REST - Intacct**)
3. Introduza:
    * **Nome da ligação** — nome amigável apresentado nos passos do fluxo de trabalho
    * **ID do cliente** — o seu Sender ID do Intacct
    * **Segredo do cliente** — a sua Sender password do Intacct
    * **Nome de utilizador do utilizador de serviço Web** — o início de sessão do utilizador de Web Services
    * **ID da empresa** — a empresa Intacct à qual se está a ligar
4. Clique em `Test` para validar as credenciais
5. Clique em `Save`


## Utilizar nos passos do fluxo de trabalho

A mesma ligação serve para ler do Intacct e para lançar no Intacct. Pode ser selecionada em:

* [Import Sage AP](../../../workflow-steps/sage-intacct/import-sage-ap/) — cabeçalhos de faturas de fornecedor
* [Import Sage AP Lines](../../../workflow-steps/sage-intacct/import-sage-ap-lines/) — detalhe das linhas das faturas de fornecedor
* [Import Sage Intacct Query](../../../workflow-steps/sage-intacct/import-intacct-query/) — consulta genérica a qualquer objeto Intacct
* [Import Intacct Entity](../../../workflow-steps/sage-intacct/import-intacct-entity/) — detalhe do razão geral, saldos, lançamentos e dados mestre de dimensões, com paginação automática
* [Intacct: Lançar lançamento de diário](../../../workflow-steps/sage-intacct/export-to-sage/) — lançar lançamentos de diário
