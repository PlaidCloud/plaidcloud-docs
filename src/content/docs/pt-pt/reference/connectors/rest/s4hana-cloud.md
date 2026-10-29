---
title: Conector REST SAP S/4HANA Cloud
description: Configure uma ligação ao SAP S/4HANA Cloud Public Edition no PlaidCloud para importar dados de balancete e de itens de lançamentos de diário através de OData e lançar lançamentos de diário através de SOAP.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/s4hana-cloud.md
---

## Documentação da API

A [Trial Balance API (`API_OPLACCTGDOCITEMCUBE_SRV`)](https://api.sap.com/) e a [Journal Entry Item - Basic API (`API_JOURNALENTRYITEMBASIC_SRV`)](https://api.sap.com/) do SAP S/4HANA Cloud, no SAP API Business Hub, documentam os pontos de acesso OData que este conector utiliza, a par do serviço SOAP de criação em massa de lançamentos de diário exposto através de um Communication Arrangement.

## Como funciona a autenticação

A ligação autentica-se como uma aplicação através de **credenciais de cliente OAuth2** — o ID de cliente e o segredo de um Communication Arrangement são trocados por um token de acesso no ponto de acesso de tokens OAuth2 do inquilino. Não existe início de sessão interativo.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de apresentação desta ligação. |
| Anfitrião | Texto | O anfitrião do seu inquilino S/4HANA Cloud, por exemplo `https://yourorg.s4hana.ondemand.com`. |
| URL do token | Texto | O ponto de acesso de tokens OAuth2 do Communication Arrangement. |
| ID do cliente | Texto | O ID de cliente OAuth2 do Communication Arrangement. |
| Segredo do cliente | Texto | O segredo de cliente OAuth2 do Communication Arrangement. Guardado cifrado. |

## Entidades disponíveis para importação

O passo **Import S/4HANA Entity** abrange duas entidades: `trial_balance` (saldos agregados das contas do razão geral no fim do período, através de `API_OPLACCTGDOCITEMCUBE_SRV`) e `journal_entry_items` (linhas de lançamentos de diário registados, através de `API_JOURNALENTRYITEMBASIC_SRV`). Ambas suportam filtros do lado do servidor em `CompanyCode`, `GLAccount`, `CostCenter`, `ProfitCenter`, `FiscalYear`, `FiscalPeriod` e `Ledger`, sendo que `PostingDate`, `FiscalYear` e `FiscalPeriod` aceitam limites de intervalo `ge`/`le`. Consulte [Import S/4HANA Entity](/pt-pt/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) para a referência completa dos campos.

## Lançamento de lançamentos de diário

O passo **S/4HANA: Post Journal Entry** lança lançamentos de diário do razão geral através do pipeline de escrita ERP partilhado do PlaidCloud: submete através do serviço SOAP `JournalEntryBulkCreateRequest_In` do S/4HANA Cloud, aguarda a confirmação `JournalEntryBulkCreateConfirmation_Out` e confirma antes de comunicar que um lançamento foi efetuado. Uma correção lança um novo lançamento de estorno, com débito e crédito trocados, em vez de editar o original. Consulte [S/4HANA: Post Journal Entry](/pt-pt/reference/workflow-steps/s4hana-cloud/s4hana-post/) para a referência dos campos e [Ligar ao SAP S/4HANA Cloud](/pt-pt/guides/connections/s4hana-cloud/) para o passo a passo completo do lançamento.

## Limitações conhecidas

| Limitação | O que significa |
|---|---|
| Latência de confirmação | O serviço SOAP de criação em massa processa os pedidos de forma assíncrona — substancialmente mais lento do que uma escrita OData síncrona do mesmo tamanho. |
| Os campos filtráveis dependem do seu Communication Scenario | Um objeto de custo ou dimensão que não seja exposto pelo seu Communication Scenario não pode ser filtrado no servidor; delimite-o no seu fluxo de trabalho depois da extração. |
## Relacionado

- [Ligar ao SAP S/4HANA Cloud (guia)](/pt-pt/guides/connections/s4hana-cloud/) — passo a passo: criar a ligação, testá-la, importar uma entidade e lançar um diário.
- [Import S/4HANA Entity](/pt-pt/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/)
- [S/4HANA: Post Journal Entry](/pt-pt/reference/workflow-steps/s4hana-cloud/s4hana-post/)
- [Rever o histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/)
- [Conector SAP ECC / S/4HANA](/pt-pt/reference/connectors/erp/sap-s4/) — o conector separado, baseado em RFC/agente, para S/4HANA nas instalações ou em nuvem privada.
