---
title: Dateneditoren verwalten
description: Verwalten Sie Dateneditor-Zuweisungen in PlaidCloud-Projekten, um zu steuern, wer Tabellendaten direkt über die Datenoberfläche ändern darf.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-data-editors.md
---

PlaidCloud ermöglicht es, Dateneditoren einschließlich ihrer Beschriftungen zu organisieren und zu verwalten. Mit Dateneditoren können Tabellendaten bearbeitet oder durch Benutzerinteraktion neue Daten erstellt werden.



PlaidCloud organisiert Dateneditoren über ein pfadbasiertes System, ähnlich wie Sie durch eine Reihe von Ordnern navigieren. Das ermöglicht eine flexiblere und logischere Organisation (Steuerungshierarchie) der Dateneditoren. In diesem System können Dateneditoren innerhalb einer Steuerungshierarchie verschoben werden. Auf einen Dateneditor können mehrere Verweise von verschiedenen Stellen der Steuerungshierarchie aus angelegt werden (alternative Hierarchien). Mit dieser Art der Verwaltung kann die Struktur den betrieblichen Anforderungen, dem Reporting und der Steuerung entsprechen.




## Dateneditor aus einer Tabelle erstellen


Sie können direkt aus einer vorhandenen Tabelle einen gebrauchsfertigen Dateneditor erstellen. PlaidCloud untersucht die Spalten der Tabelle und konfiguriert den Editor vor – es wählt für jede Spalte ein Eingabesteuerelement und wandelt Spalten, die eine kleine Menge wiederkehrender Werte enthalten, in Dropdown-Auswahllisten um.


So erstellen Sie einen Dateneditor aus einer Tabelle:


1. Öffnen Sie die Ansicht **Tabellen** des Projekts und wählen Sie eine einzelne Tabelle aus
2. Öffnen Sie **Dateneditor aus Tabelle erstellen** – im Menü **Neu** der Symbolleiste oder per Rechtsklick auf die Tabelle
3. PlaidCloud profiliert die Tabelle und öffnet das Fenster **Dateneditor-Konfiguration** mit allen vorausgefüllten Angaben: Es legt sowohl Quelle als auch Ziel auf die ausgewählte Tabelle fest, sodass Ihre Änderungen direkt dorthin zurückgespeichert werden, und weist jeder Spalte auf der Registerkarte **Formularspalten** ein Steuerelement zu, das zu ihrem Datentyp und ihren Werten passt
4. Prüfen Sie die Spalten und passen Sie die Steuerelemente bei Bedarf an
5. Klicken Sie auf **Speichern** oder **Speichern und schließen**

Erst durch das Speichern wird der Editor erstellt – ein Klick auf **Abbrechen** fügt nichts hinzu.

Wenn eine Spalte einer Dimension zugeordnet ist, wählen Sie vor dem Speichern auf der Registerkarte „Formularspalten“ eine Hierarchie dafür aus. PlaidCloud verhindert das Speichern, solange eine Dimensionsspalte keine Hierarchie hat.


## Wie PlaidCloud Spalten konfiguriert


Wenn Sie einen Editor aus einer Tabelle erstellen – oder **Aus Quelle füllen** verwenden –, richtet PlaidCloud jede Spalte automatisch ein:


