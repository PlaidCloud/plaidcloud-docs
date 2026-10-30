---
title: "TM1: Cube abfragen"
description: Lesen Sie Cube-Daten von einem IBM TM1 / Planning Analytics-Server über eine gespeicherte Ansicht oder MDX, wenden Sie optional einen Betrachtungspunkt als Ausschnitt an und legen Sie das Ergebnis als Tabelle ab – cloud-direkt über REST, mit Vorschau vor dem Speichern.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query.md
---

## Beschreibung

Liest Daten aus einem IBM **TM1 / Planning Analytics**-Cube über Ihre [TM1-Verbindung](/de/guides/connections/tm1/), entweder durch Ausführen einer gespeicherten **Ansicht** oder durch eine von Ihnen geschriebene **MDX**-Abfrage. Ein Betrachtungspunkt (Point of View, POV) kann zusätzliche Dimensionselemente festlegen, die über das hinausgehen, was die Ansicht oder die MDX-Abfrage bereits festlegt. Das zurückgegebene Cellset landet als Projekttabelle – Schema-on-Read, mit Dimensionsspalten und einer Messwertspalte `Value`, erstellt aus den eigenen Achsen der Abfrage.

Dieser Schritt erscheint im Schrittmenü unter **IBM TM1 / Planning Analytics**.

Der Schritt greift **cloud-direkt** über die REST-API auf TM1 zu – es ist kein lokaler Agent beteiligt, und für diesen Schritt ist auch noch keiner verfügbar.

## Konfiguration

### Quelle und Ziel

| Feld | Erforderlich | Hinweise |
|---|---|---|
| TM1-Verbindung | Ja | Die [TM1-Verbindung](/de/guides/connections/tm1/), über die gelesen wird. |
| Umgebung | Ja | Die Umgebung der Verbindung. |
| Datenbank | Ja | Die abzufragende TM1-Datenbank (Instanz). Standardmäßig die Standarddatenbank der Verbindung, sofern eine festgelegt ist. |
| Cube | Ja | Der abzufragende TM1-Cube. Wird live von der verbundenen Datenbank ermittelt oder von Hand eingegeben. |
| Zieltabelle | Ja | Die Projekttabelle, in der das zurückgegebene Cellset abgelegt wird. |

### Ausschnitt

| Feld | Erforderlich | Hinweise |
|---|---|---|
| Quellmodus | Ja | `By View` (Standard) führt eine gespeicherte TM1-Ansicht aus. `By MDX` führt eine von Ihnen geschriebene MDX-Abfrage aus. |
| Ansicht | Bei Nach Ansicht | Die auszuführende gespeicherte TM1-Cube-Ansicht. Wird live ermittelt, sobald ein Cube ausgewählt ist, oder von Hand eingegeben. |
| MDX | Bei Nach MDX | Die MDX-Abfrage, die gegen den Cube ausgeführt wird. |

### Betrachtungspunkt

Legen Sie pro Dimension ein Element fest, um den Ausschnitt über das hinaus einzugrenzen, was die Ansicht oder die MDX-Abfrage bereits festlegt – nützlich für eine inkrementelle Extraktion (siehe unten). Fügen Sie eine Dimensionszeile hinzu, wählen Sie die Dimension und geben Sie das Element ein. Ein Elementwert kann ein Literal (`Jan-2026`) oder ein `{variable}`-Token sein, das zur Laufzeit aus den eigenen Variablen des Workflows aufgelöst wird – dieselbe Ersetzung, die auch das MDX-Feld selbst erhält. Lassen Sie den Betrachtungspunkt leer, um eine einfache Ansicht oder MDX-Abfrage zu lesen. Einen Betrachtungspunkt zusammen mit `By View` anzuwenden, wird nicht unterstützt – verwenden Sie `By MDX`, wenn Sie einen benötigen.

### Optionen

| Feld | Standard | Hinweise |
|---|---|---|
| Null-/Leerzellen unterdrücken | Aus | Verwirft Zellen, deren Wert genau numerisch `0` ist, **nachdem** sie abgerufen wurden. Das spart keine Bandbreite und verwirft in einem Planungs-Cube eine gebuchte `0`, die ein echter Fakt ist. Unterdrücken Sie Nullen besser in der Abfrage selbst – mit `NON EMPTY` in Ihrer MDX-Abfrage oder mit der Unterdrückungseinstellung der gespeicherten Ansicht –, damit TM1 sie gar nicht erst berechnet. |
| Zeilenlimit | 250.000 | Begrenzt die Anzahl der zurückgegebenen Zellen. Lassen Sie das Feld leer, um die Standardgrenze von 250.000 zu verwenden; erhöhen oder senken Sie sie ausdrücklich – ein nicht gesetztes Zeilenlimit bedeutet nicht „unbegrenzt“. Eine Abfrage, die das wirksame Limit überschreitet, wird abgelehnt, statt stillschweigend abgeschnitten zu werden. |

