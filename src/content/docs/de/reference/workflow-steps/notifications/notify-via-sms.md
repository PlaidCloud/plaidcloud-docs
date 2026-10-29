---
title: Notify Via SMS
description: Senden Sie aus einem Workflow-Schritt eine SMS an Workspace-Mitglieder, die Textbenachrichtigungen zugestimmt haben, mit Zustellbestätigung, E-Mail-Ersatz, Zusammenfassen von Wiederholungen und Ruhezeiten.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-sms.md
---

## Beschreibung

Senden Sie Workspace-Mitgliedern eine SMS, wenn ein Workflow ihre Aufmerksamkeit braucht. Eine SMS geht nur an ein Mitglied, das sich selbst über **Textbenachrichtigungen** im Benutzermenü angemeldet hat, mit einer bestätigten US-Mobilfunknummer. Sie wählen Mitglieder oder eine Verteilerliste aus; eine Telefonnummer geben Sie nie in den Schritt ein. Informationen zur Anmeldung finden Sie unter [Textbenachrichtigungen](/de/guides/workflows/text-alerts/).

SMS sind nur an US-Nummern möglich. Geben Sie in einer SMS keine personenbezogenen Gesundheits- oder Finanzdaten an.

SMS kommen von einer PlaidCloud-Benachrichtigungsnummer und lauten `PlaidCloud [your workspace name]: ` gefolgt von Ihrer Nachricht. Siehe die [SMS-Bedingungen](https://plaidcloud.com/sms-terms/) und die [SMS-Datenschutzerklärung](https://plaidcloud.com/sms-privacy/).

## Empfänger

Wählen Sie **Mitglieder** oder **Verteilerliste**.

- **Mitglieder** listet Ihre Workspace-Mitglieder auf. Jedes zeigt **Angemeldet**, **Nicht angemeldet** oder **Abbestellt – Senden Sie START per SMS an die Benachrichtigungsnummer**.
- **Verteilerliste** sendet eine SMS an jedes Mitglied der Liste, das sich angemeldet hat.

Ein Mitglied, das sich nicht angemeldet hat, erhält keine SMS. Es stellt ein Problem für den Schritt dar (siehe **Wenn eine SMS nicht zugestellt werden kann**) und erhält die Nachricht standardmäßig stattdessen per E-Mail.

## Nachricht

Verfassen Sie die **Nachricht**. Projektvariablen und Workflow-Variablen funktionieren, und **Variable einfügen** fügt jede der folgenden ein:

| Variable | Wert |
|---|---|
| `{workflow_name}` | Der Name des laufenden Workflows |
| `{project_name}` | Der Name des Projekts |
| `{run_url}` | Ein Link zur Ausführung in PlaidCloud |
| `{project}`, `{model}`, `{cloud}`, `{date}` | Die vorhandenen Variablen |

Der Zähler unter der Nachricht zeigt ungefähr, wie viele Zeichen und Segmente die SMS umfasst, einschließlich des Präfixes `PlaidCloud [workspace]:` und des Ausführungslinks. Eine SMS wird nach 3 Segmenten abgeschnitten. Links öffentlicher Link-Kürzungsdienste werden abgelehnt.

## Zustellung

| Einstellung | Was sie bewirkt |
|---|---|
| **Wenn eine SMS nicht zugestellt werden kann** | **Schritt fehlschlagen lassen** (Standard) oder **Warnen und fortfahren**. Eine nicht zugestellte SMS bleibt nie unbemerkt: Sie wird immer im Schritt gemeldet. |
| **Empfängern, deren SMS nicht zugestellt werden kann, eine E-Mail senden** | Standardmäßig aktiviert. Ein Mitglied, dessen SMS fehlschlägt, das sich nicht angemeldet hat oder das sich abgemeldet hat, erhält die Nachricht per E-Mail. |
| **Wiederholungen zusammenfassen für (Minuten)** | Standard 60. Eine Wiederholung derselben Nachricht an dasselbe Mitglied innerhalb dieser Zeit wird nicht gesendet, und die nächste SMS, die hinausgeht, endet mit `(+N similar since HH:MM)`. |
| **SMS in Ruhezeiten zurückhalten** | Wählen Sie Zeiten für **Von** und **bis** sowie eine Zeitzone. Eine SMS, die innerhalb des Zeitfensters hinausginge, wird bis zu dessen Ende zurückgehalten. |

Jedes Mitglied erhält höchstens 20 SMS pro Tag, ein Workspace sendet höchstens 500 SMS und Ersatz-E-Mails pro Tag, und ein Schritt sendet höchstens 50 Mitgliedern gleichzeitig eine SMS.

## Test an mich senden

**Test an mich senden** sendet eine Test-SMS an Ihre eigene Nummer und zeigt das Ergebnis neben der Schaltfläche an. Wenn Sie sich nicht angemeldet haben, öffnet sich das Fenster **Textbenachrichtigungen**, damit Sie das nachholen können.

## Was Empfänger sehen

Jede SMS stammt von der Benachrichtigungsnummer. Die Antwort **STOP** beendet alle SMS von PlaidCloud an diese Nummer, und **HELP** liefert Kontaktinformationen. Nach STOP sendet ein Mitglied **START** per SMS an die Benachrichtigungsnummer, um fortzufahren, und aktiviert die Textbenachrichtigungen dann unter **Textbenachrichtigungen** erneut. Das Schrittformular zeigt neben diesem Mitglied **Abbestellt – Senden Sie START per SMS an die Benachrichtigungsnummer** an, bis es das getan hat.

Workspace-Administratoren sehen den Status der Textbenachrichtigungen jedes Mitglieds, mit maskierter Nummer, auf der Registerkarte **Mitgliedsinformationen** des Mitgliedsfensters. Mitglieder melden sich selbst an und ab; ein Administrator kann das nicht für sie tun.

## Schritte mit eingegebener Nummer

Eine frühere Version dieses Schritts verwendete einen Mobilfunkanbieter und eine eingegebene Telefonnummer. Ein Schritt, der noch so gespeichert ist, lässt den Workflow nicht fehlschlagen und sendet keine SMS an die eingegebene Nummer.

- **Keine Empfänger ausgewählt:** Der Schritt endet mit einer Warnung, *No text was sent: this step still uses the retired mobile provider and number. Open the step, choose members who've opted in to text alerts, and save it.* Es wird nichts gesendet.
- **Mitglieder oder eine Verteilerliste ausgewählt:** Der Schritt sendet diesen Empfängern eine SMS und ignoriert den übrig gebliebenen Anbieter und die Nummer.

Um einen Schritt zu beheben, öffnen Sie ihn, wählen Sie Mitglieder oder eine Verteilerliste aus und speichern Sie.

## Beispiele

Noch keine Beispiele …
