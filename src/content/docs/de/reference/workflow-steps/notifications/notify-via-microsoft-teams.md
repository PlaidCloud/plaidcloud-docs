---
title: Notify via Microsoft Teams
description: Senden Sie aus einem PlaidCloud-Workflow-Schritt Microsoft-Teams-Benachrichtigungen, um Kanäle oder Benutzer über Workflow-Ereignisse und den Status zu informieren.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-microsoft-teams.md
---

Das Hinzufügen von Microsoft-Teams-Benachrichtigungen aus einem Workflow erfolgt in zwei Teilen. Die beiden Teile sind:


1. Eine externe Microsoft-Teams-Verbindung erstellen
2. Microsoft-Teams-Benachrichtigungsschritte zu Ihren Workflows hinzufügen

## Microsoft-Teams-Benachrichtigungsschritt zum Workflow hinzufügen


Das Hinzufügen von Microsoft-Teams-Benachrichtigungsschritten zum Workflow funktioniert genauso wie das Hinzufügen anderer Schritte zu einem Workflow. Öffnen Sie nach dem Hinzufügen des Schritts die Schrittkonfiguration, füllen Sie das Formular aus und speichern Sie es. Sie können Ihre Microsoft-Teams-Benachrichtigung jetzt testen.



## Die Microsoft-Teams-Nachricht formatieren


Teams bietet viele Formatierungsoptionen, darunter das Hinzufügen von Bildern und das Erwähnen von Benutzern. Einzelheiten finden Sie in der Dokumentation [Teams Message Text Formatting](https://support.microsoft.com/en-us/office/use-markdown-formatting-in-teams-4d10bd65-55e2-4b2d-a1f3-2bebdcd2c772).



## Externe Microsoft-Teams-Verbindung erstellen


Dies ist eine einmalige Einrichtung, damit PlaidCloud in Ihrem Namen Microsoft-Teams-Benachrichtigungen senden kann. Microsoft Teams ermöglicht das Erstellen einer Webhook-App (eine generische Möglichkeit, eine Benachrichtigung über das Internet zu senden). Fügen Sie nach dem Erstellen der Webhook-App in Microsoft Teams die bereitgestellten Anmeldedaten in PlaidCloud hinzu, um ihre Verwendung zu ermöglichen.



### Microsoft-Teams-Webhook-App erstellen


Diese Schritte müssen von einem Microsoft-Teams-Administrator ausgeführt werden. Folgen Sie den hier beschriebenen Schritten zum [Erstellen eines eingehenden Webhooks (Microsoft-Teams-Dokumentation)](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook#create-incoming-webhook-1).



### Externe PlaidCloud-Verbindung einrichten


Diese Schritte müssen von einem PlaidCloud-Workspace-Administrator mit Berechtigung zum Erstellen von Externen Datenverbindungen ausgeführt werden. Gehen Sie zum Erstellen der Verbindung wie folgt vor:


1. Navigieren Sie zu `Analyze > Tools > External Data Connections`
2. Wählen Sie unter `+ New Connection` die Option Microsoft-Teams-Webhook
3. Geben Sie Name und Beschreibung ein und fügen Sie die Webhook-URL ein, die beim oben beschriebenen Erstellen des Webhooks erzeugt wurde. Der hier angegebene Name wird im Workflow-Schritt als Auswahl angezeigt und sollte daher möglichst aussagekräftig sein. Jeder, der die URL besitzt, kann in Ihrem Kanal posten; deshalb maskiert das Feld **Webhook-URL** sie beim Einfügen und zeigt sich beim erneuten Öffnen der Verbindung leer; lassen Sie es leer, um die gespeicherte URL beizubehalten.
4. Wählen Sie die Schaltfläche `+ Create`


## Beispiele

Noch keine Beispiele …
