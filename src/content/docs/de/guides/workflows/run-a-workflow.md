---
title: Einen Workflow ausführen
description: Führen Sie einen PlaidCloud-Workflow manuell oder bei Bedarf aus, verfolgen Sie den Status jedes Schritts, und halten Sie eine Ausführung an, beenden Sie sie oder setzen Sie sie dort fort, wo sie aufgehört hat.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Sie können eine vollständige Ausführung eines Workflows starten, indem Sie entweder in der Hierarchie **Workflows** auf das Ausführungssymbol klicken oder innerhalb eines bestimmten Workflows im Menü **Aktionen** die Option **Run All** wählen.



Sie können auch oben in der Workflow-Tabelle auf die Schaltfläche **Toggle Start/Stop** klicken. Diese Umschaltfläche beendet einen laufenden Workflow oder startet einen Workflow.

Wenn Sie bei einem Workflow, der bereits ausgeführt wird, auf **Ausführen** klicken, weist PlaidCloud Sie darauf hin, statt eine zweite Ausführung zu starten.

## Einen Buchungsmodus auswählen

Jede Ausführung hat einen ERP-Buchungsmodus. Um ihn in PlaidCloud auszuwählen, verwenden Sie **Mit Buchungsmodus ausführen** im Kontextmenü eines Workflows oder die Schaltfläche für den Ausführungsmodus auf der Workflow-Arbeitsfläche; ein einfaches **Workflow starten** oder **Workflow ausführen** fordert „Live“ an, weiterhin vorbehaltlich der unten beschriebenen Obergrenze des Projekts. Sie können den Modus auch wählen, wenn Sie eine Ausführung über die Ausführungs-API oder den Assistenten starten.

| Modus | Was geschieht |
|---|---|
| Live | Buchungsschritte buchen genau so wie bisher. Dies ist der Standard. |
| Simulieren | Jeder ERP-Buchungsschritt erstellt und validiert genau das, was er buchen würde, schreibt dann aber nichts fest und kontaktiert das ERP nie. Die Einträge, die gebucht würden, werden im [ERP-Buchungsverlauf](/de/guides/connections/erp-post-history/) als simuliert gekennzeichnet erfasst, sodass Sie sie prüfen können, bevor Sie live ausführen. |
| Aus | Buchungsschritte werden vollständig übersprungen. |

Ein Projekt hat außerdem eine eigene Obergrenze für den Buchungsmodus, die jedes Mitglied mit Schreibzugriff auf ein nicht gesperrtes Projekt über die Projekt-API oder den Assistenten festlegen kann. Die Obergrenze macht eine Ausführung immer nur sicherer, nie freizügiger: Der wirksame Modus einer Ausführung ist der restriktivere aus dem von Ihnen gewählten Modus und der Obergrenze des Projekts, sodass ein auf „Simulieren“ begrenztes Projekt simuliert bleibt, selbst wenn Sie die Ausführung als „Live“ starten.

