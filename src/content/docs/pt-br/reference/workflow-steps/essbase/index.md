---
title: Etapas do Oracle Essbase
description: Etapas de fluxo de trabalho que leem de um cubo do Oracle Essbase por meio da sua conexão do Essbase (consultas MDX ao vivo e esboços de dimensão carregados em uma dimensão do PlaidCloud), diretamente na nuvem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/index.md
---

Etapas de fluxo de trabalho que leem do Oracle **Essbase** por meio da sua [conexão do Oracle Essbase](/pt-br/guides/connections/essbase/): dados de cubo por consulta MDX ao vivo e o esboço de uma dimensão carregado em uma dimensão do PlaidCloud. O Essbase é acessado **diretamente na nuvem** por sua API REST: não há caminho por agente local para estas etapas.

## Etapas

- [Essbase: Consultar cubo](/pt-br/reference/workflow-steps/essbase/essbase-query/) — executa uma consulta MDX ao vivo em um cubo e grava a grade de resultado como tabela. Diretamente na nuvem.
- [Essbase: Ler dimensão](/pt-br/reference/workflow-steps/essbase/essbase-dimension-read/) — carrega o esboço de uma dimensão do Essbase em uma dimensão do PlaidCloud. Diretamente na nuvem.

## Relacionados

- [Conectar-se ao Oracle Essbase (guia)](/pt-br/guides/connections/essbase/)
- [Conector do Oracle Essbase](/pt-br/reference/connectors/erp/oracle-essbase/)
