---
title: Tabellen und Ansichten verwalten
description: Verwalten Sie Tabellen und Ansichten in PlaidCloud-Projekten, einschließlich Erstellung, Konfiguration, Berechtigungen und Organisation von Datenobjekten.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

PlaidCloud ermöglicht es, Tabellen einschließlich ihrer Beschriftungen zu organisieren und zu verwalten. Tabellen stehen allen Workflows innerhalb eines Projekts zur Verfügung und bieten viele Werkzeuge und Optionen.


Zusätzlich zu Tabellen bietet PlaidCloud auch Ansichten auf Basis von Tabellendaten. Ansichten werden sofort aktualisiert, wenn sich die zugrunde liegenden Tabellen ändern, und sparen Speicherplatz.



Zu den Optionen gehören:


* Dieselbe Tabelle kann auf mehreren Pfaden in der Hierarchie existieren (alternative Hierarchien)
* Tabellen können mit Tags versehen werden, um die Suche und die Einbindung in PlaidCloud-Prozesse zu erleichtern
* Tabellen können versioniert werden
* Tabellen können veröffentlicht werden, damit sie für Dashboard-Visualisierungen verfügbar sind

PlaidCloud organisiert Tabellen über ein pfadbasiertes System, ähnlich wie Sie durch eine Reihe von Ordnern navigieren. Das ermöglicht eine flexiblere und logischere Organisation von Tabellen. In diesem System können Tabellen innerhalb einer Hierarchie verschoben werden, oder es können mehrere Verweise auf eine Tabelle von verschiedenen Stellen der Hierarchie aus angelegt werden (alternative Hierarchien). Mit dieser Art der Verwaltung kann die Struktur den betrieblichen Anforderungen, dem Reporting und der Steuerung entsprechen.



## Tabellen finden


