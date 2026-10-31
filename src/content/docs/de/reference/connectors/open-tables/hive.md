---
title: Apache-Hive-Format für offene Tabellen
description: Richten Sie in PlaidCloud eine Apache-Hive-Katalogverbindung für Abfragen offener Tabellenformate über den Dienst PlaidCloud Lakehouse ein.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/open-tables/hive.md
---

## Katalogdokumentation
[Apache-Hive-Dokumentation](https://hive.apache.org/docs/latest/).

## Konfiguration

Diese Felder werden angezeigt, wenn Sie diese Verbindung erstellen oder bearbeiten. Ob ein Feld erforderlich oder optional ist, hängt von den aktivierten Authentifizierungsoptionen ab.

### Identifikation

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename für diese Verbindung. |
| Alias | Text (mehrzeilig) | Optionaler Alias oder Notizen zur Verbindung. |
| Ist aktiv | Schalter | Gibt an, ob die Verbindung aktiviert ist. Deaktivieren Sie sie, um sie zu pausieren, ohne sie zu löschen. |
| Db schreibgeschützt | Schalter | Beschränkt die Verbindung auf Lesevorgänge. |
| Zugriffstyp | Auswahl | Zugriffsebene für diese Verbindung: schreibgeschützt, nur schreibend oder lesend und schreibend. |

### Verbindung

| Feld | Typ | Beschreibung |
|---|---|---|
| Db-Host | Text | Hostname oder IP-Adresse des Datenbankservers. |
| Db-Port | Zahl | Portnummer für die Datenbankverbindung. |
| Db-Katalog | Text | Datenbank, Katalog oder Schema, zu dem die Verbindung hergestellt wird. |

### Authentifizierung

| Feld | Typ | Beschreibung |
|---|---|---|
| Db-Benutzer | Text | Benutzername für die Datenbankauthentifizierung. |
| SSO verwenden | Schalter | Authentifiziert sich per Single Sign-on statt mit Benutzername und Passwort. |
| Db-Passwort | Passwort | Passwort für die Datenbankauthentifizierung. |

### SSL / TLS

| Feld | Typ | Beschreibung |
|---|---|---|
| SSL verwenden | Schalter | Verschlüsselt die Verbindung mit SSL/TLS. |
| SSL-Modus | Auswahl | Modus der SSL-Überprüfung (z. B. disable, require, verify-ca, verify-full). |
| SSL-Authentifizierung Clientzertifikat | Text (mehrzeilig) | Clientzertifikat (PEM) für die gegenseitige TLS-Authentifizierung. |
| SSL-Authentifizierung Clientschlüssel | Text (mehrzeilig) | Privater Clientschlüssel (PEM) für die gegenseitige TLS-Authentifizierung. |
| SSL-Authentifizierung Root-Zertifikat | Text (mehrzeilig) | Root-CA-Zertifikat (PEM) zur Überprüfung des Serverzertifikats. |
| SSL-Authentifizierung Zertifikatsperre | Text (mehrzeilig) | Zertifikatsperrliste, falls Ihre Umgebung eine verwendet. |

### SSH-Tunnel

| Feld | Typ | Beschreibung |
|---|---|---|
| SSH verwenden | Schalter | Leitet die Verbindung über einen SSH-Bastion-Host. |
| SSH-Host | Text | Hostname des SSH-Bastion-Hosts. |
| SSH-Port | Zahl | Port des SSH-Bastion-Hosts (Standard 22). |
| SSH-Benutzer | Text | Benutzername für den SSH-Bastion-Host. |
| SSH-Passwort | Passwort | Passwort für den SSH-Bastion-Host (bei Passwortauthentifizierung). |
| SSH-Zertifikat verwenden | Schalter | Authentifiziert sich am SSH-Bastion-Host mit einem privaten Schlüssel statt mit einem Passwort. |
| Privater SSH-Schlüssel | Text (mehrzeilig) | Privater SSH-Schlüssel (PEM) für die Authentifizierung am Bastion-Host. |
| SSH-Hostschlüssel | Text (mehrzeilig) | Erwarteter SSH-Hostschlüssel zur Fingerabdruckprüfung des Bastion-Hosts. |
