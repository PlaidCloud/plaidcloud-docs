---
title: Notify via Slack
description: Senden Sie aus einem PlaidCloud-Workflow-Schritt Slack-Benachrichtigungen, um Kanäle oder Benutzer über Workflow-Ereignisse, Fehler und den Status zu informieren.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-slack.md
---

Das Hinzufügen von Slack-Benachrichtigungen aus einem Workflow erfolgt in zwei Teilen. Die beiden Teile sind:


1. Eine externe Slack-Webhook-Verbindung erstellen
2. Slack-Benachrichtigungsschritte zu Ihren Workflows hinzufügen

## Slack-Benachrichtigungsschritt zum Workflow hinzufügen


Das Hinzufügen von Slack-Benachrichtigungsschritten zum Workflow funktioniert genauso wie das Hinzufügen anderer Schritte zu einem Workflow. Öffnen Sie nach dem Hinzufügen des Schritts die Schrittkonfiguration, füllen Sie das Formular aus und speichern Sie es. Sie können Ihre Slack-Benachrichtigung jetzt testen.



## Eine Datei anhängen

Wählen Sie unter **Hochzuladende Datei** ein Dokument aus, um es mit der Nachricht als Kommentar an den Kanal zu senden. Ein Webhook kann keine Datei übertragen, daher läuft ein Anhang über ein Bot-Token der Slack-Verbindung:

- Fügen Sie der Verbindung ein **Bot-Token** hinzu. Es ist das `xoxb-`-Token einer Slack-App mit dem Scope `files:write`, und die App muss in den Kanal eingeladen sein.
- Geben Sie im Schritt die **Kanal-ID** ein, etwa `C0123ABCD`, keinen Kanalnamen. Der Datei-Upload von Slack akzeptiert nur IDs, und der Schritt schlägt ohne eine fehl. Um eine ID zu finden, öffnen Sie in Slack die Details des Kanals und scrollen Sie ganz nach unten.
- Wird das Dokument nicht gefunden, wird die Nachricht ohne es per Webhook gesendet, und der Schritt warnt mit dem Pfad des Dokuments.

## Die Slack-Nachricht formatieren


Slack bietet viele Formatierungsoptionen, darunter das Hinzufügen von Bildern und das Erwähnen von Benutzern. Einzelheiten finden Sie in der Dokumentation [Slack Text Formatting](https://api.slack.com/reference/surfaces/formatting).



## Externe Slack-Webhook-Verbindung erstellen


Dies ist eine einmalige Einrichtung, damit PlaidCloud in Ihrem Namen Slack-Benachrichtigungen senden kann. Slack ermöglicht das Erstellen einer Webhook-App (eine generische Möglichkeit, eine Benachrichtigung über das Internet zu senden). Fügen Sie nach dem Erstellen der Webhook-App in Slack die bereitgestellten Anmeldedaten in PlaidCloud hinzu, um ihre Verwendung zu ermöglichen.



### Slack-Webhook-App erstellen


Diese Schritte müssen von einem Slack-Administrator ausgeführt werden. Gehen Sie zum Erstellen einer Slack-Webhook-App wie folgt vor:


1. Öffnen Sie in Slack das Workspace-Steuerungsmenü und wählen Sie `Settings & administration > Manage Apps`
2. Wählen Sie in der Liste der App-Kategorien `Custom Integrations`
3. Wählen Sie in der App-Liste `Incoming Webhooks`
4. Wählen Sie die Schaltfläche `Add to Slack`
5. Wählen Sie auf dem nächsten Bildschirm den Slack-Kanal, in dem die Nachrichten gepostet werden sollen, und fahren Sie fort. Dies ist der Standardkanal, der verwendet wird; er kann in jeder Benachrichtigung überschrieben werden, auch zum Senden von Direktnachrichten an bestimmte Personen.
6. Kopieren Sie die angezeigte Webhook-URL. Sie wird später benötigt, bewahren Sie sie also an einem sicheren Ort auf. Sie sieht etwa so aus: `https://hooks.slack.com/services/T04QZ1435/G02TGBFTOP8/K9GZrR2ThdJz1uSiL9YeZxoR`
7. Vor dem Speichern können Sie Aussehen, Namen und Emoji anpassen. Diese Anpassungen sind nur Standardwerte und können in jedem Benachrichtigungsschritt innerhalb eines PlaidCloud-Workflows überschrieben werden.

### Externe PlaidCloud-Verbindung einrichten


Diese Schritte müssen von einem PlaidCloud-Workspace-Administrator mit Berechtigung zum Erstellen von Externen Datenverbindungen ausgeführt werden. Gehen Sie zum Erstellen der Verbindung wie folgt vor:


1. Navigieren Sie zu `Analyze > Tools > External Data Connections`
2. Wählen Sie unter `+ New Connection` die Option Slack-Webhook
3. Geben Sie Name und Beschreibung ein und fügen Sie die Webhook-URL aus Schritt 6 oben ein. Der hier angegebene Name wird im Workflow-Schritt als Auswahl angezeigt und sollte daher möglichst aussagekräftig sein. Jeder, der die URL besitzt, kann in Ihrem Kanal posten; deshalb maskiert das Feld **Webhook-URL** sie beim Einfügen und zeigt sich beim erneuten Öffnen der Verbindung leer; lassen Sie es leer, um die gespeicherte URL beizubehalten.
4. Um Anhänge zu senden, fügen Sie außerdem das Bot-Token der Slack-App in das Feld **Bot-Token (für Datei-Uploads)** ein. Eine Verbindung kann die Webhook-URL, das Bot-Token oder beides enthalten. Das Bot-Token wird wie die Webhook-URL maskiert und zeigt sich beim erneuten Öffnen der Verbindung leer.
5. Wählen Sie die Schaltfläche `+ Create`


## Beispiele

Noch keine Beispiele …
