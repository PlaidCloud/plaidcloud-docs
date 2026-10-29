---
title: Conector REST do Dynamics 365 Finance & Operations
description: Configure uma conexão com o Dynamics 365 Finance & Operations no PlaidCloud para importar entidades OData/DMF e lançar lançamentos contábeis de forma assíncrona.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics-365-fo.md
---

## Documentação da API

Os [endpoints OData v4](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata) e o [Data Management Framework](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-management-import-export) do D365 F&O documentam os endpoints e o caminho de extração em massa usados por este conector.

## Como funciona a autenticação

A conexão se autentica como um aplicativo usando **credenciais de cliente** do Entra ID (Azure AD): o ID do cliente e o segredo de um registro de aplicativo são trocados por um token de acesso, com escopo no recurso do ambiente. Não há login interativo.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| URL do ambiente | Texto | A URL do seu ambiente D365 F&O, por exemplo `https://yourorg.operations.dynamics.com`. |
| ID do cliente | Texto | O ID do aplicativo (cliente) do registro de aplicativo do Entra. |
| Segredo do cliente | Texto | O segredo do cliente do registro de aplicativo. Armazenado de forma criptografada. |
| ID do tenant | Texto | O ID do seu tenant do Azure AD. |
| Recurso/Escopo | Texto | O escopo OAuth2 solicitado, normalmente a URL do ambiente mais `/.default`. |

## Entidades disponíveis para importação

A etapa **Import D365 F&O Entity** cobre seis entidades: `main_accounts`, `currencies`, `customers`, `vendors`, `released_products`, `ledger_journal_headers`. Cada extração é executada no modo de sincronização `odata` (uma chamada direta, para extrações de rotina) ou no modo em massa `dmf` (um job de exportação assíncrono do Data Management Framework, para extrações grandes) e oferece filtros do lado do servidor por entidade, incluindo intervalos de data, conta e dimensão. Consulte a etapa [Import D365 F&O Entity](/pt-br/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) para a referência completa dos campos.

## Lançamento de lançamentos contábeis

A etapa **D365 F&O: Post Journal Entry** lança lançamentos contábeis do razão geral pelo pipeline de gravação de ERP compartilhado do PlaidCloud: envia para a ação assíncrona de lançamento de diário do serviço personalizado do D365 F&O, consulta até um estado final e confirma antes de informar que um lançamento foi efetuado. Uma correção lança um novo lançamento de estorno, com débito e crédito invertidos, em vez de editar o original. Consulte a etapa [D365 F&O: Post Journal Entry](/pt-br/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) para a referência dos campos e [Conectar ao Dynamics 365 Finance & Operations](/pt-br/guides/connections/dynamics-365-fo/) para o passo a passo completo de lançamento.

## Limitações conhecidas

| Limitação | O que significa |
|---|---|
| O modo de sincronização DMF tem latência de extração | Uma extração `dmf` espera por um job de exportação assíncrono, o que é bem mais lento do que uma extração `odata` do mesmo tamanho. |
| A filtragem por dimensão depende da estrutura | Uma dimensão financeira que não faz parte da estrutura de contas não pode ser filtrada no servidor; delimite-a no seu fluxo de trabalho depois da extração. |
## Relacionados

- [Conectar ao Dynamics 365 Finance & Operations (guia)](/pt-br/guides/connections/dynamics-365-fo/) — passo a passo: criar a conexão, testá-la, importar uma entidade e lançar um diário.
- [Import D365 F&O Entity](/pt-br/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/)
- [D365 F&O: Post Journal Entry](/pt-br/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/)
- [Revisar o histórico de lançamentos de ERP](/pt-br/guides/connections/erp-post-history/)
