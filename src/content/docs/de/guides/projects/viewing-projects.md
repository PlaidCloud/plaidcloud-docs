---
title: Projekte anzeigen
description: Zeigen Sie die Projekte an, für die Sie berechtigt sind, und durchsuchen Sie sie, einschließlich Projektdetails, Status, Mitgliedschaft und zugehöriger Datenressourcen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/viewing-projects.md
---

## Beschreibung


In **Analysieren** bieten Projekte eine Ebene der Abgrenzung, die das Steuern des Zugriffs und das Ändern von Berechtigungen erheblich erleichtert. Projekte bilden die primäre Trennung von Daten innerhalb einer Workspace-Registerkarte.



Projekte gehören zu Analyze, und Workflows gehören zu Projekten, das heißt, Projekte enthalten Workflows. Workflows erfüllen ganz einfach gesagt ein breites Spektrum an Aufgaben, darunter Datentransformations-Pipelines, Datenanalyse und sogar ETL-Prozesse. Weitere Informationen zu Workflows finden Sie im Abschnitt „Workflows“.



## Auf Projekte zugreifen


**So greifen Sie auf Projekte zu:**


1. Öffnen Sie Analyze
2. Wählen Sie in der oberen Menüleiste „Projekte“ aus

Daraufhin wird die Projekthierarchie angezeigt. Dort sehen Sie eine Hierarchie der Projekte, auf die Sie Zugriff haben. Im Workspace kann es weitere Projekte geben, die Sie jedoch nicht sehen, wenn Sie weder Eigentümer noch dem Projekt zugewiesen sind.


## Der Aktivitätsbereich

Der Bereich **Aktivität** rechts im Fenster „Projekte“ zeigt, was in Ihren Projekten ausgeführt wurde, ob es funktioniert hat und wer was geändert hat. Er listet die Aktivität aller Projekte auf, auf die Sie Zugriff haben, die neueste zuerst, unter einer Kopfzeile für jeden Tag. Er prüft etwa alle 15 Sekunden auf neue Aktivität, solange das Fenster „Projekte“ das aktive Fenster und Ihr Browser-Tab sichtbar ist.

Die Kopfzeile jedes Tages lautet **Heute**, **Gestern** oder das Datum, mit einer Zusammenfassung der Zeilen dieses Tages, etwa „12 Ausführungen · 1 fehlgeschlagen · 3 Änderungen“. Die Kopfzeile des Tages, durch den Sie gerade blättern, bleibt oben in der Liste stehen.

### Ausführungen

Eine Ausführung eines Workflows hat eine Zeile. Ein Symbol zeigt, wie sie verlaufen ist, und beim Daraufzeigen nennt es den Status: Erfolgreich, Fehlgeschlagen, Warnung, Gestoppt oder Gestartet. Zeilen mit einem Fehler oder einer Warnung haben außerdem einen farbigen Balken am linken Rand.

- **Die erste Zeile** nennt den Workflow und die Zeit: „jetzt“, vor Minuten oder vor Stunden für heute oder die Uhrzeit an einem früheren Tag. Zeigen Sie auf die Zeit, um das vollständige Datum zu sehen.
- **Die zweite Zeile** nennt, wer sie ausgeführt hat und in welchem Projekt, etwa „mike hat ausgeführt · CFO Services“, „Geplante Ausführung · CFO Services“ oder „Sensor-Ausführung · CFO Services“. Rechts steht, wie lange die Ausführung gedauert hat, oder **Fehlgeschlagen** oder **Gestoppt** mit ihrer Dauer. Bei einer gestoppten Ausführung steht, wer sie gestoppt hat.
- **Eine dritte Zeile**, falls vorhanden, zeigt, was schiefgegangen ist. Wenn während der Ausführung ein Schritt fehlgeschlagen ist oder eine Warnung ausgegeben hat, zeigt sie den Namen des Schritts und seine Meldung, mit „+2 weitere“, wenn auch andere Schritte Probleme hatten. Klicken Sie auf diese Zeile, um den Workflow an diesem Schritt zu öffnen.

