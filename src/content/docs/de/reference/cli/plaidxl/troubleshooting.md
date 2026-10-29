---
title: PlaidXL-Fehlerbehebung
description: Lösungen für häufige PlaidXL-Probleme — das Add-in fehlt im Menüband, ein Anmelde-Popup öffnet sich nicht, Workspaces oder Projekte fehlen, Tabellen werden rot angezeigt, Abrufe sind langsam und PlaidXL-Formeln liefern Fehler.
sidebar:
  label: Fehlerbehebung
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## Die Registerkarte „PlaidCloud“ fehlt im Menüband

- Schließen Sie alle Excel-Fenster und öffnen Sie Excel erneut. Ein neu installiertes Add-in erscheint oft erst nach einem Neustart.
- Öffnen Sie **Insert → My Add-ins** und wählen Sie **PlaidCloud** aus.
- Prüfen Sie, ob Sie Excel für Microsoft 365 oder Excel 2021 oder höher als Desktop-Version verwenden. Siehe [PlaidXL installieren](/de/reference/cli/plaidxl/install/).
- Wenn Ihre Organisation Add-ins verwaltet, fragen Sie Ihren Microsoft-365-Administrator, ob das Add-in **PlaidCloud** für Sie bereitgestellt ist.

## Das Anmelde-Popup öffnet sich nicht

Wenn Sie auf **Sign In** klicken, fragt Excel, ob ein Popup-Fenster angezeigt werden soll. Lassen Sie es zu. Wenn Sie die Abfrage verworfen haben, klicken Sie erneut auf **Sign In**.

Wenn sich das Popup öffnet, Sie die Anmeldung aber nicht abschließen können, versuchen Sie, sich mit derselben E-Mail-Adresse im Browser bei PlaidCloud anzumelden. Ein Problem dort — ein abgelaufenes Passwort oder ein Zwei-Faktor-Gerät, das Sie nicht mehr besitzen — muss zuerst in PlaidCloud behoben werden. Siehe [Mitgliederauthentifizierung](/de/administration/access/member-authentication/).

## Ein Workspace wird nicht aufgeführt

**Select a tenant** listet die Workspaces auf, denen Ihre E-Mail-Adresse angehört. Wenn einer fehlt, prüfen Sie, ob Sie dieselbe E-Mail-Adresse eingegeben haben, die Sie für diesen Workspace verwenden, und bitten Sie dann einen Workspace-Administrator, Ihre Mitgliedschaft zu bestätigen. Siehe [Workspace-Mitglieder verwalten](/de/administration/access/overview/managing-workspace-members/).

Um zu einem anderen Workspace zu wechseln, dem Sie angehören, klicken Sie auf **Logout** und melden Sie sich erneut an.

## Ein Projekt, eine Tabelle oder eine Dimension fehlt

PlaidXL zeigt an, was Ihr Konto in PlaidCloud sehen kann. Wenn ein Projekt fehlt, bitten Sie dessen Eigentümer, Ihnen Zugriff zu geben. Wenn eine Tabelle fehlt, prüfen Sie, ob sie im ausgewählten Projekt existiert und mit Daten geladen wurde — eine Tabelle, in die nie geschrieben wurde, zeigt beim Auswählen **Unable to get table metadata** an.

Ordner in den Listen der Projekte, Tabellen und Dimensionen sind zunächst eingeklappt. Geben Sie einen Teil des Namens in das Filterfeld oben in der Liste ein, um ein Element in einem Ordner zu finden.

## Eine Tabelle wird rot angezeigt

Die Tabelle hat mehr Zeilen oder Spalten, als ein Excel-Arbeitsblatt fasst. Wählen Sie **Erweitert**, um die Zeilen zu filtern, und deaktivieren Sie die nicht benötigten Spalten, bis sie passt. Siehe [Rot angezeigte Tabellen](/de/reference/cli/plaidxl/retrieve/#rot-angezeigte-tabellen).

## Ein Abruf ist langsam

Excel ist bei breiten Tabellen am langsamsten. Deaktivieren Sie die Kontrollkästchen von Spalten, die Sie nicht benötigen, und filtern Sie die Zeilen mit **Erweitert**. Wenn Sie nur die Daten abrufen, mit denen Sie arbeiten, geht es schneller und die Arbeitsmappe wird kleiner.

## Eine Formel zeigt einen Fehler an

| Was Sie sehen | Was zu prüfen ist |
|---|---|
| `#SPILL!` | In den Zellen, die das Ergebnis benötigt, steht etwas. Leeren Sie die Zellen unterhalb oder neben der Formel. |
| `#NAME?` | Excel erkennt die Funktion nicht. Prüfen Sie, ob PlaidXL installiert ist — die Registerkarte **PlaidCloud** ist im Menüband vorhanden — und prüfen Sie die Schreibweise anhand der [Funktionsliste](/de/reference/cli/plaidxl/functions/). |
| Ein Fehler einer `PLAIDXL`-Funktion | Prüfen Sie, ob Sie angemeldet und das richtige Projekt ausgewählt sind, und prüfen Sie dann jeden Namen von Tabelle, Spalte, Dimension und Knoten anhand von PlaidCloud — die Namen müssen exakt übereinstimmen. |
| `CELL` meldet, dass eine Filterspalte nicht gefunden wurde | Das erste Argument von `DIMENSION_REPR` ist eine Spalte der Tabelle, keine Dimension. Verwenden Sie den Spaltennamen der Tabelle exakt. Siehe [Werte](/de/reference/cli/plaidxl/functions/#werte). |
| `CELL` liefert 0 oder eine unerwartete Summe | Prüfen Sie den Knotennamen anhand der Dimension — ein Knoten, der nicht existiert, aggregiert nichts und liefert 0. Ein Knoten wird nur für eine Spalte aggregiert, die mit seiner Dimension verknüpft ist; bei jeder anderen Spalte muss er exakt einem Wert entsprechen. |
| Werte ändern sich nicht, nachdem sich die Daten oder das Projekt geändert haben | Erzwingen Sie eine vollständige Neuberechnung — unter Windows mit **Strg+Alt+F9**. |
| `MEASURE_TYPE` liefert einen Fehler | Verwenden Sie eines von `sum`, `mean`, `median`, `min`, `max`, `std` oder `var`, in Kleinbuchstaben. |

## Formeln liefern Daten eines anderen Projekts

PlaidXL-Funktionen lesen aus dem im Aufgabenbereich ausgewählten Projekt, und diese Auswahl gilt für alle geöffneten Arbeitsmappen. Wählen Sie das Projekt aus, für das der Bericht erstellt wurde, und erzwingen Sie dann eine vollständige Neuberechnung. **Als Standard festlegen** speichert ein Projekt in der Arbeitsmappe, sodass es beim Öffnen des Aufgabenbereichs dort ausgewählt ist. Siehe [Standardprojekt festlegen](/de/reference/cli/plaidxl/retrieve/#standardprojekt-festlegen).

## Verwandte Themen

- [PlaidXL installieren](/de/reference/cli/plaidxl/install/)
- [Bei PlaidXL anmelden](/de/reference/cli/plaidxl/connect/)
- [Hilfe erhalten](/de/guides/support/getting-help/) — ein Support-Ticket erstellen
