---
title: Hinweise und Zusammenfassungen
description: Benachrichtigen Sie Personen, wenn eine Zahl in einer Panel-App einen Grenzwert überschreitet, oder senden Sie eine geplante Zusammenfassung wichtiger Zahlen per Push-Benachrichtigung, E-Mail, Slack oder Microsoft Teams.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/alerts-and-digests.md
---

Ein **Hinweis** überwacht eine Zahl aus den Daten einer Panel-App und meldet Ihnen sofort, wenn sie einen Grenzwert überschreitet. Eine **Zusammenfassung** sendet jeden Tag oder jede Woche eine kurze Übersicht von bis zu 10 Zahlen. Beide richten Sie in der App in [Panel Studio](/de/guides/panel-apps/studio/) ein, und beide gehören Ihnen: Sie sehen und ändern nur Ihre eigenen.

## Hinweise und Zusammenfassungen öffnen

1. Wählen Sie unter **Meine Panel-Apps** oder auf der Board **Startseite** eines Projekts bei der App **Open in Studio**.
2. Wählen Sie **Alerts & Digests**.

Das Fenster hat die Registerkarten **Alerts** und **Digests**. Die App muss einem Projekt zugewiesen sein, und ihre Tabellen sind die Tabellen in diesem Projekt.

## Eine zu überwachende Zahl definieren

Hinweise und Zusammenfassungen messen eine **KPI**, die Sie aus einer Tabelle im Projekt der App erstellen:

| Feld | Was es festlegt |
|---|---|
| **Tabelle** | Die Tabelle, die gelesen wird. Sie muss erstellt sein. |
| **Messspalte** | Die Spalte, die summiert oder gezählt wird. |
| **Funktion** | `sum`, `avg`, `min`, `max`, `count` oder `count_distinct`. |
| **Filter hinzufügen** | Optionale Bedingungen, die die Zeilen eingrenzen, jeweils eine Spalte, ein Vergleich und ein Wert. Trennen Sie bei *is in* die Werte durch Kommas. **Remove filter** entfernt einen Filter. |

Die Zahl wird immer mit Ihrem eigenen Zugriff auf die Tabelle berechnet, einschließlich [Sicherheit auf Zeilenebene](/de/guides/panel-apps/accessing-data/). Sie sehen oder senden nie einen Wert für Zeilen, die Sie nicht lesen dürfen.

## Einen Hinweis erstellen

1. Wählen Sie auf der Registerkarte **Alerts** die Option **Neu**.
2. Geben Sie einen **Name** ein.
3. Erstellen Sie die KPI.
4. Wählen Sie unter **Alert when the KPI is** `>`, `>=`, `<` oder `<=` und geben Sie einen **Schwellenwert** ein.
5. Legen Sie unter **Senden per** fest, wie Sie benachrichtigt werden (siehe [Kanäle](#kanäle)).
6. Lassen Sie **Aktiviert** angehakt und wählen Sie **Speichern**.

PlaidCloud prüft jeden aktivierten Hinweis einmal pro Stunde. Ein Hinweis wird jedes Mal einmal ausgelöst, wenn die Zahl den Schwellenwert überschreitet, und schweigt dann, bis die Zahl wieder auf der unkritischen Seite liegt und ihn erneut überschreitet. Die Liste zeigt, wann jeder Hinweis zuletzt ausgelöst wurde, und **(off)** hinter dem Namen eines ausgeschalteten Hinweises.

Pro App können Sie bis zu 20 eigene Hinweise haben.

## Eine Zusammenfassung erstellen

1. Wählen Sie auf der Registerkarte **Digests** die Option **Neu**.
2. Geben Sie einen **Name** ein.
3. Wählen Sie **Add KPI**, vergeben Sie ein **KPI label** und erstellen Sie die Zahl. Wiederholen Sie dies für bis zu 10 KPIs. **Remove KPI** entfernt eine KPI.
4. Wählen Sie neben **Senden** die Option **Jeden Tag** oder **Jede Woche**.
5. Legen Sie unter **Senden per** fest, wie die Zusammenfassung gesendet wird, und wählen Sie **Speichern**.

Eine Zusammenfassung wird einmal pro Tag oder Woche versendet, bei der ersten stündlichen Prüfung nach Beginn des Zeitraums, wobei der Zeitraum in UTC gilt. Die Liste zeigt, wann jede Zusammenfassung zuletzt gesendet wurde. Eine KPI, für die Ihr Zugriff auf die Tabelle keine Zeilen übrig lässt, wird als „keine Daten“ angezeigt, nie als ungefilterter Wert.

Sie können pro App bis zu 10 eigene Zusammenfassungen und insgesamt 20 über alle Apps hinweg haben.

## Kanäle

| Senden per | Wohin es geht |
|---|---|
| **Push-Benachrichtigung** | Die mobile PlaidCloud-App auf Ihren Geräten. Nur für Hinweise. |
| **E-Mail** | Die E-Mail-Adresse Ihres Kontos. |
| **Slack** | Ein Slack-Kanal über eine Slack-Verbindung. |
| **Microsoft Teams** | Ein Teams-Kanal über eine Microsoft-Teams-Verbindung. |

Wählen Sie bei **Slack** und **Microsoft Teams** die **Verbindung**, über die gepostet wird. Ein Workspace-Administrator erstellt die Verbindung, und Sie benötigen Zugriff darauf. Die Adresse der Verbindung muss mit `https` beginnen.

### Was eine Slack- oder Teams-Karte zeigt

Eine Karte zeigt die Werte nur, wenn Ihr eigener Zugriff auf die Tabelle uneingeschränkt ist, das heißt, wenn keine Sicherheit auf Zeilenebene die Zeilen begrenzt, die Sie lesen dürfen. Ist Ihr Zugriff auf einige Zeilen beschränkt, teilt die Karte mit, dass neue Werte bereitstehen, und verlinkt auf die App, in der jeder Leser nur die Zeilen sieht, die sein eigener Zugriff erlaubt. Jede Karte enthält einen Link zur App. Die Mitglieder eines Kanals werden außerhalb von PlaidCloud verwaltet, weshalb die Zahlen eines eingeschränkten Eigentümers nicht an einen Kanal gehen.

## Wenn die Zustellung fehlschlägt

Ein Hinweis oder eine Zusammenfassung, der bzw. die 24 Stunden in Folge nicht zugestellt werden kann, zum Beispiel weil die zugehörige Slack-Verbindung entfernt wurde, wird ausgeschaltet. Die Liste zeigt ihn als **(off)**, und das Formular nennt, wie viele Zustellungen fehlgeschlagen sind. Beheben Sie den Kanal, haken Sie **Aktiviert** an und wählen Sie **Speichern**, um ihn wieder einzuschalten.

## Bearbeiten oder löschen

Wählen Sie ein Element in der Liste, um es zu ändern, und dann **Speichern**. Wählen Sie **Löschen**, um es zu entfernen. Wenn Sie das Element wechseln, obwohl ungespeicherte Änderungen vorliegen, fragt PlaidCloud nach, bevor sie verworfen werden.

## Nächste Schritte

- [Panel Studio](/de/guides/panel-apps/studio/) – dort erreichen Sie **Alerts & Digests**.
- [Das Panel App Kit](/de/guides/panel-apps/app-kit/) – erstellen Sie die App, die die Hinweise überwachen.
