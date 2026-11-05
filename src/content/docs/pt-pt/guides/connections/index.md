---
title: Ligações
description: Configure e gira ligações do PlaidCloud — configurações guardadas que permitem aos fluxos de trabalho aceder a bases de dados externas, armazenamento na cloud, ERP e APIs REST.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

Uma **ligação** é uma configuração guardada que permite ao PlaidCloud aceder a um sistema externo — uma base de dados, uma conta de armazenamento na cloud, um ERP ou uma API REST. Os passos de fluxo de trabalho que precisam de ler ou escrever nesse sistema referenciam a ligação, pelo que as credenciais e os detalhes do ponto de acesso ficam num único local.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="Muitos passos de fluxo de trabalho referenciam uma única ligação guardada, que contém as credenciais e o ponto de acesso num único local e chega ao sistema externo — uma base de dados, armazenamento na cloud, ERP ou API REST." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">passos de fluxo de trabalho</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Passo de importação</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Passo de exportação</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Passo de consulta</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Ligação</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">credenciais + ponto de acesso, uma vez</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">sistema externo</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">BD · armazenamento · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Configure a ligação uma só vez; todos os passos que leem ou escrevem no sistema externo apontam para ela, pelo que as credenciais e os detalhes do ponto de acesso não são duplicados entre passos.</figcaption>
</figure>

## Guias

- [Criar e gerir uma ligação](/pt-pt/guides/connections/create-connection/) — criar, editar, testar e controlar o acesso a uma ligação, e configurá-la por ambiente.
- [Utilizar o seu próprio armazém](/pt-pt/guides/connections/external-lakehouse/) — ligar por si o seu próprio armazém Snowflake ou Databricks, iniciar sessão com a sua própria identidade, gerir vários armazéns e ver o custo de cada execução.
- [Ligação PlaidCloud Git](/pt-pt/guides/connections/plaidcloud-git/) — ligar ao servidor Git gerido da sua área de trabalho sem URL de servidor nem credenciais, e automatizar a partir dele as compilações de aplicações Panel.
- [Clonar uma ligação](/pt-pt/guides/connections/clone-connection/) — duplicar uma ligação existente para um novo ambiente ou tenant.
- [Data Foundation: o Common Finance Model](/pt-pt/guides/projects/data-foundation/) — o Common Finance Model reúne dados de ERP de vários sistemas e instâncias ERP num único modelo, com um só plano de contas, um só conjunto de entidades e uma só moeda de relato, que os relatórios, os indicadores e os assistentes de IA leem.
- [Origens Singer](/pt-pt/guides/connections/singer-sources/) — ligar a origens como Stripe, GitHub, Slack e BigQuery com taps Singer e importar os respetivos dados para tabelas de projeto.
- [Ligar ao NetSuite](/pt-pt/guides/connections/netsuite/) — configurar uma ligação ao NetSuite e obter dados financeiros e operacionais com SuiteQL.
- [Acesso ao NetSuite para o Data Foundation](/pt-pt/guides/connections/netsuite-access-for-data-foundation/) — o que o administrador do NetSuite configura para que o Data Foundation possa ler o NetSuite diretamente, e o que enviar de volta.
- [Importar dados financeiros do NetSuite](/pt-pt/guides/connections/import-netsuite-financials/) — obter saldos, detalhe do razão geral e dados mestre com os passos de importação do NetSuite predefinidos, sem SuiteQL para escrever.
- [Lançar um lançamento de diário no NetSuite](/pt-pt/guides/connections/post-netsuite-journal-entries/) — mapear tabelas de cabeçalho e de linhas, pré-visualizar e lançar lançamentos de diário no NetSuite.
- [Ligar ao Acumatica](/pt-pt/guides/connections/acumatica/) — configurar uma ligação ao Acumatica, importar entidades e lançar transações de diário, faturas, contas a pagar e pagamentos.
- [Ligar ao Business Central](/pt-pt/guides/connections/business-central/) — configurar uma ligação ao Business Central com Azure AD, importar entidades OData e lançar linhas do diário geral.
- [Ligar ao Dynamics 365 Finance & Operations](/pt-pt/guides/connections/dynamics-365-fo/) — configurar uma ligação ao D365 F&O com Azure AD, importar entidades OData/DMF e lançar lançamentos de diário.
- [Ligar ao Oracle Fusion](/pt-pt/guides/connections/oracle-fusion/) — configurar uma ligação ao Oracle Fusion, importar saldos do razão geral e lotes de diário, e lançar diários através de FBDI.
- [Ligar ao Workday Financials](/pt-pt/guides/connections/workday-financials/) — configurar uma ligação ao Workday Financials com um Utilizador do sistema de integração, importar um relatório RaaS e lançar lançamentos de diário.
- [Ligar ao SAP S/4HANA Cloud](/pt-pt/guides/connections/s4hana-cloud/) — configurar uma ligação direta ao S/4HANA Cloud com OAuth2, importar o balancete e os itens de lançamentos de diário, e lançar lançamentos de diário por SOAP.
- [Extrações ad hoc do SAP ECC / S/4HANA](/pt-pt/guides/connections/sap-adhoc-extract/) — pesquisar no SAP por tabela, código de transação ou SAP Query guardada, pré-visualizar e planear a extração e carregá-la numa tabela através de um agente PlaidLink.
- [Ligar ao Sage Intacct](/pt-pt/guides/connections/sage-intacct/) — configurar uma ligação ao Sage Intacct e obter dados financeiros e contabilísticos.
- [Ligar ao Xero](/pt-pt/guides/connections/xero/) — autorizar uma organização Xero com um clique, importar entidades da API de contabilidade e lançar lançamentos manuais, faturas, contas a pagar, pagamentos e notas de crédito.
- [Ligar ao Salesforce](/pt-pt/guides/connections/salesforce/) — configurar uma External Client App e um utilizador Run As do Salesforce, e depois extrair objetos de CRM para tabelas de projeto.
- [Extrair do HFM / FCCS (ad hoc)](/pt-pt/guides/connections/hfm-fccs/) — ligar ao Oracle FCCS e obter por autoatendimento um segmento de dados com um seletor de ponto de vista, sem pedido à equipa do HFM.
- [Ligar ao TM1](/pt-pt/guides/connections/tm1/) — ligar a um servidor IBM TM1 / Planning Analytics e ler dados de cubos por vista ou MDX, segmentados por período.
- [Ligar ao Anaplan](/pt-pt/guides/connections/anaplan/) — ligar ao Anaplan e ler uma vista guardada, executar uma ação de exportação já existente ou carregar listas para uma dimensão do PlaidCloud. Só de leitura.
- [OneStream para o Data Foundation](/pt-pt/guides/connections/onestream-for-data-foundation/) — o que o administrador do OneStream configura para que o Data Foundation possa ler resultados consolidados através de um adaptador de dados.
- [Ligar ao QuickBooks](/pt-pt/guides/connections/quickbooks/) — pré-requisitos e limitações atuais do QuickBooks Online.
- [Rever o registo de lançamentos](/pt-pt/guides/connections/posting-register/) — uma consola ao nível do tenant para as equipas de finanças e contabilidade reverem os lançamentos de ERP em todos os projetos e ligações que podem ver.

## Relacionados

- [Referência de conectores](/pt-pt/reference/connectors/) — o catálogo completo de sistemas suportados e dos campos de que cada um precisa.
