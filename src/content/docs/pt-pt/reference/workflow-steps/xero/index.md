---
title: Passos Xero
description: Passos de fluxo de trabalho que leem e escrevem no Xero através da sua ligação Xero — importam entidades da API Accounting e lançam lançamentos manuais de diário, faturas, faturas de fornecedor, pagamentos e notas de crédito.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/xero/index.md
---

Passos de fluxo de trabalho que leem e escrevem no Xero através da sua [ligação Xero](/pt-pt/guides/connections/xero/). O passo de importação obtém as entidades da API Accounting do Xero sem necessidade de escrever uma consulta; o passo de lançamento lança lançamentos manuais de diário, faturas, faturas de fornecedor, pagamentos e notas de crédito através do pipeline partilhado de escrita ERP do PlaidCloud.

## Passos

- [Xero: Importar entidade](/pt-pt/reference/workflow-steps/xero/import-xero-entity/) — contas, contactos, faturas, notas de crédito, pagamentos, lançamentos manuais de diário, transações bancárias, artigos, categorias de acompanhamento, taxas de imposto e moedas.
- [Xero: Lançar documento](/pt-pt/reference/workflow-steps/xero/xero-post/) — lance lançamentos manuais de diário, faturas, faturas de fornecedor, pagamentos e notas de crédito.

## Ver também

- [Conector REST do Xero](/pt-pt/reference/connectors/rest/xero/)
- [Ligar ao Xero](/pt-pt/guides/connections/xero/)
- [Consultar o histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/)
