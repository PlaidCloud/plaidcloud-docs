---
title: Ein Projekt archivieren
description: Archivieren Sie PlaidCloud-Projekte, um abgeschlossene Arbeit zu sichern, Ressourcen im Workspace freizugeben und eine übersichtliche Projektumgebung zu erhalten.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/archive-a-project.md
---

## Ein Archiv erstellen


Projekte enthalten in der Regel kritische Prozesse und Logik, die archiviert werden sollten. Wenn Sie ein Projekt jemals auf einen bestimmten Stand zurücksetzen müssen, sind Archive unverzichtbar. 



PlaidCloud ermöglicht es Ihnen, Projekte zu jedem beliebigen Zeitpunkt zu archivieren. Archive ergänzen die integrierte Nachverfolgung von PlaidCloud, indem sie bestimmte Zeitpunkte festhalten. Das ist besonders nützlich vor einer größeren Änderung oder um den exakten Zustand einer Produktionsumgebung dauerhaft zu dokumentieren.



**Vollständige Sicherung**: Sie umfasst alle Datentabellen eines Projekts. Das Archiv kann je nach Datenmenge im Projekt recht groß werden.


**Teilweise Sicherung:** Sie eignet sich, wenn sich alle Projektdaten aus anderen Quellen ableiten lassen. In diesem Fall müssen die Daten im Projekt nicht archiviert werden, da sie an anderer Stelle erhalten bleiben. Teilweise Archive sparen beim Erstellen Zeit und Speicherplatz.



So archivieren Sie ein Projekt:


1. Öffnen Sie Analyze.
2. Wählen Sie die Registerkarte „Projekte“.
3. Wählen Sie das Projekt aus und wählen Sie dann im Menü **Aktionen** die Option **Projektarchiv exportieren** (oder klicken Sie mit der rechten Maustaste auf das Projekt und wählen Sie **Projektarchiv exportieren**).

Das Fenster nennt in seiner Titelleiste das Projekt, das archiviert wird, sodass Sie vor dem Start prüfen können, ob es das richtige ist.

### Während das Archiv erstellt wird

Das Exportfenster schließt sich, sobald PlaidCloud die Anfrage angenommen hat, und ein Fortschrittsfenster begleitet das Archivieren von da an. Sie können dieses Fortschrittsfenster geöffnet lassen, um den Vorgang zu verfolgen, oder es in den Hintergrund schicken und weiterarbeiten – das Archiv wird in beiden Fällen auf der Plattform erstellt, und das Schließen des Fortschrittsfensters bricht es nicht ab.

Eine Benachrichtigung teilt Ihnen mit, wie der Vorgang geendet hat: dass das Archiv geschrieben wurde, welche Tabellen ohne ihre Daten aufgenommen wurden oder, falls er fehlgeschlagen ist, warum. Dafür müssen Sie das Fenster nicht geöffnet lassen.

:::note
Das Archivieren eines großen Projekts kann je nach Umfang der enthaltenen Tabellendaten zwischen wenigen Sekunden und einer Stunde dauern. Ein lange laufendes Archiv ist normal und bedeutet nicht, dass etwas schiefgegangen ist – warten Sie auf die Benachrichtigung, statt einen zweiten Export zu starten, der das Projekt noch einmal von Grund auf archivieren würde.
:::

### Tabellen, deren Daten nicht aufgenommen werden können

Gelegentlich hat eine in einem Projekt aufgeführte Tabelle keine Daten mehr – zum Beispiel eine Tabelle, die nie erstellt wurde oder deren Daten außerhalb des Projekts entfernt wurden. Das Archiv wird dennoch geschrieben: Diese Tabellen werden bei den Tabellendaten ausgelassen, und der Export endet mit einer Meldung, die sie nennt. Alles andere – die Projektkonfiguration, Workflows, Tabellendefinitionen und die Daten aller übrigen Tabellen – wird wie gewohnt archiviert.

