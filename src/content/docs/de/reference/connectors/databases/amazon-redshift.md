---
title: Amazon Redshift
description: Richten Sie in PlaidCloud eine Amazon-Redshift-Datenbankverbindung ein, um Daten Ihres Redshift-Warehouse abzufragen, zu importieren und zu exportieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/amazon-redshift.md
---

**Amazon Redshift** ist das verwaltete Cloud-Data-Warehouse von AWS, das für analytische Workloads auf großen Datensätzen konzipiert ist. Mit diesem Konnektor lesen und schreiben Sie Redshift-Tabellen aus PlaidCloud-Workflows. Der Konnektor spricht das PostgreSQL-Wire-Protokoll; die Authentifizierung erfolgt mit Standard-Datenbankanmeldedaten oder mit IAM-gestützten temporären Anmeldedaten.

## Upstream-Dokumentation
Anleitungen und Referenzmaterial finden Sie in der [Amazon-Redshift-Dokumentation](https://docs.aws.amazon.com/redshift/).

## Konfiguration

Diese Felder werden beim Erstellen oder Bearbeiten dieser Verbindung angezeigt. Ob ein Feld erforderlich oder optional ist, hängt von den aktivierten Authentifizierungsoptionen ab.

### Identifikation

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename dieser Verbindung. |
| Alias | Text (mehrzeilig) | Optionaler Alias oder optionale Notizen zur Verbindung. |
| Ist aktiv | Umschalter | Gibt an, ob die Verbindung aktiviert ist. Deaktivieren Sie sie, um sie anzuhalten, ohne sie zu löschen. |
| Datenbank schreibgeschützt | Umschalter | Beschränkt die Verbindung auf Lesevorgänge. |
| Zugriffstyp | Auswahl | Zugriffsebene dieser Verbindung: schreibgeschützt, nur schreiben oder lesen und schreiben. |

### Verbindung

| Feld | Typ | Beschreibung |
|---|---|---|
| Datenbank-Host | Text | Hostname oder IP-Adresse des Datenbankservers. |
| Datenbank-Port | Zahl | Portnummer der Datenbankverbindung. |
| Datenbankkatalog | Text | Datenbank, Katalog oder Schema, mit dem die Verbindung hergestellt wird. |

### Authentifizierung

| Feld | Typ | Beschreibung |
|---|---|---|
| Datenbankbenutzer | Text | Benutzername für die Datenbankauthentifizierung. |
| SSO verwenden | Umschalter | Authentifizierung per Single Sign-on statt mit Benutzername und Passwort. |
| Datenbankpasswort | Passwort | Passwort für die Datenbankauthentifizierung. |

### SSL / TLS

| Feld | Typ | Beschreibung |
|---|---|---|
| SSL verwenden | Umschalter | Verschlüsselt die Verbindung mit SSL/TLS. |
| SSL-Modus | Auswahl | SSL-Prüfmodus (z. B. disable, require, verify-ca, verify-full). |
| SSL-Clientzertifikat | Text (mehrzeilig) | Clientzertifikat (PEM) für die gegenseitige TLS-Authentifizierung. |
| SSL-Client-Schlüssel | Text (mehrzeilig) | Privater Clientschlüssel (PEM) für die gegenseitige TLS-Authentifizierung. |
| SSL-Root-Zertifikat | Text (mehrzeilig) | CA-Stammzertifikat (PEM) zur Überprüfung des Serverzertifikats. |
| SSL-Zertifikatsperrung | Text (mehrzeilig) | Zertifikatsperrliste, falls Ihre Umgebung eine verwendet. |

### SSH-Tunnel

| Feld | Typ | Beschreibung |
|---|---|---|
| SSH verwenden | Umschalter | Tunnelt die Verbindung über einen SSH-Bastion-Host. |
| SSH-Host | Text | Hostname des SSH-Bastion-Hosts. |
| SSH-Port | Zahl | Port des SSH-Bastion-Hosts (Standard 22). |
| SSH-Benutzer | Text | Benutzername für den SSH-Bastion-Host. |
| SSH-Passwort | Passwort | Passwort für den SSH-Bastion-Host (bei Passwortauthentifizierung). |
| SSH-Zertifikat verwenden | Umschalter | Authentifizierung am SSH-Bastion-Host mit einem privaten Schlüssel statt mit einem Passwort. |
| Privater SSH-Schlüssel | Text (mehrzeilig) | Privater SSH-Schlüssel (PEM) für die Authentifizierung am Bastion-Host. |
| SSH-Hostschlüssel | Text (mehrzeilig) | Erwarteter SSH-Hostschlüssel zur Überprüfung des Fingerabdrucks des Bastion-Hosts. |
