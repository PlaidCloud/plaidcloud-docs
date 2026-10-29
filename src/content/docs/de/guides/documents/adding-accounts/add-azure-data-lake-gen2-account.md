---
title: Azure-Data-Lake-Gen2-Konto hinzufügen
description: Fügen Sie PlaidCloud ein Azure-Data-Lake-Storage-Gen2-Konto hinzu, um Datendateien mit hierarchischem Namespace-Speicher in Azure zu importieren und zu exportieren.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-data-lake-gen2-account.md
---

## Azure-Data-Lake-Gen2-Einrichtung

Azure Data Lake Storage Gen2 baut auf Azure Blob Storage mit aktiviertem hierarchischem Namespace auf. Diese Schritte müssen im Azure-Portal durchgeführt werden.

1. Melden Sie sich beim [Azure-Portal](https://portal.azure.com) an
2. Navigieren Sie zu **Storage accounts** und wählen Sie ein Speicherkonto mit aktiviertem **Hierarchical namespace** aus oder erstellen Sie eines
3. Wählen Sie in der linken Seitenleiste unter **Security + networking** den Eintrag **Access keys**
4. Kopieren Sie den **Storage account name** und einen der **Key**-Werte. Speichern Sie beide für die PlaidCloud-Document-Einrichtung unten.
5. Navigieren Sie unter **Data storage** zu **Containers** und erstellen Sie ein Dateisystem (Container), falls noch keines vorhanden ist. Notieren Sie sich den Namen des Dateisystems.

Damit haben Sie nun alles, was Sie brauchen, um Ihr Azure-Data-Lake-Gen2-Konto zu PlaidCloud Document hinzuzufügen.


## PlaidCloud-Document-Einrichtung

1. Melden Sie sich bei PlaidCloud an
2. Wählen Sie den Workspace, in dem sich das neue Dokumentenkonto befinden soll
3. Gehen Sie zu `Document > Manage Accounts`
4. Klicken Sie auf die Schaltfläche `+ New Account`
5. Wählen Sie `Azure Data Lake Gen2` als **Diensttyp**
6. Geben Sie einen Namen und eine Beschreibung ein
7. Geben Sie den Namen des Dateisystems und ein optionales Pfadpräfix in das Feld **Startpfad** ein (z. B. `my-filesystem/data`). Das erste Pfadsegment ist der Name des Dateisystems.
8. Wählen Sie ein für Ihren Anwendungsfall geeignetes **Sicherheitsmodell**. Wenn Sie unsicher sind, belassen Sie es bei `Private`.
9. Fügen Sie den **Storage account name** unter Authentifizierungsdaten in das Feld Kontoname ein
10. Fügen Sie den **Key** unter Authentifizierungsdaten in das Feld Kontoschlüssel ein
11. Klicken Sie auf die Schaltfläche „Speichern“, und Ihr neues Dokumentenkonto ist aktiv
