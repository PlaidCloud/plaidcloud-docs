---
title: Etapas do Acumatica
description: Etapas de fluxo de trabalho que leem e gravam no Acumatica pela sua conexão do Acumatica — importam entidades REST baseadas em contrato e lançam transações de diário, faturas, faturas de fornecedor e pagamentos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/acumatica/index.md
---

Etapas de fluxo de trabalho que leem e gravam no Acumatica pela sua [Conexão do Acumatica](/pt-br/guides/connections/acumatica/). A etapa de importação busca as entidades REST baseadas em contrato do Acumatica sem precisar escrever OData; a etapa de lançamento lança transações de diário, faturas de venda, faturas de fornecedor e pagamentos por meio do pipeline compartilhado de gravação em ERP do PlaidCloud.

## Etapas

- [Etapa Import Acumatica Entity](/pt-br/reference/workflow-steps/acumatica/import-acumatica-entity/) — dados mestres e entidades transacionais, com filtros do lado do servidor.
- [Etapa Acumatica: Post Documents](/pt-br/reference/workflow-steps/acumatica/acumatica-post/) — lança transações de diário, faturas de venda, faturas de fornecedor e pagamentos.

## Relacionados

- [Conector REST do Acumatica](/pt-br/reference/connectors/rest/acumatica/)
- [Conectar ao Acumatica](/pt-br/guides/connections/acumatica/)
- [Revisar o histórico de lançamentos em ERP](/pt-br/guides/connections/erp-post-history/)
