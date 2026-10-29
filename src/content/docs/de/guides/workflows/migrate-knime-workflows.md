---
title: KNIME-Workflows migrieren
description: Konvertieren Sie einen KNIME-Workflow (.knwf) oder eine Workflow-Gruppe (.knar) über die Analyze-App, die REST-API oder einen per MCP verbundenen KI-Agenten in erweiterte PlaidCloud-Workflows, binden Sie Eingaben und Verbindungen und lesen Sie den Konvertierungsbericht.
sidebar:
  order: 31.7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-knime-workflows.md
---

PlaidCloud ist ein Drop-in-Ersatz für KNIME. 98,5 % der KNIME-Knotenkonfigurationen werden vollständig konvertiert, und 205 der 207 Kernknotentypen sind Full: Jeder wird zu standardmäßigen PlaidCloud-Workflow-Schritten, die die Aufgabe des Knotens übernehmen. Der Konverter wandelt ein KNIME-Workflow-Archiv in ausführbare erweiterte Workflows um, behält den ursprünglichen Graphen bei und liefert einen Konvertierungsbericht, der alles benennt, was Sie noch festlegen müssen. Die [KNIME-Konvertierungsmatrix](/de/reference/knime-conversion-matrix/) listet jeden Knoten auf.

Die Konvertierung liest nur das Archiv, auf das Sie verweisen. Sie nimmt nie Kontakt zu dem System auf, aus dem ein KNIME-Knoten liest oder in das er schreibt.

Die Konvertierung ist ein einmaliger Vorgang. Wenn Sie dasselbe Archiv erneut konvertieren, entstehen neue Workflows, und Änderungen, die Sie in PlaidCloud vorgenommen haben, werden nie mit einem späteren Export zusammengeführt.

## Was PlaidCloud erstellt

- Ein erweiterter Workflow für jeden KNIME-Workflow. Aus einer `.knwf` entsteht ein Workflow, aus einer `.knar` einer für jeden Workflow der Gruppe.
- Jeder KNIME-Knoten wird zum passenden Workflow-Schritt, zur Projektvariablen oder zum Arbeitsflächenobjekt, wobei die Beziehungen zu vor- und nachgelagerten Knoten erhalten bleiben. Metaknoten und Komponenten werden in den Workflow aufgelöst, sodass ihre Knoten als gewöhnliche Schritte ausgeführt werden.
- Flow-Variablen sowie Configuration- und Widget-Knoten werden zu Projektvariablen mit ihren Standardwerten. Switches und Schleifen, deren Werte bei der Konvertierung bekannt sind, werden bereinigt und in die Schritte aufgelöst, die sie ausführen.
- Die KNIME-Ausdruckssprachen – Expression, String Manipulation, Math Formula, Column Expressions und Rule Engine – werden in PlaidCloud-Ausdrücke konvertiert.
- Datendateien, die im Archiv enthalten sind, werden in einen Ordner `knime/` im Standard-Dokumentenkonto des Projekts hochgeladen, ein Ordner pro Workflow, und die konvertierten Reader importieren sie von dort.
- Ansichten, Diagramme und Color Manager haben keine Auswirkung auf die Daten. Sie werden verworfen und im Konvertierungsbericht aufgeführt.

## Bevor Sie beginnen

