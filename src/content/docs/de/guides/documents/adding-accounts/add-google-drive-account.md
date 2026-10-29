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
3. Wählen Sie **Schlüssel hinzufügen > Neuen Schlüssel erstellen**
4. Wählen Sie das Format **JSON** und klicken Sie auf **Erstellen**
5. Eine JSON-Schlüsseldatei wird heruntergeladen. Speichern Sie diese Datei sicher – sie enthält die Zugangsdaten, die PlaidCloud verwendet.

### Drive-Inhalte für das Dienstkonto freigeben

1. Kopieren Sie die E-Mail-Adresse des Dienstkontos (z. B. `plaidcloud-drive@your-project.iam.gserviceaccount.com`)
2. Geben Sie in Google Drive die Ordner, auf die PlaidCloud zugreifen soll, für diese E-Mail-Adresse frei und gewähren Sie dabei den Zugriff **Editor**

Damit haben Sie nun alles, was Sie brauchen, um Ihr Google-Drive-Konto zu PlaidCloud Document hinzuzufügen.


## PlaidCloud-Document-Einrichtung

1. Melden Sie sich bei PlaidCloud an
2. Wählen Sie den Workspace, in dem sich das neue Dokumentenkonto befinden soll
3. Gehen Sie zu `Document > Manage Accounts`
4. Klicken Sie auf die Schaltfläche `+ New Account`
5. Wählen Sie `Google Drive` als **Diensttyp**
6. Geben Sie einen Namen und eine Beschreibung ein
7. Geben Sie den Pfad des freigegebenen Ordners in das Feld **Startpfad** ein oder lassen Sie es leer, um auf alle freigegebenen Inhalte zuzugreifen
8. Wählen Sie ein für Ihren Anwendungsfall geeignetes **Sicherheitsmodell**. Wenn Sie unsicher sind, belassen Sie es bei `Private`.
9. Fügen Sie den gesamten Inhalt der JSON-Schlüsseldatei unter Authentifizierungsdaten in das Feld OAuth2-Anmeldeinformationen (JSON) ein
10. Klicken Sie auf die Schaltfläche „Speichern“, und Ihr neues Dokumentenkonto ist aktiv
