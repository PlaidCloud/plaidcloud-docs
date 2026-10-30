---
title: Étapes D365 F&O
description: Étapes de workflow qui lisent et écrivent dans Dynamics 365 Finance & Operations via votre connexion D365 F&O — importation d'entités OData/DMF et comptabilisation d'écritures de journal.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dynamics-365-fo/index.md
---

Étapes de workflow qui lisent et écrivent dans Dynamics 365 Finance & Operations (D365 F&O) via votre [connexion D365 F&O](/fr/guides/connections/dynamics-365-fo/). L'étape d'importation récupère des entités OData ou des extractions DMF en bloc sans OData à écrire ; l'étape de comptabilisation comptabilise des écritures de journal du grand livre via le pipeline d'écriture ERP partagé de PlaidCloud.

## Étapes

- [Import D365 F&O Entity](/fr/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) — données de base et en-têtes de journal, en mode OData ou DMF en bloc, avec des filtres côté serveur.
- [D365 F&O: Post Journal Entry](/fr/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) — comptabilise des écritures de journal du grand livre, avec une écriture d'extourne comptabilisée pour les corrections.

## Voir aussi

- [Connecteur REST Dynamics 365 F&O](/fr/reference/connectors/rest/dynamics-365-fo/)
- [Se connecter à Dynamics 365 Finance & Operations](/fr/guides/connections/dynamics-365-fo/)
- [Examiner l'historique des comptabilisations ERP](/fr/guides/connections/erp-post-history/)
