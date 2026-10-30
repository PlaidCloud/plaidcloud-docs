---
title: Prophecy-Projekte migrieren
description: Konvertieren Sie einen Prophecy-Projektexport über die Analyze-App, die REST-API oder einen MCP-verbundenen KI-Agenten in PlaidCloud-Workflows, binden Sie dessen Datasets und Verbindungen und lesen Sie den Konvertierungsbericht.
sidebar:
  order: 31.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-prophecy-projects.md
---

PlaidCloud ist ein vollwertiger Ersatz für Prophecy. Jedes Prophecy-Gem wird in native PlaidCloud-Workflow-Schritte konvertiert, die die Arbeit des Gems erledigen: Der Konverter erstellt je einen Workflow für jede Spark-Pipeline und einen für das SQL-Projekt, ordnet jedes Gem einem Workflow-Schritt, einer Projektvariable oder einem Arbeitsflächenobjekt zu, behält den ursprünglichen Graphen bei und liefert einen Konvertierungsbericht. Die wenigen Verhaltensweisen, die ein konvertierter Workflow nicht von selbst nachbildet, sind unter [Sonderfälle](#sonderfälle) aufgeführt.

Die Konvertierung liest nur den Export, auf den Sie sie verweisen. Sie nimmt nie Kontakt zu dem System auf, aus dem ein Prophecy-Dataset liest oder in das es schreibt, und sie führt nie Projektcode aus.

Die Konvertierung ist ein einmaliger Vorgang. Wenn Sie dasselbe Projekt erneut konvertieren, entstehen neue Workflows und Tabellen; Änderungen, die Sie in PlaidCloud vorgenommen haben, werden nie mit einem späteren Export zusammengeführt.

## Was PlaidCloud erstellt

- Jedes Prophecy-Gem wird zum passenden Workflow-Schritt, wobei die Beziehungen zu vor- und nachgelagerten Schritten erhalten bleiben.
- Prophecy-Parameter werden zu Projektvariablen, und Verweise darauf in den Gem-Einstellungen werden in die PlaidCloud-Variablensyntax umgeschrieben. Sie können Parameterwerte bei der Konvertierung überschreiben.
- Jedes Dataset, das ein Gem liest, wird zu einem Import-Schritt oder liest eine vorhandene Tabelle oder ein vorhandenes Dokument – je nachdem, wie Sie es binden.
- Jeder Prophecy-Job und jeder Zeitplan einer SQL-Pipeline wird zu einem [geplanten Ereignis](/de/administration/scheduled-events/) für den konvertierten Workflow und ist aktiviert, wenn er in Prophecy aktiviert ist. Siehe [Zeitpläne](#dienste-und-steuerung).
- Skripte, SQL-Anweisungen, Makros und anderer Projektcode gelangen in Schritten an, die den Code enthalten. Siehe [Projektcode in Schritten](#projektcode-in-schritten).
- Ein benutzerdefiniertes Gem, einschließlich eines Gem-Builder-Gems, führt den Code aus, den der Export dafür enthält, und zwar in einem Python-Schritt. Siehe [Projektcode in Schritten](#projektcode-in-schritten).
- Ein Pivot-Gem mit einer HAVING-Bedingung oder einer Spalte mit allen Werten wird konvertiert, ebenso die Sortier- und Deduplicate-Typen, die Prophecy anbietet.
- Ausdrücke werden unter der Annahme des Spark-SQL-Verhaltens bei Null-Behandlung, Ganzzahldivision und impliziten Casts konvertiert. Prüfen Sie die Ergebnisse dort, wo sich dies auf Ihrer PlaidCloud-Engine unterscheidet.

## Vorbereitung

1. Exportieren Sie das Projekt aus Prophecy als `.zip`-Datei, oder exportieren Sie eine einzelne Pipeline, ein Modell oder einen Subgraphen als `.json`-Datei.
2. Laden Sie die Datei in ein [Dokumentenkonto](/de/guides/documents/adding-accounts/) hoch, auf das Sie lesend zugreifen können.
3. Wählen Sie das PlaidCloud-Projekt aus, das die Workflows erhalten soll. Sie benötigen Schreibzugriff darauf.
4. Legen Sie fest, woher die Dateien für ungebundene Datasets gelesen werden. Wählen Sie ein Dokumentenkonto und einen Basisordner.

## Das Projekt konvertieren

Konvertieren Sie über die Analyze-App, die REST-API oder den MCP-Werkzeugkatalog. Alle drei nehmen dieselben Felder entgegen.

### Analyze-App

1. Öffnen Sie **Analysieren** und wählen Sie **Tools → Prophecy-Projekt importieren**.
2. Wählen Sie das **Zielprojekt**, das **Prophecy-Projekt (.zip oder .json)**, das Sie in ein Dokumentenkonto hochgeladen haben, und den **Speicherort der Quelldateien**, also das Dokumentenkonto und den Basisordner, aus denen die Dateien für ungebundene Datasets gelesen werden.
3. Legen Sie unter **Objektnamen und Optionen** optional Präfixe für Workflows, Schritte und Tabellen fest, wählen Sie den **Workflow-Typ** und entscheiden Sie, ob nicht konvertierte Komponenten als Durchreich-Platzhalter importiert werden sollen.
4. Binden Sie unter **Quellbindungen und Parameter** optional ein Dataset an eine vorhandene Tabelle, indem Sie den Dataset-Namen und die Tabellen-ID eingeben, und überschreiben Sie Prophecy-Parameter anhand ihres Namens. Um Verbindungen zu binden, verwenden Sie die REST-API oder das MCP-Werkzeug. Siehe [Verbindungen binden](#verbindungen-binden).
5. Wählen Sie **Importieren**.

Das Fenster zeigt den Fortschritt an, während es das Projekt liest, die Pipelines parst, sie PlaidCloud-Operationen zuordnet und die Workflows, Tabellen und Schritte erstellt. Nach Abschluss zeigt das Fenster den Konvertierungsbericht: Schrittanzahlen nach Konfidenz, Warnungen, **Teilweise Konvertierungen**, **Nicht konvertierte Platzhalter**, **Verworfene Komponenten** und die **Hochzuladenden Quelldateien**.

### Felder

Die REST-API und das MCP-Werkzeug nehmen diese Felder entgegen.

| Feld | Erforderlich | Funktion |
| --- | --- | --- |
| `source_account_id` | Ja | Dokumentenkonto, das den Prophecy-Export enthält. |
| `source_file_path` | Ja | Pfad der Projekt-`.zip` oder einer einzelnen `.json`-Datei mit Pipeline, Modell oder Subgraph innerhalb dieses Kontos. |
| `project_id` | Ja | Projekt, in dem die Workflows erstellt werden. |
| `document_account_id` | Ja | Dokumentenkonto, aus dem ungebundene Datasets lesen. |
| `document_account_path` | Ja | Basisordner in diesem Konto für ungebundene Datasets. Ein leerer Wert oder `/` steht für das Stammverzeichnis des Kontos, ein führendes `/` wird ignoriert. Pfade mit `..` oder mit Punkt beginnenden Segmenten, geschweiften Klammern, einem Laufwerksbuchstaben oder URL-Schema sowie Steuerzeichen werden abgelehnt. |
| `workflow_prefix` | Nein | Präfix, das den Workflow-Namen hinzugefügt wird. |
| `step_prefix` | Nein | Präfix, das den Schrittnamen hinzugefügt wird. |
| `table_prefix` | Nein | Präfix, das den Tabellennamen hinzugefügt wird. Standardmäßig der eigene Name des Workflows. Ein Präfix, das einen vorhandenen Tabellennamen wiederverwenden würde, wird abgelehnt, bevor etwas erstellt wird. Das verwendete Präfix wird im Konvertierungsbericht zurückgegeben. |
| `workflow_type` | Nein | `advanced` (Standard) legt den Graphen auf die DAG-Arbeitsfläche. `standard` erzeugt eine serielle Schrittliste. |
| `source_bindings` | Nein | Bindet Datasets und Operationen an vorhandene Daten. Siehe [Quellen binden](#quellen-binden). |
| `connection_bindings` | Nein | Bindet die Datenbanken, Dateispeicher, REST-APIs und E-Mail, die ein Projekt erreicht, an PlaidCloud-Verbindungen und Dokumentenkonten. Siehe [Verbindungen binden](#verbindungen-binden). |
| `parameters` | Nein | Überschreibt Prophecy-Parameter. Siehe [Parameter](#parameter). |
| `allow_unconverted_placeholders` | Nein | Steuert, was ein Platzhalter zur Laufzeit tut. Siehe [Platzhalter für nicht konvertierte Gems](#platzhalter-für-nicht-konvertierte-gems). |

### REST

Senden Sie die Felder als JSON-Body an:

```text
POST /rest/v1/analyze/prophecy/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/prophecy/customer-360.zip",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/prophecy-inputs"
}
```

Sie benötigen die Rolle `analyze.workflow.write`.

### MCP

Ein MCP-verbundener KI-Agent ruft das Werkzeug `prophecy_convert` mit denselben Feldern auf. Wie Sie einen Agenten verbinden, lesen Sie unter [KI-Agenten (MCP)](/de/integrations/ai-coding-agents/). Das Werkzeug ändert Ihr Projekt, prüfen Sie den Aufruf daher, bevor Sie ihn genehmigen.

## Quellen binden

Ein Prophecy-Export beschreibt, woher seine Daten stammen, enthält aber weder Daten noch Zugangsdaten. Verwenden Sie `source_bindings`, um jedes Dataset mit Daten zu verbinden, die Sie bereits in PlaidCloud haben. Ein Schlüssel ist der Dataset-Name, wie ihn der Konvertierungsbericht aufführt. Ein Wert ist entweder:

- Eine `analyzetable_`-ID für eine Tabelle im Zielprojekt. Der konvertierte Workflow liest diese Tabelle direkt.
- Ein Objekt mit `account`, `path` und optional `sheet`, um eine Datei aus einem Dokumentenkonto zu lesen.

```json
"source_bindings": {
  "customers": "analyzetable_1234",
  "budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

Eine Bindung, die Sie nicht lesen können, wird abgelehnt. Ein Schlüssel, der zu keinem Dataset passt, wird als Warnung gemeldet. Das Analyze-Fenster bindet Datasets an Tabellen; verwenden Sie die REST-API oder das MCP-Werkzeug, um ein Dataset an eine Dokumentdatei zu binden.

### Ungebundene Datasets

Ein Dataset ohne Bindung wird zu einem Import-Schritt ohne Daten, und der Konvertierungsbericht enthält dazu eine Warnung. Der Schritt liest aus:

```text
<document_account_path>/prophecy/<workflow id>/<dataset name>.csv
```

Laden Sie die Datei in diesen Pfad hoch und führen Sie den Workflow aus. Solange die Datei nicht vorhanden ist, endet der Import-Schritt mit einer Warnung und erstellt eine leere Tabelle, und der Workflow läuft weiter. Der Bericht führt jeden Pfad unter **Hochzuladende Quelldateien** auf.

### Tabellen- und Dateioperationen binden

Gems, die Tabellen oder Dateien ändern, etwa Table Operations (Aktualisieren, Löschen, Verwerfen) und File Operation (Kopieren), wirken nur auf Daten, die die Konvertierung erstellt hat. Damit eines auf bereits vorhandene Daten wirkt, binden Sie diese mit einem Schlüssel der Form `operation:<pipeline>/<id>`, wobei `<pipeline>` der Name der Pipeline und `<id>` die ID des Gems ist. Der Konvertierungsbericht nennt den Schlüssel für jedes solche Gem.

```json
"source_bindings": {
  "operation:daily_load/Operation_1": "analyzetable_5678"
}
```

Eine zerstörerische Tabellen- oder Dateioperation wird nur ausgeführt, wenn Sie sie binden. Ohne Bindung arbeitet ein Table-Operations-Gem mit einer Tabelle, die ein anderes Gem desselben Projekts geschrieben hat, und wird andernfalls zu einem Platzhalter, der seinen Schlüssel nennt. Eine File Operation kopiert aus ihrem eigenen Staging-Ordner. Außerhalb der eigenen Tabellen und Ordner der Konvertierung wird nichts geändert, sofern Sie es nicht binden.

## Verbindungen binden

Ein Prophecy-Projekt erreicht Datenbanken, Dateispeicher, REST-APIs und Mailserver über Verbindungen. Der Export enthält die Verbindungsnamen, aber keine Zugangsdaten. Verwenden Sie daher `connection_bindings`, um jede einzelne auf eine PlaidCloud-Verbindung oder ein Dokumentenkonto zu richten, die Sie bereits haben. Der Konvertierungsbericht führt jeden Schlüssel unter seinen Bindungen auf.

```json
"connection_bindings": {
  "connection:warehouse_pg": "<connection id>",
  "connection:landing_s3": "<document account id>",
  "operation:daily_load/Email_1": "<connection id>"
}
```

Ein Schlüssel ist einer der folgenden:

| Schlüssel | Bindet | Wert |
| --- | --- | --- |
| `connection:<name>` | Die Prophecy-Verbindung, die ein Gem oder ein Datenbank-Dataset benennt. Eine Bindung gilt für jedes Gem an dieser Verbindung. Ein Gem ohne Verbindungsnamen verwendet `connection:<pipeline>/<gem id>`, ein Datenbank-Dataset `connection:<dataset name>`. | Eine PlaidCloud-Verbindungs-ID: eine Datenbankverbindung (einschließlich BigQuery und SAP HANA), eine MongoDB- oder Apache-Kafka-Verbindung, eine Salesforce-Verbindung für Salesforce-Lese- und -Schreibvorgänge, eine Tableau-Verbindung für ein Tableau-Gem, eine REST-Verbindung für Azure Cosmos DB, Pinecone, Power BI sowie Schreibvorgänge nach Smartsheet und Slack oder eine Singer-basierte Verbindung für Lesevorgänge aus Smartsheet, Slack und Iceberg. Eine Dokumentenkonto-ID für ein File-Storage- oder Directory-Gem. |
| `operation:<pipeline>/<gem id>` | Ein REST-Gem, das etwas anderes als GET, HEAD oder OPTIONS sendet, und jedes Email-Gem. | Eine Verbindungs-ID. Bei REST eine REST-Verbindung, die die Zugangsdaten enthält. |

Die Bindung ist Ihre Einwilligung für Gems, die Dinge außerhalb der Konvertierung ändern:

- Eine REST-Anfrage, die ändern kann, was die API enthält, und eine E-Mail, die echte Personen erreicht, werden nur dann zu funktionsfähigen Schritten konvertiert, wenn Sie ihren `operation:`-Schlüssel binden. Ungebunden ist das Gem ein Platzhalter, der den Schlüssel nennt.
- Ein Dokumentenkonto, das an ein File-Storage- oder Directory-Gem gebunden ist, erlaubt den Schritten dieses Gems, Dateien in diesem Konto zu schreiben, zu löschen oder zu verschieben.
- Eine GET-, HEAD- oder OPTIONS-Anfrage wird so gesendet, wie das Gem sie sendet. Ungebunden hat sie keine Zugangsdaten, bis Sie im konvertierten Schritt eine REST-Verbindung auswählen.

Ein Datenbank-Dataset oder External-Table-Gem ohne Bindung wird zu einem Schritt, der seinen Schlüssel nennt und darauf wartet, dass Sie eine Verbindung auswählen, und der Bericht enthält eine Warnung. Konvertieren Sie erneut mit gebundenem Schlüssel oder wählen Sie die Verbindung im Schritt aus. Eine Bindung, deren ID die falsche Art von Speicher für ihre Gems bezeichnet oder die Sie nicht verwenden können, wird abgelehnt. Ein Schlüssel, der zu nichts passt, wird als Warnung gemeldet.

## Parameter

`parameters` überschreibt Prophecy-Parameter bei der Konvertierung:

```json
"parameters": {
  "instance": "prod",
  "values": { "run_date": "2026-10-01", "region": "EMEA" },
  "pipelines": {
    "daily_load": { "instance": "prod", "values": { "region": "APAC" } }
  }
}
```

`instance` benennt eine Konfigurationsinstanz. `values` sind Text, Zahlen oder boolesche Werte. Ein Pipeline-Eintrag überschreibt die projektweiten Werte für diese Pipeline. Der Bericht führt die verwendeten Parameter auf sowie diejenigen, die umbenannt wurden, damit sie zu PlaidCloud-Variablennamen passen.

## Den Konvertierungsbericht lesen

Die Antwort enthält den Konvertierungsbericht. Lesen Sie ihn, bevor Sie die Workflows ausführen.

| Abschnitt | Was er Ihnen sagt |
| --- | --- |
| Zusammenfassung | Wie viele Schritte mit hoher, mittlerer oder niedriger Konfidenz konvertiert wurden und wie viele nicht. |
| Warnungen | Alles, was der Konverter angenommen, angenähert oder übersprungen hat, einschließlich ungebundener Datasets und Bindungsschlüssel, die zu nichts passten. |
| Teilweise Konvertierungen | Schritte, die konvertiert werden, sich aber in einem Modus oder einer Option vom Gem unterscheiden. Jeder enthält einen Hinweis, was zu prüfen ist. |
| Nicht konvertierte Platzhalter | Gems ohne PlaidCloud-Äquivalent, mit Begründung. |
| Verworfene Komponenten | Gems, die keine eigene Arbeit leisten, etwa Grenzmarkierungen des Kontrollflusses, und der Schritt, der sie jeweils aufgenommen hat. |
| Hochzuladende Quelldateien | Der Dokumentpfad, aus dem jedes ungebundene Dataset liest. |
| Workflows | Der für jede Pipeline erstellte Workflow in Ausführungsreihenfolge. Eine Pipeline, die der Konverter abgelehnt hat, ist markiert. |

Der Bericht nennt außerdem das verwendete Tabellenpräfix und die angewendeten Parameter. Ein Schritt, bei dem sich der Konverter nicht sicher ist, wird gemäß der wahrscheinlichsten Lesart konvertiert und erhält im Bericht einen Hinweis. Prüfen Sie diese Schritte anhand Ihrer Prophecy-Ausgabe.

## Projektcode in Schritten

Prophecy-Projekte enthalten Code: Script-Gems, SQL-Anweisungen, Makros, dynamische Eingaben, Aufrufe gespeicherter Prozeduren und benutzerdefinierte Gems. Der Konverter führt diesen Code nicht aus. Er legt ihn in einem Schritt ab:

- SQL wird in den SQL-Dialekt Ihres Mandanten übersetzt und in einem SQL-Schritt abgelegt; die Eingaben des Gems stehen unter den Namen zur Verfügung, unter denen die Abfrage sie liest.
- Python-Skripte werden in einem Python-Schritt abgelegt, wobei der Tabellenzugriff umgeschrieben wird. Ein Skript, das Methoden von Spark-DataFrames aufruft, behält diese Aufrufe und führt sie im Schritt aus.
- Ein benutzerdefiniertes Gem, einschließlich eines Gem-Builder-Gems, führt den PySpark-Code aus, den sein Pipeline-Export dafür enthält, und zwar in einem Python-Schritt.
- Ein Makro aus einem bekannten dbt-Paket wird zu den Standardschritten, die tun, was das Makro tut. Ein Makro in Ihrem eigenen Projekt oder in einem Paket, das der Export enthält, wird ebenfalls gelesen und konvertiert, einschließlich if- und for-Blöcken, set, Filtern, verschachtelten Makros und Adapter-Dispatch.
- Eine in Python geschriebene benutzerdefinierte Aggregatfunktion in einem Aggregate-Gem läuft für jede Gruppe in einem Python-Schritt.

Jeder Schritt, der Projektcode enthält, erhält eine Warnung, ebenso übersetztes SQL. Prüfen Sie den Code in jedem dieser Schritte, bevor Sie den Workflow ausführen. Der Konverter hält alles zurück, was in Code-Zeichenfolgen und Kommentaren wie Zugangsdaten aussieht; hinterlegen Sie Zugangsdaten daher in einer Verbindung und nicht im Code.

## Platzhalter für nicht konvertierte Gems

Ein Gem, das der Konverter nicht nachbilden kann, wird als Platzhalter-Schritt angelegt, der den Namen des Gems trägt. Beispiele sind ein benutzerdefiniertes Gem, dessen Code nicht im Export enthalten ist, und ein Gem, das Daten außerhalb der Konvertierung ändert, etwa eine REST-Anfrage, die Daten ändern kann, eine E-Mail oder eine Tabellen- oder Dateioperation, wenn Sie den zugehörigen `operation:`-Schlüssel nicht gebunden haben. Ein Datenbank-Dataset oder eine External Table ohne gebundene Verbindung ist kein Platzhalter: Es wird zu einem Schritt, der darauf wartet, dass Sie eine Verbindung auswählen. Standardmäßig schlägt ein Platzhalter fehl, sobald der Workflow ihn erreicht, damit eine Ausführung nicht Erfolg für Arbeit melden kann, die nie stattgefunden hat.

Setzen Sie `allow_unconverted_placeholders` auf `true` (im Fenster **Nicht konvertierte Komponenten als Durchreich-Platzhalter importieren**), um stattdessen jeden Platzhalter als Durchreich-Schritt zu importieren. Die Ausführung läuft dann an ihm vorbei weiter, und die Ausgabe des Platzhalters ist seine Eingabe. Der Bericht zählt die Durchreich-Platzhalter und führt ihre Schritte auf. Bauen Sie die Funktion mit einem nativen Schritt nach, wenn ihr Ergebnis wichtig ist.

## Die konvertierten Workflows ausführen

1. Öffnen Sie die neuen Workflows im Projekt. Der Bericht führt sie in Ausführungsreihenfolge auf.
2. Setzen Sie alle Projektvariablen, die aus Prophecy-Parametern stammen.
3. Laden Sie die Dateien für ungebundene Datasets in die Pfade aus dem Bericht hoch.
4. Prüfen Sie die Schritte, die Projektcode enthalten.
5. Führen Sie die Workflows aus und prüfen Sie die Ausgabetabelle jedes Schritts.

Geplante Ereignisse, die aus Prophecy-Zeitplänen erstellt wurden, sind aktiviert, wenn sie in Prophecy aktiviert waren, und führen die konvertierten Workflows daher nach ihrem Zeitplan aus. Um die Workflows zuvor zu prüfen, deaktivieren Sie die Ereignisse unter [Geplante Ereignisse](/de/administration/scheduled-events/) und aktivieren Sie sie, wenn Sie bereit sind.

## Was konvertiert wird

Jedes Prophecy-Gem wird mit den Optionen, die es bietet, vollständig in native Schritte, Projektvariablen, geplante Ereignisse oder Arbeitsflächenobjekte konvertiert. Die [Prophecy-Konvertierungsmatrix](/de/reference/prophecy-conversion-matrix/) führt jedes Gem mit dem PlaidCloud-Schritt auf, zu dem es wird, und unter [Sonderfälle](#sonderfälle) stehen die wenigen Verhaltensweisen, die Sie prüfen sollten; der Konvertierungsbericht nennt jede davon dort, wo sie auftritt.

### Datenbewegung

| Funktion | So wird konvertiert |
| --- | --- |
| Schreibmodi | Schreibmodi von Zielen werden in Plattformschritte konvertiert: SCD2 mit den Strategien „check" und „timestamp" (die Strategie „timestamp" datiert jede Version anhand der Spalte, die `scd2.updatedAtColumn` des Gems benennt), Merge, `replaceWhere` und `insertInto`. Ein Merge wendet die SET-Ausdrücke pro Spalte aus seinen Klauseln für Update bei Übereinstimmung und Insert bei fehlender Übereinstimmung an; eine Klausel, die keine Spalte setzt, übernimmt jede Spalte aus der eingehenden Zeile. Eine erste Ausführung in ein leeres Ziel schreibt jede Zeile, wie es dbt und Delta tun. Die erste Ausführung benötigt keine vorab erstellte Tabelle, auch nicht bei einer Pipeline, die ein Dataset liest, das sie auch schreibt – es sei denn, der Export gibt nicht an, welche Spalten dieses Dataset hat: Dann erstellen Sie die Tabelle vor der ersten Ausführung. Spätere Ausführungen wenden den inkrementellen Filter oder die Merge-Bedingung an. Die Modi `error` und `ignore` prüfen mit der [Bedingung „Tabelle existiert"](/de/guides/workflows/step-conditions/#bedingungen-für-das-vorhandensein-einer-tabelle). |
| Time Travel | Eine Delta- oder Katalogtabellenquelle, die eine frühere Version ihrer Tabelle liest, per `versionAsOf` oder `timestampAsOf`, liest diese Version aus Databricks über die Verbindung, die Sie binden. |
| Streaming | Streaming-Quellen und -Ziele laufen als geplanter Batch. Die Streaming-Senke ersetzt ihre Tabelle, statt anzuhängen, sodass eine erneute Ausführung nie Zeilen dupliziert. Planen Sie den Workflow, damit neu eingetroffene Daten aufgenommen werden. |
| Datenbanken | JDBC-, Snowflake-, Redshift-, Hive-, BigQuery-, SAP-HANA- und External-Table-Gems lesen und schreiben über die PlaidCloud-Verbindung, die Sie binden. Ein BigQuery-Dataset wird mit [SQL importieren](/de/reference/workflow-steps/import/import-sql/) gelesen und mit dem Schritt [Export External Database Tables](/de/reference/workflow-steps/export/export-external-tables/) über eine [BigQuery-Verbindung](/de/reference/connectors/google/big-query/) geschrieben. Eine SAP-HANA-Tabelle, die in einem der Merge-Modi des HANA-Gems geschrieben wird, einschließlich SCD2 und der Löschmodi, wird neben dem Ziel bereitgestellt und über den Primärschlüssel des Ziels oder die Merge-Spalten des Gems in dieses gemergt; ein fehlendes Ziel wird zuvor erstellt. |
| MongoDB und Kafka | Ein MongoDB-Dataset wird mit [MongoDB importieren](/de/reference/workflow-steps/import/import-mongodb/) gelesen, einschließlich seines Filters oder seiner Aggregationspipeline, und ein Lesevorgang, der keine Spalten deklariert, übernimmt sie aus den ersten Dokumenten, wie es der Spark-Connector tut. Ein Schreibvorgang verwendet [MongoDB exportieren](/de/reference/workflow-steps/export/export-mongodb/) im passenden Schreibmodus: `update` aktualisiert die Felder des passenden Dokuments oder fügt eines ein, `ignore` schreibt nur, solange die Collection kein Dokument enthält, und `error` beendet die Ausführung, wenn sie eines enthält. Eine Kafka-Quelle liest ihre Topics zwischen dem Start- und dem Ende-Offset mit [Kafka importieren](/de/reference/workflow-steps/import/import-kafka/), und ein Kafka-Ziel sendet jede Zeile mit [Kafka exportieren](/de/reference/workflow-steps/export/export-kafka/). Ein Kafka-Dataset, das sich mit `OAUTHBEARER` anmeldet, verwendet die [OAuth-Anmeldung](/de/reference/connectors/databases/apache-kafka/#oauth-oauthbearer) der Kafka-Verbindung, die Sie binden, da der Export keine Zugangsdaten enthält. |
| Azure Cosmos DB | Ein Lesevorgang sendet die Abfrage des Datasets oder liest jedes Dokument mit [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) über eine REST-Verbindung mit Cosmos-DB-Authentifizierung und folgt dem Continuation-Header von Seite zu Seite. Ein Schreibvorgang sendet je Zeile eine Anfrage gemäß der Schreibstrategie des Gems: Überschreiben, Anhängen, Löschen oder Patchen. Eine Zeile, die das ETag ihres Dokuments trägt, wird nur ersetzt oder gelöscht, wenn sich das Dokument seither nicht geändert hat, und eine Zeile, die der Container aus diesem Grund oder wegen eines fehlenden oder vorhandenen Dokuments ablehnt, wird übersprungen, wie es der Spark-Connector tut. Der Modus `ignore` schreibt nur, solange der Container kein Dokument enthält. |
| Salesforce | Ein Lesevorgang verwendet [Salesforce: Objekt abfragen](/de/reference/workflow-steps/salesforce/query-salesforce-object/), einschließlich gelöschter und archivierter Datensätze, wenn das Gem sie anfordert. Ein Schreibvorgang fügt ein, aktualisiert, führt ein Upsert aus oder löscht, mit einer Anfrage je Zeile; ein Upsert gleicht über das externe ID-Feld des Gems ab, über `Id`, wenn es keines benennt. |
| Smartsheet, Slack und Pinecone | Ein Smartsheet-Lesevorgang eines benannten Blatts mit deklarierten Spalten ruft das Blatt über Ihre REST-Verbindung ab und legt für jede Blattzeile eine Zeile und für jede deklarierte Spalte eine Spalte an. Andere Smartsheet-Lesevorgänge sowie Slack- und Iceberg-Lesevorgänge verwenden [Import Singer Source](/de/reference/workflow-steps/import/import-singer/). Ein Smartsheet-Schreibvorgang fügt die Zeilen dem benannten Blatt hinzu, und ein Überschreiben löscht zuvor die Zeilen des Blatts. Ein Slack-Schreibvorgang postet für jede Zeile eine Nachricht, und eine Nachricht, die Slack ablehnt, lässt den Schritt fehlschlagen. Ein Pinecone-Index wird als seine Vektoren und deren Metadaten gelesen, und ein Schreibvorgang führt ein Upsert der Zeilen als Vektoren aus. |
| Tableau und Power BI | Tableau und Tableau Write veröffentlichen die Eingabe als Hyper-Extrakt mit [Publish to Tableau](/de/reference/workflow-steps/export/export-to-tableau/) über die Tableau-Verbindung, die Sie binden. Power BI Write überträgt die Eingaben über eine REST-Verbindung mit OAuth 2.0 in ein Power-BI-Push-Dataset, wobei der Workspace anhand des Namens gefunden und das Dataset erstellt wird, wenn es neu ist. |
| Dateiformate | CSV, JSON, Parquet, Avro, Excel, XML, feste Breite und ORC über [ORC importieren](/de/reference/workflow-steps/import/import-orc/). Formatoptionen werden abgebildet oder als neutral markiert, wenn sie keine Zeile ändern: das Änderungszeitfenster eines Avro-Lesevorgangs, die EBCDIC-Kodierung einer Datei mit fester Breite, Header- und Footer-Datensätze sowie Datensätze ohne Zeilenumbrüche, die Blattzuordnung und das Kennwort eines Excel-Lesevorgangs, die Anführungszeichen-Optionen eines CSV-Schreibvorgangs und ein Excel-Schreibvorgang mit einem Blatt je Wert. Komprimierte Textdateien werden mit gzip, Deflate (zlib), Zstandard, LZ4, Snappy und LZO gelesen und geschrieben; eine komprimierte Datei wird gelesen, wenn ihr Name auf die Erweiterung ihres Codecs endet. Verschlüsselte Dateien werden an Ort und Stelle entschlüsselt und verschlüsselt. Siehe [Verschlüsselte Dateien](#verschlüsselte-dateien). |
| File Operation | Copy und Move werden in [Dokument: Datei kopieren](/de/reference/workflow-steps/document/copy-document-file/) oder Copy Directory für den Ordner konvertiert, den Sie binden; es werden nur die Dateien behalten, deren Name zum `filenameRegex` des Gems passt, und jede Datei behält ihren Pfad unterhalb des Quellordners, wenn das Gem rekursiv arbeitet. |
| Directory | Listet die Dateien des gebundenen Dokumentordners mit [Verzeichnisliste](/de/reference/workflow-steps/document/directory-listing/) in den Spalten des Gems auf. Bei aktivierter Option für den Blattnamen liefert jede Excel-Arbeitsmappe eine Zeile je Blatt samt `sheet_name`; andere Dateien liefern eine Zeile mit leerem `sheet_name`. |

### Spalten und Zeilen

| Gem oder Funktion | So wird konvertiert |
| --- | --- |
| Surrogate Key | Schlüssel setzen sich ab einer Tabelle fort, die den zuletzt vergebenen Schlüssel behält, wie es die Schlüsseldatei des Gems tut. Jedes Gem, das dieselbe Schlüsseldatei benennt, teilt sich diese Tabelle, sodass sich ihre Schlüssel nie überschneiden. Eine Ausführung ohne Zeilen lässt sie unverändert, und Schlüssel beginnen beim Anfangswert, bevor eine Ausführung einen vergeben hat. |
| Column Parser, XML Parse, JSON-Parsing | XML- und JSON-Text wird mit den Schritten [XML parsen](/de/reference/workflow-steps/tables/table-xml-parse/) und [JSON parsen](/de/reference/workflow-steps/tables/table-json-parse/) geparst, wobei jedes Feld aus dem Text des Elements, einem Attribut oder einem untergeordneten Element gelesen wird. XML, das ohne Schema geparst wird, übernimmt den Typ jedes Felds aus den Daten, wie es `schema_of_xml` von Spark tut. |
| Business Rules | Eine Projekt-Business-Rule, die in einem Ausdruck aufgerufen wird, wird in dieselben Bedingungen konvertiert, mit einem `CASE` je Spalte, die sie setzt. |
| Casts | Ein Cast von Text in eine Dezimalzahl oder ein Long folgt Spark exakt: Leerzeichen und Steuerzeichen um die Zahl werden entfernt, eine Dezimalzahl wird kaufmännisch auf ihre Skalierung gerundet, und Text, der keine Zahl ist, oder ein Wert außerhalb des Bereichs ergibt Null. |
| Datum und Uhrzeit | Datums- und Uhrzeitformate werden für die Engine Ihres Workspace geschrieben, einschließlich Databend, und `window()` ordnet jeden Zeitstempel seinem rollierenden Fenster zu, so ausgerichtet, wie Spark es ausrichtet. |
| Iterator-Ausgaben | Ein Table Iterator oder While Iterator, dessen Ausgabespalten erst zur Laufzeit bekannt sind, sammelt die Zeilen jedes Durchlaufs positionsbasiert mit [Tabelle: Union All](/de/reference/workflow-steps/tables/table-union-all/#spaltenzuordnung), wobei jede Spalte auf einen Typ erweitert wird, in den jeder Durchlauf passt, so wie Prophecy die Durchläufe stapelt. |
| Data Encoder/Decoder AES | Läuft auf jeder Engine. Der Schlüssel sowie der Initialisierungsvektor und die zusätzlichen Daten, wenn das Gem sie benennt, stammen aus den Workflow-Variablen `aes_key`, `aes_iv` und `aes_aad`, die Sie setzen. |
| Data Masking Hash | Berechnet dieselben Werte wie `hash()` von Spark. |
| Buffer, Simplify, Heat Map | Buffer zeichnet eine abgerundete Ecke mit derselben Segmentanzahl wie Prophecy, Simplify entfernt dieselben Stützpunkte, und Heat Map summiert Heat in H3-Sechsecken in der Auflösung des Gems, wobei eine Dezimal-Heat eine Dezimalzahl bleibt. |

### Dienste und Steuerung

| Gem | So wird konvertiert |
| --- | --- |
| Pipeline | Führt die benannte Pipeline mit einer [Workflow Loop](/de/reference/workflow-steps/workflow-control/workflow-loop/) aus, einmal für jede Eingabezeile (einmal, wenn es keine Eingabe gibt, nie bei null Zeilen), wobei jeder Parameter aus einer Konstante, einer Spalte der Zeile oder einem Ausdruck darüber gesetzt wird. Jede Ausführung wird fortgesetzt, auch wenn eine frühere fehlschlägt, und die Ausgabe des Gems hat je Ausführung eine Zeile mit Status, Meldung und Zeiten, so wie Prophecy sie aufzeichnet. |
| Zeitpläne | Ein Prophecy-Job oder der Zeitplan einer SQL-Pipeline wird zu einem [geplanten Ereignis](/de/administration/scheduled-events/) mit dem Namen `Prophecy <name>` für den konvertierten Workflow, aktiviert, sofern er in Prophecy nicht deaktiviert ist. Ein Spark-Job wird auf diese Weise konvertiert, wenn er eine konvertierte Pipeline ohne Konfigurationsüberschreibungen oder Ausführungsbedingungen ausführt. |
| Script | Ein Python-Skript wird in einem Python-Schritt abgelegt. Ein Wert, den das Skript auf `Config` setzt, wird zu einer Workflow-Variable, die spätere Schritte lesen und die zu Beginn jeder Ausführung auf den Wert der Pipeline zurückgesetzt wird, wie es bei `Config` in Prophecy der Fall ist. |
| REST API, REST API Enrich | [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/)-Schritte, eine Anfrage je Eingabezeile, wobei eine Fehlerantwort wie in Prophecy beibehalten wird. Enrich liest zusätzlich Status, Grund und endgültige URL. Eine Anfrage, die auf ein asynchrones Ergebnis wartet, fragt so lange ab, bis die Antwort meldet, dass sie fertig ist. |
| Stored Procedure | Ein Gem, das Argumente übergibt, ruft seine Prozedur mit [Remote-Ausführung: SQL](/de/reference/workflow-steps/agent/agent-remote-execution-of-sql/#eine-anweisung-einmal-pro-zeile-ausführen) einmal je Eingabezeile auf, wobei jedes Argument aus seiner Spalte als Parameter gebunden wird. Ein Gem ohne Argumente ruft sie einmal über einen Agent auf. Wählen Sie die Verbindung oder den Agent im konvertierten Schritt. |
| Email, Email Data | [Notify Via Email](/de/reference/workflow-steps/notifications/notify-via-email/) mit Cc, Bcc, Reply-To und einer Nachricht je Zeile, wenn ein Feld aus einer Spalte liest. |
| OpenAI, Bedrock, SageMaker Endpoint | [Text: NLP (AI)](/de/reference/workflow-steps/text-documents/nlp-ai/) über die LLM-Verbindung Ihres Workspace. OpenAI- und Bedrock-Einbettungen verwenden die Aufgabe Embed, die eine OpenAI-kompatible oder eine Azure-OpenAI-Verbindung benötigt; eine Anthropic-Verbindung wird abgelehnt. |
| Pinecone Lookup | Eine REST-Anfrage je Zeile. |
| Data Quality Check, Deequ, Soda | Die Prüfungen laufen im Warehouse und schreiben die Ergebnistabelle. Ein Data Quality Check beendet die Ausführung nur, wenn das Gem `minFailedChecks` oder eine Nachaktion `fail_pipeline` setzt; andernfalls führt die Ergebnistabelle die Fehler auf. Deequ und Soda beenden die Ausführung nie. Eine Prüfung der minimalen oder maximalen Länge einer numerischen Spalte misst die Zahl als Text. Soda-Prüfungen werden aus dem YAML des Projekts konvertiert, einschließlich fehlender, ungültiger und gültiger Werte, Statistiken, Längen, Perzentile, Duplikate über Spalten hinweg, Aktualität, fehlgeschlagener Zeilen und Ihrer eigenen Kennzahlabfragen. |
| ToDo | Löst einen Fehler aus, der das ursprüngliche Tool und die Meldung nennt, wenn die Ausführung ihn erreicht. |

### Verschlüsselte Dateien

Ein File-Storage-Gem, das eine verschlüsselte Datei liest, wird in [Dokument: Datei entschlüsseln](/de/reference/workflow-steps/document/encrypt-decrypt-file/) konvertiert, das die Datei in einen eigenen Ordner entschlüsselt, bevor der Import sie liest; die entschlüsselte Kopie wird anschließend entfernt. Ein Gem, das eine verschlüsselte Datei schreibt, exportiert in diesen Ordner und verschlüsselt die Datei dann mit Dokument: Datei verschlüsseln an ihren Platz. AES- und Blowfish-Dateien sowie kennwortgeschützte Excel-Arbeitsmappen werden unterstützt.

Der Export enthält nie einen Schlüssel, daher lesen ihn die konvertierten Schritte aus einer Workflow-Variable: `aes_key` für einen AES- oder Blowfish-Schlüssel und `xlsx_password` für ein Arbeitsmappenkennwort. Setzen Sie die Variable, bevor Sie den Workflow ausführen, und verwenden Sie einen Schlüssel, der ausschließlich für diese Dateien bestimmt ist. Schlüssel- und Kennwortfelder akzeptieren nur einen Variablenverweis, sodass nie ein Schlüssel in einen Schritt eingegeben wird.

## Sonderfälle

Dies sind die Verhaltensweisen, die ein konvertierter Workflow nicht von selbst nachbildet. Der Konvertierungsbericht nennt jede davon dort, wo sie auftritt.

- **Code oder Daten, die der Export nicht enthält**: Ein Gem-Builder- oder anderes benutzerdefiniertes Gem, dessen Code nicht im Export enthalten ist, und der Aufruf eines Makros eines dbt-Pakets, das der Export auslässt, werden zu einem Schritt, der nennt, was fehlt; exportieren Sie das Projekt mit seinem Pipeline-Code und den dbt-Paketen oder bauen Sie die Logik in einem Python- oder SQL-Schritt nach. Ab-Initio-Gems für Error Detection und MTime reichen ihre Eingabe durch, weil die Regel, die sie anwenden, nicht im Export enthalten ist. Soda-Prüfungen, die aus einer Datei außerhalb des Projekts lesen, sowie Soda-Prüfungen, die mit früheren Scans oder mit einem anderen Dataset vergleichen oder ein von Soda benanntes Format testen, haben keine Zeile in der Ergebnistabelle; berechnen Sie sie in einem späteren Schritt.
- **Ergebnisse, die erst bekannt sind, wenn die Pipeline läuft**: Ein REST-API-Gem, das seine Antwort abflacht, legt die gesamte Antwort in eine Spalte, wenn nichts die Feldnamen deklariert, was erst eine Ausführung offenbart; extrahieren Sie die benötigten Felder in einem späteren Schritt. Ein dbt-Makro, das das Warehouse abfragt, während dbt kompiliert, wird zu einem Schritt, der es benennt; ersetzen Sie die Abfrage durch die Werte, die sie zurückgibt. Ein Spark-StoredProcedure-Gem läuft, aber seine OUT-Werte werden nicht zurückgegeben; die Ausgabe sind die durchgereichten Spalten. `input_file_name()` liefert über einer Tabellen- oder Delta-Quelle, die keine Datei zu benennen hat, eine leere Zeichenfolge, und `hash()` / `xxhash64()` innerhalb eines Aggregats, eines Fensters oder eines Gems mit mehreren Eingaben werden vom Warehouse berechnet und können daher von Spark abweichen.
- **Werte, die beim Konvertieren des Projekts in einen Schritt geschrieben werden**: Ein Parameterwert mit Anführungszeichen, Backslash oder geschweifter Klammer, ein Pipeline-Wert, den ein SQL-Schritt liest, und die Datenbank, die eine Delta-Tabellenoperation über die Konfiguration benennt, werden als feste Werte in den Schritt geschrieben, sodass eine Änderung der Workflow-Variable sie nicht ändert; bearbeiten Sie den Schritt, wenn sich die Konfiguration ändert.
- **Scala-Code**: Ein Scala-Skript, ein Scala-Ausdruck oder eine benutzerdefinierte Scala-Funktion bzw. -Aggregatfunktion wird zu einem Schritt, der sie benennt; schreiben Sie sie in SQL oder Python neu.
- **Kafka-Kerberos-Anmeldung**: Eine Kafka-Quelle oder ein Kafka-Ziel, die sich mit Kerberos (GSSAPI) anmelden, werden ohne den Kerberos-Dienstnamen und den Anmeldemechanismus konvertiert; setzen Sie diese in der PlaidCloud-Verbindung.
- **Streaming**: Streaming-Quellen, -Ziele und -Pipelines laufen als Batch-Workflows über die Daten, die bei der Ausführung vorhanden sind; planen Sie den Workflow so häufig, wie Sie es benötigen.
- **Job-Komponenten**: Ein Spark-Job wird mit seiner einen Pipeline und seinem Zeitplan konvertiert; seine übrigen Komponenten, Ausführungsbedingungen und Konfigurationsüberschreibungen werden nicht konvertiert.
- **Seltene Aufrufe**: Eine benutzerdefinierte Aggregatfunktion, die aus einem Rollup oder einem Fenster aufgerufen wird, und ein dbt-Makro, das über if, for, set und die gängigen Filter hinaus Jinja verwendet, werden zu einem Schritt, der das Gem benennt; rufen Sie die Funktion aus einem Aggregate-Gem auf oder fügen Sie das Makro inline ein.

## Verwandte Leitfäden

- [Savant-Analysen migrieren](/de/guides/workflows/migrate-savant-analyses/)
- [Alteryx-Workflows migrieren](/de/guides/workflows/migrate-alteryx-workflows/)
- [Dokumentenkonten hinzufügen](/de/guides/documents/adding-accounts/)
- [Workflow-Variablen verwalten](/de/guides/workflows/manage-workflow-variables/)
- [Einen Workflow ausführen](/de/guides/workflows/run-a-workflow/)
