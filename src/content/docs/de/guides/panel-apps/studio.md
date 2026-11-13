---
title: Panel Studio
description: Panel-Apps erstellen, bearbeiten, in der Vorschau ansehen und veröffentlichen, ohne PlaidCloud zu verlassen – anschließend eine frühere Version wiederherstellen, Nutzung und Geschwindigkeit der App einsehen, Warnungen und Zusammenfassungen einrichten, sie in der Galerie aufnehmen und an die Startseite anheften.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio ist der Editor für Panel-Apps in PlaidCloud. Er zeigt die Dateien der App neben einem Editor, erstellt eine private Vorschau, die Sie öffnen können, und veröffentlicht die App, wenn Sie bereit sind. Sie benötigen zum Einstieg kein Git-Repository.

## Panel Studio öffnen

- Wählen Sie auf der **Startseite**-Tafel eines Projekts bei einer Panel-App **In Studio öffnen**.
- Wählen Sie in **Meine Panel-Apps** in der Zeile einer App **Studio**.

Um eine neue App zu starten, wählen Sie **Neue Studio-App**. Das ist die erste Schaltfläche in der Symbolleiste von **Meine Panel-Apps**, und sie befindet sich im Feld **Panel-Apps** auf der Registerkarte **Startseite** eines Projekts. Um auf einer Tabelle aufzubauen, wählen Sie sie auf der Registerkarte **Tabellen** des Projekts aus und wählen Sie **Panel-App erstellen**.

## Eine App erstellen

Der Dialog **Neue Studio-App** bietet Ihnen fünf Ausgangspunkte:

| Starten mit | Sie erhalten |
|---|---|
| **Leere App** | Eine minimale App mit einer `app.py` und einer `requirements.txt`. |
| **Aus einer Tabelle** | Eine App, die auf der gewählten Tabelle aufbaut. |
| **Aus einer Ansicht** | Dasselbe, aufgebaut auf einer Projektansicht. |
| **Aus einer anderen Studio-App** | Eine Kopie einer Ihrer Studio-Apps. |
| **Aus der Galerie** | Eine Kopie einer App, die Ihr Workspace in der [App-Galerie](/de/guides/panel-apps/gallery/) aufgenommen hat. |

Benennen Sie die App, wählen Sie ihr **Projekt** und wählen Sie **Erstellen**. Studio öffnet die neue App mit ihren Dateien links in der Liste. Bei einer Tabelle oder einer Ansicht steht der Prompt von Weave zum Erstellen der ersten Seite der App zum Senden bereit. Siehe [Eine Panel-App erstellen](/de/guides/panel-apps/creating/).

## Wo Ihre App liegt

Eine Studio-App ist ein nach der App benannter Ordner (`<app-slug>/`) im Repository `apps` Ihres Workspace in [PlaidCloud Git](/de/guides/git/), demselben Repository, in dem Ihre anderen Panel-Apps liegen. Studio erstellt für die App kein eigenes Repository, sodass Sie ihren Quellcode in `apps` neben Ihren anderen Apps finden und bearbeiten können.

- **Entwurfs-Branch.** Arbeit, die noch nicht live ist, wird in einem Branch namens `studio-<app-slug>` gehalten. **Veröffentlichen** kopiert den Ordner der App aus diesem Branch in den Haupt-Branch.
- **Neuaufbau.** Ein Push in `apps` baut eine App nur dann neu auf, wenn sich der Ordner dieser App oder die `requirements.txt` im Stammverzeichnis des Repositorys geändert hat.
- **Vorhandene Apps.** Eine Studio-App, die in einem eigenen Repository lag, wird automatisch in ihren Ordner verschoben. Das alte Repository wird archiviert: Es bleibt schreibgeschützt erhalten und wird nie gelöscht.

## Bearbeiten

