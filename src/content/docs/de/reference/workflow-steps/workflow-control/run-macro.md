---
title: Macro Run-Schritt
description: Ruft einen Makro-Workflow als isolierten Unteraufruf mit deklarierten Bindungen für Eingabe- und Ausgabeports auf – jeder Aufruf läuft in einem eigenen Scratch-Schema.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/run-macro.md
---

## Beschreibung

Ruft einen [Makro](/de/guides/workflows/create-a-macro/)-Workflow als ausführungsisolierten Unteraufruf auf. Anders als bei [Workflow ausführen](/de/reference/workflow-steps/workflow-control/run-workflow/) gilt für jeden Aufruf des Macro Run-Schritts:

- Er erhält eine neue, eindeutige `run_id`.
- Er läuft in einem eigenen, temporären Scratch-Schema (`macrorun_<run_id>`) im Katalog des Projekts.
- Er bindet beim Hineinkopieren aufruferseitige Tabellen und Variablen an die deklarierten Eingabeports des Makros.
- Er kopiert die deklarierten Ausgabetabellen des Makros bei Erfolg in aufruferseitige Ziele zurück.
- Er löscht das Scratch-Schema immer, wenn der Aufruf endet (Erfolg, Fehler oder Beenden).

Durch diese Isolation kann dasselbe Makro bedenkenlos gleichzeitig aufgerufen werden – aus einer übergeordneten Schleife, aus unabhängigen Workflows, die gleichzeitig laufen, oder rekursiv aus einem anderen Makro –, ohne dass Namen von Zwischentabellen zwischen Ausführungen kollidieren.

Der Ziel-Workflow muss als Makro gekennzeichnet sein. Ein Macro Run-Schritt, der auf einen Workflow ohne Makro-Kennzeichnung zeigt, schlägt mit einer eindeutigen Fehlermeldung fehl. Umgekehrt kann ein [Workflow ausführen](/de/reference/workflow-steps/workflow-control/run-workflow/)- oder [Workflow Loop-Schritt](/de/reference/workflow-steps/workflow-control/workflow-loop/) kein Makro als Ziel haben (diese Schritte besitzen den Isolationslebenszyklus pro Ausführung nicht).

## Auszuführendes Makro

- **Projekt** – das Projekt, das das Makro enthält. In v1 muss es dasselbe Projekt wie das des Aufrufers sein.
- **Makro** – der Makro-Workflow, der aufgerufen werden soll. Nach der Auswahl füllen die deklarierten Eingabe- und Ausgabeports des Makros die unten stehenden Bindungslisten.

## Bindungen der Eingabeports

Fügen Sie für jeden im Makro deklarierten Eingabeport eine Bindung hinzu. Bindungen werden in zwei Durchgängen verarbeitet – zuerst Skalar- und Dimensionseingaben (die in die ausführungsbezogene Variablenüberlagerung des Makros geschrieben werden), dann Tabelleneingaben –, sodass ein Filter einer Tabelleneingabe auf die Skalareingaben verweisen kann.

**Tabelleneingabeports:**

- **Quelle** – eine aufruferseitige Tabelle (per Name oder ID), deren Inhalt unter dem Portnamen in das Scratch-Schema des Makros kopiert wird.
- **Spalten** – optionale Spaltenprojektion. Wählen Sie eine Teilmenge aus und benennen Sie bei Bedarf um (`source` → `target`); die Spalten werden beim Hineinkopieren in Anführungszeichen gesetzt und angewendet, sodass nur die projizierten Spalten materialisiert werden.
- **Filter** – optionale `WHERE`-Klausel, die beim Hineinkopieren angewendet wird. Sie kann per Namen auf die Eingabevariablen des Makros verweisen (aufgelöst aus den obigen Skalarbindungen). Beispielsweise beschränkt `month = {month}` das Hineinkopieren auf den Ausschnitt eines Monats aus einer mehrjährigen Tabelle.

**Skalar-/Dimensionseingabeports:**

- **Variable** – der makroseitige Variablenname, der gesetzt werden soll (entspricht einem im Makro deklarierten Port).
- **Wert** – der Wert, der gebunden werden soll, entweder ein Literal oder ein Verweis auf eine aufruferseitige Variable (wird anhand der Variablen des Aufrufers aufgelöst, bevor er in die Überlagerung des Unteraufrufs geschrieben wird).

## Bindungen der Ausgabeports

Fügen Sie für jeden im Makro deklarierten Ausgabeport eine Bindung hinzu, die auf eine aufruferseitige Zieltabelle zeigt. Die Zieltabelle wird bei Bedarf automatisch angelegt, falls sie noch nicht existiert. Das Herauskopieren der Ausgabe:

- Erfolgt, nachdem das Makro erfolgreich abgeschlossen wurde (Status `done` oder `warn`).
- Wird **übersprungen**, wenn das Makro während der Ausführung manuell beendet wird (Status `stop`) – andernfalls würden Teilausgaben unbemerkt im dauerhaften Schema des Aufrufers landen.
- Die optionale Projektion der **Spalten** funktioniert genauso wie bei Eingabebindungen.

## Verhalten bei Fehlern

| Ergebnis des Makros     | Auswirkung beim Aufrufer                                                          |
|-------------------------|-----------------------------------------------------------------------------------|
| `done` / `warn`         | Ausgabetabellen in aufruferseitige Ziele kopiert; Scratch-Schema gelöscht.        |
| `stop` (manuell beendet) | Herauskopieren übersprungen; Scratch-Schema gelöscht; Warnung beim Aufrufer protokolliert. |
| Fehler während der Ausführung | Der Macro Run-Schritt schlägt fehl; Scratch-Schema gelöscht; Ausgaben nicht geschrieben. |

Schlägt der Workflow des Makros fehl, zeigt das Protokoll des Macro Run-Schritts die eigene Fehlermeldung des Makros („Child workflow run failed:“, gefolgt von der Meldung“). So sehen Sie, was zu beheben ist, ohne die Ausführung des Makros zu öffnen.

Das Scratch-Schema wird immer in einem `finally`-Block freigegeben, sodass ein fehlgeschlagenes oder beendetes Makro nie Zwischentabellen im Projektschema zurücklässt.

## Beispiele

Noch keine Beispiele …

## Verwandte Themen

- [Makro erstellen](/de/guides/workflows/create-a-macro/) – deklarieren Sie einen Workflow als Makro und definieren Sie seinen Port-Vertrag.
- [Workflow ausführen](/de/reference/workflow-steps/workflow-control/run-workflow/) – der nicht isolierte Aufrufer von Unter-Workflows (kann kein Makro als Ziel haben).
