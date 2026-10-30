---
title: Panel Studio
description: Erstellen, bearbeiten, in der Vorschau ansehen und veröffentlichen Sie Panel-Apps, ohne PlaidCloud zu verlassen – stellen Sie dann eine frühere Version wieder her, lesen Sie Nutzung und Geschwindigkeit der App, richten Sie Warnungen und Digests ein, führen Sie sie in der Galerie auf und heften Sie sie an die Startseite.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio ist der Editor für Panel-Apps in PlaidCloud. Er zeigt die Dateien der App neben einem Editor, erstellt eine private Vorschau, die Sie öffnen können, und veröffentlicht die App, wenn Sie bereit sind. Zum Einstieg benötigen Sie kein Git-Repository.

## Panel Studio öffnen

- Wählen Sie auf der **Startseite**-Übersicht eines Projekts bei einer Panel-App **In Studio öffnen**.
- Wählen Sie in **Meine Panel-Apps** in der Zeile einer App **In Studio öffnen**.

Um eine neue App zu beginnen, wählen Sie **Neue Studio-App**. Das ist die erste Schaltfläche in der Symbolleiste von **Meine Panel-Apps** und befindet sich im Feld **Panel-Apps** auf der Registerkarte **Startseite** eines Projekts. Um auf einer Tabelle aufzubauen, wählen Sie sie auf der Registerkarte **Tabellen** des Projekts aus und wählen Sie **Panel-App erstellen**.

## Eine App erstellen

Das Dialogfeld **Neue Studio-App** lässt Sie an einem von fünf Orten beginnen:

| Starten mit | Sie erhalten |
|---|---|
| **Leere App** | Eine minimale App mit einer `app.py` und einer `requirements.txt`. |
| **Aus einer Tabelle** | Eine App auf Basis der gewählten Tabelle. |
| **Aus einer Ansicht** | Dasselbe, auf Basis einer Projektansicht. |
| **Aus einer anderen Studio-App** | Eine Kopie einer Ihrer Studio-Apps. |
| **Aus der Galerie** | Eine Kopie einer App, die Ihr Workspace in der [App-Galerie](/de/guides/panel-apps/gallery/) aufgeführt hat. |

Benennen Sie die App, wählen Sie ihr **Projekt** und wählen Sie **Erstellen**. Studio öffnet die neue App mit ihren Dateien links in der Liste. Bei einer Tabelle oder Ansicht ist Weaves Aufforderung, die erste Seite der App zu erstellen, versandbereit. Siehe [Eine Panel-App erstellen](/de/guides/panel-apps/creating/).

## Bearbeiten

Wählen Sie eine Datei in der Liste aus, um sie im Editor zu bearbeiten. Führen Sie Ihre Python-Abhängigkeiten in `requirements.txt` auf, ein Paket pro Zeile. Sie werden installiert, wenn die App erstellt wird.

Wählen Sie **Weave fragen**, damit Weave die App für Sie schreibt oder ändert. Siehe [Panel-Apps mit Weave erstellen](/de/guides/panel-apps/build-with-weave/).

## Speichern, Vorschau und Veröffentlichen

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Speichern behält einen Entwurf, den nur Sie sehen. Die Vorschau erstellt eine private Kopie des Entwurfs für den Editor. Veröffentlichen ersetzt nach Ihrer Bestätigung die Live-App." style="width:100%;max-width:660px;height:auto;">
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

**Speichern** legt Ihre Änderungen als Entwurf ab. Die Live-App ändert sich nicht, und niemand sonst sieht den Entwurf.

### Vorschau

**Vorschau** erstellt Ihren gespeicherten Entwurf als private Kopie und öffnet sie. Nur Bearbeiter der App können eine Vorschau öffnen.

- Eine Vorschau wird nach 24 Stunden ohne Speichern entfernt.
- Ein Workspace kann bis zu 10 Vorschauen gleichzeitig haben.
- Speichern Sie erneut und wählen Sie **Vorschau**, um Ihre neuesten Änderungen zu sehen.

### Veröffentlichen

**Veröffentlichen** ersetzt die Live-App durch Ihren gespeicherten Entwurf. Dafür ist die Bearbeitungsberechtigung für das Projekt der App erforderlich, und Studio bittet zuvor um Bestätigung.

Hat jemand anderes eine Änderung veröffentlicht, nachdem Sie die App geöffnet haben, meldet Studio einen Konflikt, statt dessen Arbeit zu überschreiben. Laden Sie die App neu, übernehmen Sie Ihre Änderungen und veröffentlichen Sie erneut.

## Build-Status und Fehler

Die Registerkarte **Erstellen** zeigt den Status des letzten Builds und aktualisiert sich währenddessen. Schlägt ein Build fehl, listet die Registerkarte jeden Fehler mit Datei und Zeilennummer auf, sodass Sie direkt zur Zeile springen können. Zu Abhängigkeitsproblemen in `requirements.txt` gibt es einen Hinweis zur Behebung.

Fehler und Warnungen sind außerdem in ihren Zeilen im Editor markiert, sodass Sie ein Problem dort sehen, wo es auftritt.