Das Archiv hält fest, welche Tabellen ohne ihre Daten aufgenommen wurden, und beim Wiederherstellen werden sie am Ende noch einmal genannt, statt als vollständig dargestellt zu werden. Eine Tabelle, deren Definition noch lesbar war, kommt mit ihren Spalten und ohne Zeilen zurück; eine, deren Definition ebenfalls fehlte, kommt als Eintrag ohne zugehörige Tabelle zurück. Führen Sie den Workflow, der eine Tabelle erstellt, erneut aus, um sie zu füllen.

:::note
Ein geplantes Archiv hält übersprungene Tabellen im Systemprotokoll fest, statt Ihnen eine Meldung anzuzeigen, da nichts auf dem Bildschirm vorhanden ist, wo sie angezeigt werden könnte. Prüfen Sie die Exportmeldung, wenn es darauf ankommt, welche Tabellen enthalten waren.
:::

### Wenn Sie die Tabellen des Projekts nicht lesen können

Das Lesen der Tabellen eines Projekts ist eine andere Berechtigung als das Lesen des Projekts selbst, und ein Archiv hängt von beiden ab. Wenn Sie ein Projekt öffnen können, aber keinen Lesezugriff auf Tabellen haben, wird das Archiv trotzdem geschrieben – es enthält dann lediglich keine Tabellendaten und auch keine Tabellendefinitionen, da beides hinter derselben Berechtigung liegt. Der Export endet mit einer Meldung, die die ausgelassenen Tabellen nennt, und zwar anhand ihrer internen IDs statt ihrer Namen, weil die Namen aus den Definitionen stammen, die das Archiv nicht enthalten hat.

Ein auf diese Weise erstelltes Archiv ist eine Kopie der Konfiguration des Projekts – seiner Workflows, Variablen, Dimensionen, Ansichten und Layouts, soweit Sie jeweils zum Lesen berechtigt sind – und nicht seiner Daten. **Beim Wiederherstellen werden überhaupt keine Tabellen angelegt**; es ist also keine Sicherung, aus der Sie die Daten des Projekts neu aufbauen können. Prüfen Sie die Exportmeldung, bevor Sie sich auf ein solches Archiv verlassen.

Anders als bei den oben beschriebenen Tabellen lässt sich dies nicht dadurch beheben, dass Sie einen Workflow erneut ausführen – die Daten wurden von vornherein nie gelesen. Bitten Sie einen Workspace-Administrator, Ihnen Lesezugriff auf die Tabellen des Projekts zu gewähren, und erstellen Sie das Archiv dann erneut.

:::caution
Das gilt auch für geplante Archive, die als ein bestimmtes Mitglied ausgeführt werden. Hat dieses Mitglied keinen Lesezugriff auf Tabellen, enthält jedes vom Zeitplan erzeugte Archiv nur die Konfiguration, und das Defizit wird im Systemprotokoll festgehalten, statt jemandem angezeigt zu werden. Wenn Sie geplante Archive als Sicherungen aufbewahren, stellen Sie sicher, dass das Mitglied, als das sie ausgeführt werden, die Tabellen des Projekts lesen kann.
:::

### Wenn das Projekt Zeilenzugriff verwendet

