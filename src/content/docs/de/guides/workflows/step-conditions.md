---
title: Bedingte Schrittausführung
description: Konfigurieren Sie die bedingte Ausführung für PlaidCloud-Workflow-Schritte, um anhand von Variablenwerten und Logik zu steuern, welche Schritte ausgeführt werden.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/step-conditions.md
---

## Überblick

Workflow-Schritte werden normalerweise in der für den Workflow definierten Reihenfolge ausgeführt. Oft ist es jedoch sinnvoll, bestimmte Schritte nur dann auszuführen, wenn vordefinierte Bedingungen erfüllt sind. Mit den Schrittbedingungen können Sie die Ausführung anhand der folgenden Optionen steuern:
 - Variablenwerte
 - Tabelle enthält Zeilen oder ist leer
 - Tabelle ist vorhanden oder nicht vorhanden
 - Eine Datei ist in Document vorhanden
 - Eine Datei fehlt in Document
 - Ergebnis einer Tabellenabfrage
 - Datums- und Zeitbedingungen sind erfüllt

Für Vergleiche von Variablen oder Ergebnissen von Tabellenabfragen stehen die folgenden Vergleiche zur Verfügung:
 - Gleich
 - Ungleich
 - Enthält
 - Enthält nicht
 - Beginnt mit
 - Endet mit
 - Größer als
 - Kleiner als
 - Größer oder gleich
 - Kleiner oder gleich

Wichtig ist außerdem, dass Sie mehrere Bedingungen festlegen können, die alle erfüllt sein müssen, damit der Schritt ausgeführt wird. Das ist ein leistungsfähiges Werkzeug, um genau zu steuern, wann ein Schritt ausgeführt werden soll.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 640 190" role="img" aria-label="Eine Schrittbedingung steuert, ob ein Schritt ausgeführt wird. Wenn der vorherige Schritt abgeschlossen ist, wird die Bedingung geprüft; ist sie erfüllt, wird der Schritt ausgeführt, andernfalls wird der Schritt übersprungen und der Workflow läuft mit dem nächsten Schritt weiter." style="width:100%;max-width:640px;height:auto;">
  <defs><marker id="sc3-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="74" width="104" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="66" y="100" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">vorheriger Schritt</text>
  <path d="M118 96 L150 96" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <rect x="152" y="66" width="150" height="60" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="227" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">Bedingung erfüllt?</text>
  <text x="227" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">Variable · Zeilen · Dokument</text>
  <path d="M302 82 C340 82 350 54 384 54" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="345" y="48" text-anchor="middle" font-size="10" fill="var(--sl-color-accent)">wahr</text>
  <path d="M302 110 C340 110 350 138 384 138" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="5 4" marker-end="url(#sc3-arrow)" />
  <text x="345" y="132" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">falsch</text>
  <rect x="386" y="34" width="128" height="40" rx="8" fill="var(--sl-color-accent)" fill-opacity="0.12" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="450" y="59" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-text)">Schritt läuft</text>
  <rect x="386" y="118" width="128" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="450" y="143" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">Schritt übersprungen</text>
  <path d="M514 54 C548 54 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <path d="M514 138 C548 138 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="606" y="100" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">weiter</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Eine Bedingung steuert den Schritt: erfüllt → der Schritt wird ausgeführt; nicht erfüllt → er wird übersprungen. In beiden Fällen geht der Workflow zum nächsten Schritt über. Bedingungen prüfen Variablen, ob eine Tabelle Zeilen enthält oder ob ein Dokument vorhanden ist.</figcaption>
</figure>

## Bedingungen hinzufügen und steuern

So aktivieren Sie Bedingungen für einen Schritt und fügen sie hinzu:
1) Suchen Sie den Schritt, dem Sie eine Bedingung hinzufügen möchten.
2) Klicken Sie mit der rechten Maustaste auf den Schritt und wählen Sie **Schrittdetails bearbeiten**, oder klicken Sie auf sein Zahnradsymbol und wechseln Sie zur Registerkarte **Allgemein**.
3) Scrollen Sie zum Abschnitt **Bedingungsprüfungen** am unteren Ende der Registerkarte **Allgemein**.
4) Aktivieren Sie das Kontrollkästchen **Bedingungen vor der Ausführung prüfen**, um den Dialog zu aktivieren und Bedingungen hinzuzufügen.
5) Wählen Sie im Abschnitt **Bedingungsprüfungen** links das „+“, um eine neue Bedingung hinzuzufügen.
6) Fügen Sie auf der rechten Seite in den Registerkarten eine Bedingung hinzu.
7) Wiederholen Sie die Schritte 5 und 6 nach Bedarf, um alle Ihre Bedingungen hinzuzufügen.

