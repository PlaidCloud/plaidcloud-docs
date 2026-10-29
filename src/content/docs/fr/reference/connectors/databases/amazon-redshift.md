---
title: Amazon Redshift
description: Configurez une connexion de base de données Amazon Redshift dans PlaidCloud pour interroger, importer et exporter des données avec votre entrepôt Redshift.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/amazon-redshift.md
---

**Amazon Redshift** est l'entrepôt de données cloud géré d'AWS, conçu pour les charges de travail analytiques sur de grands jeux de données. Utilisez ce connecteur pour lire et écrire des tables Redshift depuis des workflows PlaidCloud. Le connecteur parle le protocole filaire PostgreSQL ; l'authentification utilise des identifiants de base de données standard ou des identifiants temporaires reposant sur IAM.

## Documentation du fournisseur
Consultez la [documentation Amazon Redshift](https://docs.aws.amazon.com/redshift/) pour les guides et le matériel de référence.

## Configuration

Ces champs apparaissent lors de la création ou de la modification de cette connexion. Le caractère obligatoire ou facultatif dépend des options d'authentification que vous activez.

### Identification

| Champ | Type | Description |
|---|---|---|
| Name | Texte | Nom d'affichage de cette connexion. |
| Alias | Texte (multiligne) | Alias ou notes facultatifs sur la connexion. |
| Is active | Interrupteur | Indique si la connexion est activée. Désactivez-la pour la mettre en pause sans la supprimer. |
| Db read only | Interrupteur | Restreint la connexion aux opérations en lecture seule. |
| Access type | Sélection | Niveau d'accès de cette connexion : lecture seule, écriture seule ou lecture-écriture. |

### Connexion

| Champ | Type | Description |
|---|---|---|
| Db host | Texte | Nom d'hôte ou adresse IP du serveur de base de données. |
| Db port | Nombre | Numéro de port de la connexion à la base de données. |
| Db catalog | Texte | Base de données, catalogue ou schéma auquel se connecter. |

### Authentification

| Champ | Type | Description |
|---|---|---|
| Db user | Texte | Nom d'utilisateur pour l'authentification à la base de données. |
| Use sso | Interrupteur | S'authentifier par authentification unique plutôt que par nom d'utilisateur et mot de passe. |
| Db password | Mot de passe | Mot de passe pour l'authentification à la base de données. |

### SSL / TLS

| Champ | Type | Description |
|---|---|---|
| Use ssl | Interrupteur | Chiffre la connexion avec SSL/TLS. |
| Ssl mode | Sélection | Mode de vérification SSL (par exemple disable, require, verify-ca, verify-full). |
| Ssl auth client cert | Texte (multiligne) | Certificat client (PEM) pour l'authentification TLS mutuelle. |
| Ssl auth client key | Texte (multiligne) | Clé privée du client (PEM) pour l'authentification TLS mutuelle. |
| Ssl auth root cert | Texte (multiligne) | Certificat d'AC racine (PEM) pour vérifier le certificat du serveur. |
| Ssl auth cert revoke | Texte (multiligne) | Liste de révocation de certificats, si votre environnement en utilise une. |

### Tunnel SSH

| Champ | Type | Description |
|---|---|---|
| Use ssh | Interrupteur | Fait passer la connexion par un bastion SSH. |
| Ssh host | Texte | Nom d'hôte du bastion SSH. |
| Ssh port | Nombre | Port du bastion SSH (22 par défaut). |
| Ssh user | Texte | Nom d'utilisateur du bastion SSH. |
| Ssh password | Mot de passe | Mot de passe du bastion SSH (si l'authentification par mot de passe est utilisée). |
| Use ssh cert | Interrupteur | S'authentifie auprès du bastion SSH avec une clé privée plutôt qu'avec un mot de passe. |
| Ssh private key | Texte (multiligne) | Clé privée SSH (PEM) pour l'authentification auprès du bastion. |
| Ssh host key | Texte (multiligne) | Clé d'hôte SSH attendue pour vérifier l'empreinte du bastion. |