Beim Erstellen eines Archivs werden die Tabellen des Projekts gelesen, daher gilt der [Zeilenzugriff](/de/administration/access/managing-security-groups-and-assignments/#zeilenzugriff-verwalten) hier wie bei jedem anderen Lesevorgang. Bei jeder steuernden Spalte enthält das Archiv die Zeilen, die Ihren Gruppen gewährt sind. Haben Sie für eine Spalte keine Berechtigung, hängt das Ergebnis davon ab, wie die Spalte deklariert wurde: Eine Spalte, die standardmäßig verweigert, liefert Ihnen überhaupt keine Zeilen, eine Spalte, die standardmäßig alles erlaubt, bleibt ungefiltert. Eine Tabelle ohne steuernde Spalten wird vollständig archiviert, und ein Architect des Projekts archiviert unabhängig von den Berechtigungen jede Zeile. Ein geplantes Archiv wird unter der eigenen Identität des Projekts statt unter Ihrer ausgeführt und archiviert daher jede Zeile.

Ein Archiv, das ein Mitglied mit nur einem Teil der Berechtigungen erstellt hat, ist eine teilweise Kopie der Projektdaten, und eine Spalte, die standardmäßig verweigert, bedeutet, dass eine Tabelle leer statt nur eingeschränkt zurückkommen kann. Beim Wiederherstellen eines solchen Archivs wird das Projekt ohne diese Zeilen neu aufgebaut, und nichts in der Wiederherstellung weist darauf hin, denn aus Sicht des Archivs waren die Zeilen nie vorhanden.

:::caution
Wenn Sie ein Archiv benötigen, aus dem sich das gesamte Projekt neu aufbauen lässt, erstellen Sie es als Mitglied, das das Projekt vollständig lesen kann.
:::

### Wenn der Export fehlschlägt

Ein fehlgeschlagener Export meldet den Fehler nun. Früher konnte ein Archiv als abgeschlossen gemeldet werden, obwohl es nicht geschrieben worden war, sodass Sie die fehlende Datei erst später bemerkten – meist erst beim Wiederherstellen. Ein fehlgeschlagener Export sagt das jetzt, daher können Sie einen gemeldeten Erfolg als echten Erfolg behandeln und bei allem, was einen Fehler meldet, die Meldung prüfen. Dasselbe gilt für die anderen Exporttypen, nicht nur für Projektarchive.

## Ein Archiv wiederherstellen


Wenn Sie ein Archiv haben, möchten Sie es möglicherweise wiederherstellen. Sie können ein Archiv in ein neues oder in ein vorhandenes Projekt wiederherstellen.



So stellen Sie ein Archiv wieder her:


1. Öffnen Sie Analyze.
2. Wählen Sie die Registerkarte „Projekte“.
3. Wählen Sie im Menü **Aktionen** (oder in der Symbolleiste) die Option **Projektarchiv importieren** und wählen Sie das wiederherzustellende Archiv aus.
4. Wählen Sie, ob Sie **Neues Projekt erstellen** oder **In vorhandenes Projekt importieren** möchten, und legen Sie in der Auswahlstruktur fest, was übernommen werden soll.
5. Klicken Sie auf **Projekt importieren**.

Der Import läuft im Hintergrund. Ein Fortschrittsfenster zeigt, wie weit er ist, und eine Meldung teilt Ihnen mit, wann er abgeschlossen ist, bei ausgelassenen Inhalten zusätzlich per E-Mail. Kann der Import nicht gestartet werden – etwa weil das gewählte Projekt gesperrt ist –, bleibt das Fenster geöffnet und nennt Ihnen den Grund.


Ein Archiv wird beim Öffnen geprüft. Enthält es Inhalte, die ein Projektarchiv nie enthält – etwa eine Datei, die außerhalb des archiveigenen Ordners landen würde, einen Link, der nach außerhalb verweist, oder Einstellungen, die etwas anderes als reine Daten anzulegen versuchen –, wird es abgelehnt, bevor etwas daraus wiederhergestellt wird.


Sie müssen nicht das gesamte Archiv übernehmen. Die Auswahlstruktur listet nach Typ auf, was das Archiv enthält – Workflows, Schritte, Tabellen, Dimensionen, Dateneditoren, benutzerdefinierte Funktionen –, und alles, was Sie markieren, bringt seine Abhängigkeiten mit.


### Wenn ein Teil eines Archivs nicht importiert wird


Ein Import läuft weiter, wenn ein Teil des Archivs nicht wiederhergestellt werden kann. Solange das Archiv gelesen und das Projekt selbst eingerichtet werden kann, wird das Projekt importiert, und alles, was nicht wiederhergestellt werden konnte, wird in seinem Importergebnis aufgeführt. Kann das Archiv nicht gelesen oder das Projekt selbst nicht eingerichtet werden, schlägt der Import fehl und nennt den Grund, und ein neues Projekt wird entfernt. Ein Import in ein vorhandenes Projekt kann auch vor dem Abschluss abbrechen. Alles, was bereits wiederhergestellt wurde, bleibt im Projekt. Die Meldung und die E-Mail teilen mit, dass der Import abgebrochen wurde, und das Importergebnis nennt, wann und warum, und listet auf, was bis dahin nicht wiederhergestellt werden konnte.

Wurde etwas ausgelassen, weisen die Meldung und die E-Mail am Ende des Imports darauf hin, und die Meldung verlinkt auf das Fenster **Importergebnis**. Das Fenster nennt jedes Element mit Typ und Namen, gibt den Grund an und gruppiert die Elemente unter diesen Überschriften:

- **Nicht importiert** – Das Element ist nicht im Projekt.
- **Ohne Daten erstellt** – Die Tabelle, Ansicht oder Dimension ist im Projekt, enthält aber keine Daten, weil ihre Daten nicht gelesen oder geladen werden konnten.
- **Warnungen** – Das Element wurde importiert, aber es gibt etwas zu prüfen, etwa Spalten, die das Warehouse in die Spaltentypen der Tabelle umgewandelt hat.
- **Variablen, die den Wert dieses Projekts behalten haben** – Das Projekt hatte bereits eine Variable mit diesem Namen und hat daher seinen eigenen Wert behalten.

Die schwerwiegendsten Elemente stehen zuerst, und das Fenster weist darauf hin, wenn es mehr gibt, als es auflistet. Um das Fenster später erneut zu öffnen, wählen Sie das Projekt auf der Registerkarte **Projekte** aus und wählen Sie im Menü **Aktionen** die Option **Import- oder Kopierergebnis anzeigen**, oder klicken Sie mit der rechten Maustaste auf das Projekt.

Das Ergebnis bleibt am Projekt, bis jemand es verwirft oder ein späterer Import in dasselbe Projekt es ersetzt. Klicken Sie auf **Ergebnis verwerfen**, um es für alle zu entfernen, die das Projekt öffnen können; im Projekt ändert sich dadurch nichts. Zum Verwerfen ist Bearbeitungszugriff auf das Projekt erforderlich, und das Projekt darf nicht gesperrt sein.


### In ein vorhandenes Projekt importieren


Der Import in ein bereits vorhandenes Projekt ergänzt es, statt es zu ersetzen. Zwei Dinge entscheiden, was geschieht, wenn Archiv und Projekt dasselbe Element enthalten.


**Sie müssen das Zielprojekt ändern dürfen.** Ein Import in ein Projekt, in dem Sie keine Rolle haben, wird abgelehnt, ebenso ein Import in ein Projekt, das gegen Änderungen gesperrt wurde – dies wird geprüft, bevor etwas gelesen oder geschrieben wird, sodass ein abgelehnter Import das Projekt unberührt lässt.


**Das Projekt behält seine eigenen Einstellungen.** Name, Kennung, Umgebung der Datenverbindung, Speicherstandards, Dokumentenkonto, Zugriffstyp, Zugriffslisten und Zeilenzugriffsberechtigungen bleiben unverändert. Nur die ausgewählten Inhalte werden übernommen.

Ein Schritt, der auf **Projektstandard** festgelegt ist, übernimmt diese Einstellung, kein Konto – nach der Wiederherstellung wird sie zu dem Standard aufgelöst, den das Projekt hat, nicht zu dem, den es beim Archivieren hatte.


### Doppelte Elemente


Ist ein eingehendes Element dasselbe Element wie eines, das bereits im Projekt vorhanden ist, legen Sie fest, was damit geschieht:


- **Doppelte Elemente mit eingehenden Daten überschreiben** – Die Version aus dem Archiv ersetzt die im Projekt.
- **Neue Kopie doppelter Elemente erstellen** – Das Projekt behält, was es hat, und das eingehende Element wird daneben hinzugefügt, wobei seinem Namen ` copy` angehängt wird (und ein Zähler, falls auch dieser Name vergeben ist). Das gilt für Workflows, Schritte, Tabellen, Dimensionen, Dateneditoren, Ansichten und benutzerdefinierte Funktionen.


**Projekt- und Workflow-Variablen sind die Ausnahme.** Eine Variable wird anhand ihres Namens identifiziert, daher gibt es keine Möglichkeit, eine zweite Kopie hinzuzufügen, ohne sie in etwas umzubenennen, auf das sich nichts bezieht. Definiert das Projekt bereits eine Variable, die auch das Archiv enthält, bleibt der eigene Wert des Projekts erhalten, und das Importergebnis listet die Variablen auf, die unangetastet blieben. Wenn Sie den Wert aus dem Archiv möchten, legen Sie ihn anschließend an der Variablen fest.


Eines sollten Sie wissen: Der Abgleich erfolgt anhand der Identität, nicht anhand des Namens. Ein Element, das ursprünglich aus demselben Projekt stammt – alles, woraus das Archiv exportiert wurde, oder eine Kopie davon –, wird als dasselbe Element erkannt. Zwei Elemente, die nur zufällig denselben Namen tragen, werden als verschiedene Elemente behandelt, und beide sind nach dem Import vorhanden.

### Wenn eine Tabelle ohne ihre Daten zurückkommt


Das Wiederherstellen der Daten einer Tabelle setzt voraus, dass ihre Spalten zur Zieltabelle passen – dieselben Namen in derselben Reihenfolge, weil sich ein Ladevorgang danach richtet. Passen sie nicht zusammen, werden die Daten dieser Tabelle ausgelassen, und die Tabelle wird im Importergebnis unter **Ohne Daten erstellt** aufgeführt, genauso wie eine Tabelle, deren Daten nicht im Archiv waren. Ein Unterschied allein im gespeicherten Typ einer Spalte hält die Daten nicht zurück: Die Daten werden geladen, und die Tabelle wird unter **Warnungen** mit den Spalten aufgeführt, die das Warehouse umgewandelt hat.


Ein Import, bei dem alle Tabellen ihre Daten nicht laden konnten, behält das Projekt dennoch. Seine abschließende Meldung besagt, dass keine der Tabellendaten geladen werden konnten, und das Importergebnis ebenso. Wenn ein Import abgeschlossen ist und jeder Workflow, jede Tabelle und jede Dimension vorhanden ist, lesen Sie die abschließende Meldung, bevor Sie davon ausgehen, dass die Zeilen mitgekommen sind.


## Archivierungszeitplan


Archive können auch als regelmäßige Sicherung Ihres Projekts dienen. PlaidCloud ermöglicht es Ihnen, den Sicherungszeitplan zu verwalten und die Aufbewahrungsdauer der Sicherungsarchive so festzulegen, wie es am praktischsten oder gewünscht ist.


Da alle Änderungen an einem Projekt automatisch nachverfolgt werden, ist das Archivieren für ein Zurücksetzen nicht erforderlich. Es liefert jedoch bestimmte Momentaufnahmen des Projektzustands, was zu Kontrollzwecken und/oder für die Möglichkeit, einen bekannten Stand wiederherzustellen, oft nützlich ist.



So legen Sie einen Archivierungszeitplan fest:


1. Öffnen Sie Analyze.
2. Wählen Sie die Registerkarte „Projekte“.
3. Klicken Sie auf das Sicherungssymbol.
4. Wählen Sie ein Zielverzeichnis in einem **Dokument**-Konto.
5. Wählen Sie die Sicherungshäufigkeit und die Aufbewahrung.
6. Wählen Sie, welche Elemente gesichert werden sollen.
7. Klicken Sie auf „Aktualisieren“.
