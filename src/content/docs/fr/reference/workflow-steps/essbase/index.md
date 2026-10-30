---
title: Étapes Oracle Essbase
description: Étapes de workflow qui lisent un cube Oracle Essbase via votre connexion Essbase — requêtes MDX en direct et plans de dimension chargés dans une dimension PlaidCloud — en accès direct au cloud.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/index.md
---

Étapes de workflow qui lisent Oracle **Essbase** via votre [connexion Oracle Essbase](/fr/guides/connections/essbase/) : les données d'un cube par requête MDX en direct, et le plan d'une dimension chargé dans une dimension PlaidCloud. Essbase est atteint **en direct dans le cloud** par son API REST : il n'existe aucun chemin par agent local pour ces étapes.

## Étapes

- [Essbase : interroger un cube](/fr/reference/workflow-steps/essbase/essbase-query/) — exécute une requête MDX en direct sur un cube et dépose la grille de résultat sous forme de table. Accès direct au cloud.
- [Essbase : lire une dimension](/fr/reference/workflow-steps/essbase/essbase-dimension-read/) — charge le plan d'une dimension Essbase dans une dimension PlaidCloud. Accès direct au cloud.

## Voir aussi

- [Se connecter à Oracle Essbase (guide)](/fr/guides/connections/essbase/)
- [Connecteur Oracle Essbase](/fr/reference/connectors/erp/oracle-essbase/)
