---
title: Conector REST do SAP S/4HANA Cloud
description: Configure uma conexão com o SAP S/4HANA Cloud Public Edition no PlaidCloud para importar dados de balancete e de itens de lançamento contábil por OData e lançar lançamentos contábeis por SOAP.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/s4hana-cloud.md
---

## Documentação da API

A [Trial Balance API (`API_OPLACCTGDOCITEMCUBE_SRV`)](https://api.sap.com/) e a [Journal Entry Item - Basic API (`API_JOURNALENTRYITEMBASIC_SRV`)](https://api.sap.com/) do SAP S/4HANA Cloud, no SAP API Business Hub, documentam os endpoints OData usados por este conector, além do serviço SOAP de criação em massa de lançamentos contábeis, exposto por meio de um Communication Arrangement.

## Como funciona a autenticação

A conexão se autentica como um aplicativo usando **credenciais de cliente OAuth2**: o ID do cliente e o segredo de um Communication Arrangement são trocados por um token de acesso no endpoint de token OAuth2 do tenant. Não há login interativo.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| Host | Texto | O host do seu tenant do S/4HANA Cloud, por exemplo `https://yourorg.s4hana.ondemand.com`. |
| URL do token | Texto | O endpoint de token OAuth2 do Communication Arrangement. |
| ID do cliente | Texto | O ID do cliente OAuth2 do Communication Arrangement. |
| Segredo do cliente | Texto | O segredo do cliente OAuth2 do Communication Arrangement. Armazenado de forma criptografada. |

## Entidades disponíveis para importação

A etapa **Import S/4HANA Entity** cobre duas entidades: `trial_balance` (saldos agregados das contas do razão geral no fim do período, por `API_OPLACCTGDOCITEMCUBE_SRV`) e `journal_entry_items` (itens de linha de lançamentos contábeis lançados, por `API_JOURNALENTRYITEMBASIC_SRV`). Ambas oferecem filtros do lado do servidor em `CompanyCode`, `GLAccount`, `CostCenter`, `ProfitCenter`, `FiscalYear`, `FiscalPeriod` e `Ledger`, com `PostingDate`, `FiscalYear` e `FiscalPeriod` aceitando limites de intervalo `ge`/`le`. Consulte a etapa [Import S/4HANA Entity](/pt-br/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) para a referência completa dos campos.

## Lançamento de lançamentos contábeis

A etapa **S/4HANA: Post Journal Entry** lança lançamentos contábeis do razão geral pelo pipeline de gravação de ERP compartilhado do PlaidCloud: envia pelo serviço SOAP `JournalEntryBulkCreateRequest_In` do S/4HANA Cloud, consulta a confirmação `JournalEntryBulkCreateConfirmation_Out` e confirma antes de informar que um lançamento foi efetuado. Uma correção lança um novo lançamento de estorno, com débito e crédito invertidos, em vez de editar o original. Consulte a etapa [S/4HANA: Post Journal Entry](/pt-br/reference/workflow-steps/s4hana-cloud/s4hana-post/) para a referência dos campos e [Conectar ao SAP S/4HANA Cloud](/pt-br/guides/connections/s4hana-cloud/) para o passo a passo completo de lançamento.

## Limitações conhecidas

| Limitação | O que significa |
|---|---|
| Latência de confirmação | O serviço SOAP de criação em massa processa as solicitações de forma assíncrona, o que é bem mais lento do que uma gravação OData síncrona do mesmo tamanho. |
| Os campos filtráveis dependem do seu Communication Scenario | Um objeto de custo ou uma dimensão que o seu Communication Scenario não expõe não pode ser filtrado no servidor; delimite-o no seu fluxo de trabalho depois da extração. |
## Relacionados

- [Conectar ao SAP S/4HANA Cloud (guia)](/pt-br/guides/connections/s4hana-cloud/) — passo a passo: criar a conexão, testá-la, importar uma entidade e lançar um diário.
- [Import S/4HANA Entity](/pt-br/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/)
- [S/4HANA: Post Journal Entry](/pt-br/reference/workflow-steps/s4hana-cloud/s4hana-post/)
- [Revisar o histórico de lançamentos de ERP](/pt-br/guides/connections/erp-post-history/)
- [Conector SAP ECC / S/4HANA](/pt-br/reference/connectors/erp/sap-s4/) — o conector separado, baseado em RFC/agente, para S/4HANA local ou em nuvem privada.
