---
title: Fehlerbehebung für PlaidXL
description: Lösungen für häufige PlaidXL-Probleme — das Add-in fehlt im Menüband, ein Anmelde-Popup öffnet sich nicht, Workspaces oder Projekte fehlen, Tabellen werden rot angezeigt, langsame Abrufe, Fehler in PlaidXL-Formeln und -Kennzahlen, eingegebene Werte, die nicht geschrieben werden, und Speichervorgänge, die abbrechen.
sidebar:
  label: Fehlerbehebung
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## Die Registerkarte „PlaidCloud“ fehlt im Menüband

- Schließen Sie alle Excel-Fenster und öffnen Sie Excel erneut. Ein neu installiertes Add-in erscheint oft erst nach einem Neustart.
- Öffnen Sie **Insert → My Add-ins** und wählen Sie **PlaidCloud** aus.
- Prüfen Sie, ob Sie Desktop-Excel für Microsoft 365 oder Excel 2021 oder höher verwenden. Siehe [PlaidXL installieren](/de/reference/cli/plaidxl/install/).
- Wenn Ihre Organisation Add-ins verwaltet, fragen Sie Ihren Microsoft-365-Administrator, ob das Add-in **PlaidCloud** für Sie bereitgestellt ist.

## Das Anmelde-Popup öffnet sich nicht

Wenn Sie auf **Sign In** klicken, fragt Excel, ob ein Popup-Fenster angezeigt werden soll. Erlauben Sie es. Wenn Sie die Abfrage verworfen haben, klicken Sie erneut auf **Sign In**.

Wenn sich das Popup öffnet, Sie die Anmeldung aber nicht abschließen können, versuchen Sie, sich in Ihrem Browser mit derselben E-Mail-Adresse bei PlaidCloud anzumelden. Ein Problem dort — ein abgelaufenes Kennwort oder ein Zwei-Faktor-Gerät, das Sie nicht mehr haben — muss zuerst in PlaidCloud behoben werden. Siehe [Mitgliederauthentifizierung](/de/administration/access/member-authentication/).

## Ein Workspace wird nicht aufgelistet

**Select a workspace** listet die Workspaces auf, denen Ihre E-Mail-Adresse angehört. Wenn einer fehlt, prüfen Sie, ob Sie dieselbe E-Mail-Adresse eingegeben haben, die Sie für diesen Workspace verwenden, und bitten Sie dann einen Workspace-Administrator zu bestätigen, dass Sie Mitglied sind. Siehe [Workspace-Mitglieder verwalten](/de/administration/access/overview/managing-workspace-members/).

Um zu einem anderen Workspace zu wechseln, dem Sie angehören, öffnen Sie das Kontomenü und wählen Sie **Switch workspace**.

## Ein Projekt, eine Tabelle oder eine Dimension fehlt

PlaidXL zeigt, was Ihr Konto in PlaidCloud sehen kann. Wenn ein Projekt fehlt, bitten Sie dessen Eigentümer, Ihnen Zugriff zu geben. Wenn eine Tabelle fehlt, prüfen Sie, ob sie im ausgewählten Projekt existiert und mit Daten geladen wurde — bei einer Tabelle, in die nie geschrieben wurde, erscheint beim Auswählen **Unable to get table metadata**.

Ordner in den Listen der Projekte, Tabellen und Dimensionen sind zunächst eingeklappt. Geben Sie einen Teil des Namens in das Filterfeld oben in der Liste ein, um ein Element in einem Ordner zu finden.

## Eine Tabelle wird rot angezeigt

