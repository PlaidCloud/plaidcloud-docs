---
title: Alteryx-Konvertierungsmatrix
description: Wie PlaidCloud Alteryx-Tools in native Schritte erweiterter Workflows, Makros, Variablen und verwaltete Executors konvertiert, mit dem Unterstützungsstatus pro Tool.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/alteryx-conversion-matrix.md
---

PlaidCloud konvertiert Alteryx-Workflows, -Apps und -Makros in native erweiterte
Workflows. Der Importer ordnet jedes Alteryx-Tool einem Workflow-Schritt, einem
Makrokonstrukt, einer gesteuerten Variablen, einem Dokument-basierten Dateivorgang
oder einem verwalteten Job-Executor zu, sodass ein konvertierter Workflow
cloudnativ läuft und nicht als Emulation.

**Nahezu jedes Standard-Alteryx-Tool wird vollständig konvertiert.** Der
Unterstützungsstatus gilt pro Tool:

- **Vollständig**: wird in einen nativen PlaidCloud-Schritt, ein Makro, eine Variable, ein Artefakt oder
  einen verwalteten Executor konvertiert und führt die Funktion des Tools aus. Die meisten Tools gehören hierher.
- **Teilweise**: wird konvertiert und läuft für den üblichen Einsatzzweck, während ein bestimmter
  *Funktionsmodus* des Tools noch nicht nachgebildet wird. Selten.
- **Nicht unterstützt**: keine Konvertierung; die Funktion wird stattdessen nativ neu aufgebaut.

