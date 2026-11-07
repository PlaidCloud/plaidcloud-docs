---
title: Fehlerbehebung bei PlaidXL
description: Lösungen für häufige PlaidXL-Probleme — das im Menüband fehlende Add-in, ein Anmelde-Popup, das sich nicht öffnet, fehlende Workspaces oder Projekte, rot angezeigte Tabellen, langsame Abrufe, Fehler in PlaidXL-Formeln und Kennzahlen, eingegebene Werte, die nicht geschrieben werden, und Speichervorgänge, die abbrechen.
sidebar:
  label: Fehlerbehebung
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## Die Registerkarte „PlaidCloud“ fehlt im Menüband

- Schließen Sie alle Excel-Fenster und starten Sie Excel neu. Ein neu installiertes Add-in erscheint oft erst nach einem Neustart.
- Öffnen Sie **Insert → My Add-ins** und wählen Sie **PlaidCloud**.
- Prüfen Sie, ob Sie Desktop-Excel für Microsoft 365 oder Excel 2021 oder höher verwenden. Siehe [PlaidXL installieren](/de/reference/cli/plaidxl/install/).
- Wenn Ihre Organisation Add-ins verwaltet, fragen Sie Ihren Microsoft-365-Administrator, ob das Add-in **PlaidCloud** für Sie bereitgestellt ist.

## Das Anmelde-Popup öffnet sich nicht

Wenn Sie auf **Sign In** klicken, fragt Excel, ob ein Popup-Fenster angezeigt werden soll. Lassen Sie es zu. Haben Sie die Aufforderung geschlossen, klicken Sie erneut auf **Sign In**.

Öffnet sich das Popup, aber Sie können die Anmeldung nicht abschließen, versuchen Sie, sich in Ihrem Browser mit derselben E-Mail-Adresse bei PlaidCloud anzumelden. Ein Problem dort — ein abgelaufenes Kennwort oder ein Zwei-Faktor-Gerät, das Sie nicht mehr haben — muss zuerst in PlaidCloud behoben werden. Siehe [Mitgliederauthentifizierung](/de/administration/access/member-authentication/).

## Ein Workspace wird nicht aufgelistet

**Select a workspace** listet die Workspaces auf, zu denen Ihre E-Mail-Adresse gehört. Fehlt einer, prüfen Sie, ob Sie dieselbe E-Mail-Adresse eingegeben haben, die Sie für diesen Workspace verwenden, und bitten Sie dann einen Workspace-Administrator zu bestätigen, dass Sie Mitglied sind. Siehe [Workspace-Mitglieder verwalten](/de/administration/access/overview/managing-workspace-members/).

Um zu einem anderen Workspace zu wechseln, zu dem Sie gehören, öffnen Sie das Kontomenü und wählen Sie **Switch workspace**.

## Ein Projekt, eine Tabelle oder eine Dimension fehlt

PlaidXL zeigt, was Ihr Konto in PlaidCloud sehen kann. Fehlt ein Projekt, bitten Sie dessen Inhaber, Ihnen Zugriff zu geben. Fehlt eine Tabelle, prüfen Sie, ob sie im ausgewählten Projekt vorhanden und mit Daten geladen ist — bei einer Tabelle, in die noch nie geschrieben wurde, wird beim Auswählen **Unable to get table metadata** angezeigt.

Ordner in den Listen der Projekte, Tabellen und Dimensionen sind zunächst zugeklappt. Geben Sie einen Teil des Namens in das Filterfeld oben in der Liste ein, um ein Element in einem Ordner zu finden.

## Eine Tabelle wird rot angezeigt