Ein [geplantes Ereignis](/de/administration/scheduled-events/event-scheduler/#erp-buchungsmodus) behält seinen eigenen Buchungsmodus, sodass ein auf „Simulieren“ gesetzter Zeitplan bei jedem Auslösen simuliert ausgeführt wird.

Der Modus gilt für alles, was die Ausführung berührt. Ein Sub-Workflow, ein Makro sowie ein Schritt **Run Model**, **Conditional Run Model** oder **Loop Model** übernehmen alle den Modus der übergeordneten Ausführung, ebenso eine Ausführung, die Sie nach einem Beenden [fortsetzen](#anhalten-beenden-und-fortsetzen) – eine simulierte Ausführung kann nirgendwo in sich selbst tatsächlich buchen.

:::caution
SAP-Buchungs-, SAP-Anhangs- und generische SAP-RFC-Schritte unterstützen keinen Probelauf. Unter „Simulieren“ oder „Aus“ werden sie vollständig übersprungen, weil die eigenen Test-Flags von SAP trotzdem eine echte Verbindung zu SAP öffnen – das Überspringen des Schritts ist die einzige Möglichkeit, dass eine simulierte Ausführung SAP nie erreicht.
:::

:::note
Ein einzelner ERP-Buchungsschritt hat außerdem eine eigene Einstellung „Validate Only“ (bei manchen Schritten als „Vorschau“ oder „Test Only Mode“ bezeichnet), unabhängig vom oben beschriebenen Buchungsmodus der Ausführung. Der Schritteditor speichert diese Einstellung immer explizit. Eine Schrittkonfiguration, die auf anderem Weg geschrieben wird – über die REST-API, MCP oder einen Workflow-Bundle-Import – und die Einstellung ganz weglässt, verwendet jetzt ebenfalls standardmäßig eine Vorschau statt einer Live-Buchung.
:::

## Das Projekt zum Buchen autorisieren

Eine Workflow-Ausführung bucht als das Projekt in ein ERP, nicht als die Person, die sie gestartet hat. Bevor eine Ausführung buchen kann, benötigt das Projekt eine Autorisierung für jede ERP-Verbindung und Umgebung, die seine Buchungsschritte verwenden. Fehlt sie, schlägt der Schritt mit „Dieses Projekt ist nicht berechtigt, in die Verbindung … zu buchen“ fehl, wobei Verbindung und Umgebung genannt werden. Die Schritte **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** und **Call SAP RFC** benötigen keine.

Um ein Projekt zu autorisieren, öffnen Sie seine Startseite und wählen Sie unter **ERP-Buchung** die Option **ERP-Schreibautorisierungen**. Jede Zeile steht für eine Verbindung in einer Umgebung. Aktivieren Sie **Autorisiert**, damit das Projekt dort buchen darf, oder deaktivieren Sie die Option, um dies zu beenden. **Autorisiert von** und **Autorisiert am** zeigen, wer die Autorisierung zuletzt erteilt hat und wann.

- Die Schaltfläche wird den Architects des Projekts und Workspace-Administratoren angezeigt, aber nur ein Architect kann eine Autorisierung ändern, und nur solange das Projekt nicht gesperrt ist. Ein Workspace-Administrator, der kein Architect ist, kann sich zuerst selbst als Architect hinzufügen.
- Das Auswählen einer Zeile zum Autorisieren oder Entfernen lädt die Liste nicht neu: Die Scrollposition und eine von Ihnen gewählte Spaltensortierung bleiben erhalten. Die Größe des Fensters lässt sich ändern, und der Hinweis zu öffentlichen Projekten wird vollständig umbrochen.
- Um eine Verbindung zu autorisieren, benötigen Sie selbst ebenfalls Schreibzugriff darauf: Sie sind ihr Eigentümer, oder sie ist namentlich oder über eine Ihrer Sicherheitsgruppen für Sie freigegeben. Eine Verbindung, die auf **Alle Arbeitsbereichsmitglieder** gesetzt ist, zählt nicht.
- Ein Projekt, das auf **Alle Arbeitsbereichsmitglieder** gesetzt ist, wird wie jedes andere autorisiert. Jedes Mitglied ist Architect dieses Projekts, sodass jedes Mitglied mit Schreibzugriff auf eine Verbindung das Projekt dafür autorisieren kann. Sobald es autorisiert ist, kann jedes Mitglied aus den Workflows des Projekts in diese Verbindung buchen, und das Fenster weist oberhalb des Rasters darauf hin.
- Eine neue Kopie, die privat für Sie ist und mit Tabellendaten oder Dimensionselementen erstellt wurde, behält die Autorisierungen der Quelle, die Sie selbst erteilen könnten, und kommt im Modus „Simulieren“ an, wenn die Quelle auf „Live“ stand – siehe [ERP-Schreibautorisierungen in der Kopie](/de/guides/projects/managing-projects/#erp-schreibautorisierungen-in-der-kopie). Jede andere Kopie oder ein aus einem Projektarchiv erstelltes Projekt startet ohne Autorisierungen. Autorisieren Sie es, bevor es bucht.

## Den Status eines Schritts verfolgen

Während ein Workflow ausgeführt wird, zeigt jeder Schritt ein Statussymbol, das angibt, wo er steht, zusammen mit seiner bisherigen Laufzeit. Bewegen Sie den Mauszeiger über das Symbol, um die zugehörige Meldung zu sehen.

| Status | Bedeutung |
|---|---|
| Wartend | Der Schritt ist in der Warteschlange und hat noch nicht begonnen. |
| Wird ausgeführt | Der Schritt arbeitet, und seine Dauer zählt währenddessen hoch. |
| Abgeschlossen | Der Schritt wurde erfolgreich beendet. |
| Warnung | Der Schritt wurde beendet, hat aber etwas markiert, das Sie im [Workflow-Protokoll](/de/guides/workflows/viewing-workflow-log/) lesen sollten. |
| Fehler | Der Schritt ist fehlgeschlagen. Siehe [Schrittfehler verwalten](/de/guides/workflows/managing-step-errors/). |
| Übersprungen | Der Schritt wurde ausgelassen – er ist deaktiviert, oder seine Ausführungsbedingungen waren nicht erfüllt. Siehe [Schritte in einem Workflow überspringen](/de/guides/workflows/skip-steps-in-a-workflow/). |
| Fortgesetzt | Der Schritt ist fehlgeschlagen, ist aber so eingestellt, dass bei einem Fehler fortgefahren wird, daher lief der Workflow weiter. Siehe [Bei Fehler fortfahren](/de/guides/workflows/continue-on-error/). |
| Beendet | Die Ausführung wurde beendet, bevor der Schritt abgeschlossen werden konnte. |
| Abgebrochen | Die Ausführung des Schritts wurde unterbrochen, sodass er nie abgeschlossen wird. Setzen Sie die Ausführung fort oder führen Sie den Workflow erneut aus. |

Eine geöffnete Workflow-Ansicht aktualisiert sich im Verlauf einer Ausführung selbstständig, sodass die angezeigten Status aktuell bleiben, ohne dass Sie die Seite neu laden müssen.

### Abgebrochene Schritte

Ein Schritt wird als **abgebrochen** markiert, wenn das, was ihn ausgeführt hat, während der Ausführung weggefallen ist – meist weil jemand auf **Beenden** geklickt hat oder weil Wartungsarbeiten an der Plattform die Ausführung unterbrochen haben. Die Dauer des Schritts zählt nicht weiter hoch, und der Status-Tooltip erklärt, was geschehen ist.

Ein abgebrochener Schritt wurde nicht abgeschlossen und hat keine Ausgabe erzeugt. Er ist kein langsamer Schritt, und es liegt kein Problem mit Ihren Daten oder Ihrer Konfiguration vor.

Um die Arbeit wieder aufzunehmen, können Sie die Ausführung entweder [**fortsetzen**](#anhalten-beenden-und-fortsetzen) – der abgebrochene Schritt wird erneut ausgeführt – oder den gesamten Workflow erneut ausführen. Beides ist sicher.

### Unterbrochene Schritte

Fällt der Server, der einen Schritt ausführt, während der Ausführung aus, führt PlaidCloud den Schritt automatisch erneut aus, wenn eine Wiederholung sicher ist: Ein Schritt, der seine Ausgabe ersetzt, erzielt dasselbe Ergebnis wie eine einzelne saubere Ausführung, sodass Sie nichts prüfen müssen.

Ein Schritt, der sich nicht sicher wiederholen lässt, wird nicht erneut ausgeführt. Er schlägt einmal mit der Meldung **Unterbrochen** fehl, weil eine zweite Ausführung duplizieren könnte, was der erste Versuch bereits geschrieben hat. Schritte, die Ausgaben mit `{date}` im Namen oder Pfad schreiben, gelten als nicht sicher wiederholbar, da eine erneute Ausführung auf ein anderes Datum fallen könnte. Prüfen Sie zur Wiederherstellung im Ziel des Schritts, was der erste Versuch geschrieben hat, bereinigen Sie es bei Bedarf und [führen Sie den Schritt erneut aus](/de/guides/workflows/running-one-step-in-a-workflow/) oder **setzen Sie die Ausführung fort**.

### Schritte, die nie starten

Wenn kein Worker den Job eines Import- oder Dimensionsschritts innerhalb von etwa 40 Minuten übernimmt, schlägt der Schritt fehl, statt bis zum 24-Stunden-Timeout **Wird ausgeführt** anzuzeigen. Wenn ein Worker den Job gestartet hat und dann weggefallen ist, schlägt der Schritt ebenfalls fehl, mit einer Meldung, dass der Worker beendet wurde. Beide Meldungen lauten: „Verwenden Sie Ab hier ausführen, um es erneut zu versuchen.“

## Anhalten, Beenden und Fortsetzen

Während ein Workflow ausgeführt wird, können Sie ihn **anhalten**, sodass laufende Schritte abgeschlossen werden und neue Schritte warten, oder ihn **beenden**, wodurch die Schritte in der Warteschlange sowie alle noch laufenden Import- oder Exportjobs abgebrochen werden. Import- und Dimensionsschritte, die noch in der Warteschlange standen, werden sauber abgebrochen, sodass sie spätere Importe und Dimensionsladevorgänge im Workspace nicht aufhalten.

**Fortsetzen** nimmt eine angehaltene, beendete oder fehlgeschlagene Ausführung dort wieder auf, wo sie aufgehört hat, statt von vorn zu beginnen. Die Funktion ist immer dann verfügbar, wenn die letzte Ausführung eines Workflows mit dem Status „angehalten“, „beendet“ oder „Fehler“ endete.

Was „dort, wo sie aufgehört hat“ bedeutet, hängt davon ab, wie der Workflow ausgeführt wird:

| Ausführung | Beim Fortsetzen |
|---|---|
| Seriell | Startet bei dem Schritt neu, der lief, als die Ausführung endete, und fährt von dort fort. Liegt dieser Schritt in einer Gruppe, nimmt Fortsetzen die gesamte übergeordnete Gruppe der obersten Ebene auf, die ihn enthält: Bereits erfolgreich abgeschlossene Schritte der Gruppe bleiben unberührt, die anderen werden ausgeführt, und die Ausführung wird nach der Gruppe fortgesetzt. |
| Parallel | Führt jeden Schritt erneut aus, der noch nicht erfolgreich abgeschlossen war, und lässt abgeschlossene Schritte unberührt. |
| Erweitert (Graph) | Führt den fehlgeschlagenen Knoten und alles, was noch auf ihn wartet, erneut aus und lässt abgeschlossene Knoten unberührt. |

Schritte, die einen anderen Workflow aufrufen – **Run Model**, **Conditional Run Model** und **Loop Model** –, setzen den aufgerufenen Workflow fort, statt ihn neu zu starten, über beliebig viele Verschachtelungsebenen hinweg. Ein Schleifenschritt setzt die unterbrochene Iteration fort und überspringt die bereits abgeschlossenen Iterationen.

Wenn Sie einen Workflow fortsetzen, der als **verschachtelter untergeordneter Workflow** eines anderen ausgeführt wurde – einer, den ein Schritt **Run Model** in einem übergeordneten Workflow aufgerufen hat –, bietet PlaidCloud **Von Kettenanfang fortsetzen** an. Wird der untergeordnete Workflow allein fortgesetzt, kann die Orchestrierung des übergeordneten Workflows nicht weiterlaufen; diese Option setzt daher stattdessen den übergeordneten Workflow der obersten Ebene fort – den Anfang der Kette – und führt die gesamte Kette dort fort, wo sie angehalten hat. Das Fortsetzen eines Workflows der obersten Ebene bleibt unverändert. Der Kettenanfang wird innerhalb desselben Projekts ermittelt: Eine Kette, die in ein anderes Projekt übergeht, wird vom Anfang des Abschnitts innerhalb des Projekts fortgesetzt.

Fortsetzen setzt immer die **ursprüngliche** Ausführung fort. Es führt jeden Schritt dieser Ausführung erneut aus, der nicht erfolgreich abgeschlossen wurde – ein fehlgeschlagener oder abgebrochener Schritt wird erneut ausgeführt, nicht als abgeschlossen behandelt –, und das zwischenzeitliche erneute Ausführen eines einzelnen Schritts ändert nichts daran, was Fortsetzen als Nächstes aufnimmt.

Eine fortgesetzte Ausführung wird im Ausführungsverlauf des Workflows als **neue Ausführung** erfasst, die nur die erneut ausgeführten Schritte enthält. Die ursprüngliche Ausführung behält ihren eigenen Verlaufseintrag.

:::note
Ein Schleifenschritt ordnet seine abgeschlossenen Iterationen anhand ihrer Variablenwerte zu. Haben sich die Daten, über die die Schleife iteriert, zwischen der ursprünglichen Ausführung und dem Fortsetzen geändert, werden Iterationen, die sich nicht mehr zuordnen lassen, erneut ausgeführt statt übersprungen.
:::
