---
title: Connecteur REST Ramp
description: Configurez une connexion à l'API REST de Ramp dans PlaidCloud pour intégrer à vos workflows les données de dépenses par carte d'entreprise et de notes de frais.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/ramp.md
---

## Documentation de l'API
La [référence de l'API du fournisseur](https://docs.ramp.com/developer-api/v1) couvre les points de terminaison de ce connecteur.

## Configuration

Ces champs s'affichent lors de la création ou de la modification de cette connexion. Leur caractère obligatoire ou facultatif dépend des options d'authentification que vous activez.

### Identification

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| Alias | Texte (multiligne) | Alias ou remarques facultatifs sur la connexion. |
| Est active | Interrupteur | Indique si la connexion est activée. Désactivez-la pour la mettre en pause sans la supprimer. |
| Base en lecture seule | Interrupteur | Limite la connexion aux opérations en lecture seule. |
| Type d'accès | Sélection | Niveau d'accès de cette connexion : lecture seule, écriture seule ou lecture-écriture. |

### Autres

| Champ | Type | Description |
|---|---|---|
| ID client OAuth2 | Texte | — |
| Secret client OAuth2 | Texte | Identifiant secret, stocké chiffré. |
| Portée Ramp | Texte | — |