Wählen Sie eine Datei in der Liste, um sie im Editor zu bearbeiten. Führen Sie Ihre Python-Abhängigkeiten in `requirements.txt` auf, ein Paket pro Zeile. Sie werden installiert, wenn die App erstellt wird.

Wählen Sie **Weave fragen**, damit Weave die App für Sie schreibt oder ändert. Siehe [Panel-Apps mit Weave erstellen](/de/guides/panel-apps/build-with-weave/).

## Speichern, Vorschau und Veröffentlichen

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Speichern behält einen Entwurf, den nur Sie sehen. Die Vorschau erstellt eine private Kopie des Entwurfs für den Editor. Veröffentlichen ersetzt die Live-App, nachdem Sie bestätigt haben." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Speichern</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">nur Entwurf</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Vorschau</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">nur Editor</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Veröffentlichen</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">die Live-App</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Ihre Änderungen erreichen Betrachter erst, wenn Sie veröffentlichen.</figcaption>
</figure>

### Speichern

**Speichern** sichert Ihre Änderungen als Entwurf. Die Live-App ändert sich nicht, und niemand sonst sieht den Entwurf.

### Vorschau

**Vorschau** erstellt Ihren gespeicherten Entwurf als private Kopie und öffnet sie. Nur Bearbeiter der App können eine Vorschau öffnen.

- Eine Vorschau wird entfernt, wenn 24 Stunden lang nicht gespeichert wurde.
- Ein Workspace kann bis zu 10 Vorschauen gleichzeitig haben.
- Speichern Sie erneut und wählen Sie **Vorschau**, um Ihre neuesten Änderungen zu sehen.

### Veröffentlichen

**Veröffentlichen** ersetzt die Live-App durch Ihren gespeicherten Entwurf. Dafür ist die Bearbeitungsberechtigung für das Projekt der App erforderlich, und Studio bittet Sie zuvor um Bestätigung.

Wenn jemand anderes eine Änderung veröffentlicht hat, nachdem Sie die App geöffnet haben, meldet Studio einen Konflikt, statt dessen Arbeit zu überschreiben. Laden Sie die App neu, übernehmen Sie Ihre Änderungen und veröffentlichen Sie erneut.

## Build-Status und Fehler

Die Registerkarte **Erstellen** zeigt den Status des letzten Builds und wird während der Ausführung aktualisiert. Wenn ein Build fehlschlägt, listet die Registerkarte jeden Fehler mit seiner Datei und Zeilennummer auf, sodass Sie direkt zur Zeile springen können. Zu Abhängigkeitsproblemen in `requirements.txt` gibt es einen Hinweis zur Behebung.

Fehler und Warnungen werden außerdem im Editor in den betreffenden Zeilen markiert, sodass Sie ein Problem dort sehen, wo es auftritt.

