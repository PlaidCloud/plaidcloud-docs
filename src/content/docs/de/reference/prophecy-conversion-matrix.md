---
title: Prophecy-Konvertierungsmatrix
description: Wie PlaidCloud Prophecy-Pipelines und SQL-Projekte in native Schritte erweiterter Workflows konvertiert, mit dem Unterstützungsstatus je Gem.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/prophecy-conversion-matrix.md
---

PlaidCloud konvertiert Prophecy-Spark-Pipelines und SQL-Projekte in native
erweiterte Workflows. Der Importer ordnet jedes Prophecy-Gem einem Workflow-Schritt,
einer Projektvariablen oder einem Arbeitsflächenobjekt zu, sodass ein konvertierter Workflow Cloud-nativ
ausgeführt wird und nicht als Emulation.

Jedes Gem, jeder Konnektor und jede Projektstruktur wird konvertiert: **Vollständig** bedeutet, dass das Gem
zu einem nativen PlaidCloud-Schritt, einer Variablen oder einem Arbeitsflächenobjekt wird, das die Arbeit des
Gems übernimmt. Die wenigen Verhaltensweisen, die ein konvertierter Workflow nicht von
selbst abbildet, sind unter [Bekannte Sonderfälle](#bekannte-sonderfälle) aufgeführt, jeweils mit dem, was
zu tun ist.

Wie Sie eine Konvertierung durchführen, lesen Sie unter [Prophecy-Projekte migrieren](/de/guides/workflows/migrate-prophecy-projects/).

## Spark-Pipeline-Gems

### Quelle/Ziel

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Lookup | Vollständig | [Tabelle: Nachschlagen](/de/reference/workflow-steps/tables/table-lookup/) | Jeder Lookup-Aufruf wird zu einem Schritt „Tabelle: Nachschlagen“ in dem Schritt, der ihn verwendet; ein Schlüssel ohne Treffer liefert NULL, und ein doppelter Schlüssel liefert eine seiner Zeilen. |
| Source | Vollständig | Import-Schritt, gewählt nach dem Datensatzformat (siehe [Konnektoren](#konnektoren)) | Jede Source wird zu einem Import-Schritt in eine Tabelle, die nach dem Datensatz benannt ist; ein Format, das der Konverter nicht erkennt, wird als CSV-Datei gelesen, die in den Dokumentordner des Workflows hochgeladen wurde, mit einer Warnung. |
| Streaming Source | Vollständig | Derselbe Import wie die Batch-Source | Streaming-Quellen werden mit einer Warnung in einen einmaligen Batch-Import konvertiert. |
| Streaming Target | Vollständig | Batch-Append-Ladevorgang | Streaming-Ziele werden mit einer Warnung in ein Batch-Append konvertiert. |
| Target | Vollständig | Tabellenexport-/Ladeschritt, gewählt nach Datensatzformat und writeMode | Jedes Target wird zu einem Tabellenlade- oder Exportschritt im Schreibmodus des Gems: append, overwrite, merge mit seinen SET-Ausdrücken, upsert, SCD2, replaceWhere und insertInto. |

### Vorbereiten

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Data Cleansing | Vollständig | Spaltenausdrücke in einem Schritt [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Konvertiert die Optionen für Null-Auffüllung, Trimmen und Groß-/Kleinschreibung in Spaltenausdrücke; bereinigte Spalten wandern ans Ende. |
| Sequence | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Zeilennummernausdruck | Fügt eine Sequenzspalte aus Startwert und Inkrement hinzu. |
| Surrogate Key Generator | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Zeilennummernausdruck | Fügt einen fortlaufenden Schlüssel ab dem Anfangswert hinzu; Schlüssel werden über Ausführungen hinweg aus einer Tabelle fortgesetzt, die den zuletzt vergebenen Schlüssel enthält. |

### Transformieren

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Aggregate | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Aggregation; [Pivot](/de/reference/workflow-steps/tables/table-pivot/), wenn das Gem pivotiert | Gruppiert und aggregiert, wendet die HAVING-Bedingung an und pivotiert in eine Spalte je Pivot-Wert; propagate-all übernimmt jede andere Eingabespalte. |
| Bulk Column Expressions | Vollständig | Erweiterung zu einem Ausdruck je Spalte in einem Schritt [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Ein Ausdruck je aufgeführter Spalte in einem Table-Extract-Schritt; die Konvertierung warnt, dass das Layout des Gems angenommen wird. |
| Bulk Column Rename | Vollständig | Spaltenumbenennung in einem Schritt [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Eine Umbenennung je aufgeführter Spalte in einem Table-Extract-Schritt; die Konvertierung warnt, dass das Layout des Gems angenommen wird. |
| Deduplicate | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Distinct oder einem Zeilennummernfilter | Behält eine Zeile je Schlüssel: distinct, erste oder letzte nach Ihrer Sortierreihenfolge, beliebige oder nur die Schlüssel, die einmal vorkommen. |
| Dynamic Replace | Vollständig | Dynamic-Replace-Transformation, von Hand konfiguriert | Wird in Ersetzungsregeln der Dynamic-Replace-Transformation konvertiert; die Konvertierung warnt, dass das Layout des Gems angenommen wird. |
| Dynamic Select | Vollständig | Spaltenauswahl in einem Schritt [Table Extract](/de/reference/workflow-steps/tables/table-extract/), nach Typ aufgelöst | Löst Spalten zum Konvertierungszeitpunkt nach Typ in eine explizite Auswahl auf. |
| Filter | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Filterausdruck | Wird in einen Table-Extract-Schritt mit Filterausdruck konvertiert; NULL-Bedingungen verwerfen die Zeile. |
| Flatten Schema | Vollständig | [JSON parsen](/de/reference/workflow-steps/tables/table-json-parse/) und [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Flacht verschachtelte Felder in Spalten ab, die mit dem Trennzeichen des Gems benannt werden, und zerlegt Arrays in eine Zeile je Element. |
| Fuzzy Match | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) und [User Defined Transform](/de/reference/workflow-steps/general/user-defined-transform/) | Paart die Datensätze, bewertet jedes Abgleichsfeld nach der Methode des Gems, bildet den Durchschnitt der Bewertungen und behält die Paare ab Ihrem Schwellenwert. |
| Group By Rollup | Vollständig | Union von [Table Extract](/de/reference/workflow-steps/tables/table-extract/)-Aggregationsschritten je Rollup-Ebene | Erweitert den Rollup in ein Aggregat je Gruppierungsebene, per Union mit NULL-Zwischensummen zusammengeführt. |
| Limit | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Zeilenlimit | Wird in ein Zeilenlimit konvertiert; Konfigurationsverweise werden zu Projektvariablen. |
| Normalize | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Explode-Ausdruck | Wiederholt jeden Datensatz entsprechend dem Längenausdruck, berechnet die Ausgabespalten je Index und endet am ersten Index, an dem die Abschlussbedingung zutrifft. |
| Order By | Vollständig | Sortierung in einem Schritt [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Wird in eine Sortierung mit denselben Schlüsseln, derselben Richtung und derselben Platzierung von Nullwerten konvertiert. |
| Reformat | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Spaltenausdrücken | Wird in einen Table-Extract-Schritt mit einem Ausdruck je Ausgabespalte konvertiert; nicht aufgeführte Spalten werden verworfen. |
| Sample Rows | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Zeilenlimit oder Zufallsstichprobe | Behält einen zufälligen Anteil oder eine zufällige Anzahl von Zeilen; die gewählten Zeilen weichen vom Spark-Lauf ab, weil die Stichprobe zufällig ist. |
| Schema Transform | Vollständig | Kette von [Table Extract](/de/reference/workflow-steps/tables/table-extract/)-Schritten, der Reihe nach angewendet | Wendet jede Operation der Reihe nach an: Spalte hinzufügen oder ersetzen, löschen, umbenennen, bei Fehlen mit ihrem Standardwert hinzufügen und eine Projekt-Geschäftsregel hinzufügen. |
| Set Operation | Vollständig | [Union All](/de/reference/workflow-steps/tables/table-union-all/); [Anti-Join](/de/reference/workflow-steps/tables/table-anti-join/) für except; [Inner Join](/de/reference/workflow-steps/tables/table-inner-join/) für intersect | Union all stapelt die Eingaben; except all und intersect all behalten die richtige Anzahl doppelter Zeilen. |
| TransposeAgg | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Aggregation | Konvertiert Gruppierung, Aggregate und Pivot des Gems als Aggregate, mit einer Warnung zur Überprüfung. |
| Unpivot | Vollständig | [Melt](/de/reference/workflow-steps/tables/table-melt/) | Stapelt die ausgewählten Spalten in Namens- und Wertspalten. |
| Watermark | Vollständig | Kein Schritt erforderlich | Verworfen: Eine Batch-Ausführung liest alle vorhandenen Daten, daher gibt es keine Schwelle für verspätete Daten, die anzuwenden wäre. |
| Window Function | Vollständig | Fensterausdrücke in einem Schritt [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Fügt Fensterspalten mit Partition, Reihenfolge und Frame des Gems hinzu, Zeilen oder Bereich, mit unbegrenzten, zeilenaktuellen oder versetzten Grenzen. |

### Join/Split

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Compare Columns | Vollständig | Full Outer Join plus Aggregate je Spalte | Vergleicht die Spalten über einen Full Outer Join der entpivotierten Daten, mit Anzahlen für Übereinstimmungen und Abweichungen. |
| Join | Vollständig | [Inner Join](/de/reference/workflow-steps/tables/table-inner-join/), [Mehrtabellen-Join](/de/reference/workflow-steps/tables/table-multi-table-join/), [Anti-Join](/de/reference/workflow-steps/tables/table-anti-join/) oder [Cross Join](/de/reference/workflow-steps/tables/table-cross-join/) | Erstellt den Join jedes Typs — inner, left, right, full, semi, anti, cross und natural — über eine beliebige Join-Bedingung, wendet die where-Klausel an und schreibt die Select-Liste. |
| Repartition | Vollständig | Kein Schritt erforderlich | Verworfen: PlaidCloud verwaltet die Partitionierung, daher liest der nächste Schritt die vorgelagerte Tabelle direkt. |
| Row Distributor | Vollständig | Ein [Table Extract](/de/reference/workflow-steps/tables/table-extract/)-Filter je Ausgabe | Wird in einen Filter je Ausgabe konvertiert; Zeilen können in mehreren Ausgaben landen. |

### Parsen

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Column Parser | Vollständig | [JSON parsen](/de/reference/workflow-steps/tables/table-json-parse/) / [XML parsen](/de/reference/workflow-steps/tables/table-xml-parse/) | Wird in ein JSON- oder XML-Parsen der benannten Spalte konvertiert; die Konvertierung warnt, dass das Layout des Gems angenommen wird. |

### Benutzerdefiniert

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Custom Gem (Gem Builder) | Vollständig | [User Defined Transform](/de/reference/workflow-steps/general/user-defined-transform/), der den generierten Code des Gems ausführt | Der generierte PySpark-Code des Gems aus dem Pipeline-Export wird in einem Python-Schritt ausgeführt, mit einer Warnung zur Überprüfung. |
| CustomReformatBitbucket | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Wird als das Reformat konvertiert, dessen Ausdrücke das Gem enthält, mit einer Warnung zur Überprüfung. |
| Data Quality Check | Vollständig | [Union All](/de/reference/workflow-steps/tables/table-union-all/) mit einer Ergebniszeile je Prüfung; [Workflow-Fehler auslösen](/de/reference/workflow-steps/workflow-control/raise-workflow-error/), um bei Fehlern anzuhalten | Wertet jede Prüfung über die Eingabe aus und schreibt eine Ergebniszeile je Prüfung mit Status und Meldung. Die Daten werden durchgereicht, und die Ausführung hält an, wenn der Fehlerschwellenwert des Gems erreicht wird. |
| Deequ | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/)-Prüfungen | Reicht Daten durch und erstellt die Ergebnistabelle der Constraints für die Regeln isComplete, isUnique, isNonNegative und isContainedIn. |
| Delta Table Operations | Vollständig | [Table In-Place Delete](/de/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/de/reference/workflow-steps/tables/table-update/), [Table Drop](/de/reference/workflow-steps/tables/table-drop/), [Table Restore to Timestamp](/de/reference/workflow-steps/tables/table-restore-timestamp/) | Löschen, Aktualisieren, Verwerfen und Wiederherstellen auf einen Zeitstempel werden Tabellenschritten zugeordnet; optimize, vacuum und restore nach Version reichen die Daten mit einer Warnung durch. |
| Directory | Vollständig | [Verzeichnisliste](/de/reference/workflow-steps/document/directory-listing/) | Listet die Dateien des gebundenen Dokumentordners in den Spalten des Gems auf; mit der Option für Blattnamen liefert jede Arbeitsmappe eine Zeile je Blatt. Ein fehlender Ordner liefert null Zeilen. |
| Email | Vollständig | [Notify Via Email](/de/reference/workflow-steps/notifications/notify-via-email/) | Sendet die E-Mail, optional mit Datenanhang, über eine gebundene E-Mail-Verbindung. |
| Email Data | Vollständig | [Notify Via Email](/de/reference/workflow-steps/notifications/notify-via-email/) | Sendet die Eingabezeilen als Tabelle per E-Mail und reicht die Eingabe unverändert durch. |
| File Operation | Vollständig | [Copy Document File](/de/reference/workflow-steps/document/copy-document-file/) oder [Copy Document Directory](/de/reference/workflow-steps/document/copy-document-directory/) | Kopiert, verschiebt oder synchronisiert Dateien aus dem gebundenen Dokumentordner in den Dokumentordner des konvertierten Workflows; ein Verschieben entfernt die Quelldateien. |
| Log | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Schreibt die Ereigniszeile des Gems (Zeit, Gem-Name, Ereignistyp und Text) in seine Ausgabetabelle. |
| REST API Enrich | Vollständig | [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) | Ruft die API einmal je Zeile auf und fügt die Antwortspalten hinzu. |
| Script | Vollständig | Python-Schritt mit umgeschriebenem Frame-Zugriff | Bettet den Skriptrumpf in einen Python-Schritt ein, wobei der Data-Frame-Zugriff umgeschrieben wird; Scala-Rümpfe werden mit einem Hinweis übernommen. |
| Soda Data Quality Check | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/)-Prüfungen | Erstellt die Ergebnistabelle der Prüfungen aus den Soda-Checks. |
| SQL Statement | Vollständig | SQL-Schritt je Ausgabe-Registerkarte, Text in den Dialekt des Mandanten übersetzt | Bettet jede Registerkarte als SQL-Schritt ein, wobei Eingaben als temporäre Tabellen gebunden werden; in den Dialekt des Mandanten übersetzt. |
| Todo | Vollständig | [Workflow-Fehler auslösen](/de/reference/workflow-steps/workflow-control/raise-workflow-error/) oder [Notify via Log](/de/reference/workflow-steps/notifications/notify-via-log/) | Markiert noch zu schreibende Logik: eine Protokollmeldung, wenn nichts sie liest, oder ein Schritt, der die Ausführung mit der Meldung des Gems anhält, wenn ein späterer Schritt davon abhängt. |

### Bericht

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Tableau | Vollständig | [Publish to Tableau](/de/reference/workflow-steps/export/export-to-tableau/) | Schreibt einen Hyper-Extrakt und veröffentlicht ihn über die gebundene Tableau-Verbindung. |

### ML/KI

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Bedrock | Vollständig | [Text NLP AI](/de/reference/workflow-steps/text-documents/nlp-ai/) | Erzeugt Embeddings der Textspalte über die KI-Verbindung des Workspace. |
| OpenAI | Vollständig | [Text NLP AI](/de/reference/workflow-steps/text-documents/nlp-ai/) | Beantwortet Fragen oder erzeugt Text-Embeddings über die KI-Verbindung des Workspace. |
| Pinecone Lookup | Vollständig | [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) | Fragt den Pinecone-Index für jede Zeile ab und fügt die Spalten pinecone_matches und pinecone_error hinzu. |
| SageMaker Endpoint | Vollständig | [Text NLP AI](/de/reference/workflow-steps/text-documents/nlp-ai/) | Beantwortet Fragen über die KI-Verbindung des Workspace. |
| Text Processing | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) für die Chunk-Aufteilung; [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) für Web Scraping | Die Chunk-Aufteilung wird zu einem Zeichen-Chunk-Ausdruck; Web Scraping ruft die URL jeder Zeile ab und fügt den Seiteninhalt wieder an die Zeile an. |

### Subgraph/Steuerung

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Control Flow Input | Vollständig | Verworfen (nur Grenzmarkierung) | Verworfen; es markiert nur die Eingabegrenze des Iterator-Unterworkflows. |
| Control Flow Output | Vollständig | Verworfen (nur Grenzmarkierung) | Verworfen; es markiert nur die Ausgabegrenze des Iterator-Unterworkflows. |
| Subgraph (Basic) | Vollständig | Arbeitsflächen-Container / verschachtelter Workflow aus Inline-Prozessen | Konvertiert den Inline-Innengraphen in einen verschachtelten Workflow (oder aufgelöste Schritte) mit Ein-/Ausgabe-Tabellenparametern. |
| Table Iterator | Vollständig | [Workflow Loop](/de/reference/workflow-steps/workflow-control/workflow-loop/) | Führt den Schleifenrumpf einmal je Eingabezeile aus und setzt jeden Konfigurationswert aus seiner Spalte, bis maxIteration. |
| While Iterator | Vollständig | [Workflow Loop](/de/reference/workflow-steps/workflow-control/workflow-loop/) | Führt den Schleifenrumpf einmal je Durchlauf aus und übergibt die Iterationsnummer, bis der Rumpf keine Zeilen mehr zurückgibt oder das Maximum des Gems erreicht ist. |

## SQL-/Analyst-Gems

### Quelle/Ziel

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| External table Source/Target (BigQuery, Databricks, SAP HANA, MongoDB, MSSQL, Oracle, Postgres, Redshift, Salesforce, Snowflake, Synapse) | Vollständig | Import-/Export-Schritt für externe Daten mit der passenden Datenbankverbindung | Liest oder schreibt eine Tabelle in einer externen Datenbank über eine PlaidCloud-Verbindung. |
| File storage Source/Target (ADLS, Databricks Volumes, GCS, OneDrive, S3, SFTP, SharePoint, Smartsheet) | Vollständig | Import-/Export-Dateischritte gegen ein Dokumentenkonto (ADLS/GCS/S3/SFTP/SharePoint/OneDrive) | Liest oder schreibt Dateien in Cloud-/SFTP-Speicher mit Platzhalter-Union, Trigger, Löschen/Verschieben und Verschlüsselungsoptionen. |
| Model | Vollständig | Ausgabetabelle des vorgelagerten Schritts | Liest ein anderes Modell als die Tabelle, die der referenzierte vorgelagerte Schritt erzeugt. |
| Seed | Vollständig | [Import: CSV](/de/reference/workflow-steps/import/import-csv/) | Die Seed-CSV wird in eine PlaidCloud-Tabelle importiert. |
| Source | Vollständig | Import-Schritt, gewählt nach dem Datensatzformat (siehe [Konnektoren](#konnektoren)) | Jede Source wird zu einem Import-Schritt in eine Tabelle, die nach dem Datensatz benannt ist; ein Format, das der Konverter nicht erkennt, wird als CSV-Datei gelesen, die in den Dokumentordner des Workflows hochgeladen wurde, mit einer Warnung. |
| Target Model / Table (Target) | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/), [Upsert](/de/reference/workflow-steps/tables/table-upsert/), [Tabelle kopieren](/de/reference/workflow-steps/tables/table-copy/) und [Union All](/de/reference/workflow-steps/tables/table-union-all/) | Schreibt das abschließende Select des Modells in eine PlaidCloud-Tabelle als replace, append, upsert, delete-and-insert, SCD2 oder replace by predicate. |
| Upload Files | Vollständig | [Import: CSV](/de/reference/workflow-steps/import/import-csv/) | Hochgeladene lokale Dateien werden über einen Import-Schritt zu einer Tabelle. |

### Vorbereiten

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Data Cleansing | Vollständig | Spaltenausdrücke in einem Schritt [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Konvertiert die Optionen für Null-Auffüllung, Trimmen und Groß-/Kleinschreibung in Spaltenausdrücke; bereinigte Spalten wandern ans Ende. |
| Data Masking | Vollständig | Spaltenausdrücke für Zeichenmaskierung oder Hashing | Maskiert oder hasht ausgewählte Textspalten an Ort und Stelle oder als neue Spalten. |
| Find Duplicates | Vollständig | Fensterausdruck mit Zeilennummer plus Filter | Liefert je Schlüssel eindeutige Zeilen, doppelte Zeilen oder nach Anzahl/Position ausgewählte Zeilen. |
| Generate Rows | Vollständig | Sequenztabelle, je Eingabezeile verknüpft und gefiltert | Erzeugt je Eingabezeile Zeilen aus Init-, Bedingungs- und Schleifenausdrücken. |
| Imputation | Vollständig | Aggregat plus Rück-Join und Spaltenausdruck | Ersetzt Nullwerte oder Platzhalterwerte durch Durchschnitt, Median, Modus oder einen festen Wert. |
| Multi-Column Edit | Vollständig | Ausdrücke je Spalte, aus der Vorlage erweitert | Wendet eine Ausdrucksvorlage auf jede ausgewählte Spalte an. |
| Multi-Column Rename | Vollständig | Zuordnung zur Spaltenumbenennung in einem Select-Schritt | Benennt ausgewählte Spalten per Präfix, Suffix oder Namensausdruck um. |
| Record ID | Vollständig | Spaltenausdruck mit Zeilennummer oder UUID | Fügt eine Spalte mit UUID oder fortlaufender Datensatz-ID hinzu. |
| Sample | Vollständig | Zeilenlimit oder Stichprobenoption beim Extrahieren | Nimmt erste/letzte/zufällige/jede n-te Zeilen oder Prozent der Zeilen insgesamt oder je Gruppe. |
| Tile | Vollständig | Fensterausdrücke für Tile-Nummer und Sequenz | Vergibt Tile-Nummern nach gleicher Summe, Anzahl, Standardabweichungsbändern, eindeutigen Werten oder manuellen Grenzen. |

### Transformieren

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Aggregate | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Aggregation; [Pivot](/de/reference/workflow-steps/tables/table-pivot/), wenn das Gem pivotiert | Gruppiert und aggregiert, wendet die HAVING-Bedingung an und pivotiert in eine Spalte je Pivot-Wert; propagate-all übernimmt jede andere Eingabespalte. |
| Count Records | Vollständig | Aggregationsschritt mit Zählfunktionen | Liefert Gesamtanzahl, Anzahl nicht leerer oder eindeutiger Werte als eine Zeile. |
| Data Encoder/Decoder | Vollständig | Spaltenausdrücke für base64-/hex-Kodierung und -Dekodierung | Kodiert oder dekodiert ausgewählte Spalten; AES nur auf Databricks. |
| Deduplicate | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Distinct oder einem Zeilennummernfilter | Behält eine Zeile je Schlüssel: distinct, erste oder letzte nach Ihrer Sortierreihenfolge, beliebige oder nur die Schlüssel, die einmal vorkommen. |
| Dynamic Select | Vollständig | Spaltenauswahl in einem Schritt [Table Extract](/de/reference/workflow-steps/tables/table-extract/), nach Typ aufgelöst | Löst Spalten zum Konvertierungszeitpunkt nach Typ in eine explizite Auswahl auf. |
| Filter | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Filterausdruck | Wird in einen Table-Extract-Schritt mit Filterausdruck konvertiert; NULL-Bedingungen verwerfen die Zeile. |
| Finance | Vollständig | Spaltenausdruck, der die Finanzfunktion umsetzt | Hängt das Ergebnis einer Finanzfunktion (FV, PV, NPV, IRR, ...) als neue Spalte an. |
| Flatten Schema | Vollständig | [JSON parsen](/de/reference/workflow-steps/tables/table-json-parse/) und [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Flacht verschachtelte Felder in Spalten ab, die mit dem Trennzeichen des Gems benannt werden, und zerlegt Arrays in eine Zeile je Element. |
| Fuzzy Match | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) und [User Defined Transform](/de/reference/workflow-steps/general/user-defined-transform/) | Paart die Datensätze, bewertet jedes Abgleichsfeld nach der Methode des Gems, bildet den Durchschnitt der Bewertungen und behält die Paare ab Ihrem Schwellenwert. |
| Limit | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Zeilenlimit | Wird in ein Zeilenlimit konvertiert; Konfigurationsverweise werden zu Projektvariablen. |
| Order By | Vollständig | Sortierung in einem Schritt [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Wird in eine Sortierung mit denselben Schlüsseln, derselben Richtung und derselben Platzierung von Nullwerten konvertiert. |
| Pivot | Vollständig | [Pivot](/de/reference/workflow-steps/tables/table-pivot/) | Wandelt die ausgewählten Pivot-Werte in Aggregatspalten um; eine im Simple-Modus zur Entwurfszeit abgerufene Werteliste wird als die aufgeführten Werte konvertiert. |
| Reformat | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Spaltenausdrücken | Wird in einen Table-Extract-Schritt mit einem Ausdruck je Ausgabespalte konvertiert; nicht aufgeführte Spalten werden verworfen. |
| Running Total | Vollständig | Spalte mit kumulativem Summen-Fensterausdruck | Hängt je ausgewählter Spalte kumulative Summen an. |
| Snowflake Unpivot (third-party) | Vollständig | [Melt](/de/reference/workflow-steps/tables/table-melt/) | Entpivotiert Spalten über Snowflake UNPIVOT. |
| Transpose | Vollständig | [Melt](/de/reference/workflow-steps/tables/table-melt/) | Stapelt Datenspalten in Namens- und Zeichenfolgen-Wertspalten. |
| TransposeAgg | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Aggregation | Konvertiert Gruppierung, Aggregate und Pivot des Gems als Aggregate, mit einer Warnung zur Überprüfung. |
| Unpivot | Vollständig | [Melt](/de/reference/workflow-steps/tables/table-melt/) | Stapelt Datenspalten in Namens- und Wertspalten. |
| Weighted Average | Vollständig | Aggregationsschritt mit Ausdruck für den gewichteten Durchschnitt | Berechnet einen gewichteten Mittelwert insgesamt oder je Gruppe. |
| Window Function | Vollständig | Fensterausdrücke in einem Schritt [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Fügt Fensterspalten mit Partition, Reihenfolge und Frame des Gems hinzu, Zeilen oder Bereich, mit unbegrenzten, zeilenaktuellen oder versetzten Grenzen. |

### Join/Split

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Except | Vollständig | [Anti-Join](/de/reference/workflow-steps/tables/table-anti-join/) über alle Spalten plus ein Distinct-[Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Behält Zeilen der ersten Eingabe, die in keiner der anderen Eingaben vorkommen. |
| Intersect | Vollständig | [Inner Join](/de/reference/workflow-steps/tables/table-inner-join/) über alle Spalten plus Distinct | Behält Zeilen, die in jeder Eingabe vorhanden sind. |
| Join | Vollständig | [Inner Join](/de/reference/workflow-steps/tables/table-inner-join/), [Mehrtabellen-Join](/de/reference/workflow-steps/tables/table-multi-table-join/), [Anti-Join](/de/reference/workflow-steps/tables/table-anti-join/) oder [Cross Join](/de/reference/workflow-steps/tables/table-cross-join/) | Erstellt den Join jedes Typs — inner, left, right, full, semi, anti, cross und natural — über eine beliebige Join-Bedingung, wendet die where-Klausel an und schreibt die Select-Liste. |
| Union | Vollständig | [Union All](/de/reference/workflow-steps/tables/table-union-all/) | Stapelt die Eingaben nach Position und entfernt Duplikate, wenn das Gem sie nicht behält. |
| Union By Name | Vollständig | [Union All](/de/reference/workflow-steps/tables/table-union-all/) | Wird zu einem Union All, das Spalten nach Namen ausrichtet und fehlende mit Null auffüllt. |

### Parsen

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| JSON Parse | Vollständig | [JSON parsen](/de/reference/workflow-steps/tables/table-json-parse/) | Parst eine JSON-Textspalte in strukturierte Felder. |
| Regex | Vollständig | Regex-Ausdrücke in einem Table-Extract-/Transform-Schritt | Ersetzt, parst, vergleicht oder tokenisiert eine Textspalte mit einem regulären Ausdruck. |
| Text To Columns | Vollständig | Schritte zum Aufteilen von Spalten / Explode mit Regex-Trennzeichen | Teilt eine getrennte Spalte mithilfe eines Regex-Trennzeichens in Spalten oder Zeilen auf. |
| XML Parse | Vollständig | [XML parsen](/de/reference/workflow-steps/tables/table-xml-parse/) | Parst eine XML-Textspalte in strukturierte Felder. |

### Benutzerdefiniert

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Directory | Vollständig | [Verzeichnisliste](/de/reference/workflow-steps/document/directory-listing/) | Listet die Dateien des gebundenen Dokumentordners in den Spalten des Gems auf; mit der Option für Blattnamen liefert jede Arbeitsmappe eine Zeile je Blatt. Ein fehlender Ordner liefert null Zeilen. |
| DynamicInput | Vollständig | SQL-Schritt für Abfragevorlagen; Workflow-Schleife für den Mehrdatei-Modus | Der Abfragevorlagen-Modus bettet die Vorlage als SQL-Schritt ein; der Mehrdatei-Modus wird mit Annahmen zugeordnet. |
| Email | Vollständig | [Notify Via Email](/de/reference/workflow-steps/notifications/notify-via-email/) | Sendet die E-Mail, optional mit Datenanhang, über eine gebundene E-Mail-Verbindung. |
| RestAPI | Vollständig | [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) | Sendet eine Anfrage je Eingabezeile mit Ihrer URL, Ihren Headern, Abfrage, Ihrem Body und Wiederholungen, behält die Antwort und fragt eine asynchrone Anfrage ab, bis sie abgeschlossen ist. Die Anmeldedaten stammen aus der Verbindung, die Sie binden. |
| Script | Vollständig | Python-Schritt mit umgeschriebenem Frame-Zugriff | Bettet den Skriptrumpf in einen Python-Schritt ein, wobei der Data-Frame-Zugriff umgeschrieben wird; Scala-Rümpfe werden mit einem Hinweis übernommen. |
| SQL Statement | Vollständig | SQL-Schritt je Ausgabe-Registerkarte, Text in den Dialekt des Mandanten übersetzt | Bettet jede Registerkarte als SQL-Schritt ein, wobei Eingaben als temporäre Tabellen gebunden werden; in den Dialekt des Mandanten übersetzt. |
| StoredProcedure | Vollständig | [Agent Remote Execution of SQL](/de/reference/workflow-steps/agent/agent-remote-execution-of-sql/) | Ruft die Prozedur in ihrem Warehouse über die von Ihnen gewählte Verbindung auf: einmal je Eingabezeile, wobei jedes Argument aus seiner Spalte gebunden wird, oder einmal, wenn sie keine Argumente hat. Die Eingabespalten werden durchgereicht. |
| Table Operations | Vollständig | [Table In-Place Delete](/de/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/de/reference/workflow-steps/tables/table-update/), [Table Drop](/de/reference/workflow-steps/tables/table-drop/) | Update, delete und drop werden Tabellenschritten zugeordnet; vacuum und optimize werden zu einer Tabellenoptimierung oder, mit einer Warnung, zu einem No-op. |
| ToDo | Vollständig | [Workflow-Fehler auslösen](/de/reference/workflow-steps/workflow-control/raise-workflow-error/) oder [Notify via Log](/de/reference/workflow-steps/notifications/notify-via-log/) | Markiert noch zu schreibende Logik: eine Protokollmeldung, wenn nichts sie liest, oder ein Schritt, der die Ausführung mit der Meldung des Gems anhält, wenn ein späterer Schritt davon abhängt. |

### Räumlich

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Buffer | Vollständig | [Spatial Buffer](/de/reference/workflow-steps/spatial/spatial-buffer/) | Vergrößert jede Geometrie um die konfigurierte Entfernung in Meilen oder Kilometern. |
| CreatePoint | Vollständig | [Table Extract](/de/reference/workflow-steps/spatial/spatial-sql-recipes/) mit `geom_point` | Erstellt Punktgeometrie aus Längen- und Breitengradspalten. |
| Distance | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Berechnet Entfernung, Himmelsrichtung und Peilung zwischen zwei WKT-Punkten. |
| FindNearest | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Cross Join | Findet für jeden Quellpunkt die N nächstgelegenen Zielpunkte innerhalb einer maximalen Entfernung. |
| HeatMap | Vollständig | [Heat Map (macro)](/de/reference/workflow-steps/macros/macro-heat-map/) | Ordnet Punkte H3-Hexagonen mit der Auflösung des Gems zu, verteilt die Wärme mit ihrem Abklingen über die Rasterdistanz und liefert Dichte und Umriss jedes Hexagons. |
| PolyBuild | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) und ein Python-Schritt | Erstellt Polygon- oder Polylinien-WKT aus geordneten Punkten je Gruppe. |
| Simplify | Vollständig | [Spatial Generalize](/de/reference/workflow-steps/spatial/spatial-generalize/) | Vereinfacht WKT-Geometrien um eine Toleranz in Meilen/km. |
| SpatialMatch | Vollständig | [Räumlicher Abgleich](/de/reference/workflow-steps/spatial/spatial-match/) | Gleicht Quell- und Zielgeometrien nach intersects/contains/within/touches/envelope ab. |

### Bericht

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| PowerBIWrite | Vollständig | [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) | Erstellt das Power-BI-Dataset und überträgt die Zeilen über die Power BI REST API. |
| TableauWrite | Vollständig | [Publish to Tableau](/de/reference/workflow-steps/export/export-to-tableau/) | Schreibt einen Hyper-Extrakt und veröffentlicht ihn über die gebundene Tableau-Verbindung. |
| Visualize | Vollständig | [Tabelle kopieren](/de/reference/workflow-steps/tables/table-copy/) | Reicht die Zeilen unverändert weiter; erstellen Sie das Diagramm als PlaidCloud-Dashboard auf derselben Tabelle. |

### Subgraph/Steuerung

| Gem | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Condition | Vollständig | [Cross Join](/de/reference/workflow-steps/tables/table-cross-join/) und [Table Extract](/de/reference/workflow-steps/tables/table-extract/) | Wertet die Bedingungen über die gesamte Eingabe aus und sendet jede Zeile an die erste Ausgabe, deren Bedingung zutrifft, sonst an die letzte Ausgabe. |
| Macro | Vollständig | SQL-Schritt mit aufgelöstem Makro-Rumpf | Bettet den Makro-Rumpf als in den Dialekt des Mandanten übersetzten SQL-Schritt ein, mit als temporäre Tabellen gebundenen Eingaben. |
| Pipeline (trigger) | Vollständig | [Workflow Loop](/de/reference/workflow-steps/workflow-control/workflow-loop/) | Führt die benannte Pipeline einmal je Eingabezeile mit Ihren Parametern und Ihrer Trigger-Bedingung aus, fährt nach einer fehlgeschlagenen Ausführung fort und liefert eine Zeile je Ausführung. |
| Subgraph (Basic) | Vollständig | Arbeitsflächen-Container / verschachtelter Workflow aus Inline-Prozessen | Konvertiert den Inline-Innengraphen in einen verschachtelten Workflow (oder aufgelöste Schritte) mit Ein-/Ausgabe-Tabellenparametern. |

## Konnektoren

Datensatzformate und Konnektoren sind Quell- und Zieleinstellungen eines Gems, keine Gems. Jedes Format wird in den angegebenen Import- oder Exportschritt konvertiert, und die Konvertierung kontaktiert nie das Quell- oder Zielsystem.

| Format | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Avro | Vollständig | Import: [Avro](/de/reference/workflow-steps/import/import-avro/); Export: [Avro](/de/reference/workflow-steps/export/export-to-avro/) | Liest und schreibt Avro-Dateien. |
| BigQuery | Vollständig | Externe Datenbankverbindung mit Tabellenimport | Liest und schreibt über eine Verbindung. |
| Binary files | Vollständig | [Verzeichnisliste](/de/reference/workflow-steps/document/directory-listing/) mit Dateiinhalten; [Alteryx-Executor](/de/reference/workflow-steps/general/alteryx-executor/) zum Schreiben | Liest jede Datei des Ordners mit Pfad, Änderungszeit, Länge und Inhalt; schreibt den Inhalt jeder Zeile in die Datei, die ihr Pfad benennt. |
| Catalog table | Vollständig | Bindung an eine vorhandene PlaidCloud-Tabelle | Bindet per Namen an eine Tabelle; Lesen und jeder Schreibmodus werden konvertiert. |
| Cosmos DB | Vollständig | Import und Export: [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) | Liest und schreibt die Dokumente des Containers über Ihre Cosmos-DB-Verbindung. |
| CSV | Vollständig | [Import: CSV](/de/reference/workflow-steps/import/import-csv/); Export: CSV | Liest und schreibt getrennte Dateien mit Optionen für Header, Trennzeichen, Anführungszeichen, Escape und Kodierung. |
| Data Generator | Vollständig | [Table Faker](/de/reference/workflow-steps/tables/table-faker/) | Erzeugt die Spalten des Datensatzes mit denselben Arten von Fake-Daten. |
| DataHub table | Vollständig | [SQL importieren](/de/reference/workflow-steps/import/import-sql/) | Liest die Tabelle, die der Datensatz benennt, über Ihre Verbindung; ein Schreibvorgang landet in einer PlaidCloud-Tabelle. |
| Delta | Vollständig | Bindung an eine vorhandene PlaidCloud-Tabelle | Liest und schreibt die Tabelle in jedem Schreibmodus; das Lesen einer früheren Version erfolgt über die Databricks-Verbindung, die Sie binden. |
| Excel (XLSX) | Vollständig | Import: Excel; Export: Excel | Liest und schreibt Blätter und Bereiche von Arbeitsmappen. |
| Fixed format | Vollständig | Import: [Feste Breite](/de/reference/workflow-steps/import/import-fixed-width/); Export: [CSV](/de/reference/workflow-steps/export/export-to-csv/) | Liest Dateien mit fester Breite, deren Layout sich aus den Spaltenbreiten des Datensatzes ergibt; schreibt eine getrennte Datei. |
| Hive | Vollständig | Import: [SQL importieren](/de/reference/workflow-steps/import/import-sql/); Export: [Externe Tabellen](/de/reference/workflow-steps/export/export-external-tables/) | Liest und schreibt die Tabelle über Ihre Hive-Verbindung. |
| Iceberg | Vollständig | Bindung an eine vorhandene PlaidCloud-Tabelle | Liest und schreibt die Tabelle. |
| JDBC | Vollständig | Externe Datenbankverbindung mit Tabellenimport | Liest eine Tabelle oder Abfrage und schreibt im Replace- oder Append-Modus über Ihre Verbindung; eine Anweisung nach dem Schreiben wird nach dem Schreibvorgang ausgeführt. |
| JSON | Vollständig | [JSON parsen](/de/reference/workflow-steps/tables/table-json-parse/) | Lädt Datensätze und flacht verschachtelte Felder ab. |
| Kafka | Vollständig | Import: [Kafka importieren](/de/reference/workflow-steps/import/import-kafka/); Export: [Kafka exportieren](/de/reference/workflow-steps/export/export-kafka/) | Liest ein Topic als einen Batch von Nachrichten und schreibt Zeilen als Nachrichten. |
| MongoDB | Vollständig | Import: [MongoDB](/de/reference/workflow-steps/import/import-mongodb/); Export: [MongoDB](/de/reference/workflow-steps/export/export-mongodb/) | Liest und schreibt die Collection über Ihre MongoDB-Verbindung. |
| ORC | Vollständig | Import: [ORC](/de/reference/workflow-steps/import/import-orc/); Export: ORC | Liest und schreibt ORC-Dateien. |
| Parquet | Vollständig | Import: Parquet; Export: Parquet | Liest und schreibt Parquet-Dateien. |
| Pinecone | Vollständig | Import und Export: [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) | Liest die Datensätze eines Index und führt Upserts von Zeilen als Vektoren über die Pinecone REST API durch. |
| Redshift | Vollständig | Externe Datenbankverbindung mit Tabellenimport | Liest und schreibt über eine Verbindung. |
| Salesforce | Vollständig | Import: [Query Salesforce Object](/de/reference/workflow-steps/salesforce/query-salesforce-object/); Export: [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) | Liest ein Objekt oder eine SOQL-Abfrage und schreibt Datensätze über Ihre Salesforce-Verbindung. |
| Seed (inline) | Vollständig | [Import: CSV](/de/reference/workflow-steps/import/import-csv/) | Lädt die Inline-Zeilen als Tabelle. |
| Slack | Vollständig | Import: [Singer](/de/reference/workflow-steps/import/import-singer/); Export: [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) | Liest Kanalnachrichten und postet jede Zeile als Nachricht über Ihre Slack-Verbindung. |
| Smartsheet | Vollständig | Import und Export: [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) | Liest und schreibt die Zeilen des Sheets über Ihre Smartsheet-Verbindung. |
| Snowflake | Vollständig | Externe Datenbankverbindung mit Tabellenimport | Liest und schreibt über eine Verbindung. |
| SQL file types (CSV, Excel, JSON, Parquet, Text, XML, fixed-width) | Vollständig | Import- und Export-Dateischritte gegen ein Dokumentenkonto | Liest und schreibt den Dateityp; Optionen ohne PlaidCloud-Äquivalent werden gekennzeichnet. |
| Text | Vollständig | [Import: CSV](/de/reference/workflow-steps/import/import-csv/) als einzelne Spalte | Liest jede Zeile als eine Spalte. |
| Web page | Vollständig | [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) | Liest die Seite unter der URL des Datensatzes in eine Tabelle. |
| XML | Vollständig | [XML parsen](/de/reference/workflow-steps/tables/table-xml-parse/) | Lädt Datensätze nach Zeilen-Tag. |

## Ausdrücke und Projektstruktur

| Bereich | Status | PlaidCloud-Äquivalent | Konvertierung |
| --- | --- | --- | --- |
| Expressions | Vollständig | Spark- und Warehouse-SQL-Ausdrücke, Funktion für Funktion übersetzt | Funktionen und Operatoren werden in PlaidCloud-Ausdrücke konvertiert; eine Funktion ohne Äquivalent wird namentlich gekennzeichnet. |
| Project and graph structure | Vollständig | Projekt-Loader | Jede Prophecy-Exportform wird geladen und in ein Modell normalisiert. |

## Bekannte Sonderfälle

| Fall | Was geschieht |
| --- | --- |
| Code oder Daten, die der Export nicht enthält | Ein Gem Builder oder ein anderes benutzerdefiniertes Gem, dessen Code nicht im Export enthalten ist, und der Aufruf eines Makros eines dbt-Pakets, das der Export auslässt, werden zu einem Schritt, der benennt, was fehlt; exportieren Sie das Projekt mit seinem Pipeline-Code und den dbt-Paketen oder bauen Sie die Logik in einem Python- oder SQL-Schritt nach. Ab-Initio-Gems für Error Detection und MTime reichen ihre Eingabe durch, weil die Regel, die sie anwenden, nicht im Export enthalten ist. Soda-Checks, die aus einer Datei außerhalb des Projekts lesen, und Soda-Checks, die mit früheren Scans oder mit einem anderen Datensatz vergleichen oder ein von Soda benanntes Format prüfen, haben keine Zeile in der Ergebnistabelle; berechnen Sie sie in einem späteren Schritt. |
| Ergebnisse, die erst bekannt sind, wenn die Pipeline läuft | Ein REST-API-Gem, das seine Antwort abflacht, legt die gesamte Antwort in eine Spalte, wenn nichts die Feldnamen deklariert, was erst eine Ausführung offenbart; extrahieren Sie die benötigten Felder in einem späteren Schritt. Ein dbt-Makro, das das Warehouse abfragt, während dbt kompiliert, wird zu einem Schritt, der es benennt; ersetzen Sie die Abfrage durch die Werte, die sie zurückgibt. Ein Spark-StoredProcedure-Gem wird ausgeführt, aber seine OUT-Werte werden nicht zurückgegeben; die Ausgabe sind die durchgereichten Spalten. `input_file_name()` liefert über einer Tabellen- oder Delta-Quelle, die keine Datei zu benennen hat, eine leere Zeichenfolge, und `hash()` / `xxhash64()` innerhalb eines Aggregats, eines Fensters oder eines Gems mit mehreren Eingaben werden vom Warehouse berechnet, sodass sie von Spark abweichen können. |
| Werte, die bei der Konvertierung des Projekts in einen Schritt geschrieben werden | Ein Parameterwert mit Anführungszeichen, Backslash oder geschweifter Klammer, ein Pipeline-Wert, den ein SQL-Schritt liest, und die Datenbank, die eine Delta-Tabellenoperation über die Konfiguration benennt, werden als feste Werte in den Schritt geschrieben, sodass eine Änderung der Workflow-Variablen sie nicht ändert; bearbeiten Sie den Schritt, wenn sich die Konfiguration ändert. |
| Scala-Code | Ein Scala-Skript, ein Scala-Ausdruck oder eine benutzerdefinierte Scala-Funktion oder Aggregatfunktion wird zu einem Schritt, der sie benennt; schreiben Sie sie in SQL oder Python neu. |
| Kafka-Kerberos-Anmeldung | Eine Kafka-Quelle oder ein Kafka-Ziel, das sich per Kerberos (GSSAPI) anmeldet, wird ohne den Kerberos-Dienstnamen und den Anmeldemechanismus konvertiert; legen Sie sie in der PlaidCloud-Verbindung fest. |
| Streaming | Streaming-Quellen, -Ziele und -Pipelines werden als Batch-Workflows über die zum Zeitpunkt der Ausführung vorhandenen Daten ausgeführt; planen Sie den Workflow so oft ein, wie Sie ihn benötigen. |
| Job-Komponenten | Ein Spark-Job wird mit seiner einen Pipeline und seinem Zeitplan konvertiert; seine anderen Komponenten, Ausführungsbedingungen und Konfigurationsüberschreibungen werden nicht konvertiert. |
| Seltene Aufrufe | Eine benutzerdefinierte Aggregatfunktion, die aus einem Rollup oder einem Fenster aufgerufen wird, und ein dbt-Makro, das Jinja über if, for, set und die gängigen Filter hinaus verwendet, werden zu einem Schritt, der das Gem benennt; rufen Sie die Funktion aus einem Aggregate-Gem auf oder lösen Sie das Makro inline auf. |

## Einen konvertierten Workflow validieren

Vergleichen Sie die Ausgabe des konvertierten Workflows mit der Ausgabe Ihrer eigenen Prophecy-Pipeline: Schema, Zeilenanzahl und Zeilenwerte. Ignorieren Sie die Zeilenreihenfolge, sofern der Workflow nicht von ihr abhängt.
