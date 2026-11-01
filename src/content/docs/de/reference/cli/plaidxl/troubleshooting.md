---
title: PlaidXL – Fehlerbehebung
description: Lösungen für häufige PlaidXL-Probleme – das Add-in fehlt im Menüband, ein Anmelde-Pop-up öffnet sich nicht, Workspaces oder Projekte fehlen, Tabellen werden rot angezeigt, Abrufe sind langsam und PlaidXL-Formeln liefern Fehler.
sidebar:
  label: Fehlerbehebung
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## Die Registerkarte PlaidCloud fehlt im Menüband

- Schließen Sie alle Excel-Fenster und öffnen Sie Excel erneut. Ein neu installiertes Add-in erscheint oft erst nach einem Neustart.
- Öffnen Sie **Insert → My Add-ins** und wählen Sie **PlaidCloud** aus.
- Prüfen Sie, ob Sie Desktop-Excel für Microsoft 365 oder Excel 2021 oder höher verwenden. Siehe [PlaidXL installieren](/de/reference/cli/plaidxl/install/).
- Wenn Ihre Organisation Add-ins verwaltet, fragen Sie Ihren Microsoft-365-Administrator, ob das Add-in **PlaidCloud** für Sie bereitgestellt ist.

## Das Anmelde-Pop-up öffnet sich nicht

Wenn Sie auf **Sign In** klicken, fragt Excel, ob ein Pop-up-Fenster angezeigt werden soll. Lassen Sie es zu. Wenn Sie die Aufforderung verworfen haben, klicken Sie erneut auf **Sign In**.

Wenn sich das Pop-up öffnet, Sie die Anmeldung aber nicht abschließen können, versuchen Sie, sich mit derselben E-Mail-Adresse in Ihrem Browser bei PlaidCloud anzumelden. Ein Problem dort – ein abgelaufenes Passwort oder ein Zwei-Faktor-Gerät, das Sie nicht mehr haben – muss zuerst in PlaidCloud behoben werden. Siehe [Mitgliederauthentifizierung](/de/administration/access/member-authentication/).

## Ein Workspace ist nicht aufgeführt

**Select a workspace** listet die Workspaces auf, zu denen Ihre E-Mail-Adresse gehört. Wenn einer fehlt, prüfen Sie, ob Sie dieselbe E-Mail-Adresse eingegeben haben, die Sie für diesen Workspace verwenden, und bitten Sie dann einen Workspace-Administrator zu bestätigen, dass Sie Mitglied sind. Siehe [Workspace-Mitglieder verwalten](/de/administration/access/overview/managing-workspace-members/).

Um zu einem anderen Workspace zu wechseln, dem Sie angehören, öffnen Sie das Kontomenü und wählen Sie **Switch workspace**.

## Ein Projekt, eine Tabelle oder eine Dimension fehlt

PlaidXL zeigt, was Ihr Konto in PlaidCloud sehen kann. Wenn ein Projekt fehlt, bitten Sie dessen Inhaber, Ihnen Zugriff zu geben. Wenn eine Tabelle fehlt, prüfen Sie, ob sie im ausgewählten Projekt existiert und mit Daten geladen wurde – bei einer Tabelle, in die noch nie geschrieben wurde, wird beim Auswählen **Unable to get table metadata** angezeigt.

Ordner in den Listen der Projekte, Tabellen und Dimensionen sind zunächst eingeklappt. Geben Sie einen Teil des Namens in das Filterfeld oben in der Liste ein, um ein Element in einem Ordner zu finden.

## Eine Tabelle wird rot angezeigt

