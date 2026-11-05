---
title: Passos de fluxo de trabalho
description: Todos os tipos de passo de fluxo de trabalho do PlaidCloud — importação, exportação, transformações, alocações, dimensões, documentos, notificações e mais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/index.md
---

Os passos de fluxo de trabalho são os blocos de construção da automação do PlaidCloud. Cada passo realiza uma operação (importar um CSV, juntar duas tabelas, enviar uma notificação) e os passos são compostos em fluxos de trabalho que são executados em sequência, em paralelo, condicionalmente ou em ciclos.

## Categorias

### Movimentação de dados

- [Importação](/pt-pt/reference/workflow-steps/import/) — obter dados de CSV, Excel, Parquet, JSON, ORC, Delta Lake, SQL, BigQuery, MongoDB, Kafka, SPSS, origens Singer e mais
- [Exportação](/pt-pt/reference/workflow-steps/export/) — enviar dados para CSV, XML, SQL, Excel, Folhas de cálculo Google, Parquet, ORC, MongoDB, Kafka, arquivo de tabelas e mais

### Transformações de tabelas

- [Tabelas](/pt-pt/reference/workflow-steps/tables/) — junções, uniões, filtros, consultas, pivôs, melts, atualizações direcionadas, concessões de Acesso a linhas a partir de uma tabela de origem, restauro para um ponto no tempo
- [Operações comuns](/pt-pt/reference/workflow-steps/common/) — padrões partilhados de mapeamento e filtragem de dados

### Geoespacial

- [Geoespacial](/pt-pt/reference/workflow-steps/spatial/) — importar e exportar ficheiros espaciais, criar áreas de influência, corresponder, medir, reprojetar e construir geometria; cobertura completa das ferramentas espaciais do Alteryx

### Modelação

- [Alocação](/pt-pt/reference/workflow-steps/allocation/) — distribuição baseada em indutores, alocações divididas, etiquetagem baseada em regras
- [Dimensões](/pt-pt/reference/workflow-steps/dimensions/) — carregar, ordenar, limpar, exportar e gerir hierarquias
- [Otimização](/pt-pt/reference/workflow-steps/optimization/) — passos de solver linear e de programação inteira mista
- [Aprendizagem automática](/pt-pt/reference/workflow-steps/machine-learning/) — treinar modelos, incluindo aprendentes XGBoost e KNIME, e pontuar tabelas com eles

### Documentos e ficheiros

- [Documento](/pt-pt/reference/workflow-steps/document/) — operações com ficheiros, listagem de diretórios, cifragem, manipulação de PDF, processamento de imagem, conversão de codificação, atualizações de células do Excel
- [Texto e documentos](/pt-pt/reference/workflow-steps/text-documents/) — extração de texto de PDF, OCR de imagem, leitura e escrita de blobs, sentimento, modelação de tópicos, nuvens de palavras

### Comunicação

- [Notificações](/pt-pt/reference/workflow-steps/notifications/) — correio eletrónico, Slack, Teams, SMS, webhook, Twitter, registo
- [Relatórios](/pt-pt/reference/workflow-steps/reports/) — gerar relatórios PDF individuais ou em lote a partir de modelos RML

### Controlo de fluxos de trabalho

- [Controlo de fluxos de trabalho](/pt-pt/reference/workflow-steps/workflow-control/) — variáveis, ciclos, subfluxos de trabalho, macros, tratamento de erros, validação da contagem de linhas
- [Geral](/pt-pt/reference/workflow-steps/general/) — passo LLM, pass, aguardar, transformação definida pelo utilizador, executar Python remoto, executor Alteryx
- [Macros empacotadas](/pt-pt/reference/workflow-steps/macros/) — equivalentes das macros empacotadas do Alteryx: Create Samples, DateTime Now, Heat Map, Pie Wedge Trade Area

### Integrações empresariais

- [Agente](/pt-pt/reference/workflow-steps/agent/) — operações do agente PlaidLink para recursos locais
- [NetSuite](/pt-pt/reference/workflow-steps/netsuite/) — importar saldos, detalhe do razão geral, dados mestre ou a sua própria [consulta SuiteQL](/pt-pt/reference/workflow-steps/netsuite/import-suiteql-query/); lançar lançamentos de diário no NetSuite
- [Acumatica](/pt-pt/reference/workflow-steps/acumatica/) — importar entidades mestre e transacionais; lançar transações de diário, faturas, contas a pagar e pagamentos
- [Business Central](/pt-pt/reference/workflow-steps/business-central/) — importar entidades OData; lançar linhas do diário geral
- [Xero](/pt-pt/reference/workflow-steps/xero/) — importar entidades da API de contabilidade; lançar diários manuais, faturas, contas a pagar, pagamentos e notas de crédito
- [Dynamics 365 F&O](/pt-pt/reference/workflow-steps/dynamics-365-fo/) — importar entidades OData/DMF; lançar lançamentos de diário
- [Oracle Fusion](/pt-pt/reference/workflow-steps/oracle-fusion/) — importar saldos do razão geral e lotes de diário; lançar lançamentos de diário através de FBDI
- [Oracle EPM (HFM / FCCS)](/pt-pt/reference/workflow-steps/oracle-epm/) — obter por autoatendimento um segmento de dados ad hoc do Oracle FCCS com um seletor de ponto de vista; carregamento recorrente agendado opcional
- [Oracle Essbase](/pt-pt/reference/workflow-steps/essbase/) — executar uma consulta MDX em direto contra um cubo, ou carregar o esquema de uma dimensão como dimensão do PlaidCloud; direto na cloud
- [IBM TM1 / Planning Analytics](/pt-pt/reference/workflow-steps/ibm-planning-analytics/) — ler um cubo por vista guardada ou MDX, ou uma hierarquia de dimensão; direto na cloud ou através de um agente local
- [Anaplan](/pt-pt/reference/workflow-steps/anaplan/) — ler uma vista guardada, executar uma ação de exportação já existente ou carregar uma ou mais listas para uma dimensão do PlaidCloud; direto na cloud, só de leitura
- [OneStream](/pt-pt/reference/workflow-steps/onestream/) — ler um adaptador de dados, uma chamada por membro de consolidação, para uma tabela; só de leitura
- [Workday Financials](/pt-pt/reference/workflow-steps/workday-financials/) — importar um relatório RaaS; lançar diários contabilísticos
- [Salesforce](/pt-pt/reference/workflow-steps/salesforce/) — extrair qualquer objeto de CRM padrão ou personalizado para uma tabela de projeto através da Bulk API 2.0, com o objeto e a lista de campos lidos da organização
- [Sage Intacct](/pt-pt/reference/workflow-steps/sage-intacct/) — importar saldos, contas a pagar, consultas ad hoc e objetos de razão geral/dimensão; lançar lançamentos de diário
- [SAP S/4HANA Cloud](/pt-pt/reference/workflow-steps/s4hana-cloud/) — importar o balancete e os itens de lançamentos de diário por OData; lançar lançamentos de diário por SOAP
- [SAP](/pt-pt/reference/workflow-steps/sap/) — chamadas RFC do SAP ECC / S/4HANA
- [SAP-PCM](/pt-pt/reference/workflow-steps/sap-pcm/) — controlo de modelos do SAP Profitability and Cost Management
