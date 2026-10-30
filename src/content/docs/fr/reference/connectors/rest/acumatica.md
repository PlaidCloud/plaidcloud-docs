---
title: Connecteur REST Acumatica
description: Configurez une connexion à l'API REST contractuelle d'Acumatica dans PlaidCloud pour importer des données de base et transactionnelles et comptabiliser des transactions de journal, des factures, des factures fournisseur et des paiements.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/acumatica.md
---

## Documentation de l'API

L'[API REST contractuelle](https://help.acumatica.com/Help?ScreenId=ShowWiki&pageid=e0dea52d-0339-4f34-a6c0-9615ce6a25c2) d'Acumatica documente les points de terminaison et les options de requête qu'utilise ce connecteur.

## Fonctionnement de l'authentification

La connexion est **basée sur une session** : PlaidCloud se connecte une seule fois par unité de travail délimitée (`POST <instance>/entity/auth/login` avec votre nom d'utilisateur, votre mot de passe, la société et, éventuellement, la succursale), réutilise le cookie de session obtenu pour chaque appel de cette unité, puis se déconnecte une fois terminé. Il ne s'agit pas d'un flux par jeton Bearer ni OAuth : les sessions comptent dans la limite de sessions simultanées de votre licence Acumatica, que les instances d'essai et d'entrée de gamme peuvent plafonner à 2 ; évitez donc d'exécuter de nombreuses étapes Acumatica en parallèle sur une même connexion.

## Configuration

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| URL de base de l'instance | Texte | URL de votre instance Acumatica, par exemple `https://yourcompany.acumatica.com`. |
| Nom du point de terminaison | Texte | Nom du point de terminaison contractuel. `Default`, sauf si un point de terminaison personnalisé a été publié. |
| Version du point de terminaison | Texte | Facultatif, par exemple `25.200.001`. Laissez vide pour utiliser la dernière version publiée du point de terminaison. |
| Société / locataire | Texte | L'ID exact de la société Acumatica à laquelle cette connexion se connecte. |
| Succursale | Texte | Facultatif. Laissez vide pour utiliser la succursale par défaut de l'utilisateur de connexion. |
| Nom d'utilisateur | Texte | L'identifiant de connexion de l'utilisateur d'API PlaidCloud. |
| Mot de passe | Texte | Le mot de passe de l'utilisateur d'API PlaidCloud. Stocké chiffré. |

## Entités disponibles à l'import

L'étape **Import Acumatica Entity** couvre 18 entités contractuelles :

**Données de base et de référence** — `account`, `subaccount`, `ledger`, `financial_period`, `branch`, `currency`, `currency_rate`, `customer`, `vendor`, `stock_item`, `warehouse`, `employee`, `tax_category`, `project`

**Données transactionnelles** — `sales_invoice`, `bill`, `sales_order`, `shipment`

Chaque extraction prend en charge un interrupteur `Active Only`, une date limite `Updated After` et des filtres côté serveur propres à chaque entité. Consultez [Import Acumatica Entity](/fr/reference/workflow-steps/acumatica/import-acumatica-entity/) pour la référence complète des champs.

## Comptabilisation de documents

L'étape **Acumatica Post** comptabilise les documents **JournalTransaction**, **SalesInvoice**, **Fact.** et **Paiements** via le pipeline d'écriture ERP partagé de PlaidCloud : création en attente (Hold), libération (une action asynchrone), puis confirmation de la libération avant de signaler un document comme comptabilisé. Consultez [Acumatica: Post Documents](/fr/reference/workflow-steps/acumatica/acumatica-post/) pour la référence des champs, et [Se connecter à Acumatica](/fr/guides/connections/acumatica/) pour la procédure complète de comptabilisation.

## Limitations connues

| Limitation | Ce que cela signifie |
|---|---|
| Lectures dépendantes des GI non couvertes | La balance générale, le détail des transactions du grand livre, les stocks disponibles, les budgets et les données intersociétés se trouvent derrière les requêtes génériques (Generic Inquiries, GI) d'Acumatica, et non dans les 18 entités contractuelles ci-dessus. Créez la GI dans Acumatica et extrayez-la avec une [connexion REST générique](/fr/reference/connectors/rest/generic-rest/). |
| Pas de clé d'idempotence native en écriture | L'API d'écriture d'Acumatica, basée sur PUT, n'a pas de champ d'idempotence : la réservation du registre propre à PlaidCloud est la seule protection contre une double comptabilisation. |
| Extourne manuelle | Aucun type de document ne dispose d'une action d'annulation ou d'extourne documentée. Un document comptabilisé ne peut pas être extourné depuis PlaidCloud : corrigez-le directement dans Acumatica. |
| Pas de champ de corrélation pour les paiements | Acumatica n'expose aucun champ documenté permettant de corréler un paiement à la requête de PlaidCloud après un résultat ambigu : un paiement en doute est mis en quarantaine pour résolution manuelle. |
| Le filtrage des lignes n'est pas côté serveur | Les filtres de type `$filter` portent sur les champs de l'entité et de l'en-tête, pas sur les dimensions des lignes d'un document (par exemple un centre de coûts au niveau de la ligne). Limitez les lignes dans votre workflow après l'extraction. |

## Voir aussi

- [Se connecter à Acumatica (guide)](/fr/guides/connections/acumatica/) — pas à pas : créer la connexion, la tester, importer une entité et comptabiliser un lot.
- [Import Acumatica Entity](/fr/reference/workflow-steps/acumatica/import-acumatica-entity/)
- [Acumatica: Post Documents](/fr/reference/workflow-steps/acumatica/acumatica-post/)
- [Consulter l'historique de comptabilisation ERP](/fr/guides/connections/erp-post-history/)
