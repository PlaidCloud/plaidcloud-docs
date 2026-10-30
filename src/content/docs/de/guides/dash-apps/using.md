---
title: Eine Dash-App verwenden
description: Verfolgen Sie den Build-Status veröffentlichter Plotly-Dash-Apps und öffnen, erstellen neu, sperren, protokollieren, bearbeiten und entfernen Sie sie im Bildschirm „Meine Panel-Apps“ in PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/using.md
---

Dash-Apps erscheinen im selben Bildschirm **Meine Panel-Apps** wie Ihre WASM- und Server-Panel-Apps, mit **Dash** in der Spalte **Laufzeit** und einem eigenen Symbol, damit sie leicht zu unterscheiden sind. Alles auf dieser Seite entspricht [Eine Panel-App verwenden](/de/guides/panel-apps/using/) für eine Server-App, mit einer unten erläuterten Ausnahme: Dash-Apps haben noch keine **Usage Metrics**.

## Build-Status

Die Spalte **Status** einer Dash-App verfolgt ihren Build, und die Liste aktualisiert sich selbstständig, solange ein Build läuft:

- **Wird erstellt…** – PlaidCloud erstellt aus Ihrem Repository einen Container. Die App hat noch keine URL.
- **Bereit** – der Build war erfolgreich. Die URL der App ist aktiv, und in ihrer Zeile erscheint das Symbol **Öffnen**.
- **Fehlgeschlagen** – der Build wurde nicht abgeschlossen. Prüfen Sie Einstiegspunkt und Branch und bearbeiten Sie die App, um sie erneut zu veröffentlichen.

## Eine Dash-App neu erstellen

Klicken Sie in der Zeile einer Dash-App auf das Symbol **Neu erstellen**, um sie ohne Änderung ihrer Einstellungen neu zu erstellen und erneut bereitzustellen. Der Status der App wechselt zu **Wird erstellt…**, während PlaidCloud denselben Branch und Einstiegspunkt erneut erstellt, und danach zurück zu **Bereit**, sobald der neue Build live ist.

Verwenden Sie **Neu erstellen** nach Änderungen an Abhängigkeiten, Aktualisierungen des Basisimages oder einem vorübergehend fehlgeschlagenen Build. Auch das Bearbeiten und Speichern einer Dash-App erstellt sie neu, ein Neuerstellen erfordert aber nicht, dass Sie das Bearbeitungsformular öffnen.

## Eine App sperren

Klicken Sie in der Zeile einer App auf das **Sperren**-Symbol, um sie vor versehentlichen Änderungen zu schützen. Solange eine Dash-App gesperrt ist:

- Verweigern **Bearbeiten**, **Entfernen** und **Neu erstellen** die Ausführung und melden, dass die App gesperrt ist.
- **Ein Push auf den Branch der App erstellt sie nicht neu** – die automatische Neuerstellung wird übersprungen, bis Sie die App entsperren. Pushen Sie nach dem Entsperren erneut (oder verwenden Sie **Neu erstellen**), um die Änderung zu übernehmen.
- Das Öffnen der App und das Anzeigen ihrer Protokolle funktionieren weiterhin – die Sperre verhindert nur Änderungen, nie die Betrachter.

Klicken Sie erneut auf das Symbol, um die Sperre aufzuheben. Das Symbol zeigt den aktuellen Zustand der App: geschlossen, wenn gesperrt, geöffnet, wenn nicht. Die Sperre schützt vor Versehen und ist keine Sicherheitskontrolle – jeder, der Dash-Apps bearbeiten kann, kann sie auch entsperren.

## Eine Dash-App öffnen

Klicken Sie auf das Symbol **Öffnen** am Anfang der Zeile einer bereiten App, um sie in einem neuen Tab unter `https://<your-tenant-host>/serve/<slug>/` zu starten. Das Symbol erscheint erst, wenn die App **Bereit** ist.

Eine Dash-App skaliert bei Leerlauf auf null, um Ressourcen zu sparen, sodass das erste Öffnen nach einer Leerlaufphase sie erst hochfahren muss. Währenddessen sehen Sie statt eines leeren Tabs einen **PlaidCloud-Ladebildschirm**, und die App erscheint von selbst, sobald sie bereit ist. Kann eine App nicht starten, wird aus dem Ladebildschirm die Meldung **„This app didn't start“** mit der Schaltfläche **Erneut versuchen**; tritt das wiederholt auf, bearbeiten Sie die App, prüfen Sie Einstiegspunkt und Branch und veröffentlichen Sie sie erneut.

> **Ein `dcc.Interval` (oder jedes andere dauerhafte Polling) verhindert Scale-to-Zero, solange sein Tab geöffnet bleibt.** Scale-to-Zero setzt voraus, dass die App ruhig wird – keine laufenden Anfragen –, sobald sie niemand aktiv nutzt. Eine Komponente, die in einem Takt ständig Anfragen sendet, etwa `dcc.Interval`, hält die App wach, solange dieser Tab geöffnet ist, auch wenn die Person davor sich entfernt hat. Wenn eine App zwischen den Besuchen herunterskalieren soll, vermeiden Sie dauerhaftes Polling oder stoppen Sie das Intervall, nachdem die Seite eine Weile im Leerlauf war.

## Protokolle anzeigen

Klicken Sie in der Zeile einer Dash-App auf das Symbol **Protokolle anzeigen**, um die Protokollansicht zu öffnen – mit denselben Registerkarten **Laufzeit** und **Erstellen**, denselben Filtern, demselben Zeitbereich und demselben Detailbereich wie bei einer Server-Panel-App; die vollständige Funktionsweise steht unter [Protokolle anzeigen](/de/guides/panel-apps/using/#protokolle-anzeigen-server-apps). Jede Laufzeit-Protokollzeile ist mit dem **Benutzer** gekennzeichnet, dessen Sitzung sie erzeugt hat, genau wie bei einer Server-Panel-App.

**Usage Metrics sind für Dash-Apps in dieser Version nicht verfügbar** – das Symbol **Usage Metrics**, das in der Zeile einer Server-Panel-App erscheint, wird für Dash-Apps nicht angezeigt, es gibt also noch keine Aufschlüsselung nach eindeutigen Benutzern und Sitzungen.

## Eine App bearbeiten

Klicken Sie in der Zeile einer Dash-App auf das **Stift**-Symbol, um sie zu bearbeiten. Sie können Name, Slug, Branch, Einstiegspunkt, CPU, Arbeitsspeicher, Leerlauffenster, öffentliches Kennzeichen, Domains für eingebettete Bereitstellung und Notiz ändern. Die **Git-Verbindung** steht fest, sobald die App erstellt ist, und wird schreibgeschützt angezeigt. Ein Feld **Design** zum Bearbeiten gibt es nicht – diese Einstellung ist Panel-spezifisch. Das Speichern erstellt die App neu – ihr Status wechselt zu **Wird erstellt…**, bis der neue Build bereit ist.

## Eine App entfernen

Klicken Sie in der Zeile einer Dash-App auf das **Minus**-Symbol und bestätigen Sie. Das Entfernen baut ihren Build und ihre Bereitstellung ab, und die URL der App funktioniert sofort nicht mehr.
