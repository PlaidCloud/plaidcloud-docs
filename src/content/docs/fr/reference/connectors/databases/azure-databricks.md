---
title: Azure Databricks
description: Configurez une connexion Azure Databricks dans PlaidCloud pour intégrer à vos workflows des analyses basées sur Spark et des données de lakehouse.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/azure-databricks.md
---

**Azure Databricks** associe Apache Spark, Delta Lake et un environnement de notebooks géré sur Microsoft Azure. Utilisez ce connecteur pour lire et écrire des tables dans un espace de travail Databricks depuis des workflows PlaidCloud. L'authentification utilise un jeton d'accès personnel ou un principal de service ; l'URL de l'espace de travail et le chemin HTTP identifient l'entrepôt SQL ciblé.

## Documentation en amont
[Documentation d'Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/).

## Configuration

Ces champs apparaissent lors de la création ou de la modification de cette connexion. Le caractère obligatoire ou facultatif dépend des options d'authentification que vous activez.

### Identification

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| Alias | Texte (multiligne) | Alias facultatif ou remarques sur la connexion. |
| Actif | Interrupteur | Indique si la connexion est activée. Désactivez-la pour la mettre en pause sans la supprimer. |
| Base de données en lecture seule | Interrupteur | Limite la connexion aux opérations en lecture seule. |
| Type d'accès | Liste de sélection | Niveau d'accès de cette connexion : lecture seule, écriture seule ou lecture-écriture. |

### Connexion

| Champ | Type | Description |
|---|---|---|
| Hôte de la base de données | Texte | Nom d'hôte ou adresse IP du serveur de base de données. |
| Catalogue de la base de données | Texte | Base de données, catalogue ou schéma auquel se connecter. |
| Schéma de la base de données | Texte | Nom du schéma au sein de la base de données. |

### Authentification

| Champ | Type | Description |
|---|---|---|
| Utilisateur de la base de données | Texte | Nom d'utilisateur pour l'authentification à la base de données. |
| Utiliser l'authentification unique | Interrupteur | S'authentifier par authentification unique plutôt qu'avec un nom d'utilisateur et un mot de passe. |
| Mot de passe de la base de données | Mot de passe | Mot de passe pour l'authentification à la base de données. |

### SSL / TLS

| Champ | Type | Description |
|---|---|---|
| Utiliser SSL | Interrupteur | Chiffre la connexion avec SSL/TLS. |
| Mode SSL | Liste de sélection | Mode de vérification SSL (par exemple : disable, require, verify-ca, verify-full). |
| Certificat client d'authentification SSL | Texte (multiligne) | Certificat client (PEM) pour l'authentification TLS mutuelle. |
| Clé client d'authentification SSL | Texte (multiligne) | Clé privée du client (PEM) pour l'authentification TLS mutuelle. |
| Certificat racine d'authentification SSL | Texte (multiligne) | Certificat d'AC racine (PEM) pour vérifier le certificat du serveur. |
| Révocation de certificat d'authentification SSL | Texte (multiligne) | Liste de révocation de certificats, si votre environnement en utilise une. |

### Tunnel SSH

| Champ | Type | Description |
|---|---|---|
| Utiliser SSH | Interrupteur | Fait transiter la connexion par un bastion SSH. |
| Hôte SSH | Texte | Nom d'hôte du bastion SSH. |
| Port SSH | Nombre | Port du bastion SSH (22 par défaut). |
| Utilisateur SSH | Texte | Nom d'utilisateur du bastion SSH. |
| Mot de passe SSH | Mot de passe | Mot de passe du bastion SSH (si l'authentification par mot de passe est utilisée). |
| Utiliser un certificat SSH | Interrupteur | S'authentifier auprès du bastion SSH avec une clé privée plutôt qu'avec un mot de passe. |
| Clé privée SSH | Texte (multiligne) | Clé privée SSH (PEM) pour l'authentification auprès du bastion. |
| Clé d'hôte SSH | Texte (multiligne) | Clé d'hôte SSH attendue pour la vérification de l'empreinte du bastion. |

### Autres

| Champ | Type | Description |
|---|---|---|
| Chemin HTTP | Texte | — |
