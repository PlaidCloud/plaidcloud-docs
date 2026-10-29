---
title: Tabellen und Ansichten verwalten
description: Verwalten Sie Tabellen und Ansichten in PlaidCloud-Projekten, einschließlich Erstellung, Konfiguration, Berechtigungen und Organisation der Datenobjekte.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

PlaidCloud bietet die Möglichkeit, Tabellen zu organisieren und zu verwalten, einschließlich Bezeichnungen. Tabellen stehen allen Workflows innerhalb eines Projekts zur Verfügung und bieten zahlreiche Werkzeuge und Optionen.


Zusätzlich zu Tabellen bietet PlaidCloud auch Ansichten, die auf Tabellendaten basieren. Ansichten werden sofort aktualisiert, wenn sich die zugrunde liegenden Tabellen ändern, und sparen außerdem Speicherplatz.



Zu den Optionen gehören:


* Dieselbe Tabelle kann auf mehreren Pfaden in der Hierarchie vorhanden sein (alternative Hierarchien)
* Tabellen lassen sich mit Tags versehen, um sie leichter zu suchen und in PlaidCloud-Prozesse einzubinden
* Tabellen können versioniert werden
* Tabellen können veröffentlicht werden, damit sie für Dashboard-Visualisierungen verfügbar sind

PlaidCloud verwendet ein pfadbasiertes System zur Organisation von Tabellen, ähnlich der Navigation durch eine Reihe von Ordnern. Das ermöglicht eine flexiblere und logischere Organisation. Mit diesem System lassen sich Tabellen innerhalb einer Hierarchie verschieben, und es können mehrere Verweise auf eine Tabelle von verschiedenen Stellen der Hierarchie aus angelegt werden (alternative Hierarchien). Durch die Verwaltung von Tabellen auf diese Weise kann die Struktur betriebliche Anforderungen, Berichtswesen und Kontrolle widerspiegeln.



## Tabellen finden


Verwenden Sie das Filterfeld unten links in der Hierarchie, um Tabellennamen und Bezeichnungen zu durchsuchen. Die Treffer werden oben in der Hierarchie angezeigt.


### Nach Workflow

Der Ordner **By Workflow** am Ende der Registerkarte **Tabellen** gruppiert Tabellen unter jedem Workflow, der sie liest oder schreibt. Öffnen Sie einen Workflow, um seine Tabellen zu sehen. Der Ordner ist eine Ansicht derselben Tabellen, daher können Sie darin nichts verschieben oder kopieren.


### Nach Spalte

Geben Sie in das Suchfeld für Spalten auf der Registerkarte **Tabellen** einen Spaltennamen ein, um nur die Tabellen anzuzeigen, die eine Spalte mit diesem Namen haben. Wählen Sie **Enthält**, um einen Teil eines Spaltennamens statt des gesamten Namens abzugleichen. Leeren Sie das Feld, um wieder alle Tabellen anzuzeigen. Eine umfangreiche Suche kann seitenweise Ergebnisse liefern, und die Statuszeile zeigt an, wenn sie noch läuft oder unvollständig sein kann.

Wählen Sie **Column Tree**, um in einem eigenen Fenster zu suchen. Jede Tabelle, die die Spalte hat, öffnet sich mit zwei Listen:

* **Fed by**: die Tabellen, die die Spalte liefern
* **Feeds**: die Tabellen, die die Spalte anschließend weiter speist

Ein über MCP verbundener KI-Assistent findet dieselben Tabellen mit `table_find(column=...)`, wobei der gesamte Name oder ein Teil davon abgeglichen wird.


### Werte suchen

Um herauszufinden, welche Tabellen einen Wert enthalten, wählen Sie auf der Registerkarte **Tabellen** die Option **Search Values**, oder klicken Sie mit der rechten Maustaste auf eine Tabelle und wählen Sie **Search Value**, um nur in dieser Tabelle zu suchen. Geben Sie den Wert ein, wählen Sie **Enthält**, um einen Teil eines Werts abzugleichen, und wählen Sie **Suchen**. Jede Tabelle, die den Wert enthält, wird mit den Spalten, in denen er vorkommt, und einigen der übereinstimmenden Werte aufgelistet.

Beachten Sie vor der Suche Folgendes:

