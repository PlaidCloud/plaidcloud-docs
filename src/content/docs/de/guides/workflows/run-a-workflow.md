---
title: Einen Workflow ausführen
description: Führen Sie einen PlaidCloud-Workflow manuell oder bei Bedarf aus, verfolgen Sie den Status jedes Schritts und halten Sie eine Ausführung an, beenden Sie sie oder setzen Sie sie dort fort, wo sie aufgehört hat.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Sie können eine vollständige Workflow-Ausführung starten, indem Sie in der Hierarchie **Workflows** auf das Symbol „Ausführen“ klicken oder im Menü **Aktionen** eines bestimmten Workflows **Run All** wählen.



Sie können auch oben in der Workflow-Tabelle auf die Schaltfläche **Toggle Start/Stop** klicken. Mit dieser Umschalttaste beenden Sie einen laufenden Workflow oder starten einen Workflow.

Wenn Sie bei einem Workflow, der bereits läuft, auf **Ausführen** klicken, weist PlaidCloud Sie darauf hin, anstatt eine zweite Ausführung zu starten.

## Einen Buchungsmodus wählen

Jede Ausführung hat einen ERP-Buchungsmodus. Um in PlaidCloud einen Modus zu wählen, verwenden Sie **Mit Buchungsmodus ausführen** im Kontextmenü eines Workflows oder die Schaltfläche für den Ausführungsmodus auf der Arbeitsfläche des Workflows; **Workflow starten** oder **Workflow ausführen** ohne Moduswahl fordert Live an, weiterhin begrenzt durch die unten beschriebene Obergrenze des Projekts. Sie können den Modus auch wählen, wenn Sie eine Ausführung über die Run-API oder den Assistenten starten.

| Modus | Was geschieht |
|---|---|
| Live | Buchungsschritte buchen genau so, wie sie es immer getan haben. Dies ist der Standard. |
| Simulate | Jeder ERP-Buchungsschritt erstellt und validiert genau das, was er buchen würde, schreibt dann aber nichts fest und kontaktiert das ERP nie. Die Buchungen, die gebucht würden, werden erfasst, sodass Sie sie prüfen können, bevor Sie live ausführen: die eines Schritts **Belege buchen** im [Buchungsregister](/de/guides/connections/posting-register/) als **Würde gebucht** (siehe [Belege in ERP-Systemen buchen](/de/guides/connections/post-documents/)), die des eigenen Buchungsschritts eines Systems in der [ERP-Buchungshistorie](/de/guides/connections/erp-post-history/), als simuliert gekennzeichnet. |
| Off | Buchungsschritte werden vollständig übersprungen. |

Ein Projekt hat außerdem eine eigene Obergrenze für den Buchungsmodus. Sie wird über die Projekt-API oder den Assistenten von jedem Mitglied mit Schreibzugriff auf ein entsperrtes Projekt festgelegt. Die Obergrenze macht eine Ausführung immer nur sicherer, nie freizügiger: Der wirksame Modus einer Ausführung ist der restriktivere aus dem von Ihnen gewählten Modus und der Obergrenze des Projekts. Ein Projekt mit der Obergrenze Simulate bleibt also simuliert, auch wenn Sie die Ausführung als Live starten.

