---
title: Passos do Acumatica
description: Passos de fluxo de trabalho que leem do Acumatica e escrevem nele através da sua ligação Acumatica — importam entidades REST baseadas em contrato e lançam lançamentos de diário, faturas, faturas de fornecedor e pagamentos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/acumatica/index.md
---

Passos de fluxo de trabalho que leem do Acumatica e escrevem nele através da sua [ligação Acumatica](/pt-pt/guides/connections/acumatica/). O passo de importação obtém as entidades REST baseadas em contrato do Acumatica sem necessidade de escrever OData; o passo de lançamento lança lançamentos de diário, faturas de venda, faturas de fornecedor e pagamentos através do pipeline partilhado de escrita ERP do PlaidCloud.

## Passos

- [Import Acumatica Entity](/pt-pt/reference/workflow-steps/acumatica/import-acumatica-entity/) — dados mestre e entidades transacionais, com filtros do lado do servidor.
- [Acumatica: Post Documents](/pt-pt/reference/workflow-steps/acumatica/acumatica-post/) — lançar lançamentos de diário, faturas de venda, faturas de fornecedor e pagamentos.

## Relacionado

- [Conector REST do Acumatica](/pt-pt/reference/connectors/rest/acumatica/)
- [Ligar ao Acumatica](/pt-pt/guides/connections/acumatica/)
- [Rever o histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/)
