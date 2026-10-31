---
title: Panel-Apps
description: Erstellen und stellen Sie interaktive HoloViz-Panel-Datenanwendungen in PlaidCloud bereit – als statische Apps im Browser oder als serverseitige Apps, die aus einem Git-Repository erstellt werden.
sidebar:
  label: Panel-Apps
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/index.md
---

Mit Panel-Apps veröffentlichen Sie interaktive [HoloViz-Panel](https://panel.holoviz.org/)-Anwendungen – parametrisierte Eingaben, Live-Diagramme und eingebettete Datentabellen – direkt aus PlaidCloud. Sie verwalten sie auf dem Bildschirm **Meine Panel-Apps**, der jede App mit ihrer Laufzeit, ihrem Build-Status und ihrer URL auflistet.

Beginnen Sie in [Panel Studio](/de/guides/panel-apps/studio/): Wählen Sie **Neue Studio-App**, um in PlaidCloud eine App aus einer leeren App, einer Tabelle, einer Ansicht oder der Galerie zu erstellen, ohne ein Repository einzurichten. Für Sonderfälle veröffentlichen Sie mit einer der folgenden Laufzeiten, die in der Spalte **Laufzeit** angezeigt werden:

- **WASM** – eine statische App, die vollständig im Browser läuft (Pyodide). Sie veröffentlichen eine vorgefertigte HTML-Datei aus einem Dokumentenkonto. Es gibt keinen Serverprozess und nichts zu skalieren; die App wird sofort bereitgestellt.
- **Server** – eine App, die aus einem Git-Repository erstellt und serverseitig ausgeführt wird. Beim Veröffentlichen baut PlaidCloud Ihr Repository zu einem Container, der bei null Replikaten im Leerlauf bleibt, bei der ersten Anfrage an seine URL aufwacht, bereitstellt (einschließlich Live-Aktualisierungen) und im Leerlauf wieder auf null herunterskaliert. Das ist die richtige Wahl für Apps, die eine Python-Laufzeit, serverseitige Berechnung oder Bibliotheken benötigen, die nicht im Browser laufen können.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 250" role="img" aria-label="Die zwei Panel-App-Laufzeiten. Eine WASM-App ist eine vorgefertigte HTML-Datei, die ohne Server direkt an den Browser ausgeliefert wird. Eine Server-App wird aus einem Git-Repository zu einem Container gebaut, der bei null Replikaten im Leerlauf bleibt, bei der ersten Anfrage nach etwa fünfzehn Sekunden aufwacht, bereitstellt und im Leerlauf wieder auf null herunterskaliert." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pa-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="14" y="40" font-size="12" font-weight="700" fill="var(--sl-color-accent)">WASM</text>
  <rect x="70" y="24" width="150" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="49" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">fertige HTML-Datei</text>
  <path d="M220 45 L286 45" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="288" y="24" width="164" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="370" y="43" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Browser · Pyodide</text>
  <text x="370" y="58" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">sofort bereitgestellt</text>
  <line x1="14" y1="96" x2="666" y2="96" stroke="var(--sl-color-gray-5)" stroke-dasharray="3 3" />
  <text x="14" y="146" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Server</text>
  <rect x="70" y="128" width="96" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="118" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Git-Repo</text>
  <path d="M166 149 L186 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="188" y="128" width="110" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="243" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Container bauen</text>
  <path d="M298 149 L318 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="320" y="128" width="120" height="42" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="380" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Leerlauf · 0 Replikate</text>
  <text x="380" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">nichts läuft</text>
  <path d="M440 149 L474 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <text x="457" y="140" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">1. Anfr.</text>
  <rect x="476" y="128" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="536" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Bereitstellung</text>
  <text x="536" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">wacht auf ~15 s</text>
  <path d="M536 170 C536 212 380 212 380 174" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#pa-arrow)" />
  <text x="458" y="206" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">skaliert im Leerlauf auf 0 zurück</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Zwei Laufzeiten: Eine <strong>WASM</strong>-App ist eine vorgefertigte HTML-Datei, die direkt an den Browser ausgeliefert wird; eine <strong>Server</strong>-App wird aus Git gebaut, bleibt bei null im Leerlauf, wacht bei der ersten Anfrage auf (~15 s), stellt bereit und skaliert wieder auf null zurück.</figcaption>
</figure>

## Eine Laufzeit wählen

| | WASM | Server |
|---|---|---|
| Quelle | Eine veröffentlichte HTML-Datei | Ein Git-Repository (Verbindung, Branch, Einstiegspunkt) |
| Läuft | Im Browser | Serverseitig, Scale-to-Zero |
| Am besten für | Leichtgewichtige, eigenständige Dashboards | Apps, die Serverberechnung oder vollständige Python-Bibliotheken benötigen |
| Kaltstart | Keiner | Die erste Anfrage fährt die App hoch (~15 Sekunden) |

## Nächste Schritte

- [Panel Studio](/de/guides/panel-apps/studio/) – erstellen, bearbeiten, in der Vorschau ansehen und veröffentlichen Sie eine App in PlaidCloud, ohne ein Repository einzurichten.
- [Eine Panel-App aus PlaidCloud Git bereitstellen](/de/guides/panel-apps/deploy-from-git/) – der vollständige Weg vom Repository zu einer bereitgestellten App über eine verwaltete Verbindung ohne Anmeldedaten.
- [Panel-Apps mit Weave erstellen](/de/guides/panel-apps/build-with-weave/) – beschreiben Sie die App und genehmigen Sie die genaue Änderung, die Weave vorschlägt.
- [Eine Panel-App erstellen](/de/guides/panel-apps/creating/) – starten Sie eine Studio-App aus einer leeren App, einer Tabelle oder der Galerie, oder veröffentlichen Sie eine Server-App aus Git oder eine WASM-App aus einer Datei.
- [Das Panel-App-Kit](/de/guides/panel-apps/app-kit/) – erstellen Sie Apps im PlaidCloud-Look, in Hell und Dunkel, mit Filtern, Kennzahlen auf einen Blick, einem serverseitig paginierten Datenraster, Diagrammen, Formularen, Ausführungsschaltflächen, gespeicherten Einstellungen und Drucken.
- [Die Data API für Panel-Apps](/de/guides/panel-apps/data-api/) – filtern, paginieren, zählen und aggregieren Sie Tabellen auf dem Server.
- [Warnungen und Digests](/de/guides/panel-apps/alerts-and-digests/) – erhalten Sie eine Push-Benachrichtigung, E-Mail, Slack- oder Teams-Nachricht, wenn eine Zahl eine Grenze überschreitet, oder eine geplante Zusammenfassung.
- [Die App-Galerie](/de/guides/panel-apps/gallery/) – führen Sie eine App als Vorlage auf und erstellen Sie aus aufgeführten Apps neue Apps.
- [Projekt-Branding und App-Projekte](/de/guides/panel-apps/branding/) – legen Sie Farben und ein Logo für die Apps eines Projekts fest und ordnen Sie Apps Projekten zu.
- [Eine Panel-App verwenden](/de/guides/panel-apps/using/) – Build-Status, Öffnen der App, Bearbeiten und Entfernen.
- [Einen KI-Agent in einer Panel-App erstellen](/de/get-started/tutorials/panel-ai-agent/) – ein Tutorial: Geben Sie einem KI-Agent die REST-API als Werkzeuge, beschränkt auf die eigenen Berechtigungen des Betrachters.
