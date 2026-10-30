---
title: Étapes Business Central
description: "Étapes de workflow qui lisent et écrivent dans Microsoft Dynamics 365 Business Central via votre connexion Business Central : importer des entités OData et comptabiliser des lignes de journal général."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/business-central/index.md
---

Étapes de workflow qui lisent et écrivent dans Business Central via votre [connexion Business Central](/fr/guides/connections/business-central/). L'étape d'importation récupère les entités OData v2.0 standard de Business Central sans requête à rédiger ; l'étape de comptabilisation comptabilise des lignes de journal général via le pipeline d'écriture ERP partagé de PlaidCloud.

## Étapes

- [Import Business Central Entity](/fr/reference/workflow-steps/business-central/import-business-central-entity/) : comptes, écritures du grand livre, clients, fournisseurs, articles et journaux, avec des filtres côté serveur.
- [Business Central: Post General Journal Lines](/fr/reference/workflow-steps/business-central/business-central-post/) : comptabiliser des lignes dans un lot de journal existant, puis comptabiliser le lot.

## Voir aussi

- [Connecteur REST Business Central](/fr/reference/connectors/rest/business-central/)
- [Se connecter à Business Central](/fr/guides/connections/business-central/)
- [Consulter l'historique des comptabilisations ERP](/fr/guides/connections/erp-post-history/)
