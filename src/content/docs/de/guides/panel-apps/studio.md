---
title: Panel Studio
description: Erstellen, bearbeiten, prüfen und veröffentlichen Sie Panel-Apps, ohne PlaidCloud zu verlassen – und stellen Sie bei Bedarf eine frühere Version wieder her, lesen Sie Nutzung und Geschwindigkeit der App ab, richten Sie Warnungen und Zusammenfassungen ein, nehmen Sie die App in die Galerie auf und heften Sie sie an die Startseite an.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio ist der Editor für Panel-Apps in PlaidCloud. Er zeigt die Dateien der App neben einem Editor, erstellt eine private Vorschau, die Sie öffnen können, und veröffentlicht die App, wenn Sie so weit sind. Sie benötigen kein Git-Repository, um loszulegen.

## Panel Studio öffnen

- Wählen Sie auf der **Startseite** eines Projekts bei einer Panel-App **In Studio öffnen**.
- Wählen Sie unter **Apps** in der Zeile einer App **Studio**.

Um eine neue App zu starten, wählen Sie **Neue App** > **Studio**. Die Option finden Sie auch in der Zeile **Studio-Apps** der Karte **Apps & Branding** auf der Registerkarte **Startseite** eines Projekts. Um eine App auf Basis einer Tabelle zu erstellen, wählen Sie die Tabelle auf der Registerkarte **Tabellen** des Projekts aus und wählen Sie **Panel-App erstellen**.

## App erstellen

Im Dialogfeld **Neue Studio-App** können Sie von fünf Ausgangspunkten starten:

| Starten mit | Ergebnis |
|---|---|
| **Leere App** | Eine minimale App mit einer `app.py` und einer `requirements.txt`. |
| **Aus einer Tabelle** | Eine App, die auf der gewählten Tabelle aufbaut. |
| **Aus einer Ansicht** | Dasselbe, aufgebaut auf einer Projektansicht. |
| **Aus einer anderen Studio-App** | Eine Kopie einer Ihrer Studio-Apps. |
| **Aus der Galerie** | Eine Kopie einer App, die Ihr Workspace in der [App-Galerie](/de/guides/panel-apps/gallery/) aufgenommen hat. |

Benennen Sie die App, wählen Sie ihr **Projekt** und wählen Sie **Erstellen**. Studio öffnet die neue App, wobei links ihre Dateien aufgelistet sind. Bei einer Tabelle oder einer Ansicht ist der Weave-Prompt zum Erstellen der ersten Seite der App versandbereit. Siehe [Panel-App erstellen](/de/guides/panel-apps/creating/).

## Wo Ihre App gespeichert ist

Eine Studio-App ist ein Ordner, der nach der App benannt ist (`<app-slug>/`), im Repository `apps` Ihres Workspace in [PlaidCloud Git](/de/guides/git/) – demselben Repository, in dem auch Ihre anderen Panel-Apps liegen. Studio legt für die App kein eigenes Repository an, sodass Sie ihren Quellcode in `apps` neben Ihren anderen Apps finden und bearbeiten können.

- **Entwurfs-Branch.** Arbeit, die noch nicht live ist, wird in einem Branch namens `studio-<app-slug>` aufbewahrt. **Veröffentlichen** kopiert den Ordner der App aus diesem Branch in den Haupt-Branch.
- **Neu-Builds.** Ein Push nach `apps` erstellt eine App nur dann neu, wenn sich der Ordner dieser App oder die `requirements.txt` im Stammverzeichnis des Repositorys geändert hat.
- **Bestehende Apps.** Eine Studio-App, die in einem eigenen Repository lag, wird automatisch in ihren Ordner verschoben. Das alte Repository wird archiviert: Es bleibt schreibgeschützt erhalten und wird nie gelöscht.

## Bearbeiten

