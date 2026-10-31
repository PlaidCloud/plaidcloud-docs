---
title: Azure Databricks
description: Konfigurieren Sie in PlaidCloud eine Azure-Databricks-Verbindung, um Spark-basierte Analysen und Lakehouse-Daten in Workflows zu integrieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/azure-databricks.md
---

**Azure Databricks** kombiniert Apache Spark, Delta Lake und eine verwaltete Notebook-Umgebung auf Microsoft Azure. Verwenden Sie diesen Konnektor, um Tabellen in einem Databricks-Workspace aus PlaidCloud-Workflows zu lesen und zu schreiben. Die Authentifizierung erfolgt über ein persönliches Zugriffstoken oder einen Service Principal; die Workspace-URL und der HTTP-Pfad bestimmen das SQL-Warehouse, auf das zugegriffen wird.

## Dokumentation des Anbieters
[Azure-Databricks-Dokumentation](https://learn.microsoft.com/en-us/azure/databricks/).

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
| DB-Katalog | Text | Datenbank, Katalog oder Schema, zu dem eine Verbindung hergestellt wird. |
| DB-Schema | Text | Schemaname innerhalb der Datenbank. |

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

### Sonstiges

| Feld | Typ | Beschreibung |
|---|---|---|
| HTTP-Pfad | Text | — |
