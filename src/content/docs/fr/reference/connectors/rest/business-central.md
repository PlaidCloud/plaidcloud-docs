---
title: Connecteur REST Business Central
description: Configurez une connexion Microsoft Dynamics 365 Business Central dans PlaidCloud avec les informations d'identification client Azure AD pour importer des entités OData et comptabiliser des lignes de journal général.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/business-central.md
---

## Documentation de l'API

L'[API OData v2.0 standard](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) de Business Central documente les entités et les options `$filter`/`$orderby` qu'utilise ce connecteur.

## Fonctionnement de l'authentification

La connexion s'authentifie en tant qu'application via les **informations d'identification client (S2S)** d'Entra ID (Azure AD) : l'ID client et le secret d'un enregistrement d'application sont échangés contre un jeton d'accès à `https://login.microsoftonline.com/<tenant id>/oauth2/v2.0/token`, avec pour portée `https://api.businesscentral.dynamics.com/.default`. Il n'y a aucune connexion interactive. L'enregistrement d'application nécessite des autorisations d'API accordées à Business Central (`API.ReadWrite.All` ou une portée plus restreinte délivrée par votre administrateur).

Chaque requête est limitée à un **environnement** (par exemple `Production` ou un environnement de test) et à une **société** de cet environnement. Les deux sont définis sur la connexion et non choisis à chaque requête.

## Configuration

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| ID client | Texte | L'ID d'application (client) de l'enregistrement d'application Entra. |
| Secret client | Texte | Le secret client de l'enregistrement d'application. Stocké chiffré. |
| ID du locataire | Texte | L'ID de votre locataire Azure AD. |
| Environnement | Texte | Le nom de l'environnement Business Central, par exemple `Production`. |
| Société | Texte | L'ID de la société Business Central sur laquelle cette connexion lit et comptabilise. |

## Entités disponibles à l'import

L'étape **Import Business Central Entity** couvre six entités : `accounts`, `generalLedgerEntries`, `customers`, `vendors`, `items`, `journals`. Chaque extraction prend en charge des filtres côté serveur propres à chaque entité. Consultez [Import Business Central Entity](/fr/reference/workflow-steps/business-central/import-business-central-entity/) pour la référence complète des champs.

`generalLedgerEntries` est en lecture seule et ne contient que des écritures comptabilisées : c'est l'entité à extraire pour une balance générale ou un détail du grand livre, car elle n'inclut jamais une ligne encore présente dans un lot de journal non comptabilisé.

## Comptabilisation des lignes de journal général

L'étape **Business Central Post** crée des lignes dans un lot de journal **existant** et comptabilise ce lot via le pipeline d'écriture ERP partagé de PlaidCloud. Elle vérifie que le lot ne contient que les lignes de cette requête avant la comptabilisation, puis confirme la comptabilisation auprès de `generalLedgerEntries` (et non du lot de journal lui-même). Consultez [Business Central: Post General Journal Lines](/fr/reference/workflow-steps/business-central/business-central-post/) pour la référence des champs, et [Se connecter à Business Central](/fr/guides/connections/business-central/) pour la procédure complète de comptabilisation.

## Limitations connues

| Limitation | Ce que cela signifie |
|---|---|
| Un seul type de document en écriture | Seule la comptabilisation de lignes de journal général est prise en charge. Le flux de documents brouillons (factures de vente/d'achat, Brouillon → Comptabilisé) ne l'est pas : l'action de comptabilisation de ce flux n'est pas précisée dans la documentation publiée de Microsoft. |
| Comptabilisation dans un lot existant uniquement | Ce connecteur ne crée jamais de lot de journal dans Business Central : créez-le d'abord dans Business Central. |
| Comptabilisations simultanées dans le même lot | La protection d'idempotence est définie par numéro de document, et non par lot de journal : deux numéros de document différents comptabilisés simultanément dans le même lot ne sont pas garantis d'être sérialisés. |

## Voir aussi

- [Se connecter à Business Central (guide)](/fr/guides/connections/business-central/) — pas à pas : créer la connexion, la tester, importer une entité et comptabiliser un journal.
- [Import Business Central Entity](/fr/reference/workflow-steps/business-central/import-business-central-entity/)
- [Business Central: Post General Journal Lines](/fr/reference/workflow-steps/business-central/business-central-post/)
- [Consulter l'historique de comptabilisation ERP](/fr/guides/connections/erp-post-history/)
