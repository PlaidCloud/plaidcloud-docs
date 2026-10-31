---
title: DigitalOcean-Spaces-Konto hinzufügen
description: Fügen Sie PlaidCloud ein DigitalOcean-Spaces-Speicherkonto hinzu, um Datendateien mit dem S3-kompatiblen Objektspeicher von DigitalOcean zu importieren und zu exportieren.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-digitalocean-spaces-account.md
---

## DigitalOcean-Spaces-Einrichtung

Diese Schritte müssen im DigitalOcean Control Panel durchgeführt werden.

1. Melden Sie sich beim [DigitalOcean Control Panel](https://cloud.digitalocean.com) an
2. Navigieren Sie in der linken Seitenleiste zu **Spaces Object Storage**
3. Erstellen Sie einen Space, falls noch keiner vorhanden ist. Notieren Sie sich den Namen des Space und die Region (z. B. `nyc3`).
4. Navigieren Sie zu **API > Spaces Keys** (im Abschnitt Tokens)
5. Wählen Sie **Generate New Key**
6. Geben Sie dem Schlüssel einen Namen
7. Kopieren Sie den **Key** (Access Key) und das **Secret**. Speichern Sie beide für die PlaidCloud-Document-Einrichtung unten. Das Secret wird nur einmal angezeigt.
8. Notieren Sie sich die Endpunkt-URL für die Region Ihres Space. Sie folgt dem Muster `https://{region}.digitaloceanspaces.com` (z. B. `https://nyc3.digitaloceanspaces.com`)

Damit haben Sie nun alles, was Sie brauchen, um Ihr DigitalOcean-Spaces-Konto zu PlaidCloud Document hinzuzufügen.


## PlaidCloud-Document-Einrichtung

1. Melden Sie sich bei PlaidCloud an
2. Wählen Sie den Workspace, in dem sich das neue Dokumentenkonto befinden soll
3. Gehen Sie zu `Document > Manage Accounts`
4. Klicken Sie auf die Schaltfläche `+ New Account`
5. Wählen Sie `DigitalOcean Spaces` als **Diensttyp**
6. Geben Sie einen Namen und eine Beschreibung ein
7. Geben Sie als **Startpfad** die Endpunkt-URL gefolgt vom Namen des Space ein: `https://nyc3.digitaloceanspaces.com/my-space`
8. Geben Sie die **Region** ein (z. B. `nyc3`, `sfo3`, `ams3`)
9. Wählen Sie ein für Ihren Anwendungsfall geeignetes **Sicherheitsmodell**. Wenn Sie unsicher sind, belassen Sie es bei `Private`.
10. Fügen Sie den **Key** unter Authentifizierungsdaten in das Feld Zugriffsschlüssel-ID ein
11. Fügen Sie das **Secret** unter Authentifizierungsdaten in das Feld Geheimer Zugriffsschlüssel ein
12. Klicken Sie auf die Schaltfläche „Speichern“, und Ihr neues Dokumentenkonto ist aktiv
