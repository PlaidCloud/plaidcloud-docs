---
title: Etapas de fluxo de trabalho
description: Todos os tipos de etapa de fluxo de trabalho do PlaidCloud — importação, exportação, transformações, alocações, dimensões, documentos, notificações e mais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/index.md
---

As etapas de fluxo de trabalho são os blocos de construção da automação do PlaidCloud. Cada etapa executa uma operação (importar um CSV, juntar duas tabelas, enviar uma notificação), e as etapas são compostas em fluxos de trabalho que são executados em sequência, em paralelo, condicionalmente ou em loops.

## Categorias

### Movimentação de dados

- [Importação](/pt-br/reference/workflow-steps/import/) — traga dados de CSV, Excel, Parquet, JSON, ORC, Delta Lake, SQL, BigQuery, MongoDB, Kafka, SPSS, origens Singer e mais
- [Exportação](/pt-br/reference/workflow-steps/export/) — envie dados para CSV, XML, SQL, Excel, Planilhas Google, Parquet, ORC, MongoDB, Kafka, arquivo compactado de tabelas e mais

### Transformações de tabelas

- [Tabelas](/pt-br/reference/workflow-steps/tables/) — junções, uniões, filtros, consultas, pivôs, melts, atualizações direcionadas, concessões de Acesso a linhas a partir de uma tabela de origem, restauração para um ponto no tempo
- [Operações comuns](/pt-br/reference/workflow-steps/common/) — padrões compartilhados de mapeamento e filtragem de dados

### Geoespacial

- [Geoespacial](/pt-br/reference/workflow-steps/spatial/) — importe e exporte arquivos espaciais, crie buffers, correspondências, medições, reprojeções e construa geometrias; cobertura completa das ferramentas espaciais do Alteryx

### Modelagem

- [Alocação](/pt-br/reference/workflow-steps/allocation/) — distribuição baseada em direcionadores, alocações divididas, marcação baseada em regras
- [Dimensões](/pt-br/reference/workflow-steps/dimensions/) — carregue, ordene, limpe, exporte e gerencie hierarquias
- [Otimização](/pt-br/reference/workflow-steps/optimization/) — etapas de solver linear e de programação inteira mista
- [Aprendizado de máquina](/pt-br/reference/workflow-steps/machine-learning/) — treine modelos, incluindo XGBoost e learners do KNIME, e pontue tabelas com eles

### Documentos e arquivos

- [Documento](/pt-br/reference/workflow-steps/document/) — operações com arquivos, listagem de diretórios, criptografia, manipulação de PDF, processamento de imagens, conversão de codificação, atualizações de células do Excel
- [Texto e documentos](/pt-br/reference/workflow-steps/text-documents/) — extração de texto de PDF, OCR de imagens, leitura e gravação de blobs, sentimento, modelagem de tópicos, nuvens de palavras

### Comunicação

- [Notificações](/pt-br/reference/workflow-steps/notifications/) — e-mail, Slack, Teams, SMS, webhook, Twitter, log
- [Relatórios](/pt-br/reference/workflow-steps/reports/) — gere relatórios PDF únicos ou em lote a partir de modelos RML

### Controle de fluxo de trabalho

- [Controle de fluxo de trabalho](/pt-br/reference/workflow-steps/workflow-control/) — variáveis, loops, subfluxos de trabalho, macros, tratamento de erros, verificação de contagem de linhas
- [Geral](/pt-br/reference/workflow-steps/general/) — etapa de LLM, pass, wait, transformação definida pelo usuário, execução de Python remoto, executor Alteryx
- [Macros empacotadas](/pt-br/reference/workflow-steps/macros/) — equivalentes das macros empacotadas do Alteryx: Create Samples, DateTime Now, Heat Map, Pie Wedge Trade Area

### Integrações corporativas

- [Agente](/pt-br/reference/workflow-steps/agent/) — operações do agente PlaidLink para recursos locais
- [NetSuite](/pt-br/reference/workflow-steps/netsuite/) — importe saldos, detalhes do razão geral, dados mestres ou sua própria [consulta SuiteQL](/pt-br/reference/workflow-steps/netsuite/import-suiteql-query/); lance lançamentos contábeis no NetSuite
- [Acumatica](/pt-br/reference/workflow-steps/acumatica/) — importe entidades mestres e transacionais; lance transações contábeis, faturas, contas a pagar e pagamentos
- [Business Central](/pt-br/reference/workflow-steps/business-central/) — importe entidades OData; lance linhas de diário geral
- [Xero](/pt-br/reference/workflow-steps/xero/) — importe entidades da Accounting API; lance diários manuais, faturas, contas a pagar, pagamentos e notas de crédito
- [Dynamics 365 F&O](/pt-br/reference/workflow-steps/dynamics-365-fo/) — importe entidades OData/DMF; lance lançamentos contábeis
- [Oracle Fusion](/pt-br/reference/workflow-steps/oracle-fusion/) — importe saldos do razão geral e lotes de lançamentos; lance lançamentos contábeis por meio de FBDI
- [Oracle EPM (HFM / FCCS)](/pt-br/reference/workflow-steps/oracle-epm/) — obtenha por conta própria um recorte ad hoc de dados do Oracle FCCS com um seletor de ponto de vista; carga recorrente agendada opcional
- [Oracle Essbase](/pt-br/reference/workflow-steps/essbase/) — execute uma consulta MDX ao vivo em um cubo ou carregue o contorno de uma dimensão como dimensão do PlaidCloud; direto na nuvem
- [IBM TM1 / Planning Analytics](/pt-br/reference/workflow-steps/ibm-planning-analytics/) — leia um cubo por visão salva ou MDX, ou uma hierarquia de dimensão; direto na nuvem ou por um agente local
- [Anaplan](/pt-br/reference/workflow-steps/anaplan/) — leia uma visão salva, execute uma ação de exportação já existente ou carregue uma ou mais listas em uma dimensão do PlaidCloud; direto na nuvem, somente leitura
- [Workday Financials](/pt-br/reference/workflow-steps/workday-financials/) — importe um relatório RaaS; lance diários contábeis
- [Salesforce](/pt-br/reference/workflow-steps/salesforce/) — extraia qualquer objeto de CRM padrão ou personalizado para uma tabela de projeto por meio da Bulk API 2.0, com o objeto e a lista de campos lidos da organização
- [Sage Intacct](/pt-br/reference/workflow-steps/sage-intacct/) — importe saldos, contas a pagar, consultas ad hoc e objetos de razão geral/dimensão; lance lançamentos contábeis
- [SAP S/4HANA Cloud](/pt-br/reference/workflow-steps/s4hana-cloud/) — importe balancete e itens de lançamentos contábeis por OData; lance lançamentos contábeis por SOAP
- [SAP](/pt-br/reference/workflow-steps/sap/) — chamadas RFC do SAP ECC / S/4HANA
- [SAP-PCM](/pt-br/reference/workflow-steps/sap-pcm/) — controle de modelos do SAP Profitability and Cost Management
