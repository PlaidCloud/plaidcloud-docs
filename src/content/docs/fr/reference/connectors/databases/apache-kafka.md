---
title: Apache Kafka
description: Configurez une connexion Apache Kafka dans PlaidCloud pour lire les messages de topics dans des tables et envoyer des lignes de table sous forme de messages.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/apache-kafka.md
---

**Apache Kafka** est une plateforme distribuée de streaming d'événements. Utilisez cette connexion avec [Importer depuis Kafka](/fr/reference/workflow-steps/import/import-kafka/) pour lire les messages de topics dans une table, et avec [Exporter vers Kafka](/fr/reference/workflow-steps/export/export-kafka/) pour envoyer chaque ligne d'une table sous forme de message. Pour en créer une, choisissez **Apache Kafka** comme type de connexion.

## Documentation en amont
[Documentation d'Apache Kafka](https://kafka.apache.org/documentation/).

## Configuration

### Connexion Kafka

| Champ | Obligatoire | Description |
|---|---|---|
| Brokers | Oui | Les brokers auxquels se connecter, séparés par des virgules, par exemple `broker1:9092,broker2:9092`. |
| Protocole de sécurité | Non | `PLAINTEXT` (valeur par défaut), `SSL`, `SASL_PLAINTEXT` ou `SASL_SSL`. |
| Délai d'expiration de session (ms) | Non | Durée pendant laquelle les brokers attendent sans nouvelles de PlaidCloud avant de le retirer du groupe de consommateurs. Au moins 1000. |

### Identifiants SASL

Utilisés lorsque le protocole de sécurité est `SASL_PLAINTEXT` ou `SASL_SSL`.

| Champ | Description |
|---|---|
| Mécanisme SASL | `PLAIN` (valeur par défaut), `SCRAM-SHA-256`, `SCRAM-SHA-512` ou `OAUTHBEARER`. Kerberos (`GSSAPI`) n'est pas disponible. |
| Utilisateur | L'utilisateur avec lequel se connecter, pour `PLAIN` et `SCRAM`. |
| Mot de passe | Le mot de passe de l'utilisateur (en écriture seule), pour `PLAIN` et `SCRAM`. |

### OAuth (OAUTHBEARER)

Utilisé lorsque le mécanisme SASL est `OAUTHBEARER`. PlaidCloud obtient son jeton auprès de votre fournisseur d'identité avec le flux OAuth d'identifiants client (client-credentials), et en obtient un nouveau à son expiration.

| Champ | Description |
|---|---|
| URL du point de terminaison du jeton | Le point de terminaison de jeton du fournisseur d'identité. Il doit s'agir d'une adresse `https` sur Internet public. |
| ID client | Le client au nom duquel demander le jeton. Obligatoire. |
| Secret client | Le secret du client (en écriture seule). Obligatoire. |
| Portée | La portée à demander, lorsque votre fournisseur en exige une. |
| Extensions SASL | Paires `key=value` facultatives, séparées par des virgules, envoyées avec le jeton, comme les valeurs `logicalCluster` et `identityPoolId` que demande Confluent Cloud. |

### TLS

| Champ | Description |
|---|---|
| Certificat d'AC (PEM) | L'autorité de certification qui a signé les certificats des brokers, lorsqu'elle n'est pas publique. Laissez le champ vide lors d'une modification pour conserver le certificat enregistré. |
