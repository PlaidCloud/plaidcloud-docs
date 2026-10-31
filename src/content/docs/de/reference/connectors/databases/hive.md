---
title: Apache Hive
description: Richten Sie in PlaidCloud eine Apache-Hive-Data-Lake-Verbindung ein, um große, in Hadoop-Ökosystemen gespeicherte Datenmengen abzufragen und zu integrieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/hive.md
---

**Apache Hive** ist die SQL-Schicht über verteiltem Speicher im Hadoop-Stil, verbreitet in älteren Data-Lake-Bereitstellungen. Verwenden Sie diesen Konnektor, um Hive-Tabellen zu lesen und zu schreiben. Die Authentifizierung hängt von der Bereitstellung ab — gängige Modi sind LDAP, Kerberos oder keine Authentifizierung in internen Netzwerken; prüfen Sie Ihre Hive-Metastore-Konfiguration.

## Dokumentation des Anbieters
[Apache-Hive-Dokumentation](https://hive.apache.org/docs/latest/).

## Konfiguration

Diese Felder erscheinen beim Erstellen oder Bearbeiten dieser Verbindung. Ob sie erforderlich oder optional sind, hängt von den aktivierten Authentifizierungsoptionen ab.

### Identifikation

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename dieser Verbindung. |
| Alias | Text (mehrzeilig) | Optionaler Alias oder Notizen zur Verbindung. |
| Ist aktiv | Schalter | Ob die Verbindung aktiviert ist. Deaktivieren Sie sie, um sie zu pausieren, ohne sie zu löschen. |
| DB schreibgeschützt | Schalter | Beschränkt die Verbindung auf Lesevorgänge. |
| Zugriffstyp | Auswahl | Zugriffsstufe für diese Verbindung: nur lesen, nur schreiben oder lesen und schreiben. |

### Verbindung

| Feld | Typ | Beschreibung |
|---|---|---|
| DB-Host | Text | Hostname oder IP-Adresse des Datenbankservers. |
| DB-Port | Zahl | Portnummer für die Datenbankverbindung. |
| DB-Katalog | Text | Datenbank, Katalog oder Schema, zu dem eine Verbindung hergestellt wird. |

### Authentifizierung

| Feld | Typ | Beschreibung |
|---|---|---|
| DB-Benutzer | Text | Benutzername für die Datenbankauthentifizierung. |
| SSO verwenden | Schalter | Authentifizierung per Single Sign-on statt mit Benutzername und Passwort. |
| DB-Passwort | Passwort | Passwort für die Datenbankauthentifizierung. |

### SSL / TLS

| Feld | Typ | Beschreibung |
|---|---|---|
| SSL verwenden | Schalter | Verschlüsselt die Verbindung mit SSL/TLS. |
| SSL-Modus | Auswahl | SSL-Prüfmodus (z. B. disable, require, verify-ca, verify-full). |
| SSL-Client-Zertifikat | Text (mehrzeilig) | Client-Zertifikat (PEM) für die gegenseitige TLS-Authentifizierung. |
| SSL-Client-Schlüssel | Text (mehrzeilig) | Privater Client-Schlüssel (PEM) für die gegenseitige TLS-Authentifizierung. |
| SSL-Stammzertifikat | Text (mehrzeilig) | Root-CA-Zertifikat (PEM) zur Prüfung des Serverzertifikats. |
| SSL-Zertifikatssperrliste | Text (mehrzeilig) | Zertifikatssperrliste, falls Ihre Umgebung eine verwendet. |

### SSH-Tunnel

| Feld | Typ | Beschreibung |
|---|---|---|
| SSH verwenden | Schalter | Leitet die Verbindung über einen SSH-Bastion-Host durch einen Tunnel. |
| SSH-Host | Text | Hostname des SSH-Bastion-Hosts. |
| SSH-Port | Zahl | Port des SSH-Bastion-Hosts (Standard 22). |
| SSH-Benutzer | Text | Benutzername für den SSH-Bastion-Host. |
| SSH-Passwort | Passwort | Passwort für den SSH-Bastion-Host (bei Passwortauthentifizierung). |
| SSH-Zertifikat verwenden | Schalter | Authentifiziert sich am SSH-Bastion-Host mit einem privaten Schlüssel statt mit einem Passwort. |
| Privater SSH-Schlüssel | Text (mehrzeilig) | Privater SSH-Schlüssel (PEM) für die Authentifizierung am Bastion-Host. |
| SSH-Host-Schlüssel | Text (mehrzeilig) | Erwarteter SSH-Host-Schlüssel zur Prüfung des Fingerabdrucks des Bastion-Hosts. |
