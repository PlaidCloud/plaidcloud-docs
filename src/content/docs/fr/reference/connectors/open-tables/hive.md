---
title: Format de table ouvert Apache Hive
description: Configurez une connexion à un catalogue Apache Hive dans PlaidCloud pour interroger des formats de table ouverts via le service PlaidCloud Lakehouse.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/open-tables/hive.md
---

## Documentation du catalogue
[Documentation d'Apache Hive](https://hive.apache.org/docs/latest/).

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

### Connexion

| Champ | Type | Description |
|---|---|---|
| Hôte de la base | Texte | Nom d'hôte ou adresse IP du serveur de base de données. |
| Port de la base | Nombre | Numéro de port de la connexion à la base de données. |
| Catalogue de la base | Texte | Base de données, catalogue ou schéma auquel se connecter. |

### Authentification

| Champ | Type | Description |
|---|---|---|
| Utilisateur de la base | Texte | Nom d'utilisateur pour l'authentification à la base de données. |
| Utiliser le SSO | Interrupteur | S'authentifier par authentification unique (SSO) plutôt qu'avec un nom d'utilisateur et un mot de passe. |
| Mot de passe de la base | Mot de passe | Mot de passe pour l'authentification à la base de données. |

### SSL / TLS

| Champ | Type | Description |
|---|---|---|
| Utiliser SSL | Interrupteur | Chiffre la connexion avec SSL/TLS. |
| Mode SSL | Sélection | Mode de vérification SSL (p. ex. disable, require, verify-ca, verify-full). |
| Certificat client d'authentification SSL | Texte (multiligne) | Certificat client (PEM) pour l'authentification TLS mutuelle. |
| Clé client d'authentification SSL | Texte (multiligne) | Clé privée client (PEM) pour l'authentification TLS mutuelle. |
| Certificat d'AC racine d'authentification SSL | Texte (multiligne) | Certificat d'AC racine (PEM) pour vérifier le certificat du serveur. |
| Révocation des certificats d'authentification SSL | Texte (multiligne) | Liste de révocation de certificats, si votre environnement en utilise une. |

### Tunnel SSH

| Champ | Type | Description |
|---|---|---|
| Utiliser SSH | Interrupteur | Fait passer la connexion par un bastion SSH. |
| Hôte SSH | Texte | Nom d'hôte du bastion SSH. |
| Port SSH | Nombre | Port du bastion SSH (22 par défaut). |
| Utilisateur SSH | Texte | Nom d'utilisateur du bastion SSH. |
| Mot de passe SSH | Mot de passe | Mot de passe du bastion SSH (si l'authentification par mot de passe est utilisée). |
| Utiliser un certificat SSH | Interrupteur | S'authentifier auprès du bastion SSH avec une clé privée plutôt qu'avec un mot de passe. |
| Clé privée SSH | Texte (multiligne) | Clé privée SSH (PEM) pour l'authentification auprès du bastion. |
| Clé d'hôte SSH | Texte (multiligne) | Clé d'hôte SSH attendue pour vérifier l'empreinte du bastion. |
