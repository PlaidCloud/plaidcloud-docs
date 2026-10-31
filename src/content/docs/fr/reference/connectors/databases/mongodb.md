---
title: MongoDB
description: Configurez une connexion MongoDB dans PlaidCloud pour lire des collections dans des tables et réécrire des tables sous forme de documents.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/mongodb.md
---

**MongoDB** est une base de données documentaire. Utilisez cette connexion avec [Importer depuis MongoDB](/fr/reference/workflow-steps/import/import-mongodb/) pour lire une collection, ou le résultat d'un pipeline d'agrégation, dans une table, et avec [Exporter vers MongoDB](/fr/reference/workflow-steps/export/export-mongodb/) pour réécrire une table sous forme de documents. Pour en créer une, choisissez **MongoDB** comme type de connexion.

## Documentation officielle
[La documentation de MongoDB](https://www.mongodb.com/docs/).

## Configuration

### Connexion MongoDB

| Champ | Obligatoire | Description |
|---|---|---|
| Hôte | Oui | Nom d'hôte du serveur. |
| Utiliser une adresse SRV (mongodb+srv://, sans port) | Non | Se connecter via une liste de seeds DNS, comme le fait MongoDB Atlas. Le port n'est pas utilisé. |
| Port | Non | Port du serveur. La valeur par défaut est `27017`. |
| Base de données par défaut | Non | Base de données qu'une étape utilise lorsqu'elle n'en nomme aucune. |

### Identifiants d'authentification

| Champ | Description |
|---|---|
| Utilisateur | Utilisateur avec lequel se connecter. |
| Mot de passe | Mot de passe de l'utilisateur (en écriture seule). |

### Options

| Champ | Description |
|---|---|
| Options de connexion | Options d'URI MongoDB jointes par `&`, par exemple `authSource=admin&tls=true`. Seules les options autorisées par PlaidCloud sont acceptées. Laissez le champ vide lors d'une modification pour conserver les options enregistrées. |

### TLS

| Champ | Description |
|---|---|
| Certificat d'AC (PEM) | Autorité de certification qui a signé les certificats des serveurs, lorsqu'elle n'est pas publique. Laissez le champ vide lors d'une modification pour conserver le certificat enregistré. |