* Sie sehen nur Zeilen, die Sie ohnehin öffnen könnten. Die Sicherheit auf Zeilenebene gilt für jede Suche.
* Der Abfrageverlauf Ihres Warehouse zeichnet die Werte auf, nach denen Sie suchen.
* Die Suche umfasst die Textspalten von Tabellen. Tabellen, die noch nicht erstellt wurden, werden übersprungen und in einer Warnung genannt.
* Die Ergebnisse kommen seitenweise. Wenn die Statuszeile meldet, dass die Suche vorzeitig beendet wurde, wählen Sie **Search more**, um mit den noch nicht durchsuchten Tabellen fortzufahren.

Ein über MCP verbundener KI-Assistent verwendet `table_value_search`. Es liefert die Tabellen und Spalten, die den Wert enthalten, aber nie die Werte selbst. Wenn Sie den KI-Assistenten in einem Projekt bitten, einen Wert zu finden, sendet Weave die Namen der passenden Tabellen und Spalten an den Anbieter des Sprachmodells.



## CSV-Datei importieren

**So wandeln Sie eine CSV-Datei in eine neue Tabelle in diesem Projekt um:**

1. Ziehen Sie die Datei von Ihrem Computer auf die Liste **Tabellen** des Projekts, oder wählen Sie in der Symbolleiste **Neu** > **Tabelle aus CSV-Datei** und legen Sie die Datei im Feld ab oder klicken Sie auf **CSV-Datei auswählen**.
2. PlaidCloud lädt die Datei auf Ihr **Personal Temp Drive** hoch, oder auf das **Temp Drive** des Workspace, wenn Sie keines haben, und importiert sie in eine neue Tabelle auf der obersten Ebene der Liste, benannt nach der Datei: `Sales Data.csv` wird zu `sales_data`. Wenn das Projekt bereits eine Tabelle mit diesem Namen hat, erhält die neue eine Nummer, etwa `sales_data_2`.
3. Die Liste wird aktualisiert, die neue Tabelle ist ausgewählt, und **Ihre Daten auf einen Blick** öffnet sich dazu. Was das Panel zeigt, lesen Sie unter [Mit der eigenen CSV-Datei beginnen](/de/get-started/quickstart/#mit-der-eigenen-csv-datei-beginnen).

Es werden nur Dateien mit der Endung `.csv` akzeptiert. Sie benötigen die Berechtigung, Tabellen zu erstellen und in den Dokumentspeicher zu schreiben, und ein gesperrtes Projekt akzeptiert keine CSV-Datei, bis es entsperrt ist. Wenn der Import fehlschlägt, nennt das Fenster den Grund, und Ihr Projekt bleibt unverändert. PlaidCloud löscht die hochgeladene Datei vom Temp Drive, sobald der Import abgeschlossen ist, unabhängig vom Erfolg; andernfalls löscht das Temp Drive sie nach einem Tag.

## Verschieben


**So verschieben Sie eine Tabelle:**


1. Ziehen Sie sie in den Ordner, in dem sie liegen soll

## Umbenennen


**So benennen Sie eine Tabelle um:**


1. Klicken Sie mit der rechten Maustaste auf die Tabelle
2. Wählen Sie die Option zum Umbenennen
3. Geben Sie den neuen Namen ein und speichern Sie ihn
4. Die Tabelle ist nun umbenannt, behält aber ihre ursprüngliche eindeutige Kennung.

## Leeren


**So leeren Sie eine Tabelle:**


1. Wählen Sie die Tabellen in der Hierarchie aus ‘
2. Klicken Sie in der oberen Symbolleiste auf die Schaltfläche „Leeren“.

*Hinweis: Sie können eine einzelne Tabelle oder mehrere Tabellen leeren*



## Löschen


**So löschen Sie eine Tabelle:**


1. Wählen Sie die Tabellen in der Hierarchie aus
2. Klicken Sie in der oberen Symbolleiste auf die Schaltfläche „Löschen“
3. Beim Löschen wird geprüft, ob die Tabelle von Workflow-Schritten oder Ansichten verwendet wird. Ist das der Fall, werden Sie aufgefordert, diese Zuordnungen zu entfernen, bevor das Löschen erfolgen kann.

*Hinweis: Sie können die Tabellen auch zwangsweise löschen. Beim erzwungenen Löschen bleiben Verweise defekt, daher sollten Sie es sparsam einsetzen.*


### Zuletzt gelesen

Das Löschfenster zeigt, wann die Tabelle zuletzt gelesen wurde, zum Beispiel **Last read 3 days ago by** eine Person oder ein Schritt, damit Sie eine Tabelle, die niemand verwendet, von einer unterscheiden können, die noch in Gebrauch ist. PlaidCloud entnimmt dies dem eigenen Abfrageverlauf Ihres Warehouse und lässt Lesezugriffe der eigenen Wartungsvorgänge aus.

| Warehouse | Was erforderlich ist |
| --- | --- |
| Snowflake | Lesezugriffe stammen aus dem Access History, das Snowflake mit bis zu etwa 3 Stunden Verzögerung aufzeichnet. Die Rolle der Verbindung benötigt die Datenbankrolle `SNOWFLAKE.GOVERNANCE_VIEWER` (`IMPORTED PRIVILEGES` auf der Datenbank `SNOWFLAKE` funktioniert ebenfalls). Snowflake Standard Edition hat kein Access History. |
| Databricks | Lesezugriffe stammen aus der Lineage-Tabelle, die Databricks ebenfalls mit Verzögerung aufzeichnet, sodass ein kürzlicher Lesezugriff möglicherweise noch nicht angezeigt wird. Die Identität der Verbindung benötigt `USE CATALOG` auf `system`, `USE SCHEMA` auf `system.access` und `SELECT` auf `system.access.table_lineage`. |
| PlaidCloud Lakehouse | Der Leseverlauf ist noch nicht verfügbar. Das Fenster zeigt **Read history incomplete**. |

Wenn Sie Ihr Warehouse verbinden, empfiehlt die [Verbindungsprüfung](/de/guides/connections/external-lakehouse/#3-prüfen-und-dann-verwenden) jede dieser Berechtigungen, die fehlt, jeweils mit der auszuführenden Anweisung. Sie werden empfohlen, sind aber nicht erforderlich: Ohne sie wird das Warehouse trotzdem verbunden, und das Fenster zeigt **Read history incomplete**.

Wenn PlaidCloud nicht den gesamten Verlauf lesen kann, lautet die Zeile **Read history incomplete** und meldet nie stattdessen „no reads“. Jeder mit direktem SQL-Zugriff auf Ihr Warehouse kann ein Sitzungs-Tag setzen, das ändert, wie seine eigenen Lesezugriffe gekennzeichnet werden.

Ein über MCP verbundener KI-Assistent erhält dieselbe Antwort mit `table_describe(include=['last_read'])`.



## Sehen, wo eine Tabelle verwendet wird


Wenn Sie eine Tabelle auswählen, öffnet sich ihr Detailpanel, das die Workflow-Schritte auflistet, die sie berühren:


* **Tabelle erstellt von**: Schritte, die in die Tabelle schreiben
* **Tabelle liefert Daten an**: Schritte, die aus ihr lesen
* **Kann auf diese Tabelle verweisen**: Schritte, die über eine Variable, die sich nicht auflösen lässt, auf eine Tabelle zugreifen. Dieser Abschnitt erscheint nur, wenn es solche Schritte gibt.


Ein Schritt kann eine Tabelle direkt benennen oder sie über einen Pfad erreichen, der eine Variable enthält, etwa `/Periods/{period}/Sales`. Hat diese Variable einen aktuellen Wert, erscheint der Schritt in den ersten beiden Listen mit einem Informationssymbol daneben. Bewegen Sie den Mauszeiger über die Zeile, um den Pfad so zu sehen, wie der Schritt ihn speichert.


Betrachten Sie diese Zeilen als die schwächere Antwort, die sie sind. Sie beschreiben, was eine jetzt gestartete Ausführung berühren würde, nicht alles, was die Tabelle je berührt hat. Ändern Sie die Variable, und es wird eine andere Tabelle gelesen.


Manche Variablen lassen sich nicht auflösen. Entweder hat nichts die Variable gesetzt, oder der Wert, den eine Ausführung verwendet, stammt nicht aus dem Gespeicherten: Ein Workflow Loop bezieht seine Variablen beim Durchlaufen aus Daten, ein Set-Variable-Schritt weist während der Ausführung zu, ein Makro erhält seine Variablen von dem Schritt, der es aufruft, und eine von einem Sensor gestartete Ausführung trägt die eigenen Angaben dieses Sensors. In jedem Fall ist das, was zwischen den Ausführungen gespeichert ist, ein Rest der letzten Ausführung und kein Wert, dem Sie vertrauen sollten. Statt diese zu einer Tabelle aufzulösen, die falsch sein könnte, listet PlaidCloud die Schritte namentlich unter **Kann auf diese Tabelle verweisen** auf, zusammen mit der Variable, die nicht aufgelöst werden konnte, damit Sie sie öffnen und prüfen können.


Ein Schritt, den Ihre Rolle nicht sehen kann, wird dennoch aufgelistet, damit Sie wissen, dass die Tabelle verwendet wird, jedoch ohne seinen Namen oder Workflow, und Sie können ihn nicht öffnen. Er zählt beim Löschen der Tabelle trotzdem mit. Ein Schritt, den Sie sehen können, wird ohne einen Workflow aufgelistet, den Ihre Rolle nicht sehen darf. Vor einem Architect wird nichts verborgen.


*Hinweis: Wenn Sie Tabellen aus der Liste **Tabellen** löschen, gilt ein Schritt, der eine Tabelle über einen Pfad erreicht, mit oder ohne Variable, als Verwender, auch wenn sich seine Variable nicht auflösen lässt. Das Löschfenster listet den Schritt auf, und das Löschen wird nur fortgesetzt, wenn Sie es erzwingen.*



## Neue Verzeichnisstruktur erstellen


**So fügen Sie einen neuen Ordner hinzu:**


1. Klicken Sie in der Symbolleiste auf die Schaltfläche „Neuer Ordner“

**So fügen Sie einen Ordner zu einem vorhandenen Ordner hinzu:**


1. Klicken Sie mit der rechten Maustaste auf den Ordner
2. Wählen Sie „Neuer Ordner“


## Daten anzeigen (Tabellen-Explorer)


Tabellendaten werden mit dem Data Explorer angezeigt. Der Data Explorer bietet eine Rasteransicht der Daten sowie eine spaltenweise Zusammenfassung von Werten und Statistiken. Filtern per Mausklick und der Export in gängige Dateiformate sind beide verfügbar. Die Filterauswahl kann außerdem als Extract-Schritt gespeichert werden, der in einem Workflow verwendet werden kann.



## Tabelle für Berichte veröffentlichen


Dashboard-Visualisierungen sind bewusst auf Tabellen beschränkt, die veröffentlicht wurden. Beim Veröffentlichen einer Tabelle können Sie einen eindeutigen Namen vergeben, der die Daten besser unterscheidet. Das kann nützlich sein, wenn die Tabelle in dem Workflow-Teil, der sie erzeugt hat, einen eher unklaren Namen trägt, aber für die Ersteller von Dashboards einen verständlicheren Namen benötigt.


Veröffentlichte Tabellen haben keine zugeordneten Pfade. Sie erscheinen als Liste von Tabellen zur Verwendung im Dashboard-Bereich.



## Tabelle für Anzeigerollen markieren


Die Anzeige von Tabellen durch verschiedene Rollen lässt sich steuern, indem Sie die Kontrollkästchen Explorer oder Manager anklicken. Wenn mehrere Tabellen aktualisiert werden sollen, wählen Sie die Tabellen in der Hierarchie aus und wählen Sie im Menü „Aktionen“ der oberen Symbolleiste die gewünschte Anzeigerolle.



## Memos zur Beschreibung von Tabelleninhalten


Fügen Sie einer Tabelle ein Memo hinzu, um die Daten besser zu verstehen.



## Form, Größe und Zeitpunkt der letzten Aktualisierung einer Tabelle anzeigen


Die Anzahl der Zeilen und Spalten sowie die Datengröße jeder Tabelle werden in der Tabellenhierarchie angezeigt. Bei sehr großen Tabellen (mehrere Millionen Zeilen) kann die Zeilenanzahl geschätzt sein, und ein Hinweis zeigt die ungefähre Zeilenanzahl an.



## Weitere Tabellenattribute anzeigen


**So zeigen und bearbeiten Sie weitere Tabellenattribute:**


1. Wählen Sie eine Tabelle aus
2. Klicken Sie rechts auf das Tabellenkontext-Formular, um es anzuzeigen.


## Eine Tabelle duplizieren


**So duplizieren Sie eine Tabelle:**


1. Wählen Sie die Tabelle aus
2. Klicken Sie in der oberen Symbolleiste auf die Schaltfläche „Duplizieren“.


## Einen Dateneditor aus einer Tabelle erstellen


Sie können eine Tabelle in einem Schritt in einen konfigurierten Dateneditor umwandeln: Wählen Sie die Tabelle aus und wählen Sie **Dateneditor aus Tabelle erstellen** im Menü **Neu** oder im Kontextmenü. PlaidCloud untersucht die Spalten der Tabelle und erstellt die Eingabesteuerelemente des Editors vor. Einzelheiten finden Sie unter [Einen Dateneditor aus einer Tabelle erstellen](/de/guides/projects/managing-data-editors/#einen-dateneditor-aus-einer-tabelle-erstellen).
