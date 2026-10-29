---
title: Connecteur REST Quickbooks
description: Configurez une connexion à l'API REST de QuickBooks dans PlaidCloud pour intégrer des données comptables et financières à vos workflows d'analyse.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/quickbooks.md
---

## Documentation de l'API
La [référence de l'API du fournisseur](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api) couvre les points de terminaison de ce connecteur.

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
