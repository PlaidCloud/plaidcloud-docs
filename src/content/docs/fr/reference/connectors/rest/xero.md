---
title: Connecteur REST Xero
description: Configurez une connexion Xero dans PlaidCloud avec une autorisation OAuth en un clic, importez des entités de l'API Accounting et comptabilisez des écritures manuelles, des factures, des factures fournisseur, des paiements et des avoirs.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/xero.md
---

## Documentation de l'API

La [référence de l'API Accounting](https://developer.xero.com/documentation/api/accounting/overview) de Xero documente les entités, les filtres `where=` et les charges utiles de création utilisés par ce connecteur.

## Fonctionnement de l'authentification

La connexion s'authentifie avec l'autorisation **OAuth 2.0** de Xero. PlaidCloud enregistre lui-même l'application OAuth ; vous n'avez donc ni identifiant client ni secret client à obtenir ou à saisir : vous cliquez sur **Se connecter à Xero**, vous vous connectez à Xero et vous approuvez l'autorisation. PlaidCloud stocke les jetons obtenus sur la connexion et les actualise pour vous, en conservant chaque jeton d'actualisation renouvelé afin qu'une connexion longtemps inactive continue de fonctionner.

Une seule autorisation couvre toutes les organisations Xero pour lesquelles vous l'approuvez. La connexion cible exactement l'une d'elles : le sélecteur **Organisation** liste les organisations renvoyées par l'autorisation, et chaque requête transporte l'identifiant de tenant de cette organisation. Pour lire ou comptabiliser dans une seconde organisation, créez une seconde connexion Xero et choisissez cette organisation.

La société de démonstration (Demo Company) de Xero est une propriété de l'organisation, et non un paramètre de connexion : une organisation de démonstration apparaît dans la liste **Organisation** comme n'importe quelle autre ; une connexion de test est donc une connexion qui pointe vers elle.

## Configuration

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| Se connecter à Xero | Bouton | Lance le flux de connexion et de consentement Xero. |
| Statut de la connexion | Statut | Affiche `Not connected` tant que l'autorisation n'est pas terminée, puis indique le nombre d'organisations qu'elle couvre. |
| Organisation | Sélection | L'organisation Xero dans laquelle cette connexion lit et comptabilise. Alimentée à partir de l'autorisation. |

## Limites de débit

Xero limite chaque organisation à 60 appels par minute et à 5 000 appels par jour, avec un plafond de 5 appels simultanés. PlaidCloud gère les limites par minute et de simultanéité par connexion, de sorte que la limitation d'une organisation ne bloque jamais les appels d'une autre connexion, et respecte l'en-tête `Retry-After` de Xero en cas de réponse limitée. Le plafond quotidien relève de votre gestion : planifiez les extractions volumineuses plutôt que d'en lancer beaucoup à la fois.

## Entités disponibles à l'import

L'étape **Xero : importer une entité** couvre onze entités de l'API Accounting : `accounts`, `contacts`, `invoices`, `credit_notes`, `payments`, `manual_journals`, `bank_transactions`, `items`, `tracking_categories`, `tax_rates` et `currencies`. Chaque extraction accepte un filtre de statut facultatif, une plage de dates et une date limite de modification. Consultez [Xero : importer une entité](/fr/reference/workflow-steps/xero/import-xero-entity/) pour la référence complète des champs.

## Comptabilisation de documents

L'étape **Xero : comptabiliser un document** comptabilise des écritures manuelles, des factures, des factures fournisseur, des paiements et des avoirs via le pipeline d'écriture ERP partagé de PlaidCloud, à partir d'une table d'en-têtes et d'une table de lignes. Consultez [Xero : comptabiliser un document](/fr/reference/workflow-steps/xero/xero-post/) pour la référence des champs, et [Se connecter à Xero](/fr/guides/connections/xero/) pour le guide complet de la comptabilisation.

## Limitations connues

| Limitation | Signification |
|---|---|
| Les écritures manuelles et les paiements ne peuvent pas être recherchés après un résultat ambigu | Les factures, factures fournisseur et avoirs portent un numéro de document que PlaidCloud appose et peut interroger en retour. Le libellé d'une écriture manuelle et la référence d'un paiement ne sont pas interrogeables ; une écriture dont le résultat est incertain est donc placée en quarantaine pour que vous la régliez dans Xero, plutôt que d'être devinée. |
| L'annulation ne couvre que les écritures manuelles et les factures | Une écriture manuelle est annulée par une écriture dont le débit et le crédit sont inversés ; une facture est annulée par un avoir miroir. Les factures fournisseur, les paiements et les avoirs n'ont pas de charge utile d'annulation documentée ; PlaidCloud refuse donc l'annulation plutôt que d'en inventer une. |
| Les filtres sont des champs fixes, pas un langage de requête | L'API de requête de Xero expose, pour chaque entité, un filtre de statut et une plage de dates, et non un langage de filtre ouvert ; l'étape d'import propose donc ces champs plutôt qu'un tableau champ/opérateur/valeur. |
| Une organisation par connexion | Chaque requête transporte un seul identifiant de tenant. Une seconde organisation nécessite une seconde connexion. |

## Voir aussi

- [Se connecter à Xero (guide)](/fr/guides/connections/xero/) : étape par étape, créez la connexion, testez-la, importez une entité et comptabilisez un document.
- [Xero : importer une entité](/fr/reference/workflow-steps/xero/import-xero-entity/)
- [Xero : comptabiliser un document](/fr/reference/workflow-steps/xero/xero-post/)
- [Consulter l'historique des comptabilisations ERP](/fr/guides/connections/erp-post-history/)
