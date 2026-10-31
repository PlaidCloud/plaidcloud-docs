---
title: Passos do Oracle Fusion
description: Passos de fluxo de trabalho que leem e escrevem no Oracle Fusion Cloud através da ligação Oracle Fusion — importam saldos do razão geral e lotes de lançamentos por OData/BIP ou por extração em massa FBDI, e lançam lançamentos de diário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-fusion/index.md
---

Passos de fluxo de trabalho que leem e escrevem no Oracle Fusion Cloud através da sua [ligação Oracle Fusion](/pt-pt/guides/connections/oracle-fusion/). Dois passos de importação cobrem dimensões de extração diferentes — uma chamada direta OData/BIP para extrações correntes e uma extração em massa assíncrona FBDI/BIP para as de grande dimensão; o passo de lançamento regista lotes de lançamentos através do pipeline de escrita ERP partilhado do PlaidCloud.

## Passos

- [Import Fusion Entity](/pt-pt/reference/workflow-steps/oracle-fusion/import-fusion-entity/) — saldos do razão geral e lotes de lançamentos, com filtros de data, período e intervalo numérico aplicados no servidor.
- [Import Fusion Bulk Extract](/pt-pt/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) — as mesmas entidades, através de uma tarefa de exportação assíncrona FBDI/BIP para extrações de grande dimensão.
- [Oracle Fusion: Post Journal Entry](/pt-pt/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) — lança lotes de lançamentos do razão geral através da interface GL FBDI, com um lançamento de reversão registado para correções.

## Ver também

- [Oracle Fusion Connector](/pt-pt/reference/connectors/erp/oracle-fusion/)
- [Connect to Oracle Fusion](/pt-pt/guides/connections/oracle-fusion/)
- [Review ERP Post History](/pt-pt/guides/connections/erp-post-history/)
