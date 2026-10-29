---
title: Neue Dokumentenkonten hinzufügen
description: Verbinden Sie Cloud- und On-Premises-Dokumentenspeicher mit PlaidCloud – S3, GCS, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV und mehr.
sidebar:
  label: Neue Dokumentenkonten hinzufügen
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/index.md
---

Verbinden Sie Cloud- und On-Premises-Dokumentenspeicher mit PlaidCloud – S3, Google Cloud Storage, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV und mehr. Jeder Anbieter hat eigene Anmeldedaten und einen eigenen Verbindungsablauf.

Die schnellste Option ist ein **Von PlaidCloud verwalteter Bucket**: PlaidCloud richtet den Speicher für Sie ein und betreibt ihn, Sie wählen nur einen Namen und müssen nichts weiter konfigurieren. Um bereits vorhandenen Speicher zu verbinden, wählen Sie unten den passenden Anbieter.

## Gespeicherte Secrets sind nur schreibbar

Das Secret eines Kontos, das Feld mit der Bezeichnung **Privater Schlüssel / Passwort** oder je nach Kontotyp **Geheimer Zugriffsschlüssel**, **Kontoschlüssel**, **Client-Secret**, **Zugriffstoken**, **Kennwort**, **JSON-Schlüssel des Systembenutzers** oder **OAuth2-Anmeldeinformationen (JSON)**, ist nur schreibbar, ebenso der **RSA Private Key** eines SFTP-Kontos. Nach dem Speichern werden sie nie wieder angezeigt, weder im Formular noch in der API noch einem KI-Assistenten. Wenn Sie ein Konto bearbeiten, ist das Feld leer und zeigt den Hinweis *Paste the value; leave blank on edit to keep the saved one.* Lassen Sie es leer, um das gespeicherte Secret beizubehalten, oder fügen Sie ein neues ein, um es zu ersetzen.

Wenn Sie ändern, wohin sich ein Konto verbindet, müssen Sie sein Secret erneut eingeben. Wenn Sie den ersten Teil des **Startpfads** ändern (bei Cloud-Speicher den Bucket oder Container), den **Host oder die IP-Adresse** bzw. den **SSH-Verbindungsport** eines SFTP-Kontos oder die **OneDrive-Mandanten-ID** eines OneDrive-Kontos, fügen Sie ebenfalls das Secret ein, sonst wird das Speichern mit der Meldung *Changing where the account connects needs its secret entered again* abgelehnt. Das verhindert, dass jemand, der ein Konto bearbeiten, aber nie sein Secret sehen kann, dieses Secret an einen Server seiner Wahl sendet.

Ein KI-Assistent, der über den PlaidCloud-MCP-Connector verbunden ist, kann ebenfalls Konten mit Speichertyp, Anmeldedaten und Startpfad erstellen und aktualisieren. Anmeldedaten sind nur schreibbar und werden beim Zurücklesen des Kontos ausgeblendet. Ein ausführliches Beispiel finden Sie unter [OneDrive-/SharePoint-Konto hinzufügen](/de/guides/documents/adding-accounts/add-onedrive-account/#konto-mit-einem-ki-assistenten-erstellen).
