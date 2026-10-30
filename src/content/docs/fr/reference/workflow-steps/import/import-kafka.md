---
title: Importer depuis Kafka
description: Lisez les messages de topics Apache Kafka entre deux offsets dans une table PlaidCloud, avec une ligne par message.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-kafka.md
---

## Description

Lit les messages d'un ou de plusieurs topics Apache Kafka dans une table de projet, avec une ligne par message. L'étape lit une plage fixe : des offsets de début aux offsets de fin, où `latest` désigne la fin de chaque partition au démarrage de l'étape. Les messages qui arrivent pendant l'exécution de l'étape ne sont pas lus. L'étape accède à Kafka via une [connexion Apache Kafka](/fr/reference/connectors/databases/apache-kafka/).

## Source et cible

| Paramètre | Obligatoire | Fonction |
| --- | --- | --- |
| Connexion Kafka | Oui | La connexion à utiliser pour la lecture. |
| Topics | L'un des deux | Les topics à lire, un par ligne. |
| Motif de topics | L'un des deux | Une expression régulière qui sélectionne les topics à lire, utilisée à la place de **Topics**. |
| Table cible | Oui | La table dans laquelle les messages sont enregistrés. |

## Plage de messages

| Paramètre | Par défaut | Fonction |
| --- | --- | --- |
| Offsets de début | `earliest` | `earliest`, `latest`, ou un JSON nommant un offset pour chaque partition, par exemple `{"orders": {"0": 1200, "1": 980}}`. En JSON, `-2` signifie earliest et `-1` latest. |
| Offsets de fin | `latest` | `latest`, ou un JSON de même forme que les offsets de début. |
| Limite de messages (0 = tous) | `0` | Le nombre maximal de messages à lire. `0` lit tous les messages de la plage. |
| Délai d'inactivité (secondes) | `10` | La lecture se termine après ce nombre de secondes sans nouveau message. |
| Limite de durée (secondes) | `10800` | La durée maximale de la lecture. |

Les offsets acceptent des variables de workflow écrites sous la forme `{name}`.

## Valeur du message

| Paramètre | Fonction |
| --- | --- |
| Format de la valeur | **JSON**, **Texte** ou **Avro**. |
| Schéma Avro (JSON) | Le schéma Avro de la valeur du message. Obligatoire lorsque le format est **Avro**. |
| Paramètres supplémentaires du consommateur (JSON) | Paramètres supplémentaires du consommateur Kafka sous forme d'objet JSON, par exemple `{"fetch.min.bytes": 1}`. Seuls les paramètres autorisés par PlaidCloud sont acceptés. |

## Mappage des colonnes

Mappez au moins une colonne dans l'onglet de mappage. Une colonne lit l'un des éléments du message (`key`, `value`, `topic`, `partition`, `offset`, `timestamp`, `timestamp_type` ou `headers`), ou un champ de la valeur analysée à partir de son chemin. Cette étape n'offre pas de bouton **Inspecter la source** ; saisissez donc les colonnes à la main.

## Voir aussi

- [Exporter vers Kafka](/fr/reference/workflow-steps/export/export-kafka/)
- [Connexion Apache Kafka](/fr/reference/connectors/databases/apache-kafka/)
