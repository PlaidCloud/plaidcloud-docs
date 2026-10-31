---
title: Backblaze-B2-Konto hinzufügen
description: Fügen Sie PlaidCloud ein Backblaze-B2-Speicherkonto hinzu, um Datendateien mit kostengünstigem Cloud-Objektspeicher zu importieren und zu exportieren.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-backblaze-b2-account.md
---

## Backblaze-B2-Einrichtung

Diese Schritte müssen in der Backblaze-B2-Konsole durchgeführt werden.

1. Melden Sie sich bei der [Backblaze-B2-Konsole](https://secure.backblaze.com/b2_buckets.htm) an
2. Navigieren Sie zu **Buckets** und erstellen Sie einen Bucket, falls noch keiner vorhanden ist. Notieren Sie sich den Bucket-Namen.
3. Navigieren Sie zu **App Keys**
4. Wählen Sie **Add a New Application Key**
5. Geben Sie dem Schlüssel einen Namen, wählen Sie den Bucket, auf den er zugreifen soll, und wählen Sie die passenden Berechtigungen (Lesen und Schreiben)
6. Wählen Sie **Create New Key**
7. Kopieren Sie die **keyID** (das ist Ihr Access Key) und den **applicationKey** (das ist Ihr Secret Key). Speichern Sie beide für die PlaidCloud-Document-Einrichtung unten. Der Application Key wird nur einmal angezeigt.
8. Notieren Sie sich den **S3 Endpoint** für die Region Ihres Buckets. Er folgt dem Muster `https://s3.{region}.backblazeb2.com` (z. B. `https://s3.us-west-004.backblazeb2.com`). Sie finden ihn auf der Detailseite des Buckets.

Damit haben Sie nun alles, was Sie brauchen, um Ihr Backblaze-B2-Konto zu PlaidCloud Document hinzuzufügen.


## PlaidCloud-Document-Einrichtung

1. Melden Sie sich bei PlaidCloud an
2. Wählen Sie den Workspace, in dem sich das neue Dokumentenkonto befinden soll
3. Gehen Sie zu `Document > Manage Accounts`
4. Klicken Sie auf die Schaltfläche `+ New Account`
5. Wählen Sie `Backblaze B2` als **Diensttyp**
6. Geben Sie einen Namen und eine Beschreibung ein
7. Geben Sie als **Startpfad** Ihren S3-kompatiblen Endpunkt gefolgt vom Bucket-Namen ein: `https://s3.us-west-004.backblazeb2.com/my-bucket`
8. Geben Sie die **Region** Ihres Buckets ein (z. B. `us-west-004`)
9. Wählen Sie ein für Ihren Anwendungsfall geeignetes **Sicherheitsmodell**. Wenn Sie unsicher sind, belassen Sie es bei `Private`.
10. Fügen Sie die **keyID** unter Authentifizierungsdaten in das Feld Zugriffsschlüssel-ID ein
11. Fügen Sie den **applicationKey** unter Authentifizierungsdaten in das Feld Geheimer Zugriffsschlüssel ein
12. Klicken Sie auf die Schaltfläche „Speichern“, und Ihr neues Dokumentenkonto ist aktiv
