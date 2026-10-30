---
title: Dateneditoren verwalten
description: Verwalten Sie Dateneditor-Zuweisungen in PlaidCloud-Projekten, um zu steuern, wer Tabellendaten direkt über die Datenschnittstelle ändern darf.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-data-editors.md
---

PlaidCloud ermöglicht es, Dateneditoren einschließlich Labels zu organisieren und zu verwalten. Mit Dateneditoren lassen sich Tabellendaten bearbeiten oder durch Benutzerinteraktion Daten erzeugen.



PlaidCloud organisiert Dateneditoren über ein pfadbasiertes System, wie Sie es von der Navigation durch eine Reihe von Ordnern kennen, was eine flexiblere und logischere Organisation (Steuerungshierarchie) der Dateneditoren erlaubt. Mit diesem System lassen sich Dateneditoren innerhalb einer Steuerungshierarchie verschieben. Es lassen sich mehrere Verweise auf einen Dateneditor von verschiedenen Stellen der Steuerungshierarchie aus (alternative Hierarchien) anlegen. Die Verwaltung von Dateneditoren auf diese Weise ermöglicht es, dass die Struktur den betrieblichen Anforderungen, dem Reporting und der Kontrolle entspricht.




## Einen Dateneditor aus einer Tabelle erstellen


Sie können direkt aus einer vorhandenen Tabelle einen sofort einsatzbereiten Dateneditor erstellen. PlaidCloud untersucht die Spalten der Tabelle und konfiguriert den Editor vor – es wählt für jede Spalte ein Eingabesteuerelement und macht Spalten, die eine kleine Menge sich wiederholender Werte enthalten, zu Dropdown-Auswahllisten.


So erstellen Sie einen Dateneditor aus einer Tabelle:


1. Öffnen Sie die Ansicht **Tabellen** des Projekts und wählen Sie eine einzelne Tabelle aus.
2. Öffnen Sie **Dateneditor aus Tabelle erstellen** – über das Menü **Neu** in der Symbolleiste oder per Rechtsklick auf die Tabelle.
3. PlaidCloud profiliert die Tabelle und öffnet das Fenster **Dateneditor-Konfiguration** mit allem vorausgefüllt: Es setzt Quelle und Ziel auf die ausgewählte Tabelle, sodass Ihre Änderungen direkt dorthin zurückgespeichert werden, und weist jeder Spalte auf der Registerkarte **Formularspalten** ein Steuerelement zu, das zu ihrem Datentyp und ihren Werten passt.
4. Prüfen Sie die Spalten und passen Sie die Steuerelemente bei Bedarf an.
5. Klicken Sie auf **Speichern** oder **Speichern und schließen**.

Erst das Speichern erstellt den Editor – ein Klick auf **Abbrechen** fügt nichts hinzu.

Wenn eine Spalte einer Dimension zugeordnet ist, wählen Sie vor dem Speichern auf der Registerkarte „Formularspalten“ eine Hierarchie dafür aus. PlaidCloud verhindert das Speichern, solange eine Dimensionsspalte keine Hierarchie hat.


## Wie PlaidCloud Spalten konfiguriert


Wenn Sie einen Editor aus einer Tabelle erstellen – oder **Aus Quelle füllen** verwenden –, richtet PlaidCloud jede Spalte automatisch ein:


