---
title: Fehlerbehebung bei PlaidXL
description: Lösungen für häufige PlaidXL-Probleme – das Add-in fehlt in der Multifunktionsleiste, ein Anmelde-Pop-up öffnet sich nicht, fehlende Workspaces oder Projekte, rot angezeigte Tabellen, langsame Abrufe, Fehler in PlaidXL-Formeln und Kennzahlen, eingegebene Werte, die nicht geschrieben werden, und Speichervorgänge, die abbrechen.
sidebar:
  label: Fehlerbehebung
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## Die Registerkarte PlaidCloud fehlt in der Multifunktionsleiste

- Schließen Sie alle Excel-Fenster und starten Sie Excel neu. Ein neu installiertes Add-in erscheint oft erst nach einem Neustart.
- Öffnen Sie **Insert → My Add-ins** und wählen Sie **PlaidCloud** aus.
- Prüfen Sie, ob Sie Excel für den Desktop mit Microsoft 365 oder Excel 2021 oder neuer verwenden. Siehe [PlaidXL installieren](/de/reference/cli/plaidxl/install/).
- Wenn Ihre Organisation Add-ins zentral verwaltet, fragen Sie Ihren Microsoft-365-Administrator, ob das Add-in **PlaidCloud** für Sie bereitgestellt ist.

## Das Anmelde-Pop-up öffnet sich nicht

Wenn Sie auf **Sign In** klicken, fragt Excel, ob ein Pop-up-Fenster angezeigt werden soll. Lassen Sie es zu. Haben Sie die Abfrage verworfen, klicken Sie erneut auf **Sign In**.

Öffnet sich das Pop-up, Sie können die Anmeldung aber nicht abschließen, versuchen Sie, sich mit derselben E-Mail-Adresse im Browser bei PlaidCloud anzumelden. Ein Problem dort – ein abgelaufenes Passwort oder ein Zwei-Faktor-Gerät, das Sie nicht mehr haben – muss zuerst in PlaidCloud behoben werden. Siehe [Mitgliederauthentifizierung](/de/administration/access/member-authentication/).

## Ein Workspace wird nicht aufgeführt

**Select a workspace** listet die Workspaces auf, denen Ihre E-Mail-Adresse angehört. Fehlt einer, prüfen Sie, ob Sie dieselbe E-Mail-Adresse eingegeben haben, die Sie für diesen Workspace verwenden, und bitten Sie dann einen Workspace-Administrator, zu bestätigen, dass Sie Mitglied sind. Siehe [Workspace-Mitglieder verwalten](/de/administration/access/overview/managing-workspace-members/).

Um zu einem anderen Workspace zu wechseln, dem Sie angehören, öffnen Sie das Kontomenü und wählen Sie **Switch workspace**.

## Ein Projekt, eine Tabelle oder eine Dimension fehlt

PlaidXL zeigt, was Ihr Konto in PlaidCloud sehen kann. Fehlt ein Projekt, bitten Sie seinen Inhaber, Ihnen Zugriff zu geben. Fehlt eine Tabelle, prüfen Sie, ob sie im ausgewählten Projekt existiert und mit Daten geladen wurde – eine Tabelle, in die nie geschrieben wurde, zeigt beim Auswählen **Unable to get table metadata** an.

Ordner in den Listen der Projekte, Tabellen und Dimensionen sind zunächst eingeklappt. Geben Sie einen Teil des Namens in das Filterfeld oben in der Liste ein, um ein Element innerhalb eines Ordners zu finden.

## Eine Tabelle wird rot angezeigt

