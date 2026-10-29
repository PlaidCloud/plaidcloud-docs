---
title: Connecteur REST Stripe
description: Configurez une connexion à l'API REST de Stripe dans PlaidCloud pour intégrer à vos workflows les données de traitement des paiements et les données financières.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/stripe.md
---

## Documentation de l'API
La [référence de l'API du fournisseur](https://docs.stripe.com/api) couvre les points de terminaison de ce connecteur.

## Configuration

Ces champs s'affichent lors de la création ou de la modification de cette connexion. Leur caractère obligatoire ou facultatif dépend des options d'authentification que vous activez.

### Identification

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| Alias | Texte (multiligne) | Alias ou remarques facultatifs sur la connexion. |
| Est active | Interrupteur | Indique si la connexion est activée. Désactivez-la pour la mettre en pause sans la supprimer. |

### Autres

| Champ | Type | Description |
|---|---|---|
| Hôte | Texte | — |
| Type d'authentification | Sélection | — |
| Activer la vérification SSL | Interrupteur | — |
| Suivre les redirections | Interrupteur | — |
| Redirection : suivre HTTP | Interrupteur | — |
| Redirection : suivre l'authentification | Interrupteur | — |
| Redirection : supprimer le referer | Interrupteur | — |
| HTTP strict | Interrupteur | — |
| Encoder l'URL | Interrupteur | Point de terminaison de l'URL. |
| Désactiver le stockage des cookies | Interrupteur | — |
| Chiffrement du serveur | Interrupteur | — |
| Nombre maximal de redirections | Nombre | — |
| Point de terminaison de test | Texte | — |
| Méthode de test | Sélection | — |
