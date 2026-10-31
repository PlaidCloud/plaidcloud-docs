---
title: Google-Cloud-Storage-Konto hinzufügen
description: Fügen Sie PlaidCloud ein Google-Cloud-Storage-Konto hinzu, um Datendateien mit dem Google-Cloud-Objektspeicher zu importieren und zu exportieren.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-cloud-storage-account.md
---

## Google-Cloud-Einrichtung


Diese Schritte müssen in der Google Cloud Platform durchgeführt werden


1. Melden Sie sich bei einem Google-Cloud-Platform-Konto an oder erstellen Sie eines
2. Wählen Sie ein Projekt aus oder erstellen Sie eines, in dem sich das Google-Cloud-Storage-Konto befinden soll
3. Gehen Sie in der Google-Cloud-Platform-Konsole zu `Cloud Storage > Browser`
4. Erstellen Sie einen Standard- oder Test-Bucket
5. Gehen Sie in der Google-Cloud-Platform-Konsole zu `IAM & Admin > Service Accounts`
6. Klicken Sie auf die Schaltfläche `+ Create Service Account`
7. Geben Sie die Informationen zum Dienstkonto ein und erstellen Sie das Konto
8. Suchen Sie das soeben erstellte Dienstkonto in der Liste der Dienstkonten und wählen Sie im Kontextmenü rechts `Manage Keys`
9. Wählen Sie im Menü `Add Key` den Eintrag `Create a Key`
10. Wählen Sie bei der Aufforderung das JSON-Format für den Schlüssel. Der Schlüssel wird generiert und automatisch auf Ihren Desktop heruntergeladen. Sie können diesen Schlüssel nicht erneut abrufen, bewahren Sie ihn daher sorgfältig auf. Wenn Sie einen Schlüssel neu generieren müssen, gehen Sie einfach zurück zu Schritt 8.
11. Gehen Sie in der Google-Cloud-Platform-Konsole zu `IAM & Admin > IAM`
12. Suchen Sie das soeben erstellte Dienstkonto und klicken Sie auf das Symbol zum Bearbeiten der Berechtigungen
13. Fügen Sie dem Dienstkonto die Rechte `Storage Admin` und `Storage Transfer Admin` hinzu und speichern Sie. Hinweis: Es können weniger weitreichende Rechte zugewiesen werden, dies wirkt sich jedoch auf die über Document verfügbare Funktionalität aus.

Damit haben Sie nun alles, was Sie brauchen, um Ihr GCS-Konto zu PlaidCloud Document hinzuzufügen.



## PlaidCloud-Document-Einrichtung

1. Melden Sie sich bei PlaidCloud an
2. Wählen Sie den Workspace, in dem sich das neue Dokumentenkonto befinden soll
3. Gehen Sie zu `Document > Manage Accounts`
4. Klicken Sie auf die Schaltfläche `+ New Account`
5. Wählen Sie `Google Cloud Storage` als **Diensttyp**
6. Geben Sie einen Namen und eine Beschreibung ein
7. Geben Sie den Bucket-Namen und ein optionales Pfadpräfix in das Feld **Startpfad** ein (z. B. `my-bucket` oder `my-bucket/data`). Das erste Pfadsegment ist der Bucket-Name.
8. Wählen Sie ein für Ihren Anwendungsfall geeignetes **Sicherheitsmodell**. Wenn Sie unsicher sind, belassen Sie es bei `Private`.
9. Öffnen Sie die in Schritt 10 oben heruntergeladene JSON-Schlüsseldatei des Dienstkontos und kopieren Sie den gesamten Inhalt
10. Fügen Sie den Inhalt unter Authentifizierungsdaten in das Feld **JSON-Schlüssel des Systembenutzers** ein
11. Klicken Sie auf die Schaltfläche „Speichern“, und Ihr neues Dokumentenkonto ist aktiv

Ein gültiger Dienstkontoschlüssel ist erforderlich. Das Speichern des Kontos ohne einen solchen oder mit etwas, das kein Google-Dienstkontoschlüssel ist, wird mit der Meldung „GCS document accounts require a valid service-account key.“ abgelehnt. Ein vorhandenes Konto, das ohne gültigen Schlüssel gespeichert wurde, funktioniert nicht mehr, bis Sie einen in das Feld **JSON-Schlüssel des Systembenutzers** einfügen.
