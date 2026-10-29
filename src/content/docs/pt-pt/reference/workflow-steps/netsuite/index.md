---
title: Passos do NetSuite
description: Passos de fluxo de trabalho do NetSuite — importe saldos, detalhe do razão geral, dados mestre ou a sua própria consulta SuiteQL, e lance lançamentos de diário através da sua ligação ao NetSuite.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/netsuite/index.md
---

Passos de fluxo de trabalho que leem do NetSuite e escrevem no NetSuite através da sua [ligação ao NetSuite](/pt-pt/guides/connections/netsuite/). Os passos de importação predefinidos são a forma mais simples de obter os dados financeiros e de referência mais comuns: escolha uma ligação, uma tabela de destino e um intervalo de datas ou tipo de registo, sem SuiteQL para escrever.

## Passos de importação

- [NetSuite: Importar saldos](/pt-pt/reference/workflow-steps/netsuite/import-balances/): saldos de contas (um balancete) para um intervalo de datas e uma subsidiária.
- [NetSuite: Importar detalhe do razão geral](/pt-pt/reference/workflow-steps/netsuite/import-gl-detail/): detalhe das linhas de transação do razão geral para um intervalo de datas e uma subsidiária.
- [NetSuite: Importar dados mestre](/pt-pt/reference/workflow-steps/netsuite/import-master-data/): listas mestre: contas, subsidiárias, departamentos, classes, localizações, fornecedores ou clientes.
- [NetSuite: Importar consulta SuiteQL](/pt-pt/reference/workflow-steps/netsuite/import-suiteql-query/): execute a sua própria consulta SuiteQL e carregue o resultado numa tabela com tipos, com janelas de datas e paginação tratadas por si.

## Passos de lançamento

- [Post NetSuite Journal Entry](/pt-pt/reference/workflow-steps/netsuite/post-netsuite-journal-entry/): lance lançamentos de diário de cabeçalho/linhas no NetSuite.

## Importações personalizadas

Para dados que os passos de importação predefinidos não cobrem — uma consulta à medida ou um registo do NetSuite sem passo predefinido — utilize [NetSuite: Importar consulta SuiteQL](/pt-pt/reference/workflow-steps/netsuite/import-suiteql-query/) com o seu próprio SuiteQL. Consulte [Exemplos de consultas SuiteQL do NetSuite](/pt-pt/guides/connections/netsuite-financial-queries/) para pontos de partida.

## Relacionado

- [Conector REST do NetSuite](/pt-pt/reference/connectors/rest/netsuite/)
- [Ligar ao NetSuite](/pt-pt/guides/connections/netsuite/)
- [Importar dados financeiros do NetSuite](/pt-pt/guides/connections/import-netsuite-financials/)
