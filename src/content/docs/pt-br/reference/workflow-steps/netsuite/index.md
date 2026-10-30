---
title: Etapas do NetSuite
description: "Etapas de fluxo de trabalho do NetSuite: importe saldos, detalhes do razão geral, dados mestres ou sua própria consulta SuiteQL e lance lançamentos contábeis pela sua conexão do NetSuite."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/netsuite/index.md
---

Etapas de fluxo de trabalho que leem e gravam no NetSuite por meio da sua [conexão do NetSuite](/pt-br/guides/connections/netsuite/). As etapas de importação prontas são a maneira mais simples de extrair os dados financeiros e de referência mais comuns: escolha uma conexão, uma tabela de destino e um intervalo de datas ou tipo de registro, sem SuiteQL para escrever.

## Etapas de importação

- [NetSuite: Importar saldos](/pt-br/reference/workflow-steps/netsuite/import-balances/): saldos de contas (um balancete) para um intervalo de datas e uma subsidiária.
- [NetSuite: Importar detalhes do razão geral](/pt-br/reference/workflow-steps/netsuite/import-gl-detail/): detalhe das linhas de transação do razão geral para um intervalo de datas e uma subsidiária.
- [NetSuite: Importar dados mestres](/pt-br/reference/workflow-steps/netsuite/import-master-data/): listas mestras: contas, subsidiárias, departamentos, classes, locais, fornecedores ou clientes.
- [NetSuite: Importar consulta SuiteQL](/pt-br/reference/workflow-steps/netsuite/import-suiteql-query/): execute sua própria consulta SuiteQL e carregue o resultado em uma tabela tipada, com janelas de datas e paginação tratadas para você.

## Etapas de lançamento

- [Post NetSuite Journal Entry](/pt-br/reference/workflow-steps/netsuite/post-netsuite-journal-entry/): lance de volta no NetSuite lançamentos contábeis com cabeçalho e linhas.

## Extrações personalizadas

Para dados que as etapas de importação prontas não cobrem, como uma consulta sob medida ou um registro do NetSuite sem etapa pronta, use [NetSuite: Importar consulta SuiteQL](/pt-br/reference/workflow-steps/netsuite/import-suiteql-query/) com seu próprio SuiteQL. Consulte [Exemplos de consultas SuiteQL do NetSuite](/pt-br/guides/connections/netsuite-financial-queries/) para ver pontos de partida.

## Relacionados

- [Conector REST do NetSuite](/pt-br/reference/connectors/rest/netsuite/)
- [Conectar ao NetSuite](/pt-br/guides/connections/netsuite/)
- [Importar dados financeiros do NetSuite](/pt-br/guides/connections/import-netsuite-financials/)
