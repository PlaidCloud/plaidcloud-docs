---
title: Workflow erstellen (Anleitung)
description: Erstellen Sie in PlaidCloud einen Workflow und wählen Sie seinen Typ – Standard seriell, Standard parallel oder Erweitert (DAG-Arbeitsfläche) –, um Daten zu laden, zu transformieren und zu exportieren.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/create-workflow.md
---

Um einen neuen Workflow zu erstellen, benötigen Sie ein vorhandenes Projekt. Falls Sie noch keines haben, lesen Sie [Projekte verwalten](/de/guides/projects/managing-projects/).

## Vorgehen

1. Öffnen Sie das Projekt, das den Workflow enthalten soll.
2. Wechseln Sie zur Registerkarte **Workflows**.
3. Klicken Sie in der Symbolleiste auf **Neuer Workflow**.
4. Füllen Sie das Formular aus:
   - **Name** – kurz und aussagekräftig (z. B. „Monatsabschluss – Ist-Werte laden“)
   - **Notiz** – optionale ausführlichere Beschreibung als Kontext
   - **Workflow-Typ** – Standard seriell (Standard), Standard parallel oder Erweitert (DAG-Arbeitsfläche). Siehe [Workflow-Typ auswählen](#workflow-typ-auswählen) weiter unten.
   - **Bei Fehler Korrektur-Workflow auslösen** – optional; aktivieren Sie diese Option, um einen Korrektur-Workflow auszuwählen (siehe [Über Korrektur-Workflows](#über-korrektur-workflows) weiter unten).
5. Klicken Sie auf **Erstellen**.

Der Workflow erscheint auf der Registerkarte „Workflows“ und kann nun mit Schritten befüllt werden. Doppelklicken Sie darauf, um den [Workflow-Explorer](/de/guides/workflows/workflow-explorer/) zu öffnen und mit dem Aufbau zu beginnen.

## Prüfen, wann sich eine Quelltabelle zuletzt geändert hat

In einem Schrittformular zeigt eine Tabellenauswahl unter der ausgewählten Tabelle eine gedämpfte Zeile **Zuletzt aktualisiert** mit Datum und Uhrzeit in Ihrer Ortszeit an, sodass Sie auf einen Blick erkennen, ob die Daten aktuell sind. Zeigen Sie auf die Zeile, um den vollständigen Text zu sehen. Die Zeile wird ausgeblendet, wenn die Auswahl dynamisch ist oder die Tabelle nie aktualisiert wurde.

## Workflow-Typ auswählen

Der **Workflow-Typ**, den Sie beim Erstellen eines Workflows wählen, bestimmt, wie seine Schritte angeordnet und ausgeführt werden. Standardmäßig ist **Standard seriell** eingestellt; Sie legen den Typ über die Typauswahl im Formular „Neuer Workflow“ fest.

| Typ | Wie Schritte angeordnet und ausgeführt werden |
|------|--------------------------------|
| **Standard seriell** | Schritte werden aus der **Schrittliste** nacheinander in der festgelegten Reihenfolge ausgeführt. |
| **Standard parallel** | Schritte werden aus der **Schrittliste** ausgeführt, und zwar parallel, soweit ihre Abhängigkeiten dies zulassen. |
| **Erweitert (DAG-Arbeitsfläche)** | Schritte werden auf einer **visuellen Arbeitsfläche** angeordnet und in Abhängigkeitsreihenfolge ausgeführt, wobei unabhängige Zweige parallel laufen. „Erweitert“ schaltet außerdem Haltepunkte, Container, „Ab hier ausführen“, Simulation und Zusammenarbeit in Echtzeit frei. |

Ein vierter Typ, **Makro** – ein wiederverwendbarer, aufrufbarer Workflow mit deklarierten Ein- und Ausgaben –, folgt in Kürze und wird in der Auswahl deaktiviert angezeigt.

:::note
Ein Schritt kann in einem Workflow nur einmal vorkommen. Das Einfügen, Kopieren, Klonen oder Importieren eines Schritts an eine Position, durch die er ein zweites Mal in einem Workflow platziert würde, wird unter Nennung des Schritts abgelehnt – dieser Zustand kann also künftig nicht mehr entstehen. Enthält ein Workflow aus der Zeit vor dieser Korrektur einen Schritt an zwei Stellen, schlägt eine Ausführung als **Standard seriell** sofort mit einem Fehler fehl, der den doppelten Schritt nennt – ebenso eine Ausführung als **Standard parallel**, die an einem gewählten Endschritt angehalten wird (siehe [Einen Schrittbereich in einem Workflow ausführen](/de/guides/workflows/running-a-range-of-steps-in-a-workflow/)), da auch die Ausführung bis zu einem Endpunkt sequenziell erfolgt. Eine Ausführung als **Standard parallel** bis zum Ende toleriert das Duplikat und führt den Schritt einfach einmal aus. In beiden Fällen reparieren Sie den Workflow, indem Sie den doppelten Schritt löschen – das Entfernen von Schritten ist nie eingeschränkt.
:::

Wählen Sie hier **Erweitert (DAG-Arbeitsfläche)**, wenn Sie den [Visuellen Workflow-Designer](/de/guides/workflows/advanced-workflows/) von Anfang an nutzen möchten. Die Wahl ist nicht endgültig: Einen Standard-Workflow können Sie später in der Workflows-Liste mit **In Erweitert konvertieren…** hochstufen.

## Über Korrektur-Workflows

Wenn der neue Workflow mit einem Fehler endet, kann PlaidCloud automatisch einen **Korrektur-Workflow** als Reaktion ausführen. Das ist nützlich, um:

- eine Benachrichtigung an einen Slack-Kanal, eine E-Mail-Verteilerliste oder einen Webhook zu senden, damit sich jemand um die Ursache kümmert
- einen Rollback- oder Bereinigungs-Workflow auszulösen, der einen bekannten funktionierenden Zustand wiederherstellt
- den Fehler in einer Audit-Tabelle zu protokollieren

Ein Korrektur-Workflow ist optional. Sie können das Feld jetzt leer lassen und ihn bei Bedarf später konfigurieren. Der Korrektur-Workflow wird nur bei endgültigen Fehlern ausgelöst, nicht bei Warnungen einzelner Schritte.

## Nächste Schritte

- [Workflow-Explorer](/de/guides/workflows/workflow-explorer/) – Schritte zu Ihrem neuen Workflow hinzufügen
- [Erweiterte Workflows](/de/guides/workflows/advanced-workflows/) – einen Workflow-Typ wählen und auf der visuellen Arbeitsfläche aufbauen
- [Einen Workflow ausführen](/de/guides/workflows/run-a-workflow/) – den Workflow ausführen, sobald er Schritte enthält
- [Schrittfehler verwalten](/de/guides/workflows/managing-step-errors/) – Fehler beheben
