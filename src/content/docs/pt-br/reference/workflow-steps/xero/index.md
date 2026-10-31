---
title: Etapas do Xero
description: Etapas de fluxo de trabalho que leem do Xero e gravam nele por meio da sua conexão do Xero — importam entidades da API Accounting e lançam lançamentos manuais, faturas, faturas de compra, pagamentos e notas de crédito.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/xero/index.md
---

Etapas de fluxo de trabalho que leem do Xero e gravam nele por meio da sua [conexão do Xero](/pt-br/guides/connections/xero/). A etapa de importação busca as entidades da API Accounting do Xero sem nenhuma consulta para escrever; a etapa de lançamento registra lançamentos manuais, faturas, faturas de compra, pagamentos e notas de crédito por meio do pipeline compartilhado de gravação em ERP do PlaidCloud.

## Etapas

- [Xero: Importar entidade](/pt-br/reference/workflow-steps/xero/import-xero-entity/) — contas, contatos, faturas, notas de crédito, pagamentos, lançamentos manuais, transações bancárias, itens, categorias de rastreamento, alíquotas de imposto e moedas.
- [Xero: Lançar documento](/pt-br/reference/workflow-steps/xero/xero-post/) — lance lançamentos manuais, faturas, faturas de compra, pagamentos e notas de crédito.

## Relacionados

- [Conector REST do Xero](/pt-br/reference/connectors/rest/xero/)
- [Conectar ao Xero](/pt-br/guides/connections/xero/)
- [Revisar o histórico de lançamentos em ERP](/pt-br/guides/connections/erp-post-history/)