## Bedingungen auf der visuellen Arbeitsfläche sehen

Die Bedingungen eines Schritts sind auf der visuellen Arbeitsfläche sichtbar, ohne den Schritt zu öffnen. Der Konnektor, der in einen bedingten Schritt führt, ist **gestrichelt** und trägt an seiner Pfeilspitze einen kleinen **Schild**. Der Strich ist das, was Sie erkennen, wenn Sie so weit herausgezoomt haben, dass der Schild zu klein ist, um ihn auszumachen.

Klicken Sie auf den Schild, um den Schritt zu öffnen, wobei seine **Bedingungsprüfungen** bereits in den sichtbaren Bereich gescrollt sind. Sie können auch mit der rechten Maustaste auf den Konnektor klicken und **Bedingungen bearbeiten…** wählen, was dasselbe bewirkt. Der Schild auf der eigenen Kachel des Schritts unten links kennzeichnet den Schritt weiterhin wie gewohnt als bedingt.

In zwei Fällen wird absichtlich kein Schild an einem Pfeil angezeigt:

- **Ein Schritt ohne eingehenden Konnektor.** Ein Schritt, der von einem Datum oder einer Variablen abhängt, kann am Anfang eines Workflows stehen, ohne dass etwas in ihn führt. Es gibt keinen Pfeil, den man markieren könnte, daher erscheint nur der Schild auf der Kachel.
- **Ein Schritt in einer eingeklappten Gruppe.** Seine Kachel ist in die der Gruppe eingefaltet, und der Pfeil setzt an der Gruppe statt am Schritt an. Eine Markierung würde die Bedingung daher dem falschen Element zuordnen.

Ein Schritt mit mehreren eingehenden Konnektoren erhält einen Schild, nicht einen pro Pfeil.

:::note
Das Öffnen der Bedingungen auf diesem Weg führt bei Schritttypen, die das native Schrittformular verwenden, direkt zu den Bedingungsprüfungen. Ein Schritttyp, der noch das ältere Konfigurationsfenster öffnet, öffnet es stattdessen am Anfang – die Bedingungen sind vorhanden, es wird nur nicht zu ihnen gescrollt.
:::

### Was der Schild als Prüfung anzeigt

Der QuickInfo-Text des Schilds listet auf, was der Schritt tatsächlich prüft, anstatt nur mitzuteilen,
dass er etwas prüft:

```
Table Row Count (sales_2026) > 0 where region = 'EU'
Day of Week = Monday (UTC+2)
Project Variable (run_mode) = "full"
```

Bis zu drei Prüfungen werden aufgelistet, gefolgt von der Anzahl der übrigen – *…und 2 weitere Prüfungen* –, damit
die Liste bei einem Schritt mit vielen Bedingungen lesbar bleibt. Dieselbe Zusammenfassung erscheint am
Schild auf der Kachel des Schritts selbst, der als einziger bei einem Schritt ohne eingehenden Konnektor vorhanden ist.

Wenn Sie den Schritt auswählen, steht dieselbe Liste im Bereich **Bedingungen** des Inspektor-Bereichs,
wo sich eine lange Liste leichter lesen lässt.

Zur Formulierung ist Folgendes zu beachten:

- **Tages- und Monatsprüfungen werden als Namen angezeigt**, nicht als die dahinter gespeicherten Zahlen – *Wochentag =
  Montag*, nicht *Wochentag = 3*.
- **Die Zeitzone erscheint nur, wenn sie nicht UTC ist**, wie oben bei *(UTC+2)*.
- **Ein Filter bei einer Tabellenprüfung wird angezeigt**, und zwar nach `where`, bei Bedarf gekürzt.
- **Ein aggregierter Vergleich weist darauf hin** – *Abfragewert (aggregiert sales_2026.amount) >=
  100* vergleicht eine Summe über die Tabelle, während *Abfragewert (sales_2026.amount) >= 100*
  den Wert einer einzelnen Zeile vergleicht.