Konnektoren zu externen Systemen (Salesforce, HTTP, Google Analytics, Cassandra,
E-Mail, Hadoop, Spark und ähnliche) werden **verbunden, nicht konvertiert**. Siehe
[Verbindung zu externen Systemen](#verbindung-zu-externen-systemen).

## Tool-Unterstützung

| Alteryx-Tool | Status | PlaidCloud-Äquivalent | Konvertiert |
| --- | --- | --- | --- |
| Action | Vollständig | Variablenbindung und bedingte Schrittkonfiguration | Aktualisiert Einstellungen nachgelagerter Schritte aus konvertierten App-Eingaben. |
| Analytic App interface (`.yxwz`) | Teilweise | Veröffentlichtes Panel-„App Runner“-Frontend | Das `<Questions>`-Layout der App wird in eine funktionsfähige Panel-App umgesetzt, die Benutzereingaben erfasst und den konvertierten Workflow steuert und im Rahmen der Konvertierung automatisch veröffentlicht wird (eine App ohne Eingabe-Widgets wird übersprungen). Gängige Fragetypen (Text, numerisch (Numeric Up Down), Datum, Kontrollkästchen, Optionsfeld, Dropdown-Liste, Listenfeld, Baum, Dateiauswahl und Ordnerauswahl) werden zu App-Runner-Widgets. Eine Frage, deren Wert an keine Workflow-Variable gebunden ist, wird mit einem sichtbaren Hinweis dargestellt, statt stillschweigend einen toten Wert zu erfassen, und weniger gängige Fragetypen werden zur Prüfung markiert, statt umgesetzt zu werden. Siehe [Konvertierte Alteryx-Apps verwenden](/de/guides/workflows/use-converted-alteryx-apps/#das-app-runner-frontend). |
| Append Fields | Vollständig | Transformation „Felder anhängen“ | Hängt Felder aus einem Datenstrom an einen anderen an. |
| Auto Field | Vollständig | Transformation für automatische Feldgrößen | Behält die abgeleiteten Feldgrößen bei. |
| AutoML | Vollständig | [ML: Modell trainieren](/de/reference/workflow-steps/machine-learning/ml-train/) | Fasst die Auswahl von Modellmethode, Ziel und Kandidatenalgorithmen wie bei Classification und Regression in einem ML-Train-Schritt zusammen. AutoML hält zur Laufzeit in Alteryx nie fest, welcher Kandidatenalgorithmus tatsächlich gewonnen hat. Die Konvertierung wählt daher den ersten markierten Algorithmus, den ML Train unterstützt, und vermerkt die Wahl. Vergleichen Sie einen konvertierten AutoML-Schritt mit Ihren eigenen Alteryx-Ergebnissen. |
| Barcode | Vollständig | Barcode-Executor | Liest oder schreibt Barcodes in der konfigurierten Symbologie. |
| Batch Macro | Teilweise | Makro, aufgefächert über seine Control-Anchor-Tabelle | Der Aufrufer führt das gesamte Makro einmal pro Datensatz seiner Steuereingabe aus und bindet dabei in jedem Durchlauf die Steuerparameter des Inneren. Das schließt einen Steuerparameter ein, den der Aufrufer in eine Anzeigebezeichnung umbenannt hat, wenn genau einer im Spiel ist, sowie eine `UpdateRawXml`-Action, die die Feldliste eines Select aus einer Variablen neu schreibt. Konstellationen, deren Wert pro Durchlauf sich nicht sicher nachbilden lässt, schlagen namentlich geschlossen fehl, statt falsch konvertiert zu werden: ein `UpdateRawXml`, das etwas anderes als die Feldliste eines Select neu schreibt, und eine Action, die den gesamten Ausdruck eines Filter durch eine Variable ersetzt (seine rohe Syntax pro Durchlauf würde falsch ausgewertet). |
| Browse | Vollständig | Browse / Durchreichen | Für die Inspektion erhalten, ohne Laufzeitkosten. |
| Buffer | Vollständig | [Spatial Buffer](/de/reference/workflow-steps/spatial/spatial-buffer/) | Vergrößert jede Geometrie um einen festen Abstand. |
| Build Features | Teilweise | [Build Features](/de/reference/workflow-steps/tables/table-build-features/) | Konvertiert arithmetische und Interaktionsprimitive, die Extraktion von Datumsteilen, Binning mit expliziten Schwellenwerten, Z-Score- und Min-Max-Skalierung sowie One-Hot-Kodierung. Tabellenübergreifende Aggregation (Deep Feature Synthesis über die Registerkarte Manage Relationships), PCA, Target Encoding und datengetriebenes automatisches Binning haben kein Äquivalent. Jedes davon wird im Konvertierungsbericht namentlich markiert, statt stillschweigend verworfen zu werden. |
| Calgary Cross Count | Vollständig | [Calgary-Datenbank](/de/guides/workflows/migrate-alteryx-workflows/#calgary-datenbanken), Aggregat | Gruppiert indizierte Felder und zählt die benannten Werte jedes benutzerdefinierten Felds. |
| Calgary Cross Count Append | Vollständig | [Calgary Cross Count Append](/de/guides/workflows/migrate-alteryx-workflows/#calgary-join-und-cross-count-append) | Gleicht jeden Eingabedatensatz mit einem Werteindex ab und zählt dann, wie viele Datenbankdatensätze er getroffen hat. |
| Calgary Input | Vollständig | [Calgary-Datenbank](/de/guides/workflows/migrate-alteryx-workflows/#calgary-datenbanken), Eingabe | Liest die Datenbank, wobei ihre gespeicherte Abfrage als Filter angewendet wird. |
| Calgary Join | Vollständig | [Calgary Join](/de/guides/workflows/migrate-alteryx-workflows/#calgary-join-und-cross-count-append) | Gleicht jeden Datensatz mit einem Werteindex der Datenbank ab und behält die Datensätze, die getroffen wurden. |
| Calgary Loader | Vollständig | [Calgary-Datenbank](/de/guides/workflows/migrate-alteryx-workflows/#calgary-datenbanken), Schreibvorgang | Schreibt die Stellvertretertabelle, an die jeder Calgary-Leser gebunden wird. |
| Centroid | Vollständig | Centroid-Executor-Operation | Reduziert jede Geometrie auf ihren Mittelpunkt, der als Spalte `Centroid` angehängt wird. |
| Check Box | Vollständig | Gesteuerte Workflow-Variable | Konvertiert Kontrollkästchen-Auswahlen der App in gesteuerte Eingaben. |
| Classification | Vollständig | [ML: Modell trainieren](/de/reference/workflow-steps/machine-learning/ml-train/) | Fasst die Assisted-Modeling-Kette in einem ML-Train-Schritt mit Algorithmus, Ziel, Merkmalen und Hyperparametern zusammen. |
| Comment / Annotation / Link | Vollständig | Anmerkung auf der Arbeitsfläche | Als Workflow-Kontext erhalten. |
| Condition | Vollständig | Schrittbedingung | Löst aus einem Ausdruck Warnungen, Fehler oder Verzweigungen aus. |
| Control Parameter | Vollständig | Makro-Steuerparameter | Wird auf PlaidCloud-Makroparameter abgebildet. |
| Convex Hull | Vollständig | Convex-Hull-Executor-Operation | Erzeugt das kleinste konvexe Polygon, das jede Geometrie umschließt, und hängt es als Spalte `ConvexHull` an. |
| Create Points | Vollständig | [Table Extract](/de/reference/workflow-steps/spatial/spatial-sql-recipes/)-Schritt mit `geom_point` | Erzeugt Punktgeometrie aus Längen- und Breitengradspalten, in SQL. |
| Create Samples | Vollständig | Table Extract, eine pro Ausgabe | Teilt die Eingabe mit den konfigurierten Prozentsätzen in Estimation, Validation und Holdout auf. |
| Cross Tab | Vollständig | Pivot- / Kreuztabellen-Transformation | Pivotiert Zeilen in Spalten über alle Aggregationsmethoden und die abgeleiteten Summen. |
| Data Cleansing | Vollständig | Transformation zur Datenbereinigung | Bereinigt Leerzeichen, Nullwerte, Interpunktion und Groß-/Kleinschreibung. |
| Date | Vollständig | Workflow-Variable (Datum) | Gibt ISO-Datumswerte für Schritte und Bedingungen aus. |
| DateTime | Vollständig | Datums-/Zeittransformation | Konvertiert das Parsen und Formatieren von Datum und Uhrzeit. |
| Detour | Vollständig | Bedingte Verzweigungsweiterleitung | Konvertiert die Routenauswahl in DAG-Bedingungen. |
| Detour End | Vollständig | Bedingte Verzweigungszusammenführung | Führt bedingt ausgewählte Verzweigungen wieder zusammen. |
| Directory | Vollständig | Verzeichnisliste von Dokumenten | Listet Dateien aus einem Dokumentpfad auf. |
| Distance | Vollständig | [Table Extract](/de/reference/workflow-steps/spatial/spatial-sql-recipes/)-Schritt mit `ST_DISTANCE_SPHERE` | Geodätischer Punkt-zu-Punkt-Abstand und Peilung, in SQL. |
| Download | Vollständig | [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/)-Schritt gegen eine REST-Verbindung | Lädt externe Daten oder Artefakte herunter; weisen Sie dem konvertierten Schritt vor der Ausführung eine REST-Verbindung zu. |
| Drop Down | Vollständig | Gesteuerte Workflow-Variable | Konvertiert Dropdown-Auswahlen der App in gesteuerte Eingaben. |
| Dynamic Input | Teilweise | Dynamische Dokumenteneingabe | Löst Dateimuster und variablengesteuerte Eingaben zur Laufzeit auf. Ein Excel-*ReadList*, bei dem ein Arbeitsblatt aus jeder von einem Directory-Tool aufgelisteten Arbeitsmappe gelesen und dann vereinigt wird, wird in ein Lesen des Blatts per Ordner-Glob konvertiert, wenn ein vorgelagerter Filter das Blatt per exakter Übereinstimmung auf einen einzigen Namen festlegt. Ein Blatt, das über Contains, eine Ungleichung oder einen OR-Filter gewählt wird, oder ein Lesevorgang über mehr als ein Blatt wird abgelehnt, statt das falsche Blatt zu lesen. |
| Dynamic Rename | Vollständig | Dynamische Umbenennungstransformation | Benennt Felder anhand von Metadaten oder Regeln um. |
| Dynamic Replace | Vollständig | Dynamische Ersetzungstransformation | Wendet Ersetzungsregeln aus einem zweiten Datenstrom an. |
| Dynamic Select | Vollständig | Transformation für dynamische Feldauswahl | Wählt Felder nach Typ, Name oder Regel aus. |
| Error | Vollständig | Schrittbedingung (Fehler) | Konvertiert das konfigurierte Fehlerverhalten in Schrittbedingungen. |
| Feature Types | Vollständig | [ML: Modell trainieren](/de/reference/workflow-steps/machine-learning/ml-train/), Merkmalskonfiguration | Übernimmt die zugewiesene Modellrolle jedes Felds in den zusammengefassten ML-Train-Schritt. |
| File Browse | Vollständig | Gesteuerte Dokument-Dateivariable | Lässt Benutzer eine Datei für eine konvertierte App-Ausführung auswählen. |
| Filter | Vollständig | Filtertransformation | Teilt Datensätze per Ausdruck in Wahr- und Falsch-Pfade auf. |
| Fit | Vollständig | [ML: Modell trainieren](/de/reference/workflow-steps/machine-learning/ml-train/) | Geht im zusammengefassten ML-Train-Schritt auf. |
| Folder Browse | Vollständig | Gesteuerte Dokument-Ordnervariable | Lässt Benutzer einen Ordner für eine konvertierte App-Ausführung auswählen. |
| Formatted Excel output into a styled template | Teilweise | Vorlagenfähiger Excel-Writer ([Export to Excel Sheets](/de/reference/workflow-steps/export/export-to-excel-sheets/) für mehrere Blätter) | Beim Schreiben in eine formatierte Vorlage bleibt deren Formatierung erhalten: Werte, Zahlenformate, Schriftarten, Füllungen, Rahmen, verbundene Zellen und Spaltenbreiten werden in das benannte Blatt und den benannten Bereich übernommen. Das gilt sowohl für ein einzelnes Blatt als auch für mehrere Ausgaben, die in verschiedenen Blättern einer Arbeitsmappe zusammengestellt und in einem Durchgang gefüllt werden, sodass sich die Blätter nicht mehr gegenseitig überschreiben. Ein Fall bleibt teilweise: Eine Vorlage mit Pivot-Tabellen oder Diagrammen verliert diese Objekte, wenn ihre Blätter geschrieben werden. Einfache (unformatierte) Excel-Ausgabe ist vollständig, siehe Output Data. |
| Formula | Vollständig | Formeltransformation | Konvertiert Feldausdrücke in PlaidCloud-Ausdrücke oder SQL. |
| Fuzzy Match | Vollständig | Fuzzy-Matching-Executor | Gleicht anhand von Schlüsseln, Schwellenwerten und Kandidatenprüfung ab. |
| Generalize | Vollständig | [Spatial Generalize](/de/reference/workflow-steps/spatial/spatial-generalize/) | Vereinfacht Geometrie auf eine Toleranz und erhält dabei die Topologie. |
| HTML | Vollständig | Berichtstext / HTML-Artefakt | Erhält den Inhalt als Bericht oder Artefaktausgabe. |
| Image Processing | Vollständig | Bildtransformations-Executor | Wendet Graustufen, Skalierung, Zuschnitt und Drehung in der Reihenfolge der Arbeitsfläche an. |
| Image Profile | Vollständig | Bildprofil-Executor | Meldet Abmessungen, Modus, Format, Kanäle und Luminanzstatistiken. |
| Image to Text | Vollständig | OCR-Executor | Extrahiert Text aus Bildern per verwalteter OCR. |
| Input Data | Vollständig | Dokument-basierte Dateieingabe | Lädt Quelldateien vom Typ `.yxdb`, `.dbf`, Excel und `.flat` mit fester Breite in Workflow-Daten. |
| Insights | Vollständig | Dashboard- / Artefaktausgabe | Erstellt ein cloudnatives Prüfartefakt. |
| Interactive Chart | Vollständig | Diagrammartefakt | Erstellt aus konvertierten Daten ein Diagrammartefakt. |
| Join | Vollständig | Join-Transformation | Erzeugt Datenströme für verbundene, nur links vorhandene und nur rechts vorhandene Datensätze über einen Schlüssel aus einem oder mehreren Feldern oder nach Position. |
| Join Multiple | Vollständig | Multi-Join-Transformation | Verbindet mehrere Eingabedatenströme. |
| Key/Value Pairs | Vollständig | [Text: NLP AI](/de/reference/workflow-steps/text-documents/nlp-ai/) (Aufgabe keyvalue) | Extrahiert Schlüssel-Wert-Paare aus einer Textspalte über den LLM-gestützten NLP-AI-Schritt, mit optionalen Kandidatenschlüsseln und unscharfem oder exaktem Abgleich. |
| Line To Polygon | Vollständig | Line-To-Polygon-Executor-Operation | Schließt jede Linie zu einem Polygonring, der als Spalte `Polygon` angehängt wird. |
| List Box | Vollständig | Gesteuerte Workflow-Variable | Konvertiert Listenauswahlen der App in gesteuerte Eingaben. |
| Location Optimizer | Teilweise | [Standortoptimierer](/de/reference/workflow-steps/optimization/location-optimizer/) | Konvertiert den Fall der linearen Abstandsminimierung (K Standorte wählen, um den gesamten oder gewichteten Abstand zur Nachfrage zu minimieren) in den nativen p-Median-MIP-Schritt. Ein Gravitations-Kernel-Score, ein individuelles Bewertungsmakro oder jedes andere Zielkriterium der Kandidatensuche wird weiterhin abgelehnt; siehe [Alteryx-Workflows migrieren](/de/guides/workflows/migrate-alteryx-workflows/#makros-in-einem-konvertierten-workflow). |
| Macro calls | Vollständig | Makroaufruf | Importiert bekannte Makroquellen und bildet Makroaufrufe auf PlaidCloud-Makroschritte ab. |
| Macro Input / Macro Output | Vollständig | Makro-Eingabe- / Ausgabeport | Werden direkt auf PlaidCloud-Makroports abgebildet. |
| Make Grid | Vollständig | [Räumlich: Raster erstellen](/de/reference/workflow-steps/spatial/spatial-make-grid/) | Unterteilt eine Ausdehnung in quadratische Zellen, eine Zeile pro Zelle. |
| Map | Vollständig | Kartenartefakt | Erstellt ein PlaidCloud-Kartenartefakt. |
| Map Input | Vollständig | [Räumlicher Dateiimport](/de/reference/workflow-steps/spatial/spatial-file-import/) | Liest MapInfo-, ESRI-, KML- und GeoJSON-Dateien mit ihren Begleitdateien. |
| Master Selector | Teilweise | Gesteuerte Workflow-Variable und bedingte Schrittsichtbarkeit | Konvertiert die Anzeige-/Ausblendebedingungen des Tools für Oberflächenelemente in bedingte Schrittsichtbarkeit. Konvertiert, welchen Teil-Workflow die Auswahl ausführt, nach bestem Bemühen. Die Validierung anhand echter Apps im Mandanten steht noch aus, prüfen Sie daher das ausgewählte Ausführungsziel, bevor Sie sich in der Produktion darauf verlassen. |
| Message | Vollständig | Schrittbedingung (Meldung) | Gibt aus einer Bedingung eine Workflow-Warnung, -Meldung oder einen -Fehler aus. |
| Modeling | Vollständig | [ML: Modell trainieren](/de/reference/workflow-steps/machine-learning/ml-train/) | Geht mit der Modellwahl der Pipeline im ML-Train-Schritt auf. |
| Multi-Field Formula | Vollständig | Mehrfeld-Formeltransformation | Wendet eine Formel auf ausgewählte Felder an. |
| Multi-Row Formula | Vollständig | Fenster- / zeilenbezogene Formeltransformation | Konvertiert zeilenrelative Logik in Fensterverhalten, partitioniert nach Gruppieren nach. |
| Named Entity Recognition (NER) | Vollständig | [Text: NLP AI](/de/reference/workflow-steps/text-documents/nlp-ai/) (Aufgabe ner) | Extrahiert Entitäten (Personen, Organisationen, Orte, Daten, Mengen oder eine benutzerdefinierte Typliste) aus einer Textspalte über den LLM-gestützten NLP-AI-Schritt. |
| Numeric Up Down | Vollständig | Gesteuerte numerische Variable | Konvertiert numerische App-Eingaben in eine typisierte Variable. |
| Output Data | Vollständig | Dokument- / Tabellenausgabe | Schreibt die Ausgabe in Dokumente oder PlaidCloud-Tabellen, einschließlich Parquet- und Avro-Dateien; Ausgaben vom Typ `.yxdb`, `.hyper` und `.dbf` werden als Parquet geschrieben. |
| Overlay | Vollständig | [Räumliche Verarbeitung](/de/reference/workflow-steps/spatial/spatial-process/) | Schneidet, vereinigt oder trennt zwei Geometriespalten. |
| PDF Input | Vollständig | PDF-Extraktions-Executor | Extrahiert Text oder Tabellen aus PDFs. |
| Point To Line | Vollständig | Point-To-Line-Executor-Operation | Verbindet die Punkte jeder Gruppe zu einer `SequenceLine` pro Gruppe, geordnet nach dem Sequenzfeld. |
| Poly-Build | Vollständig | [Spatial Poly-Build](/de/reference/workflow-steps/spatial/spatial-poly-build/) | Erzeugt pro Punktgruppe ein Polygon oder eine konvexe Hülle. |
| Poly-Split | Vollständig | [Spatial Poly-Split](/de/reference/workflow-steps/spatial/spatial-poly-split/) | Eine Zeile pro Eckpunkt, Teilpolygon oder Loch. |
| Portfolio Composer (Text / Table / Image / Layout / Render) | Vollständig | Berichtsartefakte | Konvertieren Berichtsinhalt, Layout und Rendering in PlaidCloud-Berichtsausgabe. |
| POS Tagger | Vollständig | [Text: NLP AI](/de/reference/workflow-steps/text-documents/nlp-ai/) (Aufgabe pos) | Kennzeichnet die Wortart jedes Tokens aus einer Textspalte über den LLM-gestützten NLP-AI-Schritt. |
| Predict | Vollständig | [ML: Bewerten](/de/reference/workflow-steps/machine-learning/ml-score/) | Bewertet Daten mit der trainierten Modelltabelle und hängt eine Prognosespalte an. |
| Radio Button | Vollständig | Gesteuerte Workflow-Variable | Konvertiert Optionsfeld-Auswahlen der App in gesteuerte Eingaben. |
| Random % Sample | Vollständig | Table Extract (zufällig) | Liefert die exakt angeforderte Anzahl oder den angeforderten Prozentsatz an Datensätzen. |
| Record ID | Vollständig | Zeilenkennungs-Transformation | Fügt eine deterministische Datensatzkennung im konfigurierten Typ und Startwert hinzu, die pro Gruppe neu beginnt. |
| Redistribute | Vollständig | Redistribute-Executor-Operation | Verteilt eine Kennzahl nach Überlappungsfläche von einem Satz von Geografien auf einen anderen um und hängt sie als Spalte `Redistributed` an. |
| RegEx | Vollständig | Transformation mit regulärem Ausdruck | Parst, gleicht ab oder ersetzt Text. |
| Regression | Vollständig | [ML: Modell trainieren](/de/reference/workflow-steps/machine-learning/ml-train/) | Fasst die Assisted-Modeling-Kette in einem ML-Train-Schritt zusammen. |
| Report Map | Vollständig | Kartenberichtsartefakt | Erzeugt ein cloudnatives Karten-/Berichtsartefakt. |
| Run Command | Teilweise | [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/)-Schritt gegen eine REST-Verbindung (nur `curl`/`wget`) | Konvertiert eine `curl`- oder `wget`-Befehlszeile in einen REST-Anfrage-Schritt. Interpreter- und Skriptbefehle (`cscript`, PowerShell, Python und ähnliche), Excel-COM-Automatisierung, Dateisystemoperationen sowie undurchsichtige oder Workflow-startende Befehle werden namentlich zur manuellen Prüfung markiert, statt automatisch konvertiert zu werden. |
| Sample | Vollständig | Stichprobentransformation | Behält Datensätze nach Anzahl, Prozentsatz oder Gruppierung. |
| Select | Vollständig | Auswahl- und Schemaprojektionsschritt | Wählt Felder aus, benennt sie um, ordnet sie neu und ändert ihre Typen. |
| Smooth | Vollständig | [Spatial Smooth](/de/reference/workflow-steps/spatial/spatial-smooth/) | Glättet jede Geometrie über eine Anzahl von Durchläufen. |
| Sort | Vollständig | Sortiertransformation | Sortiert Datensätze nach konfigurierten Feldern und Richtungen. |
| Spatial Info | Vollständig | [Spatial Info](/de/reference/workflow-steps/spatial/spatial-info/) | Fläche, Länge, Schwerpunkt und umschließendes Rechteck als geodätische Maße. |
| Spatial Match | Vollständig | [Räumlicher Abgleich](/de/reference/workflow-steps/spatial/spatial-match/) / [Spatial Match (Intersect / Unmatched)](/de/reference/workflow-steps/spatial/spatial-match-executor/) | Konvertiert jede Beziehung (Within, Contains, Intersects, Touches, Crosses, Overlaps und Centroid-In), abgeglichen in der Datenbank oder in der Workflow-Engine. |
| Spatial Process | Vollständig | [Räumliche Verarbeitung](/de/reference/workflow-steps/spatial/spatial-process/) | Schneidet, vereinigt oder trennt Geometriespalten. |
| Summarize | Vollständig | Aggregattransformation | Gruppiert und aggregiert: Summe, Anzahl, Durchschnitt, Minimum, Maximum, Median, Modus, Standardabweichung, Varianz und Anzahl eindeutiger Werte. |
| Tab | Vollständig | App-Registerkartengruppierung | Als Struktur der konvertierten App erhalten. |
| Test | Vollständig | Schrittbedingung | Konvertiert Testzusicherungen in Schrittbedingungen. |
| Text Box | Vollständig | Gesteuerte Textvariable | Konvertiert Texteingaben der App in eine typisierte Variable. |
| Text Input | Vollständig | Inline-Tabelleneingabe | Erstellt Inline-Daten für den Workflow. |
| Text Pre-processing | Vollständig | NLP-Vorverarbeitungs-Executor | Normalisiert und verarbeitet Text vor. |
| Text Summary | Vollständig | [Text: NLP AI](/de/reference/workflow-steps/text-documents/nlp-ai/) (Aufgabe summary) | Fasst eine Textspalte über den LLM-gestützten NLP-AI-Schritt auf eine konfigurierte maximale Satzanzahl zusammen. |
| Text To Columns | Vollständig | Transformation zum Aufteilen von Spalten | Teilt Text in Felder oder Zeilen auf. |
| Tile | Vollständig | Kachel- / Gruppierungstransformation | Weist Kachelgruppen nach konfigurierter Regel zu. |
| Tool Container | Vollständig | Container auf der Arbeitsfläche / Ausführungsgruppe | Als Workflow-Organisation erhalten. |
| Topic Modeling | Vollständig | Topic-Modeling-Executor | Führt Topic Modeling über verwaltetes NLP aus. |
| Transformation | Vollständig | Transformationsschritt | Konvertiert Transformationslogik in PlaidCloud-Ausdrücke oder SQL. |
| Transpose | Vollständig | Unpivot-Transformation | Wandelt Spalten in Zeilen als Name/Wert-Paar um. |
| Tree | Vollständig | Gesteuerte Workflow-Variable | Konvertiert die Baumauswahl der App in gesteuerte Eingaben. |
| Union | Vollständig | Union-Transformation | Kombiniert Datenströme nach Name, Position oder konfigurierten Regeln. |
| Unique | Vollständig | Transformation zur Trennung eindeutiger Datensätze und Duplikate | Trennt erste eindeutige Datensätze von Duplikaten. |
| Visual Layout | Vollständig | Layout-Metadaten der Arbeitsfläche | Als Designkontext erhalten. |
| Word Cloud | Vollständig | Textvisualisierungsartefakt | Erstellt aus der Textanalyse ein Visualisierungsartefakt. |
| XML Parse | Vollständig | XML-Parse-Transformation | Extrahiert XML-Felder in Workflow-Daten. |
| Zero-shot Text Classification | Vollständig | [Text: NLP AI](/de/reference/workflow-steps/text-documents/nlp-ai/) (Aufgabe zeroshot) | Klassifiziert eine Textspalte anhand einer Liste von Kandidatenlabels pro Zeile, mit einem oder mehreren Labels, über den LLM-gestützten NLP-AI-Schritt. |
| Find Nearest | Vollständig | [Spatial Find Nearest](/de/reference/workflow-steps/spatial/spatial-find-nearest/) | Nach Abstand geordneter Nearest-Neighbor-Join: Luftlinie sowie Fahrzeit-Nächste (geordnet nach Minuten in einem Straßennetz) über die selbst gehostete Routing-Engine von PlaidCloud. Fahrzeit wird pro Workspace aktiviert. |
| Trade Area | Vollständig | [Spatial Trade Area](/de/reference/workflow-steps/spatial/spatial-trade-area/) | Konzentrische Puffer in realen Einheiten: Einzugsgebiete mit festem Radius sowie Fahrzeit-Einzugsgebiete (Minuten in einem Straßennetz) über die selbst gehostete Routing-Engine. Fahrzeit wird pro Workspace aktiviert. |
| Image Template | Vollständig | Image-Template-Executor-Operation | Der manuelle Modus schneidet das Bild auf jede Region zu, die Sie auf der Vorlage zeichnen. Der automatische Modus erkennt die Seitenbereiche mit einem Layoutmodell nach offenem Standard für Sie und gibt eine Zeile pro Bereich aus, jeweils mit den erkannten Grenzen und der Konfidenz zur Prüfung; eine Seite, die das Modell nicht sicher lesen kann, wird namentlich markiert, statt zugeschnitten zu werden. Die Erkennung nach offenem Standard kann von der von Alteryx abweichen: Prüfen Sie die erkannten Bereiche oder verwenden Sie den manuellen Modus für exakte Kontrolle. |
| Image Recognition | Vollständig | Bilderkennungs-Executor | Trainiert im Workflow einen Bildklassifikator und bewertet damit neue Bilder an Ort und Stelle, ohne externes Konto, und es verlassen keine Daten PlaidCloud. Der Klassifikator wird neu trainiert und nicht von Alteryx kopiert, die Ergebnisse sind daher eine getreue Annäherung und keine bitgenaue Übereinstimmung, und das Training läuft auf der CPU. Wird pro Workspace aktiviert. |
| Geocoder | Vollständig | Selbst gehosteter Geocoder | Geokodiert Adressen zu Koordinaten und kodiert Koordinaten per Reverse-Geocoding zu Adressen mit dem eigenen Geocoder von PlaidCloud, ohne externes Konto, und es verlassen keine Daten PlaidCloud. Wird pro Workspace aktiviert. |

Oberflächen-Widgets (Dropdown-Listen, Listenfelder, Kontrollkästchen,
Text-/Zahlen-/Datumseingaben, Datei- und Ordnerauswahlen), Objekte auf der Arbeitsfläche (Kommentare, Verknüpfungen,
Container) und Makroports werden alle als native gesteuerte Variablen oder
Objekte der Arbeitsfläche konvertiert. Das vollständige Oberflächenlayout einer Alteryx-App, die
`<Questions>`-Definition der `.yxwz`-Datei, wird außerdem in ein veröffentlichtes Panel-„App
Runner“-Frontend umgesetzt. Die Konvertierung der App erzeugt also ein funktionsfähiges Eingabeformular, das dieselben Werte
erfasst und den konvertierten Workflow steuert, nicht nur die
einzelnen gesteuerten Variablen. Siehe die Zeile Analytic App interface oben und
[Konvertierte Alteryx-Apps verwenden](/de/guides/workflows/use-converted-alteryx-apps/#das-app-runner-frontend).

**Hinweis zur Excel-Ausgabe.** Eine einfache neue Arbeitsmappe, in die Daten mit Standardformatierung
geschrieben werden, wird vollständig konvertiert. Das Schreiben in eine *formatierte Vorlage*, bei dem benannte
Blätter und Bereiche gefüllt und ihre Formatierung erhalten bleibt, wird für ein einzelnes
Blatt und für mehrere Ausgaben konvertiert, die in verschiedenen Blättern einer Arbeitsmappe zusammengestellt werden
(der Schritt [Export to Excel Sheets](/de/reference/workflow-steps/export/export-to-excel-sheets/)
füllt alle Blätter in einem Durchgang). Vorlagen mit Pivot-Tabellen oder Diagrammen
verlieren diese Objekte, wenn ihre Blätter geschrieben werden; Eingriffe auf Blattebene, die über
Run Command gesteuert werden (Excel COM/VBS), werden namentlich zur manuellen Prüfung markiert, statt
automatisch konvertiert zu werden.

## Abdeckung der räumlichen Tools

Jedes Tool der Alteryx-Palette **Spatial** hat in PlaidCloud eine Route, und jede
dieser Routen ist ein Schritt, den Sie auch von Hand aufbauen können. Die Konvertierung ist eine
Erleichterung, nicht der einzige Weg. Siehe [Geodaten-Schritte](/de/reference/workflow-steps/spatial/)
für die vollständige Referenz und [Geodatenanalyse](/de/guides/workflows/geospatial-analytics/)
dazu, wie sie zusammenspielen.

| Alteryx-Spatial-Tool | PlaidCloud-Route | Läuft in |
| --- | --- | --- |
| Buffer | [Spatial Buffer](/de/reference/workflow-steps/spatial/spatial-buffer/) | Workflow-Engine |
| Centroid | Centroid-Executor-Operation | Workflow-Engine |
| Convex Hull | Convex-Hull-Executor-Operation | Workflow-Engine |
| Create Points | [Table-Extract-Ausdruck](/de/reference/workflow-steps/spatial/spatial-sql-recipes/) | Datenbank |
| Distance | [Table-Extract-Ausdruck](/de/reference/workflow-steps/spatial/spatial-sql-recipes/) | Datenbank |
| Find Nearest | [Spatial Find Nearest](/de/reference/workflow-steps/spatial/spatial-find-nearest/) | Datenbank; Routing-Dienst für Fahrzeit |
| Generalize | [Spatial Generalize](/de/reference/workflow-steps/spatial/spatial-generalize/) | Workflow-Engine |
| Heat Map | [Heat Map (macro)](/de/reference/workflow-steps/macros/macro-heat-map/) | Workflow-Engine |
| Line To Polygon | Line-To-Polygon-Executor-Operation | Workflow-Engine |
| Make Grid | [Räumlich: Raster erstellen](/de/reference/workflow-steps/spatial/spatial-make-grid/) | Workflow-Engine |
| Point To Line | Point-To-Line-Executor-Operation | Workflow-Engine |
| Poly-Build | [Spatial Poly-Build](/de/reference/workflow-steps/spatial/spatial-poly-build/) | Workflow-Engine |
| Poly-Split | [Spatial Poly-Split](/de/reference/workflow-steps/spatial/spatial-poly-split/) | Workflow-Engine |
| Redistribute | Redistribute-Executor-Operation | Workflow-Engine |
| Smooth | [Spatial Smooth](/de/reference/workflow-steps/spatial/spatial-smooth/) | Workflow-Engine |
| Spatial Info | [Spatial Info](/de/reference/workflow-steps/spatial/spatial-info/) | Workflow-Engine |
| Spatial Match | [Räumlicher Abgleich](/de/reference/workflow-steps/spatial/spatial-match/) | Datenbank |
| Spatial Match, Schnittobjekt, Unmatched | [Spatial Match (Intersect / Unmatched)](/de/reference/workflow-steps/spatial/spatial-match-executor/) | Workflow-Engine |
| Spatial Process | [Räumliche Verarbeitung](/de/reference/workflow-steps/spatial/spatial-process/) | Workflow-Engine |
| Trade Area (fester Radius + Fahrzeit) | [Spatial Trade Area](/de/reference/workflow-steps/spatial/spatial-trade-area/) | Workflow-Engine; Routing-Dienst für Fahrzeit |
| Pie Wedge Trade Area | [Pie Wedge Trade Area (macro)](/de/reference/workflow-steps/macros/macro-pie-wedge-trade-area/) | Workflow-Engine |
| Spatial file input | [Räumlicher Dateiimport](/de/reference/workflow-steps/spatial/spatial-file-import/) | Workflow-Engine |
| Summarize: SpatialObjCombine, SpatialObjConvexHull | [Räumlich kombinieren](/de/reference/workflow-steps/spatial/spatial-combine/) | Workflow-Engine |
| Report Map | [Report Map](/de/reference/workflow-steps/reports/report-map/) | Workflow-Engine |

**Fahrzeit-Einzugsgebiete und Nächstgelegene**: Die Fahrzeitringe von Trade Area und das Fahrzeit-Ranking von Find
Nearest laufen auf der selbst gehosteten Routing-Engine von PlaidCloud
(Isochronen und Fahrzeitmatrizen im Straßennetz), nicht auf einer gehosteten Drittanbieter-
API, sodass Ausgangskoordinaten die Plattform nie verlassen. Fahrzeit wird pro
Workspace aktiviert. Routing und Fahrzeitgebiete verwenden OpenStreetMap-Daten,
© OpenStreetMap-Mitwirkende, verfügbar unter der [Open Database License
(ODbL)](https://www.openstreetmap.org/copyright).

### Bekannte räumliche Voraussetzungen

Die räumlichen Tools selbst werden konvertiert; dies sind Voraussetzungen an die Eingabe.

- **Das GeoFile-Format `.geo`.** Das proprietäre binäre GeoFile von Alteryx hat
  keinen offenen Reader, daher schlägt der Import einer solchen Datei kontrolliert fehl, statt zur Laufzeit abzustürzen.
  Exportieren Sie die Ebene in Alteryx erneut in ein Standard-Geodatenformat
  (Shapefile oder GeoJSON) und importieren Sie stattdessen dieses; andere Geodatenformate
  sind nicht betroffen. Siehe
  [Räumliche Alteryx-Workflows migrieren](/de/guides/workflows/migrate-spatial-alteryx-workflows/#räumliche-eingaben-paketieren).
- **Das Spatial-Info-Maß Peano key.** Der Peano key ist ein proprietärer räumlicher Alteryx-Index
  ohne öffentliche Spezifikation, daher überspringt ein Spatial Info, das ihn anfordert,
  diese eine Spalte und nennt sie in einem Hinweis. Jedes andere Spatial-Info-Maß
  (Fläche, Länge, Schwerpunkt, umschließendes Rechteck, Objekttyp, Teil- und Punkt-
  anzahlen sowie Endpunkte) wird konvertiert.
- **Projizierte Create-Points-Koordinaten.** Create Points konvertiert
  Gleitkomma- und Ganzzahlkoordinaten (×1.000.000) für Längen-/Breitengrad direkt.
  Koordinaten, die bereits in einem projizierten System vorliegen, müssen zuvor vorgelagert in WGS84-Längen-/Breitengrad umprojiziert werden,
  da der Workflow nicht festhält, welche Projektion sie verwenden.

## Abdeckung der Calgary-Tools

Eine Alteryx-Calgary-Datenbank (`.cydb`) ist ein proprietärer indizierter Speicher, den PlaidCloud nicht öffnen kann. Die Konvertierung behandelt jede als Stellvertreter einer gewöhnlichen PlaidCloud-Tabelle mit dem Namen `calgary_<database name>`, sodass die darauf aufbauenden Tools als gewöhnliche Tabellenoperationen konvertiert werden, statt rundweg abgelehnt zu werden. Wie die Stellvertretertabelle funktioniert, steht unter [Calgary-Datenbanken](/de/guides/workflows/migrate-alteryx-workflows/#calgary-datenbanken), und zu den Tools für den Indexabgleich siehe [Calgary Join und Cross Count Append](/de/guides/workflows/migrate-alteryx-workflows/#calgary-join-und-cross-count-append).

| Alteryx-Calgary-Tool | PlaidCloud-Route | Konvertiert |
| --- | --- | --- |
| Calgary Loader | Table Extract, das `calgary_<database>` schreibt | Ja, sobald die Datenbank benannt ist und mindestens ein Datenfeld speichert. |
| Calgary Input | Dynamische Dokumenteneingabe, die `calgary_<database>` liest, mit der gespeicherten Abfrage als Filter | Ja, einschließlich einer Abfrage aus einem Or oder in einem Not sowie eines Contains- oder Starts-with-Filters (neu aufgebaut als SQL LIKE). Wird bei einer Abfrage mit räumlichem Lookup und bei Begrenzungen durch Skip Records/Max Records abgelehnt. |
| Calgary Input (Count Only) / Calgary Cross Count | Aggregattransformation über `calgary_<database>` | Ja, einschließlich eines Buckets aus einem Or oder in einem Not. Wird bei einem Cross über mehr als ein benutzerdefiniertes Feld und bei einem Count-Only-Lesevorgang abgelehnt, der keine zu zählende Spalte nennt. |
| Calgary Join | Dynamische Dokumenteneingabe, die jeden Datensatz ihrer Eingabe mit `calgary_<database>` abgleicht | Wenn das eingehende Feld ein einfacher Wert ist, der mit einem Werteindex abgeglichen wird, einschließlich des Modus Count Only, der die von jedem Eingabedatensatz getroffenen Datenbankdatensätze zählt, wobei ein Datensatz ohne Treffer null zählt. Wird abgelehnt, wenn das Feld räumlich ist (als Spatial Match neu aufbauen) oder sein Typ nicht aufgelöst ist, bei Joins mit Bereichsindex oder mit angeschlossener Unmatched-Ausgabe, bei einem Join ohne Abgleichsfeld und bei einem Join, an dessen Eingabe nichts angeschlossen ist. |
| Calgary Cross Count Append | Dynamische Dokumenteneingabe, die jeden Datensatz abgleicht, dann ein gezählter Join über `calgary_<database>` | Wenn das eingehende Feld ein einfacher Wert ist, der mit einem Werteindex abgeglichen wird: Es zählt pro Eingabedatensatz die getroffenen Datenbankdatensätze, und ein Datensatz ohne Treffer zählt null. Wird bei einem räumlichen oder nicht aufgelösten Index (als Spatial Match neu aufbauen), einem Cross-Count-Raster mit benutzerdefinierten Werten, einem Bereichsindex und einem Abgleich ohne Feldangabe abgelehnt. |

### Bekannte Calgary-Voraussetzungen

Die meisten davon sind Voraussetzungen an die Eingabe und keine Konvertierungsgrenzen.

- **Ein Abgleich mit räumlichem Index muss als Spatial Match neu aufgebaut werden.** Ein Calgary Join oder Cross Count Append, der gegen einen räumlichen Index abgleicht, wird abgelehnt und nennt die Stellvertretertabelle. Der Workflow hält den Namen des Index fest, aber nicht, ob er gewöhnliche Werte oder räumliche Geometrie enthält, und ein Wertabgleich (ein Equi-Join) und ein räumlicher Abgleich (Punkt-in-Polygon) sind unterschiedliche Operationen. Exportieren Sie die Datenbank in eine Tabelle und bauen Sie den Abgleich als Join (Werteindex) oder Spatial Match (räumlicher Index) neu auf.
- **Ein durch Skip Records oder Max Records begrenzter Lesevorgang braucht eine explizite Reihenfolge.** Die exportierte Stellvertretertabelle enthält keine Datensatzreihenfolge. Fügen Sie beim Export daher eine Ordnungsspalte hinzu, wenn Sie die ersten oder letzten N Datensätze nach Position benötigen.
- **Eine demografische oder Referenzdatenbank muss zuerst geladen werden.** Ein Calgary-Lesevorgang, bevor seine Datenbank geladen wurde, stoppt und nennt die zu erstellende Tabelle. Die `.cydb`-Datei selbst hat keinen offenen Reader. Exportieren Sie sie daher in Alteryx erneut (ein Calgary Input in ein Output-Data-Tool, das CSV oder Parquet schreibt) und importieren Sie sie als die benannte Tabelle, siehe [Nicht lesbare .cydb-Datenbanken (Calgary)](/de/guides/workflows/troubleshoot-alteryx-imports/#nicht-lesbare-cydb-datenbanken-calgary). Das ist der häufige Fall bei den lizenzierten demografischen und Referenz-`.cydb`-Dateien, die Alteryx mitliefert (Experian, Census und ähnliche): Kein Konverter kann diese Drittanbieterdaten reproduzieren, bringen Sie daher Ihre eigenen lizenzierten Referenzdaten mit und laden Sie sie in die benannte Tabelle, genau wie bei den Referenzdaten des Geocoders.
- **Ein Calgary Loader, der kein Datenfeld speichert, wird nicht konvertiert**, da die geschriebene Tabelle keine Spalten hätte.
- **Ein Cross-Count-Raster mit benutzerdefinierten Werten wird noch nicht konvertiert.** Ein einzelnes einfaches Cross-Count-Feld wird konvertiert (es zählt pro Eingabedatensatz die passenden Datenbankdatensätze), doch ein Raster *benannter* benutzerdefinierter Werte würde pro Wert eine Zählspalte anhängen, und Alteryx dokumentiert weder, wie viele Spalten das sind, noch wie sie heißen. Für eine künftige Version vorgemerkt, bis ein Referenzexport vorliegt, aus dem sich der Spaltenvertrag ableiten lässt.

Wert-, Bereichs-, Contains- und Starts-with-Abfragen werden alle in einen Filter konvertiert; nur eine Abfrage mit räumlichem Lookup, eine Indexoperation ohne Äquivalent auf Spaltenebene, wird nicht konvertiert.

## Verbindung zu externen Systemen

Die Konnektor-Endpunkte von Alteryx (Salesforce, HTTP, Google Analytics, Cassandra,
E-Mail, Hadoop und Spark, jeweils in beide Richtungen) werden nicht konvertiert, da
PlaidCloud diese Systeme über eine Verbindung erreicht und nicht über ein
Tool auf der Arbeitsfläche. Jeder wird namentlich abgelehnt und nennt, wohin die Arbeit
gehört:

| Alteryx-Tool | Wohin es in PlaidCloud gehört |
| --- | --- |
| Salesforce Input / Output | Eine **Salesforce**-Verbindung |
| Anaplan | Eine **Anaplan**-Verbindung |
| HTTP Input | Ein Schritt **REST-Anfrage** gegen eine **REST**-Verbindung |
| Google Analytics Input | **Import: Singer-Quelle** mit dem Google-Analytics-Tap |
| Cassandra Input | **Import: Singer-Quelle** mit dem Cassandra-Tap |
| Email Input | **Import: Singer-Quelle** mit dem GMail-Tap |
| Hadoop Input / Output | **Import: SQL** / **Export: SQL** über eine Hive-, Impala- oder Presto-Verbindung |
| Spark Input / Output | **Import: SQL** / **Export: SQL** über eine Databricks-Verbindung |

Vier davon haben überhaupt keinen Schreibpfad. PlaidCloud liest Google Analytics
und Cassandra, schreibt aber nie dorthin, daher wird ein Tool Google Analytics Output oder
Cassandra Output stattdessen zu einem **Export: SQL** an ein unterstütztes Ziel.
E-Mail ist ebenfalls kein Datenziel: **Benachrichtigen: E-Mail** sendet eine
Benachrichtigung an Personen, daher wird ein Tool Email Output zu einem Export-Schritt plus einer
separaten Benachrichtigung. Die **Anaplan**-Verbindung ist auf dieselbe Weise schreibgeschützt:
Sie liest eine gespeicherte Ansicht, führt eine bereits vorhandene Exportaktion aus oder lädt
Listen in eine PlaidCloud-Dimension, aber es gibt keinen PlaidCloud-Schritt, der
zurück nach Anaplan schreibt.

## Einen konvertierten Workflow validieren

Validieren Sie bei Produktions-Workflows die konvertierten Ausgaben anhand vertrauenswürdiger Alteryx-
Ausgaben. Die PlaidCloud-Validierung konzentriert sich auf Schema, Zeilenanzahl und Zeilenwerte
und ignoriert die Zeilenreihenfolge, sofern der Workflow nicht davon abhängt. Spezialisierte
Operationen (räumlich, Fuzzy Matching, OCR, NLP, Berichte) laufen über verwaltete
Job-Executors, die den Workflow cloudnativ halten; Pipelines für maschinelles Lernen
werden in die nativen Schritte [ML: Modell trainieren](/de/reference/workflow-steps/machine-learning/ml-train/)
und [ML: Bewerten](/de/reference/workflow-steps/machine-learning/ml-score/) konvertiert.
Die durchgängige Anleitung zu Import und Validierung finden Sie unter [Alteryx-Workflows migrieren](/de/guides/workflows/migrate-alteryx-workflows/).
