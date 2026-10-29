---
title: Savant-Konvertierungsmatrix
description: Wie PlaidCloud Savant-Labs-Analysen in native erweiterte Workflows konvertiert, mit der Zuordnungsstufe jedes Agents und den wenigen genannten Sonderfällen.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/savant-conversion-matrix.md
---

PlaidCloud konvertiert Savant-Labs-Analysen in native erweiterte Workflows. Der
Importer ordnet jeden Savant-Agent einem Workflow-Schritt, einer Projektvariable oder
einem Objekt auf der Arbeitsfläche zu, sodass ein konvertierter Workflow Cloud-nativ ausgeführt wird.

Informationen zum Durchführen einer Konvertierung finden Sie unter [Savant-Analysen migrieren](/de/guides/workflows/migrate-savant-analyses/).

Jeder Agent hat eine Zuordnungsstufe. **Vollständig** bedeutet, dass jede Option des Agents eine
gültige Zuordnung zu einem PlaidCloud-Schritt hat. Konstrukte, die ausdrücklich abgelehnt werden, sind
unter „Ausdrücklich abgelehnte Konstrukte“ aufgeführt.

Konnektoren zu externen Systemen werden **verbunden, nicht konvertiert**. Siehe
[Verbindung zu externen Systemen](#verbindung-zu-externen-systemen).

## Agent-Unterstützung

Alle 33 Agents werden vollständig konvertiert.

| Agent | Stufe | PlaidCloud-Äquivalent | Konvertiert |
| --- | --- | --- | --- |
| Adapter Agent (`adapter`) | Vollständig | Schritt für Auswahl und Schemaprojektion | Benennt Felder um, ändert ihre Typen und sortiert sie. |
| API / Infer Agent (legacy service) (`service`) | Vollständig | Wie der API Agent oder Infer Agent, je nach serviceType | Ein LLMService wird als Infer Agent und ein APIService als API Agent konvertiert; ein fehlender oder falsch geschriebener serviceType wird mit einer Warnung aus den Schlüsseln des Knotens gelesen. |
| API Agent (`apiService`) | Vollständig | Table Extract, [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) und ein Left Join zurück | Eine GET-, POST-, PUT-, PATCH- oder DELETE-Anfrage pro Eingabezeile; der rohe Antworttext landet in einer Textspalte, HTTP-Fehler bleiben als Zeilen erhalten, jede Eingabezeile bleibt erhalten, und ein Kontingent pro Zeitraum wird zu einer gebrochenen Anzahl Anfragen pro Sekunde. Eine relative URL wird mit der Basis-URL aus api_bindings oder dem Host der REST-Verbindung verbunden; ein Host, Port oder Pfad aus einem Zeilenfeld wird pro Zeile eingesetzt; Paginierung über next-URL, Link-Header, Offset und Seite wird verfolgt, einschließlich eines Starts, einer Seitengröße oder eines Parameternamens, die aus einem Zeilenfeld vorlagenbasiert eingesetzt werden. |
| Blend Agent (`blend`) | Vollständig | [Inner Join](/de/reference/workflow-steps/tables/table-inner-join/), [Outer Join](/de/reference/workflow-steps/tables/table-outer-join/), [Anti-Join](/de/reference/workflow-steps/tables/table-anti-join/) | Inner-, Left-, Right-, Full-, Anti- und Outer-excluding-Inner-Blends, ODER-verknüpfte Bedingungen sowie „contains“- und „is part of“-Bedingungen, mit Datenströmen für Treffer und Nichttreffer; Spalten, die ein Pivot oder Parse erst zur Laufzeit benennt, werden durchgereicht. |
| Dedupe Agent (`deduplicate`) | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit eindeutigen Zeilen | Behält pro Schlüssel den ersten Datensatz, innerhalb von Gruppieren-nach-Gruppen, und leitet Duplikate in einen zweiten Datenstrom um oder markiert sie. |
| Destination Agent (`destination`) | Vollständig | [Export: CSV](/de/reference/workflow-steps/export/export-to-csv/), [Export: Excel](/de/reference/workflow-steps/export/export-to-excel/), Export: Parquet, JSON, Avro oder XML, [Export to PDF](/de/reference/workflow-steps/export/export-to-pdf/), [Export: Tableau Hyper](/de/reference/workflow-steps/export/export-hyper/) mit [Publish to Tableau](/de/reference/workflow-steps/export/export-to-tableau/), [Export: External Database Tables](/de/reference/workflow-steps/export/export-external-tables/), [Export to Google Spreadsheet](/de/reference/workflow-steps/export/export-to-google-spreadsheet/), [Notify via Slack](/de/reference/workflow-steps/notifications/notify-via-slack/) oder E-Mail | Schreibt über destination_bindings in ein Dokumentenkonto (CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF oder ein Tableau-.hyper, in jedem Java-Zeichensatz, einschließlich Aliasen, CESU-8 und Formen mit Byte-Order-Mark; ein Zeichen, das dem Zeichensatz fehlt, wird als ? geschrieben), in eine Verbindungstabelle, ein Google Sheet, eine Tableau-Datenquelle oder einen Slack-Kanal bzw. an E-Mail-Empfänger. Ein ungebundenes Ziel schreibt stattdessen in eine Projekttabelle oder eine Document-Datei (siehe „Wohin es geht“ weiter unten). Eine Datei, ein Unterordner oder eine Registerkarte pro Feldwert teilt CSV-, Excel-, Parquet- und PDF-Dateien sowie Google-Sheets-Registerkarten auf; eine Vorlage dient als Ausgangspunkt für jede Arbeitsmappe einer Aufteilung. Excel-Optionen werden zugeordnet: Leere Werte gehen nach `Sheet1`, kollidierende Blattnamen erhalten ein Suffix, `formatFromTemplate`, `topLeftCell` und der Modus `create`. Append, upsert, update und groupReplace führen anhand der Abgleichsschlüssel zusammen (eine Datei oder Tabelle wird zurückgelesen und neu geschrieben; bei einer Aufteilung wird die Datei zurückgelesen, in die jeder Wert der Ausführung geschrieben wird, und innerhalb dieser Datei zusammengeführt, wobei die übrigen Dateien unverändert bleiben; Tableau aktualisiert seine Zeilen direkt). Spalten, die nur die Daten benennen (die Kopfzeile nach einer Kopfzeilen-Heraufstufung, die Werte eines Pivots, die Schlüssel eines geparsten JSON oder XML), werden bei jedem Export und jedem Tabellenschreibvorgang neben den bekannten Spalten geschrieben, danach sortiert und aufgeteilt und an eine Tabelle angehängt oder darin zusammengeführt, bzw. in eine Datei, die mit allen ihren Spalten zurückgelesen wird. |
| Explode Agent (`explode`) | Vollständig | [Cross Join](/de/reference/workflow-steps/tables/table-cross-join/) | Bildet das Kreuzprodukt einer kleinen Seite mit dem Hauptdatenstrom. |
| Filter Agent (`filter`) | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit einem Filterausdruck | Teilt Datensätze per Assistent oder Ausdruck in Wahr- und Falsch-Pfade auf. |
| Filter Pushdown (`pdfilter`) | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit einem Filterausdruck | Datenbankseitiger Filter, konvertiert wie Filter. |
| Format Agent (`format`) | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Spaltenumbenennungen oder Promote Header | Blendet Felder aus, ändert ihre Typen, benennt sie um und füllt sie, wenn sie nach Namen (enthält, beginnt mit, endet mit) oder durch Leersein ausgewählt werden; ein Füllvorgang schreibt seinen Standardwert in jede Spalte, in deren Typ sich der Standardwert umwandeln lässt (Text, Zahl, Datum). Die Heraufstufung der Kopfzeile und der Abgleich auf „ist leer“ laufen zur Laufzeit im Schritt Promote Header, und eine heraufgestufte Kopfzeile liest jede Spalte ihrer Datei. |
| Fuse Agent (`fuzzy_match`) | Vollständig | [Fuzzy Match](/de/reference/workflow-steps/tables/table-fuzzy-match/), zwischen einem Union All und zwei Joins | Stapelt beide Eingaben, gleicht Datensätze anhand der Schlüsselfelder mit einem Ähnlichkeitsschwellenwert von 80 ab und verbindet beide Seiten mit einem Konfidenzwert wieder zurück. |
| Group (`group`) | Vollständig | Container auf der Arbeitsfläche | Bleibt als Workflow-Organisation erhalten. |
| Infer Agent (`gen_ai`) | Vollständig | Prompt-Aufgabe von [AI/NLP](/de/reference/workflow-steps/text-documents/nlp-ai/) | Der Prompt läuft pro Zeile über die Eingabefelder auf der sichtbaren LLM-Verbindung, die dem Anbieter und Modell von Savant entspricht; die Antwort landet neben jeder Eingabespalte in einer Spalte „AI Answer“. rowLimit begrenzt die pro Ausführung beantworteten Zeilen und behält frühere Antworten: Eine bereits beantwortete Zeile (gleicher Prompt, gleiches Modell und gleiche Eingabewerte) behält ihre Antwort, und nur unbeantwortete Zeilen zählen zum Limit. |
| JSON Agent (`json`) | Vollständig | [JSON parsen](/de/reference/workflow-steps/tables/table-json-parse/) | Flacht ein JSON-Feld in Spalten mit Schlüsseln in Punktnotation ab oder zerlegt ein Array in eine Zeile pro Element; die Schlüssel werden zur Laufzeit aus den Daten gelesen. |
| Notes Agent (`notes`) | Vollständig | Anmerkung auf der Arbeitsfläche | Bleibt als Workflow-Kontext erhalten. |
| Pivot Agent (`pivot`) | Vollständig | [Pivot](/de/reference/workflow-steps/tables/table-pivot/) | Pivotiert Zeilen mit Aggregation in Spalten. |
| Recursion Agent (`hierarchy`) | Vollständig | Hierarchy Closure, [Table Extract](/de/reference/workflow-steps/tables/table-extract/) und [Mehrtabellen-Join](/de/reference/workflow-steps/tables/table-multi-table-join/) | Durchläuft einen Eltern-Kind-Baum bis zu beliebiger Tiefe, aggregiert jeden Knoten über die IDs auf seinem Pfad zur Wurzel, ihn selbst eingeschlossen, und schreibt Depth und Path; eine Schleife endet am wiederholten Knoten. |
| Sample Agent (`sample`) | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit einem Zeilenlimit | Behält die ersten N Zeilen, optional pro Gruppe, einen zufälligen Prozentsatz oder N Zeilen, oder jede N-te Zeile. |
| Search and Replace (`search_replace`) | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit verschachtelten Ersetzungsausdrücken, auf Phasen verteilt | Suchen-und-Ersetzen-Regeln (enthält oder entspricht; ersetzen oder anhängen), mit oder ohne Beachtung der Groß-/Kleinschreibung, ganzes Wort oder nicht, der Reihe nach auf die gewählten Textfelder angewendet, oder auf jedes Textfeld, wenn keines benannt ist. |
| Source Agent (`source`) | Vollständig | Import-Schritte, gebunden über `source_bindings` ([Import: CSV](/de/reference/workflow-steps/import/import-csv/), [Import: Excel](/de/reference/workflow-steps/import/import-excel/), [Import: SQL](/de/reference/workflow-steps/import/import-sql/)), oder eine vorhandene Tabelle | Liest die gebundene Tabelle oder das gebundene Dokument; eine ungebundene Quelle erzeugt einen leeren Import und eine Warnung. XML-Text liest sein Dokument über XML importieren (ein ungebundener liest savant/<workflow>/<name>.xml). Eine an ein XML-Dokument gebundene Quelle schreibt auch die übrigen Spalten des Exports: eine Spalte mit Dateiname oder Pfad aus dem Dokument, der Rest bleibt leer. Eine Quelle unterhalb eines Format, das eine Kopfzeile heraufstuft, liest jede Spalte ihrer CSV-, Excel- (einschließlich Excel 97 .xls), JSON-, Parquet- oder Avro-Datei nach Position. |
| Spatial Match Agent (`spatial_match`) | Vollständig | [Räumlicher Abgleich (executor)](/de/reference/workflow-steps/spatial/spatial-match-executor/), [Cross Join](/de/reference/workflow-steps/tables/table-cross-join/) oder [Nächstgelegene finden](/de/reference/workflow-steps/spatial/spatial-find-nearest/) | Intersects, within, contains, touches, crosses, overlaps, equals, disjoint sowie Abgleiche mit mehreren Regeln per UND/ODER, geodätisch „innerhalb der Entfernung“ zwischen beliebigen Geometrien (Punkte, Linien, Polygone: die geringste Entfernung auf einer Kugel mit 6371 km), die nächsten N nach derselben Entfernung mit einer Maximalentfernung (eine einzelne Nearest-Regel schreibt keine Spalte Distance, da Savant keine schreibt; in Kombination mit anderen Regeln als Nearest-dann-Filter, UND-Joins und ODER-Vereinigungen fügt jede Nearest-Regel eine eigene Spalte Distance hinzu) und Cross, mit Datenströmen für Treffer und Nichttreffer. |
| Spatial Summarize Agent (`spatial_summarize`) | Vollständig | [Räumlich kombinieren](/de/reference/workflow-steps/spatial/spatial-combine/), Spatial Centroid und Schritte für Punkt zu Linie | Vereinigung, Schnittmenge, Begrenzungsrahmen, ein oder mehrere geometrische Zentren sowie Polylinien- oder Polygon-Aufbau, pro Gruppe mit optionaler Sortierung. |
| Split Agent (`split`) | Vollständig | Split Text oder [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit split_part-Spalten | Teilt ein Textfeld an einem literalen Trennzeichen beliebiger Länge in Zeilen oder Spalten auf, mit Trim und Beibehalten des Originals; die Anzahl der Spalten wird zur Laufzeit aus den Daten gelesen. |
| Split Output (`outlet`) | Vollständig | Workflow-Kante | Leitet eine benannte Ausgabe an ihre Verbraucher weiter. |
| Stack Agent (`multi_stack`) | Vollständig | [Union All](/de/reference/workflow-steps/tables/table-union-all/) | Stapelt beliebig viele Eingaben nach Name oder Position. |
| Summarize Agent (`summarize`) | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Aggregation | Gruppiert und aggregiert, einschließlich first/last nach einer deterministischen Sortierung und zeilenweiser Fensteraggregate (useWindow). |
| Summarize Pushdown (`pdsummarize`) | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Aggregation | Datenbankseitige Aggregation, konvertiert wie Summarize. |
| Text (`text`) | Vollständig | Anmerkung auf der Arbeitsfläche | Bleibt als Workflow-Kontext erhalten. |
| Time Series Agent (`rollup`) | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/)-Aggregation über einen Periodenintervall-Ausdruck, Period Spine, [Anti-Join](/de/reference/workflow-steps/tables/table-anti-join/) und [Union All](/de/reference/workflow-steps/tables/table-union-all/) | Verdichtet Datensätze pro Gruppe auf Tages-, Wochen-, Monats-, Quartals-, Jahres- oder Jahrzehntperioden zwischen optionalen Start- und Enddaten, schließt NULL-Datumswerte aus und füllt leere Perioden mit Nullen. |
| Transform Agent (`edit`) | Vollständig | [Table Extract](/de/reference/workflow-steps/tables/table-extract/) mit Spaltenausdrücken | Berechnete Spalten, Typänderungen und Fensterberechnungen (lag, lead, kumulierte Summe, Zeilennummer, Vorwärts- und Rückwärtsauffüllung), der Reihe nach ausgewertet. Ein Edit, der nur seine kompilierten Schritte enthält, wird als diese Schritte konvertiert, der Reihe nach angewendet, wobei jeder den nächsten speist. |
| Unpivot Agent (`unpivot`) | Vollständig | [Melt](/de/reference/workflow-steps/tables/table-melt/) | Wandelt Spalten als Name/Wert-Paar in Zeilen um. |
| Vision Agent (`vision`) | Vollständig | [Image OCR](/de/reference/workflow-steps/text-documents/image-ocr/), dann die Prompt-Aufgabe von [AI/NLP](/de/reference/workflow-steps/text-documents/nlp-ai/) | Jedes Dokument geht als Bild oder PDF an den Anbieter, wenn dieser Typ und Größe akzeptiert; andernfalls wird seine PDF-Textebene oder der OCR-Text gesendet; die Antwort des Prompts landet in einer Spalte „AI Answer“. |
| XML Agent (`xml`) | Vollständig | [XML parsen](/de/reference/workflow-steps/tables/table-xml-parse/) | Wählt Elemente aus, extrahiert untergeordnete Werte und Attribute in Spalten oder konvertiert XML in JSON; ein einfacher //a/b-Pfad wird wie bisher konvertiert, und jeder andere XPath-1.0-Pfad (Prädikate, Attributtests, Platzhalter, Funktionen wie count(), name() und contains()) wird als XPath ausgewertet, namespace-bewusst oder wie geschrieben. |

Verdrahtungs-, Arbeitsflächen- und Pushdown-Varianten (Split Output, Group, Text, Filter Pushdown, Summarize Pushdown) sind Savant-Knotentypen ohne eigenen Help-Center-Artikel zum Agent; jede wird als der Agent konvertiert, den sie widerspiegelt.

Eine Anmeldeinformation in einer API-Agent-Anfrage wird nie in einen Workflow-Schritt kopiert. Über https wandert sie in eine REST-Verbindung; über http, ohne Berechtigung zum Schreiben von Verbindungen oder bei einer über MCP durchgeführten Konvertierung wird sie mit einer Warnung zurückgehalten. Das ist beabsichtigt und senkt die Stufe nicht.

Zwei Einschränkungen bei Zielen senken die Stufe nicht. Einige seltene Zeichensätze (zum Beispiel `x-ISCII91` oder `JIS_X0212`) lassen sich nicht schreiben; die Datei wird als UTF-8 geschrieben, und die Konvertierung gibt eine Warnung aus. Eine Tableau-Veröffentlichung, die anhand von Schlüsseln zusammenführt, benötigt `replace: true` in ihrer Zielbindung; ohne diese warnt die Konvertierung und veröffentlicht eine neue Datenquelle, was bei einer Ausführung fehlschlägt, in der bereits eine existiert.

## Ausdrücklich abgelehnte Konstrukte

Acht Konstrukte werden ausdrücklich abgelehnt, statt konvertiert zu werden. Keines senkt die Stufe eines Agents.

| Konstrukt | Warum es abgelehnt wird |
| --- | --- |
| Eine API-Agent-Anfrage, die eine Anmeldeinformation mitführt und ihren Host aus einem Eingabefeld bezieht | Jede Zeile könnte die Anmeldeinformation an einen Host senden, den die Daten bestimmen. Die Anfrage wird zu einem benannten Platzhalter. Eine Anfrage ohne Anmeldeinformation und eine Anmeldeinformation auf einem festen Host werden konvertiert. |
| Ein Transform-Edit ohne Ausdruck und ohne kompilierte Schritte, etwa ein Copilot-Edit, der nur seinen Prompt enthält | Es gibt nichts zu konvertieren: Ein Prompt ist keine Formel. Ein Edit mit kompilierten Schritten wird konvertiert. |
| Ein Regex-Konstrukt in einem Transform- oder Filter-Ausdruck, das PlaidCloud nicht lesen kann: eine Klasse in einer Klasse, eine Klassenschnittmenge (`&&`) oder eine unbekannte `\p{}`-Eigenschaft | Der Schritt wird zu einem benannten Platzhalter, der zur Laufzeit abgelehnt wird. |
| Eine Aggregat- oder Fensterfunktion in einem Transform- oder Filter-Ausdruck | Savant selbst schlägt damit zur Laufzeit fehl. Als Transform-Berechnung oder in einem Summarize wird sie konvertiert. |
| `HASH` in einem Transform- oder Filter-Ausdruck mit einem literalen Algorithmus außer `md5` oder `sha1` | Savant selbst schlägt damit fehl (der Algorithmus ist `md5` oder `sha1`). Ein aus einer Spalte gelesener Algorithmus wird konvertiert und liefert für jeden anderen Wert NULL. |
| Eine Zielsortierung nach einer Spalte, die ihre Eingabe nicht enthält | Savant selbst schlägt damit zur Laufzeit fehl. |
| Eine Zieldatei, ein Zielunterordner, eine Zielregisterkarte oder ein Zielarbeitsblatt pro Wert einer Spalte, die ihre Eingabe nicht enthält | Savant selbst schlägt damit zur Laufzeit fehl. |
| Ein XML-Agent-Pfad, der kein XPath 1.0 ist | Savant kann ihn ebenfalls nicht ausführen. |

Eine relative API-URL wird konvertiert, wenn Sie mit `api_bindings` eine Basis-URL oder REST-Verbindung binden; siehe [Bindungen zur Konvertierungszeit](/de/guides/workflows/migrate-savant-analyses/#bindungen-zur-konvertierungszeit).

## Ausdruckssprache

Savant-Ausdrucksfunktionen und -Operatoren werden in PlaidCloud-Ausdrücke konvertiert. Stufe: **Vollständig**. Jede Funktion und jedes Format wird konvertiert, einschließlich `TO_TEXT` mit einem numerischen Muster, einem Format, das erst pro Zeile bekannt ist, Datumstoken für Sekundenbruchteile, wochenbasierte, Quartals- und Zonen-Token, zweistellige Jahre und Java-Regex-Konstrukte. GEO_*-Funktionen an beliebiger Stelle in einem Ausdruck laufen in begleitenden Spatial-Schritten. Die Ausnahmen sind die [ausdrücklich abgelehnten Konstrukte](#ausdrücklich-abgelehnte-konstrukte).

Bekannte Sonderfälle: `TO_DATE` oder `TO_DATETIME` mit einem Format, das ein Literal `[`, `]`, Anführungszeichen, Backslash oder `^` enthält, bei Text, der als 9999-12-30 oder 9999-12-31 gelesen wird, was nach dem letzten Zeitstempel liegt, den das Warehouse speichert; die Konvertierung gibt eine Warnung aus.

## Exportformate

Der Loader akzeptiert jede Savant-Exportform — flach, modellumhüllt, Serverdatensatz, Rezept-Umschlag, arrayumhüllt, mit BOM-Präfix und veraltete Typ-Aliase — und normalisiert sie zu einem einzigen Modell. Stufe: **Vollständig**.

## Analyseparameter

Savant-Analyseparameter werden in Workflow-Variablen konvertiert, und Verweise darauf innerhalb von Knotenkonfigurationen werden in die PlaidCloud-Variablensyntax umgeschrieben. Parameterformen als Liste, als Dictionary und mit Alias werden alle geladen. Stufe: **Vollständig**.

Bekannte Sonderfälle: Ein Parameter, dessen Name ein Geheimwort enthält oder dessen Wert wie eine Anmeldeinformation aussieht, wird mit einer Warnung zu einer Variable mit leerem Wert. Ein Parameter, den ein Knoten verwendet und den der Export nicht deklariert, wird mit einer Warnung zu einer Variable mit leerem Wert.

## Verbindung zu externen Systemen

Savant-Konnektoren sind Quell- und Zielvorgaben, keine Schritte, und ein Export enthält weder Datensätze noch Anmeldeinformationen. PlaidCloud erreicht diese Systeme über eine Verbindung statt über einen Knoten auf der Arbeitsfläche.

| Savant | Wohin es in PlaidCloud geht |
| --- | --- |
| Quellkonnektor | `source_bindings` ordnet den Savant-Knoten oder das Dataset einer PlaidCloud-Tabelle oder einer Document-Datei zu, die über den passenden Import-Schritt gelesen wird; eine ungebundene Quelle warnt und verarbeitet nichts |
| Ziel: CSV, Excel und andere Dateiformate | Ein Export-Schritt ([Export: CSV](/de/reference/workflow-steps/export/export-to-csv/), [Export: Excel](/de/reference/workflow-steps/export/export-to-excel/), [Export to PDF](/de/reference/workflow-steps/export/export-to-pdf/)) |
| Ziel: Google Sheets, Tableau, Slack | [Export to Google Spreadsheet](/de/reference/workflow-steps/export/export-to-google-spreadsheet/), [Publish to Tableau](/de/reference/workflow-steps/export/export-to-tableau/) oder [Notify via Slack](/de/reference/workflow-steps/notifications/notify-via-slack/), über eine Verbindung, die Sie mit `destination_bindings` binden |
| Ziel: ungebundenes Datenbank-, Warehouse- oder SaaS-Ziel (Oracle, generische Datenbank, Looker Studio, NetSuite, SAP sowie Google Sheets, Tableau oder Slack ohne gebundene Verbindung) | Eine Projekttabelle, benannt nach dem Zielknoten, mit einer Warnung, die das ursprüngliche Ziel nennt |
| Ziel: ungebundenes Dateisystemziel (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | Die Datei, im Dateityp des Ziels, in einem Document-Ordner, der den Zielordner widerspiegelt, mit einer Warnung. Anmeldeinformationen und Freigabe-Token werden aus dem Ordnerpfad entfernt |
| Ziel: ungebundene E-Mail | Eine CSV mit einer Warnung |
| Ziel: nicht verwendbare Bindung | Eine CSV mit einer Warnung, die das ursprüngliche Ziel nennt |

Die Konvertierung kontaktiert nie das Quell- oder Zielsystem.
