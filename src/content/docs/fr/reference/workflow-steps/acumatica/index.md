---
title: Étapes Acumatica
description: "Étapes de workflow qui lisent et écrivent dans Acumatica via votre connexion Acumatica : importation d'entités REST par contrat, et comptabilisation d'écritures de journal, de factures, de factures fournisseur et de paiements."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/acumatica/index.md
---

Étapes de workflow qui lisent et écrivent dans Acumatica via votre [connexion Acumatica](/fr/guides/connections/acumatica/). L'étape d'importation récupère les entités REST par contrat d'Acumatica sans OData à écrire ; l'étape de comptabilisation comptabilise des écritures de journal, des factures de vente, des factures fournisseur et des paiements via le pipeline d'écriture ERP partagé de PlaidCloud.

## Étapes

- [Import Acumatica Entity](/fr/reference/workflow-steps/acumatica/import-acumatica-entity/) : données de base et entités transactionnelles, avec des filtres côté serveur.
- [Acumatica: Post Documents](/fr/reference/workflow-steps/acumatica/acumatica-post/) : comptabilisation d'écritures de journal, de factures de vente, de factures fournisseur et de paiements.

## Voir aussi

- [Connecteur REST Acumatica](/fr/reference/connectors/rest/acumatica/)
- [Se connecter à Acumatica](/fr/guides/connections/acumatica/)
- [Consulter l'historique des comptabilisations ERP](/fr/guides/connections/erp-post-history/)
