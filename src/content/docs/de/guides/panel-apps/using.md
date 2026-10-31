---
title: Eine Panel-App verwenden
description: Verfolgen Sie in PlaidCloud auf dem Bildschirm „Meine Panel-Apps“ den Build-Status veröffentlichter HoloViz-Panel-Apps und öffnen, neu erstellen, sperren, bearbeiten und entfernen Sie sie, zeigen Sie ihre Protokolle und Nutzungskennzahlen an.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/using.md
---

Jede veröffentlichte App erscheint auf dem Bildschirm **Meine Panel-Apps** mit ihrer **Laufzeit**, ihrem **Status**, ihrem **Slug** und ihren Zeitstempeln. Die Spalte ganz links öffnet die App; über die übrigen Symbole in der Zeile können Sie die App gegen versehentliche Änderungen sperren, bearbeiten und entfernen und – bei Server-Apps – neu erstellen, ihre Protokolle anzeigen und ihre Nutzungskennzahlen anzeigen. Das Symbol zum Öffnen richtet sich nach der Laufzeit der App, sodass sich WASM- und Server-Apps auf einen Blick unterscheiden lassen.

## Build-Status (Server-Apps)

Die Spalte **Status** einer Server-App zeigt den Fortschritt ihres Builds an, und die Liste aktualisiert sich selbstständig, solange ein Build läuft:

- **Wird erstellt…** – PlaidCloud erstellt aus Ihrem Repository einen Container. Die App hat noch keine URL.
- **Bereit** – Der Build war erfolgreich. Die URL der App ist aktiv, und in ihrer Zeile erscheint das Symbol **Öffnen**.
- **Fehlgeschlagen** – Der Build wurde nicht abgeschlossen. Prüfen Sie den Einstiegspunkt und den Branch, und bearbeiten Sie dann die App, um sie erneut zu veröffentlichen.

WASM-Apps haben keinen Build-Schritt und sind sofort nach der Veröffentlichung verfügbar.

## Eine Server-App neu erstellen

Klicken Sie in der Zeile einer Server-App auf das Symbol **Neu erstellen**, um sie neu zu erstellen und erneut bereitzustellen, ohne ihre Einstellungen zu ändern. Der Status der App wechselt wieder zu **Wird erstellt…**, während PlaidCloud denselben Branch und denselben Einstiegspunkt erneut erstellt, und anschließend zurück zu **Bereit**, sobald der neue Build aktiv ist.

Verwenden Sie **Neu erstellen** nach Änderungen an Abhängigkeiten, nach Aktualisierungen des Basis-Images oder nach einem vorübergehend fehlgeschlagenen Build. Auch das Bearbeiten und Speichern einer Server-App löst einen neuen Build aus, ein erneuter Build erfordert jedoch nicht, dass Sie das Bearbeitungsformular öffnen.

