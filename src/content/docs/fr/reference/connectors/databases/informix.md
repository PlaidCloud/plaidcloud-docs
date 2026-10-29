---
title: IBM Informix
description: Configurez une connexion à une base de données IBM Informix dans PlaidCloud pour interroger, importer et exporter des données avec vos instances Informix.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/informix.md
---

**IBM Informix** est la base de données transactionnelle d'IBM, répandue dans le commerce de détail et les déploiements OLTP. Utilisez ce connecteur pour lire et écrire des tables Informix depuis des workflows PlaidCloud. Un accès réseau au serveur Informix est nécessaire ; le tunnel SSH est pris en charge pour les réseaux non plats.

## Documentation officielle
[Documentation d'IBM Informix](https://www.ibm.com/docs/ar/informix-servers/14.10.0?).

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
| Utiliser le SSO | Interrupteur | S'authentifier par authentification unique (SSO) plutôt que par nom d'utilisateur et mot de passe. |
| Mot de passe de la base | Mot de passe | Mot de passe pour l'authentification à la base de données. |

### SSL / TLS

| Champ | Type | Description |
|---|---|---|
| Utiliser SSL | Interrupteur | Chiffrer la connexion avec SSL/TLS. |
| Mode SSL | Liste de sélection | Mode de vérification SSL (par ex. disable, require, verify-ca, verify-full). |
| Certificat client SSL | Texte (multiligne) | Certificat client (PEM) pour l'authentification TLS mutuelle. |
| Clé client SSL | Texte (multiligne) | Clé privée client (PEM) pour l'authentification TLS mutuelle. |
| Certificat racine SSL | Texte (multiligne) | Certificat d'AC racine (PEM) pour vérifier le certificat du serveur. |
| Révocation de certificat SSL | Texte (multiligne) | Liste de révocation de certificats, si votre environnement en utilise une. |

### Tunnel SSH

| Champ | Type | Description |
|---|---|---|
| Utiliser SSH | Interrupteur | Faire transiter la connexion par un bastion SSH. |
| Hôte SSH | Texte | Nom d'hôte du bastion SSH. |
| Port SSH | Nombre | Port du bastion SSH (22 par défaut). |
| Utilisateur SSH | Texte | Nom d'utilisateur du bastion SSH. |
| Mot de passe SSH | Mot de passe | Mot de passe du bastion SSH (si l'authentification par mot de passe est utilisée). |
| Utiliser un certificat SSH | Interrupteur | S'authentifier auprès du bastion SSH avec une clé privée plutôt qu'un mot de passe. |
| Clé privée SSH | Texte (multiligne) | Clé privée SSH (PEM) pour l'authentification auprès du bastion. |
| Clé d'hôte SSH | Texte (multiligne) | Clé d'hôte SSH attendue pour vérifier l'empreinte du bastion. |
