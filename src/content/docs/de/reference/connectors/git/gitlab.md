---
title: GitLab-Repository-Konnektor
description: Konfigurieren Sie in PlaidCloud eine GitLab-Repository-Verbindung, um versionskontrollierten Code und Konfigurationen in Ihre Workflows zu integrieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/git/gitlab.md
---

## Servicedokumentation
[Die GitLab-Servicedokumentation](https://docs.gitlab.com/).

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

### Authentifizierung

| Feld | Typ | Beschreibung |
|---|---|---|
| SSO verwenden | Schalter | Authentifiziert sich per Single Sign-on statt mit Benutzername und Passwort. |

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

### Sonstiges

| Feld | Typ | Beschreibung |
|---|---|---|
| Repository-Pfad | Text | — |
| Standardbranch | Text | — |
| Startpfad | Text | — |
| Dienstbenutzername | Text | — |
| Token | Passwort | — |
