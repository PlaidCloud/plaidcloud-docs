---
title: Linode-Object-Storage-Konto hinzufügen
description: Fügen Sie PlaidCloud ein Linode-(Akamai-)Object-Storage-Konto hinzu, um Datendateien mit dem S3-kompatiblen Cloud-Speicher von Linode zu importieren und zu exportieren.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-linode-object-storage-account.md
---

## Linode-Object-Storage-Einrichtung

Diese Schritte müssen im Linode Cloud Manager durchgeführt werden.

1. Melden Sie sich beim [Linode Cloud Manager](https://cloud.linode.com) an
2. Navigieren Sie in der linken Seitenleiste zu **Object Storage**
3. Erstellen Sie einen Bucket, falls noch keiner vorhanden ist. Notieren Sie sich den Bucket-Namen (als **Bezeichnung** bezeichnet) und die Region (z. B. `us-east-1`).
4. Navigieren Sie zu **Object Storage > Access Keys**
5. Wählen Sie **Create Access Key**
6. Geben Sie dem Schlüssel eine Bezeichnung und wählen Sie den oder die Buckets, auf die er mit Lese- und Schreibberechtigung zugreifen soll
7. Wählen Sie **Create Access Key**
8. Kopieren Sie den **Access Key** und den **Secret Key**. Speichern Sie beide für die PlaidCloud-Document-Einrichtung unten. Das Secret wird nur einmal angezeigt.
9. Notieren Sie sich die Endpunkt-URL für die Region Ihres Buckets. Sie folgt dem Muster `https://{region}.linodeobjects.com` (z. B. `https://us-east-1.linodeobjects.com`)

Damit haben Sie nun alles, was Sie brauchen, um Ihr Linode-Object-Storage-Konto zu PlaidCloud Document hinzuzufügen.


## PlaidCloud-Document-Einrichtung

1. Melden Sie sich bei PlaidCloud an
2. Wählen Sie den Workspace, in dem sich das neue Dokumentenkonto befinden soll
3. Gehen Sie zu `Document > Manage Accounts`
4. Klicken Sie auf die Schaltfläche `+ New Account`
5. Wählen Sie `Linode Object Storage` als **Diensttyp**
6. Geben Sie einen Namen und eine Beschreibung ein
7. Geben Sie als **Startpfad** die Endpunkt-URL gefolgt vom Bucket-Namen ein: `https://us-east-1.linodeobjects.com/my-bucket`
8. Geben Sie die **Region** ein (z. B. `us-east-1`)
9. Wählen Sie ein für Ihren Anwendungsfall geeignetes **Sicherheitsmodell**. Wenn Sie unsicher sind, belassen Sie es bei `Private`.
10. Fügen Sie den **Access Key** unter Authentifizierungsdaten in das Feld Zugriffsschlüssel-ID ein
11. Fügen Sie den **Secret Key** unter Authentifizierungsdaten in das Feld Geheimer Zugriffsschlüssel ein
12. Klicken Sie auf die Schaltfläche „Speichern“, und Ihr neues Dokumentenkonto ist aktiv
