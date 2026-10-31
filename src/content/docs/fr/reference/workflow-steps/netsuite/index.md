---
title: Étapes NetSuite
description: Étapes de workflow NetSuite pour importer des soldes, le détail du grand livre, des données de base ou votre propre requête SuiteQL, et pour comptabiliser des écritures de journal via votre connexion NetSuite.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/netsuite/index.md
---

Étapes de workflow qui lisent et écrivent dans NetSuite via votre [connexion NetSuite](/fr/guides/connections/netsuite/). Les étapes d'importation prédéfinies sont le moyen le plus simple d'extraire les données financières et de référence courantes : choisissez une connexion, une table cible et une plage de dates ou un type d'enregistrement, sans SuiteQL à écrire.

## Étapes d'importation

- [NetSuite : importer les soldes](/fr/reference/workflow-steps/netsuite/import-balances/) : soldes de comptes (une balance générale) pour une plage de dates et une filiale.
- [NetSuite : importer le détail du grand livre](/fr/reference/workflow-steps/netsuite/import-gl-detail/) : détail des lignes de transactions du grand livre pour une plage de dates et une filiale.
- [NetSuite : importer les données de base](/fr/reference/workflow-steps/netsuite/import-master-data/) : listes de données de base (comptes, filiales, départements, classes, emplacements, fournisseurs ou clients).
- [NetSuite : importer une requête SuiteQL](/fr/reference/workflow-steps/netsuite/import-suiteql-query/) : exécutez votre propre requête SuiteQL et chargez le résultat dans une table typée, les fenêtres de dates et la pagination étant gérées pour vous.

## Étapes de comptabilisation

- [Post NetSuite Journal Entry](/fr/reference/workflow-steps/netsuite/post-netsuite-journal-entry/) : comptabilisez dans NetSuite des écritures de journal composées d'un en-tête et de lignes.

## Extractions personnalisées

Pour les données que les étapes d'importation prédéfinies ne couvrent pas (une requête sur mesure ou un enregistrement NetSuite sans étape prédéfinie), utilisez [NetSuite : importer une requête SuiteQL](/fr/reference/workflow-steps/netsuite/import-suiteql-query/) avec votre propre SuiteQL. Consultez [Exemples de requêtes SuiteQL NetSuite](/fr/guides/connections/netsuite-financial-queries/) pour des points de départ.

## Voir aussi

- [Connecteur REST NetSuite](/fr/reference/connectors/rest/netsuite/)
- [Se connecter à NetSuite](/fr/guides/connections/netsuite/)
- [Importer les données financières NetSuite](/fr/guides/connections/import-netsuite-financials/)
