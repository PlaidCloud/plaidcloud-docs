---
title: Export Kafka
description: Senden Sie jede Zeile einer PlaidCloud-Tabelle als Nachricht an ein Apache-Kafka-Topic.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-kafka.md
---

## Beschreibung

Sendet jede Zeile einer Projekttabelle als eine Nachricht an ein Apache-Kafka-Topic. Eine gesendete Nachricht lässt sich nicht zurücknehmen; wird der Schritt erneut ausgeführt, werden die Zeilen daher erneut gesendet. Der Schritt erreicht Kafka über eine [Apache-Kafka-Verbindung](/de/reference/connectors/databases/apache-kafka/).

## Quelle und Ziel

| Einstellung | Erforderlich | Funktion |
| --- | --- | --- |
| Quelltabelle | Ja | Die Tabelle, die gesendet wird. |
| Kafka-Verbindung | Ja | Die Verbindung, über die gesendet wird. |
| Topic | Ja | Das Topic, an das jede Zeile gesendet wird. |

## Nachricht

| Einstellung | Funktion |
| --- | --- |
| Schlüsselspalte | Die Spalte, deren Wert der Nachrichtenschlüssel ist. Lassen Sie das Feld leer, um Nachrichten ohne Schlüssel zu senden. |
| Wertspalten | Die durch Kommas getrennten Spalten, die den Nachrichtenwert bilden. Lassen Sie das Feld leer, um jede Spalte zu senden. |
| Partitionsspalte | Eine Ganzzahlspalte, die für jede Nachricht die Partition benennt. Lassen Sie das Feld leer, damit Kafka wählt. |
| Wertformat | **JSON**, **Text** oder **Avro**. |
| Avro-Schema (JSON) | Das Avro-Schema des Nachrichtenwerts. Erforderlich, wenn das Format **Avro** ist. |

## Zustellung

| Einstellung | Standard | Funktion |
| --- | --- | --- |
| Zustellungswartezeit (Sekunden) | `60` | Wie lange der Schritt am Ende darauf wartet, dass Kafka jede Nachricht bestätigt. |
| Zeitlimit (Sekunden) | `10800` | Die längste Dauer, die das Senden laufen darf. |
| Zusätzliche Producer-Einstellungen (JSON) | — | Zusätzliche Kafka-Producer-Einstellungen als JSON-Objekt, etwa `{"compression.type": "gzip"}`. Es werden nur Einstellungen akzeptiert, die PlaidCloud erlaubt. |

## Verwandte Themen

- [Kafka importieren](/de/reference/workflow-steps/import/import-kafka/)
- [Apache-Kafka-Verbindung](/de/reference/connectors/databases/apache-kafka/)
