---
title: Étapes Oracle EPM (HFM / FCCS)
description: "Étapes de workflow qui permettent d'obtenir en libre-service une tranche de données ad hoc d'Oracle FCCS via votre connexion HFM/FCCS : construisez un point de vue, exécutez-le et déposez le résultat sous forme de table."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/index.md
---

Étapes de workflow qui lisent des données depuis Oracle **FCCS** (Financial Consolidation and Close, EPM Cloud) via votre [connexion HFM/FCCS](/fr/guides/connections/hfm-fccs/). Un utilisateur de la finance construit un point de vue dans le formulaire de l'étape et l'exécute ; la grille renvoyée arrive automatiquement sous forme de table de projet, sans ticket auprès de l'équipe HFM et sans connaissance de la consolidation.

## Étapes

- [HFM/FCCS : lire les données (ad hoc)](/fr/reference/workflow-steps/oracle-epm/hfm-fccs-read/) : obtenez une tranche de données en libre-service avec un sélecteur de point de vue ; met en cache les extractions répétées, est prête pour la sécurité au niveau des lignes et peut être promue en chargement récurrent planifié.

## Voir aussi

- [Extraire depuis HFM / FCCS (guide)](/fr/guides/connections/hfm-fccs/)
- [Connecteur HFM / FCCS](/fr/reference/connectors/rest/hfm-fccs/)
