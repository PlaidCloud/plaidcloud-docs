---
title: Connecteur REST Workday
description: Configurez une connexion à l'API REST de Workday dans PlaidCloud pour intégrer vos données de RH, de finance et de planification à vos workflows.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday.md
---

## Documentation de l'API
La [référence de l'API du fournisseur](https://community.workday.com/sites/default/files/file-hosting/restapi/) couvre les points de terminaison de ce connecteur.

## Configuration

Ces champs apparaissent lors de la création ou de la modification de cette connexion. Le caractère obligatoire ou facultatif dépend des options d'authentification que vous activez.

### Identification

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| Alias | Texte (multiligne) | Alias ou remarques facultatifs sur la connexion. |
| Est active | Bascule | Indique si la connexion est activée. Désactivez-la pour la suspendre sans la supprimer. |
| Base de données en lecture seule | Bascule | Limite la connexion aux opérations en lecture seule. |
| Type d'accès | Sélection | Niveau d'accès de cette connexion : lecture seule, écriture seule ou lecture-écriture. |

### Autres

| Champ | Type | Description |
|---|---|---|
| ID client OAuth2 | Texte | — |
| Secret client OAuth2 | Texte | Identifiant secret, stocké chiffré. |
| URL Workday | Texte | Point de terminaison de l'URL. |
| Jeton d'actualisation OAuth2 | Texte | — |
