---
title: Einen Workflow optimieren
description: Beschleunigen Sie einen erweiterten Workflow, indem Sie seine Abhängigkeiten aus der Datenherkunft neu aufbauen und Ketten von Extraktionsschritten zusammenführen – jede Zusammenführung wird vor der Anwendung an Ihren Daten verifiziert.
sidebar:
  order: 19.6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/optimize-a-workflow.md
---

**Optimieren** prüft einen erweiterten Workflow und schlägt Änderungen vor, die ihn schneller ausführen. Sie sehen jede Änderung, bevor etwas geschieht, wählen die gewünschten aus und können das Ergebnis später rückgängig machen.

Die Optimierung funktioniert bei erweiterten (DAG-)Workflows. Wählen Sie bei einem Standard-Workflow zuerst **In Erweitert konvertieren...**; siehe [Erweiterte Workflows](/de/guides/workflows/advanced-workflows/#workflow-typ-wählen).

## Einen Workflow optimieren

1. Klicken Sie in der Liste **Workflows** mit der rechten Maustaste auf einen erweiterten Workflow und wählen Sie **Optimieren...**. Der Workflow darf nicht ausgeführt oder angehalten werden, und Sie benötigen Schreibzugriff darauf.
2. Das Fenster **Workflow optimieren** zeigt eine Kopfzeile wie *34 Schritte → 30 Schritte · 12 Schritte können parallel ausgeführt werden*. Hat der Workflow einen Ausführungsverlauf, kommt *~11 s schneller pro Ausführung* hinzu.
3. Unter der Kopfzeile steht pro Änderung eine Zeile, jeweils mit einem Kontrollkästchen, den betroffenen Schritten, ihrer Bedeutung für den Workflow und der eingesparten Zeit, gemessen als Änderung der Laufzeit (Wanduhrzeit). Alle sind angehakt; entfernen Sie den Haken bei denen, die Sie nicht möchten.
4. Eine Liste **Optimierung nicht möglich** nennt die Schritte, die die Optimierung unverändert gelassen hat, und den jeweiligen Grund; siehe [Warum ein Schritt nicht optimiert werden kann](#warum-ein-schritt-nicht-optimiert-werden-kann).
5. Wählen Sie **N Änderungen anwenden**.

Gibt es im Workflow nichts mehr zu verbessern, sagt das Fenster dies.

## Die zwei Arten von Änderungen

### Abhängigkeiten aus der Datenherkunft neu aufbauen

Die Optimierung liest, welche Tabellen jeder Schritt liest und schreibt, und zeichnet die Verbindungen neu, sodass ein Schritt nur auf die Schritte wartet, deren Tabellen er verwendet. Schritte, die keine Tabellen gemeinsam nutzen, werden parallel ausgeführt.

- Ein Schritt wartet nicht mehr auf nicht verwandte Schritte und hält daher nicht mehr an, wenn ein nicht verwandter Schritt fehlschlägt. Ein Fehler setzt sich entlang der neuen Abhängigkeiten fort.
- Eine Teilausführung nach Schrittbereich, etwa mit **Ab hier ausführen**, folgt den neuen Abhängigkeiten.
- Der Server begrenzt weiterhin, wie viele Schritte gleichzeitig laufen.
- Schritte, die ihre Tabellen über Namen oder Pfad angeben, werden genauso verstanden wie Schritte, die Tabellen-IDs verwenden. Ein Name muss genau einer Tabelle im Projekt entsprechen; ein Name, der mehreren Tabellen entspricht, ein Verweis mit einer Variable und eine Tabelle in einem anderen Projekt können nicht nachverfolgt werden.
- Ein deaktivierter Schritt trägt nie eine Reihenfolge und zählt nicht zu den Schritten, die parallel ausgeführt werden können.
- Die Optimierung lässt diese Änderung aus, solange ein Zeitplan oder ein anderer Workflow einen Bereich der Schritte dieses Workflows ausführt.

### Eine Kette von Extraktionsschritten zu einem zusammenführen

Eine Kette von Schritten vom Typ Extract Data, von denen jeder die Tabelle liest, die der vorige geschrieben hat, wird zu einem einzigen Schritt, der die erste Quelle liest und das letzte Ergebnis schreibt.

Jede Zusammenführung wird vor der Anwendung verifiziert. Die Optimierung führt die ursprünglichen Schritte und den zusammengeführten Schritt mit Ihren aktuellen Daten in temporäre Zwischentabellen aus und vergleicht die beiden Ergebnisse Zeile für Zeile. Die Zusammenführung wird nur angewendet, wenn sie identisch sind. Ihr Workflow und seine Tabellen werden während der Verifizierung nicht angetastet.

- Eine Umbenennung gefolgt von einem Filter, etwa ein Select-Schritt gefolgt von einem Filter, kann zu einem Schritt zusammengeführt werden.
- Lässt sich eine ganze Kette nicht zusammenführen, bietet die Optimierung den längsten Teil an, der sich zusammenführen lässt.
- Die Tabellen in der Mitte einer zusammengeführten Kette werden vom Workflow nicht mehr geschrieben. Sie bleiben erhalten und werden nicht gelöscht, und die Änderung nennt sie.
- Eine Zusammenführung, deren Ergebnisse abweichen oder die sich nicht verifizieren lässt, wird nicht angewendet, und die Ergebnisse nennen den Grund. Zusammenführungen benötigen eine Quelltabelle mit Daten.

## Warum ein Schritt nicht optimiert werden kann

Jede Zeile unter **Optimierung nicht möglich** nennt ihre eigene Ursache:

| Ursache | Bedeutung |
|---|---|
| Aggregiert | Der Schritt fasst Zeilen zusammen und kann daher nicht in einen Nachbarn aufgehen. |
| Zwei Filter | Eine Kette mit zwei Filtern kann nicht zu einem Schritt werden. |
| Filter auf einen Float, der runden kann | Eine Zusammenführung könnte ändern, welche Zeilen den Filter passieren, daher bleibt der Filter, wo er ist. |
| Ein Schritt, der Benutzercode ausführt | Ausdrücke, Skripte und ähnliche Schritte lassen sich nicht als gleichwertig verifizieren. |
| Eine Tabelle, die von mehr als einem Schritt gelesen wird | Die Tabelle in der Mitte der Kette wird anderswo benötigt. |
| Deaktivierter Schritt | Ein deaktivierter Schritt wird nicht zusammengeführt und trägt keine Reihenfolge. |
| Mitglied eines Ausführungscontainers | Schritte in einem Ausführungscontainer laufen als Einheit. |
| Keine Zeilenanzahl verfügbar | Die Zeilenanzahl der Quelltabelle lässt sich auch live nicht lesen, sodass die Zusammenführung für die Verifizierung nicht dimensioniert werden kann. |
| Tabelle nicht identifizierbar | Der Tabellenname des Schritts entspricht keiner oder mehr als einer Tabelle, verwendet eine Variable oder verweist auf ein anderes Projekt. |
| Sicherheit auf Zeilenebene oder zu groß | Die Tabelle unterliegt der Sicherheit auf Zeilenebene oder ist zu groß für eine automatische Verifizierung. |

Visuelle Container, die Schritte nur auf der Arbeitsfläche gruppieren, verhindern keine Zusammenführung. Entfernt eine Zusammenführung Schritte aus einem solchen Container, nimmt der zusammengeführte Schritt ihren Platz ein, und ein leer gewordener Container wird verworfen. Rückgängig machen stellt das Layout exakt wieder her.

## Den Fortschritt verfolgen

Nach dem Anwenden zeigt **Workflow wird optimiert** die Phase: *Verifizierung (3 von 6 Ausführungen)...*, *Ergebnisse werden verglichen...* und *Anwendung...*. Nach Abschluss listen die Ergebnisse auf, was **Angewendet** wurde, einschließlich der Zeilenanzahl, an der jede Zusammenführung verifiziert wurde, und was **Nicht angewendet** wurde, jeweils mit einem Grund.

Hat sich der Workflow geändert, während die Optimierung verifizierte, werden die betroffenen Änderungen übersprungen, und das Fenster nennt die Anzahl. Schlägt eine Anwendung fehl, wird der Workflow in den Zustand vor der Anwendung zurückversetzt.

Eine Ausführung, die startet, während die Änderungen übernommen werden, wird kurz verzögert, nicht verworfen.

## Eine Optimierung rückgängig machen

Klicken Sie mit der rechten Maustaste auf den Workflow und wählen Sie **Optimierung rückgängig machen...**, oder verwenden Sie **Optimierung rückgängig machen** in den Ergebnissen. Bestätigen Sie, und die Schritte, Einstellungen und das Layout des Workflows kehren in den Zustand vor der Optimierung zurück. Änderungen, die Sie seitdem am Workflow vorgenommen haben, gehen verloren.

Rückgängig machen benötigt Wiederherstellungspunkte, die nicht auf jedem Tenant verfügbar sind. Ein Tenant ohne sie kann keine Optimierung anwenden.

## Optimieren über die API und KI-Assistenten

Die Optimierung ist auch über die REST-API und über das Tool `workflow_optimize` für KI-Assistenten verfügbar, mit denselben Schritten für Vorschau, Anwenden und Rückgängigmachen.

## Nächste Schritte

- [Erweiterte Workflows](/de/guides/workflows/advanced-workflows/) – die Arbeitsfläche, Verbindungen und Ausführungssteuerung
- [Parallele Ausführung steuern](/de/guides/workflows/controlling-parallel-execution/) – Schritte gleichzeitig ausführen
- [Einen Workflow ausführen](/de/guides/workflows/run-a-workflow/) – einen Workflow von Anfang bis Ende ausführen
