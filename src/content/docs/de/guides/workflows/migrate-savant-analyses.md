---
title: Savant-Analysen migrieren
description: Konvertieren Sie einen Savant-Labs-Analyseexport über die Analyze-App, die REST-API oder einen MCP-verbundenen KI-Agenten in einen erweiterten PlaidCloud-Workflow, binden Sie dessen Quellen und lesen Sie den Konvertierungsbericht.
sidebar:
  order: 31
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-savant-analyses.md
---

PlaidCloud ist ein vollwertiger Ersatz für Savant. Jeder Savant-Agent, jeder Ausdruck und jede Einstellung wird in PlaidCloud konvertiert und läuft dort. Der Konverter wandelt einen Savant-Labs-Analyseexport in einen lauffähigen erweiterten Workflow um: Er ordnet jeden Savant-Agenten einem Workflow-Schritt, einer Projektvariable oder einem Arbeitsflächenobjekt zu, behält den ursprünglichen Graphen bei und liefert einen Konvertierungsbericht, der alles benennt, was er nicht konvertieren konnte.

Die Konvertierung liest die Exportdatei, auf die Sie verweisen, und die Kopfzeilen der Dateien, die Sie an ihre Quellen binden. Sie nimmt nie Kontakt zu dem System auf, mit dem eine Savant-Quelle oder ein Savant-Ziel verbunden ist.

## Was PlaidCloud erstellt

