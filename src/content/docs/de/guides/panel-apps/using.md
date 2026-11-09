---
title: Eine Panel-App verwenden
description: Verfolgen Sie den Build-Status veröffentlichter HoloViz-Panel-Apps, öffnen, erstellen Sie sie neu, sperren Sie sie, zeigen Sie ihre Protokolle und Nutzungskennzahlen an, bearbeiten und entfernen Sie sie auf dem Bildschirm Meine Panel-Apps in PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/using.md
---

Jede veröffentlichte App erscheint auf dem Bildschirm **Meine Panel-Apps** mit ihrer **Laufzeit**, ihrem **Status**, ihrem **Slug** und ihren Zeitstempeln. Die Spalte ganz links öffnet die App; mit den übrigen Zeilensymbolen sperren Sie die App gegen versehentliche Änderungen, bearbeiten oder entfernen sie und – bei Server-Apps – erstellen sie neu, zeigen ihre Protokolle an und rufen ihre Nutzungskennzahlen auf. Das Symbol zum Öffnen spiegelt die Laufzeit der App wider, sodass sich WASM- und Server-Apps auf einen Blick unterscheiden lassen.

## Build-Status (Server-Apps)

Die Spalte **Status** einer Server-App verfolgt ihren Build, und die Liste aktualisiert sich selbstständig, solange ein Build läuft:

- **Wird erstellt…** – PlaidCloud erstellt aus Ihrem Repository einen Container. Die App hat noch keine URL.
- **Bereit** – der Build war erfolgreich. Die URL der App ist aktiv, und das Symbol **Öffnen** erscheint in ihrer Zeile.
- **Fehlgeschlagen** – der Build wurde nicht abgeschlossen. Prüfen Sie den Einstiegspunkt und den Branch und bearbeiten Sie dann die App, um sie erneut zu veröffentlichen.

WASM-Apps haben keinen Build-Schritt und sind verfügbar, sobald sie veröffentlicht sind.

## Eine Server-App neu erstellen

Klicken Sie in der Zeile einer Server-App auf das Symbol **Neu erstellen**, um sie ohne Änderung ihrer Einstellungen neu zu erstellen und erneut bereitzustellen. Der Status der App wechselt zurück zu **Wird erstellt…**, während PlaidCloud denselben Branch und Einstiegspunkt erneut erstellt, und dann wieder zu **Bereit**, sobald der neue Build aktiv ist.

Verwenden Sie **Neu erstellen** nach Änderungen an Abhängigkeiten, Aktualisierungen des Basis-Images oder einem vorübergehend fehlgeschlagenen Build. Auch das Bearbeiten und Speichern einer Server-App erstellt sie neu, ein Neuerstellen erfordert aber nicht das Öffnen des Bearbeitungsformulars.

