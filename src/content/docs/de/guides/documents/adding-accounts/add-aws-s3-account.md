---
title: AWS-S3-Konto hinzufügen
description: Fügen Sie PlaidCloud ein AWS-S3-Speicherkonto hinzu, um Datendateien mit dem Amazon-Cloud-Objektspeicher zu importieren und zu exportieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-aws-s3-account.md
---

## AWS-S3-Einrichtung

Diese Schritte müssen in der AWS-Konsole durchgeführt werden.

1. Melden Sie sich bei einem Amazon-Web-Services-(AWS-)Konto an oder erstellen Sie eines
2. Gehen Sie in der Konsole zu `All services > Storage > S3`
3. Erstellen Sie einen Standard- oder Test-Bucket. Notieren Sie sich den Bucket-Namen und die Region (z. B. `us-east-1`).
4. Gehen Sie in der Konsole zu `All Services > Security Identity & Compliance > IAM > Users`
5. Klicken Sie auf die Schaltfläche `Create User`
6. Geben Sie bei der Aufforderung einen Benutzernamen ein und wählen Sie ausschließlich `Access Key - Programmatic access`. Klicken Sie auf die Schaltfläche `Next: Permissions`.
7. Wählen Sie das Optionsfeld `Attach existing policies directly`
8. Geben Sie im Filtersuchfeld `s3` ein. Wenn die Liste auf S3-bezogene Einträge reduziert ist, wählen Sie `AmazonS3FullAccess`, indem Sie das Kontrollkästchen links davon aktivieren. Klicken Sie auf die Schaltfläche `Next: Tags`.
9. Überspringen Sie diesen Schritt, indem Sie auf die Schaltfläche `Next: Review` klicken
10. Prüfen Sie die Benutzereinstellungen und wählen Sie `Create user`
11. Sichern Sie die für den Benutzer generierten Schlüssel, indem Sie die CSV-Datei herunterladen oder die Schlüssel zur späteren Verwendung irgendwo hineinkopieren. Sie können diesen Schlüssel nicht erneut abrufen, bewahren Sie ihn daher sorgfältig auf. Wenn Sie einen Schlüssel neu generieren müssen, gehen Sie einfach zurück zu Schritt 5.

Damit haben Sie nun alles, was Sie brauchen, um Ihr S3-Konto zu PlaidCloud Document hinzuzufügen.


## PlaidCloud-Document-Einrichtung

1. Melden Sie sich bei PlaidCloud an
2. Wählen Sie den Workspace, in dem sich das neue Dokumentenkonto befinden soll
3. Gehen Sie zu `Document > Manage Accounts`
4. Klicken Sie auf die Schaltfläche `+ New Account`
5. Wählen Sie `Amazon S3` als **Diensttyp**
6. Geben Sie einen Namen und eine Beschreibung ein
7. Geben Sie den Bucket-Namen und ein optionales Pfadpräfix in das Feld **Startpfad** ein (z. B. `my-bucket` oder `my-bucket/data`). Das erste Pfadsegment ist der Bucket-Name.
8. Wählen Sie ein für Ihren Anwendungsfall geeignetes **Sicherheitsmodell**. Wenn Sie unsicher sind, belassen Sie es bei `Private`.
9. Fügen Sie den in Schritt 11 oben erstellten **Access Key** unter Authentifizierungsdaten in das Feld Zugriffsschlüssel-ID ein
10. Fügen Sie den in Schritt 11 oben erstellten **Secret Key** unter Authentifizierungsdaten in das Feld Geheimer Zugriffsschlüssel ein
11. Geben Sie die **Region** Ihres Buckets ein (z. B. `us-east-1`, `eu-west-1`). Bleibt das Feld leer, gilt standardmäßig `us-east-2`.
12. Klicken Sie auf die Schaltfläche „Speichern“, und Ihr neues Dokumentenkonto ist aktiv