1. Exportieren Sie den Workflow aus der KNIME Analytics Platform als `.knwf`-Datei. Um mehrere Workflows auf einmal zu konvertieren, exportieren Sie deren Workflow-Gruppe als `.knar`-Datei. Legen Sie die Dateien, die Ihre Reader verwenden, im Ordner `data` des Workflows ab, damit sie im Archiv enthalten sind.
2. Laden Sie das Archiv in ein [Dokumentenkonto](/de/guides/documents/adding-accounts/) hoch, auf das Sie lesend zugreifen können. In der Analyze-App lädt **Durchsuchen** im Importfenster es von Ihrem Computer hoch.
3. Wählen Sie das PlaidCloud-Projekt aus, das die Workflows erhalten soll. Sie müssen Architect oder Manager des Projekts sein, und das Projekt muss ein Standard-Dokumentenkonto haben.
4. Notieren Sie sich die PlaidCloud-Tabellen, Dateien und Verbindungen, die die Reader und Connector-Knoten des Workflows verwenden sollen. Siehe [Quellen binden](#quellen-binden).

## Einen Workflow konvertieren

Konvertieren Sie über die Analyze-App, die REST-API oder einen per MCP verbundenen KI-Agenten. Die REST-API und das MCP-Tool nehmen dieselben Felder entgegen; das Fenster nimmt die Felder entgegen, die es anzeigt.

### Analyze-App

1. Öffnen Sie **Analyze** und wählen Sie **Tools → KNIME-Workflow importieren**.
2. Wählen Sie unter **Importquelle und -ziel** das **Zielprojekt** und das **KNIME-Archiv (.knwf oder .knar)** in einem Dokumentenkonto aus. Wählen Sie **Durchsuchen**, um das Archiv von Ihrem Computer hochzuladen.
3. Legen Sie unter **Objektpräfixe** optional das **Workflow-Präfix**, das **Schrittpräfix** und das **Tabellenpräfix** fest. Das Tabellenpräfix ist standardmäßig der Name des Workflows.
4. Binden Sie unter **Quellbindungen (optional)** optional einen Reader an eine vorhandene Tabelle im Zielprojekt: Wählen Sie **Hinzufügen** und geben Sie dann den **KNIME-Reader** (seine Knoten-ID, etwa `12:3`, seinen Knotennamen oder seinen Dateinamen) und die **Tabellen-ID** ein. Um Verbindungen, Dokumente oder Tabellen in anderen Projekten zu binden, verwenden Sie die REST-API oder das MCP-Tool. Siehe [Quellen binden](#quellen-binden).
5. Wählen Sie **Importieren**.

Das Fenster zeigt den Fortschritt, während es das Archiv konvertiert, und danach den Konvertierungsbericht: Schrittanzahlen (**Schritte**, **Hohe Konfidenz**, **Mittel**, **Niedrig** und **Nicht konvertiert**), die Knoten, die nicht konvertiert werden konnten, und die ihnen nachgelagerten Schritte, teilweise Konvertierungen, Warnungen, die hochzuladenden Quelldateien und die Knoten ohne Schritt. Wenn bei einer Konvertierung nichts zu prüfen ist, wird dies angezeigt, und das Fenster schließt sich von selbst.

### Felder

| Feld | Erforderlich | Funktion |
| --- | --- | --- |
| `source_account_id` | Ja | Dokumentenkonto, das das KNIME-Archiv enthält. |
| `source_file_path` | Ja | Pfad der `.knwf`- oder `.knar`-Datei innerhalb dieses Kontos. |
| `project_id` | Ja | Projekt, in dem die Workflows erstellt werden. |
| `workflow_prefix` | Nein | Präfix, das den Workflow-Namen vorangestellt wird. |
| `step_prefix` | Nein | Präfix, das den Schrittnamen vorangestellt wird. |
| `table_prefix` | Nein | Präfix, das den Tabellennamen vorangestellt wird. Standardmäßig der eigene Name des Workflows. Ein Präfix, das einen vorhandenen Tabellennamen wiederverwenden würde, wird abgelehnt, bevor etwas erstellt wird. Bei einer `.knar` folgt auf das Präfix jeweils der Name des jeweiligen Workflows. |
| `source_bindings` | Nein | Bindet Reader und Connector-Knoten an Daten und Verbindungen, die Sie bereits haben, bis zu 500 Einträge. Siehe [Quellen binden](#quellen-binden). |

### REST

Senden Sie die Felder als JSON-Body an:

```text
POST /rest/v1/analyze/knime/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/knime/monthly-close.knwf",
  "project_id": "<project id>"
}
```

### MCP

Ein per MCP verbundener KI-Agent ruft das Tool `knime_convert` mit denselben Feldern auf. Wie Sie einen Agenten verbinden, finden Sie unter [KI-Agenten (MCP)](/de/integrations/ai-coding-agents/). Das Tool verändert Ihr Projekt, prüfen Sie den Aufruf daher, bevor Sie ihn genehmigen.

## Quellen binden

Verwenden Sie `source_bindings`, um einen KNIME-Reader auf Daten zu richten, die bereits in PlaidCloud vorhanden sind, statt auf die Kopie im Archiv. Ein Schlüssel ist eine Knoten-ID (etwa `12:3`), ein Knotenname, ein Pfad einer enthaltenen Datei (etwa `data/sales.csv`) oder ein Dateiname; die erste Übereinstimmung in dieser Reihenfolge gilt. Ein Wert ist einer der folgenden:

- Eine `analyzetable_`-ID für eine Tabelle im Zielprojekt. Die Tabelle ersetzt den Reader.
- `{"project": "<project id>", "table": "<table id>"}` für eine Tabelle in einem anderen Projekt, auf die Sie lesend zugreifen können. Der Reader wird zu einem Schritt [Import Project Table](/de/reference/workflow-steps/import/import-project-table/), der sie kopiert. Das Quellprojekt muss Lesen für das Zielprojekt freigeben, sonst gibt der Schritt eine Warnung aus. Eine Tabelle, für die Zeilenzugriff gilt, wird abgelehnt.
- `{"account": "<document account id>", "path": "/finance/budget.xlsx"}` für ein Dokument, auf das Sie lesend zugreifen können. Der Reader importiert es.
- `{"connection": "<connection id>"}` für einen Datenbank- oder REST-Connector-Knoten. Die konvertierten Schritte werden über diese Verbindung ausgeführt.

Das Fenster der Analyze-App bindet Reader per Tabellen-ID an Tabellen im Zielprojekt. Binden Sie Verbindungen, Dokumente und Tabellen in anderen Projekten über die REST-API oder das MCP-Tool.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "data/budget.xlsx": { "account": "<document account id>", "path": "/finance/budget.xlsx" }
}
```

Eine gebundene Tabelle, die nicht existiert, oder ein Schlüssel, der zu keinem Reader passt, führt zu einer Warnung. Die angewendeten Bindungen mit ihren Projekt- und Tabellennamen sind im Konvertierungsbericht unter `bindings` aufgeführt.

### Ungebundene Eingaben

Ein Reader, dessen Datei nicht im Archiv enthalten ist, liest aus `inputs/<file name>` im Ordner des Workflows im Standard-Dokumentenkonto, und der Konvertierungsbericht führt den Pfad unter `missing_inputs` mit einer Warnung auf. Laden Sie die Datei dort hoch und führen Sie den Workflow aus. Solange die Datei nicht vorhanden ist, endet der Import mit einer Warnung und erstellt eine leere Tabelle, und der Workflow läuft weiter.

## Anmeldedaten und Verbindungen

KNIME-Anmeldedaten werden nie migriert. Jeder Schritt, der sich bei einem anderen System anmeldet, liest seine Anmeldedaten aus einer PlaidCloud-Verbindung oder einer von Ihnen festgelegten Projektvariablen, und die Warnung des Schritts im Konvertierungsbericht nennt, welche.

| KNIME | Was Sie festlegen |
| --- | --- |
| Datenbank-Connectors | Eine Datenbankverbindung: Binden Sie sie mit `{"connection": "<id>"}` oder wählen Sie sie im Schritt aus. |
| REST- und Webservice-Knoten, die sich anmelden | Eine [REST-Verbindung](/de/reference/connectors/rest/generic-rest/): Binden Sie sie mit `{"connection": "<id>"}` oder wählen Sie sie im Schritt aus. |
| Speech Recognizer (IBM Watson) | Eine REST-Verbindung, deren Basis-URL die in der Warnung genannte Watson-Dienst-URL ist, mit dem Benutzer `apikey` und Ihrem API-Schlüssel als Basic-Anmeldung. Binden Sie sie an den Knoten. |
| Email Connector, mit Email Reader oder Email Mover | Eine Projektvariable mit dem Kennwort des Mailservers, mit dem in der Warnung genannten Namen. Host und Benutzer stammen vom Email Connector. |
| Excel Reader oder Excel Writer mit Arbeitsmappenkennwort | Eine Projektvariable mit dem Kennwort, mit dem in der Warnung genannten Namen. |
| LLM-Connectors und -Authenticators | Eine LLM-Verbindung im KI-Schritt. |

Wie Sie Projektvariablen festlegen, finden Sie unter [Workflow-Variablen verwalten](/de/guides/workflows/manage-workflow-variables/).

## Den Konvertierungsbericht lesen

Das Fenster der Analyze-App zeigt den Konvertierungsbericht an, wenn der Import abgeschlossen ist, und die Antworten von REST und MCP enthalten ihn. Lesen Sie ihn, bevor Sie die Workflows ausführen.

- `summary` zählt die erstellten Schritte und wie viele davon mit hoher, mittlerer oder niedriger Konfidenz zugeordnet wurden.
- `warnings` listet jede Warnung mit ihrem Knoten, ihrem Schritt und der erforderlichen Maßnahme auf, einschließlich aller Anmeldedaten oder Verbindungen, die Sie festlegen müssen.
- `missing_inputs` listet die Dokumentenpfade auf, in die Dateien für ungebundene Eingaben hochzuladen sind.
- `bindings` listet die angewendeten Bindungen auf.
- `table_prefix` ist das verwendete Präfix. Bei einer `.knar` listet `workflows` jeden Workflow mit seinem eigenen Präfix auf.
- `uploaded_files` führt neben dem Bericht die enthaltenen Dateien auf, die in das Standard-Dokumentenkonto hochgeladen wurden.
- `dropped_tools` listet die Ansichten und Diagramme auf, die verworfen wurden.

## Platzhalter

Ein Knoten ohne Konvertierungspfad bleibt als benannter Platzhalter auf der Arbeitsfläche. Der Platzhalter reicht seine Daten durch und warnt mit dem Namen des KNIME-Knotens, und jeder nachgelagerte Schritt wird im Bericht markiert, sodass ein fehlendes Ergebnis nie unbemerkt bleibt. Bauen Sie die Funktion mit einem Standardschritt nach, wenn ihr Ergebnis wichtig ist.

## Den konvertierten Workflow ausführen

1. Öffnen Sie den neuen Workflow im Projekt.
2. Legen Sie die Projektvariablen und Verbindungen fest, die die Warnungen nennen.
3. Laden Sie Dateien für ungebundene Eingaben in die Pfade hoch, die im Fenster unter **Hochzuladende Quelldateien** oder in `missing_inputs` stehen.
4. [Führen Sie den Workflow aus](/de/guides/workflows/run-a-workflow/) und prüfen Sie die Ausgabetabelle jedes Schritts.

## Sonderfälle

Dies sind die einzigen bekannten Unterschiede zu KNIME.

- **Crosstab.** Wird zu [Table: Pivot](/de/reference/workflow-steps/tables/table-pivot/) konvertiert. Einige Kombinationen von Einstellungen liefern Ergebnisse, die von KNIME abweichen.
- **Loop End (Column Append).** Wird zu [Tabelle: Inner Join](/de/reference/workflow-steps/tables/table-inner-join/) konvertiert. Einige Kombinationen von Einstellungen liefern Ergebnisse, die von KNIME abweichen.
- **Zufallsziehungen.** Row Sampler, Table Partitioner und Equal Size Sampling führen KNIMEs eigene Zufallsziehung mit [Table: KNIME Random Sample](/de/reference/workflow-steps/tables/table-knime-random-sample/) aus, sodass ein Knoten mit einem Seed dieselben Zeilen auswählt wie in KNIME. Die Ziehung akzeptiert eine Tabelle mit höchstens 10.000.000 Zeilen; bei einer größeren Tabelle schlägt der Schritt fehl.

## Verwandte Anleitungen

- [KNIME-Konvertierungsmatrix](/de/reference/knime-conversion-matrix/)
- [REST-Verbindung](/de/reference/connectors/rest/generic-rest/)
- [Dokumentenkonten hinzufügen](/de/guides/documents/adding-accounts/)
- [Workflow-Variablen verwalten](/de/guides/workflows/manage-workflow-variables/)
- [Einen Workflow ausführen](/de/guides/workflows/run-a-workflow/)
