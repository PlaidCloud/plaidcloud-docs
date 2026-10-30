---
title: Connexion Tableau
description: Connectez PlaidCloud à Tableau Server ou Tableau Cloud avec un jeton d'accès personnel afin que les workflows puissent publier des sources de données.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/collaboration/tableau.md
---

Une connexion Tableau contient l'adresse d'un site Tableau Server ou Tableau Cloud et un jeton d'accès personnel. L'étape [Publish to Tableau](/fr/reference/workflow-steps/export/export-to-tableau/) l'utilise pour publier des extraits `.hyper` en tant que sources de données.

## Avant de commencer

Dans Tableau, créez un jeton d'accès personnel pour le compte qui doit publier : choisissez **My Account Settings**, puis **Personal Access Tokens**. Copiez le secret du jeton lorsque Tableau l'affiche, car Tableau ne l'affiche plus ensuite. Le compte doit avoir l'autorisation de publier des sources de données dans le projet dans lequel vous allez publier.

## Créer la connexion

1. Ouvrez **Analyze**, choisissez **Tools → Connexions de données externes**, puis sélectionnez **+ Nouvelle connexion → Tableau**.
2. Saisissez le nom et la description de la connexion.
3. Saisissez les paramètres de la connexion :

| Champ | Valeur à saisir |
| --- | --- |
| **URL du serveur** | L'adresse du serveur ou du pod Tableau Cloud, par exemple `https://prod-useast-a.online.tableau.com`. Un nom d'hôte seul est interprété comme `https`, et une adresse `http` est refusée. |
| **Site** | L'URL de contenu du site, c'est-à-dire la partie de l'adresse du navigateur située après `#/site/`. Laissez vide pour le site par défaut (Default). |
| **Nom du jeton d'accès personnel** | Le nom que vous avez donné au jeton dans Tableau. |
| **Secret du jeton d'accès personnel** | Le secret du jeton. Il est stocké chiffré et s'affiche vide lorsque vous rouvrez la connexion. Laissez-le vide pour conserver le secret enregistré. |

4. Sélectionnez **Créer**.

Le serveur doit être accessible depuis Internet. PlaidCloud ne se connecte pas à un serveur Tableau situé sur un réseau privé.

## Voir aussi

- [Publish to Tableau](/fr/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export](/fr/reference/workflow-steps/export/export-hyper/)