## Inkrementelle Extraktionen

TM1 hat keine integrierte Änderungsverfolgung, es gibt also keinen Aufruf nach dem Muster „liefere nur, was sich seit dem letzten Mal geändert hat“. Stattdessen **schneiden Sie bei jeder Ausführung nach Periode (oder Version) aus**: Legen Sie `Period` im Betrachtungspunkt auf eine Workflow-Variable `{period}` statt auf einen festen Elementnamen fest, sodass jede Ausführung ihre eigene Zielperiode einsetzt und die Daten einer einzelnen Periode statt des gesamten Cubes abruft. Kombinieren Sie dies mit einem geplanten Workflow und einer Variable, die sich bei jeder Ausführung weiterbewegt, um eine inkrementelle Historie Periode für Periode aufzubauen.

## Vorschau

Vor dem Speichern führt die **Vorschau** den aktuellen Ausschnitt gegen TM1 aus und zeigt die ersten Zeilen sowie die Zellenanzahl, begrenzt auf ein kleines Zeilenlimit, das unabhängig vom im Schritt konfigurierten Zeilenlimit gilt.

## Wenn Value als Text landet

Eine TM1-Messwertdimension enthält regelmäßig numerische Elemente (`Sales`, `Cost`) neben String-Elementen (`Comment`, `Status`) in derselben Dimension. Ein Ausschnitt, der beide umfasst, legt die Spalte `Value` als Text ab – eine Spalte hat genau einen physischen Typ, und eine einzige nicht numerische Zelle im Ausschnitt genügt, um ihn zu bestimmen.

Das ist korrektes Verhalten: Die String-Zellen auf null zu setzen, würde Daten verlieren, die Abfrage fehlschlagen zu lassen, würde einen legitimen Cube blockieren, und eine Aufteilung in zwei Spalten würde das Schema von den zurückgegebenen Daten abhängig machen. Stattdessen weist der Schritt darauf hin. Er gibt eine Warnung aus, die die Spalte, den Umfang und die verursachenden Elemente nennt, zum Beispiel:

> Column Value landed as text: 3 of 4,812 cells are non-numeric (text or boolean), and a column can only have one type. The non-numeric cells come from element Comment. Exclude that element from the slice, or query it separately, to keep this column numeric.

Die **Vorschau** zeigt dieselben Details vor dem Speichern, und die Elementauswahl für den Betrachtungspunkt kennzeichnet den TM1-Typ jedes Elements (Numeric, String oder Consolidated), sodass ein String-Element sichtbar ist, bevor Sie es festlegen. Ein String-Element im Betrachtungspunkt festzulegen, wird nicht blockiert – es ist eine legitime Möglichkeit, einen Textmesswert zu lesen –, legt aber die gesamte Spalte `Value` als Text ab, da der Messwert im Betrachtungspunkt statt auf einer Achse liegt; in diesem Fall meldet die Warnung die Anzahlen ohne Nennung eines Elements, weil jedes Element auf den Achsen gleichermaßen nicht numerisch ist und keines den Ausschnitt unterscheidet.

Um `Value` numerisch zu halten, schließen Sie das String-Element aus dem Ausschnitt aus oder fragen Sie die String-Messwerte und die numerischen Messwerte getrennt ab.

## Funktionsgrenzen

| Einschränkung | Bedeutung |
|---|---|
| Nur lesend | Liest Cube-Daten aus TM1. Kein Zurückschreiben, keine Ausführung von TI-Prozessen. |
| Nur cloud-direkt | Für diesen Schritt gibt es noch keinen lokalen PlaidLink-Agent-Pfad – der TM1-Server benötigt einen Netzwerkpfad, den PlaidCloud direkt erreichen kann. |
| Keine Änderungsverfolgung | TM1 bietet keine Delta- bzw. Seit-Änderung-API. Schneiden Sie stattdessen bei jeder Ausführung nach Periode oder Version aus (siehe Inkrementelle Extraktionen oben). |
| Kein Import von Dimensionen/Hierarchien | Dieser Schritt liest Cube-Daten. Der Import von TM1-Dimensionshierarchien als PlaidCloud-Dimensionen ist noch nicht verfügbar. |

## Verwandte Themen

- [Mit TM1 verbinden (Leitfaden)](/de/guides/connections/tm1/) – Verbindung erstellen und eine Abfrage aufbauen.
- [TM1-Konnektor](/de/reference/connectors/rest/tm1/) – Referenz der Verbindungsfelder.
- [IBM TM1 / Planning Analytics-Schritte](/de/reference/workflow-steps/ibm-planning-analytics/)