- **Eine Dokumentprüfung zeigt den Pfad, aber nicht das Konto.** Zwei Bedingungen, die denselben
  Pfad in verschiedenen Document-Konten prüfen, lesen sich identisch; öffnen Sie den Schritt, um sie
  zu unterscheiden.
- **Eine im Strukturbrowser ausgewählte Tabelle wird mit ihrem Namen angezeigt**, wenn der Workflow diese Tabelle
  irgendwo liest oder schreibt. Andernfalls wird die Prüfung ohne den Tabellennamen aufgelistet,
  statt mit einer internen Kennung.


### Was die Sperre Sie kosten würde

Bewegen Sie den Mauszeiger über den Schild, ohne zu klicken, und die Arbeitsfläche hebt den bedingten Schritt und alles, was ihm nachgelagert ist, mit einer gestrichelten Hervorhebung hervor – die Schritte, die nicht ausgeführt würden, wenn diese Bedingung blockiert. Es ändert sich nichts; bewegen Sie den Zeiger weg, und die Hervorhebung verschwindet. Vorgelagerte Schritte werden nie hervorgehoben: Sie werden in jedem Fall ausgeführt.

Das ist dieselbe Vorschau, die das Kennzeichen **deaktiviert** einer deaktivierten Gruppe bietet, mit einem wichtigen Unterschied in der Formulierung. Eine deaktivierte Gruppe ist wirklich ausgeschaltet, daher nennt ihr Kennzeichen, wie viele Schritte übersprungen *werden*. Eine Bedingung wird erst ausgewertet, wenn die Ausführung sie erreicht, daher gibt der Schild an, wie viele Schritte nicht ausgeführt *würden*, **falls** die Bedingung blockiert. Es kann durchaus sein, dass sie alles durchlässt.

### Was der Schild über die letzte Ausführung aussagt

Der Schild zeigt auch, was bei der letzten Ausführung geschehen ist, sodass Sie einen abgeschlossenen Ablauf nachvollziehen und sehen können, wo er angehalten hat:

| Schild | Bedeutung |
| --- | --- |
| Einfacher Schild | Der Schritt ist bedingt. Er wurde entweder noch nicht ausgeführt oder läuft gerade. |
| Schild mit **+** | Der Schritt wurde bei der letzten Ausführung ausgeführt. |
| Schild mit **−** | Der Schritt wurde bei der letzten Ausführung nicht ausgeführt. |

Die drei Varianten unterscheiden sich durch ihre Form, nicht durch die Farbe, und der QuickInfo-Text des Schilds beschreibt den Zustand in Worten. Er wird während der Ausführung eines Workflows live aktualisiert, sodass Sie die Arbeitsfläche nicht neu laden müssen, um zu beobachten, wie eine Ausführung ein Gate erreicht.

:::caution
Ein Schild mit **−** sagt Ihnen, dass der Schritt nicht ausgeführt wurde. Er sagt nicht, *warum*, und Sie sollten ihn nicht so lesen, dass „die Bedingung ihn blockiert hat“. Ein Schritt wird auch als nicht ausgeführt erfasst, wenn er deaktiviert ist, wenn seine Gruppe deaktiviert ist, wenn ein vorgelagerter Schritt fehlgeschlagen ist oder wenn er außerhalb des Umfangs einer Teilausführung lag. Mit **Protokolle anzeigen** in der Symbolleiste öffnen Sie das [Ausführungsprotokoll](/de/guides/workflows/viewing-workflow-log/), das den Grund für jeden übersprungenen Schritt nennt. Ein an einem Haltepunkt angehaltener Schritt ist der einzige Fall, der bewusst ausgenommen ist – er behält den einfachen Schild, weil das Anhalten dort Ihre Entscheidung war und kein Ergebnis der Ausführung.
:::


## Bedingungen verwalten

Im Abschnitt **Bedingungsprüfungen** können Sie beliebig viele Bedingungen hinzufügen. Beim Hinzufügen empfiehlt es sich, ihnen einen aussagekräftigen Namen zu geben, damit Sie die Bedingungen später leicht wiederfinden.

Sobald Sie eine Bedingung hinzugefügt haben, wählen Sie sie links aus, und die Auswertungskriterien der Bedingung lassen sich rechts bearbeiten.