- Spalten vom Typ **Boolean** werden zu einem Kontrollkästchen oder, wenn die Spalte leere Werte zulässt, zu einer Wahr/Falsch-Liste.
- Spalten vom Typ **Datum** werden zu einer Datumsauswahl.
- Spalten vom Typ **Numerisch** werden zu einem Zahlenfeld.
- Spalten, die einer **Dimension** zugeordnet sind, werden zu einer Dimensionsauswahl, in der Sie die Hierarchie wählen – das Bearbeiten einer Zelle öffnet dieselbe Mitgliederauswahl-Baumstruktur, die unter [Eigenschaften vom Typ Dimension und die Mitgliederauswahl](/de/guides/dimensions/dimensions/#eigenschaften-vom-typ-dimension-und-die-mitgliederauswahl) beschrieben ist, mit **Alle erweitern**, **Alle reduzieren**, **Übernehmen**, **Leeren** und **Abbrechen**.
- Spalten, deren Werte sich über eine kleine Menge wiederholen – zum Beispiel ein Status- oder Regionscode –, werden zu einem **Dropdown**, das die in der Spalte gefundenen Werte auflistet.
- Andere Spalten vom Typ **Text** werden zu einem Textfeld oder bei langen Werten zu einem Textbereich.
- PlaidCloud nimmt schlüsselähnliche Spalten wie automatisch generierte IDs auf, markiert sie aber als schreibgeschützt.

Bei sehr großen Tabellen schätzt PlaidCloud die Werteliste anhand einer Stichprobe von Zeilen. Sie können das Steuerelement jeder Spalte anschließend ändern.

Wählen Sie auf der Registerkarte **Formularspalten** eine Spalte aus, um eine kurze Erklärung zu sehen, warum PlaidCloud ihr Steuerelement gewählt hat.


## Die Grenze für Auswahllisten anpassen


PlaidCloud macht eine Spalte nur dann zu einem Dropdown, wenn sich ihre Werte über eine kleine Menge wiederholen. Sie können diese Grenze ändern und die Spalten neu ableiten:


1. Legen Sie auf der Registerkarte **Formularspalten** unter **Max. Werte der Auswahlliste** die größte Anzahl unterschiedlicher Werte fest, die eine Spalte haben darf und trotzdem ein Dropdown wird.
2. Klicken Sie auf **Neu profilieren**.

PlaidCloud untersucht die Quelltabelle mit der neuen Einstellung erneut und baut die Spalten neu auf. Hat der Editor bereits Spalten, ersetzt das erneute Profilieren sie, daher bittet PlaidCloud Sie um Bestätigung.


## Einen vorhandenen Editor aus einer Tabelle füllen


Sie können dieselbe automatische Konfiguration auf einen Editor anwenden, den Sie gerade bearbeiten:


1. Öffnen Sie die Konfiguration des Dateneditors und wechseln Sie zur Registerkarte **Quelle und Ziel**.
2. Legen Sie die Quelle auf eine Tabelle fest.
3. Klicken Sie auf der Registerkarte **Formularspalten** auf **Aus Quelle füllen**.

PlaidCloud fügt für jede Spalte der Quelltabelle eine konfigurierte Spalte hinzu. Spalten, die Sie bereits angepasst haben, bleiben erhalten, und Sie werden aufgefordert, Spalten zu entfernen, die nicht mehr in der Quelle vorhanden sind.


## Suchen


So suchen Sie nach Dateneditoren:


1. Verwenden Sie das Filterfeld unten links in der Steuerungshierarchie.

Der Suchfilter durchsucht die Namen und Labels der Dateneditoren nach Treffern und zeigt die Ergebnisse oben in der Steuerungshierarchie an.




## Verschieben


So verschieben Sie einen Dateneditor innerhalb der Steuerungshierarchie:


1. Ziehen Sie ihn in den Ordner, in dem Sie ihn ablegen möchten.

## Umbenennen


So benennen Sie einen Dateneditor um:


1. Klicken Sie mit der rechten Maustaste auf den Dateneditor.
2. Wählen Sie die Option zum Umbenennen.
3. Geben Sie den neuen Namen ein und speichern Sie ihn.

Der Dateneditor ist nun umbenannt, behält aber seine ursprüngliche eindeutige Kennung.




## Löschen


Sie können einen einzelnen Dateneditor oder mehrere Dateneditoren löschen.


So löschen Sie einen Dateneditor:


1. Wählen Sie die Dateneditoren in der Steuerungshierarchie aus.
2. Klicken Sie in der oberen Symbolleiste auf die Schaltfläche „Löschen“.


## Neue Verzeichnisstruktur erstellen


So fügen Sie der Steuerungshierarchie einen neuen Ordner hinzu:


1. Klicken Sie in der Symbolleiste auf die Schaltfläche „Neuer Ordner“.

So fügen Sie einem vorhandenen Ordner einen Ordner hinzu:


1. Klicken Sie mit der rechten Maustaste auf den Ordner.
2. Wählen Sie „Neuer Ordner“.


## Hierarchie für Ansichtsrollen markieren


Die Anzeige von Dateneditoren für verschiedene Rollen:


1. Klicken Sie auf die Kontrollkästchen „Explorer“ oder „Manager“.

So aktualisieren Sie mehrere Dateneditoren:


1. Wählen Sie die Dateneditoren in der Steuerungshierarchie aus.
2. Wählen Sie im Menü „Aktionen“ der oberen Symbolleiste die gewünschte Ansichtsrolle.


## Memos zur Beschreibung des Tabelleninhalts


So fügen Sie einem Dateneditor ein Memo hinzu:


1. Wählen Sie den Dateneditor aus.
2. Aktualisieren Sie das Memo im Kontextformular rechts.


## Weitere Hierarchieattribute anzeigen


So zeigen und bearbeiten Sie weitere Attribute eines Dateneditors:


1. Wählen Sie den Dateneditor aus und sehen Sie sich das Kontextformular des Dateneditors rechts an.


## Einen Dateneditor duplizieren


So duplizieren Sie einen Dateneditor:


1. Wählen Sie den Dateneditor aus.
2. Klicken Sie in der oberen Symbolleiste auf die Schaltfläche „Duplizieren“.


## Schreiben über den KI-Assistenten oder MCP

Über die Konfigurationsbildschirme hinaus kann `editor_upsert` Quelle, Ziel und Steuerelemente eines Dateneditors festlegen und direkt Zeilen in ihn schreiben – `data` ist eine Liste von Zeilenobjekten, die nach der ID des jeweiligen Steuerelements benannt sind. Ein ungültiges Datum wird abgelehnt, bevor etwas die Zieltabelle berührt, sodass ein fehlerhafter Schreibvorgang nie teilweise ankommt.
