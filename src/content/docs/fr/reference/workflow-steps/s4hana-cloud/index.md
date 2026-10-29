---
title: Étapes SAP S/4HANA Cloud
description: "Étapes de workflow qui lisent et écrivent dans SAP S/4HANA Cloud Public Edition via votre connexion S/4HANA Cloud : importation de la balance générale et des postes d'écritures, et comptabilisation d'écritures de journal."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/s4hana-cloud/index.md
---

Étapes de workflow qui lisent et écrivent dans SAP S/4HANA Cloud Public Edition via votre [connexion S/4HANA Cloud](/fr/guides/connections/s4hana-cloud/). L'étape d'importation récupère la balance générale ou les postes d'écritures sans OData à rédiger. L'étape de comptabilisation enregistre les écritures de journal via le pipeline d'écriture ERP partagé de PlaidCloud.

## Étapes

- [Import S/4HANA Entity](/fr/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) (étape) : données de balance générale et de postes d'écritures, avec des filtres côté serveur.
- [S/4HANA: Post Journal Entry](/fr/reference/workflow-steps/s4hana-cloud/s4hana-post/) (étape) : comptabilise des écritures de journal via SOAP, avec une écriture d'extourne comptabilisée pour les corrections.

## Voir aussi

- [Connecteur REST SAP S/4HANA Cloud](/fr/reference/connectors/rest/s4hana-cloud/)
- [Se connecter à SAP S/4HANA Cloud](/fr/guides/connections/s4hana-cloud/)
- [Consulter l'historique des comptabilisations ERP](/fr/guides/connections/erp-post-history/)