Wählen Sie eine Datei in der Liste aus, um sie im Editor zu bearbeiten. Führen Sie Ihre Python-Abhängigkeiten in der `requirements.txt` auf, ein Paket pro Zeile. Sie werden installiert, wenn die App erstellt wird.

Wählen Sie **Weave fragen**, damit Weave die App für Sie schreibt oder ändert. Siehe [Panel-Apps mit Weave erstellen](/de/guides/panel-apps/build-with-weave/).

## Speichern, Vorschau und Veröffentlichen

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Beim Speichern entsteht ein Entwurf, den nur Sie sehen. Die Vorschau erstellt eine private Kopie des Entwurfs für den Editor. Das Veröffentlichen ersetzt nach Ihrer Bestätigung die Live-App." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Speichern</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">nur Entwurf</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Vorschau</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">nur für Editoren</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Veröffentlichen</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">die Live-App</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Ihre Änderungen erreichen die Betrachter erst, wenn Sie veröffentlichen.</figcaption>
</figure>

### Speichern

**Speichern** sichert Ihre Änderungen als Entwurf. Die Live-App ändert sich nicht, und niemand sonst sieht den Entwurf.

### Vorschau

**Vorschau** erstellt Ihren gespeicherten Entwurf als private Kopie und öffnet sie. Nur Editoren der App können eine Vorschau öffnen.

- Eine Vorschau wird entfernt, wenn 24 Stunden lang nicht gespeichert wurde.
- Ein Workspace kann bis zu 10 Vorschauen gleichzeitig haben.
- Speichern Sie erneut und wählen Sie **Vorschau**, um Ihre neuesten Änderungen zu sehen.

### Veröffentlichen

**Veröffentlichen** ersetzt die Live-App durch Ihren gespeicherten Entwurf. Dafür ist die Bearbeitungsberechtigung für das Projekt der App erforderlich, und Studio bittet Sie zuvor um Bestätigung.

Hat jemand anderes eine Änderung veröffentlicht, nachdem Sie die App geöffnet haben, meldet Studio einen Konflikt, anstatt dessen Arbeit zu überschreiben. Laden Sie die App neu, übernehmen Sie Ihre Änderungen und veröffentlichen Sie erneut.

## Build-Status und Fehler

Die Registerkarte **Erstellen** zeigt den Status des letzten Builds und aktualisiert sich während der Ausführung. Schlägt ein Build fehl, listet die Registerkarte jeden Fehler mit Datei und Zeilennummer auf, sodass Sie direkt zur Zeile springen können. Zu Abhängigkeitsproblemen in der `requirements.txt` erhalten Sie einen Hinweis zur Behebung.

Fehler und Warnungen sind außerdem im Editor in ihren Zeilen markiert, sodass Sie ein Problem dort sehen, wo es auftritt.

