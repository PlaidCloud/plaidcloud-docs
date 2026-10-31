---
title: Eine Panel-App erstellen
description: Erstellen Sie eine Panel-App in Panel Studio aus einer leeren App, einer Tabelle, einer Ansicht oder der Galerie, oder veröffentlichen Sie für Sonderfälle eine Server-App aus Git oder eine statische WASM-App.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

Beginnen Sie mit Panel Studio. Es benötigt weder ein Repository noch eine Einrichtung: Sie erstellen die App in PlaidCloud, sehen sich eine Vorschau an und veröffentlichen sie, wenn Sie bereit sind. Wählen Sie eine eigene Laufzeit nur, wenn Studio nicht passt.

## Eine Studio-App erstellen

Öffnen Sie **Meine Panel-Apps**. **Neue Studio-App** ist die erste Schaltfläche in der Symbolleiste. Sie können **Neue Studio-App** auch im Feld **Panel-Apps** auf der Registerkarte **Startseite** eines Projekts wählen oder [mit einer Tabelle beginnen](#mit-einer-tabelle-beginnen).

1. Wählen Sie **Neue Studio-App**.
2. Geben Sie einen **Name** ein. Der **URL-Slug** wird daraus ausgefüllt.
3. Wählen Sie das **Projekt**, dem die App gehört. Sie benötigen Bearbeitungszugriff auf das Projekt.
4. Wählen Sie unter **Starten mit**, womit die App beginnt:

   | Starten mit | Sie erhalten |
   |---|---|
   | **Leere App** | Eine minimale App mit einer `app.py` und einer `requirements.txt`. |
   | **Aus einer Tabelle** | Eine App auf Basis der gewählten Tabelle. |
   | **Aus einer Ansicht** | Dasselbe, auf Basis einer Projektansicht. |
   | **Aus einer anderen Studio-App** | Eine Kopie einer Ihrer Studio-Apps. |
   | **Aus der Galerie** | Eine Kopie einer App, die Ihr Workspace [in der Galerie aufgeführt](#mit-der-galerie-beginnen) hat. |

5. Wählen Sie **Erstellen**. Studio öffnet die neue App. Bei einer Tabelle oder Ansicht ist Weaves Aufforderung, die erste Seite zu erstellen, versandbereit.

Wie Sie die App bearbeiten, in der Vorschau ansehen und veröffentlichen, lesen Sie unter [Panel Studio](/de/guides/panel-apps/studio/).

### Mit einer Tabelle beginnen

Sie können auch auf der Registerkarte **Tabellen** eines Projekts beginnen. Wählen Sie eine Tabelle oder Ansicht aus und wählen Sie dann **Panel-App erstellen** im Menü **Neu** oder im Kontextmenü. Das Dialogfeld **Neue Studio-App** öffnet sich mit bereits gewähltem Projekt und gewählter Tabelle. Der Befehl ist verfügbar, wenn Sie Bearbeitungszugriff auf das Projekt haben und das Projekt nicht schreibgeschützt ist.

### Mit der Galerie beginnen

Wählen Sie **Galerie** in der Symbolleiste von **Meine Panel-Apps**, um die Apps zu durchsuchen, die Ihr Workspace aufgeführt hat, und dann **App daraus erstellen…**, um Ihre eigene Kopie zu erstellen. Oder wählen Sie **Aus der Galerie** im Dialogfeld **Neue Studio-App**. Siehe [Die App-Galerie](/de/guides/panel-apps/gallery/), auch dazu, wie Sie Ihre eigene App aufführen.

## Andere Laufzeiten

Studio-Apps decken die meisten Dashboards und Tools ab. Für Sonderfälle veröffentlichen Sie in der Symbolleiste von **Meine Panel-Apps** mit einer der anderen [Laufzeiten](/de/guides/panel-apps/):

- **WASM-App hinzufügen** – eine statische App, die im Browser läuft, aus einer Datei veröffentlichen.
- **Neue Server-App** – eine App aus einem von Ihnen verwalteten Git-Repository erstellen und ausführen, zum Beispiel um vorhandenen Code oder Ihren eigenen Build-Prozess wiederzuverwenden.
- **Neue Dash-App** – eine Plotly-Dash-App veröffentlichen. Siehe [Dash-Apps](/de/guides/dash-apps/).

## Eine Server-App erstellen

Eine Server-App wird aus einem Git-Repository erstellt und unter `https://<your-tenant-host>/serve/<slug>/` bereitgestellt. Sie verweisen PlaidCloud auf einen Branch eines Repositorys; PlaidCloud baut den Code zu einem Container, führt darin `panel serve` aus und baut automatisch neu, sobald Sie auf diesen Branch pushen.

### Ihr App-Repository vorbereiten

Ihr Repository braucht zwei Dinge: einen **Einstiegspunkt** – eine Python-Datei, die eine Panel-App erstellt und mit `.servable()` markiert – und optional eine **`requirements.txt`**, die zusätzliche Pakete auflistet, entweder im Stammverzeichnis des Repositorys oder neben Ihrem Einstiegspunkt.

```
my-panel-app/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

#### Hello World

Erstellen Sie `app.py`:

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello, PlaidCloud 👋\n\nYour first server-side Panel app is running.").servable()
```

Das ist eine vollständige App. Der Aufruf `.servable()` bestimmt, was PlaidCloud bereitstellt – alles, was dargestellt werden soll, muss als servable markiert sein (direkt oder als Teil eines servable-Layouts).

#### Ein etwas umfangreicheres Beispiel

Panel-Apps sind interaktiv. Diese hier fügt einen Schieberegler hinzu, der eine Tabelle live aktualisiert:

```python
import pandas as pd
import panel as pn

pn.extension()

multiplier = pn.widgets.IntSlider(name="Multiplier", start=1, end=10, value=3)

@pn.depends(multiplier)
def times_table(m):
    df = pd.DataFrame({"n": range(1, 6)})
    df["result"] = df["n"] * m
    return pn.pane.DataFrame(df, index=False)

pn.Column(
    "# Times Table",
    multiplier,
    times_table,
).servable()
```

#### Abhängigkeiten hinzufügen

Dieses zweite Beispiel importiert `pandas`, das nicht Teil des Basis-Images ist. Fügen Sie daher eine `requirements.txt` hinzu (im Stammverzeichnis des Repositorys oder neben Ihrem Einstiegspunkt):

```text
pandas
```

PlaidCloud installiert diese mit `pip`, wenn es das Image erstellt. Gängige Visualisierungsbibliotheken – `plotly`, `holoviews`, `hvplot` – gehören ebenfalls nicht zum Basis-Image. Führen Sie hier daher alle auf, die Ihre App importiert.

> **Was die Plattform bereitstellt – und erwartet.** Beachten Sie diese Annahmen beim Schreiben Ihrer App:
>
> - **`panel` und `bokeh` sind vorinstalliert** durch das Basis-Image der Plattform. Führen Sie sie nicht in `requirements.txt` auf und vermeiden Sie es, eine ältere Panel-Version festzulegen – der Wiederverbindungsmechanismus der Live-Aktualisierung setzt eine aktuelle voraus.
> - **Die PlaidCloud-Clientbibliotheken (`plaidcloud-rpc`, `plaidcloud-utilities`) sind vorinstalliert.** Importieren Sie `plaidcloud.rpc` oder `plaidcloud.utilities` direkt – führen Sie sie nicht in `requirements.txt` auf.
> - **`requirements.txt` kann im Stammverzeichnis des Repositorys oder neben Ihrem Einstiegspunkt liegen.** Halten Sie in einem gemeinsam genutzten Repository (Monorepo) die Abhängigkeiten jeder App im eigenen Ordner. Eine Datei auf Stammebene wird, falls vorhanden, ebenfalls installiert – legen Sie gemeinsame Abhängigkeiten dort ab und App-spezifische neben der App.
> - **Die App läuft als Nicht-Root-Benutzer auf einem schreibgeschützten Dateisystem.** Nur `/tmp` ist beschreibbar, schreiben Sie temporäre Dateien also dorthin (die meisten Bibliotheken beachten `$TMPDIR` bereits).
> - **Codieren Sie Port, URL-Präfix oder Host nicht fest.** PlaidCloud weist sie zu und fügt sie bei der Bereitstellung ein – rufen Sie einfach `.servable()` auf.

Für den PlaidCloud-Look und fertige Filter, Raster und Diagramme erstellen Sie Ihre App mit [dem Panel-App-Kit](/de/guides/panel-apps/app-kit/).

### Das Design festlegen: Hell, Dunkel oder Umschalter

Server-Apps werden standardmäßig im modernen **Fast**-Design von PlaidCloud dargestellt – ein sauberer Look im Fluent-Stil, der plattformweit angewendet wird. Im Veröffentlichungsdialog steuert **Design** diese Plattformebene:

- **FAST** – der PlaidCloud-Standard. Verwenden Sie ihn für neue Apps und für Apps, die mit Fast-Vorlagen erstellt wurden.
- **Standard** – das Standard-Styling von Panel. Verwenden Sie es, wenn das CSS oder die Darstellung einer vorhandenen App unter FAST nicht mehr funktioniert.

In Ihrem App-Code steuern Sie das **Theme**: hell, dunkel oder ein Umschalter, den der Betrachter betätigen kann.

Das Theme ist eine Eigenschaft der **Vorlage**, die Sie bereitstellen. Die Fast-Vorlagen – `FastListTemplate` (eine einzelne Spalte) und `FastGridTemplate` (ein responsives Raster) – kennen dafür zwei Einstellungen:

- **`theme`** – `"default"` für hell oder `"dark"`. Wenn Sie es setzen, bleibt die App auf dieses Theme festgelegt, auch wenn ein Betrachter `?theme=dark` an die URL anhängt.
- **`theme_toggle`** – `True` zeigt in der Kopfzeile einen Umschalter zwischen Hell und Dunkel; `False` blendet ihn aus. Standard ist `True`. Das Ausblenden des Umschalters legt das Theme nicht von selbst fest – legen Sie es mit `theme` (oben) fest; setzen Sie danach `theme_toggle=False`, damit Betrachter keinen Umschalter sehen, der nichts mehr ändert.

Wählen Sie das Muster, das zu Ihrer App passt.

**Nur hell** – am besten für dichte Berichte und Finanztabellen, die meist von Hand für einen hellen Hintergrund gestaltet sind:

```python
import panel as pn

pn.extension("tabulator")

pn.template.FastListTemplate(
    title="Sales Dashboard",
    theme="default",      # light
    theme_toggle=False,   # hide the switch
    main=[...],
).servable()
```

**Nur dunkel:**

```python
pn.template.FastListTemplate(
    title="Ops Monitor",
    theme="dark",
    theme_toggle=False,
    main=[...],
).servable()
```

**Den Betrachter wählen lassen** – standardmäßig hell, mit einem Umschalter in der Kopfzeile. Lassen Sie `theme` weg, damit es dem Umschalter folgt:

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **Wenn Sie Dunkel zulassen, machen Sie Ihre Tabellen dunkelfähig.** Ein `Tabulator`, der auf ein helles Tabellen-Theme (`theme="bootstrap"`) festgelegt ist, oder benutzerdefiniertes CSS mit fest codierten hellen Farben wie `background: #fff` erscheint auf einer dunklen Seite als unleserlicher weißer Block. Verwenden Sie ein Tabellen-Theme, das der App folgt – `pn.widgets.Tabulator(..., theme="fast")` – und vermeiden Sie fest codierte helle Farben. Wenn ein Bericht stark von Hand für Hell gestaltet ist, legen Sie ihn stattdessen auf Hell fest (das erste Muster oben).

Eine einfache App ohne Vorlage – `pn.Column(...).servable()` – folgt dem Standard von Panel und wird von diesen Einstellungen nicht beeinflusst; greifen Sie zu einer Vorlage, wenn Sie explizite Kontrolle wünschen.

Ihr Repository muss über eine **Git-Verbindung** in PlaidCloud erreichbar sein. Wenn Ihr Code in [PlaidCloud Git](/de/guides/git/) liegt, erstellen Sie unter **Tools > Connections** eine verwaltete **PlaidCloud Git**-Verbindung – sie braucht weder Server-URL noch Anmeldedaten. Den gesamten Weg von einem leeren Repository bis zu einer bereitgestellten App finden Sie unter [Eine Panel-App aus PlaidCloud Git bereitstellen](/de/guides/panel-apps/deploy-from-git/).

### Die App veröffentlichen

1. Klicken Sie auf **Neue Server-App**, um das Dialogfeld **Server-Panel-App veröffentlichen** zu öffnen. Seine Einstellungen sind in Abschnitte gegliedert.
2. Unter **Verzeichniseinstellungen**:
   - **App-Name** – der Anzeigename in der Liste.
   - **URL-Slug** – sowohl die URL der App als auch ihr interner Name, daher muss er ein gültiges DNS-Label sein: Kleinbuchstaben, Ziffern und Bindestriche, beginnend mit einem Buchstaben, höchstens 40 Zeichen (zum Beispiel `sales-dashboard`). Das Dialogfeld prüft dies vor dem Veröffentlichen.
   - **Notiz** – eine optionale Beschreibung.
   - **Projekt** – das Projekt, dem die App gehört. Es liefert das [Branding](/de/guides/panel-apps/branding/) der App und ist das Standardprojekt für ihre Tabellen. Sie können es nach dem Veröffentlichen hier nicht mehr ändern; verwenden Sie [Assign](/de/guides/panel-apps/branding/#für-vorhandene-apps).
3. Unter **Git-Verbindung und Veröffentlichungsüberwachung**:
   - **Git-Verbindung** – die Verbindung, die das Repository Ihrer App enthält.
   - **Branch** – der Branch, aus dem erstellt wird. Pushes auf diesen Branch bauen die App automatisch neu und stellen sie erneut bereit.
   - **Einstiegspunkt** – die `.py`-Datei, die Panel bereitstellen soll (Ihre `app.py`).
4. Unter **Laufzeit**:
   - **CPU** und **Arbeitsspeicher**, die der Container der App anfordern soll.

     > Weniger Ressourcen (niedrigere CPU / weniger Arbeitsspeicher) lassen die App schneller einplanen und kalt starten.

   - **Design** – wählen Sie **FAST** für das moderne Design von PlaidCloud oder **Standard**, wenn das CSS der App das Standard-Styling von Panel erwartet.
   - **Leerlauf (Minuten)** – wie lange die App ohne Datenverkehr betriebsbereit bleibt, bevor sie auf null herunterskaliert wird. Der Standard sind 5 Minuten.
   - **Öffentlichen Zugriff zulassen** – aktivieren Sie das Kontrollkästchen, um nicht authentifizierten Zugriff zuzulassen; andernfalls müssen sich Betrachter an Ihrem Tenant anmelden.
5. Unter **Erweitert (eingebettete Bereitstellung)** – optional. Standardmäßig wird die App nur von Ihrem PlaidCloud-Tenant bereitgestellt. Um sie in eine andere Website einzubetten, klicken Sie auf **Domäne hinzufügen** und geben Sie jede Domäne ein, die sie laden darf, eine pro Zeile – nur ein Host, ohne Schema oder Pfad (zum Beispiel `example.com` oder `app.example.com:8443`). Lassen Sie die Liste leer, sofern Sie die App nicht anderswo einbetten.
6. Klicken Sie auf **Veröffentlichen**.

Nach dem Veröffentlichen wird die App **erstellt** – ihr **Status** erscheint in der Liste und aktualisiert sich automatisch. Unter [Eine Panel-App verwenden](/de/guides/panel-apps/using/) lesen Sie, was die Status bedeuten, wie Sie die App öffnen, sobald sie bereit ist, und wie Sie einen Neuaufbau auslösen, ohne die Veröffentlichung aufzuheben.

> Die URL der App funktioniert erst, wenn ihr Build-Status **Bereit** lautet, und die erste Anfrage nach einer Leerlaufzeit fährt sie hoch (~15 Sekunden).

### Fortgeschritten: PlaidCloud lokal nachbilden

Technisch versierte Benutzer können die App mit denselben Eingaben erstellen und testen, die PlaidCloud verwendet. Das ist die engste lokale Prüfung vor dem Veröffentlichen oder dem Klicken auf **Neu erstellen**.

PlaidCloud baut aus dem gewählten Git-Branch mit diesem generierten Dockerfile. Verwenden Sie lokal denselben Inhalt als `Dockerfile.plaidcloud-panel`:

```dockerfile
FROM us-docker.pkg.dev/plaidcloud-build/panel-base/platform-panel-base:0.5.1
USER root
COPY . /app
RUN if [ -f /app/requirements.txt ]; then pip install --no-cache-dir -r /app/requirements.txt; fi
# If your entry point is in a subfolder, PlaidCloud also installs that folder's requirements.txt,
# after the root one (so a per-app pin wins). Replace <app-folder> with your entry point's folder,
# or drop this line if your app is at the repository root.
RUN if [ -f "/app/<app-folder>/requirements.txt" ]; then pip install --no-cache-dir -r "/app/<app-folder>/requirements.txt"; fi
USER 10001
```

So bilden Sie den Server-Build nach:

1. Checken Sie denselben Branch aus, den Sie unter **Branch** wählen.
2. Führen Sie den Build vom Stammverzeichnis des Repositorys aus, damit `COPY . /app` zu PlaidCloud passt.
3. Legen Sie optionale Abhängigkeiten in einer `requirements.txt` ab – im Stammverzeichnis des Repositorys oder neben Ihrem Einstiegspunkt. Beide werden installiert, die des App-Ordners zuletzt (damit eine app-spezifische Festlegung gewinnt).
4. Verwenden Sie denselben Einstiegspunktpfad, den Sie unter **Einstiegspunkt** wählen.

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

Das bereitgestellte Image überschreibt den Einstiegspunkt des Basis-Images nicht. Es führt `panel serve` mit Umgebungsvariablen aus, die PlaidCloud einfügt. Testen Sie das erstellte Image mit demselben Laufzeitvertrag:

```sh
docker run --rm \
  --cpus 0.5 \
  --memory 512m \
  -p 5006:5006 \
  -e APP_PATH=/app/app.py \
  -e PANEL_PREFIX=/serve/local \
  -e PANEL_PORT=5006 \
  -e PANEL_ORIGIN=localhost:5006 \
  -e PANEL_KEEP_ALIVE_MS=25000 \
  -e PLAID_PANEL_DESIGN=fast \
  local-panel-app:plaidcloud
```

Öffnen Sie `http://localhost:5006/serve/local/`.

Gleichen Sie beim Testen die Einstellungen des Veröffentlichungsdialogs ab:

- **Einstiegspunkt** entspricht `APP_PATH=/app/<entry-point>`.
- **CPU** und **Arbeitsspeicher** entsprechen den Docker-Grenzwerten `--cpus` und `--memory`.
- **Design: FAST** entspricht `PLAID_PANEL_DESIGN=fast`.
- **Design: Standard** bedeutet, `PLAID_PANEL_DESIGN` wegzulassen.
- **Leerlauf (Minuten)** entspricht dem Zeitfenster für das Herunterskalieren in der Bereitstellung. Lokales Docker erzwingt es nicht, aber die App verwendet weiterhin dieselben Einstellungen für Panel-Websocket-Keepalive und Sitzungsbereinigung.
- Domänen unter **Eingebettete Bereitstellung** entsprechen `PANEL_ORIGIN`; verwenden Sie eine durch Leerzeichen getrennte Liste, wenn Sie mehr als einen Host testen möchten.

Wenn Sie keinen Container benötigen, können Sie die Serve-Schicht dennoch aus einer lokalen Python-Umgebung testen. Installieren Sie dieselbe `requirements.txt`, setzen Sie die Umgebungsvariablen der Plattform und führen Sie dann `panel serve` mit denselben Flags aus, die das bereitgestellte Image verwendet.

```sh
export APP_PATH=app.py
export PANEL_PREFIX=/serve/local
export PANEL_PORT=5006
export PANEL_ORIGIN=localhost:5006
export PANEL_KEEP_ALIVE_MS=25000
export PLAID_PANEL_DESIGN=fast

panel serve "$APP_PATH" \
  --address 0.0.0.0 \
  --port "$PANEL_PORT" \
  --prefix "$PANEL_PREFIX" \
  --allow-websocket-origin "$PANEL_ORIGIN" \
  --num-procs 1 \
  --keep-alive "$PANEL_KEEP_ALIVE_MS" \
  --unused-session-lifetime 15000 \
  --index "$(basename "$APP_PATH" .py)"
```

Öffnen Sie `http://localhost:5006/serve/local/`.

Verwenden Sie `PLAID_PANEL_DESIGN=fast`, um dem standardmäßig bereitgestellten Look zu entsprechen. Um die Option **Standard** für das Design im Veröffentlichungsdialog zu testen, lassen Sie `PLAID_PANEL_DESIGN` ungesetzt und führen Sie denselben Befehl aus. Behalten Sie `PANEL_PREFIX`, `PANEL_ORIGIN`, `--keep-alive` und `--unused-session-lifetime` bei; sie sind Teil des Laufzeitvertrags der Bereitstellung.

## Eine WASM-App erstellen

Eine WASM-App läuft im Browser aus einer vorgefertigten HTML-Datei.

1. Klicken Sie auf **WASM-App hinzufügen**, um das Dialogfeld **Serverlose Panel-App veröffentlichen** zu öffnen.
2. Geben Sie einen **App-Name** und eine **Version** ein.
3. Wählen Sie den **HTML-Speicherort der App** – die HTML-Datei in einem Dokumentenkonto.
4. Geben Sie einen **URL-Slug der App** und eine optionale **Notiz** ein.
5. Klicken Sie auf **Veröffentlichen**. Eine WASM-App hat keinen Build-Schritt und wird sofort bereitgestellt.
