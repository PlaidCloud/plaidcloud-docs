---
title: Tabellen und Ansichten verwalten
description: Verwalten Sie Tabellen und Ansichten in PlaidCloud-Projekten, einschließlich Erstellung, Konfiguration, Berechtigungen und Organisation der Datenobjekte.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

PlaidCloud bietet die Möglichkeit, Tabellen zu organisieren und zu verwalten, einschließlich Labels. Tabellen stehen allen Workflows innerhalb eines Projekts zur Verfügung und bieten viele Werkzeuge und Optionen.


Zusätzlich zu Tabellen bietet PlaidCloud auch Ansichten, die auf Tabellendaten basieren. Ansichten ermöglichen sofortige Aktualisierungen, wenn sich die zugrunde liegenden Tabellen ändern, und sparen Speicherplatz.



Zu den Optionen gehören:


* Dieselbe Tabelle kann an mehreren Pfaden in der Hierarchie existieren (alternative Hierarchien)
* Tabellen lassen sich mit Tags versehen, damit sie leichter gesucht und in PlaidCloud-Prozesse einbezogen werden können
* Tabellen können versioniert werden
* Tabellen können veröffentlicht werden, damit sie für Dashboard-Visualisierungen zur Verfügung stehen

PlaidCloud verwendet ein pfadbasiertes System zur Organisation von Tabellen, ähnlich dem, mit dem Sie durch eine Reihe von Ordnern navigieren. Das ermöglicht eine flexiblere und logischere Organisation der Tabellen. Mit diesem System können Tabellen innerhalb einer Hierarchie verschoben werden, oder es können mehrere Verweise auf eine Tabelle von verschiedenen Stellen der Hierarchie aus erstellt werden (alternative Hierarchien). Durch die Verwaltung von Tabellen auf diese Weise kann die Struktur betriebliche Anforderungen, Berichtswesen und Kontrolle widerspiegeln.



## Tabellen finden


Verwenden Sie das Filterfeld unten links in der Hierarchie, um Tabellennamen und Labels zu durchsuchen. Die Treffer werden oben in der Hierarchie angezeigt.


### Nach Workflow

Der Ordner **Nach Workflow** am Ende der Registerkarte **Tabellen** gruppiert Tabellen unter jedem Workflow, der sie liest oder schreibt. Öffnen Sie einen Workflow, um seine Tabellen zu sehen. Der Ordner ist eine Ansicht derselben Tabellen, daher können Sie daraus nichts verschieben oder kopieren.


### Nach Spalte

Geben Sie im Spaltensuchfeld auf der Registerkarte **Tabellen** einen Spaltennamen ein und drücken Sie die Eingabetaste, oder wählen Sie die Lupe daneben, um nur die Tabellen anzuzeigen, die eine Spalte mit diesem Namen haben. Die Suche liest Spaltennamen, nicht die Daten, und ist daher schnell. Wählen Sie **Enthält**, um einen Teil eines Spaltennamens statt des ganzen Namens abzugleichen. Leeren Sie das Feld, um wieder alle Tabellen anzuzeigen. Eine lange Suche kann seitenweise Ergebnisse liefern, und die Statuszeile weist darauf hin, wenn sie noch sucht oder möglicherweise unvollständig ist.

Wählen Sie **Spaltenbaum**, um in einem eigenen Fenster zu suchen. Jede Tabelle mit der Spalte öffnet sich zu zwei Listen:

* **Gespeist von** – die Tabellen, die die Spalte liefern
* **Speist** – die Tabellen, die die Spalte weiter speist

Ein über MCP verbundener KI-Assistent findet dieselben Tabellen mit `table_find(column=...)` und gleicht dabei den ganzen Namen oder einen Teil davon ab.


### Werte suchen

