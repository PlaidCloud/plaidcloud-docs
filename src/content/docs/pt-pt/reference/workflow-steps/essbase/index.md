---
title: Passos Oracle Essbase
description: Passos de fluxo de trabalho que leem de um cubo Oracle Essbase através da sua ligação Essbase — consultas MDX em direto e esboços de dimensões carregados numa dimensão PlaidCloud — diretamente na nuvem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/index.md
---

Passos de fluxo de trabalho que leem do Oracle **Essbase** através da sua [ligação Oracle Essbase](/pt-pt/guides/connections/essbase/): dados de cubos por consulta MDX em direto e um esboço de dimensão carregado numa dimensão PlaidCloud. O Essbase é acedido **diretamente na nuvem** através da respetiva API REST — não existe um caminho por agente local para estes passos.

## Passos

- [Essbase: Consultar cubo](/pt-pt/reference/workflow-steps/essbase/essbase-query/) — executa uma consulta MDX em direto sobre um cubo e coloca a grelha de resultados como uma tabela. Diretamente na nuvem.
- [Essbase: Ler dimensão](/pt-pt/reference/workflow-steps/essbase/essbase-dimension-read/) — carrega o esboço de uma dimensão Essbase numa dimensão PlaidCloud. Diretamente na nuvem.

## Relacionado

- [Ligar ao Oracle Essbase (guia)](/pt-pt/guides/connections/essbase/)
- [Conector Oracle Essbase](/pt-pt/reference/connectors/erp/oracle-essbase/)