Was die einzelnen Status nach der Veröffentlichung der App bedeuten, erfahren Sie unter [Eine Panel-App verwenden](/de/guides/panel-apps/using/#build-status-server-apps).

## Verlauf und Wiederherstellen

Die Registerkarte **Verlauf** listet jede veröffentlichte Version der App auf, die neueste zuerst, mit ihrem Build-Status. Wählen Sie **Mehr laden**, um ältere zu sehen.

Um zu einer früheren Version zurückzukehren, wählen Sie bei ihr **Wiederherstellen** und bestätigen Sie. Die wiederhergestellte Version wird zur Live-App und wird neu erstellt. Ihr nicht gespeicherter Entwurf geht nicht verloren: Er bleibt im Entwurf und geht beim nächsten Veröffentlichen auf der wiederhergestellten Version live. Wenn die App bereits dieser Version entspricht, teilt Studio dies mit und ändert nichts. Wenn jemand veröffentlicht hat, während Sie wiederhergestellt haben, stellt Studio nichts wieder her und bittet Sie, es **Erneut versuchen**.

## Erkenntnisse

Die Registerkarte **Erkenntnisse** zeigt, wie Benutzer die App verwenden und wie schnell sie antwortet. Wählen Sie die letzten 7, 14 oder 30 Tage.

| Abschnitt | Zeigt |
|---|---|
| **Aufrufe pro Tag** | Wie oft die App an jedem Tag geöffnet wurde. |
| **Seitenladezeit** | Die mittlere Ladezeit und die Zeit, die 95 Prozent der Ladevorgänge unterbieten, aus den Seitenladevorgängen des Zeitraums. |
| **Langsamste Abfragen** | Die Abfragen mit der längsten Dauer, mit ihrer Ausführungshäufigkeit sowie ihrer mittleren, langsamen und langsamsten Zeit. |
| **Fehler** | Was im Zeitraum schiefgelaufen ist, nach Fehlerart und danach, wo in der App es aufgetreten ist. |

Wenn ein Zeitraum mehr Aktivität enthält, als Erkenntnisse lesen kann, weist die Ansicht darauf hin, dass die Zahlen unvollständig sind. Wenn Seitenladevorgänge das [Leistungsbudget](/de/guides/panel-apps/app-kit/#leistungsbudgets) der App überschreiten, warnt Erkenntnisse Sie, wie viele es waren und welche Abfragen langsam waren. Erkenntnisse zeigt nie die Daten, die eine Abfrage zurückgegeben hat, oder die Namen der Personen, die die App geöffnet haben.

Die Registerkarten **Verlauf** und **Erkenntnisse** setzen voraus, dass die App einem Projekt zugeordnet ist; bei einer nicht zugeordneten App erscheint eine Aufforderung zur Zuordnung.

## Warnungen und Zusammenfassungen

Wählen Sie **Warnungen & Zusammenfassungen**, um Benachrichtigungen einzurichten, die eine Zahl in den Daten der App überwachen und Sie informieren, wenn sie einen Grenzwert überschreitet, oder die nach einem Zeitplan eine Zusammenfassung senden. Siehe [Warnungen und Zusammenfassungen](/de/guides/panel-apps/alerts-and-digests/).

## Eine App in der Galerie aufnehmen

Wählen Sie in Studio **Galerie…**. Wählen Sie **In Galerie aufnehmen**, um die App als Vorlage aufzunehmen, aus der jeder, der ihr Projekt ansehen kann, eine eigene App erstellen kann, oder **Aus der Galerie entfernen**, um sie zu entfernen. Die Schaltfläche steht für Apps zur Verfügung, die zu einem Projekt gehören. Sie benötigen Bearbeitungszugriff auf das Projekt. Siehe [Die App-Galerie](/de/guides/panel-apps/gallery/).

## An Startseite anheften

Wählen Sie **An Startseite anheften**, um die App zur **Startseite**-Tafel des Projekts hinzuzufügen, und **Von Startseite lösen**, um sie zu entfernen.

## Eine App löschen

Beim Löschen einer Panel-App werden Sie zuerst um Bestätigung gebeten. Verwenden Sie in **Meine Panel-Apps** das **Minus**-Symbol in der Zeile der App. Auch das Aufheben der Veröffentlichung erfordert eine Bestätigung.

## Nächste Schritte

- [Panel-Apps mit Weave erstellen](/de/guides/panel-apps/build-with-weave/) – die App beschreiben und die genaue Änderung genehmigen.
- [Das Panel App Kit](/de/guides/panel-apps/app-kit/) – die Komponenten, die die Tabellen- und Ansichts-Starts von Studio verwenden.
- [Warnungen und Zusammenfassungen](/de/guides/panel-apps/alerts-and-digests/) – Personen benachrichtigen, wenn eine Zahl einen Grenzwert überschreitet, oder nach einem Zeitplan.
- [Die App-Galerie](/de/guides/panel-apps/gallery/) – eine App als Ausgangspunkt für andere teilen.
- [Eine Panel-App verwenden](/de/guides/panel-apps/using/) – Protokolle, Nutzung und Neuaufbauten nach dem Veröffentlichen.