Bei einer [App Runner](/de/guides/workflows/use-converted-alteryx-apps/#die-app-aktuell-halten)-App – dem Eingabeformular, das für eine konvertierte Alteryx-App generiert wird – aktualisieren **Neu erstellen** und das Speichern einer Bearbeitung zuerst ihre generierten Dateien auf die aktuelle App-Runner-Version und erstellen sie dann. PlaidCloud tut dies auch für jede App-Runner-App, die nicht gesperrt ist, wenn PlaidCloud selbst aktualisiert wird; eine gesperrte App benötigt nach dem Entsperren ein **Neu erstellen**.

## Eine App sperren

Klicken Sie in der Zeile einer App auf das **Schloss**-Symbol, um sie vor versehentlichen Änderungen zu schützen. Solange eine App gesperrt ist:

- Lehnen **Bearbeiten**, **Entfernen** und **Neu erstellen** die Ausführung ab und teilen Ihnen mit, dass die App gesperrt ist.
- Löst ein **Push auf den Branch einer Server-App keinen Neubau aus** – der automatische Neubau wird übersprungen, bis Sie die App entsperren. Für einen übersprungenen Push läuft kein Build, daher erscheint nichts Neues in den Erstellungsprotokollen der App; pushen Sie nach dem Entsperren erneut (oder verwenden Sie **Neu erstellen**), um die Änderung zu übernehmen.
- Funktionieren das Öffnen der App, das Anzeigen ihrer Protokolle und das Anzeigen ihrer Nutzungskennzahlen weiterhin – die Sperre verhindert nur Änderungen, nie Betrachter.

Klicken Sie erneut auf das Symbol, um zu entsperren. Das Symbol zeigt den aktuellen Zustand der App: geschlossen, wenn sie gesperrt ist, geöffnet, wenn nicht.

Die Sperre schützt vor Versehen – einer irrtümlichen Bearbeitung, einem unbeabsichtigten Löschen oder einem Git-Push auf eine App, die Sie gerade vorführen – genau wie die Sperre bei Workflows und Workflow-Schritten. Sie ist **keine** Sicherheitskontrolle: Jeder, der Panel-Apps bearbeiten kann, kann sie auch entsperren.

> Zwei Dinge deckt die Sperre nicht ab: Ein **bereits laufender Build** wird auch dann fertiggestellt und geht live, wenn Sie währenddessen sperren, und die Dateien einer **WASM**-App liegen in ihrem Dokumentenkonto, sodass das Ersetzen dieser Dateien die laufende App ändert, ohne den gesperrten Datensatz zu berühren.

## Eine App öffnen

Klicken Sie am Anfang der Zeile einer bereiten App auf das Symbol **Öffnen**, um sie in einer neuen Registerkarte zu starten. **Öffnen** ist auch der erste Eintrag im Menü **⋯** der Zeile. Siehe [Das Zeilenaktionsmenü](/de/guides/dashboards/using-dashboards/#das-zeilenaktionsmenü).

- Eine Server-App wird unter `https://<your-tenant-host>/serve/<slug>/` bereitgestellt.
- Das Symbol **Öffnen** erscheint erst, wenn eine Server-App **Bereit** ist.

Eine Server-App skaliert im Leerlauf auf null, um Ressourcen zu sparen, daher muss das erste Öffnen nach einer Leerlaufzeit sie erst hochfahren. Währenddessen sehen Sie statt eines leeren Tabs einen **PlaidCloud-Ladebildschirm** – mit dem Namen Ihrer App, einer Fortschrittsanzeige und den Details Ihres Workspace. Die App erscheint von selbst, sobald sie bereit ist (meist nach wenigen Sekunden, bei einem Kaltstart bis zu etwa einer Minute), und reagiert dann normal, bis sie wieder in den Leerlauf geht.

> Wenn eine App nicht starten kann, wird der Ladebildschirm zu einer Meldung **„This app didn't start“** mit einer Schaltfläche **Erneut versuchen**, statt endlos zu drehen. Wenn das immer wieder passiert, bearbeiten Sie die App, prüfen Sie Einstiegspunkt und Branch und veröffentlichen Sie sie erneut, oder wenden Sie sich an Ihren PlaidCloud-Administrator.

### Erscheinungsbild

Server-Panel-Apps verwenden standardmäßig das moderne **FAST**-Design von PlaidCloud, mit der Einstellung **Design** der App können Sie jedoch auf das **Standard**-Styling von Panel zurückwechseln, wenn vorhandenes CSS davon abhängt. Das Theme – hell, dunkel oder ein Hell/Dunkel-Umschalter, den Betrachter bedienen können – legen Sie in der Vorlage Ihrer App fest. Die Muster dazu finden Sie unter [Das Theme festlegen](/de/guides/panel-apps/creating/#das-design-festlegen-hell-dunkel-oder-umschalter) im Leitfaden zum Erstellen. Wenn die Tabellen oder das benutzerdefinierte Styling Ihrer App für einen hellen Hintergrund gebaut sind, lassen Sie sie fest auf hell eingestellt.

## Protokolle anzeigen (Server-Apps)

Klicken Sie in der Zeile einer Server-App auf das Symbol **Protokolle anzeigen**, um ihren Protokollviewer zu öffnen. (WASM-Apps laufen vollständig im Browser und haben keine Serverprotokolle, daher erscheint das Symbol nur in den Zeilen von Server-Apps.)

Der Viewer hat zwei Registerkarten:

- **Laufzeit** (zuerst angezeigt) – die eigene Ausgabe der laufenden App: alles, was sie protokolliert, alles, was sie ausgibt, und alle nicht abgefangenen Fehler. Diese bleiben auch erhalten, nachdem die App auf null skaliert wurde, sodass Sie nachlesen können, was eine frühere Sitzung getan hat.
- **Erstellen** – die Ausgabe beim Erstellen des Containers der App. Damit sehen Sie, *warum* ein Build **Fehlgeschlagen** anzeigt – zum Beispiel eine Abhängigkeit, die sich nicht installieren ließ.

Jede Registerkarte bietet Ihnen Filter für **Info / Warnung / Fehler**, einen Zeitraum **Protokolle seit** (von der letzten Stunde bis zu 30 Tagen oder alle), eine Schaltfläche **Aktualisieren** und **Automatisch aktualisieren**, um neue Einträge abzufragen – praktisch, wenn Sie eine laufende App oder einen laufenden Build beobachten. Die neuesten Einträge stehen zuoberst.

> Wenn die Build-Ausgabe nicht erfasst werden konnte, zeigt die Registerkarte „Erstellen“ einen kurzen Hinweis mit der Begründung, statt leer zu erscheinen.

### Eine vollständige Protokollmeldung lesen

Die Protokolltabelle kürzt lange Zeilen, damit die Liste lesbar bleibt. Wählen Sie eine Protokollzeile aus, um neben der Tabelle einen **Detailbereich** zu öffnen, der die vollständige Meldung des Eintrags zeigt. So lesen Sie am einfachsten etwas, das für die Tabelle zu lang ist – eine lange Fehlermeldung oder einen vollständigen Stack-Trace –, ohne dass es abgeschnitten wird.

### Protokollzeilen kopieren

Sie können mehrere Protokollzeilen gleichzeitig auswählen und auf **Kopieren** klicken, um sie in die Zwischenablage zu legen. Das ist praktisch, um Protokolle beim Debuggen Ihrer App in einen Chat mit einem KI-Assistenten einzufügen oder in eine Nachricht an Ihr Team oder den PlaidCloud-Support.

### Wer eine Protokollzeile ausgelöst hat

Wenn Ihre App Betrachter anmeldet, wird jede Protokollzeile mit dem **Benutzer** gekennzeichnet, dessen Sitzung sie erzeugt hat, sodass Sie erkennen können, welcher Betrachter einen bestimmten Fehler oder eine Warnung ausgelöst hat. Die Kennzeichnung erfolgt nach bestem Bemühen – einige Framework- und Startzeilen laufen, bevor ein Betrachter beteiligt ist, und zeigen möglicherweise keinen Benutzer.

## Nutzungskennzahlen (Server-Apps)

Klicken Sie in der Zeile einer Server-App auf das Symbol **Usage Metrics** – neben **Protokolle anzeigen** –, um zu sehen, wie die App genutzt wird. Die Ansicht fasst Folgendes zusammen:

- **Eindeutige Benutzer** – wie viele verschiedene Personen die App geöffnet haben.
- **Sitzungen** – wie oft sie geöffnet wurde.
- **Durchschnittliche und mediane Sitzungsdauer** – etwa wie lange ein Besuch dauert.
- **Zuletzt verwendet** – wann die App zuletzt geöffnet wurde.

Unter der Zusammenfassung erhalten Sie eine Aufschlüsselung **pro Benutzer** und **pro Tag**, sodass Sie sehen, wer die App nutzt und wie sich die Nutzung im Zeitverlauf entwickelt.

> Die Dauern sind ungefähre Werte. Server-Apps gehen in den Leerlauf und skalieren herunter, wenn sie niemand nutzt, sodass das genaue Ende einer Sitzung nicht immer beobachtet wird – verstehen Sie die Dauerwerte als Richtwert, nicht als exakte Messung.

## Eine App bearbeiten

Klicken Sie in der Zeile einer App auf das **Stift**-Symbol, um sie zu bearbeiten. Das Bearbeitungsformular richtet sich nach der Laufzeit der App.

Bei einer **Server**-App können Sie Name, Slug, Branch, Einstiegspunkt, CPU, Arbeitsspeicher, Design, Leerlaufzeitraum, Public-Flag, Domains für die eingebettete Bereitstellung und Memo ändern. Die **Git-Verbindung** steht fest, sobald die App erstellt ist, und wird schreibgeschützt angezeigt. Das Speichern erstellt die App neu – ihr Status wechselt zu **Wird erstellt…**, bis der neue Build bereit ist.

## Eine App entfernen

Klicken Sie in der Zeile einer App auf das **Minus**-Symbol und bestätigen Sie; das Löschen oder Aufheben der Veröffentlichung einer App verlangt immer zuerst eine Bestätigung. Das Entfernen einer Server-App baut ihren Build und ihre Bereitstellung ab; das Entfernen einer WASM-App hebt die Veröffentlichung der statischen Datei auf. Die URL der App funktioniert sofort nicht mehr.

Das MCP-Tool `panel_deployment_manage` bietet das Aufheben der Veröffentlichung nicht mehr an. Entfernen Sie eine App stattdessen aus dieser Liste.
