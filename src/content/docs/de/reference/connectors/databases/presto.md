---
title: Presto
description: Richten Sie in PlaidCloud eine Verbindung zur verteilten Abfrage-Engine Presto ein, um föderierte Abfragen über mehrere Datenquellen auszuführen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/presto.md
---

**Presto** ist eine verteilte SQL-Abfrage-Engine für föderierte Abfragen über mehrere Datenquellen. Mit diesem Connector fragen Sie Presto-Bereitstellungen aus PlaidCloud-Workflows ab. Die Authentifizierung erfolgt je nach Bereitstellung über HTTP Basic Auth oder Kerberos.

## Dokumentation des Herstellers
[Die Presto-Dokumentation](https://prestodb.io/docs/current/).

## Konfiguration

Diese Felder werden beim Erstellen oder Bearbeiten der Verbindung angezeigt. Welche Felder erforderlich oder optional sind, hängt von den aktivierten Authentifizierungsoptionen ab.

### Identifikation

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename dieser Verbindung. |
| Alias | Text (mehrzeilig) | Optionaler Alias oder Notizen zur Verbindung. |
| Is active | Schalter | Gibt an, ob die Verbindung aktiviert ist. Deaktivieren Sie sie, um sie zu pausieren, ohne sie zu löschen. |
| Db read only | Schalter | Beschränkt die Verbindung auf Lesevorgänge. |
| Access type | Auswahl | Zugriffsstufe dieser Verbindung: nur lesen, nur schreiben oder lesen und schreiben. |

### Verbindung

| Feld | Typ | Beschreibung |
|---|---|---|
| Db host | Text | Hostname oder IP-Adresse des Datenbankservers. |
| Db port | Zahl | Portnummer für die Datenbankverbindung. |
| Db catalog | Text | Datenbank, Katalog oder Schema, mit dem die Verbindung hergestellt wird. |

### Authentifizierung

| Feld | Typ | Beschreibung |
|---|---|---|
| Db user | Text | Benutzername für die Datenbankauthentifizierung. |
| Use sso | Schalter | Authentifizierung per Single Sign-on statt mit Benutzername und Passwort. |
| Db password | Passwort | Passwort für die Datenbankauthentifizierung. |

### SSL / TLS

| Feld | Typ | Beschreibung |
|---|---|---|
| Use ssl | Schalter | Verschlüsselt die Verbindung mit SSL/TLS. |
| Ssl mode | Auswahl | Modus der SSL-Überprüfung (z. B. disable, require, verify-ca, verify-full). |
| Ssl auth client cert | Text (mehrzeilig) | Clientzertifikat (PEM) für die gegenseitige TLS-Authentifizierung. |
| Ssl auth client key | Text (mehrzeilig) | Privater Clientschlüssel (PEM) für die gegenseitige TLS-Authentifizierung. |
| Ssl auth root cert | Text (mehrzeilig) | Root-CA-Zertifikat (PEM) zur Überprüfung des Serverzertifikats. |
| Ssl auth cert revoke | Text (mehrzeilig) | Zertifikatssperrliste, falls Ihre Umgebung eine verwendet. |

### SSH-Tunnel

| Feld | Typ | Beschreibung |
|---|---|---|
| Use ssh | Schalter | Leitet die Verbindung über einen SSH-Bastion-Host. |
| Ssh host | Text | Hostname des SSH-Bastion-Hosts. |
| Ssh port | Zahl | Port des SSH-Bastion-Hosts (Standard 22). |
| Ssh user | Text | Benutzername für den SSH-Bastion-Host. |
| Ssh password | Passwort | Passwort für den SSH-Bastion-Host (bei Passwortauthentifizierung). |
| Use ssh cert | Schalter | Authentifiziert sich am SSH-Bastion-Host mit einem privaten Schlüssel statt mit einem Passwort. |
| Ssh private key | Text (mehrzeilig) | Privater SSH-Schlüssel (PEM) für die Authentifizierung am Bastion-Host. |
| Ssh host key | Text (mehrzeilig) | Erwarteter SSH-Hostschlüssel zur Überprüfung des Fingerabdrucks des Bastion-Hosts. |