- Jeder Savant-Agent wird zum passenden Workflow-Schritt, wobei die Beziehungen zu vor- und nachgelagerten Schritten erhalten bleiben. Die [Savant-Konvertierungsmatrix](/de/reference/savant-conversion-matrix/) führt jeden Agenten und seine Zuordnungsstufe auf.
- Savant-Analyseparameter werden zu Projektvariablen, und Verweise darauf in den Agenteneinstellungen werden in die PlaidCloud-Variablensyntax umgeschrieben.
- Notizen und Gruppen erscheinen auf der Arbeitsfläche als Notizen und Gruppen.
- Jede Quelle wird zu einem Import-Schritt oder liest eine vorhandene Tabelle – je nachdem, wie Sie sie binden.
- Jeder Savant-Agententyp wird vollständig konvertiert: Jede Option hat eine Zuordnung. Eine Konfiguration, an der Savant selbst scheitert oder die es nicht dokumentiert, erscheint als benannter Platzhalter-Schritt. Siehe [Platzhalter für nicht konvertierte Konfigurationen](#platzhalter-für-nicht-konvertierte-konfigurationen).

## Vorbereitung

1. Exportieren Sie die Analyse aus Savant mit **JSON exportieren**.
2. Laden Sie die `.json`-Datei in ein [Dokumentenkonto](/de/guides/documents/adding-accounts/) hoch, auf das Sie lesend zugreifen können.
3. Wählen Sie das PlaidCloud-Projekt aus, das den Workflow erhalten soll. Sie benötigen Schreibzugriff darauf.
4. Wählen Sie ein Dokumentenkonto und einen Basisordner, aus denen die Quelldateien der Analyse gelesen werden.

## Eine Analyse konvertieren

Konvertieren Sie über die Analyze-App, die REST-API oder den MCP-Werkzeugkatalog. Alle drei nehmen dieselben Felder entgegen.

### Analyze-App

1. Öffnen Sie **Analysieren** und wählen Sie **Tools → Savant-Analyse importieren**.
2. Wählen Sie das **Zielprojekt** und die **Savant-Exportdatei (.json)**, die Sie in ein Dokumentenkonto hochgeladen haben.
3. Wählen Sie **Quellen laden**. Das Fenster listet jeden Quellknoten im Export auf.
4. Um eine Quelle mit Daten zu verbinden, die Sie bereits haben, wählen Sie sie aus und klicken Sie auf **Binden…**. Wählen Sie **Projekttabelle**, um eine Tabelle im Zielprojekt zu lesen, oder **Dokument**, um eine Datei aus einem Dokumentenkonto zu lesen (bei Excel mit optionalem Arbeitsblattnamen). Wählen Sie **Bindung aufheben**, um eine Bindung zu entfernen.
5. Wählen Sie unter **Verzeichnis für ungebundene Quellen** das Dokumentenkonto und den Basisordner, aus denen die Dateien für ungebundene Quellen gelesen werden.
6. Wählen Sie unter **Konvertierungsoptionen** den **Workflow-Typ** und ob **Nicht konvertierte Platzhalter zulassen** gelten soll. Legen Sie unter **Objektpräfixe** optional Präfixe für Workflows, Schritte und Tabellen fest.
7. Wählen Sie **Konvertieren**.

Nach Abschluss der Konvertierung zeigt das Fenster den Konvertierungsbericht: den Workflow-Namen und das Tabellenpräfix, die Warnungen, eine Tabelle mit den Dokumentpfaden, in die Sie Dateien für ungebundene Quellen hochladen, und die Schritte, die geprüft werden müssen. Wenn sich die Liste der Quellen nicht laden lässt, fügen Sie für jede Quelle eine Zeile mit ihrer Knoten-ID und der `analyzetable_`-ID der zu bindenden Tabelle hinzu.

### Felder

Die REST-API und das MCP-Werkzeug nehmen diese Felder entgegen.

| Feld | Erforderlich | Funktion |
| --- | --- | --- |
| `source_account_id` | Ja | Dokumentenkonto, das den Savant-Export enthält. |
| `source_file_path` | Ja | Pfad des Exports innerhalb dieses Kontos. |
| `project_id` | Ja | Projekt, in dem der Workflow erstellt wird. |
| `document_account_id` | Ja | Dokumentenkonto, aus dem ungebundene Quellen lesen. |
| `document_account_path` | Ja | Basisordner in diesem Konto für ungebundene Quellen. Ein leerer Wert oder `/` steht für das Stammverzeichnis des Kontos, ein führendes `/` wird ignoriert. Pfade mit `..` oder mit Punkt beginnenden Segmenten, geschweiften Klammern, einem Laufwerksbuchstaben oder URL-Schema sowie Steuerzeichen werden abgelehnt. |
| `workflow_prefix` | Nein | Präfix, das den Workflow-Namen hinzugefügt wird. |
| `step_prefix` | Nein | Präfix, das den Schrittnamen hinzugefügt wird. |
| `table_prefix` | Nein | Präfix, das den Tabellennamen hinzugefügt wird. Standardmäßig der eigene Name des Workflows. Ein Präfix, das einen vorhandenen Tabellennamen wiederverwenden würde, wird abgelehnt, bevor etwas erstellt wird. Das verwendete Präfix wird im Konvertierungsbericht zurückgegeben. |
| `workflow_type` | Nein | `advanced` (Standard) legt den Graphen auf die DAG-Arbeitsfläche. `standard` erzeugt eine serielle Schrittliste. |
| `source_bindings` | Nein | Bindet Quellen an vorhandene Daten. Siehe [Quellen binden](#quellen-binden). |
| `destination_bindings` | Nein | Leitet Ziele an ein Dokumentenkonto, eine Verbindungstabelle, ein Google Sheet, eine Tableau-Datenquelle, einen Slack-Kanal oder E-Mail-Empfänger. Nur REST und MCP. Siehe [Ziele](#ziele). |
| `api_bindings` | Nein | Legt fest, wohin die relative URL eines API-Agenten geht: eine Basis-URL oder eine REST-Verbindung. Nur REST und MCP. Siehe [API-Anfragen binden](#api-anfragen-binden). |
| `allow_unconverted_placeholders` | Nein | Steuert, was ein Platzhalter zur Laufzeit tut. Siehe [Platzhalter für nicht konvertierte Konfigurationen](#platzhalter-für-nicht-konvertierte-konfigurationen). |

### REST

Senden Sie die Felder als JSON-Body an:

```text
POST /rest/v1/analyze/savant/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/savant/quarterly-margin.json",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/savant-inputs"
}
```

Um die Quellknoten eines Exports aufzulisten, bevor Sie `source_bindings` aufbauen, senden Sie `source_account_id` und `source_file_path` an:

```text
POST /rest/v1/analyze/savant/sources
```

Jeder Eintrag in der Antwort enthält `node_id`, `name` und `connector` der Quelle.

### MCP

Ein MCP-verbundener KI-Agent ruft das Werkzeug `savant_convert` mit denselben Feldern auf. Wie Sie einen Agenten verbinden, lesen Sie unter [KI-Agenten (MCP)](/de/integrations/ai-coding-agents/). Das Werkzeug ändert Ihr Projekt, prüfen Sie den Aufruf daher, bevor Sie ihn genehmigen.

## Bindungen zur Konvertierungszeit

Ein Savant-Export enthält keine Daten, keine Zugangsdaten und keine Verbindungen, daher verbinden drei Parameter zur Konvertierungszeit ihn mit Ihren. Jeder ist eine Zuordnung von einer Savant-Knoten-ID oder einem Namen zu einem Ziel, und eine Bindung, die Sie nicht verwenden können, lässt die gesamte Konvertierung scheitern, bevor etwas erstellt wird.

| Parameter | Bindet | Abschnitt |
| --- | --- | --- |
| `source_bindings` | Quell-Agenten an Tabellen oder Dateien | [Quellen binden](#quellen-binden) |
| `destination_bindings` | Ziel-Agenten an eine Datei, Tabelle, ein Sheet, eine Tableau-Datenquelle, einen Slack-Kanal oder E-Mail | [Ziele](#ziele) |
| `api_bindings` | API-Agenten mit relativer URL an eine Basis-URL oder REST-Verbindung | [API-Anfragen binden](#api-anfragen-binden) |

## Quellen binden

Ein Savant-Export beschreibt, woher seine Daten stammen, enthält aber weder Daten noch Zugangsdaten. Verwenden Sie `source_bindings`, um jede Quelle mit Daten zu verbinden, die Sie bereits in PlaidCloud haben. Ein Schlüssel ist die Knoten-ID, die Dataset-ID oder der Name der Quelle. Ein Wert ist entweder:

- Eine `analyzetable_`-ID für eine Tabelle im Zielprojekt. Der konvertierte Workflow liest diese Tabelle direkt.
- Ein Objekt mit `account`, `path` und optional `sheet`, um eine Datei aus einem Dokumentenkonto zu lesen.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "Budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

Eine Bindung, die Sie nicht lesen können, wird abgelehnt. Ein Schlüssel, der zu keiner Quelle passt, wird als Warnung gemeldet.

Ein Quelldateipfad im Export kann mit `/` beginnen oder durch Punktordner wie `.archive` führen, und er wird konvertiert. Eine Quelle, die XML liest, konvertiert den XML-Text, und eine XML-Dokumentquelle enthält außerdem die Dateikontext-Spalten von Savant.

### Ungebundene Quellen

Eine Quelle ohne Bindung wird zu einem Import-Schritt ohne Daten, und der Konvertierungsbericht enthält dazu eine Warnung. Der Schritt liest aus:

```text
<document_account_path>/savant/<workflow id>/<source name>.csv
```

Laden Sie die Datei in diesen Pfad hoch und führen Sie den Workflow aus. Solange die Datei nicht vorhanden ist, endet der Import-Schritt mit einer Warnung und erstellt eine leere Tabelle, und der Workflow läuft weiter.

## So werden Agenten konvertiert

Die meisten Agenten werden in den Schritt konvertiert, den Sie von Hand aufbauen würden; die [Savant-Konvertierungsmatrix](/de/reference/savant-conversion-matrix/) führt jeden Agenten auf. Diese Agenten erfordern besondere Sorgfalt.

| Savant-Agent | Wozu er wird | Einschränkungen |
| --- | --- | --- |
| Infer Agent (`gen_ai` und das ältere `service` mit einem LLM-Dienst) | Ein [AI/NLP](/de/reference/workflow-steps/text-documents/nlp-ai/)-Schritt mit der Aufgabe **Prompt**. Der Prompt läuft einmal je Zeile über die Eingabefelder, und die Antwort landet in einer Spalte **AI Answer** neben jeder Eingabespalte. Ein Zeilenlimit wird zu **Max. Zeilen**, und eine leere Quelle warnt und schreibt eine leere Tabelle. **Max New Rows** beantwortet nur die Zeilen, die neu sind, und behält die Antworten früherer Ausführungen. | Ein LLM antwortet, daher ist die Ausgabe nie byteidentisch mit der von Savant und kann zwischen Ausführungen variieren. Jeder Aufruf verursacht Kosten. Siehe [KI-Anbieter](#ki-anbieter). Ein Batch, der fehlschlägt, behält seine Zeilen mit einer leeren Antwort und warnt. |
| Vision Agent (`vision`) | Ein [Document Read Blob](/de/reference/workflow-steps/text-documents/document-blob-extract/)-Schritt, [Image OCR](/de/reference/workflow-steps/text-documents/image-ocr/), dann die AI/NLP-Aufgabe **Prompt**. Jedes Dokument geht als Bild oder PDF an den Anbieter, wenn der Anbieter diesen Typ und diese Größe akzeptiert. Andernfalls sendet der Schritt die Textebene seines PDFs oder den OCR-Text. | Dieselben LLM-Einschränkungen wie beim Infer Agent. Ganze Dokumente verlassen PlaidCloud in Richtung des Anbieters, und die Konvertierung warnt. TIFF- und BMP-Dateien werden als OCR-Text gesendet, und es gibt keine Einstellung für eine maximale Dokumentgröße. Ein nicht gefundenes Dokument wird übersprungen, und der Schritt warnt mit seinem Pfad. |
| API Agent (`apiService` und das ältere `service` mit einem API-Dienst) | Ein [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/)-Schritt, der je Eingabezeile eine Anfrage sendet, dann ein Join zurück, der jede Eingabezeile behält. Der rohe Antwort-Body landet in einer Textspalte, daneben eine Statusspalte. Ein Kontingent pro Zeitraum wird zu einem gebrochenen **Max. Anfr./Sek.**. Eine relative URL wird an die Basis-URL oder REST-Verbindung angehängt, die Sie mit `api_bindings` binden. Ein Host, Port oder Pfad aus einem Zeilenfeld wird pro Zeile eingesetzt. Paging über Next-URL, Link-Header, Offset und Seite wird verfolgt, und ein Paging-Wert (Start, Seitengröße oder Parametername) kann aus einem Eingabefeld oder einem Parameter stammen. | Eine andere Methode als GET läuft bei jeder Ausführung des Workflows einmal je Eingabezeile gegen das Live-System, bestätigen Sie daher das Ziel vor der ersten Ausführung. Anfragen, die nicht GET sind, werden nicht automatisch wiederholt. Eine fehlgeschlagene Anfrage bleibt als Zeile mit ihrem Status erhalten. Eine Anfrage, die Zugangsdaten trägt, kann ihren Host nicht aus einem Zeilenfeld beziehen. Zugangsdaten werden wie unter [API-Schritte mit Zugangsdaten](#api-schritte-mit-zugangsdaten) beschrieben behandelt. |
| Recursion Agent (`hierarchy`) | Ein [Hierarchy Closure](/de/reference/workflow-steps/tables/table-hierarchy-closure/)-Schritt, der jede Zeile über ihre Eltern-Kette bis in beliebige Tiefe nach oben durchläuft und dann jeden Knoten über die IDs auf seinem Pfad zur Wurzel aggregiert, ihn selbst eingeschlossen. Er schreibt Depth und Path. Eine Zeile mit leerem Elternwert oder mit sich selbst als Elternwert ist eine Wurzel. | Eine Schleife in den Eltern-IDs endet am wiederholten Knoten und behält jeden Vorfahren davor. Zeilen mit mehreren Eltern behalten jeweils ihre eigenen Werte. |
| Search and Replace (`search_replace`) | Ein [Table Extract](/de/reference/workflow-steps/tables/table-extract/), der jede Regel der Reihe nach auf die gewählten Textspalten anwendet, mit oder ohne Beachtung der Groß-/Kleinschreibung, als ganzes Wort oder nicht. Jede Regel läuft in ihrem Modus: den passenden Text ersetzen, die ganze Zelle ersetzen, wenn sie den Text enthält, die ganze Zelle ersetzen, wenn sie genau übereinstimmt, oder an die Zelle anhängen. | Regeln sind Literaltext, keine Muster. |
| Split (`split`) | Ein [Split Text](/de/reference/workflow-steps/tables/table-split-text/)-Schritt. Er teilt an einem literalen Trennzeichen beliebiger Länge in Spalten oder Zeilen auf und bestimmt die Anzahl der Spalten aus den Daten, wenn der Workflow läuft. | Keine. |
| Time Series (`rollup`) | Ein Table Extract, der nach einem Zeitraumausdruck gruppiert, mit einem [Period Spine](/de/reference/workflow-steps/tables/table-period-spine/), einem Anti Join und einer Union, die die Zeiträume ohne Datensätze mit Nullen auffüllen. | Datensätze mit NULL-Datum werden ausgeschlossen. Der Spine endet bei 100.000 Zeiträumen. |
| Format (`format`) | Ein Table Extract mit den Umbenennungen, Typänderungen, Ausblendungen und Füllungen oder ein [Promote Header](/de/reference/workflow-steps/tables/table-promote-header/)-Schritt für „Namen durch Zeile ersetzen". | Eine Füllung einer Spalte, die kein Text ist, wandelt den Standardwert in den Typ der Spalte um. Das Hochstufen einer Kopfzeile über einer Quelle, die keine Spalten deklariert, liest jede Spalte aus CSV-, Excel-, XLS-, JSON-, Parquet- und Avro-Dateien. Siehe [Dateien ohne deklarierte Spalten](#dateien-ohne-deklarierte-spalten). |
| Spatial Match Agent (`spatial_match`) | Ein [Räumlicher Abgleich (Executor)](/de/reference/workflow-steps/spatial/spatial-match-executor/)-Schritt für intersects, within, contains, touches, crosses, overlaps, equals und disjoint, auch mit mehreren kombinierten Regeln; Cross Join für einen Kreuzabgleich; [Nächstgelegene finden](/de/reference/workflow-steps/spatial/spatial-find-nearest/) für einen Nächster-Nachbar-Abgleich. | Ein Nächster-Nachbar-Abgleich sortiert und filtert nach Großkreisentfernung, wie es Savant tut. Eine Nächster-Nachbar-Regel in Kombination mit anderen Regeln findet zuerst die nächstgelegenen Datensätze und wendet dann die anderen Regeln an: Mit AND behält das Ergebnis Datensätze, die jede Regel erfüllen, mit OR vereinigt es die nächstgelegenen Datensätze mit den Datensätzen, auf die die anderen Regeln passen. Eine Nächster-Nachbar-Regel ohne Anzahl und ohne maximale Entfernung behält den einen nächstgelegenen Datensatz. Ein Within-Distance-Abgleich wird ebenfalls konvertiert, in Kilometern, wenn die Regel keine Einheit angibt, und misst die geodätische Entfernung zwischen beliebigen Geometrien, nicht nur Punkten. Eine Geometrie, die sich nicht parsen lässt, ergibt NULL oder keine Übereinstimmung, mit einer Warnung. |
| Spatial Summarize Agent (`spatial_summarize`) | [Räumlich kombinieren](/de/reference/workflow-steps/spatial/spatial-combine/) für Vereinigung, Schnittmenge und Begrenzungsrahmen sowie [Spatial Centroid](/de/reference/workflow-steps/spatial/spatial-centroid/), [Spatial Point to Line](/de/reference/workflow-steps/spatial/spatial-point-to-line/) und [Spatial Line to Polygon](/de/reference/workflow-steps/spatial/spatial-line-to-polygon/) für den geometrischen Mittelpunkt und das Bilden von Linien oder Polygonen. | Ein Polygon aus weniger als 3 Punkten ist ein leeres Polygon. |
| Destination Agent (`destination`) | Ein Export-Schritt zu dem Ziel, das Sie binden, oder, wenn Sie keines binden, eine Projekttabelle oder Datei. Siehe [Ziele](#ziele). | Siehe [Was eingeschränkt bleibt](#what-stays-limited). |

`GEO_POINT`, `GEO_TYPE` und `GEO_SPATIAL_DISTANCE` werden in Ausdrücke konvertiert. Eine Bearbeitung, deren gesamter Ausdruck eine andere `GEO_*`-Funktion ist, etwa `GEO_AREA` oder `GEO_UNION`, wird in den passenden räumlichen Schritt konvertiert, einschließlich [Spatial Info](/de/reference/workflow-steps/spatial/spatial-info/). Geometrie wird als WKT-Text übertragen. `GEO_AREA`, `GEO_PERIMETER` und `GEO_SPATIAL_DISTANCE` in Meilen verwenden die Statute Mile.

Eine Quelle, die Binärdateien liest, etwa die Dokumente, die ein Vision-Agent liest, wird in eine Dokumentextraktion des gebundenen Dokuments oder der Datei konvertiert, die am Pfad für ungebundene Quellen erwartet wird.

## KI-Anbieter

Ein Infer- oder Vision-Agent wird in einen AI/NLP-Schritt konvertiert, der eine LLM-Verbindung verwendet. Der Konverter unterstützt Anthropic, OpenAI, Gemini, Azure OpenAI, Grok und GitHub Models.

- Der Konverter wählt die Verbindung für den Anbieter und das Modell, die der Agent nennt, aus den LLM-Verbindungen, die der importierende Benutzer sehen kann. Er nennt nie eine, die der Benutzer nicht sehen kann. Über einen KI-Assistenten (MCP) bedeutet das die Verbindungen, die der Benutzer des Assistenten sehen kann.
- Wenn für den Anbieter keine sichtbare Verbindung existiert oder der Anbieter von Savant keine Entsprechung in PlaidCloud hat (eine in der Cloud gehostete Modell-API oder ein Bring-your-own-key-Anbieter des Savant-Workspace), verwendet der Schritt die Standardverbindung des Workspace, sofern der Benutzer sie sehen kann. Andernfalls lässt er die Verbindung leer, und der Schritt verwendet bei der Ausführung die Standardverbindung des Workspace. Der Konvertierungsbericht warnt in beiden Fällen; wählen Sie daher im Schritt eine Verbindung, wenn eine andere antworten soll.

## Ziele

Ein Savant-Ziel schreibt die empfangene Tabelle in das Ziel, das Sie binden. Binden Sie Ziele mit `destination_bindings` im REST-Body oder MCP-Aufruf. Ein Schlüssel ist die Knoten-ID oder der Name des Ziels. Das Analyze-Fenster bindet keine Ziele, daher schreibt ein dort konvertiertes Ziel das ungebundene Ergebnis, das unter [Ungebundene Ziele](#ungebundene-ziele) beschrieben ist.

| Ziel | Bindung | Ergebnis |
| --- | --- | --- |
| Dokumentenkonto | `{account, path[, file_name]}` | Je nach Art des Ziels eine CSV-, TSV-, TXT-, Excel-, Parquet-, JSON-, Avro-, XML-, PDF- oder Tableau-Hyper-Datei. Sie benötigen die Schreibberechtigung für den Dokumentspeicher des Kontos. |
| Tabelle in einer Verbindung | `{connection, table[, schema, replace]}` | Ein [Export: External Database Tables](/de/reference/workflow-steps/export/export-external-tables/)-Schritt. Sie benötigen die Schreibberechtigung für die Verbindung. Das Ersetzen der Tabelle erfordert `replace: true`. |
| Google Sheets | `{connection, spreadsheet_name[, sheet_name, replace]}` oder `{connection, spreadsheet_id[, sheet_name, replace]}` | Ein [Export to Google Spreadsheet](/de/reference/workflow-steps/export/export-to-google-spreadsheet/)-Schritt über eine Google-Sheets-Verbindung. Die Registerkarte ist standardmäßig die, die das Ziel benennt, sonst `Sheet1`. Ein Ziel, das die Zeilen des Sheets ersetzt, leert die Registerkarte und erfordert daher `replace: true`. |
| Tableau | `{account, connection[, path, file_name, replace, datasource_name, tableau_project]}` | Ein Tableau-Hyper-Extrakt, der in den Ordner des Kontos geschrieben wird, dann ein [Publish to Tableau](/de/reference/workflow-steps/export/export-to-tableau/)-Schritt über eine [Tableau-Verbindung](/de/reference/connectors/collaboration/tableau/). Das Ersetzen der Datenquelle oder das Ändern ihrer Zeilen anhand von Abgleichsschlüsseln erfordert `replace: true`. |
| Slack | `{connection[, channel]}` | Die CSV wird in ein Dokumentenkonto geschrieben, dann lädt ein [Notify via Slack](/de/reference/workflow-steps/notifications/notify-via-slack/)-Schritt sie in den Kanal hoch. Die Verbindung benötigt ein Bot-Token, und der Kanal muss eine Kanal-ID sein, entnommen aus der Bindung oder andernfalls aus dem Export. |
| E-Mail | `{email_to: [...]}` und `email_export_recipients: true`, um zusätzlich die im Export aufgeführten Empfänger zu verwenden | Die CSV wird als Anhang per E-Mail verschickt. Sie benötigen die Schreibberechtigung für E-Mail. |

Eine Sheets-, Tableau- oder Slack-Verbindung wird so geprüft wie eine Tabellenverbindung: Sie müssen sie sehen können und die Schreibberechtigung für die Verbindung besitzen, sonst wird die Konvertierung abgelehnt.

### Schreibmodi

- Ein Datei- oder Tabellenziel, das anhängt, liest die frühere Datei zurück und schreibt sie mit den neuen Zeilen neu. Es überschreibt nie.
- Ein Ziel mit Upsert, Update oder groupReplace führt einen Merge über die Abgleichsschlüssel des Ziels aus. Eine Datei oder Tabelle wird zurückgelesen und neu geschrieben, und bei einer Tableau-Datenquelle werden die passenden Zeilen an Ort und Stelle geändert.
- Anhängen und Merge funktionieren auch bei vorhandenen Dateien, die pro Wert aufgeteilt sind, bei Dateien ohne Kopfzeile (Zeilen werden nach Position abgeglichen), bei Excel-Dateien, die an einer Zelle oben links verankert sind, und bei Dateien in einem Nicht-UTF-8-Zeichensatz. Eine Aufteilung liest die Datei zurück, in die jeder Wert geschrieben wird, und führt den Merge darin aus; die anderen Dateien bleiben unverändert.
- Ein Tableau-Ziel ordnet die Modi von Savant den sechs Modi von [Publish to Tableau](/de/reference/workflow-steps/export/export-to-tableau/#modi) zu: Anhängen und Einfügen fügen Zeilen hinzu, Ersetzen überschreibt, und Upsert, Update und groupReplace gleichen über Schlüssel ab. Ein Modus, der vorhandene Daten ändert, veröffentlicht nur, wenn die Bindung `replace: true` angibt; andernfalls veröffentlicht das Ziel eine neue Datenquelle, und der Bericht weist darauf hin.
- Ein Ziel mit Ausgabekodierung schreibt die Datei in diesem Java-Zeichensatz. Ein Zeichen, das dem Zeichensatz fehlt, wird als `?` geschrieben, wie es Savant tut. Java-Aliasse, CESU-8 und Formen mit Byte-Order-Mark werden akzeptiert. Einige seltene Zeichensätze (zum Beispiel `x-ISCII91` oder `JIS_X0212`) lassen sich nicht schreiben; die Datei wird als UTF-8 geschrieben, und der Bericht warnt. Eine Aufteilung in einem Nicht-UTF-8-Zeichensatz konvertiert den Ordner.
- Exportdateinamen müssen innerhalb des gebundenen Ordners bleiben.

### Was KI-Aufrufer binden können

Eine Konvertierung über einen KI-Assistenten (MCP) bindet dieselben Formen, wobei diese Teile zurückgehalten werden, jeweils mit einer Warnung, die den Teil nennt:

| Zurückgehalten | Was stattdessen geschieht |
| --- | --- |
| `replace` bei einer Tabelle, einem Sheet oder einer Tableau-Datenquelle | Ein Ziel, das anhängt, hängt weiterhin an seine gebundene Tabelle oder sein gebundenes Sheet an. Ein Ziel, das ersetzt, schreibt eine CSV. Ein Tableau-Ziel veröffentlicht eine neue Datenquelle. |
| E-Mail-Empfänger | Anstelle der E-Mail wird eine CSV geschrieben. |
| Slack | Anstelle des Slack-Beitrags wird eine CSV geschrieben. |

Konvertieren Sie über die Analyze-App oder die REST-API, oder melden Sie sich selbst an statt über einen Assistenten, um diese zu binden.

### Ungebundene Ziele

Ein Ziel ohne Bindung schreibt sein PlaidCloud-Gegenstück und warnt mit **Destination target unbound** unter Nennung des ursprünglichen Ziels. Die Konvertierung nimmt nie Kontakt zum Zielsystem auf.

| Ziel | Ergebnis |
| --- | --- |
| Datenbank-, Warehouse- oder SaaS-Ziel (Oracle, generische Datenbank, Looker Studio, NetSuite, SAP sowie Google Sheets, Tableau oder Slack ohne gebundene Verbindung) | Eine Tabelle im Projekt, benannt nach dem Zielknoten. |
| Dateispeicher (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | Die Datei im Dateityp des Ziels in einem Dokumentordner unter dem Konto, das Sie für ungebundene Quellen angegeben haben. Der Ordner spiegelt den Zielordner. Zugangsdaten und Freigabe-Tokens werden aus dem Pfad entfernt. |
| E-Mail | Eine CSV im Dokumentenkonto, das Sie für ungebundene Quellen angegeben haben. |

Die Warnung nennt, was Sie binden müssen, um das eigentliche Ziel zu erreichen. Ein Ziel, dessen Bindung nicht verwendet werden kann, schreibt eine CSV und warnt mit **Fallback, target not written**, wobei das ursprüngliche Ziel in der Meldung steht; prüfen Sie diese CSV, bevor Sie sich darauf verlassen. Ein einfaches CSV-Ziel schreibt seine eigene Datei.

### Aufgeteilte Ziele

Ein Ziel, das pro Wert eines Felds eine Datei, einen Unterordner oder eine Registerkarte schreibt, teilt CSV-, Excel-, Parquet- und PDF-Dateien sowie Google-Sheets-Registerkarten auf.

- **Parquet und PDF.** Eine Datei pro Wert.
- **Google Sheets.** Eine Registerkarte pro Wert.
- **Vorlage.** Eine Vorlagen-Arbeitsmappe dient als Ausgangspunkt der Arbeitsmappe für jeden Wert. Eine fehlende Vorlage warnt, und die Arbeitsmappe wird ohne sie geschrieben.
- **NULL-Werte.** Ein NULL-Aufteilungswert wird in eine eigene Datei oder Registerkarte geschrieben, nicht verworfen.
- **Ein Feld, das der Eingabe fehlt.** Eine Aufteilung oder Sortierung nach einem Feld, das die Eingabe nicht enthält, wird namentlich abgelehnt, weil Savant daran scheitert.
- **Ein `/` oder `\` in einem Wert.** Ein Aufteilungswert mit Schrägstrich oder Backslash kann kein Datei- oder Registerkartenname sein und wird daher bereinigt. Ein geänderter Wert erhält ein festes Suffix aus sechs Zeichen: `-` gefolgt von den ersten sechs Zeichen des MD5-Hashs des Werts, vor der Dateierweiterung. Werte, die keine Änderung brauchen, behalten ihren Namen.

### Exportierte Werte und Zeilenreihenfolge

- **Einfache Zahlen und boolesche Werte.** CSV-, TSV- und TXT-Exporte schreiben Zahlen als einfache Zahlen und boolesche Werte als `true` und `false`, ohne `+00:00` bei Zeitstempeln.
- **Stabile Zeilenreihenfolge.** Ein Ziel, das sortiert, schreibt bei jeder Ausführung dieselbe Zeilenreihenfolge: Gleichstände werden jedes Mal gleich aufgelöst, und auch Aufteilungs- und Teilrouten werden sortiert. Parquet-, Google-Sheets-, Tableau- und Tabellenziele behalten keine Zeilenreihenfolge.

### Excel-Optionen

Ein Excel-Ziel bildet diese Optionen ab:

- **Registerkarte pro Feldwert.** Jeder Wert des Felds wird zu einem Blatt. Leere Werte gehen nach `Sheet1`, und Blätter mit kollidierenden Namen erhalten ein numerisches Suffix.
- **Format aus Vorlage.** Jede Ausführung kopiert zuerst `<name>_template.xlsx` aus demselben Ordner über die Arbeitsmappe und schreibt dann hinein, sodass die Arbeitsmappe immer ersetzt wird. Ist die Vorlage nicht vorhanden, warnt das Kopieren, und die Arbeitsmappe wird ohne sie geschrieben.
- **Zelle oben links.** Die Zeilen werden ab dieser Zelle in die Arbeitsmappe geschrieben.
- **Modus `create`.** Jede Ausführung schreibt die Datei so, wie der Schreibmodus des Ziels es vorgibt.

## API-Anfragen binden

Ein API-Agent mit relativer URL, etwa `/v2/customers`, hat keinen Host, an den er senden kann. Binden Sie einen mit `api_bindings`. Ein Schlüssel ist die ID oder der Name des API-Knotens oder `*` für jeden API-Knoten ohne eigene Bindung. Ein Wert ist einer der folgenden:

- Eine Basis-URL, als Zeichenfolge oder `{"base_url": "https://host/path"}`. Die relative URL wird daran angehängt. Die URL muss `http` oder `https` mit einem öffentlichen Host sein und darf keinen Benutzer, keine Abfrage und kein Fragment enthalten.
- `{"connection": "<REST connection id>"}`. Die Anfrage geht an den Host dieser [REST-Verbindung](/de/reference/connectors/rest/generic-rest/) und trägt deren Zugangsdaten. Sie benötigen die Schreibberechtigung für die Verbindung, und die Verbindung muss eine REST-Verbindung sein, die Sie sehen können.

```json
"api_bindings": {
  "*": "https://api.example.com/v1",
  "Customers": { "connection": "<REST connection id>" }
}
```

Ein nicht passender Schlüssel ist eine Warnung, und eine Bindung, die Sie nicht verwenden können, wird abgelehnt. Eine relative URL ohne Bindung bleibt ein benannter Platzhalter.

Bei einem KI-Assistenten (MCP) ohne Schreibberechtigung für die Verbindung wird eine Verbindungsbindung mit einer Warnung ignoriert, und die relative URL, die er angehängt hätte, bleibt ein Platzhalter. Binden Sie eine Basis-URL oder konvertieren Sie über die Analyze-App oder die REST-API.

Ein Host, Port oder Pfad aus einem Eingabefeld braucht keine Bindung. Er wird pro Zeile eingesetzt, jeder Wert wird bei der Verwendung geprüft, und der Bericht führt die Hosts auf, die eine Zeile nennen darf. Eine Anfrage, die Zugangsdaten trägt, kann ihren Host nicht aus einem Zeilenfeld beziehen: Das Senden von Zugangsdaten an einen Host, den die Daten wählen, wird abgelehnt.

Auch Paging wird konvertiert. Eine Next-Page-URL in der Antwort, ein `Link`-Header, ein Offset und eine Seitennummer werden jeweils zu einem Paging-Modus des Schritts [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/), der jede Seite liest. Ein Paging-Wert kann aus einem Eingabefeld (`{{Field}}`) oder einem Parameter (`{{Param}}`) stammen, und ein als numerischer Text geschriebener Wert wie `10.0` wird als Zahl gelesen.

## API-Schritte mit Zugangsdaten

Ein Zugangsdatum in den Headern, im URL-Pfad, in der Abfrage oder im Body eines API-Agenten wird in eine PlaidCloud-REST-Verbindung verschoben, die der Import erstellt. Der REST-Anfrage-Schritt verweist auf diese Verbindung, sodass das Zugangsdatum nie im Schritt steht.

- Die Antwort führt unter `connections` die Verbindungen auf, die der Import erstellt oder wiederverwendet hat, und der Importbericht nennt sie. Beim erneuten Import derselben Analyse wird dieselbe Verbindung wiederverwendet, statt eine weitere zu erstellen.
- Zugangsdaten in den Benutzerinformationen der URL und in Headern gehen in die eigenen Authentifizierungsfelder oder Standard-Header der Verbindung. Geheimnisse in Pfad, Abfrage und Body werden verschlüsselt in der Verbindung gespeichert und zur Laufzeit eingesetzt, nur für Anfragen an den eigenen `https`-Host dieser Verbindung.
- Ein unverschlüsselter `http://`-Endpunkt wird nicht mit Zugangsdaten konvertiert. Das Zugangsdatum wird weggelassen, und der Konvertierungsbericht warnt, dass es nicht kopiert wurde.
- Ein Import über einen KI-Assistenten (MCP) erstellt keine Verbindungen. Zugangsdaten werden weggelassen, und eine Warnung weist darauf hin. Importieren Sie stattdessen über die Analyze-App oder die REST-API, oder fügen Sie das Zugangsdatum von Hand zu einer REST-Verbindung hinzu und wählen Sie diese im Schritt aus.
- Ein Benutzer ohne Schreibberechtigung für Verbindungen erhält dasselbe Ergebnis: Zugangsdaten werden weggelassen, und es erscheint eine Warnung.
- Nur ein API-Zugangsdaten-Slot verschiebt einen Parameter in eine Verbindung. Ein Pipeline-Parameter, der in einem Header, einer Abfrage, einem Pfad oder einem Body dort verwendet wird, wo ein API-Zugangsdatum hingehört, geht in die verschlüsselten `secret_values` der Verbindung, und der Schritt verweist über die Verbindung darauf. Er wird nie als Workflow-Variable angelegt, gleich wie der Parameter heißt.
- Jeder andere Parameter, dessen Name ein Geheimnis-Wort enthält (etwa `password`, `token`, `secret` oder `key`, wobei `key` nach einem Datenwort wie `sort` oder `partition` ausgenommen ist), wird zu einer Workflow-Variable mit leerem Wert und einer Warnung. Auch ein Name wie `api_key_2` wird geleert. Setzen Sie den Wert nach dem Import in der Projektvariable.
- Ein Parameter, der nach einer Anzahl oder einem Limit benannt ist, etwa `max_tokens`, behält seinen Wert.
- Ein Geheimnis, das in eine Formel, einen Filter oder einen Ersetzungswert eingegeben wurde, wird aus dem Schritt weggelassen, und der Konvertierungsbericht warnt. Ein Pfad, eine URL und ein Hex-Digest mit 40 oder 64 Zeichen bleiben erhalten, sofern nicht ein Teil davon oder ein Geheimnisname etwas anderes nahelegt. Freigabelinks für Ordner und E-Mail-Adressen von Empfängern erscheinen nie in Warnungen oder Hinweisen.
- Eine Antwort, die ein Zugangsdatum zurückspiegelt, wird so gespeichert, wie sie empfangen wurde. Behandeln Sie die Ausgabetabelle einer solchen Anfrage als vertraulich.

## JWT_ENCODE

`JWT_ENCODE` wird in einen [JWT Encode](/de/reference/workflow-steps/tables/table-jwt-encode/)-Schritt konvertiert. Ein literaler Signaturschlüssel geht in eine eigene Verbindung, die an den Schritt gebunden ist, und das Token wird zur Laufzeit signiert, sodass der Schlüssel nie in der Schrittkonfiguration erscheint. Über einen KI-Assistenten oder ohne Schreibberechtigung für Verbindungen wird der Schlüssel weggelassen, das Token ist NULL, und eine Warnung fordert Sie auf, erneut mit der Berechtigung zum Erstellen von Verbindungen zu importieren.

## Eine Datenzeile zu Spaltenüberschriften hochstufen

Ein Format-Agent mit der Einstellung **Namen durch Zeile ersetzen** wird in einen [Promote Header](/de/reference/workflow-steps/tables/table-promote-header/)-Schritt konvertiert. Zur Laufzeit wird die gewählte Zeile, ab 1 gezählt, zu den Spaltennamen und entfernt. Eine Quelle ohne Datensatzreihenfolge erhält einen Hinweis, weil sich von Ausführung zu Ausführung ändern kann, welche Zeile die Spalten benennt. Eine Spalte, die diese Zeile benennt, die aber kein späterer Schritt erwähnt, wird nicht über einen Schritt hinaus mitgeführt, der die Spalten auflistet, die er liest.

## Dateien ohne deklarierte Spalten

Eine Quelle ohne deklarierte Spalten behält diese Spalten:

- Eine beim Import gebundene CSV-, TSV- oder TXT-Quelle behält jede Spalte aus der Kopfzeile der Datei.
- Jeder andere Dateityp und jede ungebundene Quelle behält nur die Spalten, die spätere Schritte nennen, und der Konvertierungsbericht warnt.
- Eine hochgestufte Kopfzeile über einer solchen Quelle liest jede Spalte aus CSV-, Excel-, XLS-, JSON-, Parquet- und Avro-Dateien.

Wenn eine solche Quelle nur eine hochgestufte Kopfzeile speist, ist der Import ein [Import Delimited](/de/reference/workflow-steps/import/import-delimited/)-Schritt, der jede Spalte nach Position liest. Ein Schritt, der nach einer hochgestuften Kopfzeile exportiert oder verknüpft, führt jede Spalte mit, die die Tabelle zur Laufzeit hat (siehe **Auch zur Laufzeit benannte Spalten übernehmen** in [Table Extract](/de/reference/workflow-steps/tables/table-extract/)).

## Wissenswertes zum Verhalten

Diese Konvertierungen verhalten sich wie folgt.

| Agent | Verhalten |
| --- | --- |
| Blend (`blend`) | Verknüpft über OR-kombinierte Prädikate, contains und is-part-of. Blends vom Typ „äußere ohne innere" und die nicht abgeglichenen Ausgaben werden in die passenden Join-Streams konvertiert. Bei jedem Operator wird der doppelte rechte Schlüssel aus der Ausgabe entfernt. |
| Dedupe (`deduplicate`) | Behält den ersten Datensatz pro Schlüssel innerhalb jeder Gruppe von **Gruppieren nach**. Das Duplikat-Flag markiert jedes Mitglied einer Duplikatgruppe, und Duplikate können zusätzlich in einen zweiten Stream geleitet werden. Mit nur einem angeschlossenen Ausgang verhält er sich wie in Savant. |
| Summarize (`summarize`) | Fensteraggregate fügen jeder Zeile das Aggregat hinzu, statt Gruppen zusammenzufassen. |
| Sample (`sample`) | Die ersten N Zeilen, pro Gruppe oder insgesamt, ein zufälliger Prozentsatz oder eine zufällige Anzahl von Zeilen oder jede N-te Zeile. |
| Time Series (`rollup`) | Zeiträume nach Tag, Woche, Monat, Quartal, Jahr und Jahrzehnt zwischen dem optionalen Start- und Enddatum, pro Gruppe. Monatszeiträume werden als `YYYY-MM` bezeichnet, und Zeiträume ohne Datensätze erscheinen mit Nullen. Datensätze mit NULL-Datum werden ausgeschlossen. |
| Pivot (`pivot`) | COUNT zählt Zeilen. |
| XML (`xml`) | SELECT extrahiert Elemente, Pfade können Namespaces tragen, und TO_JSON konvertiert XML in JSON. Jeder XPath-1.0-Pfad wird konvertiert, einschließlich Prädikaten, Attributtests, Platzhaltern und Funktionen wie `count()`, `name()` und `contains()`, und der Schritt [XML parsen](/de/reference/workflow-steps/tables/table-xml-parse/) liest ihn als XPath. Bei ausgeschaltetem `processNs` werden Namen wörtlich abgeglichen, einschließlich Präfix. Eine XML-Datei, die bei der Konvertierung fehlt, löst ihr Wurzelelement auf, wenn der Workflow läuft. |
| JSON (`json`) | Flacht zu breiten Spalten ab. Text, der kein gültiges JSON ist, ergibt NULL, und Arrays werden als Text ausgegeben. |
| Split (`split`) | Teilt in Spalten oder Zeilen auf, wobei die Anzahl der Spalten bei jeder Ausführung des Workflows aus den Daten gelesen wird. |

Diese Ausdrucksfunktionen folgen den Ergebnissen von Savant:

| Funktion | Verhalten |
| --- | --- |
| `DATE_DIFF` | Wochen und Quartale werden so gezählt wie in Savant. |
| `PAD` | Kürzt einen Wert, der länger als die Zielbreite ist, nicht. |
| `+` bei Text | Verkettet Text. Eine Spalte aus einer Quelle ohne deklarierte Typen wird als Zahl gelesen, sodass `+` addiert, und ein Hinweis weist darauf hin. |
| Aufteilen in Zeilen | Behält leere Teile als Zeilen. |
| `LAST` ohne Sortierung | Liefert die letzte Zeile in der Reihenfolge, in der die Zeilen eintreffen, mit einem Hinweis, dass das Warehouse diese Reihenfolge nicht garantiert. |
| `JOIN_STR` | Verbindet eine Bruchzahl so, wie Savant sie schreibt, ohne Auffüllen mit nachgestellten Nullen. |
| `JSON_FORMAT` | Gibt das JSON formatiert aus; in Snowflake schreibt es das JSON kompakt in einer Zeile. |
| `JSON_SET` | Behält die Schlüsselreihenfolge von Savant. |
| `GREATEST` und `LEAST` | Überspringen NULL-Argumente. Das Ergebnis ist nur dann NULL, wenn jedes Argument NULL ist. |
| `ROUNDUP` | Rundet auf den nächsten ganzen Schritt auf, sodass eine negative Zahl zur Null hin rundet: -1,5 wird zu -1. `ROUNDDOWN` bleibt unverändert. |
| `DURING_DAYLIGHT_SAVING` und `DURING_STANDARD` | NULL hinein ergibt NULL heraus. |
| `TO_TEXT` mit einem Datumsformat | Liest die Formatzeichen so wie Savant. `YYYY`, `w` und `u` sind das ISO-Wochenjahr, die ISO-Woche und der ISO-Wochentag, und ein Zonen- oder Era-Buchstabe wird wie für eine UTC-Zeit geschrieben. |
| `TO_TEXT` und Ausgabe von Zahl zu Text | Schreibt einfache Zahlen wie `12`, nicht `12.0000000000`. |
| `TO_TEXT` mit einem numerischen Muster | Formatiert wie ein Java-`DecimalFormat`, rundet dabei zur geraden Zahl (Round-Half-Even), einschließlich wissenschaftlicher Muster wie `##0.##E0`. |
| `TO_TEXT` und Datums-Parsing mit einem Format pro Zeile | Liest das Format aus jeder Zeile. |
| Datumsformatzeichen für Sekundenbruchteile, schmale Monate und Wochenbasis | Werden konvertiert. Die Wochenzeichen werden als ISO-Wochen gelesen. |
| Zweistellige Jahre (`yy`, `y`) | Werden über ein Fenster von 80 Jahren zurück und 20 Jahren voraus ab dem aktuellen Jahr gelesen. |
| `REGEX_MATCH` | Ein Teilabgleich: Das Muster passt irgendwo im Text, nicht auf den ganzen Text. |

`TO_TEXT` und Datumsformate werden in einem [Text Function](/de/reference/workflow-steps/tables/table-text-function/)-Schritt konvertiert. Eine Bearbeitung, die nur ihre kompilierten Schritte ohne Ausdruck enthält, wird als diese Schritte konvertiert, der Reihe nach angewendet, wobei jeder den nächsten speist, und der Konvertierungsbericht vermerkt die angenommene Reihenfolge. Der Konverter lehnt namentlich ab, woran Savant selbst scheitert oder was nichts zu konvertieren hat, und der Schritt wird zu einem Platzhalter: eine einfache Aggregat- oder Fensterfunktion innerhalb eines Transform- oder Filter-Ausdrucks (innerhalb einer Berechnung oder eines Summarize wird sie konvertiert), `HASH` mit einem literalen Algorithmus außer `md5` oder `sha1`, ein regulärer Ausdruck, den PlaidCloud nicht lesen kann (eine Klasse in einer Klasse, eine Klassenschnittmenge oder eine unbekannte `\p{}`-Eigenschaft), eine Transform-Bearbeitung ohne Ausdruck und ohne kompilierte Schritte (etwa eine Copilot-Bearbeitung, die nur ihren Prompt hat), ein XML-Pfad, der kein XPath 1.0 ist, und eine API-Anfrage, die ein Zugangsdatum trägt und ihren Host aus einem Zeilenfeld bezieht. Die [Savant-Konvertierungsmatrix](/de/reference/savant-conversion-matrix/#ausdrücklich-abgelehnte-konstrukte) führt jede mit ihrer Begründung auf.

Ausdrucksfunktionen werden auch für `sha1`, `NOT_TRUE`, `LEVENSHTEIN`, die Sommerzeitfunktionen (`DST`) und reguläre Ausdrucksfunktionen mit einer n-ten Übereinstimmung konvertiert. `DAY_OF_WEEK` nummeriert den Sonntag als 7, und `DAY_NAME` liefert den Namen des Tages.

## Den Konvertierungsbericht lesen

Die Antwort enthält den Konvertierungsbericht: eine Zusammenfassung, wie viele Schritte mit hoher, mittlerer oder niedriger Konfidenz konvertiert wurden und wie viele nicht, dazu Warnungen und die Knoten, die der Konverter in andere aufgenommen hat. Lesen Sie ihn, bevor Sie den Workflow ausführen. Er nennt jeden Platzhalter, jede ungebundene Quelle und jede nicht passende Bindung sowie das verwendete Tabellenpräfix.

## Platzhalter für nicht konvertierte Konfigurationen

Eine Konfiguration, die der Konverter nicht nachbilden kann, wird als Platzhalter-Schritt angelegt, der den Namen des Agenten trägt, und der Konvertierungsbericht nennt ihn. Ein Platzhalter entsteht für ein Konstrukt, das der Konverter namentlich ablehnt (siehe die [Savant-Konvertierungsmatrix](/de/reference/savant-conversion-matrix/#ausdrücklich-abgelehnte-konstrukte)), oder für eines, das der Export nicht vollständig beschreibt, etwa eine fehlende API-Konfiguration. Standardmäßig schlägt ein Platzhalter fehl, sobald der Workflow ihn erreicht, damit eine Ausführung nicht Erfolg für Arbeit melden kann, die nie stattgefunden hat.

Setzen Sie `allow_unconverted_placeholders` auf `true`, um stattdessen jeden Platzhalter als Durchreich-Schritt zu importieren. Die Ausführung läuft dann an ihm vorbei weiter, und die Ausgabe des Platzhalters ist seine Eingabe. Bauen Sie die Funktion mit einem nativen Schritt nach, wenn ihr Ergebnis wichtig ist.

## Den konvertierten Workflow ausführen

1. Öffnen Sie den neuen Workflow im Projekt.
2. Setzen Sie alle Projektvariablen, die aus Savant-Parametern stammen.
3. Laden Sie die Dateien für ungebundene Quellen in die Pfade aus dem Bericht hoch.
4. Führen Sie den Workflow aus und prüfen Sie die Ausgabetabelle jedes Schritts.

## Sonderfälle

Dies sind die einzigen bekannten Unterschiede zu Savant. Der Konvertierungsbericht nennt jeden, der zutrifft.

- **Datumsformate.** `TO_DATE` oder `TO_DATETIME` mit einem Format, das ein Literal `[`, `]`, `'`, `\` oder `^` enthält, bei Text, der zu 9999-12-30 oder 9999-12-31 gelesen wird, liegt jenseits des letzten Zeitstempels, den das Warehouse speichert, und der Bericht warnt.
- **Geheime Parameter.** Ein Parameter, dessen Name ein Geheimnis-Wort enthält oder dessen Wert wie ein Zugangsdatum aussieht, wird absichtlich zu einer Projektvariable mit leerem Wert. Setzen Sie den Wert in der Variable.
- **Nicht deklarierte Parameter.** Ein Parameter, den ein Knoten verwendet, den der Export aber nicht deklariert, kommt als Projektvariable mit leerem Wert an.
- **`JSON_FORMAT` in Snowflake.** Schreibt kompaktes JSON in einer Zeile.
- **Zeilenreihenfolge.** Sortierte Parquet-, Google-Sheets-, Tableau- und Tabellenziele behalten keine Zeilenreihenfolge.
- **Google Sheets und Tableau.** Das Veröffentlichen in eines von beiden erfordert, dass sein Konto über `destination_bindings` gebunden ist.

## Verwandte Leitfäden

- [Savant-Konvertierungsmatrix](/de/reference/savant-conversion-matrix/)
- [REST-Verbindung](/de/reference/connectors/rest/generic-rest/)
- [Dokumentenkonten hinzufügen](/de/guides/documents/adding-accounts/)
- [Workflow-Variablen verwalten](/de/guides/workflows/manage-workflow-variables/)
- [AI/NLP-Schritt](/de/reference/workflow-steps/text-documents/nlp-ai/)
- [REST-Anfrage-Schritt](/de/guides/workflows/rest-request-step/)
- [Einen Workflow ausführen](/de/guides/workflows/run-a-workflow/)