Ein [geplantes Ereignis](/de/administration/scheduled-events/event-scheduler/#erp-buchungsmodus) behält seinen eigenen Buchungsmodus. Ein Zeitplan, der auf Simulate gesetzt ist, läuft daher bei jeder Auslösung simuliert.

Der Modus gilt für alles, was die Ausführung berührt. Ein Unter-Workflow, ein Makro sowie ein **Run Model**-, **Conditional Run Model**- oder **Loop Model**-Schritt übernehmen alle den Modus der übergeordneten Ausführung, ebenso eine Ausführung, die Sie nach einem Beenden [fortsetzen](#anhalten-beenden-und-fortsetzen) — eine simulierte Ausführung kann an keiner Stelle in sich selbst real buchen.

:::caution
SAP-Buchungsschritte, SAP-Anhangsschritte und generische SAP-RFC-Schritte führen keinen Probelauf durch. Unter Simulate oder Off werden sie vollständig übersprungen, weil die eigenen Testkennzeichen von SAP trotzdem eine echte Verbindung zu SAP öffnen — das Überspringen des Schritts ist die einzige Möglichkeit, sicherzustellen, dass eine simulierte Ausführung SAP nie erreicht.
:::

:::note
Ein einzelner ERP-Buchungsschritt hat außerdem eine eigene Einstellung „Validate Only“ (bei manchen Schritten als „Preview“ oder „Test Only Mode“ bezeichnet), unabhängig vom oben beschriebenen Buchungsmodus der Ausführung. Der Schritt-Editor speichert diese Einstellung immer explizit. Eine Schrittkonfiguration, die auf andere Weise geschrieben wird — über die REST-API, MCP oder einen Workflow-Bundle-Import — und die Einstellung ganz weglässt, verwendet jetzt ebenfalls standardmäßig eine Vorschau statt einer Live-Buchung. Der Schritt **Belege buchen** hat keine solche Einstellung: Der Modus der Ausführung und der eigene Modus seines Systems entscheiden, ob er bucht – siehe [Belege in ERP-Systemen buchen](/de/guides/connections/post-documents/).
:::

## Das Projekt zum Buchen autorisieren

Ein Workflow bucht in einem ERP als das Projekt, nicht als die Person, die ihn gestartet hat. Bevor eine Ausführung buchen kann, benötigt das Projekt eine Autorisierung für jede ERP-Verbindung und jede Umgebung, die seine Buchungsschritte verwenden. Ohne sie schlägt der Schritt mit der Meldung „This project isn't authorized to post to connection …“ fehl und nennt die Verbindung und die Umgebung. Die Schritte **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** und **Call SAP RFC** benötigen keine Autorisierung.

Um ein Projekt zu autorisieren, öffnen Sie seine Startseite und wählen unter **ERP-Buchung** den Eintrag **ERP-Schreibautorisierungen**. Jede Zeile steht für eine Verbindung in einer Umgebung. Aktivieren Sie **Autorisiert**, damit das Projekt dort buchen darf, oder deaktivieren Sie das Kontrollkästchen, um dies zu beenden. **Autorisiert von** und **Autorisiert am** zeigen, wer die Autorisierung zuletzt erteilt hat und wann.

- Die Schaltfläche wird den Architects des Projekts und den Workspace-Administratoren angezeigt, aber nur ein Architect kann eine Autorisierung ändern, und nur solange das Projekt entsperrt ist. Ein Workspace-Administrator, der kein Architect ist, kann sich zuvor selbst als Architect hinzufügen.
- Wenn Sie eine Zeile auswählen, um sie zu autorisieren oder die Autorisierung zu entziehen, wird die Liste nicht neu geladen: Die Bildlaufposition und eine von Ihnen gewählte Spaltensortierung bleiben erhalten. Die Größe des Fensters kann geändert werden, und der Hinweis zu öffentlichen Projekten wird vollständig umbrochen.
- Um eine Verbindung zu autorisieren, benötigen Sie auch selbst Schreibzugriff darauf: Sie sind ihr Eigentümer, oder sie wird namentlich oder über eine Ihrer Sicherheitsgruppen für Sie freigegeben. Eine Verbindung, die auf **Alle Arbeitsbereichsmitglieder** gesetzt ist, zählt nicht.
- Ein Projekt, das auf **Alle Arbeitsbereichsmitglieder** gesetzt ist, wird wie jedes andere autorisiert. Jedes Mitglied ist Architect des Projekts, sodass jedes Mitglied mit Schreibzugriff auf eine Verbindung das Projekt dafür autorisieren kann. Sobald es autorisiert ist, kann jedes Mitglied aus den Workflows des Projekts in diese Verbindung buchen, und das Fenster weist oberhalb des Rasters darauf hin.
- Eine neue Kopie, die nur für Sie privat ist und mit Tabellendaten oder Dimensionselementen erstellt wurde, übernimmt die Autorisierungen der Quelle, die Sie selbst erteilen könnten, und startet in Simulate, wenn die Quelle Live war — siehe [ERP-Schreibautorisierungen in der Kopie](/de/guides/projects/managing-projects/#erp-schreibautorisierungen-in-der-kopie). Jede andere Kopie und jedes aus einem Projektarchiv erstellte Projekt startet ohne Autorisierungen. Autorisieren Sie es, bevor es bucht.

## Den Status eines Schritts verfolgen

Während ein Workflow läuft, zeigt jeder Schritt ein Statussymbol, das anzeigt, wo er steht, zusammen mit seiner bisherigen Laufzeit. Bewegen Sie den Mauszeiger über das Symbol, um die zugehörige Meldung zu sehen.

| Status | Bedeutung |
|---|---|
| Waiting | Der Schritt steht in der Warteschlange und hat noch nicht begonnen. |
| Running | Der Schritt arbeitet, und seine Dauer läuft hoch. |
| Completed | Der Schritt wurde erfolgreich abgeschlossen. |
| Warning | Der Schritt wurde abgeschlossen, hat aber etwas gemeldet, das im [Workflow-Protokoll](/de/guides/workflows/viewing-workflow-log/) lesenswert ist. |
| Error | Der Schritt ist fehlgeschlagen. Siehe [Schrittfehler verwalten](/de/guides/workflows/managing-step-errors/). |
| Skipped | Der Schritt wurde übergangen — er ist deaktiviert, oder seine Ausführungsbedingungen waren nicht erfüllt. Siehe [Schritte in einem Workflow überspringen](/de/guides/workflows/skip-steps-in-a-workflow/). |
| Continued | Der Schritt ist fehlgeschlagen, ist aber so eingestellt, dass er bei einem Fehler fortfährt, sodass der Workflow weitergelaufen ist. Siehe [Bei Fehler fortfahren](/de/guides/workflows/continue-on-error/). |
| Stopped | Die Ausführung wurde beendet, bevor der Schritt abgeschlossen werden konnte. |
| Abandoned | Die Ausführung des Schritts wurde unterbrochen, sodass er nie abgeschlossen wird. Setzen Sie die Ausführung fort, oder führen Sie den Workflow erneut aus. |

Eine geöffnete Workflow-Ansicht aktualisiert sich im Verlauf einer Ausführung von selbst, sodass die Status, die Sie sehen, aktuell bleiben, ohne dass Sie die Seite neu laden müssen.

### Abgebrochene Schritte

Ein Schritt wird als **abandoned** (abgebrochen) markiert, wenn das, was ihn ausgeführt hat, mitten in der Ausführung weggefallen ist — meist weil jemand auf **Beenden** gedrückt hat oder weil eine Plattformwartung die Ausführung unterbrochen hat. Die Dauer des Schritts läuft nicht mehr weiter, und der QuickInfo-Text des Status erklärt, was geschehen ist.

Ein abgebrochener Schritt wurde nicht abgeschlossen und hat keine Ausgabe erzeugt. Er ist kein langsamer Schritt und auch kein Problem mit Ihren Daten oder Ihrer Konfiguration.

Um die Arbeit wieder aufzunehmen, [**setzen Sie die Ausführung fort**](#anhalten-beenden-und-fortsetzen) — der abgebrochene Schritt wird erneut ausgeführt — oder führen Sie den gesamten Workflow erneut aus. Beides ist unbedenklich.

### Unterbrochene Schritte

Geht der Server, auf dem ein Schritt läuft, mitten in der Ausführung verloren, führt PlaidCloud den Schritt automatisch erneut aus, wenn eine Wiederholung sicher ist: Ein Schritt, der seine Ausgabe ersetzt, liefert dasselbe Ergebnis wie eine einzelne saubere Ausführung, sodass Sie nichts prüfen müssen. Das Protokoll des Schritts zeigt an der Stelle, an der der zweite Versuch beginnt, eine Warnung: „Restarted: the server running this step stopped before it finished (e.g. out of memory or a restart); running it again from the start.“

Ein Schritt, der nicht sicher wiederholt werden kann, wird nicht erneut ausgeführt. Er schlägt einmalig mit der Meldung **interrupted** (unterbrochen) fehl, weil eine zweite Ausführung das duplizieren könnte, was der erste Versuch bereits geschrieben hat. Schritte, die Ausgaben mit `{date}` oder `{date_iso}` im Namen oder Pfad schreiben, gelten als nicht sicher wiederholbar, da eine erneute Ausführung auf einem anderen Datum landen könnte. Zur Wiederherstellung prüfen Sie das Ziel des Schritts auf das, was der erste Versuch geschrieben hat, bereinigen es bei Bedarf und [führen den Schritt dann erneut aus](/de/guides/workflows/running-one-step-in-a-workflow/) oder wählen für die Ausführung **Fortsetzen**.

### Schritte, die nie starten

Solange ein Schritt auf einen Worker wartet, lautet seine Statusmeldung „Waiting for a worker… N min. No import worker has picked this step up yet.“ (die Art des Workers entspricht dem Schritt, etwa Import oder Export). Die Meldung verschwindet, sobald die Arbeit beginnt.

Wenn der Job eines Schritts nie starten kann, schlägt der Schritt mit der Angabe des Grunds fehl, anstatt ewig zu warten:

| Ursache | Schlägt fehl nach etwa |
|---|---|
| Kein Worker übernimmt den Job eines Import- oder Dimensionsschritts | 40 Minuten |
| Der Pod des Schritts bleibt im Zustand Pending hängen | 20 Minuten |
| Das Image des Schritts kann nicht abgerufen werden | 5 Minuten |
| Für den Schritt wird kein Pod erstellt | 20 Minuten |
| Kein Runner übernimmt eine Connector-Synchronisierung (Singer) | 30 Minuten |

Die Meldung zur Connector-Synchronisierung nennt die Synchronisierung. Wenn ein Worker den Job gestartet hat und dann weggefallen ist, schlägt der Schritt ebenfalls fehl, mit einer Meldung, dass der Worker beendet wurde. Die Meldungen zu Import und Dimension lauten „Use Run from here to retry.“

### Ausführungen, die nicht mehr reagieren

Eine Ausführung bleibt nie im Status **Wird ausgeführt**, wenn die Arbeit dahinter weggefallen ist. Geht der Server verloren, auf dem der Workflow läuft, endet die Ausführung als fehlgeschlagen. Eine Ausführung dauert höchstens 12 Stunden: Läuft sie zu diesem Zeitpunkt noch, schlägt sie mit „Run failed: still running at the 12-hour limit. Re-run the workflow.“ fehl.

## Run Insight

Run Insight zeigt, wohin die Zeit einer Ausführung eines Workflows geflossen ist und welche Schritte länger oder kürzer gedauert haben als üblich. Jeder Schritt wird an seinen eigenen letzten Ausführungen gemessen, sodass ein Schritt, der immer langsam ist, nicht hervorgehoben wird.

### Run Insight öffnen

- Klicken Sie auf der Arbeitsfläche in der Symbolleiste auf **Verlauf**. Siehe [Visueller Workflow-Designer](/de/guides/workflows/advanced-workflows/).
- Wählen Sie auf der Registerkarte **Workflows** einen Workflow aus und wählen Sie im Menü **Aktionen** oder im Kontextmenü **Run Insight**.
- Wählen Sie auf der Startseite auf einer Workflow-Karte **Letzte Ausführung öffnen**.
- Wählen Sie im Dialog „Ausführungsverlauf“ in der Tabelle **Ausführungen** eine Ausführung mit **In Insight öffnen** oder öffnen Sie ihre Zeile.
- Klicken Sie in einer In-App-Weave-Nachricht zu einer langsamen Ausführung auf **Ausführung öffnen**. Siehe [Benachrichtigung am Ende einer Ausführung](/de/guides/ai-assistant/weave-findings/#benachrichtigung-am-ende-einer-ausführung).

Der Dialog trägt den Titel **Ausführungsverlauf** – Workflow-Name. Mit dem Umschalter **Insight** | **Ausführungen** wechseln Sie zwischen dieser Ansicht und der Tabelle vergangener Ausführungen. Der Ausführungsverlauf eines einzelnen Schritts, den Sie aus dem Inspektor öffnen, zeigt nur die Tabelle.

### Kopfzeile und Aufmerksamkeitsliste lesen

Die Kopfzeile nennt das Ergebnis der Ausführung in einer Zeile: **Dauer:** *Zeit*, **Läuft seit** *Zeit*, solange sie läuft, **Nach** *Zeit* **gestoppt** bei einer zuletzt gestoppten Ausführung oder **Fehlgeschlagen in** *Workflow*, dem Workflow, in dem sie fehlgeschlagen ist. Ein Satz darunter sagt, was auffällt, etwa die Schritte, die langsamer als üblich liefen, Wartezeit oder dass jeder Schritt mit Verlauf in seinem üblichen Bereich lief. Danach folgen die Startzeit, die Anzahl der Workflows und Schritte und, wenn der Verlauf einiger Schritte zu kurz für eine Bewertung ist, deren Anzahl. Wenn etwas einen Blick verdient, erscheint neben der Kopfzeile *N* **zu prüfen**.

Neben der Kopfzeile steht ein Streifen mit den letzten Ausführungen, mit einer Beschriftung darüber. Jeder Balken ist eine Ausführung, so hoch, wie sie gedauert hat, und der Tag ist nur dort beschriftet, wo er wechselt. Klicken Sie im Streifen auf eine Ausführung, um sie zu öffnen. Eine rote Kappe und ein ✕ markieren eine fehlgeschlagene Ausführung, und ein gestrichelter Umriss markiert eine Ausführung, die weniger Schritte als die meisten letzten Ausführungen ausgeführt hat, weil sie sich nicht mit einer vollständigen Ausführung vergleichen lässt.

**Was Aufmerksamkeit braucht** listet in dieser Reihenfolge zuerst Fehler, dann Zeit über dem Üblichen und dann Wartezeiten auf. Jeder Eintrag ist eine Karte mit seinem Namen, der Zeit, die er verloren hat, oder **Fehlgeschlagen**, seiner Position und einem Balken seiner Zeit, in dem Grau innerhalb des Üblichen und Bernstein darüber liegt, und der Balken eines Fehlers ist rot. Ein Schritt, der seit seiner letzten Ausführung gespeichert wurde, trägt ein Etikett **Gespeichert am** *Datum*. Klicken Sie auf eine Karte, um sie in der Ansicht auszuwählen; die ausgewählte Karte ist hervorgehoben.

### Ablauf, Zeitachse und Tabelle

Die Kopfzeile über der Ansicht enthält den Namen des Workflows, dann **Vergleichen mit**, dann **Ansicht**, deren Schaltflächen **Ablauf**, **Zeitachse** und **Tabelle** die Ansicht auswählen, und rechts die Schaltfläche Aktualisieren.

| Ansicht | Was sie zeigt |
|---|---|
| **Ablauf** | Blöcke, deren Höhe die Zeit ist. Bernstein ist Zeit über dem Üblichen eines Schritts. Ein Block, der nicht geöffnet ist, aber einen Fehler enthält, zeigt ✕ und einen roten Umriss. Ein fehlgeschlagener oder ausgewählter Block, der zu kurz für seinen Namen ist, wird höher gezeichnet, und die Legende sagt dann, dass er nicht maßstabsgetreu ist. Hat ein Schritt andere Workflows aufgerufen, ist ein Segment **Aufrufaufwand** die eigene Zeit des Schritts außerhalb dieser Workflows. Lief kein Schritt, zeigt ein Segment **Wartend** die Lücke; ein Workflow, der parallel lief, zeichnet keines. |
| **Zeitachse** | Uhrzeit ab dem Start der Ausführung. Eine gestrichelte Umrandung zeigt, wie lange der Block in der verglichenen Ausführung gedauert hat. |
| **Tabelle** | Alles in Aufrufreihenfolge, mit den Spalten **Name**, **Diese Ausführung**, **Üblicherweise**, **Zusätzlich**, **Verglichene Ausführung** und **Status**. |

Ein Workflow, der andere Workflows aufgerufen hat, zeigt diese in sich an. Doppelklicken Sie auf einen Workflow-Block oder wählen Sie **Vergrößern**, um darin zu arbeiten, und kehren Sie über den Pfad über der Ansicht zurück. Liegen mehrere Schritte im Plan beieinander, faltet **Ablauf** sie zu einem Block *N* **im Plan** zusammen; klicken Sie darauf oder klicken Sie rechts vom Pfad auf **Alle** *Anzahl* **Blöcke anzeigen**, um sie zu öffnen; die Anzahl umfasst jeden Block in der Ansicht. **Schritte im Plan einklappen** klappt sie wieder ein, und die Schaltfläche erscheint nur, wenn sich etwas einklappen lässt.

Wählen Sie einen Block aus, um sein Detailfenster zu sehen. Es zeigt den Namen und die Position des Blocks, eine Statusanzeige mit einer der unten genannten Markierungen und Zeilen für das, was von **Diese Ausführung**, **Üblicherweise**, **Verlauf**, **Über dem Üblichen** und **Verglichene Ausführung** zutrifft. Darunter folgt eine Trendlinie: für den eigenen Workflow der Ausführung seine letzten vollständigen Ausführungen, mit dieser Ausführung als Punkt, wenn sie abgeschlossen wurde; für einen Schritt mit üblichem Bereich dieser Bereich als Band mit dieser Ausführung als Punkt. Hinweise erklären die Markierung, und die Schaltflächen sind **In seinem Workflow anzeigen**, **Seine Schritte anzeigen** oder **Vergrößern**, **Workflow öffnen** und **Ausführungsprotokoll anzeigen**. **Workflow öffnen** öffnet den Workflow auf der Arbeitsfläche und **Ausführungsprotokoll anzeigen** öffnet sein [Protokoll](/de/guides/workflows/viewing-workflow-log/).

### Was die Markierungen bedeuten

| Markierung | Bedeutung |
|---|---|
| **Fehlgeschlagen** | Ein Schritt ist mit einem Fehler beendet worden. Das Fenster zeigt seine Meldung, es sei denn, Ihre Rolle kann den Namen des Schritts nicht sehen. |
| **Langsamer als üblich** | Der Schritt hat länger gedauert als sein üblicher Bereich. |
| **Durchgehend langsamer** | Jeder Schritt im Workflow lief etwa gleich viel langsamer, was auf etwas hindeutet, das der ganze Workflow gemeinsam hat, und nicht auf einen einzelnen Schritt. Seine Schritte zeigen **Teil einer gemeinsamen Verlangsamung**. |
| **Mit langsamen Schritten** | Ein Workflow mit **Langsame Schritte darin**. |
| **Im Plan** | Der Schritt lief innerhalb seines üblichen Bereichs. |
| **Schneller** | Der Schritt lief schneller als sein üblicher Bereich. |
| **Nicht genug Verlauf** | Der Schritt wurde zu selten ausgeführt, um einen üblichen Bereich zu haben, und wird deshalb nicht bewertet. |
| **Fehler, fortgesetzt** | Der Schritt ist fehlgeschlagen, ist aber so eingestellt, dass er [bei einem Fehler fortfährt](/de/guides/workflows/continue-on-error/). |
| **Übersprungen** | Der Schritt wurde übergangen. |
| **Wird ausgeführt** | Der Schritt ist noch nicht beendet. |

Ein Schritt, dessen letzte Ausführungen bereits langsam waren oder stark schwanken, wird möglicherweise nicht markiert. Eine Ausführung zum Periodenende kann im Vergleich zu gewöhnlichen Tagen durchgehend langsamer erscheinen. Eine ältere gestoppte Ausführung erscheint als kurze Ausführung, nicht als gestoppt.

Das Fenster kann eine Markierung auch erklären. **Wartend** ist Zeit, in der kein Schritt lief, sodass kein Schritt dafür verantwortlich ist. Bei einem Schritt, der langsamer als üblich lief, vergleicht **Geschriebene Zeilen** die Ausgabe mit der üblichen Anzahl und entfällt, wenn Sicherheit auf Zeilenebene filtert, was Sie lesen können, und **Seit der letzten Ausführung gespeichert** besagt, dass der Schritt nach seiner vorherigen Ausführung und vor dem Start dieser Ausführung gespeichert wurde; der Datensatz zeigt ein Speichern, nicht was sich geändert hat. **Andere Arbeit** zählt die Schritte, die nicht ausgeführt wurden, und die Schritte, die ohne Verlauf ausgeführt wurden, gemessen am Verlauf jedes Schritts oder, wenn Sie mit einer anderen Ausführung vergleichen, an dieser Ausführung. **Parallel ausgeführt** bedeutet, dass die Teile des Workflows gleichzeitig liefen, sodass ihre Zeiten mehr ergeben als die Uhrzeit. **Aufrufer unsicher** bedeutet, dass der Verlauf nicht zeigen kann, welcher Schritt einen Workflow aufgerufen hat. **Name verborgen** kennzeichnet einen Schritt oder Workflow, dessen Namen Ihre Rolle nicht sehen kann; er erscheint als **Verborgener Schritt** oder **Verborgener Workflow**.

### Vergleichen mit

**Vergleichen mit** legt fest, woran eine Ausführung gemessen wird. Die Menüschaltfläche zeigt die Auswahl: **Üblich**, **Üblich + vorherige Ausführung** oder **Üblich + Ausführung vom** Startzeitpunkt der gewählten Ausführung. **Üblich** verwendet die letzten Ausführungen jedes Schritts. **Üblich + vorherige Ausführung** und **Üblich + gewählte Ausführung** fügen außerdem die Zeit dieser Ausführung für jeden Schritt hinzu, die die **Zeitachse** umrandet und die die **Tabelle** unter **Verglichene Ausführung** zeigt. **Üblich + gewählte Ausführung** öffnet eine Liste der letzten Ausführungen zur Auswahl.

### Ein Workflow innerhalb einer größeren Ausführung

Wenn Sie einen Workflow öffnen, den ein anderer Workflow aufgerufen hat, zeigt Insight nur den Teil der Ausführung, der zu diesem Workflow gehört. **Gesamte Ausführung öffnen** schaltet denselben Dialog auf den Workflow um, der die Ausführung gestartet hat.

### Laufende Ausführungen

Eine Ausführung, die noch läuft, wird alle 30 Sekunden neu gelesen, solange der Dialog sichtbar ist. Zoom, Auswahl und Ansicht bleiben erhalten. Wenn Sie Insight zugunsten von **Ausführungen** verlassen, enden die Aktualisierungen; kehren Sie zu Insight zurück, wird die Ausführung neu gelesen und die Aktualisierung setzt sich fort. Die Schaltfläche Aktualisieren, die kreisförmigen Pfeile rechts in der Kopfzeile, lädt die Ausführung von Grund auf neu, setzt Zoom und Auswahl zurück und klappt Blöcke im Plan wieder ein.

### Für KI-Assistenten und die REST-API

Dasselbe Profil ist auch außerhalb des Dialogs verfügbar:

- REST: `GET /rest/v1/analyze/workflow/run-insight` mit `project_id` und `workflow_id`. `run_id` wählt die Ausführung (die letzte, wenn es fehlt), und `baseline` ist `typical`, `previous` oder `run:<id>`.
- MCP: `workflow_describe` mit `include=['run_insight']` und optional `run_id` und `baseline`.

Jeder Workflow und jeder Schritt wird mit seiner Zeit, seiner Stellung in der Ausführung, einer Bewertung an seinem eigenen Verlauf und den Gründen zurückgegeben. Eine Ausführung, die nicht existiert oder keine Schrittzeilen hat, liefert kein Profil, sondern eine Warnung statt eines Fehlers.

## Anhalten, Beenden und Fortsetzen

Während ein Workflow läuft, können Sie ihn **anhalten**, sodass laufende Schritte abgeschlossen werden und neue Schritte warten, oder **beenden**, wodurch die Schritte in der Warteschlange und, innerhalb weniger Sekunden, alle noch laufenden Import- oder Export-Jobs abgebrochen werden, zusammen mit der Warehouse-Abfrage, die ein Export gerade gelesen hat. Import- und Dimensionsschritte, die noch in der Warteschlange standen, werden sauber abgebrochen, sodass sie spätere Importe und Dimensionsladevorgänge im Workspace nicht blockieren. Beenden stoppt außerdem die in der Warteschlange stehenden oder laufenden Connector-Synchronisierungen (Singer) des Workflows, sodass eine Synchronisierung nicht weiterläuft, nachdem der Workflow beendet wurde.

Sobald Sie einen Workflow **beenden**, startet ein laufender Import- oder Export-Job keinen neuen Schreibvorgang mehr: Ein Export lädt keine Datei hoch, und ein Import lädt keine Tabelle. Ein bereits laufender Schreibvorgang wird zuerst abgeschlossen, sodass keine Datei, Tabelle oder Dimension halb geschrieben zurückbleibt. Ein Export mit vielen Dateien oder ein Export mehrerer Tabellen behält die Dateien, die er bereits geschrieben hatte. Ein CSV-Export mit vielen Dateien, der vorzeitig beendet wird, hat seinen Ordner bereits geleert, sodass der Ordner nur diese Dateien enthält und keine aus einer früheren Ausführung. Ein Dimensionsladevorgang sowie ein MongoDB- oder Kafka-Export schreiben fortlaufend, sodass einer, der begonnen hat, bis zum Ende läuft. Ein Schritt **SQL importieren** oder **Externe Datenbanktabellen importieren** stoppt, sobald seine Quelldatenbank zurückgegeben hat, was er gelesen hat, weil PlaidCloud die Abfrage der Quelle nicht abbricht. Auf Databend ist ein Export, den Databend selbst in Ihr Dokumentenkonto schreibt, ein einziger Schreibvorgang, sodass er bis zum Ende läuft und seine Datei schreibt.

Ein Makro kann an mehreren Stellen gleichzeitig laufen, aufgerufen von anderen Workflows oder von einem Schritt **Makro: Gleichzeitige Ausführung**. Das Beenden des Makros beendet jede laufende Instanz davon. Das Beenden einer einzelnen Instanz beendet nur diese Instanz und das, was sie gestartet hat, und lässt den aufrufenden Workflow weiterlaufen; dasselbe gilt für einen Schritt **Macro Concurrent**, der eine nicht mehr reagierende Instanz aufgibt. Ein Makro, das nur innerhalb anderer Workflows läuft, wird in der Workflow-Liste als **Wird ausgeführt** angezeigt, wobei **Beenden** verfügbar ist, und wenn Sie es öffnen, sehen Sie für jeden Schritt den Status sowie die Start- und Endzeit aus seiner letzten Ausführung.

**Fortsetzen** nimmt eine angehaltene, beendete oder fehlgeschlagene Ausführung dort wieder auf, wo sie aufgehört hat, anstatt von vorn zu beginnen. Die Option steht zur Verfügung, wenn die letzte Ausführung eines Workflows im Zustand angehalten, beendet oder Fehler endete.

Was „dort, wo sie aufgehört hat“ bedeutet, hängt davon ab, wie der Workflow ausgeführt wird:

| Ausführung | Beim Fortsetzen |
|---|---|
| Serial | Startet bei dem Schritt neu, der beim Ende der Ausführung lief, und läuft von dort weiter. Liegt dieser Schritt in einer Gruppe, nimmt Fortsetzen die gesamte Gruppe der obersten Ebene auf, die ihn enthält: Schritte der Gruppe, die bereits erfolgreich abgeschlossen wurden, bleiben unberührt, die übrigen werden ausgeführt, und die Ausführung läuft nach der Gruppe weiter. |
| Parallel | Führt jeden Schritt erneut aus, der noch nicht erfolgreich abgeschlossen war, und lässt abgeschlossene Schritte unberührt. |
| Advanced (graph) | Führt den fehlgeschlagenen Knoten und alles, was noch auf ihn wartet, erneut aus und lässt abgeschlossene Knoten unberührt. |

Schritte, die einen anderen Workflow aufrufen — **Run Model**, **Conditional Run Model** und **Loop Model** — setzen den aufgerufenen Workflow fort, anstatt ihn neu zu starten, über beliebig viele Verschachtelungsebenen hinweg. Ein Schleifenschritt setzt die unterbrochene Iteration fort und überspringt die bereits abgeschlossenen Iterationen.

Wenn Sie einen Workflow fortsetzen, der als **verschachtelter untergeordneter Workflow** eines anderen lief — einen, den ein **Run Model**-Schritt in einem übergeordneten Workflow aufgerufen hat —, bietet PlaidCloud **Von Kettenanfang fortsetzen** an. Das alleinige Fortsetzen des untergeordneten Workflows kann die Orchestrierung des übergeordneten nicht weiterführen; diese Option setzt daher stattdessen den übergeordneten Workflow der obersten Ebene fort — die Wurzel der Kette — und führt die gesamte Kette dort weiter, wo sie angehalten hat. Das Fortsetzen eines Workflows der obersten Ebene bleibt unverändert. Der Kettenanfang wird innerhalb desselben Projekts ermittelt: Eine Kette, die in ein anderes Projekt hineinreicht, wird vom Anfang des Teils innerhalb des Projekts aus fortgesetzt.

Das Fortsetzen führt immer die **ursprüngliche** Ausführung weiter. Es führt jeden Schritt dieser Ausführung erneut aus, der nicht erfolgreich abgeschlossen wurde — ein fehlgeschlagener oder abgebrochener Schritt wird erneut ausgeführt und nicht als abgeschlossen behandelt —, und die zwischenzeitliche erneute Ausführung eines einzelnen Schritts ändert nicht, was das Fortsetzen als Nächstes aufnimmt. Das gilt auch für einen untergeordneten Workflow: Wenn Sie einen seiner Schritte einzeln erneut ausgeführt haben, führt das Fortsetzen des übergeordneten Workflows trotzdem alles aus, was im untergeordneten Workflow noch offen war, nicht nur diesen Schritt.

Eine fortgesetzte Ausführung wird als **neue Ausführung** im Ausführungsverlauf des Workflows erfasst und enthält nur die Schritte, die sie erneut ausgeführt hat. Die ursprüngliche Ausführung behält ihren eigenen Verlaufseintrag. Ruft eine Ausführung denselben untergeordneten Workflow mehrmals auf, erhält jeder Aufruf einen eigenen Eintrag im Ausführungsverlauf des untergeordneten Workflows. Die Iterationen eines Schleifenschritts zählen als ein Aufruf.

:::note
Ein Schleifenschritt ordnet seine abgeschlossenen Iterationen anhand ihrer Variablenwerte zu. Haben sich die Daten, über die die Schleife iteriert, zwischen der ursprünglichen Ausführung und dem Fortsetzen geändert, werden Iterationen, die sich nicht mehr zuordnen lassen, erneut ausgeführt statt übersprungen.
:::
