---
title: Wasabi-Hot-Storage-Konto hinzufügen
description: Fügen Sie PlaidCloud ein Wasabi-Hot-Storage-Konto hinzu, um Datendateien über kostengünstigen Cloud-Speicher zu importieren und zu exportieren.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-wasabi-hot-storage-account.md
---

## Wasabi-Hot-Storage-Einrichtung


Diese Schritte führen Sie in der Wasabi-Hot-Storage-Konsole aus.


1. Melden Sie sich bei einem Wasabi-Hot-Storage-Konto an oder erstellen Sie eines.
2. Gehen Sie in der Konsole zu `Buckets`.
3. Erstellen Sie einen Standard- oder Test-Bucket.
4. Gehen Sie in der Konsole zu Users.
5. Wählen Sie die Schaltfläche `Create User`.
6. Geben Sie bei der Aufforderung einen Benutzernamen ein und wählen Sie den Benutzertyp `Programmatic (create API key)`.
7. Überspringen Sie die Gruppenzuweisung. Wählen Sie die Schaltfläche `Next`.
8. Wählen Sie das Pluszeichen neben der Richtlinie `WasabiFullAccess`, um die Richtlinie dem Benutzer zuzuordnen. Wählen Sie die Schaltfläche `Next`.
9. Prüfen Sie die Benutzereinstellungen und wählen Sie `Create User`.
10. Sichern Sie die für den Benutzer generierten Schlüssel, indem Sie die CSV-Datei herunterladen oder die Schlüssel zur späteren Verwendung an einen sicheren Ort kopieren. Dieser Schlüssel kann nicht erneut abgerufen werden, bewahren Sie ihn daher sorgfältig auf. Wenn Sie einen Schlüssel neu generieren müssen, gehen Sie einfach zurück zu Schritt 5 oben.

Sie haben nun alles, was Sie benötigen, um Ihr Wasabi-Konto zu PlaidCloud Document hinzuzufügen.



## PlaidCloud-Document-Einrichtung

1. Melden Sie sich bei PlaidCloud an.
2. Wählen Sie den Workspace aus, in dem sich das neue Dokumentenkonto befinden soll.
3. Gehen Sie zu `Document > Manage Accounts`.
4. Wählen Sie die Schaltfläche `+ New Account`.
5. Wählen Sie `Wasabi Hot Storage` als **Diensttyp**.
6. Geben Sie einen Namen und eine Beschreibung ein.
7. Geben Sie den Bucket-Namen und ein optionales Pfadpräfix in das Feld **Startpfad** ein (z. B. `my-bucket` oder `my-bucket/data`). Das erste Pfadsegment ist der Bucket-Name.
8. Wählen Sie ein für Ihren Anwendungsfall geeignetes **Sicherheitsmodell**. Lassen Sie es auf `Private`, wenn Sie unsicher sind.
9. Fügen Sie den in Schritt 10 oben erstellten **Access Key** unter Authentifizierungsdaten in das Feld Zugriffsschlüssel-ID ein.
10. Fügen Sie den in Schritt 10 oben erstellten **Secret Key** unter Authentifizierungsdaten in das Feld Geheimer Zugriffsschlüssel ein.
11. Geben Sie die **Region** ein, falls Ihr Wasabi-Konto eine bestimmte Region verwendet; lassen Sie das Feld andernfalls leer.
12. Wählen Sie die Schaltfläche Speichern, und Ihr neues Dokumentenkonto ist aktiv.
