---
title: Einen Workflow ausführen
description: Führen Sie einen PlaidCloud-Workflow manuell oder bei Bedarf aus, verfolgen Sie den Status jedes Schritts und halten Sie eine Ausführung an, beenden Sie sie oder setzen Sie sie dort fort, wo sie aufgehört hat.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Sie können eine vollständige Workflow-Ausführung starten, indem Sie in der Hierarchie **Workflows** auf das Symbol „Ausführen“ klicken oder im Menü **Aktionen** eines bestimmten Workflows **Run All** auswählen.



Sie können auch oben in der Workflow-Tabelle auf die Schaltfläche **Toggle Start/Stop** klicken. Mit dieser Umschaltfläche beenden Sie einen laufenden Workflow oder starten einen Workflow.

Wenn Sie bei einem Workflow, der bereits läuft, auf **Ausführen** klicken, teilt PlaidCloud Ihnen das mit, statt eine zweite Ausführung zu starten.

## Buchungsmodus wählen

Jede Ausführung hat einen ERP-Buchungsmodus. Um in PlaidCloud einen Modus zu wählen, verwenden Sie **Mit Buchungsmodus ausführen** im Kontextmenü eines Workflows oder die Schaltfläche für den Ausführungsmodus auf der Arbeitsfläche des Workflows; **Workflow starten** oder **Workflow ausführen** ohne Modusauswahl fordert Live an, weiterhin begrenzt durch die unten beschriebene Obergrenze des Projekts. Sie können den Modus auch wählen, wenn Sie eine Ausführung über die Ausführungs-API oder den Assistenten starten.

| Modus | Was passiert |
|---|---|
| Live | Buchungsschritte buchen genau so, wie sie es schon immer getan haben. Dies ist der Standard. |
| Simulation | Jeder ERP-Buchungsschritt erstellt und validiert genau das, was er buchen würde, schreibt dann aber nichts fest und kontaktiert das ERP nie. Die Buchungen, die gebucht würden, werden in der [ERP-Buchungshistorie](/de/guides/connections/erp-post-history/) als simuliert gekennzeichnet erfasst, sodass Sie sie prüfen können, bevor Sie live ausführen. |
| Aus | Buchungsschritte werden vollständig übersprungen. |

Ein Projekt hat außerdem eine eigene Obergrenze für den Buchungsmodus. Sie wird über die Projekt-API oder den Assistenten von jedem Mitglied mit Schreibzugriff auf ein nicht gesperrtes Projekt festgelegt. Die Obergrenze macht eine Ausführung immer nur sicherer, nie freizügiger: Der wirksame Modus einer Ausführung ist der restriktivere aus dem von Ihnen gewählten Modus und der Obergrenze des Projekts. Ein Projekt mit der Obergrenze Simulation bleibt daher simuliert, selbst wenn Sie die Ausführung als Live starten.

