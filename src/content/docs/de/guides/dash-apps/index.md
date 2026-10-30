---
title: Dash-Apps
description: Erstellen und veröffentlichen Sie serverseitige Plotly-Dash-Datenanwendungen in PlaidCloud – aus einem Git-Repository veröffentlicht und mit benutzerspezifischer Authentifizierung und Scale-to-Zero bereitgestellt, gleichwertig zu serverseitigen Panel-Apps.
sidebar:
  label: Dash-Apps
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/index.md
---

Mit Dash-Apps veröffentlichen Sie interaktive [Plotly-Dash](https://dash.plotly.com/)-Anwendungen – Callbacks, Diagramme und Datenraster (`dash-ag-grid`, `dash-mantine-components`) – direkt aus PlaidCloud. Sie verwalten sie im Bildschirm **Meine Panel-Apps**, neben Ihren Panel-Apps; dort zeigt jede Zeile Laufzeit, Build-Status und URL.

## Wo Dash passt

Eine Dash-App wird genau wie eine **serverseitige Panel-App** gehostet: Sie verweisen PlaidCloud auf einen Branch eines Git-Repositorys, es erstellt aus Ihrem Code einen Container, und der Container ruht bei null Replikaten, wacht bei der ersten Anfrage auf, bedient Anfragen und skaliert bei Leerlauf wieder auf null. Für Dash gibt es keine separate „WASM“-Laufzeit – jede Dash-App ist eine Server-App.

Greifen Sie zu einer Dash-App, wenn Ihre App mit Plotly Dash statt mit HoloViz Panel geschrieben ist – zum Beispiel bei einer bestehenden Dash-Codebasis oder einem Team, das das Callback-Modell von Dash und das Ökosystem aus `dash-ag-grid` / `dash-mantine-components` bevorzugt. Wenn Sie neu anfangen und keine Präferenz haben, finden Sie unter [Panel-Apps](/de/guides/panel-apps/) die Alternative.

Alles, was eine serverseitige Panel-App bietet, bietet auch eine Dash-App:

- **Benutzerspezifische Identität.** Jeder Betrachter meldet sich mit dem Single Sign-on der Plattform an, und jeder Aufruf der App zum Lesen von Daten wird *als dieser Betrachter* ausgeführt – dasselbe Modell wie unter [Daten und angemeldeten Benutzer lesen](/de/guides/panel-apps/accessing-data/), mit der eigenen Hilfs-API von Dash. Siehe [Daten und angemeldeten Benutzer in einer Dash-App lesen](/de/guides/dash-apps/accessing-data/).
- **Scale-to-Zero.** Die App ruht nach dem konfigurierten Leerlauffenster bei null Replikaten und wacht bei der nächsten Anfrage auf, wobei während des Kaltstarts kurz ein PlaidCloud-Ladebildschirm erscheint – siehe [Eine Dash-App verwenden](/de/guides/dash-apps/using/#eine-dash-app-öffnen).
- **Automatische Neuerstellung.** Jeder Push auf den verbundenen Branch erstellt die App neu und stellt sie erneut bereit.
- **Laufzeit- und Build-Protokolle**, jeweils mit der Kennzeichnung des Betrachters, dessen Sitzung eine Zeile erzeugt hat.

Zwei Dinge hat eine Dash-App **nicht**, beides gewollt und beides ebenso bei einer Panel-App nicht vorhanden:

- **Keine Design-/Themeneinstellung.** Die Option **Design** im Veröffentlichungsdialog von Panel (FAST oder Standard) betrifft nur Panel – Dash-Apps gestalten sich vollständig über die Komponenten, die Sie wählen (`dash-mantine-components`, eigenes CSS usw.), daher hat das Veröffentlichungsformular kein entsprechendes Feld.
- **Keine Zugriffsliste pro App.** Der Zugriff ist das SSO-Tor des Workspace – jeder in Ihrem Tenant Angemeldete kann die App öffnen (oder, wenn Sie **Öffentlichen Zugriff zulassen** aktivieren, jeder überhaupt). Für keinen der beiden App-Typen gibt es eine separate ACL-Ebene pro App.

## App-Vertrag

Die Einstiegsdatei einer Dash-App muss `app.py` heißen und einen `server` bereitstellen – das ist der gesamte Vertrag:

```python
from dash import Dash

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you
```

- **Nennen Sie die Datei `app.py`.** Der Launcher von PlaidCloud importiert Ihre App als Modul `app` und liest sein `server`-Objekt. Welchen Pfad Sie auch in **Einstiegspunkt** angeben (Repository-Stamm oder Unterordner), die Datei unter diesem Pfad muss `app.py` heißen.
- **Stellen Sie `server = app.server`** auf Modulebene bereit. Das ist das Objekt, das die Plattform importiert.
- **Sie richten die Anmeldung nicht selbst ein.** Die Plattform schaltet jede Anfrage automatisch hinter ein benutzerspezifisches Single Sign-on – Sie müssen weder `init_auth` aufrufen noch `plaidcloud_dash` importieren, nur um die Identität zu erhalten. (Eine ältere App, die `plaidcloud_dash.init_auth(server, url_base_pathname=os.environ["DASH_URL_BASE_PATHNAME"])` *aufruft*, funktioniert unverändert weiter – der Aufruf ist idempotent und verträgt sich daher mit der eigenen Einrichtung der Plattform.)
- **Setzen Sie `requests_pathname_prefix` oder `url_base_pathname` nicht bei `Dash(__name__)`.** Jede Dash-App wird unter einem verpflichtenden URL-Präfix (`/serve/<slug>/`) bereitgestellt, und die Plattform setzt es für Sie über die Umgebungsvariable `DASH_URL_BASE_PATHNAME` – Dashs eigene native Konfigurationsvariable, die vor jedem Konstruktorargument gelesen wird. Wird das Präfix zusätzlich explizit übergeben, kollidiert das mit der Konfiguration von Dash, und die App startet nicht.
- **`Entry Point` kann in einen Unterordner zeigen.** Vor dem Start der App setzt der Host das Arbeitsverzeichnis des Containers auf den Ordner der Einstiegsdatei – Importe von Geschwister-Modulen im selben Ordner (`import data`) und relative Dateipfade in Ihrer App werden daher relativ zu diesem Ordner aufgelöst, genau wie beim Ausführen von `python app.py` in diesem Ordner.
- **Lesen Sie keine Daten beim Import.** Führen Sie Ihre PlaidCloud-Lesezugriffe in Callbacks aus, nicht im Modulbereich – siehe [Daten und angemeldeten Benutzer in einer Dash-App lesen](/de/guides/dash-apps/accessing-data/). Das Modul Ihrer App wird einmal beim Containerstart ausgeführt, bevor sich ein Betrachter angemeldet hat; eine Verbindung oder ein Tabellenzugriff an dieser Stelle hat keinen Betrachter, als den es handeln könnte, und lässt die App beim Start scheitern.

PlaidCloud führt Ihre App unter **Gunicorn mit Threads** aus, sodass sie mehrere gleichzeitige Betrachter aus einem Prozess bedient – Sie müssen nichts zusätzlich tun, damit mehr als eine Person die App gleichzeitig nutzen kann.

## Zwischen Panel und Dash wählen

| | Panel-Apps | Dash-Apps |
|---|---|---|
| Framework | HoloViz Panel | Plotly Dash |
| Laufzeiten | WASM (im Browser) oder Server | Nur Server |
| Identitätsmodell | Benutzerspezifisches SSO (Server-Apps) | Benutzerspezifisches SSO |
| Scale-to-Zero | Nur Server-Apps | Ja |
| Design-/Themeneinstellung | Ja (FAST / Standard) | Nein – Gestaltung über Ihre eigenen Komponenten |
| Zugriffsliste pro App | Nein – SSO-Tor des Workspace | Nein – SSO-Tor des Workspace |

## Nächste Schritte

- [Dash-App aus PlaidCloud Git bereitstellen](/de/guides/dash-apps/deploy-from-git/) – der vollständige Weg vom Repository zur bereitgestellten App, mit einer verwalteten Verbindung ohne Zugangsdaten.
- [Daten und angemeldeten Benutzer in einer Dash-App lesen](/de/guides/dash-apps/accessing-data/) – Abfragen von PlaidCloud-Daten als die Person, die die App ansieht.
- [Eine Dash-App verwenden](/de/guides/dash-apps/using/) – Build-Status, Öffnen der App, Protokolle und Entfernen.
