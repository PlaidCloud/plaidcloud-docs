---
title: Conector REST do Sage Intacct
description: Configure uma conexão com a API REST do Sage Intacct no PlaidCloud para integrar dados financeiros e contábeis aos seus fluxos de trabalho.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/sage-intacct.md
---

## Documentação da API

A documentação da API REST do Sage Intacct está disponível no [site Sage Developer](https://developer.sage.com/intacct/docs/1/sage-intacct-rest-api/get-started/quick-start).


## Requisitos de segurança

O PlaidCloud oferece uma conexão **Intacct** dedicada na família de conexões REST (listada como **REST - Intacct**). Ela se autentica com credenciais de cliente OAuth2 na API REST do Intacct: o par Sender ID/Sender password dos **Web Services** do Sage Intacct é informado como **ID do cliente** e **Segredo do cliente** da conexão, além de um nome de usuário do usuário de serviço web e de um ID da empresa. As credenciais do remetente precisam ser habilitadas para a sua empresa pelo suporte da Sage; o usuário de Web Services precisa ter permissões em todos os objetos do Intacct que o conector vai ler.

Trate o ID do cliente e o Segredo do cliente como segredos: armazene-os somente pela área **Credenciais** do PlaidCloud e faça referência a eles a partir da conexão.


## Obter as credenciais

1. Abra a área **Company Setup** do Sage Intacct
2. Ative os Web Services para o Sender ID fornecido pela Sage
3. Crie ou selecione um usuário de Web Services para o PlaidCloud
4. Conceda ao usuário permissões em todos os objetos que você pretende consultar
5. Anote o ID da empresa, o nome de usuário do usuário de serviço web, o Sender ID e a Sender password


## Criar o conector do Sage Intacct

1. Acesse **Tools > Connections** e clique em `Add Connection`
2. Em **REST**, selecione **Intacct** (listado como **REST - Intacct**)
3. Informe:
    * **Nome da conexão** — nome amigável exibido nas etapas de fluxo de trabalho
    * **ID do cliente** — o seu Sender ID do Intacct
    * **Segredo do cliente** — a sua Sender password do Intacct
    * **Nome de usuário do usuário de serviço web** — o login do usuário de Web Services
    * **ID da empresa** — a empresa do Intacct à qual você está se conectando
4. Clique em `Test` para validar as credenciais
5. Clique em `Save`


## Usar em etapas de fluxo de trabalho

A mesma conexão serve tanto para ler quanto para lançar no Intacct. Ela pode ser selecionada em:

* [Import Sage AP](../../../workflow-steps/sage-intacct/import-sage-ap/) — cabeçalhos de contas a pagar
* [Import Sage AP Lines](../../../workflow-steps/sage-intacct/import-sage-ap-lines/) — detalhes das linhas de contas a pagar
* [Import Sage Intacct Query](../../../workflow-steps/sage-intacct/import-intacct-query/) — consulta genérica em qualquer objeto do Intacct
* [Import Intacct Entity](../../../workflow-steps/sage-intacct/import-intacct-entity/) — detalhes do razão geral, saldos, lançamentos e mestres de dimensão, com paginação automática
* [Intacct: Lançar lançamento contábil](../../../workflow-steps/sage-intacct/export-to-sage/) — lança lançamentos contábeis
