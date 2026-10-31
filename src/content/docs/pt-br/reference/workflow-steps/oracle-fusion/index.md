---
title: Etapas do Oracle Fusion
description: Etapas de fluxo de trabalho que leem e gravam no Oracle Fusion Cloud por meio da sua conexão do Oracle Fusion — importam saldos do razão geral e lotes de lançamentos via OData/BIP ou extração em massa FBDI e lançam lançamentos contábeis.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-fusion/index.md
---

Etapas de fluxo de trabalho que leem e gravam no Oracle Fusion Cloud por meio da sua [conexão do Oracle Fusion](/pt-br/guides/connections/oracle-fusion/). Duas etapas de importação cobrem tamanhos de carga diferentes — uma chamada direta OData/BIP para cargas rotineiras e uma extração em massa assíncrona FBDI/BIP para cargas grandes; a etapa de lançamento envia lotes de lançamentos pelo pipeline de gravação ERP compartilhado do PlaidCloud.

## Etapas

- [Import Fusion Entity](/pt-br/reference/workflow-steps/oracle-fusion/import-fusion-entity/) — saldos do razão geral e lotes de lançamentos, com filtros de data, período e intervalo numérico no servidor.
- [Import Fusion Bulk Extract](/pt-br/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) — as mesmas entidades, por meio de um job de exportação assíncrono FBDI/BIP para cargas grandes.
- [Oracle Fusion: Post Journal Entry](/pt-br/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) — lança lotes de lançamentos do razão geral pela interface GL FBDI, com um lançamento de estorno lançado para correções.

## Relacionados

- [Conector do Oracle Fusion](/pt-br/reference/connectors/erp/oracle-fusion/)
- [Conectar ao Oracle Fusion](/pt-br/guides/connections/oracle-fusion/)
- [Revisar o histórico de lançamentos do ERP](/pt-br/guides/connections/erp-post-history/)
