---
title: Connecteur REST MuleSoft
description: Connectez PlaidCloud à une passerelle MuleSoft Anypoint et joignez la définition de l'API pour que les étapes de workflow puissent lister ses points de terminaison.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/mulesoft.md
---

MuleSoft Anypoint est une passerelle d'API : elle expose tous les services que votre organisation a publiés derrière elle, à une adresse propre à votre déploiement. Contrairement à un connecteur conçu pour un seul service, une connexion MuleSoft ne connaît donc pas ses propres points de terminaison : c'est à vous d'indiquer où se trouvent l'API et sa définition.

## Documentation de l'API

La documentation de l'API pour cette connexion est celle des services que votre passerelle expose.

## Configuration

MuleSoft utilise le même formulaire que la [connexion REST générique](/fr/reference/connectors/rest/generic-rest/) : les mêmes quatre onglets, les mêmes champs, le même comportement partout. Deux champs comptent le plus ici :

- **Hôte ou adresse IP** — l'adresse de votre passerelle Anypoint. Il n'y a pas de valeur par défaut, car une adresse MuleSoft est propre à votre déploiement.
- **Type d'authentification** — celui de `None`, `Basic`, `API Key`, `Bearer Token` ou `OAuth 2.0` qu'attend votre passerelle. Rien n'est présumé à votre place.

## Lister les points de terminaison dans un workflow

La passerelle n'ayant pas de liste de points de terminaison intégrée, joignez à la connexion la définition OpenAPI 3.x ou Swagger 2.0 de votre API sous **Définition de l'API**, soit l'adresse à laquelle elle est publiée, soit un fichier `.json` ou `.yaml` stocké dans un compte de documents. Consultez [Définition de l'API](/fr/reference/connectors/rest/generic-rest/#définition-de-lapi) pour les champs.

Une [étape Requête REST](/fr/guides/workflows/rest-request-step/) qui utilise cette connexion peut alors définir **Source du point de terminaison** sur **À partir de la définition d'API de la connexion** et choisir **Charger le catalogue** pour sélectionner parmi les points de terminaison de l'API, au lieu de saisir chaque chemin à la main.

## Voir aussi

- [Connexion REST générique](/fr/reference/connectors/rest/generic-rest/) — la référence complète des champs de ce formulaire.
- [Créer et gérer une connexion](/fr/guides/connections/create-connection/)
- [Étape de workflow Requête REST](/fr/guides/workflows/rest-request-step/)
