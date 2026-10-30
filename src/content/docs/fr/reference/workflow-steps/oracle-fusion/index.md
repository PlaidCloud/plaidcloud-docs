---
title: Étapes Oracle Fusion
description: "Étapes de workflow qui lisent et écrivent dans Oracle Fusion Cloud via votre connexion Oracle Fusion : importation des soldes du grand livre et des lots d'écritures via OData/BIP ou extraction en masse FBDI, et comptabilisation d'écritures de journal."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-fusion/index.md
---

Étapes de workflow qui lisent et écrivent dans Oracle Fusion Cloud via votre [connexion Oracle Fusion](/fr/guides/connections/oracle-fusion/). Deux étapes d'importation couvrent des volumes différents : un appel direct OData/BIP pour les extractions courantes, et une extraction en masse asynchrone FBDI/BIP pour les gros volumes. L'étape de comptabilisation enregistre les lots d'écritures via le pipeline d'écriture ERP partagé de PlaidCloud.

## Étapes

- [Import Fusion Entity](/fr/reference/workflow-steps/oracle-fusion/import-fusion-entity/) (étape) : soldes du grand livre et lots d'écritures, avec des filtres de date, de période et de plage numérique appliqués côté serveur.
- [Import Fusion Bulk Extract](/fr/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) (étape) : les mêmes entités, via une tâche d'exportation asynchrone FBDI/BIP pour les gros volumes.
- [Oracle Fusion: Post Journal Entry](/fr/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) (étape) : comptabilise des lots d'écritures du grand livre via l'interface GL FBDI, avec une écriture d'extourne comptabilisée pour les corrections.

## Voir aussi

- [Connecteur Oracle Fusion](/fr/reference/connectors/erp/oracle-fusion/)
- [Se connecter à Oracle Fusion](/fr/guides/connections/oracle-fusion/)
- [Consulter l'historique des comptabilisations ERP](/fr/guides/connections/erp-post-history/)
