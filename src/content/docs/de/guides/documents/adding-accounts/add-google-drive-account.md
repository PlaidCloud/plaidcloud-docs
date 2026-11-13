---
title: Google-Drive-Konto hinzufügen
description: Fügen Sie PlaidCloud ein Google-Drive-Speicherkonto hinzu, um Datendateien mit dem Google-Drive-Cloud-Speicher zu importieren und zu exportieren.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-drive-account.md
---

## Google-Drive-Einrichtung

Diese Schritte müssen in der Google Cloud Console durchgeführt werden, um ein Dienstkonto zu erstellen, mit dem PlaidCloud auf Google Drive zugreifen kann.

### Ein Google-Cloud-Projekt erstellen

1. Melden Sie sich bei der [Google Cloud Console](https://console.cloud.google.com) an
2. Erstellen Sie ein neues Projekt oder wählen Sie ein vorhandenes aus

### Die Google Drive API aktivieren

1. Navigieren Sie zu **APIs & Services > Library**
2. Suchen Sie nach **Google Drive API**
3. Wählen Sie sie aus und klicken Sie auf **Aktivieren**

### Ein Dienstkonto erstellen

1. Navigieren Sie zu **APIs & Services > Credentials**
2. Wählen Sie **+ Create Credentials > Service account**
3. Geben Sie einen Namen für das Dienstkonto ein (z. B. `plaidcloud-drive`)
4. Wählen Sie **Create and Continue**
5. Weisen Sie optional Rollen zu (z. B. **Viewer** für schreibgeschützten Zugriff oder **Editor** für Lese- und Schreibzugriff). Wählen Sie **Fortfahren**.
6. Wählen Sie **Fertig**

### Einen Dienstkontoschlüssel generieren

1. Wählen Sie in der Liste **Service Accounts** das soeben erstellte Dienstkonto aus
2. Navigieren Sie zur Registerkarte **Keys**
3. Wählen Sie **Schlüssel hinzufügen > Neu erstellen**
4. Wählen Sie das Format **JSON** und klicken Sie auf **Erstellen**
5. Eine JSON-Schlüsseldatei wird heruntergeladen. Speichern Sie diese Datei sicher – sie enthält die Zugangsdaten, die PlaidCloud verwendet.

### Drive-Inhalte für das Dienstkonto freigeben

1. Kopieren Sie die E-Mail-Adresse des Dienstkontos (z. B. `plaidcloud-drive@your-project.iam.gserviceaccount.com`)
2. Geben Sie in Google Drive die Ordner, auf die PlaidCloud zugreifen soll, für diese E-Mail-Adresse frei und gewähren Sie dabei den Zugriff **Editor**. Um ein Shared Drive zu verwenden, fügen Sie stattdessen das Dienstkonto als Mitglied dieses Shared Drive hinzu.

Damit haben Sie nun alles, was Sie brauchen, um Ihr Google-Drive-Konto zu PlaidCloud Document hinzuzufügen.


## PlaidCloud-Document-Einrichtung

1. Melden Sie sich bei PlaidCloud an
2. Wählen Sie den Workspace, in dem sich das neue Dokumentenkonto befinden soll
3. Gehen Sie zu `Document > Manage`
4. Klicken Sie auf die Schaltfläche **Neues Konto**
5. Wählen Sie `Google Drive` als **Diensttyp**
6. Geben Sie einen Namen und eine Beschreibung ein
7. Geben Sie den Pfad des freigegebenen Ordners in das Feld **Startpfad** ein oder lassen Sie es leer, um auf alle freigegebenen Inhalte zuzugreifen
8. Wählen Sie ein für Ihren Anwendungsfall geeignetes **Sicherheitsmodell**. Wenn Sie unsicher sind, belassen Sie es bei `Private`.
9. Fügen Sie den gesamten Inhalt der JSON-Schlüsseldatei unter Authentifizierungsdaten in das Feld OAuth2-Anmeldeinformationen (JSON) ein
10. Klicken Sie auf die Schaltfläche „Speichern“, und Ihr neues Dokumentenkonto ist aktiv

## Das Konto in Workflows verwenden

Ein Google-Drive-Konto funktioniert sowohl in Workflows als auch im Document-Browser. Schritte können Dateien auflisten, importieren, exportieren, kopieren, verschieben, umbenennen und löschen sowie Ordner erstellen.

- **Speicherorte.** Die obersten Speicherorte des Kontos sind die für das Dienstkonto freigegebenen Ordner und die Shared Drives, in denen es Mitglied ist. Pfade bestehen aus Ordnernamen, zum Beispiel `Finance/Reports/2026`. Wenn zwei freigegebene Ordner oder Shared Drives denselben Namen haben, verweigert das Konto das Öffnen dieses Namens. Benennen Sie alle bis auf einen um oder heben Sie ihre Freigabe auf.
- **Google Sheets.** Ein Google Sheet wird als `.xlsx`-Export gelesen und erscheint als `Name.xlsx`. Andere Google-Workspace-Dateien, etwa Docs und Slides, können nicht gelesen werden.
- **Neue Dateien in My Drive.** Ein Dienstkonto hat keinen eigenen Speicherplatz. In einem Ordner, der im persönlichen My Drive einer Person liegt, kann es daher eine vorhandene Datei überschreiben, aber keine neue erstellen. Erstellen Sie die Datei dort zuerst selbst oder verwenden Sie einen Ordner in einem Shared Drive, der neue Dateien und Ordner akzeptiert.
- **Fehlende Ordner.** Ein Ordner, der nicht existiert, wird als leer aufgelistet, statt einen Fehler zu verursachen.
- **Drosselung.** PlaidCloud wiederholt Anfragen automatisch, wenn Google eine Anfrage drosselt oder einen vorübergehenden Fehler zurückgibt.