Ein [geplantes Ereignis](/de/administration/scheduled-events/event-scheduler/#erp-buchungsmodus) behält seinen eigenen Buchungsmodus. Ein Zeitplan, der auf Simulation eingestellt ist, wird also bei jedem Auslösen simuliert ausgeführt.

Der Modus gilt für alles, was die Ausführung berührt. Ein Unter-Workflow, ein Makro und jeder Schritt vom Typ **Run Model**, **Conditional Run Model** oder **Loop Model** erben den Modus der übergeordneten Ausführung, ebenso eine Ausführung, die Sie nach einem Beenden [fortsetzen](#anhalten-beenden-und-fortsetzen). Eine simulierte Ausführung kann also nirgendwo in sich selbst echt buchen.

:::caution
SAP-Buchungs-, SAP-Anhangs- und generische SAP-RFC-Schritte führen keinen Probelauf durch. In den Modi Simulation oder Aus werden sie vollständig übersprungen, denn die eigenen Testkennzeichen von SAP öffnen trotzdem eine echte Verbindung zu SAP. Nur das Überspringen des Schritts stellt sicher, dass eine simulierte Ausführung SAP nie erreicht.
:::

:::note
Ein einzelner ERP-Buchungsschritt hat außerdem eine eigene Einstellung „Nur validieren“ (bei manchen Schritten als Vorschau oder Nur-Test-Modus bezeichnet), unabhängig vom oben beschriebenen Buchungsmodus der Ausführung. Der Schritt-Editor speichert diese Einstellung immer explizit. Eine auf andere Weise geschriebene Schrittkonfiguration, etwa über die REST-API, MCP oder einen Workflow-Bundle-Import, die diese Einstellung ganz weglässt, ist jetzt ebenfalls standardmäßig eine Vorschau statt einer echten Buchung.
:::

## Das Projekt zum Buchen autorisieren

Eine Workflow-Ausführung bucht im ERP als das Projekt, nicht als die Person, die sie gestartet hat. Bevor eine Ausführung buchen kann, benötigt das Projekt eine Autorisierung für jede ERP-Verbindung und Umgebung, die seine Buchungsschritte verwenden. Ohne sie schlägt der Schritt mit der Meldung „This project isn't authorized to post to connection …“ fehl und nennt die Verbindung und die Umgebung. Die Schritte **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** und **Call SAP RFC** benötigen keine.

Um ein Projekt zu autorisieren, öffnen Sie dessen Startseite und wählen unter **ERP-Buchung** die Option **ERP-Schreibautorisierungen**. Jede Zeile ist eine Verbindung in einer Umgebung. Aktivieren Sie **Autorisiert**, damit das Projekt dort buchen darf, oder deaktivieren Sie es, um das zu beenden. **Autorisiert von** und **Autorisiert am** zeigen, wer zuletzt autorisiert hat und wann.

- Die Schaltfläche wird den Architects des Projekts und den Workspace-Administratoren angezeigt, aber nur ein Architect kann eine Autorisierung ändern, und nur solange das Projekt nicht gesperrt ist. Ein Workspace-Administrator, der kein Architect ist, kann sich zuvor selbst als Architect hinzufügen.
- Wenn Sie eine Zeile auswählen, um sie zu autorisieren oder die Autorisierung zu entziehen, wird die Liste nicht neu geladen: Die Bildlaufposition und die gewählte Spaltensortierung bleiben erhalten. Die Größe des Fensters kann geändert werden, und der Hinweis zu öffentlichen Projekten wird vollständig umbrochen.
- Um eine Verbindung zu autorisieren, benötigen Sie selbst Schreibzugriff darauf: Sie sind Eigentümer, oder sie ist namentlich oder über eine Ihrer Sicherheitsgruppen für Sie freigegeben. Eine Verbindung, die auf **Alle Arbeitsbereichsmitglieder** eingestellt ist, zählt nicht.
- Ein Projekt, das auf **Alle Arbeitsbereichsmitglieder** eingestellt ist, wird wie jedes andere autorisiert. Jedes Mitglied ist Architect dieses Projekts, daher kann jedes Mitglied mit Schreibzugriff auf eine Verbindung das Projekt dafür autorisieren. Sobald es autorisiert ist, kann jedes Mitglied aus den Workflows des Projekts in diese Verbindung buchen, und das Fenster weist oberhalb des Rasters darauf hin.
- Ein kopiertes Projekt oder eines, das aus einem Projektarchiv erstellt wurde, beginnt ohne Autorisierungen. Autorisieren Sie die Kopie, bevor sie bucht.

## Den Status eines Schritts verfolgen

Während ein Workflow läuft, zeigt jeder Schritt ein Statussymbol, das seinen Stand anzeigt, zusammen mit der bisherigen Laufzeit. Bewegen Sie den Mauszeiger über das Symbol, um die zugehörige Meldung zu sehen.

| Status | Bedeutung |
|---|---|
| Wartend | Der Schritt ist in der Warteschlange und hat noch nicht begonnen. |
| Wird ausgeführt | Der Schritt arbeitet, und seine Dauer zählt hoch. |
| Abgeschlossen | Der Schritt wurde erfolgreich beendet. |
| Warnung | Der Schritt wurde beendet, hat aber etwas gemeldet, das im [Workflow-Protokoll](/de/guides/workflows/viewing-workflow-log/) lesenswert ist. |
| Fehler | Der Schritt ist fehlgeschlagen. Siehe [Schrittfehler verwalten](/de/guides/workflows/managing-step-errors/). |
| Übersprungen | Der Schritt wurde übergangen, weil er deaktiviert ist oder seine Ausführungsbedingungen nicht erfüllt wurden. Siehe [Schritte in einem Workflow überspringen](/de/guides/workflows/skip-steps-in-a-workflow/). |
| Fortgesetzt | Der Schritt ist fehlgeschlagen, ist aber so eingestellt, dass bei einem Fehler fortgefahren wird, sodass der Workflow weitergelaufen ist. Siehe [Bei Fehler fortfahren](/de/guides/workflows/continue-on-error/). |
| Beendet | Die Ausführung wurde beendet, bevor der Schritt abgeschlossen werden konnte. |
| Verworfen | Die Ausführung des Schritts wurde unterbrochen, sodass er nie abgeschlossen wird. Setzen Sie die Ausführung fort oder führen Sie den Workflow erneut aus. |

Eine geöffnete Workflow-Ansicht aktualisiert sich im Verlauf einer Ausführung selbstständig, sodass die angezeigten Status aktuell bleiben, ohne dass Sie die Seite neu laden müssen.

### Verworfene Schritte

Ein Schritt wird als **verworfen** markiert, wenn das, was ihn ausgeführt hat, mitten in der Ausführung verschwunden ist, meist weil jemand **Beenden** gedrückt hat oder weil Plattformwartungsarbeiten die Ausführung unterbrochen haben. Die Dauer des Schritts zählt nicht weiter hoch, und der Tooltip des Status erklärt, was passiert ist.

Ein verworfener Schritt wurde nicht abgeschlossen und hat keine Ausgabe erzeugt. Er ist kein langsamer Schritt, und es liegt kein Problem mit Ihren Daten oder Ihrer Konfiguration vor.

Um die Arbeit wieder aufzunehmen, [**setzen Sie die Ausführung fort**](#anhalten-beenden-und-fortsetzen) (der verworfene Schritt wird erneut ausgeführt) oder führen Sie den gesamten Workflow erneut aus. Beides ist unbedenklich.

### Unterbrochene Schritte

Geht der Server, der einen Schritt ausführt, mitten in der Ausführung verloren, führt PlaidCloud den Schritt automatisch erneut aus, wenn eine Wiederholung sicher ist: Ein Schritt, der seine Ausgabe ersetzt, liefert dasselbe Ergebnis wie eine einzelne saubere Ausführung, sodass Sie nichts prüfen müssen.

Ein Schritt, der nicht sicher wiederholt werden kann, wird nicht erneut ausgeführt. Er schlägt einmalig mit einer Meldung **Unterbrochen** fehl, weil eine zweite Ausführung duplizieren könnte, was der erste Versuch bereits geschrieben hat. Schritte, die Ausgaben mit `{date}` im Namen oder Pfad schreiben, gelten als nicht sicher wiederholbar, da eine erneute Ausführung auf einem anderen Datum landen könnte. Prüfen Sie zur Wiederherstellung im Ziel des Schritts, was der erste Versuch geschrieben hat, bereinigen Sie es bei Bedarf und [führen Sie den Schritt dann erneut aus](/de/guides/workflows/running-one-step-in-a-workflow/) oder **setzen Sie die Ausführung fort**.

### Schritte, die nie starten

Wenn innerhalb von etwa 40 Minuten kein Worker den Auftrag eines Import- oder Dimensionsschritts übernimmt, schlägt der Schritt fehl, statt bis zum Timeout nach 24 Stunden **Wird ausgeführt** anzuzeigen. Hat ein Worker den Auftrag gestartet und ist dann verschwunden, schlägt der Schritt ebenfalls fehl, mit einer Meldung, dass der Worker beendet wurde. Beide Meldungen enthalten den Satz „Use Run from here to retry.“

## Anhalten, Beenden und Fortsetzen

Während ein Workflow läuft, können Sie ihn **anhalten**, sodass Schritte in Bearbeitung abgeschlossen werden und neue Schritte warten, oder ihn **beenden**, wodurch die Schritte in der Warteschlange und alle noch laufenden Import- oder Exportaufträge abgebrochen werden. Import- und Dimensionsschritte, die noch in der Warteschlange standen, werden sauber abgebrochen, sodass sie spätere Importe und Dimensionsladevorgänge im Workspace nicht aufhalten.

**Fortsetzen** nimmt eine angehaltene, beendete oder fehlgeschlagene Ausführung dort wieder auf, wo sie aufgehört hat, statt von vorn zu beginnen. Es ist verfügbar, sobald die letzte Ausführung eines Workflows im Zustand angehalten, beendet oder Fehler endete.

Was „dort, wo sie aufgehört hat“ bedeutet, hängt davon ab, wie der Workflow ausgeführt wird:

| Ausführung | Beim Fortsetzen |
|---|---|
| Seriell | Beginnt bei dem Schritt, der beim Ende der Ausführung lief, und läuft von dort weiter. Befindet sich dieser Schritt in einer Gruppe, setzt Fortsetzen die gesamte übergeordnete Gruppe der obersten Ebene fort: Schritte der Gruppe, die bereits erfolgreich abgeschlossen wurden, bleiben unberührt, die übrigen werden ausgeführt, und die Ausführung läuft nach der Gruppe weiter. |
| Parallel | Führt jeden Schritt erneut aus, der noch nicht erfolgreich abgeschlossen war, und lässt abgeschlossene Schritte unberührt. |
| Erweitert (Graph) | Führt den fehlgeschlagenen Knoten und alles, was noch auf ihn wartet, erneut aus und lässt abgeschlossene Knoten unberührt. |

Schritte, die einen anderen Workflow aufrufen (**Run Model**, **Conditional Run Model** und **Loop Model**), setzen den aufgerufenen Workflow fort, statt ihn neu zu starten, und zwar über beliebig viele Verschachtelungsebenen. Ein Schleifenschritt setzt die unterbrochene Iteration fort und überspringt die bereits abgeschlossenen Iterationen.

Wenn Sie einen Workflow fortsetzen, der als **verschachtelter untergeordneter Workflow** eines anderen lief, den ein **Run Model**-Schritt in einem übergeordneten Workflow aufgerufen hat, bietet PlaidCloud **Von Kettenanfang fortsetzen** an. Das alleinige Fortsetzen des untergeordneten Workflows kann die Orchestrierung des übergeordneten nicht fortführen. Diese Option setzt daher stattdessen den übergeordneten Workflow der obersten Ebene fort, die Wurzel der Kette, und führt die gesamte Kette von der Stelle weiter, an der sie angehalten hat. Das Fortsetzen eines Workflows der obersten Ebene ändert sich nicht. Der Kettenanfang wird innerhalb desselben Projekts ermittelt: Eine Kette, die in ein anderes Projekt hineinreicht, wird vom Anfang des Teils innerhalb des Projekts fortgesetzt.

Fortsetzen führt immer die **ursprüngliche** Ausführung weiter. Es führt jeden Schritt dieser Ausführung erneut aus, der nicht erfolgreich abgeschlossen wurde. Ein fehlgeschlagener oder verworfener Schritt wird erneut ausgeführt und nicht als abgeschlossen behandelt. Auch die zwischenzeitliche erneute Ausführung eines einzelnen Schritts ändert nichts daran, was Fortsetzen als Nächstes aufgreift.

Eine fortgesetzte Ausführung wird im Ausführungsverlauf des Workflows als **neue Ausführung** erfasst, die nur die Schritte enthält, die sie erneut ausgeführt hat. Die ursprüngliche Ausführung behält ihren eigenen Verlaufseintrag.

:::note
Ein Schleifenschritt ordnet seine abgeschlossenen Iterationen anhand ihrer Variablenwerte zu. Haben sich die Daten, über die die Schleife iteriert, zwischen der ursprünglichen Ausführung und dem Fortsetzen geändert, werden Iterationen, die nicht mehr zugeordnet werden können, erneut ausgeführt statt übersprungen.
:::