Um herauszufinden, welche Tabellen einen Wert enthalten, wählen Sie im Menü **Aktionen** auf der Registerkarte **Tabellen** die Option **Werte in Daten suchen… (langsam)**, oder klicken Sie mit der rechten Maustaste auf eine Tabelle und wählen Sie sie, um nur in dieser Tabelle zu suchen. Geben Sie den Wert ein, wählen Sie **Enthält**, um einen Teil eines Werts abzugleichen, und wählen Sie **Suchen**. Jede Tabelle, die den Wert enthält, wird mit den Spalten, in denen er vorkommt, und einigen der übereinstimmenden Werte aufgeführt. Doppelklicken Sie auf eine Tabelle oder drücken Sie die Eingabetaste, um sie im Tabellen-Explorer zu öffnen. Eine Spalte öffnet die Tabelle, gefiltert auf die übereinstimmenden Zeilen. Wenn das Spaltensuchfeld Text enthält, trägt es den zu suchenden Wert ein.

Beachten Sie vor der Suche:

* Die Suche liest jede Zeile jeder durchsuchten Tabelle, kann also sehr langsam sein und viele Warehouse-Ressourcen beanspruchen. Das Fenster warnt Sie, und die Suchschaltflächen bleiben deaktiviert, bis eine Suche beendet ist.
* Sie sehen nur Zeilen, die Sie ohnehin öffnen könnten. Die Sicherheit auf Zeilenebene gilt für jede Suche.
* Der Abfrageverlauf Ihres Warehouse zeichnet die Werte auf, nach denen Sie suchen.
* Die Suche umfasst die Textspalten von Tabellen. Tabellen, die noch nicht erstellt wurden, werden übersprungen und in einer Warnung genannt.
* Ergebnisse kommen seitenweise. Wenn die Statuszeile meldet, dass die Suche vorzeitig beendet wurde, wählen Sie **Weiter suchen**, um mit den noch nicht durchsuchten Tabellen fortzufahren.

Ein über MCP verbundener KI-Assistent verwendet `table_value_search`. Es gibt die Tabellen und Spalten zurück, die den Wert enthalten, nie die Werte selbst. Wenn Sie den KI-Assistenten in einem Projekt bitten, einen Wert zu finden, sendet Weave die Namen der passenden Tabellen und Spalten an den Anbieter des Sprachmodells.



## Eine CSV-Datei importieren

**So wandeln Sie eine CSV-Datei in eine neue Tabelle in diesem Projekt um:**

