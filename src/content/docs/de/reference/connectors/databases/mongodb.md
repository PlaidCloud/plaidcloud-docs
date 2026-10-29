---
title: MongoDB
description: Richten Sie in PlaidCloud eine MongoDB-Verbindung ein, um Collections in Tabellen zu lesen und Tabellen als Dokumente zurückzuschreiben.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/mongodb.md
---

**MongoDB** ist eine Dokumentendatenbank. Verwenden Sie diese Verbindung mit [MongoDB importieren](/de/reference/workflow-steps/import/import-mongodb/), um eine Collection oder das Ergebnis einer Aggregation Pipeline in eine Tabelle zu lesen, und mit [MongoDB exportieren](/de/reference/workflow-steps/export/export-mongodb/), um eine Tabelle als Dokumente zurückzuschreiben. Wählen Sie zum Erstellen **MongoDB** als Verbindungstyp.

## Dokumentation des Herstellers
[Die MongoDB-Dokumentation](https://www.mongodb.com/docs/).

## Konfiguration

### MongoDB-Verbindung

| Feld | Erforderlich | Beschreibung |
|---|---|---|
| Host | Ja | Der Hostname des Servers. |
| Use an SRV address (mongodb+srv://, no port) | Nein | Verbindung über eine DNS-Seed-Liste, wie sie MongoDB Atlas verwendet. Der Port wird nicht verwendet. |
| Port | Nein | Der Port des Servers. Standardmäßig `27017`. |
| Standarddatenbank | Nein | Die Datenbank, die ein Schritt verwendet, wenn er keine angibt. |

### Authentifizierungsdaten

| Feld | Beschreibung |
|---|---|
| User | Der Benutzer, mit dem die Verbindung hergestellt wird. |
| Password | Das Passwort des Benutzers (nur schreibbar). |

### Optionen

| Feld | Beschreibung |
|---|---|
| Verbindungsoptionen | MongoDB-URI-Optionen, mit `&` verbunden, etwa `authSource=admin&tls=true`. Es werden nur die Optionen akzeptiert, die PlaidCloud zulässt. Lassen Sie das Feld beim Bearbeiten leer, um die gespeicherten Optionen beizubehalten. |

### TLS

| Feld | Beschreibung |
|---|---|
| CA-Zertifikat (PEM) | Die Zertifizierungsstelle, die die Zertifikate der Server signiert hat, sofern sie nicht öffentlich ist. Lassen Sie das Feld beim Bearbeiten leer, um das gespeicherte Zertifikat beizubehalten. |