Bei einer [App-Runner](/de/guides/workflows/use-converted-alteryx-apps/#die-app-aktuell-halten)-App – dem Eingabeformular, das für eine konvertierte Alteryx-App generiert wird – aktualisieren **Neu erstellen** und das Speichern einer Änderung zuerst die generierten Dateien auf die aktuelle App-Runner-Version und erstellen die App anschließend. PlaidCloud tut dies auch für jede nicht gesperrte App-Runner-App, wenn PlaidCloud selbst aktualisiert wird; eine gesperrte App benötigt nach dem Entsperren ein **Neu erstellen**.

## Eine App sperren

Klicken Sie in der Zeile einer App auf das Symbol **Sperren**, um sie vor versehentlichen Änderungen zu schützen. Solange eine App gesperrt ist, gilt Folgendes:

- **Bearbeiten**, **Entfernen** und **Neu erstellen** werden verweigert, und Sie erhalten die Meldung, dass die App gesperrt ist.
- Ein **Push auf den Branch einer Server-App löst keinen neuen Build aus** – der automatische Build wird übersprungen, bis Sie die App entsperren. Für einen übersprungenen Push läuft kein Build, daher erscheint in den Build-Protokollen der App nichts Neues; pushen Sie nach dem Entsperren erneut (oder verwenden Sie **Neu erstellen**), um die Änderung zu übernehmen.
- Das Öffnen der App, das Anzeigen ihrer Protokolle und das Anzeigen ihrer Nutzungskennzahlen funktionieren weiterhin – die Sperre verhindert nur Änderungen, niemals den Zugriff von Betrachtern.

Klicken Sie erneut auf das Symbol, um die App zu entsperren. Das Symbol zeigt den aktuellen Zustand der App: geschlossen bei gesperrter, geöffnet bei nicht gesperrter App.

Die Sperre schützt vor Versehen – einer irrtümlichen Bearbeitung, einem unbeabsichtigten Löschen oder einem Git-Push auf eine App, die Sie gerade vorführen –, genau wie die Sperre bei Workflows und Workflow-Schritten. Sie ist **keine** Sicherheitsmaßnahme: Jeder, der Panel-Apps bearbeiten darf, kann sie auch entsperren.

> Zwei Dinge deckt die Sperre nicht ab: Ein **bereits laufender Build** wird auch dann noch abgeschlossen und geht live, wenn Sie die App währenddessen sperren, und die Dateien einer **WASM**-App liegen in ihrem Dokumentenkonto, sodass das Ersetzen dieser Dateien die laufende App ändert, ohne den gesperrten Datensatz zu berühren.

## Eine App öffnen

Klicken Sie am Anfang der Zeile einer bereiten App auf das Symbol **Öffnen**, um sie in einem neuen Tab zu starten.

- Eine Server-App wird unter `https://<your-tenant-host>/serve/<slug>/` bereitgestellt.
- Das Symbol **Öffnen** erscheint erst, wenn eine Server-App **Bereit** ist.

Eine Server-App wird bei Inaktivität auf null skaliert, um Ressourcen zu sparen, sodass sie beim ersten Öffnen nach einer Ruhephase erst hochgefahren werden muss. Währenddessen sehen Sie statt eines leeren Tabs einen **PlaidCloud-Ladebildschirm** mit dem Namen Ihrer App, einer Fortschrittsanzeige und den Details Ihres Workspace. Die App erscheint von selbst, sobald sie bereit ist (in der Regel nach wenigen Sekunden, bei einem Kaltstart nach bis zu etwa einer Minute), und reagiert dann normal, bis sie wieder inaktiv wird.

> Wenn eine App nicht starten kann, wechselt der Ladebildschirm zu einer Meldung **„Diese App wurde nicht gestartet“** mit der Schaltfläche **Erneut versuchen**, statt endlos zu laden. Falls das wiederholt auftritt, bearbeiten Sie die App, prüfen Sie ihren Einstiegspunkt und Branch und veröffentlichen Sie sie erneut, oder wenden Sie sich an Ihren PlaidCloud-Administrator.

### Darstellung

Server-Panel-Apps verwenden standardmäßig das moderne **FAST**-Design von PlaidCloud, doch über die Einstellung **Design** der App können Sie wieder zum **Standard**-Styling von Panel wechseln, wenn vorhandenes CSS darauf angewiesen ist. Das Theme – hell, dunkel oder ein Hell/Dunkel-Umschalter, den Betrachter selbst betätigen können – legen Sie in der Vorlage Ihrer App fest. Die Muster dafür finden Sie unter [Theme festlegen](/de/guides/panel-apps/creating/#das-design-festlegen-hell-dunkel-oder-umschalter) im Leitfaden zum Erstellen. Wenn die Tabellen oder das benutzerdefinierte Styling Ihrer App für einen hellen Hintergrund ausgelegt sind, lassen Sie sie auf „hell“ festgelegt.

## Protokolle anzeigen (Server-Apps)

Klicken Sie in der Zeile einer Server-App auf das Symbol **Protokolle anzeigen**, um die Protokollansicht zu öffnen. (WASM-Apps laufen vollständig im Browser und haben keine Serverprotokolle, daher erscheint das Symbol nur in den Zeilen von Server-Apps.)

Die Ansicht hat zwei Registerkarten:

- **Laufzeit** (zuerst angezeigt) – die eigene Ausgabe der laufenden App: alles, was sie protokolliert, alles, was sie ausgibt, und alle nicht abgefangenen Fehler. Diese bleiben auch erhalten, nachdem die App auf null skaliert wurde, sodass Sie nachvollziehen können, was eine frühere Sitzung getan hat.
- **Build** – die Ausgabe beim Erstellen des Containers der App. Damit sehen Sie, *warum* ein Build **Fehlgeschlagen** anzeigt – zum Beispiel, weil sich eine Abhängigkeit nicht installieren ließ.

Jede Registerkarte bietet die Filter **Info / Warnung / Fehler**, einen Zeitbereich **Protokolle seit** (von der letzten Stunde bis zu 30 Tagen oder alle), die Schaltfläche **Aktualisieren** und **Automatisch aktualisieren**, um nach neuen Einträgen abzufragen – praktisch, wenn Sie eine laufende App oder einen laufenden Build beobachten. Die neuesten Einträge stehen zuerst.

> Wenn die Build-Ausgabe nicht erfasst werden konnte, zeigt die Registerkarte „Build“ einen kurzen Hinweis mit der Begründung an, statt leer zu bleiben.

### Eine vollständige Protokollnachricht lesen

Die Protokolltabelle kürzt lange Zeilen, damit die Liste lesbar bleibt. Wählen Sie eine Protokollzeile aus, um neben der Tabelle einen **Detailbereich** zu öffnen, der die vollständige Nachricht des Eintrags zeigt. So lesen Sie am einfachsten, was für die Tabelle zu lang ist – etwa eine lange Fehlermeldung oder einen vollständigen Stack-Trace –, ohne dass es abgeschnitten wird.

### Protokollzeilen kopieren

Sie können mehrere Protokollzeilen gleichzeitig auswählen und auf **Kopieren** klicken, um sie in die Zwischenablage zu legen. Das ist praktisch, um Protokolle beim Debuggen Ihrer App in einen Chat mit einem KI-Assistenten einzufügen oder in eine Nachricht an Ihr Team oder den PlaidCloud-Support.

### Wer eine Protokollzeile ausgelöst hat

Wenn Ihre App Betrachter anmeldet, wird jede Protokollzeile mit dem **Benutzer** gekennzeichnet, dessen Sitzung sie erzeugt hat, sodass Sie erkennen können, welcher Betrachter auf einen bestimmten Fehler oder eine bestimmte Warnung gestoßen ist. Die Kennzeichnung erfolgt nach bestem Bemühen – einige Framework- und Startzeilen laufen, bevor ein Betrachter beteiligt ist, und zeigen möglicherweise keinen Benutzer an.

## Nutzungskennzahlen (Server-Apps)

Klicken Sie in der Zeile einer Server-App auf das Symbol **Nutzungskennzahlen** – neben **Protokolle anzeigen** –, um zu sehen, wie die App genutzt wird. Die Ansicht fasst Folgendes zusammen:

- **Eindeutige Benutzer** – wie viele verschiedene Personen die App geöffnet haben.
- **Sitzungen** – wie oft sie geöffnet wurde.
- **Durchschnittliche und mittlere Sitzungsdauer** – ungefähr, wie lange ein Besuch dauert.
- **Zuletzt verwendet** – wann die App zuletzt geöffnet wurde.

Unterhalb der Zusammenfassung erhalten Sie eine Aufschlüsselung **pro Benutzer** und **pro Tag**, damit Sie sehen, wer die App nutzt und wie sich die Nutzung im Zeitverlauf entwickelt.

> Die Dauerangaben sind ungefähr. Server-Apps werden inaktiv und herunterskaliert, wenn sie niemand nutzt, sodass das genaue Ende einer Sitzung nicht immer erfasst wird – verstehen Sie die Dauerwerte als Richtwert, nicht als exakte Messung.

## Eine App bearbeiten

Klicken Sie in der Zeile einer App auf das **Stift**-Symbol, um sie zu bearbeiten. Das Bearbeitungsformular richtet sich nach der Laufzeit der App.

Bei einer **Server**-App können Sie den Namen, den Slug, den Branch, den Einstiegspunkt, die CPU, den Arbeitsspeicher, das Design, das Leerlauffenster, das Flag „öffentlich“, die Domains für die eingebettete Bereitstellung und das Memo ändern. Die **Git-Verbindung** steht fest, sobald die App erstellt ist, und wird schreibgeschützt angezeigt. Das Speichern erstellt die App neu – ihr Status wechselt zu **Wird erstellt…**, bis der neue Build bereit ist.

## Eine App entfernen

Klicken Sie in der Zeile einer App auf das **Minus**-Symbol und bestätigen Sie; das Löschen oder Aufheben der Veröffentlichung einer App erfordert immer zuerst eine Bestätigung. Das Entfernen einer Server-App baut ihren Build und ihre Bereitstellung ab; das Entfernen einer WASM-App hebt die Veröffentlichung der statischen Datei auf. Die URL der App funktioniert sofort nicht mehr.

Das MCP-Tool `panel_deployment_manage` bietet das Aufheben der Veröffentlichung nicht mehr an. Entfernen Sie eine App stattdessen aus dieser Liste.