Was die einzelnen Status nach der Veröffentlichung der App bedeuten, lesen Sie unter [Panel-App verwenden](/de/guides/panel-apps/using/#build-status-server-apps).

## Verlauf und Wiederherstellen

Die Registerkarte **Verlauf** listet jede veröffentlichte Version der App auf, die neueste zuerst, jeweils mit ihrem Build-Status. Wählen Sie **Mehr laden**, um ältere Versionen anzuzeigen.

Um zu einer früheren Version zurückzukehren, wählen Sie bei ihr **Wiederherstellen** und bestätigen Sie. Die wiederhergestellte Version wird zur Live-App und wird neu erstellt. Ihr nicht gespeicherter Entwurf geht nicht verloren: Er bleibt im Entwurf und geht bei der nächsten Veröffentlichung auf der wiederhergestellten Version live. Entspricht die App bereits dieser Version, teilt Studio dies mit und ändert nichts. Hat jemand veröffentlicht, während Sie wiederhergestellt haben, stellt Studio nichts wieder her und bittet Sie, es erneut zu versuchen.

## Erkenntnisse

Die Registerkarte **Erkenntnisse** zeigt, wie Benutzer die App verwenden und wie schnell sie antwortet. Wählen Sie die letzten 7, 14 oder 30 Tage.

| Abschnitt | Zeigt |
|---|---|
| **Aufrufe pro Tag** | Wie oft die App an jedem Tag geöffnet wurde. |
| **Seitenladezeit** | Die mittlere Ladezeit und die Zeit, die 95 Prozent der Ladevorgänge unterschreiten, ermittelt aus den Seitenladevorgängen im Zeitraum. |
| **Langsamste Abfragen** | Die Abfragen mit der längsten Dauer, mit ihrer Ausführungshäufigkeit sowie ihrer mittleren, langsamen und langsamsten Zeit. |
| **Fehler** | Was im Zeitraum schiefgegangen ist, nach Art des Fehlers und nach Stelle in der App, an der er auftrat. |

Enthält ein Zeitraum mehr Aktivität, als Erkenntnisse auswerten kann, weist die Registerkarte darauf hin, dass die Zahlen unvollständig sind. Überschreiten Seitenladevorgänge das [Leistungsbudget](/de/guides/panel-apps/app-kit/#leistungsbudgets) der App, warnt Erkenntnisse Sie, wie viele es waren und welche Abfragen langsam waren. Erkenntnisse zeigt weder die Daten, die eine Abfrage zurückgegeben hat, noch die Namen der Personen, die die App geöffnet haben.

Die Registerkarten **Verlauf** und **Erkenntnisse** setzen voraus, dass die App einem Projekt zugewiesen ist; bei einer nicht zugewiesenen App erscheint eine Aufforderung zur Zuweisung.

## Warnungen und Zusammenfassungen

Wählen Sie **Alerts & Digests**, um Benachrichtigungen einzurichten, die eine Zahl in den Daten der App überwachen und Sie informieren, wenn sie einen Grenzwert überschreitet, oder die nach einem Zeitplan eine Zusammenfassung senden. Siehe [Warnungen und Zusammenfassungen](/de/guides/panel-apps/alerts-and-digests/).

## App in der Galerie aufnehmen

Wählen Sie in Studio **Galerie…**. Wählen Sie **In Galerie aufnehmen**, um die App als Vorlage aufzunehmen, aus der jeder, der ihr Projekt anzeigen darf, eine eigene App erstellen kann, oder **Aus der Galerie entfernen**, um sie wieder zu entfernen. Die Schaltfläche ist für Apps verfügbar, die zu einem Projekt gehören. Sie benötigen Bearbeitungszugriff auf das Projekt. Siehe [Die App-Galerie](/de/guides/panel-apps/gallery/).

## An Startseite anheften

Wählen Sie **An Startseite anheften**, um die App zur **Startseite** des Projekts hinzuzufügen, und **Von Startseite lösen**, um sie zu entfernen.

## App löschen

Beim Löschen einer Panel-App werden Sie zuvor um Bestätigung gebeten. Verwenden Sie unter **Apps** das **Minus**-Symbol in der Zeile der App. Auch das Aufheben der Veröffentlichung erfordert eine Bestätigung.

## Nächste Schritte

- [Panel-Apps mit Weave erstellen](/de/guides/panel-apps/build-with-weave/) – beschreiben Sie die App und genehmigen Sie die genaue Änderung.
- [Das Panel App Kit](/de/guides/panel-apps/app-kit/) – die Komponenten, die Studio bei Starts aus Tabellen und Ansichten verwendet.
- [Warnungen und Zusammenfassungen](/de/guides/panel-apps/alerts-and-digests/) – benachrichtigen Sie Personen, wenn eine Zahl einen Grenzwert überschreitet oder nach einem Zeitplan.
- [Die App-Galerie](/de/guides/panel-apps/gallery/) – geben Sie eine App als Ausgangspunkt für andere frei.
- [Panel-App verwenden](/de/guides/panel-apps/using/) – Protokolle, Nutzung und Neu-Builds nach der Veröffentlichung.
