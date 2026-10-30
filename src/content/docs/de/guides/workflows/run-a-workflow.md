---
title: Einen Workflow ausführen
description: Führen Sie einen PlaidCloud-Workflow manuell oder bei Bedarf aus, verfolgen Sie den Status der einzelnen Schritte und halten Sie eine Ausführung an, beenden Sie sie oder setzen Sie sie dort fort, wo sie aufgehört hat.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Sie können eine vollständige Workflow-Ausführung starten, indem Sie in der Hierarchie **Workflows** auf das Ausführen-Symbol klicken oder im Menü **Aktionen** eines bestimmten Workflows **Run All** auswählen.



Sie können auch oben in der Workflow-Tabelle auf die Schaltfläche **Toggle Start/Stop** klicken. Mit dieser Umschaltfläche beenden Sie einen laufenden Workflow oder starten einen Workflow.

Wenn Sie auf einem Workflow, der bereits läuft, auf **Ausführen** klicken, weist PlaidCloud Sie darauf hin, anstatt eine zweite Ausführung zu starten.

## Einen Buchungsmodus wählen

Jede Ausführung hat einen ERP-Buchungsmodus. Um in PlaidCloud einen Modus zu wählen, verwenden Sie **Mit Buchungsmodus ausführen** im Kontextmenü eines Workflows oder die Schaltfläche für den Ausführungsmodus auf der Workflow-Arbeitsfläche. Bei **Workflow starten** oder **Workflow ausführen** ohne Modusauswahl wird Live angefordert, weiterhin vorbehaltlich der unten beschriebenen Obergrenze des Projekts. Sie können den Modus auch wählen, wenn Sie eine Ausführung über die Run-API oder den Assistenten starten.

| Modus | Was passiert |
|---|---|
| Live | Buchungsschritte buchen genau so wie bisher. Dies ist der Standard. |
| Simulate | Jeder ERP-Buchungsschritt erstellt und validiert genau das, was er buchen würde, schreibt dann aber nichts fest und nimmt nie Kontakt zum ERP auf. Die Buchungen, die gebucht würden, werden in der [ERP-Buchungshistorie](/de/guides/connections/erp-post-history/) als simuliert gekennzeichnet erfasst, sodass Sie sie vor einer Live-Ausführung prüfen können. |
| Off | Buchungsschritte werden vollständig übersprungen. |

Ein Projekt hat außerdem eine eigene Obergrenze für den Buchungsmodus. Sie wird über die Projekt-API oder den Assistenten von jedem Mitglied mit Schreibzugriff auf ein nicht gesperrtes Projekt festgelegt. Die Obergrenze macht eine Ausführung immer nur sicherer, nie freizügiger: Der effektive Modus einer Ausführung ist der restriktivere aus dem von Ihnen gewählten Modus und der Obergrenze des Projekts. Ein Projekt, dessen Obergrenze auf Simulate gesetzt ist, bleibt also simuliert, auch wenn Sie die Ausführung als Live starten.

