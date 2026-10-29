---
title: Kafka importieren
description: Lesen Sie die Nachrichten von Apache-Kafka-Topics zwischen zwei Offsets in eine PlaidCloud-Tabelle, eine Zeile pro Nachricht.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-kafka.md
---

## Beschreibung

Liest die Nachrichten eines oder mehrerer Apache-Kafka-Topics in eine Projekttabelle, eine Zeile pro Nachricht. Der Schritt liest einen festen Bereich: von den Start-Offsets bis zu den End-Offsets, wobei `latest` das Ende jeder Partition beim Start des Schritts bedeutet. Nachrichten, die eintreffen, während der Schritt läuft, werden nicht gelesen. Der Schritt erreicht Kafka über eine [Apache-Kafka-Verbindung](/de/reference/connectors/databases/apache-kafka/).

## Quelle und Ziel

| Einstellung | Erforderlich | Funktion |
| --- | --- | --- |
| Kafka-Verbindung | Ja | Die Verbindung, über die gelesen wird. |
| Topics | Eines von beiden | Die zu lesenden Topics, eines pro Zeile. |
| Topic-Muster | Eines von beiden | Ein regulärer Ausdruck, der die zu lesenden Topics auswählt; wird anstelle von **Topics** verwendet. |
| Zieltabelle | Ja | Die Tabelle, in der die Nachrichten landen. |

## Nachrichtenbereich

| Einstellung | Standard | Funktion |
| --- | --- | --- |
| Start-Offsets | `earliest` | `earliest`, `latest` oder JSON, das für jede Partition einen Offset nennt, etwa `{"orders": {"0": 1200, "1": 980}}`. In JSON bedeutet `-2` earliest und `-1` latest. |
| End-Offsets | `latest` | `latest` oder JSON in derselben Form wie die Start-Offsets. |
| Nachrichtenlimit (0 = alle) | `0` | Die höchste Anzahl zu lesender Nachrichten. `0` liest jede Nachricht im Bereich. |
| Leerlauf-Timeout (Sekunden) | `10` | Das Lesen endet, wenn so viele Sekunden lang keine neue Nachricht eintrifft. |
| Zeitlimit (Sekunden) | `10800` | Die längste Dauer, die das Lesen laufen darf. |

Die Offsets akzeptieren Workflow-Variablen in der Schreibweise `{name}`.

## Nachrichtenwert

| Einstellung | Funktion |
| --- | --- |
| Wertformat | **JSON**, **Text** oder **Avro**. |
| Avro-Schema (JSON) | Das Avro-Schema des Nachrichtenwerts. Erforderlich, wenn das Format **Avro** ist. |
| Zusätzliche Consumer-Einstellungen (JSON) | Weitere Kafka-Consumer-Einstellungen als JSON-Objekt, etwa `{"fetch.min.bytes": 1}`. Es werden nur Einstellungen akzeptiert, die PlaidCloud zulässt. |

## Spaltenzuordnung

Ordnen Sie auf der Registerkarte „Zuordnung“ mindestens eine Spalte zu. Eine Spalte liest einen der Teile der Nachricht – `key`, `value`, `topic`, `partition`, `offset`, `timestamp`, `timestamp_type` oder `headers` – oder ein Feld des geparsten Werts über seinen Pfad. Für diesen Schritt gibt es kein **Quelle untersuchen**, geben Sie die Spalten daher von Hand ein.

## Verwandte Themen

- [Kafka exportieren](/de/reference/workflow-steps/export/export-kafka/)
- [Apache-Kafka-Verbindung](/de/reference/connectors/databases/apache-kafka/)