Verwenden Sie **Filter** am unteren Rand der Liste neben der Zeilenanzahl, um Tabellennamen und Beschriftungen zu durchsuchen. Drücken Sie **/** oder Strg/Cmd+F, um direkt dorthin zu springen. Derselbe Filter gilt für die Baumstruktur und für die flache Liste. Der Schalter **Alle | Published** neben dem Filter beschränkt die Liste auf veröffentlichte Tabellen; er steht standardmäßig auf **Alle** und gilt sowohl in der Baumstruktur als auch in der flachen Liste.


### Nach Workflow

Der Ordner **Nach Workflow** am Ende der Registerkarte **Tabellen** gruppiert Tabellen unter jedem Workflow, der sie liest oder schreibt. Öffnen Sie einen Workflow, um seine Tabellen zu sehen. Der Ordner ist eine Ansicht derselben Tabellen, daher können Sie daraus nichts verschieben oder kopieren.


### Nach Spalte

Geben Sie auf der Registerkarte **Tabellen** einen Spaltennamen in das Suchfeld für Spalten ein und drücken Sie die Eingabetaste oder wählen Sie die Lupe daneben, um nur die Tabellen anzuzeigen, die eine Spalte mit diesem Namen haben. Die Suche liest Spaltennamen, nicht die Daten, und ist daher schnell. Wählen Sie **Enthält**, um einen Teil eines Spaltennamens statt des ganzen Namens abzugleichen. Leeren Sie das Feld, um wieder alle Tabellen anzuzeigen. Eine lange Suche kann seitenweise Ergebnisse liefern, und die Statuszeile zeigt an, wenn die Suche noch läuft oder unvollständig sein könnte.

Wählen Sie **Spaltenbaum**, um in einem eigenen Fenster zu suchen. Jede Tabelle mit der Spalte öffnet sich zu zwei Listen:

* **Gespeist von** – die Tabellen, die die Spalte liefern
* **Speist** – die Tabellen, die die Spalte anschließend speist

Ein über MCP verbundener KI-Assistent findet dieselben Tabellen mit `table_find(column=...)`, wobei der gesamte Name oder ein Teil davon abgeglichen wird.


### Werte suchen

Um herauszufinden, welche Tabellen einen Wert enthalten, wählen Sie im Menü **Aktionen** auf der Registerkarte **Tabellen** die Option **Werte in Daten suchen… (langsam)** oder klicken Sie mit der rechten Maustaste auf eine Tabelle und wählen Sie sie dort, um nur in dieser Tabelle zu suchen. Geben Sie den Wert ein, wählen Sie **Enthält**, um einen Teil eines Werts abzugleichen, und wählen Sie **Suchen**. Jede Tabelle, die den Wert enthält, wird mit den Spalten, in denen er vorkommt, und einigen der passenden Werte aufgelistet. Doppelklicken Sie auf eine Tabelle oder drücken Sie die Eingabetaste, um sie im Tabellen-Explorer zu öffnen. Eine Spalte öffnet die Tabelle gefiltert nach den passenden Zeilen. Enthält das Suchfeld für Spalten Text, wird damit der zu suchende Wert vorausgefüllt.

Beachten Sie vor der Suche Folgendes:

* Die Suche liest jede Zeile jeder durchsuchten Tabelle, kann daher sehr langsam sein und viele Warehouse-Ressourcen beanspruchen. Das Fenster warnt Sie, und die Suchschaltflächen bleiben deaktiviert, bis eine Suche abgeschlossen ist.
* Sie sehen nur Zeilen, die Sie ohnehin öffnen könnten. Die Sicherheit auf Zeilenebene gilt für jede Suche.
* Der Abfrageverlauf Ihres Warehouse zeichnet die Werte auf, nach denen Sie suchen.
* Die Suche umfasst die Textspalten von Tabellen. Tabellen, die noch nicht erstellt wurden, werden übersprungen und in einer Warnung genannt.
* Die Ergebnisse kommen seitenweise. Wenn die Statuszeile meldet, dass die Suche vorzeitig beendet wurde, wählen Sie **Weiter suchen**, um mit den noch nicht durchsuchten Tabellen fortzufahren.

Ein über MCP verbundener KI-Assistent verwendet `table_value_search`. Es gibt die Tabellen und Spalten zurück, die den Wert enthalten, nie die Werte selbst. Wenn Sie den KI-Assistenten in einem Projekt bitten, einen Wert zu finden, sendet Weave die Namen der passenden Tabellen und Spalten an den Anbieter des Sprachmodells.



## CSV-Datei importieren

**So wandeln Sie eine CSV-Datei in eine neue Tabelle in diesem Projekt um:**

1. Ziehen Sie die Datei von Ihrem Computer auf die Liste **Tabellen** des Projekts oder wählen Sie in der Symbolleiste **Neu** > **Tabelle aus CSV-Datei**, legen Sie die Datei auf dem Feld ab oder klicken Sie auf **CSV-Datei auswählen**.
2. PlaidCloud lädt die Datei in Ihr **Personal Temp Drive** hoch – oder in das **Temp Drive** des Workspace, falls Sie keines haben – und importiert sie in eine neue Tabelle auf oberster Ebene der Liste, benannt nach der Datei: `Sales Data.csv` wird zu `sales_data`. Hat das Projekt bereits eine Tabelle mit diesem Namen, erhält die neue eine Nummer, etwa `sales_data_2`.
3. Die Liste wird mit der neuen ausgewählten Tabelle aktualisiert, und **Ihre Daten auf einen Blick** öffnet sich dafür. Was das Fenster zeigt, lesen Sie unter [Mit Ihrer eigenen CSV beginnen](/de/get-started/quickstart/#mit-der-eigenen-csv-datei-beginnen).

Es werden nur Dateien mit der Endung `.csv` akzeptiert. Sie benötigen die Berechtigung zum Erstellen von Tabellen und zum Schreiben in den Dokumentenspeicher, und ein gesperrtes Projekt nimmt keine CSV an, bis es entsperrt ist. Schlägt der Import fehl, nennt das Fenster den Grund, und Ihr Projekt bleibt unverändert. PlaidCloud löscht die hochgeladene Datei aus dem Temp-Laufwerk, sobald der Import abgeschlossen ist, unabhängig davon, ob er erfolgreich war; andernfalls löscht das Temp-Laufwerk sie nach einem Tag.

## Verschieben


**So verschieben Sie eine Tabelle:**


1. Ziehen Sie sie in den Ordner, in dem sie liegen soll

## Umbenennen


**So benennen Sie eine Tabelle um:**


1. Klicken Sie mit der rechten Maustaste auf die Tabelle
2. Wählen Sie die Option zum Umbenennen
3. Geben Sie den neuen Namen ein und speichern Sie ihn
4. Die Tabelle ist nun umbenannt, behält aber ihren ursprünglichen eindeutigen Bezeichner.

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

*Hinweis: Sie können die Tabellen auch erzwungen löschen. Beim erzwungenen Löschen bleiben Verweise defekt zurück, daher sollten Sie diese Option sparsam einsetzen.*


### Zuletzt gelesen

Das Löschfenster zeigt, wann die Tabelle zuletzt gelesen wurde, zum Beispiel **Last read 3 days ago by** eine Person oder ein Schritt, sodass Sie eine Tabelle, die niemand verwendet, von einer unterscheiden können, die noch in Gebrauch ist. PlaidCloud entnimmt dies dem eigenen Abfrageverlauf Ihres Warehouse und lässt Lesezugriffe seiner eigenen Wartungsvorgänge außen vor.

| Warehouse | Was erforderlich ist |
| --- | --- |
| Snowflake | Lesezugriffe stammen aus dem Access History, das Snowflake mit einer Verzögerung von bis zu etwa 3 Stunden aufzeichnet. Die Rolle der Verbindung benötigt die Datenbankrolle `SNOWFLAKE.GOVERNANCE_VIEWER` (`IMPORTED PRIVILEGES` auf der Datenbank `SNOWFLAKE` funktioniert ebenfalls). Die Snowflake-Edition Standard hat keinen Access History. |
| Databricks | Lesezugriffe stammen aus der Lineage-Tabelle, die Databricks ebenfalls mit Verzögerung aufzeichnet, sodass ein kürzlicher Lesezugriff möglicherweise noch nicht angezeigt wird. Die Identität der Verbindung benötigt `USE CATALOG` auf `system`, `USE SCHEMA` auf `system.access` und `SELECT` auf `system.access.table_lineage`. |
| PlaidCloud Lakehouse | Der Leseverlauf ist noch nicht verfügbar. Das Fenster zeigt **Read history incomplete**. |

Wenn Sie Ihr Warehouse verbinden, empfiehlt [die Verbindungsprüfung](/de/guides/connections/external-lakehouse/#3-prüfen-und-dann-verwenden) jede dieser Berechtigungen, die fehlt, jeweils mit der auszuführenden Anweisung. Sie sind empfohlen, nicht erforderlich: Ohne sie verbindet sich das Warehouse, und das Fenster zeigt **Read history incomplete**.

Kann PlaidCloud den gesamten Verlauf nicht lesen, lautet die Zeile **Read history incomplete** und meldet nie stattdessen „no reads“. Jeder mit direktem SQL-Zugriff auf Ihr Warehouse kann ein Sitzungs-Tag setzen, das ändert, wie seine eigenen Lesezugriffe gekennzeichnet werden.

Ein über MCP verbundener KI-Assistent erhält dieselbe Antwort von `table_describe(include=['last_read'])`.



## Spalten einer Tabelle anzeigen


Wenn Sie eine Tabelle auswählen, öffnet sich ihr Detailbereich. Der Abschnitt **Spalten** listet jede Spalte mit ihrem **Typ** und ihrer **Beschreibung** auf, wobei die Beschreibung aus den **Spalteneigenschaften** stammt. Zeigen Sie auf eine Zeile, um eine lange Beschreibung vollständig zu lesen.

Eine Tabelle, die gerade nicht im Warehouse vorhanden ist, weil ihre Daten abgelaufen sind oder kein Schritt sie erstellt hat, hat keine Spalten, die aufgelistet werden könnten. Der Abschnitt weist darauf hin und zeigt, wie viele Spalten die Tabelle hat. Führen Sie einen Schritt aus, der die Tabelle schreibt, um sie aufzulisten.


## Anzeigen, wo eine Tabelle verwendet wird


Wenn Sie eine Tabelle auswählen, öffnet sich ihr Detailbereich, der die Workflow-Schritte auflistet, die sie berühren:


* **Tabelle erstellt von** – Schritte, die in die Tabelle schreiben
* **Tabelle liefert Daten an** – Schritte, die aus ihr lesen
* **Kann auf diese Tabelle verweisen** – Schritte, die eine Tabelle über eine Variable erreichen, die sich nicht auflösen lässt. Dieser Abschnitt erscheint nur, wenn es solche Schritte gibt.


Die Auswahl einer anderen Tabelle leert diese Listen sofort. Ein Schritt in einem anderen Projekt, das die Daten dieses Projekts gemeinsam nutzt, etwa ein Schritt **Import: Externe Projekttabelle**, der diese Tabelle liest, wird ebenfalls aufgelistet, jedoch ohne seinen Namen oder Workflow, da Sie möglicherweise keinen Zugriff auf dieses Projekt haben. Diese Schritte können einen Moment später als die übrigen erscheinen.


Ein Schritt kann eine Tabelle direkt benennen oder sie über einen Pfad mit einer Variablen erreichen, etwa `/Periods/{period}/Sales`. Hat diese Variable einen aktuellen Wert, erscheint der Schritt in den ersten beiden Listen mit einem Informationssymbol daneben. Zeigen Sie auf die Zeile, um den Pfad so zu sehen, wie ihn der Schritt speichert.


Betrachten Sie diese Zeilen als die schwächere Antwort, die sie sind. Sie beschreiben, was eine jetzt gestartete Ausführung berühren würde – nicht alles, was die Tabelle je berührt hat. Ändern Sie die Variable, und eine andere Tabelle wird gelesen.


Manche Variablen lassen sich nicht auflösen. Entweder hat nichts die Variable gesetzt, oder der Wert, den eine Ausführung verwendet, stammt nicht aus dem Gespeicherten – ein Workflow Loop bezieht seine Variablen bei der Iteration aus Daten, ein Schritt Set Variable weist sie während der Ausführung zu, ein Makro erhält seine Variablen von dem Schritt, der es aufruft, und eine von einem Sensor gestartete Ausführung trägt die eigenen Details dieses Sensors. In jedem dieser Fälle ist das, was zwischen den Ausführungen gespeichert bleibt, ein Rest der letzten Ausführung und kein vertrauenswürdiger Wert. Statt diese zu einer möglicherweise falschen Tabelle aufzulösen, listet PlaidCloud die Schritte namentlich unter **Kann auf diese Tabelle verweisen** auf, zusammen mit der Variablen, die es nicht auflösen konnte, damit Sie sie öffnen und prüfen können.


Ein Schritt, den Ihre Rolle nicht sehen kann, wird dennoch aufgelistet, damit Sie wissen, dass die Tabelle verwendet wird, jedoch ohne seinen Namen oder Workflow, und Sie können ihn nicht öffnen. Er zählt trotzdem mit, wenn Sie die Tabelle löschen. Ein Schritt, den Sie sehen können, wird ohne einen Workflow aufgelistet, den Ihre Rolle ausblendet. Einem Architect wird nichts verborgen.


*Hinweis: Wenn Sie Tabellen aus der Liste **Tabellen** löschen, zählt ein Schritt, der eine Tabelle über einen Pfad erreicht – mit oder ohne Variable –, als Verwendung, auch wenn sich seine Variable nicht auflösen lässt. Das Löschfenster listet den Schritt auf, und das Löschen wird nur fortgesetzt, wenn Sie es erzwingen.*



## Neue Verzeichnisstruktur erstellen


**So fügen Sie einen neuen Ordner hinzu:**


1. Klicken Sie in der Symbolleiste auf die Schaltfläche „Neuer Ordner“

**So fügen Sie einem vorhandenen Ordner einen Ordner hinzu:**


1. Klicken Sie mit der rechten Maustaste auf den Ordner
2. Wählen Sie „Neuer Ordner“


## Daten anzeigen (Tabellen-Explorer)


Tabellendaten werden mit dem Data Explorer angezeigt. Der Data Explorer bietet eine Rasteransicht der Daten sowie eine spaltenweise Zusammenfassung von Werten und Statistiken. Filtern per Mausklick und der Export in gängige Dateiformate sind beide möglich. Die Filterauswahl kann außerdem als Schritt Extract gespeichert werden, der in einem Workflow verwendbar ist.



## Tabelle für Berichte veröffentlichen


Dashboard-Visualisierungen sind bewusst auf Tabellen beschränkt, die veröffentlicht wurden. Beim Veröffentlichen einer Tabelle können Sie einen eindeutigen Namen vergeben, der die Daten besser kennzeichnet. Das kann nützlich sein, wenn die Tabelle im Workflow, der sie erzeugt hat, einen unscheinbareren Namen trägt, aber für diejenigen, die Dashboards erstellen, einen klareren Namen benötigt.


Veröffentlichte Tabellen haben keine zugeordneten Pfade. Sie erscheinen als Liste von Tabellen zur Verwendung im Dashboard-Bereich.



## Tabelle für Ansichtsrollen markieren


Die Anzeige von Tabellen für verschiedene Rollen lässt sich über die Kontrollkästchen „Explorer“ oder „Manager“ steuern. Müssen mehrere Tabellen aktualisiert werden, wählen Sie die Tabellen in der Hierarchie aus und wählen Sie im Menü „Aktionen“ der oberen Symbolleiste die gewünschte Ansichtsrolle aus.



## Notizen zur Beschreibung des Tabelleninhalts


Fügen Sie einer Tabelle eine Notiz hinzu, um die Daten besser zu verstehen.



## Form, Größe und Zeitpunkt der letzten Aktualisierung einer Tabelle anzeigen


Die Anzahl der Zeilen und Spalten sowie die Datengröße jeder Tabelle werden in der Tabellenhierarchie angezeigt. Bei sehr großen Tabellen (mehrere Millionen Zeilen) kann die Zeilenanzahl geschätzt sein, und ein Hinweis auf die ungefähre Zeilenanzahl wird angezeigt.



## Weitere Tabellenattribute anzeigen


**So zeigen und bearbeiten Sie weitere Tabellenattribute:**


1. Wählen Sie eine Tabelle aus
2. Klicken Sie, um das Kontextformular der Tabelle rechts anzuzeigen.


## Tabelle duplizieren


**So duplizieren Sie eine Tabelle:**


1. Wählen Sie die Tabelle aus
2. Klicken Sie in der oberen Symbolleiste auf die Schaltfläche „Duplizieren“.


## Panel-App aus einer Tabelle erstellen


Wählen Sie eine Tabelle oder Ansicht aus und wählen Sie im Menü **Neu** oder im Kontextmenü **Panel-App erstellen**. Das Dialogfeld **Neue Studio-App** öffnet sich mit dem bereits gewählten Projekt und der Tabelle. Die App übernimmt den Namen der Tabelle; ändern Sie ihn nach Wunsch und wählen Sie dann **Erstellen**, und Panel Studio öffnet sie mit Weave, bereit zum Erstellen der ersten Seite. Der Befehl ist verfügbar, wenn Sie eine einzelne Tabelle oder Ansicht auswählen, Bearbeitungszugriff auf das Projekt haben und das Projekt nicht schreibgeschützt ist. Siehe [Panel-App erstellen](/de/guides/panel-apps/creating/#mit-einer-tabelle-beginnen).


## Anzeigen, was Tabellen speichern


Die Liste **Tabellen** zeigt neben der Größe jeder Tabelle die Spalten **Aktuelle Daten**, **Verlauf**, **Time-Travel-Tage** und **Hinweis**. **Time-Travel-Tage** ist die eigene Einstellung der Tabelle; **1** bedeutet, dass sie den Standard des Projekts verwendet. Die Statusleiste unter der Liste zeigt die Summe des Projekts: wie viel es speichert und wie viel davon aktuelle Daten und wie viel Verlauf ist. Mit **Geschätzt** markierte Größen stammen aus der Form der Tabelle, bis PlaidCloud sie misst.

Wählen Sie in der Symbolleiste **Speicher**, um das Fenster **Speicher** des Projekts zu öffnen, mit Vorschlägen zur Speicherfreigabe und den Time-Travel-Einstellungen. Siehe [Speicher verwalten](/de/guides/projects/managing-storage/#das-fenster-speicher-für-ein-projekt).


## Dateneditor aus einer Tabelle erstellen


Sie können eine Tabelle in einem Schritt in einen konfigurierten Dateneditor umwandeln – wählen Sie die Tabelle aus und wählen Sie im Menü **Neu** oder im Kontextmenü **Dateneditor aus Tabelle erstellen**. PlaidCloud untersucht die Spalten der Tabelle und erstellt die Eingabesteuerelemente des Editors vor. Einzelheiten finden Sie unter [Dateneditor aus einer Tabelle erstellen](/de/guides/projects/managing-data-editors/#dateneditor-aus-einer-tabelle-erstellen).