Um eine Bedingung umzubenennen, wählen Sie sie aus und bearbeiten das Feld **Name** oben im Konfigurationsbereich rechts – oder doppelklicken Sie in der Liste auf die Bedingung. Sie können auch mit der rechten Maustaste auf eine Bedingung klicken, um **Umbenennen** und **Löschen** zu wählen; **Löschen** ist außerdem über die Schaltfläche „−“ über der Liste verfügbar.

Eine Bedingung ohne ausgewählten Bedingungstyp – etwa eine aus einem älteren oder importierten Workflow übernommene – kann nicht ausgewertet werden. Sie gilt als nicht erfüllt, sodass der Schritt übersprungen wird, und die Meldung des Schritts besagt, dass die Bedingung nicht angibt, was geprüft werden soll. Öffnen Sie die Bedingung und wählen Sie, was sie prüfen soll.


## Variablenbedingungen

Beim Prüfen von Variablenbedingungen muss der Abschnitt **Value Check Parameters** ausgefüllt werden, damit ein Vergleich möglich ist.

Tragen Sie unter **Variable or Table Field** den Variablennamen ein. Wählen Sie einen Vergleichstyp aus und geben Sie einen Vergleichswert ein.


## Einfache Tabellenbedingungen

Wenn die Bedingung prüft, ob eine Tabelle Zeilen enthält oder leer ist, müssen Sie außerdem auf der Registerkarte **Tabellendatenauswahl** die Tabelle festlegen.


## Bedingungen für das Vorhandensein einer Tabelle

Eine Bedingung für das Vorhandensein einer Tabelle führt den Schritt nur aus, wenn die Tabelle im Warehouse erstellt wurde, oder nur, wenn sie nicht erstellt wurde. Sie liest nie die Zeilen der Tabelle, und eine Tabelle, die mit null Zeilen geschrieben wurde, ist vorhanden. Ein Tabellenname, der keiner Tabelle im Projekt entspricht, gilt als fehlend. Verwenden Sie sie, um eine Tabelle beim ersten Lauf aufzubauen und danach unangetastet zu lassen, oder um einen Schritt zu überspringen, der eine Tabelle liest, die ein früherer Schritt möglicherweise nicht erstellt hat.

Die beiden Prüftypen sind `radio_table_exists` und `radio_table_not_exists`. Wählen Sie die Tabelle genauso aus wie bei einer einfachen Tabellenbedingung. Legen Sie die Bedingung mit einem KI-Assistenten oder über die REST-API fest; die Registerkarte **Bedingungsprüfungen** führt sie noch nicht auf.

## Erweiterte Tabellenbedingungen

Bei erweiterten Tabellenbedingungen muss der Abschnitt **Value Check Parameters** ausgefüllt werden, damit ein Vergleich möglich ist.

Tragen Sie unter **Variable or Table Field** den Feldnamen aus der Tabellenauswahl ein. Wählen Sie einen Vergleichstyp aus und geben Sie einen Vergleichswert ein.

Wählen Sie auf der Registerkarte **Tabellendatenauswahl** die Tabelle aus und füllen Sie den Abschnitt für die Datenzuordnung aus, mindestens mit dem Feld, auf das sich der Bedingungsvergleich bezieht.

## Dokumentpfad-Bedingungen

Wenn die Bedingung prüft, ob eine Datei vorhanden ist, müssen Sie das Dokumentenkonto auswählen und auf der Registerkarte **Dokumentpfad** den zu prüfenden Dokumentpfad angeben. Ein Ordner unter diesem Pfad gilt als fehlend, weil die Prüfung einer Datei gilt.

## Datums- und Zeitbedingungen

Für Datums- oder Zeitauswahlen können Sie mehrere Bedingungen hinzufügen, wenn eine Kombination von Bedingungen erforderlich ist. Wenn ein Schritt beispielsweise nur montags um 2:05 Uhr ausgeführt werden soll, würden Sie drei Bedingungen erstellen:
 - Bedingung für den Wochentag auf Montag (1) gesetzt
 - Stunde des Tages auf 2 gesetzt
 - Minute der Stunde auf 5 gesetzt

### Zeitzonenversatz

