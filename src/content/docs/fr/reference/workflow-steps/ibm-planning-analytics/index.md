---
title: Étapes IBM TM1 / Planning Analytics
description: Étapes de workflow qui lisent depuis un serveur IBM TM1 / Planning Analytics via votre connexion TM1 — données de cube par vue enregistrée ou MDX, et hiérarchies de dimensions — en accès direct au cloud ou via un agent PlaidLink sur site.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/index.md
---

Étapes de workflow qui lisent depuis IBM **TM1 / Planning Analytics** via votre [connexion TM1](/fr/guides/connections/tm1/) : données de cube par vue enregistrée ou MDX, avec une tranche de point de vue facultative, et hiérarchies de dimensions chargées dans une dimension PlaidCloud. Accédez à TM1 en accès direct au cloud ou, pour un serveur accessible uniquement depuis l'intérieur de votre propre réseau, via un agent PlaidLink sur site.

## Étapes

- [TM1 : interroger un cube](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — lit un cube par vue enregistrée ou MDX, avec une tranche de point de vue et un aperçu avant enregistrement. Accès direct au cloud.
- [TM1 : interroger un cube (agent)](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — le jumeau sur site de TM1 : interroger un cube, exécuté via un agent PlaidLink installé.
- [TM1 : lire une dimension](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — charge une hiérarchie TM1 dans une dimension PlaidCloud. Accès direct au cloud.

## Voir aussi

- [Se connecter à TM1 (guide)](/fr/guides/connections/tm1/)
- [Connecteur TM1](/fr/reference/connectors/rest/tm1/)