- **Boolean**-Spalten werden zu einem Kontrollkästchen oder, wenn die Spalte leere Werte zulässt, zu einer Wahr/Falsch-Liste
- **Datum**-Spalten werden zu einer Datumsauswahl
- **Numerisch**e Spalten werden zu einem Zahlenfeld
- Spalten, die einer **Dimension** zugeordnet sind, werden zu einer Dimensionsauswahl, in der Sie die Hierarchie wählen – beim Bearbeiten einer Zelle öffnet sich dieselbe Elementauswahl-Baumstruktur, die unter [Eigenschaften vom Typ Dimension und die Elementauswahl](/de/guides/dimensions/dimensions/#eigenschaften-vom-typ-dimension-und-die-mitgliederauswahl) beschrieben ist, mit **Alle erweitern**, **Alle reduzieren**, **Übernehmen**, **Leeren** und **Abbrechen**
- Spalten, deren Werte sich über eine kleine Menge wiederholen – zum Beispiel ein Status- oder Regionscode –, werden zu einer **Dropdown-Liste**, die die in der Spalte gefundenen Werte auflistet
- Andere **Text**-Spalten werden zu einem Textfeld oder bei langen Werten zu einem Textbereich
- PlaidCloud nimmt schlüsselähnliche Spalten wie automatisch generierte IDs auf, markiert sie aber als schreibgeschützt

Bei sehr großen Tabellen schätzt PlaidCloud die Liste der Werte anhand einer Stichprobe von Zeilen. Sie können das Steuerelement jeder Spalte anschließend ändern.

Wenn Sie auf der Registerkarte **Formularspalten** eine Spalte auswählen, sehen Sie eine kurze Erklärung, warum PlaidCloud dieses Steuerelement gewählt hat.


## Grenzwert für Auswahllisten anpassen


PlaidCloud wandelt eine Spalte nur dann in eine Dropdown-Liste um, wenn sich ihre Werte über eine kleine Menge wiederholen. Sie können diesen Grenzwert ändern und die Spalten neu ableiten:


1. Legen Sie auf der Registerkarte **Formularspalten** unter **Max. Werte der Auswahlliste** die größte Anzahl unterschiedlicher Werte fest, die eine Spalte haben darf und trotzdem eine Dropdown-Liste wird
2. Klicken Sie auf **Neu profilieren**

PlaidCloud untersucht die Quelltabelle mit der neuen Einstellung erneut und erstellt die Spalten neu. Hat der Editor bereits Spalten, ersetzt das erneute Profilieren sie, daher bittet PlaidCloud Sie um Bestätigung.


## Vorhandenen Editor aus einer Tabelle füllen


Dieselbe automatische Konfiguration können Sie auf einen Editor anwenden, den Sie gerade bearbeiten:


1. Öffnen Sie die Konfiguration des Dateneditors und wechseln Sie zur Registerkarte **Quelle und Ziel**
2. Legen Sie die Quelle auf eine Tabelle fest
3. Klicken Sie auf der Registerkarte **Formularspalten** auf **Aus Quelle füllen**

PlaidCloud fügt für jede Spalte der Quelltabelle eine konfigurierte Spalte hinzu. Bereits angepasste Spalten bleiben erhalten, und PlaidCloud fordert Sie auf, Spalten zu entfernen, die nicht mehr in der Quelle vorhanden sind.


## Suchen


So suchen Sie nach Dateneditoren:


1. Verwenden Sie **Filter** am unteren Rand der Liste neben der Zeilenanzahl (drücken Sie **/** oder Strg/Cmd+F, um direkt dorthin zu springen)

Der Suchfilter durchsucht die Namen und Beschriftungen der Dateneditoren nach Treffern und zeigt die Ergebnisse in der Hierarchie an.




## Verschieben


So verschieben Sie einen Dateneditor innerhalb der Steuerungshierarchie:


1. Ziehen Sie ihn in den Ordner, in dem Sie ihn ablegen möchten

## Umbenennen


So benennen Sie einen Dateneditor um:


1. Klicken Sie mit der rechten Maustaste auf den Dateneditor
2. Wählen Sie die Option zum Umbenennen
3. Geben Sie den neuen Namen ein und speichern Sie ihn

Der Dateneditor wird nun umbenannt, behält aber seinen ursprünglichen eindeutigen Bezeichner.




## Löschen


Sie können einen einzelnen Dateneditor oder mehrere Dateneditoren löschen.


So löschen Sie einen Dateneditor:


1. Wählen Sie die Dateneditoren in der Steuerungshierarchie aus
2. Klicken Sie in der oberen Symbolleiste auf die Schaltfläche „Löschen“


## Neue Verzeichnisstruktur erstellen


So fügen Sie der Steuerungshierarchie einen neuen Ordner hinzu:


1. Klicken Sie in der Symbolleiste auf die Schaltfläche „Neuer Ordner“

So fügen Sie einem vorhandenen Ordner einen Ordner hinzu:


1. Klicken Sie mit der rechten Maustaste auf den Ordner
2. Wählen Sie „Neuer Ordner“

Wenn die Auswahl in einem Ordner liegt, enthält die Eingabeaufforderung für den Namen des neuen Ordners außerdem **Auf oberster Ebene erstellen**. Aktivieren Sie das Kontrollkästchen, um den neuen Ordner stattdessen auf der obersten Ebene des Projekts anzulegen.


## Hierarchie für Ansichtsrollen markieren


Die Anzeige von Dateneditoren für verschiedene Rollen:


1. Klicken Sie auf die Kontrollkästchen „Explorer“ oder „Manager“

So aktualisieren Sie mehrere Dateneditoren:


1. Wählen Sie die Dateneditoren in der Steuerungshierarchie aus
2. Wählen Sie im Menü „Aktionen“ der oberen Symbolleiste die gewünschte Ansichtsrolle aus


## Notizen zur Beschreibung des Tabelleninhalts


So fügen Sie einem Dateneditor eine Notiz hinzu:


1. Wählen Sie den Dateneditor aus
2. Aktualisieren Sie die Notiz im Kontextformular rechts


## Weitere Hierarchieattribute anzeigen


So zeigen und bearbeiten Sie weitere Attribute eines Dateneditors an:


1. Wählen Sie den Dateneditor aus und sehen Sie sich das Kontextformular des Dateneditors rechts an


## Dateneditor duplizieren


So duplizieren Sie einen Dateneditor:


1. Wählen Sie den Dateneditor aus
2. Klicken Sie in der oberen Symbolleiste auf die Schaltfläche „Duplizieren“


## Schreiben über den KI-Assistenten oder MCP

Über die Konfigurationsbildschirme hinaus kann `editor_upsert` Quelle, Ziel und Steuerelemente eines Dateneditors festlegen und direkt Zeilen in ihn schreiben – `data` ist eine Liste von Zeilenobjekten, die nach der ID des jeweiligen Steuerelements benannt sind. Ein ungültiges Datum wird abgelehnt, bevor die Zieltabelle berührt wird, sodass ein fehlerhafter Schreibvorgang nie teilweise ankommt.
