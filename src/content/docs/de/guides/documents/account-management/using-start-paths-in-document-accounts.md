---
title: Startpfade in Dokumentenkonten verwenden
description: Konfigurieren Sie Startpfade in PlaidCloud-Dokumentenkonten, um den Standardverzeichnisort beim Durchsuchen des Dateispeichers zu steuern.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/account-management/using-start-paths-in-document-accounts.md
---

Das Kontoverwaltungsformular ermöglicht die Konfiguration der Speicherverbindungsinformationen und eines Startpfads. Ein Startpfad erlaubt es den Benutzern des Kontos, das Durchsuchen der Verzeichnisstruktur weiter unten im Verzeichnisbaum zu beginnen. Diese Option ist nützlich, wenn mehrere Teams getrennten Dateispeicher benötigen, Sie aber nur ein zugrunde liegendes Speicherdienstkonto haben möchten.



Die Option „Startpfad“ in Dokumentenkonten ist aus folgenden Gründen nützlich:


* Zur Steuerung des Zugriffs auf Unterverzeichnisse für bestimmte Teams und Gruppen
* Zur Gewährung des Zugriffs auf nur einen Bucket

Wenn Sie zum Beispiel den Startpfad *teams/team_1/* für das Dokumentenkonto `Team 1` und *teams/team_2* für das Dokumentenkonto `Team 2` festlegen, erhalten Sie verschiedene Startpunkte auf einem gemeinsamen Konto. Wenn ein Mitglied das Dokumentenkonto Team 1 öffnet, beginnt die Dateinavigation innerhalb von *team/team_1*. Es kann im Baum nicht nach oben gehen und nichts oberhalb von *teams/team_1* sehen.



Für Team 2 gilt eine ähnliche Einschränkung: Es kann nicht in den Bereich von Team 1 navigieren.



So lassen sich bestimmte Teams auf tiefere Ebenen des Baums beschränken, während andere Teams Zugriff auf höhere Ebenen erhalten, ohne dass zusätzliche Komplexität im Cloud-Speicher wie weitere Buckets oder spezielle Berechtigungen nötig ist.



## Den Startpfad hinzufügen und aktualisieren


1. Gehen Sie zu Document > Manage Accounts
2. Wählen Sie das Konto, das Sie bearbeiten möchten, und öffnen Sie den Bearbeitungsmodus
3. Geben Sie im Textfeld „Start Path“ einen Startpfad ein
4. Klicken Sie auf die Schaltfläche „Speichern“

## Format des Startpfads


Der Pfad beginnt immer mit dem Bucket-Namen, gefolgt von den Unterverzeichnissen.



```text
<my-bucket>/folder1/folder2/
```