Die Tabelle hat mehr Zeilen oder Spalten, als ein Excel-Arbeitsblatt fasst, oder PlaidCloud kann ihre Größe nicht melden. Sie können sie abrufen, und Zeilen, die nicht passen, setzen sich auf weiteren Blättern fort, aber eine auf mehrere Blätter verteilte Tabelle kann nicht gespeichert werden. Wählen Sie **Erweitert**, um die Zeilen zu filtern, und deaktivieren Sie die nicht benötigten Spalten, bis die Tabelle passt. Siehe [Rot angezeigte Tabellen](/de/reference/cli/plaidxl/retrieve/#rot-dargestellte-tabellen).

## Ein Abruf ist langsam

Excel ist bei breiten Tabellen am langsamsten. Deaktivieren Sie die Kontrollkästchen der Spalten, die Sie nicht benötigen, und filtern Sie die Zeilen mit **Erweitert**. Wenn Sie nur die Daten abrufen, mit denen Sie arbeiten, geht es schneller und die Arbeitsmappe wird kleiner.

Große Tabellen werden in Excel im Web und in aktuellem Desktop-Excel deutlich schneller abgerufen und aktualisiert. Ältere Excel-Versionen funktionieren weiterhin, nur ohne diese Beschleunigung.

Wenn der Bereich **PlaidXL was updated — reload the pane** meldet, schließen Sie den Aufgabenbereich, öffnen Sie ihn erneut und rufen Sie die Daten noch einmal ab. Nach einer Aktualisierung von PlaidXL übernimmt der Bereich die neue Version beim nächsten Laden.

Wenn ein Abruf **This PlaidCloud workspace needs an update for PlaidXL** meldet, bitten Sie Ihren Administrator, den Workspace auf ein aktuelles PlaidCloud-Release zu aktualisieren.

## Eine Formel zeigt einen Fehler an

| Was Sie sehen | Was zu prüfen ist |
|---|---|
| `#SPILL!` | In den Zellen, die das Ergebnis benötigt, steht etwas. Leeren Sie die Zellen unterhalb oder neben der Formel. |
| `#NAME?` | Excel erkennt die Funktion nicht. Prüfen Sie, ob PlaidXL installiert ist — die Registerkarte **PlaidCloud** ist im Menüband vorhanden — und prüfen Sie die Schreibweise anhand [der Funktionsliste](/de/reference/cli/plaidxl/functions/). |
| Ein Fehler einer `PLAIDXL`-Funktion | Prüfen Sie, ob Sie angemeldet sind und das richtige Projekt ausgewählt ist, und gleichen Sie dann alle Namen von Tabellen, Spalten, Dimensionen und Knoten mit PlaidCloud ab — die Namen müssen exakt übereinstimmen. |
| `CELL` meldet, dass eine Filterspalte nicht gefunden wurde | Das erste Argument von `DIMENSION_REPR` ist eine Spalte der Tabelle, keine Dimension. Verwenden Sie den Spaltennamen der Tabelle exakt. Siehe [Werte](/de/reference/cli/plaidxl/functions/#werte). |
| `#VALUE!` von `METRIC` oder `METRIC_BREAKDOWN` | Zeigen Sie mit der Maus auf die Zelle, um den Grund zu lesen. Siehe [Kennzahlfehler](/de/reference/cli/plaidxl/functions/#kennzahlfehler). |
| `#VALUE!` von einer Kennzahl: **This PlaidCloud workspace can't combine an alternate hierarchy with other members yet. Ask your administrator to update the workspace.** | Der Workspace muss aktualisiert werden, bevor eine Kennzahl ein Mitglied einer alternativen Hierarchie mit anderen Mitgliedern kombinieren kann. Fragen Sie Ihren Administrator. Andere Zellen derselben Neuberechnung liefern weiterhin Antworten. |
| `#VALUE!` von `CELL` oder `CELLS` | Zeigen Sie mit der Maus auf die Zelle, um den von PlaidCloud genannten Grund zu lesen, etwa eine unbekannte Spalte, einen Knoten, der nicht existiert oder keine Mitglieder hat, oder ein Problem bei der Berechnung des Werts. Gleichen Sie die Namen mit PlaidCloud ab. |
| `CELL` liefert eine unerwartete Summe | Ein Knoten wird nur in einer Spalte aufsummiert, die mit seiner Dimension verknüpft ist; in jeder anderen Spalte muss er exakt mit einem Wert übereinstimmen. Prüfen Sie Spalte und Knoten jedes Filters. |
| Werte ändern sich nicht, nachdem sich die Daten oder das Projekt geändert haben | Klicken Sie im Menü **Aktualisieren** des Menübands auf **Recalculate PlaidXL formulas**. |
| `MEASURE_TYPE` liefert einen Fehler | Verwenden Sie einen der Werte `sum`, `mean`, `median`, `min`, `max`, `std` oder `var`, in Kleinbuchstaben. |

## Formeln geben Daten eines anderen Projekts zurück

PlaidXL-Funktionen lesen aus dem Projekt, das mit der Arbeitsmappe verknüpft ist. Öffnen Sie den Aufgabenbereich in dieser Arbeitsmappe, wählen Sie das Projekt aus, für das der Bericht erstellt wurde, und klicken Sie dann im Menü **Aktualisieren** des Menübands auf **Recalculate PlaidXL formulas**. Jede Arbeitsmappe hat ihr eigenes Projekt, daher ändert die Auswahl in einer anderen Arbeitsmappe nichts an dieser. Siehe [Das Projekt gehört zur Arbeitsmappe](/de/reference/cli/plaidxl/retrieve/#das-projekt-gehört-zur-arbeitsmappe).

## Tabellen aus einem anderen Workspace werden übersprungen

Nachdem Sie den Workspace gewechselt haben, meldet **Refresh All Tables**, dass Tabellen oder Dimensionen aus einem anderen Workspace in dieser Arbeitsmappe nicht aktualisiert wurden, und sie werden unter **On this sheet** nicht aufgeführt. Rufen Sie jede Tabelle im aktuellen Workspace erneut ab, um sie zu verknüpfen.

## Ein eingegebener Wert wird nicht geschrieben

Wenn Sie einen Wert über ein `CELL` tippen, meldet der Aufgabenbereich, was er geschrieben hat, und listet mit Begründung auf, was nicht geschrieben wurde. Siehe [Werte in PlaidCloud eingeben](/de/reference/cli/plaidxl/write-values/).

| Was Sie sehen | Was zu tun ist |
|---|---|
| Nur eine Zelle mit genau einem `PLAIDXL.CELL` nimmt einen eingegebenen Wert an | Tippen Sie über eine Zelle, deren Formel ein einzelnes `CELL` ist, optional multipliziert, dividiert oder negiert. |
| Ein Argument kann hier nicht gelesen werden | Die Argumente von `CELL` müssen Zellen oder Text sein, keine anderen Berechnungen. |
| Eine Verteilungsmethode, Form oder Sperre gilt nur für Summen | Codes wie `E1200`, `1200 like FY2025` und `H` funktionieren nur bei **Summe**-Zellen. Geben Sie bei anderen eine einfache Zahl ein. |
| Alle Mitglieder gesperrt | Heben Sie eine Sperre mit `H` auf und geben Sie den Wert dann erneut ein. |
| Der Workspace nimmt in Excel eingegebene Werte noch nicht an | Bitten Sie Ihren Administrator, den Workspace zu aktualisieren. |

## Ein Speichern wird abgelehnt oder abgebrochen

Ein Speichervorgang schreibt sofort und bricht selten ab. Er bricht ab, wenn:

| Was Sie sehen | Was zu tun ist |
|---|---|
| Die Kopfzeile stimmt nicht mehr mit den abgerufenen Spalten überein | Stellen Sie die Kopfzeile so wieder her, wie sie abgerufen wurde, oder rufen Sie die Tabelle erneut ab. |
| Ein Wert kann nicht konvertiert werden | Es wird nichts geschrieben, und die Zeilen werden aufgelistet. Korrigieren Sie die Werte passend zum Datentyp der Spalte. |
| Die Tabelle setzt sich auf anderen Blättern fort | Eine auf mehrere Blätter verteilte Tabelle kann nicht gespeichert werden. Rufen Sie sie mit einem Filter ab, damit sie auf ein Blatt passt. |
| Die Tabelle wurde mit einem Filter abgerufen, auf den sich das Speichern nicht beschränken kann | Rufen Sie sie erneut mit einem Filter aus Regeln **gleich** und **in**, verbunden mit **AND**, oder ganz ohne Filter ab. |
| Zeilen liegen außerhalb Ihres Zeilenzugriffs | Es wird nichts gespeichert. Entfernen Sie diese Zeilen und speichern Sie dann erneut. |
| Spalten enthalten Text, der länger ist als die 32.767 Zeichen einer Excel-Zelle | Excel zeigt den Text abgeschnitten an, und beim Speichern würde er auch in PlaidCloud abgeschnitten, daher ist Speichern für diese Tabelle deaktiviert. Rufen Sie die Tabelle ohne diese Spalten ab, um sie zu speichern. |
| Die Tabelle wurde nur teilweise geschrieben | Excel hat einen Teil der letzten Aktualisierung abgelehnt. Aktualisieren Sie die Tabelle und speichern Sie sie dann. |
| Das Blatt ist nicht mit einer Tabelle verknüpft | Rufen Sie die Tabelle zuerst in das Blatt ab. Unter **On this sheet** werden nur Tabellen aufgeführt, die in das aktive Blatt abgerufen wurden. |

Um einen Speichervorgang rückgängig zu machen, klicken Sie in der Meldung auf **Rückgängig** oder im Menüband auf **Undo last write**. Jeder Speichervorgang behält seinen eigenen Wiederherstellungspunkt 7 Tage lang, sodass Sie jeden Speichervorgang bis zu 7 Tage nach seiner Ausführung rückgängig machen können. Siehe [Eine Tabelle in PlaidCloud speichern](/de/reference/cli/plaidxl/retrieve/#tabelle-in-plaidcloud-speichern).

## Verwandte Themen

- [PlaidXL installieren](/de/reference/cli/plaidxl/install/)
- [Bei PlaidXL anmelden](/de/reference/cli/plaidxl/connect/)
- [Hilfe erhalten](/de/guides/support/getting-help/) — ein Support-Ticket eröffnen
