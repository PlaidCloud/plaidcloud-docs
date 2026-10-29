---
title: Ligações
description: Configure e gira as ligações do PlaidCloud — configurações guardadas que permitem aos fluxos de trabalho aceder a bases de dados externas, armazenamento na nuvem, ERP e APIs REST.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

Uma **ligação** é uma configuração guardada que permite ao PlaidCloud aceder a um sistema externo — uma base de dados, uma conta de armazenamento na nuvem, um ERP ou uma API REST. Os passos de fluxo de trabalho que precisam de ler desse sistema ou de escrever nele referenciam a ligação, pelo que as credenciais e os detalhes do endpoint ficam num único local.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="Muitos passos de fluxo de trabalho referenciam uma única ligação guardada, que guarda as credenciais e o endpoint num só local e acede ao sistema externo — uma base de dados, armazenamento na nuvem, ERP ou API REST." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">passos de fluxo de trabalho</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Passo de importação</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Passo de exportação</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Passo de pesquisa</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Ligação</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">credenciais + endpoint, uma só vez</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">sistema externo</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">BD · armazenamento · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Configure a ligação uma só vez; todos os passos que leem do sistema externo ou escrevem nele apontam para ela, pelo que as credenciais e os detalhes do endpoint não ficam duplicados pelos passos.</figcaption>
</figure>

## Guias

- [Criar e gerir uma ligação](/pt-pt/guides/connections/create-connection/) — crie, edite, teste e controle o acesso a uma ligação, e configure-a por ambiente.
- [Utilizar o seu próprio data warehouse](/pt-pt/guides/connections/external-lakehouse/) — ligue o seu próprio warehouse Snowflake ou Databricks, inicie sessão com a sua própria identidade, gira vários data warehouses e veja quanto custa cada execução.
- [Ligação PlaidCloud Git](/pt-pt/guides/connections/plaidcloud-git/) — ligue-se ao servidor Git gerido da sua área de trabalho sem URL de servidor nem credenciais, e automatize a partir dele as compilações de aplicações Panel.
- [Clonar uma ligação](/pt-pt/guides/connections/clone-connection/) — duplique uma ligação existente para um novo ambiente ou inquilino.
- [Data Foundation: o Common Finance Model](/pt-pt/guides/projects/data-foundation/) — o Common Finance Model reúne dados de ERP de vários sistemas e instâncias ERP num único modelo, com um plano de contas, um conjunto de entidades e uma moeda de relato, que os relatórios, os indicadores e os assistentes de IA leem.
- [Fontes Singer](/pt-pt/guides/connections/singer-sources/) — ligue-se a fontes como Stripe, GitHub, Slack e BigQuery com taps Singer e importe os respetivos dados para tabelas do projeto.
- [Ligar ao NetSuite](/pt-pt/guides/connections/netsuite/) — configure uma ligação ao NetSuite e obtenha dados financeiros e operacionais com SuiteQL.
- [Acesso ao NetSuite para o Data Foundation](/pt-pt/guides/connections/netsuite-access-for-data-foundation/) — o que o seu administrador do NetSuite configura para que o Data Foundation possa ler diretamente o NetSuite, e o que lhe deve enviar de volta.
- [Importar dados financeiros do NetSuite](/pt-pt/guides/connections/import-netsuite-financials/) — importe saldos, detalhe do razão geral e dados mestre com os passos de importação NetSuite predefinidos, sem escrever SuiteQL.
- [Lançar um lançamento de diário no NetSuite](/pt-pt/guides/connections/post-netsuite-journal-entries/) — mapeie as tabelas de cabeçalho e de linhas, pré-visualize e lance lançamentos de diário no NetSuite.
- [Ligar ao Acumatica](/pt-pt/guides/connections/acumatica/) — configure uma ligação ao Acumatica, importe entidades e lance transações de diário, faturas, contas a pagar e pagamentos.
- [Ligar ao Business Central](/pt-pt/guides/connections/business-central/) — configure uma ligação ao Business Central com o Azure AD, importe entidades OData e lance linhas do diário geral.
- [Ligar ao Dynamics 365 Finance & Operations](/pt-pt/guides/connections/dynamics-365-fo/) — configure uma ligação ao D365 F&O com o Azure AD, importe entidades OData/DMF e lance lançamentos de diário.
- [Ligar ao Oracle Fusion](/pt-pt/guides/connections/oracle-fusion/) — configure uma ligação ao Oracle Fusion, importe saldos do razão geral e lotes de diário, e lance diários através do FBDI.
- [Ligar ao Workday Financials](/pt-pt/guides/connections/workday-financials/) — configure uma ligação ao Workday Financials com um Integration System User, importe um relatório RaaS e lance lançamentos de diário.
- [Ligar ao SAP S/4HANA Cloud](/pt-pt/guides/connections/s4hana-cloud/) — configure uma ligação direta ao S/4HANA Cloud com OAuth2, importe o balancete e os itens de lançamentos de diário, e lance lançamentos de diário por SOAP.
- [Extrações ad hoc do SAP ECC / S/4HANA](/pt-pt/guides/connections/sap-adhoc-extract/) — pesquise no SAP por tabela, código de transação ou SAP Query guardada, pré-visualize e planeie a extração e carregue-a numa tabela através de um agente PlaidLink.
- [Ligar ao Sage Intacct](/pt-pt/guides/connections/sage-intacct/) — configure uma ligação ao Sage Intacct e obtenha dados financeiros e contabilísticos.
- [Ligar ao Xero](/pt-pt/guides/connections/xero/) — autorize uma organização Xero num só clique, importe entidades da Accounting API e lance diários manuais, faturas, contas a pagar, pagamentos e notas de crédito.
- [Ligar ao Salesforce](/pt-pt/guides/connections/salesforce/) — configure uma Salesforce External Client App e um utilizador Run As, e extraia objetos de CRM para tabelas do projeto.
- [Extrair do HFM / FCCS (ad hoc)](/pt-pt/guides/connections/hfm-fccs/) — ligue-se ao Oracle FCCS e obtenha por si próprio uma fatia de dados com um seletor de ponto de vista, sem pedidos à equipa do HFM.
- [Ligar ao TM1](/pt-pt/guides/connections/tm1/) — ligue-se a um servidor IBM TM1 / Planning Analytics e leia dados de cubos por vista ou MDX, divididos por período.
- [Ligar ao Anaplan](/pt-pt/guides/connections/anaplan/) — ligue-se ao Anaplan e leia uma vista guardada, execute uma ação de exportação já existente ou carregue listas para uma dimensão do PlaidCloud. Só de leitura.
- [Ligar ao QuickBooks](/pt-pt/guides/connections/quickbooks/) — pré-requisitos e limitações atuais do QuickBooks Online.
- [Rever o registo de lançamentos](/pt-pt/guides/connections/posting-register/) — uma consola ao nível do inquilino para que as finanças e a contabilidade revejam os lançamentos ERP em todos os projetos e ligações que consigam ver.

## Relacionado

- [Referência de conectores](/pt-pt/reference/connectors/) — o catálogo completo de sistemas suportados e os campos de que cada um necessita.