Was die einzelnen Status nach dem Veröffentlichen der App bedeuten, lesen Sie unter [Eine Panel-App verwenden](/de/guides/panel-apps/using/#build-status-server-apps).

## Verlauf und Wiederherstellen

Die Registerkarte **Verlauf** listet jede veröffentlichte Version der App auf, die neueste zuerst, mit ihrem Build-Status. Wählen Sie **Mehr laden**, um ältere zu sehen.

Um zu einer früheren Version zurückzukehren, wählen Sie bei ihr **Wiederherstellen** und bestätigen Sie. Die wiederhergestellte Version wird zur Live-App und wird neu erstellt. Ihr nicht gespeicherter Entwurf geht nicht verloren: Er bleibt im Entwurf und geht beim nächsten Veröffentlichen auf der wiederhergestellten Version live. Entspricht die App bereits dieser Version, teilt Studio das mit und ändert nichts. Hat jemand veröffentlicht, während Sie wiederhergestellt haben, stellt Studio nichts wieder her und bittet Sie, es erneut zu versuchen.

## Einblicke

Die Registerkarte **Einblicke** zeigt, wie Personen die App nutzen und wie schnell sie antwortet. Wählen Sie die letzten 7, 14 oder 30 Tage.

| Abschnitt | Zeigt |
|---|---|
| **Aufrufe pro Tag** | Wie oft die App an jedem Tag geöffnet wurde. |
| **Seitenladezeit** | Die mittlere Ladezeit und die Zeit, die 95 Prozent der Ladevorgänge unterbieten, aus den Seitenaufrufen des Zeitraums. |
| **Langsamste Abfragen** | Die Abfragen, die am längsten gedauert haben, mit der Häufigkeit ihrer Ausführung sowie ihren mittleren, langsamen und langsamsten Zeiten. |
| **Fehler** | Was im Zeitraum schiefgelaufen ist, nach Art des Fehlers und Stelle in der App, an der er auftrat. |

Enthält ein Zeitraum mehr Aktivität, als Einblicke lesen kann, weist die Registerkarte darauf hin, dass die Zahlen unvollständig sind. Überschreiten Seitenaufrufe das [Leistungsbudget](/de/guides/panel-apps/app-kit/#leistungsbudgets) der App, warnt Einblicke Sie, wie viele es waren und welche Abfragen langsam waren. Einblicke zeigt nie die Daten, die eine Abfrage zurückgegeben hat, oder die Namen der Personen, die die App geöffnet haben.

Beide Registerkarten setzen voraus, dass die App einem Projekt zugeordnet ist; bei einer nicht zugeordneten App erscheint eine Aufforderung zur Zuordnung.

## Warnungen und Digests

Wählen Sie **Warnungen & Zusammenfassungen**, um Benachrichtigungen einzurichten, die eine Zahl in den Daten der App beobachten und Sie informieren, wenn sie eine Grenze überschreitet, oder die nach einem Zeitplan eine Zusammenfassung senden. Siehe [Warnungen und Digests](/de/guides/panel-apps/alerts-and-digests/).

## Eine App in der Galerie aufführen

Wählen Sie in Studio **Galerie…**. Wählen Sie **In Galerie aufnehmen**, um die App als Vorlage aufzuführen, aus der jeder, der ihr Projekt ansehen kann, eine eigene App erstellen kann, oder **Aus der Galerie entfernen**, um sie zu entfernen. Die Schaltfläche ist für Apps verfügbar, die zu einem Projekt gehören. Sie benötigen Bearbeitungszugriff auf das Projekt. Siehe [Die App-Galerie](/de/guides/panel-apps/gallery/).

## An die Startseite heften

Wählen Sie **An Startseite anheften**, um die App an die **Startseite**-Übersicht des Projekts zu heften, und **Von Startseite lösen**, um sie zu entfernen.

## Eine App löschen

Das Löschen einer Panel-App verlangt zuvor eine Bestätigung. Verwenden Sie in **Meine Panel-Apps** das **Minus**-Symbol in der Zeile der App. Auch das Aufheben der Veröffentlichung verlangt eine Bestätigung.

## Nächste Schritte

- [Panel-Apps mit Weave erstellen](/de/guides/panel-apps/build-with-weave/) – beschreiben Sie die App und genehmigen Sie die genaue Änderung.
- [Das Panel-App-Kit](/de/guides/panel-apps/app-kit/) – die Komponenten, die die Tabellen- und Ansichtsvorlagen von Studio verwenden.
- [Warnungen und Digests](/de/guides/panel-apps/alerts-and-digests/) – benachrichtigen Sie Personen, wenn eine Zahl eine Grenze überschreitet, oder nach einem Zeitplan.
- [Die App-Galerie](/de/guides/panel-apps/gallery/) – teilen Sie eine App als Ausgangspunkt für andere.
- [Eine Panel-App verwenden](/de/guides/panel-apps/using/) – Protokolle, Nutzung und Neuaufbauten nach dem Veröffentlichen.
