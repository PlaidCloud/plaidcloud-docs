---
title: Azure-Repos-Repository-Connector
description: Konfigurieren Sie in PlaidCloud eine Azure-Repos-Verbindung, um versionierten Code und versionierte Konfiguration in Ihre Workflows zu integrieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/git/azure-repos.md
---

## Dokumentation des Dienstes
[Die Azure-Repos-Dokumentation](https://learn.microsoft.com/en-us/azure/devops/repos/).

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

### Authentifizierung

| Feld | Typ | Beschreibung |
|---|---|---|
| Use sso | Schalter | Authentifizierung per Single Sign-on statt mit Benutzername und Passwort. |

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

### Sonstiges

| Feld | Typ | Beschreibung |
|---|---|---|
| Repo path | Text | — |
| Default branch | Text | — |
| Start path | Text | — |
| Service username | Text | — |
| Token | Passwort | — |
