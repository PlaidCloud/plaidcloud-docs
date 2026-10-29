---
title: Panel Studio
description: Erstellen, bearbeiten, prüfen in der Vorschau und veröffentlichen Sie Panel-Apps, ohne PlaidCloud zu verlassen – stellen Sie dann eine frühere Version wieder her, lesen Sie Nutzung und Geschwindigkeit der App, richten Sie Hinweise und Zusammenfassungen ein, listen Sie sie in der Galerie auf und heften Sie sie an die Startseite.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio ist der Editor für Panel-Apps innerhalb von PlaidCloud. Er zeigt die Dateien der App neben einem Editor, erstellt eine private Vorschau, die Sie öffnen können, und veröffentlicht die App, wenn Sie bereit sind. Sie benötigen zum Einstieg kein Git-Repository.

## Panel Studio öffnen

- Wählen Sie auf dem Board **Startseite** eines Projekts bei einer Panel-App **Open in Studio**.
- Wählen Sie unter **Meine Panel-Apps** in der Zeile einer App **Open in Studio**.

Um eine neue App zu beginnen, wählen Sie an beiden Stellen **Create app**.

## Eine App erstellen

Der Dialog **Create app** lässt Sie an einem von fünf Ausgangspunkten beginnen:

| Starten mit | Sie erhalten |
|---|---|
| **Leer** | Eine minimale App mit einer `app.py` und einer `requirements.txt`. |
| **Tabelle** | Eine App, die auf der ausgewählten Tabelle aufbaut. |
| **Ansicht** | Dasselbe, aufgebaut auf einer Projektansicht. |
| **Vorlage** | Eine fertige App aus dem [Panel App Kit](/de/guides/panel-apps/app-kit/#mit-einer-vorlage-beginnen). |
| **Aus der Galerie** | Eine Kopie einer App, die Ihr Workspace in der [App-Galerie](/de/guides/panel-apps/gallery/) aufgelistet hat. |

Benennen Sie die App, wählen Sie ihr **Projekt** und wählen Sie **Erstellen**. Studio öffnet die neue App mit ihren Dateien links in der Liste.

## Bearbeiten

Wählen Sie eine Datei in der Liste, um sie im Editor zu bearbeiten. Führen Sie Ihre Python-Abhängigkeiten in `requirements.txt` auf, ein Paket pro Zeile. Sie werden installiert, wenn die App erstellt wird.

Wählen Sie **Ask Weave**, damit Weave die App für Sie schreibt oder ändert. Siehe [Panel-Apps mit Weave erstellen](/de/guides/panel-apps/build-with-weave/).

## Speichern, Vorschau und Veröffentlichen

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Speichern legt einen Entwurf ab, den nur Sie sehen. Die Vorschau erstellt eine private Kopie des Entwurfs für den Editor. Veröffentlichen ersetzt die Live-App, nachdem Sie bestätigt haben." style="width:100%;max-width:660px;height:auto;">
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
- Ein Workspace kann gleichzeitig bis zu 10 Vorschauen haben.
- Speichern Sie erneut und wählen Sie **Vorschau**, um Ihre neuesten Änderungen zu sehen.

### Veröffentlichen

**Veröffentlichen** ersetzt die Live-App durch Ihren gespeicherten Entwurf. Dafür ist die Bearbeitungsberechtigung für das Projekt der App erforderlich, und Studio bittet Sie zuvor um Bestätigung.

Wenn jemand anderes eine Änderung veröffentlicht hat, nachdem Sie die App geöffnet haben, meldet Studio einen Konflikt, statt dessen Arbeit zu überschreiben. Laden Sie die App neu, übernehmen Sie Ihre Änderungen und veröffentlichen Sie erneut.

## Build-Status und Fehler

Die Registerkarte **Erstellen** zeigt den Status des letzten Builds und aktualisiert sich während der Ausführung. Wenn ein Build fehlschlägt, listet die Registerkarte jeden Fehler mit Datei und Zeilennummer auf, sodass Sie direkt zur Zeile springen können. Zu Abhängigkeitsproblemen in `requirements.txt` gibt es einen Hinweis zur Behebung.

Fehler und Warnungen werden außerdem in ihren Zeilen im Editor markiert, sodass Sie ein Problem dort sehen, wo es auftritt.

Was die einzelnen Status nach dem Veröffentlichen der App bedeuten, erfahren Sie unter [Eine Panel-App verwenden](/de/guides/panel-apps/using/#build-status-server-apps).

## Verlauf und Wiederherstellen

Die Registerkarte **Verlauf** listet jede veröffentlichte Version der App auf, die neueste zuerst, mit ihrem Build-Status. Wählen Sie **Mehr laden**, um ältere zu sehen.

Um zu einer früheren Version zurückzukehren, wählen Sie bei ihr **Wiederherstellen** und bestätigen Sie. Die wiederhergestellte Version wird zur Live-App und wird neu erstellt. Ihr nicht gespeicherter Entwurf geht nicht verloren: Er bleibt im Entwurf und geht beim nächsten Veröffentlichen auf der wiederhergestellten Version live. Wenn die App bereits dieser Version entspricht, teilt Studio dies mit und ändert nichts. Wenn jemand veröffentlicht hat, während Sie wiederhergestellt haben, stellt Studio nichts wieder her und bittet Sie, es erneut zu versuchen.

## Einblicke

Die Registerkarte **Einblicke** zeigt, wie Personen die App nutzen und wie schnell sie antwortet. Wählen Sie die letzten 7, 14 oder 30 Tage.

| Abschnitt | Zeigt |
|---|---|
| **Aufrufe pro Tag** | Wie oft die App an jedem Tag geöffnet wurde. |
| **Seitenladezeit** | Die mittlere Ladezeit und die Zeit, die 95 Prozent der Ladevorgänge unterbieten, aus den Seitenaufrufen des Zeitraums. |
| **Langsamste Abfragen** | Die Abfragen, die am längsten gedauert haben, mit Häufigkeit ihrer Ausführung sowie ihrer mittleren, langsamen und langsamsten Zeit. |
| **Fehler** | Was im Zeitraum schiefgelaufen ist, nach Art des Fehlers und Ort in der App. |

Enthält ein Zeitraum mehr Aktivität, als Einblicke lesen kann, wird mitgeteilt, dass die Werte unvollständig sind. Überschreiten Seitenladezeiten das [Leistungsbudget](/de/guides/panel-apps/app-kit/#leistungsbudgets) der App, warnt Einblicke, wie viele es waren und welche Abfragen langsam waren. Einblicke zeigt nie die Daten, die eine Abfrage zurückgegeben hat, oder die Namen der Personen, die die App geöffnet haben.

Beide Registerkarten setzen voraus, dass die App einem Projekt zugewiesen ist; bei einer nicht zugewiesenen App erscheint eine Aufforderung zur Zuweisung.

## Hinweise und Zusammenfassungen

Wählen Sie **Alerts & Digests**, um Benachrichtigungen einzurichten, die eine Zahl in den Daten der App überwachen und Sie informieren, wenn sie einen Grenzwert überschreitet, oder die nach Zeitplan eine Zusammenfassung senden. Siehe [Hinweise und Zusammenfassungen](/de/guides/panel-apps/alerts-and-digests/).

## Eine App in der Galerie auflisten

Wählen Sie **Gallery…**, um die App als Vorlage aufzulisten, aus der jeder, der ihr Projekt ansehen kann, eine eigene App erstellen kann, oder um sie aus der Galerie zu nehmen. Siehe [Die App-Galerie](/de/guides/panel-apps/gallery/).

## An die Startseite heften

Wählen Sie **Pin to Home**, um die App dem Board **Startseite** des Projekts hinzuzufügen, und **Unpin from Home**, um sie zu entfernen.

## Eine App löschen

Beim Löschen einer Panel-App werden Sie zunächst um Bestätigung gebeten. Verwenden Sie unter **Meine Panel-Apps** das Symbol **Minus** in der Zeile der App. Auch das Aufheben der Veröffentlichung erfordert eine Bestätigung.

## Nächste Schritte

- [Panel-Apps mit Weave erstellen](/de/guides/panel-apps/build-with-weave/) – beschreiben Sie die App und genehmigen Sie die genaue Änderung.
- [Das Panel App Kit](/de/guides/panel-apps/app-kit/) – die Komponenten, die die Starts aus Tabelle, Ansicht und Vorlage in Studio verwenden.
- [Hinweise und Zusammenfassungen](/de/guides/panel-apps/alerts-and-digests/) – benachrichtigen Sie Personen, wenn eine Zahl einen Grenzwert überschreitet, oder nach Zeitplan.
- [Die App-Galerie](/de/guides/panel-apps/gallery/) – geben Sie eine App als Ausgangspunkt für andere frei.
- [Eine Panel-App verwenden](/de/guides/panel-apps/using/) – Protokolle, Nutzung und Neuaufbauten nach dem Veröffentlichen.
