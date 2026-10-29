---
title: Conector REST Dynamics 365 Finance & Operations
description: Configure uma ligação ao Dynamics 365 Finance & Operations no PlaidCloud para importar entidades OData/DMF e lançar lançamentos de diário de forma assíncrona.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics-365-fo.md
---

## Documentação da API

Os [pontos de acesso OData v4](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata) e a [Data Management Framework](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-management-import-export) do D365 F&O documentam os pontos de acesso e o caminho de extração em massa que este conector utiliza.

## Como funciona a autenticação

A ligação autentica-se como uma aplicação através do Entra ID (Azure AD) com **credenciais de cliente** — o ID de cliente e o segredo de um registo de aplicação são trocados por um token de acesso, com o âmbito do recurso do ambiente. Não existe início de sessão interativo.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de apresentação desta ligação. |
| URL do ambiente | Texto | O URL do seu ambiente D365 F&O, por exemplo `https://yourorg.operations.dynamics.com`. |
| ID do cliente | Texto | O ID da aplicação (cliente) do registo de aplicação Entra. |
| Segredo do cliente | Texto | O segredo de cliente do registo de aplicação. Guardado cifrado. |
| ID do inquilino | Texto | O ID do seu inquilino Azure AD. |
| Recurso/Âmbito | Texto | O âmbito OAuth2 pedido, normalmente o URL do ambiente mais `/.default`. |

## Entidades disponíveis para importação

O passo **Import D365 F&O Entity** abrange seis entidades: `main_accounts`, `currencies`, `customers`, `vendors`, `released_products`, `ledger_journal_headers`. Cada extração é executada no modo de sincronização `odata` (uma chamada direta, para extrações de rotina) ou no modo em massa `dmf` (uma tarefa assíncrona de exportação da Data Management Framework, para extrações grandes) e suporta filtros do lado do servidor por entidade, incluindo intervalos de datas, de contas e de dimensões. Consulte [Import D365 F&O Entity](/pt-pt/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) para a referência completa dos campos.

## Lançamento de lançamentos de diário

O passo **D365 F&O: Post Journal Entry** lança lançamentos de diário do razão geral através do pipeline de escrita ERP partilhado do PlaidCloud: submete a ação assíncrona de lançamento de diário do serviço personalizado do D365 F&O, consulta periodicamente até um estado terminal e confirma antes de comunicar que um lançamento foi efetuado. Uma correção lança um novo lançamento de estorno, com débito e crédito trocados, em vez de editar o original. Consulte [D365 F&O: Post Journal Entry](/pt-pt/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) para a referência dos campos e [Ligar ao Dynamics 365 Finance & Operations](/pt-pt/guides/connections/dynamics-365-fo/) para o passo a passo completo do lançamento.

## Limitações conhecidas

| Limitação | O que significa |
|---|---|
| O modo de sincronização DMF tem latência de extração | Uma extração `dmf` aguarda uma tarefa de exportação assíncrona — substancialmente mais lenta do que uma extração `odata` do mesmo tamanho. |
| A filtragem por dimensão depende da estrutura | Uma dimensão financeira que não faça parte da estrutura de contas não pode ser filtrada no servidor; delimite-a no seu fluxo de trabalho depois da extração. |
## Relacionado

- [Ligar ao Dynamics 365 Finance & Operations (guia)](/pt-pt/guides/connections/dynamics-365-fo/) — passo a passo: criar a ligação, testá-la, importar uma entidade e lançar um diário.
- [Import D365 F&O Entity](/pt-pt/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/)
- [D365 F&O: Post Journal Entry](/pt-pt/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/)
- [Rever o histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/)
