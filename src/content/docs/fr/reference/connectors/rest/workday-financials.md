---
title: Connecteur Workday Financials
description: Configurez une connexion Workday Financials dans PlaidCloud avec un utilisateur du système d'intégration pour importer des données via un rapport RaaS et comptabiliser des écritures de journal via SOAP.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday-financials.md
---

## Documentation de l'API

Les [services web SOAP](https://community.workday.com/sites/default/files/file-hosting/productionapi/) et le [Report-as-a-Service (RaaS)](https://doc.workday.com/) de Workday documentent les interfaces utilisées par ce connecteur.

## Fonctionnement de l'authentification

La connexion s'authentifie avec un **utilisateur du système d'intégration (ISU)**, un type d'utilisateur Workday conçu pour l'intégration de système à système, protégé par un groupe de sécurité du système d'intégration qui ne lui accorde que l'accès nécessaire à ce connecteur (accès aux rapports pour les lectures, processus métier Submit Accounting Journal pour les comptabilisations). Les requêtes transportent le nom d'utilisateur et le mot de passe de l'ISU ; il n'y a aucune connexion interactive.

## Configuration

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| Hôte du tenant | Texte | Votre hôte Workday, par exemple `wd5-impl.workday.com`. |
| Nom du tenant | Texte | Le nom de votre tenant Workday. |
| Nom d'utilisateur ISU | Texte | Le nom d'utilisateur de l'utilisateur du système d'intégration. |
| Mot de passe ISU | Texte | Le mot de passe de l'utilisateur du système d'intégration. Stocké chiffré. |

## Importation de données

Workday Financials n'a pas d'ensemble fixe d'entités prédéfinies. L'étape **Import Workday Entity** appelle à la place un **rapport Report-as-a-Service (RaaS)** que vous créez dans Workday et publiez avec l'accès Web Service ; vous en fournissez l'URL. L'étape prend en charge des filtres sur `company`, `ledger`, `period`, `accounting_date` (plage), `ledger_account` (plage) et `cost_center`, chacun transmis comme paramètre du rapport ; un filtre ne fonctionne donc que si votre rapport définit une invite correspondante. Consultez [Import Workday Entity](/fr/reference/workflow-steps/workday-financials/import-workday-entity/) pour la référence complète des champs.

## Comptabilisation des écritures de journal

L'étape **Workday Financials: Post Journal Entry** comptabilise des journaux comptables via le pipeline d'écriture ERP partagé de PlaidCloud, en utilisant l'opération SOAP `Submit_Accounting_Journal` de Workday et en interrogeant le statut du processus métier de l'écriture jusqu'à un état terminal avant de la déclarer comptabilisée. Une correction comptabilise une nouvelle écriture d'extourne avec débit et crédit inversés, au lieu de modifier l'originale. Consultez [Workday Financials: Post Journal Entry](/fr/reference/workflow-steps/workday-financials/workday-post/) pour la référence des champs, et [Se connecter à Workday Financials](/fr/guides/connections/workday-financials/) pour le guide complet de la comptabilisation.

## Limitations connues

| Limitation | Signification |
|---|---|
| La forme de l'import dépend de votre rapport RaaS | PlaidCloud n'a aucune entité prédéfinie pour Workday Financials : les champs, les invites et le contrôle d'accès du rapport résident tous dans Workday. Une modification du rapport dans Workday peut changer la forme de votre import sans aucun changement côté PlaidCloud. |
| L'approbation du processus métier ajoute de la latence | Un journal acheminé par une étape d'approbation de votre processus métier Submit Accounting Journal reste `pending` jusqu'à son approbation dans Workday ; l'interrogation de l'état terminal attend cette approbation. |
## Voir aussi

- [Se connecter à Workday Financials (guide)](/fr/guides/connections/workday-financials/) : étape par étape, créez la connexion, testez-la, importez un rapport et comptabilisez un journal.
- [Import Workday Entity](/fr/reference/workflow-steps/workday-financials/import-workday-entity/)
- [Workday Financials: Post Journal Entry](/fr/reference/workflow-steps/workday-financials/workday-post/)
- [Consulter l'historique des comptabilisations ERP](/fr/guides/connections/erp-post-history/)
- [Connecteur REST Workday](/fr/reference/connectors/rest/workday/) : le connecteur Workday générique distinct pour les données REST de RH et de paie.
