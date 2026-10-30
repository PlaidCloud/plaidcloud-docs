---
title: Textbenachrichtigungen
description: Melden Sie sich an, um PlaidCloud-Workflow-Benachrichtigungen als Textnachrichten an Ihre US-Mobilfunknummer zu erhalten, und schalten Sie sie wieder aus.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/text-alerts.md
---

Workflows können Ihnen mit dem Schritt [Notify Via SMS](/de/reference/workflow-steps/notifications/notify-via-sms/) eine SMS senden, wenn sie Aufmerksamkeit benötigen. Ein Workflow kann Ihnen erst dann eine SMS senden, nachdem Sie sich selbst angemeldet haben.

## Textbenachrichtigungen einschalten

1. Öffnen Sie das Benutzermenü oben rechts und wählen Sie **Textbenachrichtigungen**.
2. Geben Sie Ihre **US-Mobilfunknummer** ein.
3. Aktivieren Sie **Ich bin damit einverstanden, PlaidCloud-Workflow-SMS-Benachrichtigungen an diese Nummer zu erhalten.** Lesen Sie die darüber stehenden Hinweise sowie die Links **SMS Terms** und **SMS Privacy Policy**.
4. Klicken Sie auf **Code senden**. PlaidCloud sendet einen 6-stelligen Code per SMS an Ihre Nummer. Die Zustellung kann ein bis zwei Minuten dauern.
5. Geben Sie innerhalb von 10 Minuten den **Bestätigungscode** ein und klicken Sie auf **Bestätigen**.

Nachdem Sie einen Code gesendet haben, läuft auf der Schaltfläche ein Countdown von 60 Sekunden, danach lautet sie **Code erneut senden**. Wenn Sie erneut senden, solange Ihr Code noch gültig ist, wird derselbe Code gesendet, sodass jede eintreffende SMS funktioniert. Sie können 3 Codes pro Telefonnummer und Tag sowie 3 pro Person und Stunde anfordern.

Danach lautet das Fenster **Text alerts are on for** gefolgt von Ihrer maskierten Nummer. Es werden nur US-Mobilfunknummern unterstützt. Es können Nachrichten- und Datengebühren anfallen, und die Nachrichtenhäufigkeit variiert.

## Textbenachrichtigungen ausschalten

Öffnen Sie **Textbenachrichtigungen** und klicken Sie auf **SMS-Benachrichtigungen beenden**, oder antworten Sie auf eine beliebige SMS mit **STOP**. Antworten Sie mit **HELP**, um Hilfe zu erhalten.

## Nach STOP wieder einschalten

Eine Antwort mit STOP blockiert jede SMS an Ihre Nummer. Senden Sie **START** per SMS an die im Fenster angezeigte Benachrichtigungsnummer, senden Sie dann einen neuen Code und bestätigen Sie ihn.

## Wenn etwas schiefgeht

| Meldung | Was zu tun ist |
|---|---|
| That code is not right | Prüfen Sie die SMS und geben Sie den Code erneut ein. |
| That code has expired | Klicken Sie auf **Code senden**, um einen neuen anzufordern. |
| Too many wrong codes | Klicken Sie nach 5 falschen Codes auf **Code senden**, um einen neuen anzufordern. |
| Enter a valid US mobile number | Verwenden Sie eine 10-stellige US-Mobilfunknummer. |
| Too many requests | Sie haben ein Codelimit erreicht. Warten Sie einige Minuten und versuchen Sie es erneut. |
| Text alerts are not available for your workspace right now | Versuchen Sie es später erneut. |

Verwenden Sie Textbenachrichtigungen nicht für personenbezogene Gesundheits- oder Finanzdaten. Fragen: support@plaidcloud.com.