1. Ziehen Sie die Datei von Ihrem Computer auf die Liste **Tabellen** des Projekts, oder wählen Sie in der Symbolleiste **Neu** > **Tabelle aus CSV-Datei** und legen Sie die Datei im Feld ab oder klicken Sie auf **CSV-Datei auswählen**.
2. PlaidCloud lädt die Datei in Ihr **Personal Temp Drive** hoch, oder in das **Temp Drive** des Workspace, wenn Sie keines haben, und importiert sie in eine neue Tabelle auf oberster Ebene der Liste, benannt nach der Datei: `Sales Data.csv` wird zu `sales_data`. Wenn das Projekt bereits eine Tabelle mit diesem Namen hat, erhält die neue eine Nummer, etwa `sales_data_2`.
3. Die Liste wird mit der neuen ausgewählten Tabelle aktualisiert, und **Ihre Daten auf einen Blick** öffnet sich dafür. Was der Bereich zeigt, erfahren Sie unter [Mit Ihrer eigenen CSV-Datei beginnen](/de/get-started/quickstart/#mit-der-eigenen-csv-datei-beginnen).

Es werden nur Dateien akzeptiert, die auf `.csv` enden. Sie benötigen die Berechtigung, Tabellen zu erstellen und in den Dokumentenspeicher zu schreiben, und ein gesperrtes Projekt akzeptiert keine CSV-Datei, bis es entsperrt ist. Wenn der Import fehlschlägt, nennt das Fenster den Grund, und Ihr Projekt bleibt unverändert. PlaidCloud löscht die hochgeladene Datei aus dem temporären Laufwerk, sobald der Import beendet ist, unabhängig davon, ob er erfolgreich war; andernfalls löscht das temporäre Laufwerk sie nach einem Tag.

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
3. Beim Löschen wird geprüft, ob die Tabelle von Workflow-Schritten oder Ansichten verwendet wird. Falls ja, werden Sie aufgefordert, diese Zuordnungen zu entfernen, bevor das Löschen erfolgen kann.

*Hinweis: Sie können die Tabelle(n) auch erzwungen löschen. Das erzwungene Löschen der Tabelle(n) hinterlässt defekte Verweise und sollte daher sparsam eingesetzt werden.*


### Letzter Lesezugriff

Das Löschfenster zeigt, wann die Tabelle zuletzt gelesen wurde, zum Beispiel **Last read 3 days ago by** eine Person oder ein Schritt, damit Sie eine Tabelle, die niemand verwendet, von einer unterscheiden können, die noch in Gebrauch ist. PlaidCloud entnimmt dies dem eigenen Abfrageverlauf Ihres Warehouse und lässt Lesezugriffe aus, die von seiner eigenen Verwaltung stammen.

| Warehouse | Was erforderlich ist |
| --- | --- |
| Snowflake | Lesezugriffe stammen aus dem Access History, das Snowflake mit bis zu etwa 3 Stunden Verzögerung aufzeichnet. Die Rolle der Verbindung benötigt die Datenbankrolle `SNOWFLAKE.GOVERNANCE_VIEWER` (`IMPORTED PRIVILEGES` auf der Datenbank `SNOWFLAKE` funktioniert ebenfalls). Die Snowflake-Edition Standard hat keinen Access History. |
| Databricks | Lesezugriffe stammen aus der Lineage-Tabelle, die Databricks ebenfalls verzögert aufzeichnet, sodass ein aktueller Lesezugriff möglicherweise noch nicht angezeigt wird. Die Identität der Verbindung benötigt `USE CATALOG` auf `system`, `USE SCHEMA` auf `system.access` und `SELECT` auf `system.access.table_lineage`. |
| PlaidCloud Lakehouse | Der Leseverlauf ist noch nicht verfügbar. Das Fenster zeigt **Read history incomplete**. |

Wenn Sie Ihr Warehouse verbinden, empfiehlt [die Verbindungsprüfung](/de/guides/connections/external-lakehouse/#3-prüfen-und-dann-verwenden) alle fehlenden dieser Berechtigungen, jeweils mit der auszuführenden Anweisung. Sie werden empfohlen, nicht vorausgesetzt: Ohne sie verbindet sich das Warehouse, und das Fenster zeigt **Read history incomplete**.

Wenn PlaidCloud den gesamten Verlauf nicht lesen kann, lautet die Zeile **Read history incomplete** und meldet nie stattdessen „keine Lesezugriffe“. Jeder mit direktem SQL-Zugriff auf Ihr Warehouse kann ein Sitzungs-Tag setzen, das ändert, wie seine eigenen Lesezugriffe gekennzeichnet werden.

Ein über MCP verbundener KI-Assistent erhält dieselbe Antwort von `table_describe(include=['last_read'])`.



## Die Spalten einer Tabelle ansehen


Wenn Sie eine Tabelle auswählen, öffnet sich ihr Detailbereich. Sein Abschnitt **Spalten** listet jede Spalte mit ihrem **Typ** und ihrer **Beschreibung** auf, wobei die Beschreibung aus den **Spalteneigenschaften** stammt. Zeigen Sie auf eine Zeile, um eine lange Beschreibung vollständig zu lesen.

Eine Tabelle, die derzeit nicht im Warehouse liegt, weil ihre Daten abgelaufen sind oder kein Schritt sie erstellt hat, hat keine Spalten zum Auflisten. Der Abschnitt weist darauf hin und zeigt, wie viele Spalten die Tabelle hat. Führen Sie einen Schritt aus, der die Tabelle schreibt, um sie aufzulisten.


## Sehen, wo eine Tabelle verwendet wird


Wenn Sie eine Tabelle auswählen, öffnet sich ihr Detailbereich, der die Workflow-Schritte auflistet, die sie berühren:


* **Tabelle erstellt von** – Schritte, die in die Tabelle schreiben
* **Tabelle liefert Daten an** – Schritte, die aus ihr lesen
* **Kann auf diese Tabelle verweisen** – Schritte, die eine Tabelle über eine Variable erreichen, die sich nicht auflösen lässt. Dieser Abschnitt erscheint nur, wenn es solche Schritte gibt.


Ein Schritt kann eine Tabelle direkt benennen oder sie über einen Pfad erreichen, der eine Variable enthält, etwa `/Periods/{period}/Sales`. Wenn diese Variable einen aktuellen Wert hat, erscheint der Schritt in den ersten beiden Listen mit einem Informationssymbol daneben. Zeigen Sie auf die Zeile, um den Pfad zu sehen, wie der Schritt ihn speichert.


Behandeln Sie diese Zeilen als die schwächere Antwort, die sie sind. Sie beschreiben, was eine jetzt gestartete Ausführung berühren würde – nicht alles, was die Tabelle je berührt hat. Ändern Sie die Variable, und es wird eine andere Tabelle gelesen.


Manche Variablen lassen sich nicht auflösen. Entweder hat nichts die Variable gesetzt, oder der Wert, den eine Ausführung verwendet, stammt nicht aus dem Gespeicherten – ein Workflow-Loop-Schritt bezieht seine Variablen beim Durchlaufen aus Daten, ein Set-Variable-Schritt weist während der Ausführung zu, ein Makro erhält seine Variablen von dem Schritt, der es aufruft, und eine von einem Sensor gestartete Ausführung trägt dessen eigene Details. In jedem Fall ist das, was zwischen Ausführungen gespeichert ist, ein Rest der letzten Ausführung und kein Wert, dem man vertrauen kann. Statt diese zu einer Tabelle aufzulösen, die falsch sein kann, listet PlaidCloud die Schritte mit Namen unter **Kann auf diese Tabelle verweisen** auf, mit der Variablen, die es nicht auflösen konnte, damit Sie sie öffnen und prüfen können.


Ein Schritt, den Ihre Rolle nicht sehen kann, wird dennoch aufgeführt, damit Sie wissen, dass die Tabelle verwendet wird, aber ohne Namen oder Workflow, und Sie können ihn nicht öffnen. Er zählt weiterhin, wenn Sie die Tabelle löschen. Ein Schritt, den Sie sehen können, wird ohne einen Workflow aufgeführt, den Ihre Rolle ausblendet. Vor einem Architect wird nichts ausgeblendet.


*Hinweis: Wenn Sie Tabellen aus der Liste **Tabellen** löschen, gilt ein Schritt, der eine Tabelle über einen Pfad erreicht, mit oder ohne Variable, als Verwendung, auch wenn sich seine Variable nicht auflösen lässt. Das Löschfenster listet den Schritt auf, und das Löschen wird nur fortgesetzt, wenn Sie es erzwingen.*



## Eine neue Verzeichnisstruktur erstellen


**So fügen Sie einen neuen Ordner hinzu:**


1. Klicken Sie in der Symbolleiste auf die Schaltfläche „Neuer Ordner“

**So fügen Sie einen Ordner zu einem vorhandenen Ordner hinzu:**


1. Klicken Sie mit der rechten Maustaste auf den Ordner
2. Wählen Sie „Neuer Ordner“


## Daten ansehen (Tabellen-Explorer)


Tabellendaten werden mit dem Daten-Explorer angezeigt. Der Daten-Explorer bietet eine Rasteransicht der Daten sowie eine spaltenweise Zusammenfassung von Werten und Statistiken. Filtern per Point-and-Click und der Export in gängige Dateiformate sind beide verfügbar. Die Filterauswahl kann auch als Extract-Schritt gespeichert werden, der in einem Workflow verwendet werden kann.



## Tabelle für Berichte veröffentlichen


Dashboard-Visualisierungen sind bewusst auf Tabellen beschränkt, die veröffentlicht wurden. Beim Veröffentlichen einer Tabelle können Sie einen eindeutigen Namen vergeben, der die Daten unterscheidbar macht. Das kann nützlich sein, wenn die Tabelle in dem Teil des Workflows, der sie erzeugt hat, einen eher unklaren Namen hat, für diejenigen, die Dashboards erstellen, aber einen klareren Namen braucht.


Veröffentlichte Tabellen haben keine zugeordneten Pfade. Sie erscheinen als Liste von Tabellen zur Verwendung im Dashboard-Bereich.



## Tabelle für Anzeigerollen markieren


Die Ansicht von Tabellen durch verschiedene Rollen lässt sich über die Kontrollkästchen Explorer oder Manager steuern. Wenn mehrere Tabellen aktualisiert werden sollen, wählen Sie die Tabellen in der Hierarchie aus und wählen Sie im Menü „Aktionen“ der oberen Symbolleiste die gewünschte Anzeigerolle.



## Notizen zur Beschreibung von Tabelleninhalten


Fügen Sie einer Tabelle eine Notiz hinzu, um die Daten besser zu verstehen.



## Form, Größe und Zeitpunkt der letzten Aktualisierung einer Tabelle ansehen


Die Anzahl der Zeilen und Spalten sowie die Datengröße jeder Tabelle werden in der Tabellenhierarchie angezeigt. Bei sehr großen Tabellen (mehrere Millionen Zeilen) kann die Zeilenanzahl geschätzt sein, und ein Hinweis auf die ungefähre Zeilenanzahl wird angezeigt.



## Weitere Tabellenattribute ansehen


**So sehen und bearbeiten Sie weitere Tabellenattribute:**


1. Wählen Sie eine Tabelle aus
2. Klicken Sie rechts auf das Tabellenkontextformular.


## Eine Tabelle duplizieren


**So duplizieren Sie eine Tabelle:**


1. Wählen Sie die Tabelle aus
2. Klicken Sie in der oberen Symbolleiste auf die Schaltfläche „Duplizieren“.


## Eine Panel-App aus einer Tabelle erstellen


Wählen Sie eine Tabelle oder Ansicht und wählen Sie **Panel-App erstellen** im Menü **Neu** oder im Kontextmenü (Rechtsklick). Der Dialog **Neue Studio-App** öffnet sich mit dem bereits gewählten Projekt und der Tabelle. Die App übernimmt den Namen der Tabelle; ändern Sie ihn nach Belieben und wählen Sie dann **Erstellen**, und Panel Studio öffnet sie mit Weave bereit, ihre erste Seite zu erstellen. Der Befehl ist verfügbar, wenn Sie eine einzelne Tabelle oder Ansicht auswählen, Bearbeitungszugriff auf das Projekt haben und das Projekt nicht schreibgeschützt ist. Siehe [Eine Panel-App erstellen](/de/guides/panel-apps/creating/#mit-einer-tabelle-beginnen).


## Sehen, was Tabellen speichern


Die Liste **Tabellen** zeigt neben der Größe jeder Tabelle die Spalten **Aktuelle Daten**, **Verlauf**, **Time-Travel-Tage** und **Hinweis**. **Time-Travel-Tage** ist die eigene Einstellung der Tabelle; **1** bedeutet, dass sie den Standard des Projekts verwendet. Die Statusleiste unter der Liste gibt die Gesamtsumme des Projekts an: wie viel es speichert und wie viel davon aktuelle Daten und wie viel Verlauf ist. Mit **Geschätzt** markierte Größen stammen aus der Struktur der Tabelle, bis PlaidCloud sie misst.

Wählen Sie in der Symbolleiste **Speicher**, um das Fenster **Speicher** des Projekts zu öffnen, mit Vorschlägen zum Freigeben von Platz und den Time-Travel-Einstellungen. Siehe [Speicher verwalten](/de/guides/projects/managing-storage/#das-fenster-speicher-für-ein-projekt).


## Einen Dateneditor aus einer Tabelle erstellen


Sie können eine Tabelle in einem Schritt in einen konfigurierten Dateneditor umwandeln – wählen Sie die Tabelle und wählen Sie **Dateneditor aus Tabelle erstellen** im Menü **Neu** oder im Kontextmenü (Rechtsklick). PlaidCloud untersucht die Spalten der Tabelle und erstellt die Eingabesteuerelemente des Editors vorab. Details finden Sie unter [Einen Dateneditor aus einer Tabelle erstellen](/de/guides/projects/managing-data-editors/#einen-dateneditor-aus-einer-tabelle-erstellen).