Ein [geplantes Ereignis](/de/administration/scheduled-events/event-scheduler/#erp-buchungsmodus) behält seinen eigenen Buchungsmodus. Ein Zeitplan, der auf Simulate gesetzt ist, läuft daher bei jedem Auslösen simuliert.

Der Modus gilt für alles, was die Ausführung berührt. Ein Unter-Workflow, ein Makro und ein Schritt **Run Model**, **Conditional Run Model** oder **Loop Model** erben alle den Modus der übergeordneten Ausführung. Das gilt auch für eine Ausführung, die Sie nach einem Beenden [fortsetzen](#anhalten-beenden-und-fortsetzen): Eine simulierte Ausführung kann nirgendwo in sich selbst real buchen.

:::caution
SAP-Buchungs-, SAP-Anhangs- und generische SAP-RFC-Schritte führen keinen Probelauf durch. Unter Simulate oder Off werden sie komplett übersprungen, weil selbst die Testkennzeichen von SAP eine echte Verbindung zu SAP öffnen. Das Überspringen des Schritts ist die einzige Möglichkeit, sicherzustellen, dass eine simulierte Ausführung SAP nie erreicht.
:::

:::note
Ein einzelner ERP-Buchungsschritt hat außerdem eine eigene Einstellung „Validate Only“ (bei manchen Schritten als „Preview“ oder „Test Only Mode“ bezeichnet), unabhängig vom oben beschriebenen Buchungsmodus der Ausführung. Der Schritt-Editor speichert diese Einstellung immer explizit. Eine auf andere Weise geschriebene Schrittkonfiguration – über die REST-API, MCP oder einen Workflow-Bundle-Import –, in der die Einstellung vollständig fehlt, verwendet jetzt ebenfalls standardmäßig eine Vorschau statt einer Live-Buchung.
:::

## Das Projekt zum Buchen autorisieren

Eine Workflow-Ausführung bucht in ein ERP als das Projekt, nicht als die Person, die sie gestartet hat. Bevor eine Ausführung buchen kann, benötigt das Projekt eine Autorisierung für jede ERP-Verbindung und Umgebung, die seine Buchungsschritte verwenden. Ohne sie schlägt der Schritt mit der Meldung „This project isn't authorized to post to connection …“ fehl und nennt die Verbindung und die Umgebung. Die Schritte **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** und **Call SAP RFC** benötigen keine Autorisierung.

Um ein Projekt zu autorisieren, öffnen Sie dessen Startseite und wählen unter **ERP-Buchung** den Eintrag **ERP-Schreibautorisierungen**. Jede Zeile ist eine Verbindung in einer Umgebung. Aktivieren Sie **Autorisiert**, damit das Projekt dort buchen darf, oder deaktivieren Sie das Kontrollkästchen, um dies zu beenden. **Autorisiert von** und **Autorisiert am** zeigen, wer zuletzt autorisiert hat und wann.

- Die Schaltfläche wird den Architects des Projekts und den Workspace-Administratoren angezeigt, aber nur ein Architect kann eine Autorisierung ändern, und zwar nur, solange das Projekt nicht gesperrt ist. Ein Workspace-Administrator, der kein Architect ist, kann sich zuvor selbst als Architect hinzufügen.
- Wenn Sie eine Zeile auswählen, um sie zu autorisieren oder die Autorisierung aufzuheben, wird die Liste nicht neu geladen: Die Bildlaufposition und eine von Ihnen gewählte Spaltensortierung bleiben erhalten. Die Größe des Fensters lässt sich ändern, und der Hinweis zu öffentlichen Projekten wird vollständig umbrochen.
- Um eine Verbindung zu autorisieren, benötigen Sie selbst ebenfalls Schreibzugriff auf sie: Sie besitzen sie, oder sie ist namentlich oder über eine Ihrer Sicherheitsgruppen für Sie freigegeben. Eine Verbindung, die auf **Alle Arbeitsbereichsmitglieder** gesetzt ist, zählt nicht.
- Ein Projekt, das auf **Alle Arbeitsbereichsmitglieder** gesetzt ist, wird wie jedes andere autorisiert. Jedes Mitglied ist Architect dieses Projekts, daher kann jedes Mitglied mit Schreibzugriff auf eine Verbindung das Projekt dafür autorisieren. Sobald es autorisiert ist, kann jedes Mitglied aus den Workflows des Projekts in diese Verbindung buchen, und das Fenster weist oberhalb des Rasters darauf hin.
- Ein kopiertes Projekt oder ein Projekt, das aus einem Projektarchiv erstellt wurde, startet ohne Autorisierungen. Autorisieren Sie die Kopie, bevor sie bucht.

## Den Status eines Schritts verfolgen

Während ein Workflow läuft, zeigt jeder Schritt ein Statussymbol, das anzeigt, wo er steht, zusammen mit der bisherigen Laufzeit. Bewegen Sie den Mauszeiger über das Symbol, um die zugehörige Meldung zu sehen.

| Status | Bedeutung |
|---|---|
| Wartend | Der Schritt ist eingereiht und hat noch nicht begonnen. |
| Läuft | Der Schritt arbeitet, und seine Dauer zählt hoch. |
| Abgeschlossen | Der Schritt wurde erfolgreich beendet. |
| Warnung | Der Schritt wurde beendet, hat aber etwas gemeldet, das im [Workflow-Protokoll](/de/guides/workflows/viewing-workflow-log/) lesenswert ist. |
| Fehler | Der Schritt ist fehlgeschlagen. Siehe [Schrittfehler verwalten](/de/guides/workflows/managing-step-errors/). |
| Übersprungen | Der Schritt wurde übergangen – er ist deaktiviert, oder seine Ausführungsbedingungen waren nicht erfüllt. Siehe [Schritte in einem Workflow überspringen](/de/guides/workflows/skip-steps-in-a-workflow/). |
| Fortgesetzt | Der Schritt ist fehlgeschlagen, ist aber so eingestellt, dass bei einem Fehler fortgefahren wird, sodass der Workflow weiterlief. Siehe [Bei Fehler fortfahren](/de/guides/workflows/continue-on-error/). |
| Beendet | Die Ausführung wurde beendet, bevor der Schritt abgeschlossen werden konnte. |
| Abgebrochen | Die Ausführung des Schritts wurde unterbrochen, sodass er nie abgeschlossen wird. Setzen Sie die Ausführung fort oder führen Sie den Workflow erneut aus. |

Eine geöffnete Workflow-Ansicht wird im Verlauf einer Ausführung automatisch aktualisiert, sodass die angezeigten Status aktuell bleiben, ohne dass Sie die Seite neu laden müssen.

### Abgebrochene Schritte

Ein Schritt wird als **abgebrochen** markiert, wenn das, was ihn ausgeführt hat, mitten in der Ausführung verschwunden ist – meist weil jemand auf **Beenden** gedrückt hat oder weil Plattformwartungen die Ausführung unterbrochen haben. Die Dauer des Schritts steigt nicht weiter, und der QuickInfo-Text zum Status erklärt, was passiert ist.

Ein abgebrochener Schritt wurde nicht abgeschlossen und hat keine Ausgabe erzeugt. Er ist kein langsamer Schritt, und es liegt auch kein Problem mit Ihren Daten oder Ihrer Konfiguration vor.

Um die Arbeit wieder aufzunehmen, können Sie die Ausführung entweder [**fortsetzen**](#anhalten-beenden-und-fortsetzen) – der abgebrochene Schritt wird dann erneut ausgeführt – oder den gesamten Workflow erneut ausführen. Beides ist unbedenklich.

### Unterbrochene Schritte

Geht der Server, der einen Schritt ausführt, mitten in der Ausführung verloren, führt PlaidCloud den Schritt automatisch erneut aus, wenn eine Wiederholung sicher ist: Ein Schritt, der seine Ausgabe ersetzt, liefert dasselbe Ergebnis wie eine einzelne saubere Ausführung, sodass Sie nichts prüfen müssen.

Ein Schritt, der nicht sicher wiederholt werden kann, wird nicht erneut ausgeführt. Er schlägt einmalig mit der Meldung **unterbrochen** fehl, weil eine zweite Ausführung duplizieren könnte, was der erste Versuch bereits geschrieben hat. Schritte, die Ausgaben mit `{date}` im Namen oder Pfad schreiben, gelten als nicht sicher wiederholbar, da eine erneute Ausführung auf einem anderen Datum landen könnte. Zur Wiederherstellung prüfen Sie das Ziel des Schritts auf das, was der erste Versuch geschrieben hat, bereinigen es bei Bedarf und [führen den Schritt dann erneut aus](/de/guides/workflows/running-one-step-in-a-workflow/) oder **setzen** die Ausführung **fort**.

## Anhalten, Beenden und Fortsetzen

Während ein Workflow läuft, können Sie ihn **anhalten**, sodass laufende Schritte abgeschlossen werden und neue Schritte warten, oder **beenden**, wodurch die eingereihten Schritte und alle noch laufenden Import- oder Exportjobs abgebrochen werden.

**Fortsetzen** nimmt eine angehaltene, beendete oder fehlgeschlagene Ausführung dort wieder auf, wo sie aufgehört hat, anstatt von vorn zu beginnen. Es steht zur Verfügung, wenn die letzte Ausführung eines Workflows in einem angehaltenen, beendeten oder fehlerhaften Zustand endete.

Was „dort, wo sie aufgehört hat“ bedeutet, hängt davon ab, wie der Workflow ausgeführt wird:

| Ausführung | Beim Fortsetzen |
|---|---|
| Seriell | Startet bei dem Schritt neu, der lief, als die Ausführung endete, und läuft von dort weiter. Befindet sich dieser Schritt in einer Gruppe, setzt Fortsetzen die gesamte übergeordnete Gruppe der obersten Ebene fort: Schritte der Gruppe, die bereits erfolgreich abgeschlossen wurden, bleiben unberührt, die übrigen werden ausgeführt, und die Ausführung läuft nach der Gruppe weiter. |
| Parallel | Führt jeden Schritt erneut aus, der noch nicht erfolgreich abgeschlossen war, und lässt abgeschlossene Schritte unberührt. |
| Erweitert (Graph) | Führt den fehlgeschlagenen Knoten und alles, was noch auf ihn wartet, erneut aus und lässt abgeschlossene Knoten unberührt. |

Schritte, die einen anderen Workflow aufrufen – **Run Model**, **Conditional Run Model** und **Loop Model** –, setzen den von ihnen aufgerufenen Workflow fort, anstatt ihn neu zu starten, und zwar über beliebig viele Verschachtelungsebenen. Ein Schleifenschritt setzt die unterbrochene Iteration fort und überspringt die bereits abgeschlossenen Iterationen.

Wenn Sie einen Workflow fortsetzen, der als **verschachtelter untergeordneter Workflow** eines anderen lief – aufgerufen von einem Schritt **Run Model** in einem übergeordneten Workflow –, bietet PlaidCloud **Von Kettenanfang fortsetzen** an. Das alleinige Fortsetzen des untergeordneten Workflows kann die Orchestrierung des übergeordneten nicht fortführen. Diese Option setzt daher stattdessen den übergeordneten Workflow der obersten Ebene fort – die Wurzel der Kette – und führt die gesamte Kette dort weiter, wo sie angehalten wurde. Das Fortsetzen eines Workflows der obersten Ebene bleibt unverändert. Der Kettenanfang wird innerhalb desselben Projekts bestimmt: Eine Kette, die in ein anderes Projekt hineinreicht, wird vom Anfang des Teils innerhalb des Projekts fortgesetzt.

Fortsetzen setzt immer die **ursprüngliche** Ausführung fort. Es führt jeden Schritt dieser Ausführung erneut aus, der nicht erfolgreich abgeschlossen wurde – ein fehlgeschlagener oder abgebrochener Schritt wird erneut ausgeführt und nicht als abgeschlossen behandelt –, und die zwischenzeitliche erneute Ausführung eines einzelnen Schritts ändert nichts daran, was Fortsetzen als Nächstes aufgreift.

Eine fortgesetzte Ausführung wird im Ausführungsverlauf des Workflows als **neue Ausführung** erfasst und enthält nur die Schritte, die sie erneut ausgeführt hat. Die ursprüngliche Ausführung behält ihren eigenen Verlaufseintrag.

:::note
Ein Schleifenschritt ordnet seine abgeschlossenen Iterationen anhand ihrer Variablenwerte zu. Haben sich die Daten, über die die Schleife iteriert, zwischen der ursprünglichen Ausführung und dem Fortsetzen geändert, werden Iterationen, die nicht mehr zugeordnet werden können, erneut ausgeführt statt übersprungen.
:::
