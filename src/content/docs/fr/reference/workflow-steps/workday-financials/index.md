---
title: Étapes Workday Financials
description: "Étapes de workflow qui lisent et écrivent dans Workday Financials via votre connexion Workday Financials : importer des données au moyen d'un rapport RaaS et comptabiliser des journaux comptables."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workday-financials/index.md
---

Étapes de workflow qui lisent et écrivent dans Workday Financials via votre [connexion Workday Financials](/fr/guides/connections/workday-financials/). L'étape d'import récupère un rapport Report-as-a-Service (RaaS) fourni par le client ; l'étape de comptabilisation enregistre des journaux comptables via le pipeline d'écriture ERP partagé de PlaidCloud.

## Étapes

- [Import Workday Entity](/fr/reference/workflow-steps/workday-financials/import-workday-entity/) — récupérer un rapport RaaS, avec des filtres de paramètres de rapport.
- [Workday Financials: Post Journal Entry](/fr/reference/workflow-steps/workday-financials/workday-post/) — comptabiliser des journaux comptables via `Submit_Accounting_Journal`, avec une écriture d'extourne comptabilisée pour les corrections.

## Voir aussi

- [Connecteur Workday Financials](/fr/reference/connectors/rest/workday-financials/)
- [Se connecter à Workday Financials](/fr/guides/connections/workday-financials/)
- [Consulter l'historique des comptabilisations ERP](/fr/guides/connections/erp-post-history/)
