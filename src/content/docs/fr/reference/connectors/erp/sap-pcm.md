---
title: Connecteur SAP Profitability and Cost Management (PCM)
description: Configurez une connexion SAP Profitability and Cost Management dans PlaidCloud pour intégrer aux workflows les données d'allocation des coûts.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/sap-pcm.md
---

## Documentation officielle
[La documentation héritée de SAP PCM](https://help.sap.com/docs/SAP_PROFITABILITY_AND_COST_MANAGEMENT).

## Configuration

Ces champs apparaissent lorsque vous créez ou modifiez cette connexion. Le caractère obligatoire ou facultatif d'un champ dépend des options d'authentification que vous activez.

### Identification

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| Alias | Texte (multiligne) | Alias ou notes facultatifs sur la connexion. |
| Actif | Interrupteur | Indique si la connexion est activée. Désactivez-la pour la mettre en pause sans la supprimer. |
| Base en lecture seule | Interrupteur | Limiter la connexion aux opérations en lecture seule. |
| Type d'accès | Liste de sélection | Niveau d'accès de cette connexion : lecture seule, écriture seule ou lecture-écriture. |

### Authentification

| Champ | Type | Description |
|---|---|---|
| Utilisateur de la base | Texte | Nom d'utilisateur pour l'authentification à la base de données. |
| Utiliser le SSO | Interrupteur | S'authentifier par authentification unique (SSO) plutôt que par nom d'utilisateur et mot de passe. |
| Mot de passe de la base | Mot de passe | Mot de passe pour l'authentification à la base de données. |