Die Tabelle hat mehr Zeilen oder Spalten, als ein Excel-Arbeitsblatt fasst. Wählen Sie **Erweitert**, um die Zeilen zu filtern, und deaktivieren Sie die Spalten, die Sie nicht benötigen, bis sie passt. Siehe [Rot angezeigte Tabellen](/de/reference/cli/plaidxl/retrieve/#rot-angezeigte-tabellen).

## Ein Abruf ist langsam

Excel ist bei breiten Tabellen am langsamsten. Deaktivieren Sie die Kontrollkästchen der Spalten, die Sie nicht benötigen, und filtern Sie die Zeilen mit **Erweitert**. Nur die Daten abzurufen, mit denen Sie arbeiten, ist schneller und ergibt eine kleinere Arbeitsmappe.

## Eine Formel zeigt einen Fehler

| Was Sie sehen | Was zu prüfen ist |
|---|---|
| `#SPILL!` | In den Zellen, die das Ergebnis benötigt, steht etwas. Leeren Sie die Zellen unterhalb oder neben der Formel. |
| `#NAME?` | Excel erkennt die Funktion nicht. Prüfen Sie, ob PlaidXL installiert ist – die Registerkarte **PlaidCloud** ist im Menüband – und prüfen Sie die Schreibweise anhand der [Funktionsliste](/de/reference/cli/plaidxl/functions/). |
| Ein Fehler aus einer `PLAIDXL`-Funktion | Prüfen Sie, ob Sie angemeldet sind und das richtige Projekt ausgewählt ist, und prüfen Sie dann jeden Tabellen-, Spalten-, Dimensions- und Knotennamen anhand von PlaidCloud – die Namen müssen exakt übereinstimmen. |
| `CELL` meldet, dass eine Filterspalte nicht gefunden wurde | Das erste Argument von `DIMENSION_REPR` ist eine Spalte der Tabelle, keine Dimension. Verwenden Sie den Spaltennamen der Tabelle exakt. Siehe [Werte](/de/reference/cli/plaidxl/functions/#werte). |
| `#VALUE!` von `CELL` oder `CELLS` | Zeigen Sie mit der Maus auf die Zelle, um den von PlaidCloud genannten Grund zu lesen, etwa eine unbekannte Spalte, einen Knoten, der nicht existiert oder keine Mitglieder hat, oder ein Problem bei der Berechnung des Werts. Prüfen Sie die Namen anhand von PlaidCloud. |
| `CELL` liefert eine unerwartete Summe | Ein Knoten wird nur in einer mit seiner Dimension verknüpften Spalte aggregiert; in jeder anderen Spalte muss er exakt mit einem Wert übereinstimmen. Prüfen Sie Spalte und Knoten jedes Filters. |
| Werte ändern sich nach einer Änderung der Daten oder des Projekts nicht | Erzwingen Sie eine vollständige Neuberechnung – unter Windows **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` liefert einen Fehler | Verwenden Sie eines von `sum`, `mean`, `median`, `min`, `max`, `std` oder `var`, in Kleinbuchstaben. |

## Formeln liefern die Daten eines anderen Projekts

PlaidXL-Funktionen lesen aus dem Projekt, das mit der Arbeitsmappe verknüpft ist. Öffnen Sie den Aufgabenbereich in dieser Arbeitsmappe, wählen Sie das Projekt, für das der Bericht erstellt wurde, und erzwingen Sie dann eine vollständige Neuberechnung. Jede Arbeitsmappe hat ihr eigenes Projekt, daher ändert die Auswahl eines Projekts in einer anderen Arbeitsmappe nichts an dieser. Siehe [Das Projekt gehört zur Arbeitsmappe](/de/reference/cli/plaidxl/retrieve/#das-projekt-gehört-zur-arbeitsmappe).

## Tabellen aus einem anderen Workspace werden übersprungen

Nachdem Sie den Workspace gewechselt haben, teilt der Aufgabenbereich mit, wie viele verfolgte Tabellen zu einem anderen Workspace gehören und von **Refresh All Tables** übersprungen werden. Rufen Sie jede Tabelle im aktuellen Workspace erneut ab, um sie zu verknüpfen.

## Ein Speichern wird abgelehnt oder gestoppt

| Was Sie sehen | Was zu tun ist |
|---|---|
| Zeilen innerhalb der Tabelle sind leer | Zwei oder mehr aufeinanderfolgende leere Zeilen mit Daten darunter stoppen ein Speichern. Löschen Sie die leeren Zeilen oder füllen Sie sie, und speichern Sie dann erneut. |
| Die Tabelle hat sich seit dem Abruf geändert | Jemand anderes hat die Tabelle in PlaidCloud gespeichert. Rufen Sie sie erneut ab und wenden Sie Ihre Änderungen erneut an. |
| Ein Wert kann nicht konvertiert werden | Es wird nichts geschrieben, und die Zeilen werden aufgelistet. Korrigieren Sie die Werte passend zum Datentyp der Spalte. |
| Das Blatt ist nicht mit einer Tabelle verknüpft | Rufen Sie die Tabelle zuerst in das Blatt ab. **Save to PlaidCloud…** erscheint nur für Tabellen, die in das aktive Blatt abgerufen wurden. |

Um ein Speichern rückgängig zu machen, klicken Sie in der Bestätigungsmeldung auf **Restore previous version**, oder öffnen Sie die Tabelle in PlaidCloud und wählen Sie im Menü **As of** die Version vor dem Speichern aus. Der Wiederherstellungspunkt wird 7 Tage lang aufbewahrt. Siehe [Eine Tabelle in PlaidCloud speichern](/de/reference/cli/plaidxl/retrieve/#eine-tabelle-in-plaidcloud-speichern).

## Verwandte Themen

- [PlaidXL installieren](/de/reference/cli/plaidxl/install/)
- [Bei PlaidXL anmelden](/de/reference/cli/plaidxl/connect/)
- [Hilfe erhalten](/de/guides/support/getting-help/) – ein Support-Ticket öffnen