Die Tabelle hat mehr Zeilen oder Spalten, als ein Excel-Arbeitsblatt aufnimmt, oder PlaidCloud kann ihre Größe nicht melden. Sie können sie abrufen, und Zeilen, die nicht passen, werden auf weiteren Blättern fortgesetzt, aber eine auf mehrere Blätter verteilte Tabelle kann nicht gespeichert werden. Wählen Sie **Erweitert**, um die Zeilen zu filtern, und deaktivieren Sie die Spalten, die Sie nicht benötigen, bis sie passt. Siehe [Rot angezeigte Tabellen](/de/reference/cli/plaidxl/retrieve/#rot-angezeigte-tabellen).

## Ein Abruf ist langsam

Excel ist bei breiten Tabellen am langsamsten. Deaktivieren Sie die Kontrollkästchen der Spalten, die Sie nicht benötigen, und filtern Sie die Zeilen mit **Erweitert**. Nur die Daten abzurufen, mit denen Sie arbeiten, ist schneller und ergibt eine kleinere Arbeitsmappe.

## Eine Formel zeigt einen Fehler an

| Was Sie sehen | Was zu prüfen ist |
|---|---|
| `#SPILL!` | In den Zellen, die das Ergebnis benötigt, steht etwas. Leeren Sie die Zellen unterhalb oder neben der Formel. |
| `#NAME?` | Excel erkennt die Funktion nicht. Prüfen Sie, ob PlaidXL installiert ist — die Registerkarte **PlaidCloud** ist im Menüband vorhanden — und prüfen Sie die Schreibweise anhand [der Funktionsliste](/de/reference/cli/plaidxl/functions/). |
| Ein Fehler von einer `PLAIDXL`-Funktion | Prüfen Sie, ob Sie angemeldet und das richtige Projekt ausgewählt ist, und prüfen Sie dann alle Namen von Tabellen, Spalten, Dimensionen und Knoten anhand von PlaidCloud — die Namen müssen exakt übereinstimmen. |
| `CELL` meldet, dass eine Filterspalte nicht gefunden wurde | Das erste Argument von `DIMENSION_REPR` ist eine Spalte der Tabelle, keine Dimension. Verwenden Sie den Spaltennamen der Tabelle exakt. Siehe [Werte](/de/reference/cli/plaidxl/functions/#werte). |
| `#VALUE!` von `METRIC` oder `METRIC_BREAKDOWN` | Zeigen Sie auf die Zelle, um den Grund zu lesen. Siehe [Kennzahlfehler](/de/reference/cli/plaidxl/functions/#kennzahlfehler). |
| `#VALUE!` von `CELL` oder `CELLS` | Zeigen Sie auf die Zelle, um den von PlaidCloud genannten Grund zu lesen, etwa eine unbekannte Spalte, ein Knoten, der nicht existiert oder keine Mitglieder hat, oder ein Problem bei der Berechnung des Werts. Prüfen Sie die Namen anhand von PlaidCloud. |
| `CELL` gibt eine unerwartete Gesamtsumme zurück | Ein Knoten wird nur bei einer Spalte aggregiert, die mit seiner Dimension verknüpft ist; bei jeder anderen Spalte muss er exakt mit einem Wert übereinstimmen. Prüfen Sie Spalte und Knoten jedes Filters. |
| Werte ändern sich nicht, nachdem sich die Daten oder das Projekt geändert haben | Klicken Sie im Menü **Aktualisieren** des Menübands auf **Recalculate PlaidXL formulas**. |
| `MEASURE_TYPE` gibt einen Fehler zurück | Verwenden Sie einen der Werte `sum`, `mean`, `median`, `min`, `max`, `std` oder `var`, in Kleinbuchstaben. |

## Formeln geben Daten eines anderen Projekts zurück

PlaidXL-Funktionen lesen aus dem Projekt, das mit der Arbeitsmappe verknüpft ist. Öffnen Sie den Aufgabenbereich in dieser Arbeitsmappe, wählen Sie das Projekt aus, für das der Bericht erstellt wurde, und klicken Sie dann im Menü **Aktualisieren** des Menübands auf **Recalculate PlaidXL formulas**. Jede Arbeitsmappe hat ihr eigenes Projekt, sodass die Auswahl in einer anderen Arbeitsmappe diese nicht ändert. Siehe [Das Projekt gehört zur Arbeitsmappe](/de/reference/cli/plaidxl/retrieve/#das-projekt-gehört-zur-arbeitsmappe).

## Tabellen aus einem anderen Workspace werden übersprungen

Nachdem Sie den Workspace gewechselt haben, meldet **Refresh All Tables**, dass Tabellen oder Dimensionen aus einem anderen Workspace in dieser Arbeitsmappe nicht aktualisiert wurden, und sie werden nicht unter **On this sheet** aufgelistet. Rufen Sie jede Tabelle im aktuellen Workspace erneut ab, um sie zu verknüpfen.

## Ein eingegebener Wert wird nicht geschrieben

Wenn Sie ein `CELL` überschreiben, nennt der Aufgabenbereich, was er geschrieben hat, und listet alles auf, was er nicht geschrieben hat, jeweils mit dem Grund. Siehe [Werte in PlaidCloud eingeben](/de/reference/cli/plaidxl/write-values/).

| Was Sie sehen | Was zu tun ist |
|---|---|
| Nur eine Zelle mit genau einem `PLAIDXL.CELL` nimmt einen eingegebenen Wert an | Überschreiben Sie eine Zelle, deren Formel ein einzelnes `CELL` ist, optional multipliziert, dividiert oder negiert. |
| Ein Argument kann hier nicht gelesen werden | Die Argumente von `CELL` müssen Zellen oder Text sein, keine anderen Berechnungen. |
| Eine Verteilungsmethode, -form oder Sperre gilt nur für Summen | Codes wie `E1200`, `1200 like FY2025` und `H` funktionieren nur bei Zellen vom Typ **Summe**. Geben Sie bei anderen eine einfache Zahl ein. |
| Alle Mitglieder gesperrt | Heben Sie eine Sperre mit `H` auf und geben Sie den Wert dann erneut ein. |
| Der Workspace nimmt noch keine in Excel eingegebenen Werte an | Bitten Sie Ihren Administrator, den Workspace zu aktualisieren. |

## Ein Speichern wird abgelehnt oder abgebrochen

Ein Speichern schreibt sofort und bricht selten ab. Es bricht ab, wenn:

| Was Sie sehen | Was zu tun ist |
|---|---|
| Die Kopfzeile stimmt nicht mehr mit den abgerufenen Spalten überein | Stellen Sie die Kopfzeile so wieder her, wie sie abgerufen wurde, oder rufen Sie die Tabelle erneut ab. |
| Ein Wert kann nicht umgewandelt werden | Es wird nichts geschrieben, und die Zeilen werden aufgelistet. Korrigieren Sie die Werte passend zum Datentyp der Spalte. |
| Die Tabelle wird auf anderen Blättern fortgesetzt | Eine auf mehrere Blätter verteilte Tabelle kann nicht gespeichert werden. Rufen Sie sie mit einem Filter ab, sodass sie auf ein Blatt passt. |
| Die Tabelle wurde mit einem Filter abgerufen, den Save nicht beibehalten kann | Rufen Sie sie erneut mit einem Filter aus durch **AND** verbundenen **gleich**- und **in**-Regeln ab, oder ohne Filter. |
| Zeilen liegen außerhalb Ihres Zeilenzugriffs | Es wird nichts gespeichert. Entfernen Sie diese Zeilen und speichern Sie dann erneut. |
| Das Blatt ist nicht mit einer Tabelle verknüpft | Rufen Sie die Tabelle zuerst auf das Blatt ab. Nur Tabellen, die in das aktive Blatt abgerufen wurden, werden unter **On this sheet** aufgelistet. |

Um ein Speichern rückgängig zu machen, klicken Sie in der Meldung auf **Rückgängig** oder im Menüband auf **Undo last write**. Der Wiederherstellungspunkt wird 7 Tage lang aufbewahrt. Siehe [Eine Tabelle nach PlaidCloud speichern](/de/reference/cli/plaidxl/retrieve/#tabelle-in-plaidcloud-speichern).

## Verwandte Themen

- [PlaidXL installieren](/de/reference/cli/plaidxl/install/)
- [Bei PlaidXL anmelden](/de/reference/cli/plaidxl/connect/)
- [Hilfe erhalten](/de/guides/support/getting-help/) — ein Support-Ticket öffnen
