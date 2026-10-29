---
title: Passos de fluxo de trabalho
description: Todos os tipos de passo de fluxo de trabalho do PlaidCloud — importação, exportação, transformações, alocações, dimensões, documentos, notificações e mais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/index.md
---

Os passos de fluxo de trabalho são os blocos de construção da automatização do PlaidCloud. Cada passo executa uma operação (importar um CSV, juntar duas tabelas, enviar uma notificação) e os passos são compostos em fluxos de trabalho que são executados em sequência, em paralelo, condicionalmente ou em ciclos.

## Categorias

### Movimentação de dados

- [Importação](/pt-pt/reference/workflow-steps/import/) — traga dados de CSV, Excel, Parquet, JSON, ORC, Delta Lake, SQL, BigQuery, MongoDB, Kafka, SPSS, origens Singer e mais
- [Exportação](/pt-pt/reference/workflow-steps/export/) — envie dados para CSV, XML, SQL, Excel, Google Sheets, Parquet, ORC, MongoDB, Kafka, arquivo de tabelas e mais

### Transformações de tabelas

- [Tabelas](/pt-pt/reference/workflow-steps/tables/) — junções, uniões, filtros, pesquisas, pivôs, melts, atualizações dirigidas, concessões de Acesso a linhas a partir de uma tabela de origem, restauro para um ponto no tempo
- [Operações comuns](/pt-pt/reference/workflow-steps/common/) — padrões partilhados de mapeamento e filtragem de dados

### Geoespacial

- [Geoespacial](/pt-pt/reference/workflow-steps/spatial/) — importe e exporte ficheiros espaciais, crie zonas de influência, faça correspondências, meça, reprojete e construa geometria; cobertura completa das ferramentas espaciais do Alteryx

### Modelação

- [Alocação](/pt-pt/reference/workflow-steps/allocation/) — distribuição baseada em indutores, alocações divididas, etiquetagem baseada em regras
- [Dimensões](/pt-pt/reference/workflow-steps/dimensions/) — carregue, ordene, limpe, exporte e gira hierarquias
- [Otimização](/pt-pt/reference/workflow-steps/optimization/) — passos de solver linear e de inteiros mistos
- [Aprendizagem automática](/pt-pt/reference/workflow-steps/machine-learning/) — treine modelos, incluindo XGBoost e learners KNIME, e pontue tabelas com eles

### Documentos e ficheiros

- [Documento](/pt-pt/reference/workflow-steps/document/) — operações com ficheiros, listagem de diretórios, encriptação, manipulação de PDF, processamento de imagens, conversão de codificação, atualizações de células Excel
- [Texto e documentos](/pt-pt/reference/workflow-steps/text-documents/) — extração de texto de PDF, OCR de imagens, leitura e escrita de blobs, sentimento, modelação de tópicos, nuvens de palavras

### Comunicação

- [Notificações](/pt-pt/reference/workflow-steps/notifications/) — email, Slack, Teams, SMS, webhook, Twitter, registo
- [Relatórios](/pt-pt/reference/workflow-steps/reports/) — produza relatórios PDF individuais ou em lote a partir de modelos RML

### Controlo do fluxo de trabalho

- [Controlo do fluxo de trabalho](/pt-pt/reference/workflow-steps/workflow-control/) — variáveis, ciclos, subfluxos de trabalho, macros, tratamento de erros, validação da contagem de linhas
- [Geral](/pt-pt/reference/workflow-steps/general/) — passo LLM, pass, aguardar, transformação definida pelo utilizador, execução remota de Python, executor Alteryx
- [Macros empacotadas](/pt-pt/reference/workflow-steps/macros/) — equivalentes das macros empacotadas do Alteryx: Create Samples, DateTime Now, Heat Map, Pie Wedge Trade Area

### Integrações empresariais

- [Agente](/pt-pt/reference/workflow-steps/agent/) — operações do agente PlaidLink para recursos locais
- [NetSuite](/pt-pt/reference/workflow-steps/netsuite/) — importe saldos, detalhe do razão geral, dados mestre ou a sua própria [consulta SuiteQL](/pt-pt/reference/workflow-steps/netsuite/import-suiteql-query/); lance lançamentos de diário no NetSuite
- [Acumatica](/pt-pt/reference/workflow-steps/acumatica/) — importe entidades mestre e transacionais; lance transações de diário, faturas, contas a pagar e pagamentos
- [Business Central](/pt-pt/reference/workflow-steps/business-central/) — importe entidades OData; lance linhas de diário geral
- [Xero](/pt-pt/reference/workflow-steps/xero/) — importe entidades da API Accounting; lance diários manuais, faturas, contas a pagar, pagamentos e notas de crédito
- [Dynamics 365 F&O](/pt-pt/reference/workflow-steps/dynamics-365-fo/) — importe entidades OData/DMF; lance lançamentos de diário
- [Oracle Fusion](/pt-pt/reference/workflow-steps/oracle-fusion/) — importe saldos do razão geral e lotes de diário; lance lançamentos de diário através de FBDI
- [Oracle EPM (HFM / FCCS)](/pt-pt/reference/workflow-steps/oracle-epm/) — obtenha por autosserviço um corte ad hoc de dados do Oracle FCCS com um seletor de ponto de vista; carregamento recorrente agendado opcional
- [Oracle Essbase](/pt-pt/reference/workflow-steps/essbase/) — execute uma consulta MDX em direto a um cubo ou carregue o esquema de uma dimensão como uma dimensão do PlaidCloud; diretamente na cloud
- [IBM TM1 / Planning Analytics](/pt-pt/reference/workflow-steps/ibm-planning-analytics/) — leia um cubo por vista guardada ou MDX, ou uma hierarquia de dimensão; diretamente na cloud ou através de um agente local
- [Anaplan](/pt-pt/reference/workflow-steps/anaplan/) — leia uma vista guardada, execute uma ação de exportação pré-existente ou carregue uma ou mais listas numa dimensão do PlaidCloud; diretamente na cloud, só de leitura
- [Workday Financials](/pt-pt/reference/workflow-steps/workday-financials/) — importe um relatório RaaS; lance diários contabilísticos
- [Salesforce](/pt-pt/reference/workflow-steps/salesforce/) — extraia qualquer objeto CRM padrão ou personalizado para uma tabela de projeto através da Bulk API 2.0, com o objeto e a lista de campos lidos a partir da organização
- [Sage Intacct](/pt-pt/reference/workflow-steps/sage-intacct/) — importe saldos, contas a pagar, consultas ad hoc e objetos de razão geral/dimensão; lance lançamentos de diário
- [SAP S/4HANA Cloud](/pt-pt/reference/workflow-steps/s4hana-cloud/) — importe o balancete e os itens de lançamentos de diário através de OData; lance lançamentos de diário através de SOAP
- [SAP](/pt-pt/reference/workflow-steps/sap/) — chamadas RFC do SAP ECC / S/4HANA
- [SAP-PCM](/pt-pt/reference/workflow-steps/sap-pcm/) — controlo de modelos do SAP Profitability and Cost Management
