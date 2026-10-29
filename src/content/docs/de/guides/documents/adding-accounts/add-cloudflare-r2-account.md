---
title: Cloudflare-R2-Konto hinzufügen
description: Fügen Sie PlaidCloud ein Cloudflare-R2-Speicherkonto hinzu, um Datendateien mit dem Objektspeicher von Cloudflare ohne Egress-Gebühren zu importieren und zu exportieren.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-cloudflare-r2-account.md
---

## Cloudflare-R2-Einrichtung

Diese Schritte müssen im Cloudflare-Dashboard durchgeführt werden.

1. Melden Sie sich beim [Cloudflare-Dashboard](https://dash.cloudflare.com) an
2. Wählen Sie Ihr Konto und navigieren Sie dann in der linken Seitenleiste zu **R2 Object Storage**
3. Erstellen Sie einen Bucket, falls noch keiner vorhanden ist. Notieren Sie sich den Bucket-Namen.
4. Navigieren Sie zu **R2 Object Storage > Manage R2 API Tokens**
5. Wählen Sie **Create API Token**
6. Geben Sie dem Token einen Namen, wählen Sie den oder die Buckets, auf die er zugreifen soll, und wählen Sie die Berechtigung **Object Read & Write**
7. Wählen Sie **Create API Token**
8. Kopieren Sie die **Access Key ID** und den **Secret Access Key**. Speichern Sie beide für die PlaidCloud-Document-Einrichtung unten. Das Secret wird nur einmal angezeigt.
9. Notieren Sie sich den **S3 API endpoint** für Ihr Konto. Er folgt dem Muster `https://{account_id}.r2.cloudflarestorage.com` und wird auf der R2-Übersichtsseite angezeigt.

Damit haben Sie nun alles, was Sie brauchen, um Ihr Cloudflare-R2-Konto zu PlaidCloud Document hinzuzufügen.


## PlaidCloud-Document-Einrichtung

1. Melden Sie sich bei PlaidCloud an
2. Wählen Sie den Workspace, in dem sich das neue Dokumentenkonto befinden soll
3. Gehen Sie zu `Document > Manage Accounts`
4. Klicken Sie auf die Schaltfläche `+ New Account`
5. Wählen Sie `Cloudflare R2` als **Diensttyp**
6. Geben Sie einen Namen und eine Beschreibung ein
7. Geben Sie als **Startpfad** Ihren R2-Endpunkt gefolgt vom Bucket-Namen ein: `https://{account_id}.r2.cloudflarestorage.com/my-bucket`
8. Das Feld **Region** kann auf `auto` gesetzt oder leer gelassen werden – R2 wählt automatisch die nächstgelegene Region
9. Wählen Sie ein für Ihren Anwendungsfall geeignetes **Sicherheitsmodell**. Wenn Sie unsicher sind, belassen Sie es bei `Private`.
10. Fügen Sie die **Access Key ID** unter Authentifizierungsdaten in das Feld Zugriffsschlüssel-ID ein
11. Fügen Sie den **Secret Access Key** unter Authentifizierungsdaten in das Feld Geheimer Zugriffsschlüssel ein
12. Klicken Sie auf die Schaltfläche „Speichern“, und Ihr neues Dokumentenkonto ist aktiv
