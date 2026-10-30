---
title: Conexões
description: Configure e gerencie conexões do PlaidCloud — configurações salvas que permitem aos fluxos de trabalho acessar bancos de dados externos, armazenamento em nuvem, ERPs e APIs REST.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

Uma **conexão** é uma configuração salva que permite ao PlaidCloud acessar um sistema externo — um banco de dados, uma conta de armazenamento em nuvem, um ERP ou uma API REST. As etapas de fluxo de trabalho que precisam ler ou gravar nesse sistema fazem referência à conexão, de modo que as credenciais e os detalhes do endpoint ficam em um só lugar.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="Muitas etapas de fluxo de trabalho fazem referência a uma única conexão salva, que guarda as credenciais e o endpoint em um só lugar e alcança o sistema externo — um banco de dados, armazenamento em nuvem, ERP ou API REST." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">etapas de fluxo de trabalho</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Etapa de importação</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Etapa de exportação</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Etapa de consulta</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Conexão</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">credenciais + endpoint, uma vez</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">sistema externo</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">BD · armazenamento · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Configure a conexão uma vez; toda etapa que lê ou grava no sistema externo aponta para ela, de modo que as credenciais e os detalhes do endpoint não são duplicados entre as etapas.</figcaption>
</figure>

## Guias

- [Criar e gerenciar uma conexão](/pt-br/guides/connections/create-connection/) — crie, edite, teste e controle o acesso a uma conexão, e configure-a por ambiente.
- [Usar seu próprio data warehouse](/pt-br/guides/connections/external-lakehouse/) — conecte você mesmo seu próprio data warehouse Snowflake ou Databricks, entre com a sua própria identidade, gerencie vários data warehouses e veja quanto cada execução custa.
- [Conexão PlaidCloud Git](/pt-br/guides/connections/plaidcloud-git/) — conecte-se ao servidor Git gerenciado do seu próprio espaço de trabalho, sem URL de servidor nem credenciais, e automatize a partir dele as compilações de aplicativos Panel.
- [Clonar uma conexão](/pt-br/guides/connections/clone-connection/) — duplique uma conexão existente para um novo ambiente ou tenant.
- [Data Foundation: o Common Finance Model](/pt-br/guides/projects/data-foundation/) — o Common Finance Model reúne dados de ERP de vários sistemas e instâncias de ERP em um único modelo, com um plano de contas, um conjunto de entidades e uma moeda de relatório, que relatórios, métricas e assistentes de IA leem.
- [Fontes Singer](/pt-br/guides/connections/singer-sources/) — conecte-se a fontes como Stripe, GitHub, Slack e BigQuery com taps do Singer e depois importe os dados delas para tabelas de projeto.
- [Conectar ao NetSuite](/pt-br/guides/connections/netsuite/) — configure uma conexão do NetSuite e extraia dados financeiros e operacionais com SuiteQL.
- [Acesso ao NetSuite para o Data Foundation](/pt-br/guides/connections/netsuite-access-for-data-foundation/) — o que o administrador do seu NetSuite configura para que o Data Foundation possa ler o NetSuite diretamente, e o que enviar de volta.
- [Importar dados financeiros do NetSuite](/pt-br/guides/connections/import-netsuite-financials/) — extraia saldos, detalhes do razão geral e dados mestres com as etapas de importação prontas do NetSuite, sem escrever SuiteQL.
- [Lançar um lançamento contábil no NetSuite](/pt-br/guides/connections/post-netsuite-journal-entries/) — mapeie as tabelas de cabeçalho e de linhas, visualize e lance lançamentos contábeis no NetSuite.
- [Conectar ao Acumatica](/pt-br/guides/connections/acumatica/) — configure uma conexão do Acumatica, importe entidades e lance transações contábeis, faturas, contas a pagar e pagamentos.
- [Conectar ao Business Central](/pt-br/guides/connections/business-central/) — configure uma conexão do Business Central com o Azure AD, importe entidades OData e lance linhas de diário geral.
- [Conectar ao Dynamics 365 Finance & Operations](/pt-br/guides/connections/dynamics-365-fo/) — configure uma conexão do D365 F&O com o Azure AD, importe entidades OData/DMF e lance lançamentos contábeis.
- [Conectar ao Oracle Fusion](/pt-br/guides/connections/oracle-fusion/) — configure uma conexão do Oracle Fusion, importe saldos do razão geral e lotes de lançamentos e lance diários por meio do FBDI.
- [Conectar ao Workday Financials](/pt-br/guides/connections/workday-financials/) — configure uma conexão do Workday Financials com um Usuário do sistema de integração, importe um relatório RaaS e lance lançamentos contábeis.
- [Conectar ao SAP S/4HANA Cloud](/pt-br/guides/connections/s4hana-cloud/) — configure uma conexão direta com o S/4HANA Cloud usando OAuth2, importe o balancete e os itens de lançamentos contábeis e lance lançamentos contábeis via SOAP.
- [Extrações ad hoc do SAP ECC / S/4HANA](/pt-br/guides/connections/sap-adhoc-extract/) — pesquise no SAP por tabela, código de transação ou SAP Query salva, visualize e planeje a extração e carregue-a em uma tabela por meio de um agente PlaidLink.
- [Conectar ao Sage Intacct](/pt-br/guides/connections/sage-intacct/) — configure uma conexão do Sage Intacct e extraia dados financeiros e contábeis.
- [Conectar ao Xero](/pt-br/guides/connections/xero/) — autorize uma organização do Xero com um clique, importe entidades da Accounting API e lance diários manuais, faturas, contas a pagar, pagamentos e notas de crédito.
- [Conectar ao Salesforce](/pt-br/guides/connections/salesforce/) — configure um External Client App do Salesforce e um usuário Run As, e depois extraia objetos de CRM para tabelas de projeto.
- [Extrair do HFM / FCCS (ad hoc)](/pt-br/guides/connections/hfm-fccs/) — conecte-se ao Oracle FCCS e obtenha por conta própria uma fatia de dados com um seletor de ponto de vista, sem abrir chamado para a equipe do HFM.
- [Conectar ao TM1](/pt-br/guides/connections/tm1/) — conecte-se a um servidor IBM TM1 / Planning Analytics e leia dados de cubo por visão ou MDX, fatiados por período.
- [Conectar ao Anaplan](/pt-br/guides/connections/anaplan/) — conecte-se ao Anaplan e leia uma visão salva, execute uma ação de exportação preexistente ou carregue listas em uma dimensão do PlaidCloud. Somente leitura.
- [Conectar ao QuickBooks](/pt-br/guides/connections/quickbooks/) — pré-requisitos e limitações atuais do QuickBooks Online.
- [Revisar o Registro de lançamentos](/pt-br/guides/connections/posting-register/) — um console em nível de tenant para que finanças e contabilidade revisem os lançamentos de ERP em todos os projetos e conexões que podem ver.

## Relacionados

- [Referência de conectores](/pt-br/reference/connectors/) — o catálogo completo de sistemas compatíveis e os campos de que cada um precisa.
