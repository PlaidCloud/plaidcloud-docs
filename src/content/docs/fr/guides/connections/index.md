---
title: Connexions
description: Configurez et gérez les connexions PlaidCloud, des configurations enregistrées qui permettent aux workflows d'accéder à des bases de données externes, au stockage cloud, aux ERP et aux API REST.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

Une **connexion** est une configuration enregistrée qui permet à PlaidCloud d'accéder à un système externe : base de données, compte de stockage cloud, ERP ou API REST. Les étapes de workflow qui doivent lire ou écrire dans ce système font référence à la connexion, ce qui centralise en un seul endroit les identifiants et les détails du point de terminaison.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="De nombreuses étapes de workflow font référence à une même connexion enregistrée, qui regroupe en un seul endroit les identifiants et le point de terminaison et accède au système externe : base de données, stockage cloud, ERP ou API REST." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">étapes de workflow</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Étape d'import</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Étape d'export</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Étape de recherche</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Connexion</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">identifiants + point de terminaison, une fois</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">système externe</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">BD · stockage · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Configurez la connexion une seule fois ; chaque étape qui lit ou écrit dans le système externe la référence, de sorte que les identifiants et les détails du point de terminaison ne sont pas dupliqués d'une étape à l'autre.</figcaption>
</figure>

## Guides

- [Créer et gérer une connexion](/fr/guides/connections/create-connection/) : créez, modifiez, testez et contrôlez l'accès à une connexion, et configurez-la par environnement.
- [Utiliser votre propre entrepôt de données](/fr/guides/connections/external-lakehouse/) : connectez vous-même votre propre entrepôt Snowflake ou Databricks, connectez-vous avec votre propre identité, gérez plusieurs entrepôts et consultez le coût de chaque exécution.
- [Connexion PlaidCloud Git](/fr/guides/connections/plaidcloud-git/) : connectez-vous au serveur Git géré de votre espace de travail sans URL de serveur ni identifiants, et automatisez à partir de celui-ci la génération des applications Panel.
- [Cloner une connexion](/fr/guides/connections/clone-connection/) : dupliquez une connexion existante pour un nouvel environnement ou un nouveau locataire.
- [Data Foundation : le Common Finance Model](/fr/guides/projects/data-foundation/) : le Common Finance Model rassemble les données ERP de plusieurs systèmes et instances ERP dans un seul modèle, avec un seul plan comptable, un seul ensemble d'entités et une seule devise de reporting, que les rapports, les métriques et les assistants IA lisent tous.
- [Sources Singer](/fr/guides/connections/singer-sources/) : connectez-vous à des sources comme Stripe, GitHub, Slack et BigQuery avec des taps Singer, puis importez leurs données dans des tables de projet.
- [Se connecter à NetSuite](/fr/guides/connections/netsuite/) : configurez une connexion NetSuite et importez des données financières et opérationnelles avec SuiteQL.
- [Accès NetSuite pour Data Foundation](/fr/guides/connections/netsuite-access-for-data-foundation/) : ce que votre administrateur NetSuite configure pour que Data Foundation puisse lire directement NetSuite, et ce qu'il faut renvoyer.
- [Importer les données financières NetSuite](/fr/guides/connections/import-netsuite-financials/) : importez les soldes, le détail du grand livre et les données de référence avec les étapes d'importation NetSuite prêtes à l'emploi, sans SuiteQL à écrire.
- [Comptabiliser une écriture de journal NetSuite](/fr/guides/connections/post-netsuite-journal-entries/) : associez les tables d'en-tête et de lignes, prévisualisez et comptabilisez des écritures de journal dans NetSuite.
- [Se connecter à Acumatica](/fr/guides/connections/acumatica/) : configurez une connexion Acumatica, importez des entités et comptabilisez des transactions de journal, des factures, des factures fournisseur et des paiements.
- [Se connecter à Business Central](/fr/guides/connections/business-central/) : configurez une connexion Business Central avec Azure AD, importez des entités OData et comptabilisez des lignes de journal général.
- [Se connecter à Dynamics 365 Finance & Operations](/fr/guides/connections/dynamics-365-fo/) : configurez une connexion D365 F&O avec Azure AD, importez des entités OData/DMF et comptabilisez des écritures de journal.
- [Se connecter à Oracle Fusion](/fr/guides/connections/oracle-fusion/) : configurez une connexion Oracle Fusion, importez les soldes du grand livre et les lots de journaux, et comptabilisez des journaux via FBDI.
- [Se connecter à Workday Financials](/fr/guides/connections/workday-financials/) : configurez une connexion Workday Financials avec un utilisateur du système d'intégration, importez un rapport RaaS et comptabilisez des écritures de journal.
- [Se connecter à SAP S/4HANA Cloud](/fr/guides/connections/s4hana-cloud/) : configurez une connexion directe à S/4HANA Cloud avec OAuth2, importez la balance générale et les postes d'écritures de journal, et comptabilisez des écritures de journal via SOAP.
- [Extractions ad hoc depuis SAP ECC / S/4HANA](/fr/guides/connections/sap-adhoc-extract/) : recherchez dans SAP par table, code de transaction ou requête SAP enregistrée, prévisualisez et planifiez l'extraction, puis chargez-la dans une table via un agent PlaidLink.
- [Se connecter à Sage Intacct](/fr/guides/connections/sage-intacct/) : configurez une connexion Sage Intacct et importez des données financières et comptables.
- [Se connecter à Xero](/fr/guides/connections/xero/) : autorisez une organisation Xero en un clic, importez des entités de l'API Accounting et comptabilisez des journaux manuels, des factures, des factures fournisseur, des paiements et des avoirs.
- [Se connecter à Salesforce](/fr/guides/connections/salesforce/) : configurez une External Client App Salesforce et un utilisateur Run As, puis extrayez des objets CRM dans des tables de projet.
- [Extraire depuis HFM / FCCS (ad hoc)](/fr/guides/connections/hfm-fccs/) : connectez-vous à Oracle FCCS et extrayez vous-même une tranche de données grâce à un sélecteur de point de vue, sans ticket auprès de l'équipe HFM.
- [Se connecter à TM1](/fr/guides/connections/tm1/) : connectez-vous à un serveur IBM TM1 / Planning Analytics et lisez les données de cube par vue ou MDX, découpées par période.
- [Se connecter à Anaplan](/fr/guides/connections/anaplan/) : connectez-vous à Anaplan et lisez une vue enregistrée, exécutez une action d'export existante ou chargez des listes dans une dimension PlaidCloud. Lecture seule.
- [Se connecter à QuickBooks](/fr/guides/connections/quickbooks/) : prérequis et limitations actuelles pour QuickBooks Online.
- [Consulter le registre des écritures](/fr/guides/connections/posting-register/) : une console au niveau du locataire permettant aux équipes finance et comptabilité de consulter les écritures ERP de tous les projets et connexions qu'elles peuvent voir.

## Voir aussi

- [Référence des connecteurs](/fr/reference/connectors/) : le catalogue complet des systèmes pris en charge et des champs requis par chacun.
