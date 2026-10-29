---
title: Exporter vers Kafka
description: Envoyez chaque ligne d'une table PlaidCloud vers un topic Apache Kafka sous forme de message.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-kafka.md
---

## Description

Envoie chaque ligne d'une table de projet vers un topic Apache Kafka sous forme d'un message. Un message envoyé ne peut pas être rappelé ; réexécuter l'étape renvoie donc les lignes. L'étape accède à Kafka via une [connexion Apache Kafka](/fr/reference/connectors/databases/apache-kafka/).

## Source et cible

| Paramètre | Obligatoire | Rôle |
| --- | --- | --- |
| Table source | Oui | La table à envoyer. |
| Connexion Kafka | Oui | La connexion par laquelle envoyer. |
| Topic | Oui | Le topic vers lequel chaque ligne est envoyée. |

## Message

| Paramètre | Rôle |
| --- | --- |
| Colonne de clé | La colonne dont la valeur est la clé du message. Laissez vide pour envoyer les messages sans clé. |
| Colonnes de valeur | Les colonnes, séparées par des virgules, qui composent la valeur du message. Laissez vide pour envoyer toutes les colonnes. |
| Colonne de partition | Une colonne entière qui désigne la partition de chaque message. Laissez vide pour laisser Kafka choisir. |
| Format de la valeur | **JSON**, **Texte** ou **Avro**. |
| Schéma Avro (JSON) | Le schéma Avro de la valeur du message. Obligatoire lorsque le format est **Avro**. |

## Livraison

| Paramètre | Valeur par défaut | Rôle |
| --- | --- | --- |
| Délai d'attente de livraison (secondes) | `60` | La durée pendant laquelle l'étape attend à la fin que Kafka confirme chaque message. |
| Limite de durée (secondes) | `10800` | La durée maximale de l'envoi. |
| Paramètres supplémentaires du producteur (JSON) | — | Paramètres supplémentaires du producteur Kafka sous forme d'objet JSON, comme `{"compression.type": "gzip"}`. Seuls les paramètres autorisés par PlaidCloud sont acceptés. |

## Voir aussi

- [Importer depuis Kafka](/fr/reference/workflow-steps/import/import-kafka/)
- [Connexion Apache Kafka](/fr/reference/connectors/databases/apache-kafka/)
