---
title: Connecteur REST Dynamics 365 Finance & Operations
description: Configurez une connexion Dynamics 365 Finance & Operations dans PlaidCloud pour importer des entités OData/DMF et comptabiliser des écritures de journal de façon asynchrone.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics-365-fo.md
---

## Documentation de l'API

Les [points de terminaison OData v4](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata) et le [Data Management Framework](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-management-import-export) de D365 F&O documentent les points de terminaison et le chemin d'extraction en masse qu'utilise ce connecteur.

## Fonctionnement de l'authentification

La connexion s'authentifie en tant qu'application via les **informations d'identification client** d'Entra ID (Azure AD) : l'ID client et le secret d'un enregistrement d'application sont échangés contre un jeton d'accès, limité à la ressource de l'environnement. Il n'y a aucune connexion interactive.

## Configuration

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| URL de l'environnement | Texte | L'URL de votre environnement D365 F&O, par exemple `https://yourorg.operations.dynamics.com`. |
| ID client | Texte | L'ID d'application (client) de l'enregistrement d'application Entra. |
| Secret client | Texte | Le secret client de l'enregistrement d'application. Stocké chiffré. |
| ID du locataire | Texte | L'ID de votre locataire Azure AD. |
| Ressource/portée | Texte | La portée OAuth2 demandée, généralement l'URL de l'environnement suivie de `/.default`. |

## Entités disponibles à l'import

L'étape **Import D365 F&O Entity** couvre six entités : `main_accounts`, `currencies`, `customers`, `vendors`, `released_products`, `ledger_journal_headers`. Chaque extraction s'exécute soit en mode synchrone `odata` (un appel direct, pour les extractions courantes), soit en mode en masse `dmf` (un job d'export asynchrone du Data Management Framework, pour les gros volumes), et prend en charge des filtres côté serveur propres à chaque entité, notamment des plages de dates, de comptes et de dimensions. Consultez [Import D365 F&O Entity](/fr/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) pour la référence complète des champs.

## Comptabilisation des écritures de journal

L'étape **D365 F&O: Post Journal Entry** comptabilise des écritures de journal du grand livre via le pipeline d'écriture ERP partagé de PlaidCloud : soumission à l'action asynchrone de comptabilisation de journal du service personnalisé de D365 F&O, interrogation jusqu'à un état final, puis confirmation avant de signaler une écriture comme comptabilisée. Une correction comptabilise une nouvelle écriture d'extourne, avec débit et crédit inversés, au lieu de modifier l'écriture d'origine. Consultez [D365 F&O: Post Journal Entry](/fr/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) pour la référence des champs, et [Se connecter à Dynamics 365 Finance & Operations](/fr/guides/connections/dynamics-365-fo/) pour la procédure complète de comptabilisation.

## Limitations connues

| Limitation | Ce que cela signifie |
|---|---|
| Le mode synchrone DMF a une latence d'extraction | Une extraction `dmf` attend un job d'export asynchrone, ce qui est nettement plus lent qu'une extraction `odata` de même taille. |
| Le filtrage par dimension dépend de la structure | Une dimension financière qui ne fait pas partie de votre structure de comptes ne peut pas être filtrée côté serveur : limitez-la dans votre workflow après l'extraction. |

## Voir aussi

- [Se connecter à Dynamics 365 Finance & Operations (guide)](/fr/guides/connections/dynamics-365-fo/) — pas à pas : créer la connexion, la tester, importer une entité et comptabiliser un journal.
- [Import D365 F&O Entity](/fr/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/)
- [D365 F&O: Post Journal Entry](/fr/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/)
- [Consulter l'historique de comptabilisation ERP](/fr/guides/connections/erp-post-history/)
