---
title: Tableau-Verbindung
description: Verbinden Sie PlaidCloud mit Tableau Server oder Tableau Cloud über ein persönliches Zugriffstoken, damit Workflows Datenquellen veröffentlichen können.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/collaboration/tableau.md
---

Eine Tableau-Verbindung enthält die Adresse einer Tableau-Server- oder Tableau-Cloud-Site und ein persönliches Zugriffstoken. Der Schritt [Publish to Tableau](/de/reference/workflow-steps/export/export-to-tableau/) verwendet sie, um `.hyper`-Extrakte als Datenquellen zu veröffentlichen.

## Vor dem Start

Erstellen Sie in Tableau ein persönliches Zugriffstoken für das Konto, das veröffentlichen soll: Wählen Sie **My Account Settings** und dann **Personal Access Tokens**. Kopieren Sie das Token-Secret, wenn Tableau es anzeigt, da Tableau es nicht erneut anzeigt. Das Konto benötigt die Berechtigung, Datenquellen in dem Projekt zu veröffentlichen, in dem Sie veröffentlichen möchten.

## Verbindung erstellen

1. Öffnen Sie **Analysieren**, wählen Sie **Tools → Externe Datenverbindungen** und dann **+ Neue Verbindung → Tableau**.
2. Geben Sie den Namen und die Beschreibung der Verbindung ein.
3. Geben Sie die Verbindungseinstellungen ein:

| Feld | Einzugebender Wert |
| --- | --- |
| **Server-URL** | Die Adresse des Servers oder des Tableau-Cloud-Pods, etwa `https://prod-useast-a.online.tableau.com`. Ein reiner Host wird als `https` gelesen, und eine `http`-Adresse wird abgelehnt. |
| **Site** | Die Content-URL der Site, der Teil der Browser-Adresse nach `#/site/`. Lassen Sie das Feld für die Standard-Site leer. |
| **Name des persönlichen Zugriffstokens** | Der Name, den Sie dem Token in Tableau gegeben haben. |
| **Secret des persönlichen Zugriffstokens** | Das Token-Secret. Es wird verschlüsselt gespeichert und beim erneuten Öffnen der Verbindung leer angezeigt. Lassen Sie es leer, um das gespeicherte Secret beizubehalten. |

4. Wählen Sie **Erstellen**.

Der Server muss aus dem Internet erreichbar sein. PlaidCloud stellt keine Verbindung zu einem Tableau-Server in einem privaten Netzwerk her.

## Verwandte Themen

- [Publish to Tableau](/de/reference/workflow-steps/export/export-to-tableau/)-Schritt
- [Tableau Hyper Export](/de/reference/workflow-steps/export/export-hyper/)-Schritt