Jede Datums- und Zeitbedingung hat einen eigenen **Zeitzonenversatz**, aufgeführt als ganzstündiger Versatz, benannt nach einer repräsentativen Zone – zum Beispiel *Eastern Time (US & Canada) (UTC -5)* oder *Asia/Tokyo (UTC +9)*. Die von Ihnen eingegebenen Zeiten werden mit der Uhr in dieser Zone verglichen.

Eine neue Bedingung startet mit dem Versatz, den Ihr Browser meldet, sodass Sie ihn in den meisten Fällen unverändert lassen können. Legen Sie ihn gezielt fest, wenn der Zeitplan zu einem anderen Ort gehört als dem, an dem Sie sich befinden – etwa ein Abschluss, der nach der Uhr des Finanzteams läuft. Es sind nur ganze Stunden verfügbar, sodass eine Zone mit halber Stunde wie Indien (UTC +5:30) auf die nächste volle Stunde gerundet werden muss.

Eine Bedingung, die vor Inkrafttreten dieser Einstellung gespeichert wurde, wird weiterhin gegen UTC ausgewertet, bis Sie eine Zone für sie auswählen. Bestehende Bedingungen verhalten sich also genau wie bisher.

:::caution
Bedingungen für den **Wochentag** vergleichen derzeit unabhängig vom gewählten Versatz mit UTC. Wenn eine Wochentagsbedingung in einer Zone weit von UTC auf einen bestimmten Tag fallen soll, beachten Sie, dass sie rund um Mitternacht mehrere Stunden lang von Ihrem lokalen Tag abweichen kann.
:::

### Finanzabschluss Workday

Bei **Use Financial Close Workday** beginnt die Zählung bei **0 für den 1. des Monats** – wie der Hinweis neben dem Feld besagt. Ein Abschluss, der am 5. Tag des Monats stattfindet, ist also `4`, nicht `5`.

:::caution
Diese Bedingung trifft derzeit nie zu, sodass ein durch sie geschützter Schritt nicht ausgeführt wird. Verwenden Sie bis zur Behebung eine Bedingung **Day of the month**. Auch negative Werte, die vom Monatsende zurückzählen sollen, funktionieren nicht.
:::

## Bedingungen mit einem KI-Assistenten festlegen

Ein mit Ihrem Workspace verbundener KI-Assistent kann die Bedingungen eines Schritts für Sie hinzufügen und ändern, unabhängig davon, ob er den Schritt erstellt oder einen bestehenden bearbeitet. Ihm stehen alle zuvor beschriebenen Bedingungstypen zur Verfügung, mit Ausnahme von **Finanzabschluss Workday prüfen**: Ein Assistent kann diese schreiben, sie trifft aber nie zu, daher warnt der Assistent Sie, statt sie unbemerkt durchgehen zu lassen. Legen Sie diese selbst auf der Registerkarte **Bedingungen** fest.

Drei Dinge funktionieren anders als beim manuellen Bearbeiten von Bedingungen:

- **Die gesamte Liste wird jedes Mal ersetzt.** Bitten Sie darum, eine Bedingung hinzuzufügen oder zu ändern, sendet der Assistent die vollständige Liste, sodass jede Bedingung, die er auslässt, entfernt wird. Wenn Sie nicht sicher sind, dass er alle hat, bitten Sie ihn, vor dem Schreiben die aktuellen Bedingungen des Schritts aufzulisten.
- **Eine Bedingung, die nicht ausgewertet werden kann, wird abgelehnt.** Eine Bedingung, die nicht angibt, was sie prüft, wird abgewiesen statt gespeichert, und der Schritt behält die Bedingungen, die er bereits hatte. Korrigieren Sie die Anfrage und fragen Sie erneut.
- **Eine unvollständige Bedingung wird mit einer Warnung gespeichert.** Eine Bedingung, der der Vergleichswert fehlt, oder Bedingungen, die hinzugefügt wurden, ohne dass **Bedingungen vor der Ausführung prüfen** aktiviert ist, werden gespeichert und als Warnung zurückgemeldet. Öffnen Sie die Registerkarte **Bedingungen** und vervollständigen Sie sie, sonst verhält sich der Schritt nicht wie von Ihnen gewünscht.

Ein Assistent kann außerdem die Sperre des Schritts, seine Sichtbarkeit in den Ansichten Manager und Explorer, seine Wiederholungseinstellungen und den Schritt festlegen, zu dem bei einem Fehler gewechselt wird.
