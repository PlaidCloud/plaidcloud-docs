---
title: Macro Concurrent-Schritt
description: Führt je Zeile der Treibertabelle einen isolierten Makro-Aufruf aus, mit konfigurierbarem Grenzwert für die Gleichzeitigkeit.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/macro-concurrent.md
---

## Beschreibung

Führt ein [Makro](/de/guides/workflows/create-a-macro/) einmal für jede ausgewählte Zeile einer aufruferseitigen Treibertabelle aus. Jeder untergeordnete Aufruf verhält sich wie ein [Macro Run-Schritt](/de/reference/workflow-steps/workflow-control/run-macro/):

- Er erhält eine neue `run_id`.
- Er läuft in einem eigenen Scratch-Schema (`macrorun_<run_id>`).
- Er erhält Tabellen-, Skalar- und Dimensionsbindungen vom Aufrufer.
- Er kopiert deklarierte Ausgabetabellen in aufruferseitige Ziele zurück, wenn der untergeordnete Aufruf mit `done` oder `warn` endet.
- Er löscht das Scratch-Schema, wenn der untergeordnete Aufruf endet, fehlschlägt oder beendet wird.

Verwenden Sie den Macro Concurrent-Schritt, wenn derselbe wiederverwendbare Prozess für viele Zeilen ausgeführt werden soll, etwa je Periode, Entität, Kunde, Dateistapel oder Region und Zeile der Treibertabelle.

## Treiber

- **Tabelle** – die aufruferseitige Tabelle, die für jeden Makro-Aufruf eine Zeile enthält.
- **Gleichzeitige Ausführungen** – die maximale Anzahl untergeordneter Makro-Aufrufe, die gleichzeitig aktiv sein dürfen.

## Tabellendatenauswahl

Wählen Sie die Spalten der Treibertabelle aus, die jeder untergeordnete Aufruf benötigt. Diese Spalten können in den Makro-Bindungen und im Treiberfilter verwendet werden.

## Treiberfilter

Fügen Sie optional Filterregeln für die Treibertabelle hinzu. Nur passende Zeilen starten untergeordnete Makro-Aufrufe.

## Makro

- **Projekt** – das Projekt, das das Makro enthält. In v1 muss es dasselbe Projekt wie das des Aufrufers sein.
- **Makro** – der Makro-Workflow, der für jede ausgewählte Treiberzeile aufgerufen wird.

## Eingabebindungen

Eingabebindungen verbinden aufruferseitige Daten mit den deklarierten Eingaben des Makros.

**Tabelleneingabebindungen:**

- **Quelltabelle des Aufrufers** – die Tabelle, die in das Scratch-Schema des untergeordneten Aufrufs kopiert wird.
- **Makro-Zielport** – der Name der Makro-Eingabetabelle oder der Port, der die kopierte Tabelle empfängt.
- **Filter beim Hineinkopieren** – optionale `WHERE`-Klausel, die beim Hineinkopieren angewendet wird.
- **Spalten-JSON** – optionale JSON-Spaltenprojektion, wenn nur ausgewählte Spalten kopiert werden sollen.

**Skalar- und Dimensionseingabebindungen:**

- **Makrovariable** – die makroseitige Variable, die für den untergeordneten Aufruf gesetzt wird.
- **Wert** – der Literalwert, der Verweis auf eine Aufrufervariable oder der Wert einer Treiberspalte, der gebunden werden soll.

Skalar- und Dimensionseingaben werden vor dem Hineinkopieren der Tabellen gesetzt, sodass Tabellenfilter auf diese Variablen verweisen können.

## Ausgabebindungen

Ausgabebindungen kopieren Ergebnistabellen des Makros in aufruferseitige Ziele zurück.

- **Makro-Quellport** – der Name der Makro-Ausgabetabelle oder der Port, aus dem kopiert wird.
- **Zieltabelle des Aufrufers** – die aufruferseitige Tabelle, in die kopiert wird.
- **Spalten-JSON** – optionale JSON-Spaltenprojektion für das Herauskopieren.

Jede Treiberzeile muss auf eine andere Zieltabelle führen. Nehmen Sie daher eine Treiberspalte in den Zielnamen auf, zum Beispiel `results_{region}`. Das Herauskopieren ersetzt das Ziel, statt Daten anzuhängen. Würden zwei Zeilen auf dasselbe Ziel führen, bliebe nur das Ergebnis der zweiten Zeile erhalten; der Schritt lehnt diese Konfiguration ab, bevor er etwas startet. Um die Ergebnisse in einer Tabelle zusammenzuführen, fügen Sie nachgelagert einen Schritt hinzu, der die Tabellen der einzelnen Zeilen per Union vereinigt.

Das Herauskopieren wird für einen beendeten untergeordneten Aufruf übersprungen, damit keine Teilergebnisse in dauerhafte Tabellen des Aufrufers geschrieben werden.

## Wenn ein untergeordneter Aufruf nicht mehr antwortet

Ein untergeordneter Aufruf meldet sein Ergebnis selbst, wenn er endet. Ein Aufruf, dessen Rechner unvermittelt ausfällt, meldet daher gar nichts mehr. Statt unbegrenzt zu warten, prüft der Schritt, ob jeder untergeordnete Aufruf, auf den er noch wartet, aktiv ist.

- Ein gestarteter untergeordneter Aufruf wird ungefähr einmal pro Minute geprüft, und nur solange er keinen Fortschritt zeigt. Ein Aufruf, der einen einzelnen langen Schritt abarbeitet, zeigt so lange keinen Fortschritt, wie dieser Schritt dauert, und wird in Ruhe gelassen, solange er tatsächlich noch läuft.
- Ein untergeordneter Aufruf, der angenommen wurde, aber innerhalb von 15 Minuten nicht gestartet ist, gilt als nie gestartet. Dieses Zeitfenster umfasst die Planung und das Abrufen des Images, nicht die eigentliche Arbeit des Makros.

Ein auf eine dieser beiden Arten behandelter untergeordneter Aufruf wird beendet, sein Scratch-Schema wird gelöscht, und der Schritt schlägt am Ende fehl, wobei er diesen Aufruf, den zuletzt gemeldeten Status und den Zeitpunkt der letzten Meldung nennt.

**Die übrigen untergeordneten Aufrufe sind davon nicht betroffen.** Sie laufen bis zum Ende, und ihre Ausgabetabellen werden wie gewohnt geschrieben. Ein nicht antwortender Aufruf unter vielen verwirft also nicht die Ergebnisse der anderen. Nur die Aufrufe, die nicht abgeschlossen werden konnten, werden im Fehler genannt.

Kann die Prüfung selbst nicht beantwortet werden, etwa weil die Plattform kurzzeitig nicht erreichbar ist, gilt der untergeordnete Aufruf als weiterhin laufend und wird beim nächsten Durchgang erneut geprüft.

## Verhalten beim Beenden

Wenn Sie den übergeordneten Macro Concurrent-Schritt beenden, werden alle aktiven untergeordneten Makro-Aufrufe beendet und jedes aktive Ausführungsschema gelöscht. Untergeordnete Aufrufe, die noch nicht gestartet sind, werden nach dem Beenden des übergeordneten Schritts nicht mehr gestartet.

## Verwandte Themen

- [Makro erstellen](/de/guides/workflows/create-a-macro/) – deklarieren Sie einen Workflow als Makro und definieren Sie seinen Port-Vertrag.
- [Macro Run-Schritt](/de/reference/workflow-steps/workflow-control/run-macro/) – ruft ein Makro einmal auf.