Die Tabelle hat mehr Zeilen oder Spalten, als ein Excel-Arbeitsblatt fasst, oder PlaidCloud kann ihre Größe nicht melden. Sie können sie abrufen, und Zeilen, die nicht passen, werden auf weiteren Blättern fortgesetzt, aber eine auf mehrere Blätter verteilte Tabelle kann nicht gespeichert werden. Wählen Sie **Erweitert** aus, um die Zeilen zu filtern, und deaktivieren Sie Spalten, die Sie nicht benötigen, bis sie passt. Siehe [Rot angezeigte Tabellen](/de/reference/cli/plaidxl/retrieve/#rot-angezeigte-tabellen).

## Ein Abruf ist langsam

Excel ist bei breiten Tabellen am langsamsten. Deaktivieren Sie die Kontrollkästchen von Spalten, die Sie nicht benötigen, und filtern Sie die Zeilen mit **Erweitert**. Nur die Daten abzurufen, mit denen Sie arbeiten, ist schneller und ergibt eine kleinere Arbeitsmappe.

## Eine Formel zeigt einen Fehler an

| Was Sie sehen | Was zu prüfen ist |
|---|---|
| `#SPILL!` | In den Zellen, die das Ergebnis benötigt, steht etwas. Leeren Sie die Zellen unterhalb oder neben der Formel. |
| `#NAME?` | Excel erkennt die Funktion nicht. Prüfen Sie, ob PlaidXL installiert ist – die Registerkarte **PlaidCloud** ist in der Multifunktionsleiste –, und prüfen Sie die Schreibweise anhand der [Funktionsliste](/de/reference/cli/plaidxl/functions/). |
| Ein Fehler einer `PLAIDXL`-Funktion | Prüfen Sie, ob Sie angemeldet sind und das richtige Projekt ausgewählt ist, und prüfen Sie dann jeden Tabellen-, Spalten-, Dimensions- und Knotennamen anhand von PlaidCloud – Namen müssen exakt übereinstimmen. |
| `CELL` meldet, dass eine Filterspalte nicht gefunden wurde | Das erste Argument von `DIMENSION_REPR` ist eine Spalte der Tabelle, keine Dimension. Verwenden Sie den Spaltennamen der Tabelle exakt. Siehe [Werte](/de/reference/cli/plaidxl/functions/#werte). |
| `#VALUE!` von `METRIC` oder `METRIC_BREAKDOWN` | Zeigen Sie auf die Zelle, um den Grund zu lesen. Siehe [Kennzahlfehler](/de/reference/cli/plaidxl/functions/#kennzahlfehler). |
| `#VALUE!` von `CELL` oder `CELLS` | Zeigen Sie auf die Zelle, um den von PlaidCloud genannten Grund zu lesen, etwa eine unbekannte Spalte, ein Knoten, der nicht existiert oder keine Elemente hat, oder ein Problem bei der Berechnung des Werts. Prüfen Sie die Namen anhand von PlaidCloud. |
| `CELL` liefert eine unerwartete Summe | Ein Knoten wird nur über eine Spalte aggregiert, die mit seiner Dimension verknüpft ist; bei jeder anderen Spalte muss er exakt mit einem Wert übereinstimmen. Prüfen Sie Spalte und Knoten jedes Filters. |
| Werte ändern sich nicht, nachdem sich die Daten oder das Projekt geändert haben | Klicken Sie im Menü **Aktualisieren** der Multifunktionsleiste auf **Recalculate PlaidXL formulas**. |
| `MEASURE_TYPE` liefert einen Fehler | Verwenden Sie eines von `sum`, `mean`, `median`, `min`, `max`, `std` oder `var`, in Kleinbuchstaben. |

## Formeln liefern Daten eines anderen Projekts

PlaidXL-Funktionen lesen aus dem Projekt, das mit der Arbeitsmappe verknüpft ist. Öffnen Sie in dieser Arbeitsmappe den Aufgabenbereich, wählen Sie das Projekt aus, für das der Bericht erstellt wurde, und klicken Sie dann im Menü **Aktualisieren** der Multifunktionsleiste auf **Recalculate PlaidXL formulas**. Jede Arbeitsmappe hat ihr eigenes Projekt, sodass die Auswahl eines Projekts in einer anderen Arbeitsmappe diese hier nicht ändert. Siehe [Das Projekt gehört zur Arbeitsmappe](/de/reference/cli/plaidxl/retrieve/#das-projekt-gehört-zur-arbeitsmappe).

## Tabellen aus einem anderen Workspace werden übersprungen

Nachdem Sie den Workspace gewechselt haben, meldet **Refresh All Tables**, dass Tabellen oder Dimensionen aus einem anderen Workspace in dieser Arbeitsmappe nicht aktualisiert wurden, und sie werden nicht unter **On this sheet** aufgeführt. Rufen Sie jede Tabelle im aktuellen Workspace erneut ab, um sie zu verknüpfen.

## Ein eingegebener Wert wird nicht geschrieben

Wenn Sie über ein `CELL` tippen, nennt der Aufgabenbereich, was er geschrieben hat, und listet mit Begründung auf, was er nicht geschrieben hat. Siehe [Werte in PlaidCloud eingeben](/de/reference/cli/plaidxl/write-values/).

| Was Sie sehen | Was zu tun ist |
|---|---|
| Nur eine Zelle, die genau eine `PLAIDXL.CELL` enthält, nimmt einen eingegebenen Wert an | Tippen Sie über eine Zelle, deren Formel ein einzelnes `CELL` ist, optional multipliziert, dividiert oder negiert. |
| Ein Argument kann hier nicht gelesen werden | Die Argumente des `CELL` müssen Zellen oder Text sein, keine anderen Berechnungen. |
| Eine Verteilmethode, Form oder Sperre gilt nur für Summen | Codes wie `E1200`, `1200 like FY2025` und `H` funktionieren nur bei **Summe**-Zellen. Geben Sie bei anderen eine einfache Zahl ein. |
| Alle Elemente gesperrt | Heben Sie eine Sperre mit `H` auf und geben Sie den Wert dann erneut ein. |
| Der Workspace nimmt in Excel eingegebene Werte noch nicht an | Bitten Sie Ihren Administrator, den Workspace zu aktualisieren. |

## Ein Speichern wird verweigert oder abgebrochen

Ein Speichern schreibt sofort und bricht selten ab. Es bricht ab, wenn:

| Was Sie sehen | Was zu tun ist |
|---|---|
| Die Kopfzeile stimmt nicht mehr mit den abgerufenen Spalten überein | Stellen Sie die Kopfzeile so wieder her, wie sie abgerufen wurde, oder rufen Sie die Tabelle erneut ab. |
| Ein Wert kann nicht umgewandelt werden | Es wird nichts geschrieben, und die Zeilen werden aufgelistet. Korrigieren Sie die Werte passend zum Datentyp der Spalte. |
| Die Tabelle wird auf anderen Blättern fortgesetzt | Eine auf mehrere Blätter verteilte Tabelle kann nicht gespeichert werden. Rufen Sie sie mit einem Filter ab, sodass sie auf ein Blatt passt. |
| Die Tabelle wurde mit einem Filter abgerufen, den das Speichern nicht einhalten kann | Rufen Sie sie erneut mit einem Filter aus **Gleich**- und **in**-Regeln, verknüpft mit **AND**, oder ohne Filter ab. |
| Zeilen liegen außerhalb Ihres Zeilenzugriffs | Es wird nichts gespeichert. Entfernen Sie diese Zeilen oder bitten Sie einen Projekt-Architect, sie zu speichern. |
| Das Blatt ist nicht mit einer Tabelle verknüpft | Rufen Sie die Tabelle zuerst in das Blatt ab. Nur in das aktive Blatt abgerufene Tabellen werden unter **On this sheet** aufgeführt. |

Um ein Speichern rückgängig zu machen, klicken Sie in der Meldung auf **Rückgängig** oder in der Multifunktionsleiste auf **Undo last write**. Der Wiederherstellungspunkt wird 7 Tage aufbewahrt. Siehe [Eine Tabelle nach PlaidCloud speichern](/de/reference/cli/plaidxl/retrieve/#eine-tabelle-nach-plaidcloud-speichern).

## Verwandte Themen

- [PlaidXL installieren](/de/reference/cli/plaidxl/install/)
- [Bei PlaidXL anmelden](/de/reference/cli/plaidxl/connect/)
- [Hilfe erhalten](/de/guides/support/getting-help/) – ein Support-Ticket öffnen