Solange eine Ausführung läuft, steht sie unter [Läuft jetzt](#läuft-jetzt). Sobald sie endet, zeigt ihre Zeile das Ergebnis. Ein Workflow, der von einem anderen Workflow ausgeführt wird, über einen Schritt Workflow: Ausführen oder als Makro, hat keine eigene Zeile, und ein Schrittproblem darin erscheint in der Zeile der Ausführung, die ihn aufgerufen hat. Ein Schrittproblem, dessen Ausführung nicht in der Liste steht, hat eine eigene Zeile, etwa „Schritt fehlgeschlagen · CRM Pipeline · CFO Services“.

Änderungen, etwa an Workflows, Schritten, Tabellen, Dimensionen und Projekten, haben je eine Zeile, etwa „mike hat den Schritt geändert · CFO Services“ unter dem Namen des Schritts.

Die meisten Zeilen öffnen das, was sie nennen, wenn Sie darauf klicken oder die Eingabetaste drücken. Eine Ausführung oder ein Workflow, der erstellt, geändert, importiert oder exportiert wurde, öffnet das zugehörige Projekt auf der Registerkarte **Workflows** mit dem ausgewählten Workflow. Ein Schrittproblem oder ein Schritt, der erstellt, geändert, gelöscht, kopiert oder verschoben wurde, öffnet den Workflow an diesem Schritt. Eine Tabelle, die erstellt, umbenannt, veröffentlicht oder die Veröffentlichung aufgehoben wurde, öffnet sich im Tabellen-Explorer, eine Dimension, die erstellt oder geändert wurde, öffnet sich zum Bearbeiten, und ein Projekt, das erstellt, geändert, importiert, exportiert oder gesichert wurde oder dessen Sicherheit sich geändert hat, öffnet das Projekt.

### Wiederholte Zeilen

Aufeinanderfolgende Bearbeitungen derselben Art durch dieselbe Person am selben Objekt werden zu einer Zeile zusammengefasst, ebenso aufeinanderfolgende erfolgreiche Ausführungen desselben Workflows, die auf dieselbe Weise von derselben Person oder demselben Zeitplan gestartet wurden. Klicken Sie in der Zeile auf **3 Bearbeitungen** oder **4 Ausführungen**, um jede einzelne zu sehen, und klicken Sie erneut darauf, um sie wieder einzuklappen.

### Läuft jetzt

Workflows, die gerade laufen, stehen unter **Läuft jetzt** über der Liste, mit der Person, die sie gestartet hat, und der bisherigen Laufzeit. Eine pausierte Ausführung zeigt **Pausiert**. Klicken Sie auf den Namen eines Workflows, um ihn in der Liste **Workflows** seines Projekts auszuwählen, oder auf **Beenden**, um diese Ausführung zu beenden.

### Aktionen beim Daraufzeigen

Zeigen Sie auf die Zeile einer Ausführung oder gehen Sie mit der Tastatur zu ihr, um zwei Symbolschaltflächen einzublenden, deren Tooltipps **Protokoll öffnen** und **Workflow ausführen** lauten:

- **Protokoll öffnen** öffnet das Protokoll des Projekts, gefiltert auf diesen Workflow. Die Zeile eines Schrittproblems hat diese Schaltfläche ebenfalls.
- **Workflow ausführen** führt den Workflow erneut aus.

**Beenden** und **Workflow ausführen** sind für dieselben Mitglieder erlaubt wie das Beenden und Ausführen des Workflows in seinen eigenen Bildschirmen. **Workflow ausführen** führt den gesamten Workflow mit seinen Standardeinstellungen aus, auch wenn die Ausführung in der Zeile ein einzelner Schritt, ein Bereich von Schritten oder eine Simulation war.

### Probleme und Filter

Wenn die geladene Aktivität Ausführungen oder Schritte enthält, die fehlgeschlagen sind oder eine Warnung ausgegeben haben, zeigt die Kopfzeile des Bereichs eine Anzahl wie **2 Probleme**, als Fehler markiert, wenn eines davon fehlgeschlagen ist. Klicken Sie darauf, um nur diese Zeilen anzuzeigen.

Die Leiste unten im Bereich bestimmt, was die Liste zeigt:

| Auswahl | Zeigt |
|---|---|
| **Alle** | Alles |
| **Ausführungen** | Ausführungen von Workflows |
| **Änderungen** | Änderungen an Workflows, Schritten, Tabellen, Dimensionen, Projekten und mehr |
| **Probleme** | Ausführungen und Schritte, die fehlgeschlagen sind oder eine Warnung ausgegeben haben |
| **Meine** | Ihre eigenen Ausführungen und Änderungen |

Geben Sie in **Filter** einen Text ein, um nur die Zeilen anzuzeigen, in deren Workflow-, Projekt-, Schritt-, Tabellen-, Dimensions- oder Mitgliedsnamen er vorkommt. Am Ende der Leiste steht, wie viele Ereignisse passen, etwa **12 Ereignisse**. Der Bereich merkt sich Ihre Auswahl in diesem Browser.

### Neu seit Ihrem letzten Besuch

Eine Zeile **Neu seit Ihrem letzten Besuch** trennt, was seit Ihrem vorherigen Besuch eingetroffen ist, von dem, was Sie bereits gesehen haben. Sie erscheint, wenn **Alle** ausgewählt ist und in **Filter** nichts eingegeben ist. Ein Besuch endet, wenn Sie zu einem anderen Fenster wechseln oder das Fenster „Projekte“ schließen, und die Zeile rückt weiter, wenn Sie das Fenster „Projekte“ das nächste Mal öffnen oder die Seite neu laden.

### Frühere anzeigen

Die Liste beginnt mit den letzten 7 Tagen. Klicken Sie am Ende der Liste auf **Frühere anzeigen**, um bis zu 500 weitere Ereignisse aus den 30 Tagen vor dem ältesten geladenen zu laden, und klicken Sie erneut, um weiter zurückzugehen. Die Schaltfläche verschwindet, sobald ein Zeitraum von 30 Tagen keine Aktivität enthält.

### Tastatur

Drücken Sie die Tabulatortaste, um zu einer Zeile zu gelangen, und bewegen Sie sich dann mit den Pfeiltasten nach oben und unten zwischen den Zeilen; mit der Eingabetaste öffnen Sie die Zeile, auf der Sie stehen. Die Tabulatortaste führt auch zu den Aktionen der Zeile beim Daraufzeigen.

### Einschränkungen

- **Ihr letzter Besuch wird pro Browser gespeichert.** In einem anderen Browser oder auf einem anderen Gerät bezieht sich die Zeile **Neu seit Ihrem letzten Besuch** auf Ihren letzten Besuch dort.
- **Anzahlen beschreiben die im Bereich geladene Aktivität.** Die Anzahl der Probleme, **Probleme** und die Tageszusammenfassungen umfassen zunächst die neuesten 500 Ereignisse der letzten 7 Tage und mit **Frühere anzeigen** entsprechend mehr. Es sind keine Summen für Ihre Projekte.
- **Eine eingereihte Ausführung wird als Gestartet angezeigt** und erscheint unter **Läuft jetzt**, sobald sie tatsächlich startet. Ihre Dauer zählt ab dem Zeitpunkt des Einreihens.
- **Schrittprobleme aus einem Makro in einem Makro** erscheinen nicht in der Zeile der Ausführung der obersten Ebene.
- **Ein Workflow, der oft ausgeführt wird,** hat viele Zeilen. Aufeinanderfolgende erfolgreiche Ausführungen werden zusammengefasst, die von zwei Workflows, die abwechselnd laufen, jedoch nicht.
- **Ausführungen aus der Zeit vor der Veröffentlichung dieses Bereichs** erscheinen als Gestartet, ohne Ergebnis, und Stopps aus dieser Zeit erscheinen nicht.
- **Ein verspätet aufgezeichnetes Ereignis**, nachdem bereits neuere erschienen sind, erscheint, sobald Sie die Seite neu laden.
- **Ein Fenster „Projekte“, das länger als 30 Tage geöffnet und ungenutzt bleibt,** setzt 30 Tage zurück wieder an.
- **Bei keiner Aktivität in den letzten 7 Tagen** zeigt der Bereich „Keine Aktivitäten in den letzten 7 Tagen.“, und **Frühere anzeigen** erscheint nicht, sodass sich frühere Aktivität nicht laden lässt.
