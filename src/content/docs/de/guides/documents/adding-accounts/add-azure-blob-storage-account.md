---
title: Azure-Blob-Storage-Konto hinzufügen
description: Fügen Sie PlaidCloud ein Azure-Blob-Storage-Konto hinzu, um Datendateien mit dem Microsoft-Azure-Cloud-Objektspeicher zu importieren und zu exportieren.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-blob-storage-account.md
---

## Azure-Blob-Storage-Einrichtung

Diese Schritte müssen im Azure-Portal durchgeführt werden.

1. Melden Sie sich beim [Azure-Portal](https://portal.azure.com) an
2. Navigieren Sie zu **Storage accounts** und wählen Sie ein Speicherkonto aus oder erstellen Sie eines
3. Wählen Sie in der linken Seitenleiste unter **Security + networking** den Eintrag **Access keys**
4. Kopieren Sie den **Storage account name** und einen der **Key**-Werte. Speichern Sie beide für die PlaidCloud-Document-Einrichtung unten.
5. Navigieren Sie unter **Data storage** zu **Containers** und erstellen Sie einen Container, falls noch keiner vorhanden ist. Notieren Sie sich den Container-Namen.

Damit haben Sie nun alles, was Sie brauchen, um Ihr Azure-Blob-Storage-Konto zu PlaidCloud Document hinzuzufügen.


## PlaidCloud-Document-Einrichtung

1. Melden Sie sich bei PlaidCloud an
2. Wählen Sie den Workspace, in dem sich das neue Dokumentenkonto befinden soll
3. Gehen Sie zu `Document > Manage Accounts`
4. Klicken Sie auf die Schaltfläche `+ New Account`
5. Wählen Sie `Azure Blob Storage` als **Diensttyp**
6. Geben Sie einen Namen und eine Beschreibung ein
7. Geben Sie den Container-Namen und ein optionales Pfadpräfix in das Feld **Startpfad** ein (z. B. `my-container/data`). Das erste Pfadsegment ist der Container-Name.
8. Wählen Sie ein für Ihren Anwendungsfall geeignetes **Sicherheitsmodell**. Wenn Sie unsicher sind, belassen Sie es bei `Private`.
9. Fügen Sie den **Storage account name** unter Authentifizierungsdaten in das Feld Kontoname ein
10. Fügen Sie den **Key** unter Authentifizierungsdaten in das Feld Kontoschlüssel ein
11. Klicken Sie auf die Schaltfläche „Speichern“, und Ihr neues Dokumentenkonto ist aktiv
