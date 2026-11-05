---
title: Einen Workflow ausführen
description: Führen Sie einen PlaidCloud-Workflow manuell oder bei Bedarf aus, verfolgen Sie den Status jedes Schritts und halten Sie eine Ausführung an, beenden Sie sie oder setzen Sie sie dort fort, wo sie unterbrochen wurde.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Sie können eine vollständige Workflow-Ausführung starten, indem Sie in der Hierarchie **Workflows** auf das Symbol „Ausführen“ klicken oder im Menü **Aktionen** eines bestimmten Workflows **Run All** auswählen.



Sie können auch oben in der Workflow-Tabelle auf die Schaltfläche **Toggle Start/Stop** klicken. Mit dieser Umschaltfläche beenden Sie einen laufenden Workflow oder starten einen Workflow.

Wenn Sie bei einem Workflow, der bereits läuft, auf **Ausführen** klicken, weist PlaidCloud Sie darauf hin, anstatt eine zweite Ausführung zu starten.

## Buchungsmodus wählen

Jede Ausführung hat einen ERP-Buchungsmodus. Um in PlaidCloud einen Modus zu wählen, verwenden Sie **Mit Buchungsmodus ausführen** im Kontextmenü eines Workflows oder die Schaltfläche für den Ausführungsmodus auf der Arbeitsfläche des Workflows; **Workflow starten** oder **Workflow ausführen** ohne Modusauswahl fordert Live an, weiterhin begrenzt durch die unten beschriebene Obergrenze des Projekts. Den Modus können Sie auch wählen, wenn Sie eine Ausführung über die Ausführungs-API oder den Assistenten starten.

| Modus | Was passiert |
|---|---|
| Live | Buchungsschritte buchen genau so, wie sie es schon immer getan haben. Dies ist der Standard. |
| Simulate | Jeder ERP-Buchungsschritt erstellt und prüft genau das, was er buchen würde, schreibt dann aber nichts fest und kontaktiert das ERP nie. Die Einträge, die gebucht würden, werden in der [ERP-Buchungshistorie](/de/guides/connections/erp-post-history/) als simuliert markiert aufgezeichnet, damit Sie sie vor der Live-Ausführung prüfen können. |
| Off | Buchungsschritte werden vollständig übersprungen. |

Ein Projekt hat außerdem eine eigene Obergrenze für den Buchungsmodus. Sie wird über die Projekt-API oder den Assistenten von jedem Mitglied mit Schreibzugriff auf ein nicht gesperrtes Projekt festgelegt. Die Obergrenze macht eine Ausführung immer nur sicherer, nie freizügiger: Der wirksame Modus einer Ausführung ist der restriktivere aus dem von Ihnen gewählten Modus und der Obergrenze des Projekts. Ein Projekt mit der Obergrenze Simulate bleibt daher simuliert, auch wenn Sie die Ausführung als Live starten.

