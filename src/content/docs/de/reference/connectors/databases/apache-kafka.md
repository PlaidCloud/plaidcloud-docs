---
title: Apache Kafka
description: Richten Sie in PlaidCloud eine Apache-Kafka-Verbindung ein, um Topic-Nachrichten in Tabellen zu lesen und Tabellenzeilen als Nachrichten zu senden.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/apache-kafka.md
---

**Apache Kafka** ist eine verteilte Event-Streaming-Plattform. Verwenden Sie diese Verbindung mit dem Schritt [Kafka importieren](/de/reference/workflow-steps/import/import-kafka/), um die Nachrichten von Topics in eine Tabelle zu lesen, und mit dem Schritt [Kafka exportieren](/de/reference/workflow-steps/export/export-kafka/), um jede Zeile einer Tabelle als Nachricht zu senden. Wählen Sie zum Erstellen einer Verbindung **Apache Kafka** als Verbindungstyp.

## Dokumentation des Anbieters
[Die Apache-Kafka-Dokumentation](https://kafka.apache.org/documentation/).

## Konfiguration

### Kafka-Verbindung

| Feld | Erforderlich | Beschreibung |
|---|---|---|
| Broker | Ja | Die Broker, zu denen eine Verbindung hergestellt wird, durch Kommas getrennt, etwa `broker1:9092,broker2:9092`. |
| Sicherheitsprotokoll | Nein | `PLAINTEXT` (Standard), `SSL`, `SASL_PLAINTEXT` oder `SASL_SSL`. |
| Sitzungs-Timeout (ms) | Nein | Wie lange die Broker ohne Rückmeldung von PlaidCloud warten, bevor sie es aus der Consumer-Gruppe entfernen. Mindestens 1000. |

### SASL-Anmeldedaten

Wird verwendet, wenn das Sicherheitsprotokoll `SASL_PLAINTEXT` oder `SASL_SSL` ist.

| Feld | Beschreibung |
|---|---|
| SASL-Mechanismus | `PLAIN` (Standard), `SCRAM-SHA-256`, `SCRAM-SHA-512` oder `OAUTHBEARER`. Kerberos (`GSSAPI`) ist nicht verfügbar. |
| Benutzer | Der Benutzer, als der die Verbindung hergestellt wird, für `PLAIN` und `SCRAM`. |
| Passwort | Das Passwort des Benutzers (nur schreibbar), für `PLAIN` und `SCRAM`. |

### OAuth (OAUTHBEARER)

Wird verwendet, wenn der SASL-Mechanismus `OAUTHBEARER` ist. PlaidCloud ruft sein Token mit dem OAuth-Client-Credentials-Grant von Ihrem Identitätsanbieter ab und ruft ein neues ab, wenn es abläuft.

| Feld | Beschreibung |
|---|---|
| URL des Token-Endpunkts | Der Token-Endpunkt des Identitätsanbieters. Er muss eine `https`-Adresse im öffentlichen Internet sein. |
| Client-ID | Der Client, als der das Token angefordert wird. Erforderlich. |
| Client-Secret | Das Secret des Clients (nur schreibbar). Erforderlich. |
| Scope | Der anzufordernde Scope, wenn Ihr Anbieter einen benötigt. |
| SASL-Erweiterungen | Optionale `key=value`-Paare, durch Kommas getrennt, die mit dem Token gesendet werden, etwa `logicalCluster` und `identityPoolId`, die Confluent Cloud verlangt. |

### TLS

| Feld | Beschreibung |
|---|---|
| CA-Zertifikat (PEM) | Die Zertifizierungsstelle, die die Zertifikate der Broker signiert hat, sofern sie nicht öffentlich ist. Lassen Sie das Feld beim Bearbeiten leer, um das gespeicherte Zertifikat beizubehalten. |
