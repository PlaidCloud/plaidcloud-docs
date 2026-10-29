---
title: Étapes de workflow
description: "Tous les types d'étapes de workflow de PlaidCloud : importation, exportation, transformations, allocations, dimensions, documents, notifications, et plus encore."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/index.md
---

Les étapes de workflow sont les éléments de base de l'automatisation dans PlaidCloud. Chaque étape effectue une opération (importer un CSV, joindre deux tables, envoyer une notification), et les étapes sont assemblées en workflows qui s'exécutent de façon séquentielle, en parallèle, de manière conditionnelle ou en boucle.

## Catégories

### Mouvement des données

- [Importation](/fr/reference/workflow-steps/import/) : récupérez des données depuis CSV, Excel, Parquet, JSON, ORC, Delta Lake, SQL, BigQuery, MongoDB, Kafka, SPSS, des sources Singer, et plus encore
- [Exportation](/fr/reference/workflow-steps/export/) : envoyez des données vers CSV, XML, SQL, Excel, Google Sheets, Parquet, ORC, MongoDB, Kafka, des archives de table, et plus encore

### Transformations de tables

- [Tables](/fr/reference/workflow-steps/tables/) : jointures, unions, filtres, recherches, tableaux croisés, dépivotages, mises à jour ciblées, droits d'Accès aux lignes à partir d'une table source, restauration à un instant donné
- [Opérations communes](/fr/reference/workflow-steps/common/) : modèles partagés de mappage et de filtrage des données

### Géospatial

- [Géospatial](/fr/reference/workflow-steps/spatial/) : importation et exportation de fichiers spatiaux, tampon, correspondance, mesure, reprojection et construction de géométries ; couverture complète des outils spatiaux d'Alteryx

### Modélisation

- [Allocation](/fr/reference/workflow-steps/allocation/) : répartition par inducteurs, allocations fractionnées, étiquetage par règles
- [Dimensions](/fr/reference/workflow-steps/dimensions/) : chargement, tri, effacement, exportation et gestion des hiérarchies
- [Optimisation](/fr/reference/workflow-steps/optimization/) : étapes de solveur linéaire et en nombres entiers mixtes
- [Machine learning](/fr/reference/workflow-steps/machine-learning/) : entraînement de modèles, y compris XGBoost et les apprenants KNIME, et scoring de tables avec ces modèles

### Documents et fichiers

- [Document](/fr/reference/workflow-steps/document/) : opérations sur les fichiers, liste de répertoire, chiffrement, manipulation de PDF, traitement d'images, conversion d'encodage, mises à jour de cellules Excel
- [Texte et documents](/fr/reference/workflow-steps/text-documents/) : extraction de texte de PDF, OCR d'images, lecture et écriture de blobs, analyse de sentiment, modélisation de sujets, nuages de mots

### Communication

- [Notifications](/fr/reference/workflow-steps/notifications/) : e-mail, Slack, Teams, SMS, webhook, Twitter, journal
- [Rapports](/fr/reference/workflow-steps/reports/) : génération de rapports PDF uniques ou par lots à partir de modèles RML

### Contrôle du workflow

- [Contrôle du workflow](/fr/reference/workflow-steps/workflow-control/) : variables, boucles, sous-workflows, macros, gestion des erreurs, vérification du nombre de lignes
- [Général](/fr/reference/workflow-steps/general/) : étape LLM, pass, attente, transformation définie par l'utilisateur, exécution de Python à distance, exécuteur Alteryx
- [Macros empaquetées](/fr/reference/workflow-steps/macros/) : équivalents des macros empaquetées Alteryx : Create Samples, DateTime Now, Heat Map, Pie Wedge Trade Area

### Intégrations d'entreprise

- [Agent](/fr/reference/workflow-steps/agent/) : opérations de l'agent PlaidLink pour les ressources sur site
- [NetSuite](/fr/reference/workflow-steps/netsuite/) : importation de soldes, du détail du grand livre, de données de base ou de votre propre [requête SuiteQL](/fr/reference/workflow-steps/netsuite/import-suiteql-query/) ; comptabilisation d'écritures de journal dans NetSuite
- [Acumatica](/fr/reference/workflow-steps/acumatica/) : importation d'entités de données de base et transactionnelles ; comptabilisation de transactions de journal, de factures, de factures fournisseurs et de paiements
- [Business Central](/fr/reference/workflow-steps/business-central/) : importation d'entités OData ; comptabilisation de lignes de journal général
- [Xero](/fr/reference/workflow-steps/xero/) : importation d'entités de l'API Accounting ; comptabilisation d'écritures manuelles, de factures, de factures fournisseurs, de paiements et d'avoirs
- [Dynamics 365 F&O](/fr/reference/workflow-steps/dynamics-365-fo/) : importation d'entités OData/DMF ; comptabilisation d'écritures de journal
- [Oracle Fusion](/fr/reference/workflow-steps/oracle-fusion/) : importation de soldes du grand livre et de lots de journaux ; comptabilisation d'écritures de journal via FBDI
- [Oracle EPM (HFM / FCCS)](/fr/reference/workflow-steps/oracle-epm/) : extraction en libre-service d'une tranche de données ad hoc depuis Oracle FCCS avec un sélecteur de point de vue ; chargement récurrent planifié facultatif
- [Oracle Essbase](/fr/reference/workflow-steps/essbase/) : exécution d'une requête MDX en direct sur un cube, ou chargement d'un plan de dimension comme dimension PlaidCloud ; cloud direct
- [IBM TM1 / Planning Analytics](/fr/reference/workflow-steps/ibm-planning-analytics/) : lecture d'un cube par vue enregistrée ou MDX, ou d'une hiérarchie de dimension ; cloud direct ou via un agent sur site
- [Anaplan](/fr/reference/workflow-steps/anaplan/) : lecture d'une vue enregistrée, exécution d'une action d'export existante, ou chargement d'une ou plusieurs listes dans une dimension PlaidCloud ; cloud direct, en lecture seule
- [Workday Financials](/fr/reference/workflow-steps/workday-financials/) : importation d'un rapport RaaS ; comptabilisation d'écritures comptables
- [Salesforce](/fr/reference/workflow-steps/salesforce/) : extraction de tout objet CRM standard ou personnalisé dans une table de projet via Bulk API 2.0, l'objet et la liste des champs étant lus depuis l'organisation
- [Sage Intacct](/fr/reference/workflow-steps/sage-intacct/) : importation de soldes, de factures fournisseurs, de requêtes ad hoc et d'objets du grand livre/de dimensions ; comptabilisation d'écritures de journal
- [SAP S/4HANA Cloud](/fr/reference/workflow-steps/s4hana-cloud/) : importation de la balance générale et des lignes d'écritures de journal via OData ; comptabilisation d'écritures de journal via SOAP
- [SAP](/fr/reference/workflow-steps/sap/) : appels RFC SAP ECC / S/4HANA
- [SAP-PCM](/fr/reference/workflow-steps/sap-pcm/) : contrôle des modèles SAP Profitability and Cost Management