Ein [geplantes Ereignis](/de/administration/scheduled-events/event-scheduler/#erp-buchungsmodus) behält seinen eigenen Buchungsmodus, sodass ein Zeitplan mit Simulate bei jedem Auslösen simuliert ausgeführt wird.

Der Modus gilt für alles, was die Ausführung berührt. Ein Unter-Workflow, ein Makro sowie die Schritte **Run Model**, **Conditional Run Model** und **Loop Model** übernehmen alle den Modus der übergeordneten Ausführung, ebenso eine Ausführung, die Sie nach einem Beenden [fortsetzen](#anhalten-beenden-und-fortsetzen) — eine simulierte Ausführung kann nirgendwo in sich selbst real buchen.

:::caution
SAP-Buchungen, SAP-Anhänge und generische SAP-RFC-Schritte führen keinen Probelauf aus. Unter Simulate oder Off werden sie vollständig übersprungen, weil die eigenen Testkennzeichen von SAP trotzdem eine echte Verbindung zu SAP öffnen — nur das Überspringen des Schritts stellt sicher, dass eine simulierte Ausführung SAP nie erreicht.
:::

:::note
Ein einzelner ERP-Buchungsschritt hat außerdem eine eigene Einstellung Validate Only (bei manchen Schritten als Vorschau oder Test Only Mode bezeichnet), unabhängig vom oben beschriebenen Buchungsmodus der Ausführung. Der Schrittdialog speichert diese Einstellung immer explizit. Eine auf andere Weise geschriebene Schrittkonfiguration — über die REST-API, MCP oder einen Workflow-Bundle-Import —, in der die Einstellung ganz fehlt, ergibt jetzt ebenfalls standardmäßig eine Vorschau statt einer Live-Buchung.
:::

## Das Projekt zum Buchen autorisieren

Eine Workflow-Ausführung bucht im ERP als das Projekt, nicht als die Person, die sie gestartet hat. Damit eine Ausführung buchen kann, benötigt das Projekt eine Autorisierung für jede ERP-Verbindung und jede Umgebung, die seine Buchungsschritte verwenden. Ohne sie schlägt der Schritt mit „This project isn't authorized to post to connection …“ fehl und nennt die Verbindung und die Umgebung. Die Schritte **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** und **Call SAP RFC** benötigen keine.

Um ein Projekt zu autorisieren, öffnen Sie dessen Startseite und wählen unter **ERP-Buchung** die Option **ERP-Schreibautorisierungen**. Jede Zeile steht für eine Verbindung in einer Umgebung. Aktivieren Sie **Autorisiert**, damit das Projekt dort buchen darf, oder deaktivieren Sie es, um dies zu beenden. **Autorisiert von** und **Autorisiert am** zeigen, wer zuletzt autorisiert hat und wann.

- Die Schaltfläche wird den Architects des Projekts und den Workspace-Administratoren angezeigt, aber nur ein Architect kann eine Autorisierung ändern, und nur solange das Projekt nicht gesperrt ist. Ein Workspace-Administrator, der kein Architect ist, kann sich zuvor selbst als Architect hinzufügen.
- Wenn Sie eine Zeile auswählen, um sie zu autorisieren oder die Autorisierung aufzuheben, wird die Liste nicht neu geladen: Die Bildlaufposition und die gewählte Spaltensortierung bleiben erhalten. Die Größe des Fensters kann geändert werden, und der Hinweis zu öffentlichen Projekten wird vollständig umbrochen.
- Um eine Verbindung zu autorisieren, benötigen Sie selbst ebenfalls Schreibzugriff darauf: Sie besitzen sie, oder sie ist namentlich oder über eine Ihrer Sicherheitsgruppen für Sie freigegeben. Eine Verbindung, die auf **Alle Arbeitsbereichsmitglieder** gesetzt ist, zählt nicht.
- Ein Projekt, das auf **Alle Arbeitsbereichsmitglieder** gesetzt ist, wird wie jedes andere autorisiert. Jedes Mitglied ist Architect des Projekts, sodass jedes Mitglied mit Schreibzugriff auf eine Verbindung das Projekt dafür autorisieren kann. Sobald es autorisiert ist, kann jedes Mitglied aus den Workflows des Projekts auf diese Verbindung buchen, und das Fenster weist oberhalb des Rasters darauf hin.
- Eine neue Kopie, die nur für Sie privat ist und mit Tabellendaten oder Dimensionsmitgliedern erstellt wurde, behält die Autorisierungen der Quelle, die Sie selbst erteilen könnten, und kommt in Simulate an, wenn die Quelle Live war — siehe [ERP-Schreibautorisierungen in der Kopie](/de/guides/projects/managing-projects/#erp-schreibautorisierungen-in-der-kopie). Jede andere Kopie und jedes aus einem Projektarchiv erstellte Projekt beginnt ohne Autorisierungen. Autorisieren Sie es, bevor es bucht.

## Status eines Schritts verfolgen

Während ein Workflow läuft, zeigt jeder Schritt ein Statussymbol, das seinen Stand angibt, sowie seine bisherige Laufzeit. Bewegen Sie den Mauszeiger über das Symbol, um die zugehörige Meldung zu sehen.

| Status | Bedeutung |
|---|---|
| Wartend | Der Schritt befindet sich in der Warteschlange und hat noch nicht begonnen. |
| Läuft | Der Schritt arbeitet, und seine Dauer läuft hoch. |
| Abgeschlossen | Der Schritt wurde erfolgreich beendet. |
| Warnung | Der Schritt wurde beendet, hat aber etwas gemeldet, das im [Workflow-Protokoll](/de/guides/workflows/viewing-workflow-log/) lesenswert ist. |
| Fehler | Der Schritt ist fehlgeschlagen. Siehe [Schrittfehler verwalten](/de/guides/workflows/managing-step-errors/). |
| Übersprungen | Der Schritt wurde übergangen — er ist deaktiviert, oder seine Ausführungsbedingungen waren nicht erfüllt. Siehe [Schritte in einem Workflow überspringen](/de/guides/workflows/skip-steps-in-a-workflow/). |
| Fortgesetzt | Der Schritt ist fehlgeschlagen, ist aber so eingestellt, dass er bei einem Fehler fortfährt, sodass der Workflow weitergelaufen ist. Siehe [Bei Fehler fortfahren](/de/guides/workflows/continue-on-error/). |
| Beendet | Die Ausführung wurde beendet, bevor der Schritt abgeschlossen werden konnte. |
| Abgebrochen | Die Ausführung des Schritts wurde unterbrochen, sodass er nie abgeschlossen wird. Setzen Sie die Ausführung fort oder führen Sie den Workflow erneut aus. |

Eine geöffnete Workflow-Ansicht aktualisiert sich im Verlauf einer Ausführung selbstständig, sodass die angezeigten Status aktuell bleiben, ohne dass Sie die Seite neu laden müssen.

### Abgebrochene Schritte

Ein Schritt wird als **abgebrochen** markiert, wenn das, was ihn ausgeführt hat, mitten in der Ausführung weggefallen ist — meistens, weil jemand auf **Beenden** geklickt hat oder weil Wartungsarbeiten an der Plattform die Ausführung unterbrochen haben. Die Dauer des Schritts läuft nicht mehr weiter, und der Tooltip des Status erklärt, was passiert ist.

Ein abgebrochener Schritt wurde nicht abgeschlossen und hat keine Ausgabe erzeugt. Er ist kein langsamer Schritt und kein Problem mit Ihren Daten oder Ihrer Konfiguration.

Um die Arbeit wieder aufzunehmen, [**setzen Sie die Ausführung fort**](#anhalten-beenden-und-fortsetzen) — der abgebrochene Schritt wird erneut ausgeführt — oder führen Sie den gesamten Workflow erneut aus. Beides ist unbedenklich.

### Unterbrochene Schritte

Geht der Server, der einen Schritt ausführt, mitten in der Ausführung verloren, führt PlaidCloud den Schritt automatisch erneut aus, wenn eine Wiederholung sicher ist: Bei einem Schritt, der seine Ausgabe ersetzt, entsteht dasselbe Ergebnis wie bei einer einzigen sauberen Ausführung, sodass Sie nichts prüfen müssen.

Ein Schritt, der nicht sicher wiederholt werden kann, wird nicht erneut ausgeführt. Er schlägt einmal mit einer Meldung **unterbrochen** fehl, weil eine zweite Ausführung das duplizieren könnte, was der erste Versuch bereits geschrieben hat. Schritte, die Ausgaben mit `{date}` im Namen oder Pfad schreiben, gelten als nicht sicher wiederholbar, da eine erneute Ausführung auf einem anderen Datum landen könnte. Zur Wiederherstellung prüfen Sie das Ziel des Schritts darauf, was der erste Versuch geschrieben hat, bereinigen es bei Bedarf und [führen den Schritt erneut aus](/de/guides/workflows/running-one-step-in-a-workflow/) oder **setzen die Ausführung fort**.

### Schritte, die nie starten

Während ein Schritt auf einen Worker wartet, lautet seine Statusmeldung „Waiting for a worker… N min. No import worker has picked this step up yet.“ (die Art des Workers entspricht dem Schritt, etwa Import oder Export). Die Meldung verschwindet, sobald die Arbeit beginnt.

Wenn der Auftrag eines Schritts nie starten kann, schlägt der Schritt mit der Ursache fehl, anstatt ewig zu warten:

| Ursache | Schlägt fehl nach etwa |
|---|---|
| Kein Worker übernimmt den Auftrag eines Import- oder Dimensionsschritts | 40 Minuten |
| Der Pod des Schritts bleibt im Status Pending hängen | 20 Minuten |
| Das Image des Schritts kann nicht abgerufen werden | 5 Minuten |
| Für den Schritt wird kein Pod erstellt | 20 Minuten |
| Kein Runner übernimmt eine Connector-Synchronisierung (Singer) | 30 Minuten |

Die Meldung zur Connector-Synchronisierung nennt die Synchronisierung. Hat ein Worker den Auftrag gestartet und ist dann weggefallen, schlägt der Schritt ebenfalls fehl, mit einer Meldung, dass der Worker beendet wurde. Die Meldungen zu Import und Dimension enthalten „Use Run from here to retry.“

## Anhalten, Beenden und Fortsetzen

Während ein Workflow läuft, können Sie ihn **anhalten**, sodass laufende Schritte abgeschlossen werden und neue Schritte warten, oder **beenden**, wodurch die Schritte in der Warteschlange und alle noch laufenden Import- oder Exportaufträge abgebrochen werden. Import- und Dimensionsschritte, die noch in der Warteschlange standen, werden sauber abgebrochen, sodass sie spätere Importe und Dimensionsladevorgänge im Workspace nicht aufhalten. **Beenden** stoppt außerdem die in der Warteschlange stehenden oder laufenden Connector-Synchronisierungen (Singer) des Workflows, damit eine Synchronisierung nicht weiterläuft, nachdem der Workflow beendet wurde.

**Fortsetzen** nimmt eine angehaltene, beendete oder fehlgeschlagene Ausführung dort wieder auf, wo sie unterbrochen wurde, anstatt neu zu beginnen. Die Funktion steht zur Verfügung, wenn die letzte Ausführung eines Workflows in einem angehaltenen, beendeten oder fehlerhaften Zustand endete.

Was „dort, wo sie unterbrochen wurde“ bedeutet, hängt davon ab, wie der Workflow ausgeführt wird:

| Ausführung | Beim Fortsetzen |
|---|---|
| Seriell | Beginnt bei dem Schritt, der beim Ende der Ausführung lief, und macht von dort weiter. Liegt dieser Schritt in einer Gruppe, nimmt Fortsetzen die gesamte oberste Gruppe wieder auf, die ihn enthält: Schritte der Gruppe, die bereits erfolgreich abgeschlossen wurden, bleiben unberührt, die übrigen werden ausgeführt, und die Ausführung geht nach der Gruppe weiter. |
| Parallel | Führt jeden Schritt erneut aus, der noch nicht erfolgreich abgeschlossen war, und lässt abgeschlossene Schritte unberührt. |
| Erweitert (Graph) | Führt den fehlgeschlagenen Knoten und alles, was noch auf ihn wartet, erneut aus und lässt abgeschlossene Knoten unberührt. |

Schritte, die einen anderen Workflow aufrufen — **Run Model**, **Conditional Run Model** und **Loop Model** —, setzen den aufgerufenen Workflow fort, anstatt ihn neu zu starten, über beliebig viele Verschachtelungsebenen hinweg. Ein Schleifenschritt setzt die unterbrochene Iteration fort und überspringt die bereits abgeschlossenen Iterationen.

Wenn Sie einen Workflow fortsetzen, der als **verschachtelter Kindworkflow** eines anderen ausgeführt wurde — einen, den ein **Run Model**-Schritt in einem übergeordneten Workflow aufgerufen hat —, bietet PlaidCloud **Von Kettenanfang fortsetzen** an. Das alleinige Fortsetzen des Kindworkflows kann die Orchestrierung des übergeordneten Workflows nicht fortführen. Diese Option setzt daher stattdessen den übergeordneten Workflow der obersten Ebene fort — die Wurzel der Kette — und führt die gesamte Kette von der Stelle weiter, an der sie angehalten wurde. Das Fortsetzen eines Workflows der obersten Ebene bleibt unverändert. Der Kettenanfang wird innerhalb desselben Projekts bestimmt: Eine Kette, die in ein anderes Projekt hineinreicht, wird ab dem Anfang des Teils innerhalb des Projekts fortgesetzt.

Fortsetzen führt stets die **ursprüngliche** Ausführung weiter. Es führt jeden Schritt dieser Ausführung erneut aus, der nicht erfolgreich abgeschlossen wurde — ein fehlgeschlagener oder abgebrochener Schritt wird erneut ausgeführt und nicht als abgeschlossen behandelt —, und die zwischenzeitliche erneute Ausführung eines einzelnen Schritts ändert nichts daran, was Fortsetzen als Nächstes aufnimmt.

Eine fortgesetzte Ausführung wird als **neue Ausführung** im Ausführungsverlauf des Workflows aufgezeichnet und enthält nur die Schritte, die sie erneut ausgeführt hat. Die ursprüngliche Ausführung behält ihren eigenen Verlaufseintrag.

:::note
Ein Schleifenschritt ordnet seine abgeschlossenen Iterationen anhand ihrer Variablenwerte zu. Haben sich die Daten, über die die Schleife iteriert, zwischen der ursprünglichen Ausführung und dem Fortsetzen geändert, werden Iterationen, die sich nicht mehr zuordnen lassen, erneut ausgeführt, statt übersprungen zu werden.
:::
