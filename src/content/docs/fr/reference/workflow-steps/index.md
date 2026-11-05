---
title: Étapes de workflow
description: "Tous les types d'étapes de workflow de PlaidCloud : import, export, transformations, allocations, dimensions, documents, notifications, et plus encore."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/index.md
---

Les étapes de workflow sont les éléments de base de l'automatisation PlaidCloud. Chaque étape effectue une opération (importer un CSV, joindre deux tables, envoyer une notification), et les étapes sont assemblées en workflows qui s'exécutent de manière séquentielle, en parallèle, conditionnelle ou en boucle.

## Catégories

### Déplacement des données

- [Import](/fr/reference/workflow-steps/import/) : récupérez des données depuis CSV, Excel, Parquet, JSON, ORC, Delta Lake, SQL, BigQuery, MongoDB, Kafka, SPSS, des sources Singer, et plus encore
- [Export](/fr/reference/workflow-steps/export/) : envoyez des données vers CSV, XML, SQL, Excel, Google Sheets, Parquet, ORC, MongoDB, Kafka, une archive de table, et plus encore

### Transformations de tables

- [Tables](/fr/reference/workflow-steps/tables/) : jointures, unions, filtres, recherches, pivots, fusions, mises à jour ciblées, attributions d'accès aux lignes à partir d'une table source, restauration à un instant donné
- [Opérations courantes](/fr/reference/workflow-steps/common/) : modèles partagés de mappage et de filtrage des données

### Géospatial

- [Géospatial](/fr/reference/workflow-steps/spatial/) : importez et exportez des fichiers spatiaux, créez des zones tampons, faites des correspondances, mesurez, reprojetez et construisez des géométries ; couverture complète des outils spatiaux d'Alteryx

### Modélisation

- [Allocation](/fr/reference/workflow-steps/allocation/) : répartition par inducteur, allocations fractionnées, étiquetage par règles
- [Dimensions](/fr/reference/workflow-steps/dimensions/) : chargez, triez, effacez, exportez et gérez des hiérarchies
- [Optimisation](/fr/reference/workflow-steps/optimization/) : étapes de solveur linéaire et en nombres entiers mixtes
- [Apprentissage automatique](/fr/reference/workflow-steps/machine-learning/) : entraînez des modèles, y compris des apprenants XGBoost et KNIME, et scorez des tables avec eux

### Documents et fichiers

- [Document](/fr/reference/workflow-steps/document/) : opérations sur les fichiers, liste de répertoire, chiffrement, manipulation de PDF, traitement d'images, conversion d'encodage, mises à jour de cellules Excel
- [Texte et documents](/fr/reference/workflow-steps/text-documents/) : extraction de texte de PDF, OCR d'images, lecture et écriture de blobs, sentiment, modélisation de sujets, nuages de mots

### Communication

- [Notifications](/fr/reference/workflow-steps/notifications/) : e-mail, Slack, Teams, SMS, webhook, Twitter, journal
- [Rapports](/fr/reference/workflow-steps/reports/) : produisez des rapports PDF uniques ou par lots à partir de modèles RML

### Contrôle du workflow

- [Contrôle du workflow](/fr/reference/workflow-steps/workflow-control/) : variables, boucles, sous-workflows, macros, gestion des erreurs, vérification du nombre de lignes
- [Général](/fr/reference/workflow-steps/general/) : Étape LLM, Pass, Attendre, User Defined Transform, Run Remote Python, Exécuteur Alteryx
- [Macros empaquetées](/fr/reference/workflow-steps/macros/) : équivalents des macros empaquetées d'Alteryx : Create Samples, DateTime Now, Heat Map, Pie Wedge Trade Area

### Intégrations d'entreprise

- [Agent](/fr/reference/workflow-steps/agent/) : opérations de l'agent PlaidLink pour les ressources sur site
- [NetSuite](/fr/reference/workflow-steps/netsuite/) : importez des soldes, le détail du grand livre, des données de base, ou votre propre [requête SuiteQL](/fr/reference/workflow-steps/netsuite/import-suiteql-query/) ; comptabilisez des écritures de journal dans NetSuite
- [Acumatica](/fr/reference/workflow-steps/acumatica/) : importez des entités de base et transactionnelles ; comptabilisez des transactions de journal, des factures, des factures fournisseur et des paiements
- [Business Central](/fr/reference/workflow-steps/business-central/) : importez des entités OData ; comptabilisez des lignes de journal général
- [Xero](/fr/reference/workflow-steps/xero/) : importez des entités de l'API Accounting ; comptabilisez des journaux manuels, des factures, des factures fournisseur, des paiements et des avoirs
- [Dynamics 365 F&O](/fr/reference/workflow-steps/dynamics-365-fo/) : importez des entités OData/DMF ; comptabilisez des écritures de journal
- [Oracle Fusion](/fr/reference/workflow-steps/oracle-fusion/) : importez des soldes du grand livre et des lots de journaux ; comptabilisez des écritures de journal via FBDI
- [Oracle EPM (HFM / FCCS)](/fr/reference/workflow-steps/oracle-epm/) : obtenez vous-même une tranche de données ad hoc depuis Oracle FCCS grâce à un sélecteur de point de vue ; chargement récurrent planifié en option
- [Oracle Essbase](/fr/reference/workflow-steps/essbase/) : exécutez une requête MDX en direct sur un cube, ou chargez le plan d'une dimension comme dimension PlaidCloud ; accès direct au cloud
- [IBM TM1 / Planning Analytics](/fr/reference/workflow-steps/ibm-planning-analytics/) : lisez un cube par vue enregistrée ou MDX, ou une hiérarchie de dimension ; accès direct au cloud ou via un agent sur site
- [Anaplan](/fr/reference/workflow-steps/anaplan/) : lisez une vue enregistrée, exécutez une action d'export existante ou chargez une ou plusieurs listes dans une dimension PlaidCloud ; accès direct au cloud, en lecture seule
- [OneStream](/fr/reference/workflow-steps/onestream/) : lisez un adaptateur de données, un appel par membre de consolidation, dans une table ; en lecture seule
- [Workday Financials](/fr/reference/workflow-steps/workday-financials/) : importez un rapport RaaS ; comptabilisez des journaux comptables
- [Salesforce](/fr/reference/workflow-steps/salesforce/) : extrayez n'importe quel objet CRM standard ou personnalisé dans une table de projet via Bulk API 2.0, la liste des objets et des champs étant lue depuis l'organisation
- [Sage Intacct](/fr/reference/workflow-steps/sage-intacct/) : importez des soldes, des factures fournisseur, des requêtes ad hoc et des objets de grand livre et de dimensions ; comptabilisez des écritures de journal
- [SAP S/4HANA Cloud](/fr/reference/workflow-steps/s4hana-cloud/) : importez la balance générale et les postes d'écritures de journal via OData ; comptabilisez des écritures de journal via SOAP
- [SAP](/fr/reference/workflow-steps/sap/) : appels RFC SAP ECC / S/4HANA
- [SAP-PCM](/fr/reference/workflow-steps/sap-pcm/) : contrôle des modèles SAP Profitability and Cost Management
