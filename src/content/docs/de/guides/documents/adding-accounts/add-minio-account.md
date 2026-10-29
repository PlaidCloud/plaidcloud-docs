---
title: MinIO-Konto hinzufügen
description: Fügen Sie PlaidCloud ein MinIO-Speicherkonto hinzu, um Datendateien über selbst gehosteten, S3-kompatiblen Objektspeicher zu importieren und zu exportieren.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-minio-account.md
---

## MinIO-Einrichtung

Diese Schritte führen Sie in der MinIO Console oder über die `mc`-CLI aus.

1. Melden Sie sich bei der MinIO Console an (z. B. `https://your-minio-host:9001`).
2. Wechseln Sie zu **Buckets** und erstellen Sie einen Bucket, falls noch keiner vorhanden ist. Notieren Sie sich den Bucket-Namen.
3. Wechseln Sie zu **Identity > Users** (oder **Access Keys**).
4. Erstellen Sie einen neuen Benutzer oder ein Dienstkonto mit Lese- und Schreibzugriff auf den Ziel-Bucket.
5. Kopieren Sie den **Access Key** und den **Secret Key**, die für den Benutzer generiert wurden. Speichern Sie beide für die nachfolgende PlaidCloud-Document-Einrichtung.
6. Notieren Sie sich die URL des MinIO-Endpunkts (z. B. `https://play.min.io` oder `https://minio.yourcompany.com`).

Sie haben nun alles, was Sie benötigen, um Ihr MinIO-Konto zu PlaidCloud Document hinzuzufügen.


## PlaidCloud-Document-Einrichtung

1. Melden Sie sich bei PlaidCloud an.
2. Wählen Sie den Workspace aus, in dem sich das neue Dokumentenkonto befinden soll.
3. Gehen Sie zu `Document > Manage Accounts`.
4. Wählen Sie die Schaltfläche `+ New Account`.
5. Wählen Sie `MinIO` als **Diensttyp**.
6. Geben Sie einen Namen und eine Beschreibung ein.
7. Geben Sie als **Startpfad** die URL Ihres MinIO-Endpunkts gefolgt vom Bucket-Namen und einem optionalen Präfix ein: `https://minio.yourcompany.com/my-bucket/optional/prefix`
8. Geben Sie die **Region** ein, falls Ihre MinIO-Bereitstellung Regionen verwendet; lassen Sie das Feld andernfalls leer.
9. Wählen Sie ein für Ihren Anwendungsfall geeignetes **Sicherheitsmodell**. Lassen Sie es auf `Private`, wenn Sie unsicher sind.
10. Fügen Sie den **Access Key** unter Authentifizierungsdaten in das Feld Zugriffsschlüssel-ID ein.
11. Fügen Sie den **Secret Key** unter Authentifizierungsdaten in das Feld Geheimer Zugriffsschlüssel ein.
12. Wählen Sie die Schaltfläche Speichern, und Ihr neues Dokumentenkonto ist aktiv.
