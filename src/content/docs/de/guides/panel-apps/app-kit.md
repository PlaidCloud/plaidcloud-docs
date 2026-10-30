---
title: Das Panel-App-Kit
description: Erstellen Sie Panel-Apps im PlaidCloud-Look mit dem Kit plaidcloud_panel – App-Shell, Befehlspalette, FilterBar, KpiCard, DataGrid, Chart, Form, Ausführungsschaltflächen, gespeicherte Einstellungen, Drucken und Übersetzungen, in Hell und Dunkel.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

Auf jeder Server-Panel-App ist das Kit `plaidcloud_panel` installiert. Es gibt Ihrer App den PlaidCloud-Look – dieselben Farben, Schriften und Abstände wie der Rest der Plattform, in Hell und Dunkel – und stellt fertige Komponenten für die Bildschirme bereit, die die meisten Apps benötigen: Filter, Kennzahlen auf einen Blick, ein großes Datenraster, Diagramme und Formulare. Ihre App übernimmt das [Branding Ihres Projekts](/de/guides/panel-apps/branding/) automatisch.

```python
import plaidcloud_panel as pcp
```

Das Importieren des Kits wendet den PlaidCloud-Look auch auf Plotly- und Matplotlib-Diagramme an.

## Mit einer Vorlage beginnen

In [Panel Studio](/de/guides/panel-apps/studio/) beginnt **Neue Studio-App** mit einer leeren App, einer Tabelle oder Ansicht, einer anderen Studio-App oder einer App in der [Galerie](/de/guides/panel-apps/gallery/), ohne dass ein Befehl ausgeführt werden muss.

Für eine App, die Sie in einem Git-Repository verwalten, enthält das Kit einen Befehl, der eine funktionsfähige Starter-App schreibt. Führen Sie ihn in einem beliebigen Ordner aus und passen Sie dann die Tabellen- und Spaltennamen an:

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| Option | Wirkung |
|---|---|
| `--layout dashboard` | Filter in der Seitenleiste, zwei Kennzahlen auf einen Blick und ein Diagramm. |
| `--layout explorer` | Filter in der Seitenleiste, eine Zeilenanzahl und eine Tabelle mit Zeilen. |
| `--table` | Die PlaidCloud-Tabelle, die die App liest. |
| `--filters` | Durch Kommas getrennte Spalten, nach denen gefiltert wird. Die erste steuert das Diagramm. |
| `--measure` | Die numerische Spalte, die summiert wird. |
| `--dir` | Wohin `app.py` und `requirements.txt` geschrieben werden. Standard ist der aktuelle Ordner. |

Der Befehl bricht ab, ohne etwas zu schreiben, wenn `app.py` bereits existiert. Übertragen Sie die beiden Dateien per Commit in Ihr Repository und [veröffentlichen Sie es als Server-App](/de/guides/panel-apps/creating/#eine-server-app-erstellen).

## Eine Beispiel-App

Diese App filtert eine Verkaufstabelle nach Region und Jahr, zeigt zwei Kennzahlen auf einen Blick, ein Diagramm und ein Raster mit Seitenwechsel für die passenden Zeilen. Das Raster zeigt Beträge mit Tausendertrennzeichen und Margen als Prozentwerte. Jedes Element folgt den Filtern.

```python
import panel as pn
import plaidcloud_panel as pcp
from bokeh.plotting import figure
from plaidcloud.utilities.panel_data import table

pn.extension("tabulator")

sales = table("sales")
bar = pcp.FilterBar(sales, "region", "year")


def by_region(t):
    df = t.aggregate(by=["region"], total=("amount", "sum"))
    regions = df["region"].astype(str).tolist()
    fig = figure(x_range=regions, height=320, toolbar_location=None)
    fig.vbar(x=regions, top=df["total"].astype(float).tolist(), width=0.8, color=pcp.series()[0])
    return fig


def grid(t):
    return pcp.DataGrid(t, key="id", totals={"amount": "sum"}, formats={"amount": "0,0", "margin": "0.0%"})


pcp.App(
    "Sales",
    sidebar=[bar],
    main=[
        pn.Row(
            pcp.KpiCard("Total amount", bar.table, "amount"),
            pcp.KpiCard("Orders", bar.table),
        ),
        pcp.Chart(pn.bind(by_region, bar.table), title="Amount by region"),
        pcp.Section("Orders", pn.bind(grid, bar.table)),
    ],
).servable()
```

Das Muster ist in jeder Kit-App dasselbe: Erstellen Sie eine `FilterBar` über einer Tabelle und binden Sie dann jede Ansicht an `bar.table`. Eine Ansicht, die nicht an `bar.table` (oder an ein Widget) gebunden ist, wird bei Filteränderungen nie aktualisiert.

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)` erstellt die App-Shell: eine Kopfzeile mit dem Titel, dem Logo des Projekts und dem angemeldeten Benutzer, eine Seitenleiste und einen Hauptbereich. Rufen Sie `.servable()` für das Ergebnis auf.

- **Navigation** – übergeben Sie `nav=[("Overview", overview_page), ("Detail", detail_page)]`, um oben in der Seitenleiste ein Seitenmenü zu erhalten. Jede Seite ist ein Panel-Objekt oder eine Funktion, die eines zurückgibt. Funktionen werden ausgeführt, wenn die Seite ausgewählt wird.
- **Design** – die App öffnet sich im hellen Design. Übergeben Sie `theme="dark"`, um sie im dunklen Design zu öffnen, oder hängen Sie `?theme=dark` an die URL an. Mit `theme_toggle=True` (Standard) enthält die Kopfzeile einen Umschalter zwischen Hell und Dunkel.
- **Branding** – die App liest beim Start einer Sitzung die Markenfarben und das Logo ihres Projekts. Ein Projekt ohne Branding erhält die PlaidCloud-Standards.
- **Befehlspalette** – drücken Sie Strg-K (Cmd-K auf einem Mac), um Befehle zu suchen und auszuführen. Jede Seite in `nav` wird als **Gehe zu** und dem Seitennamen aufgeführt, und mit `commands={"Refresh data": refresh}` fügen Sie eigene Einträge hinzu, jeweils eine Bezeichnung und eine Funktion ohne Argumente. Wählen Sie einen Eintrag, und die App führt ihn aus.
- **Tour beim ersten Start** – `tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]` zeigt eine kurze Schritt-für-Schritt-Einführung, jeder Schritt mit einer Überschrift und einer Textzeile. Sie erscheint oben auf der Seite, bis Sie sie beenden oder überspringen, und wird Ihnen danach nicht mehr angezeigt.
- **Alles andere** – weitere Schlüsselwortargumente werden an Panels `FastListTemplate` weitergereicht.

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))` erstellt für jede genannte Spalte ein durchsuchbares Mehrfachauswahlfeld, das die eindeutigen Werte der Spalte auflistet (bis zu 1.000, mit einem Hinweis, wenn die Liste gekürzt wird). Ein Feld zeigt **Alle**, wenn nichts ausgewählt ist. Für alles andere übergeben Sie eigene Widgets nach Spaltennamen.

- `bar.table` ist die Tabelle, eingeschränkt durch die aktuelle Auswahl. Ein leeres Widget schränkt die Daten nicht ein.
- Auswahlen werden in der Seiten-URL gespeichert (`?region=EU`), sodass sich eine gefilterte Ansicht als Link teilen lässt.

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)` zeigt eine Kennzahl auf einen Blick. `fn` ist `sum`, `count`, `avg`, `min` oder `max`, vom Server über die gesamte Tabelle berechnet. Ohne `column` zeigt sie die Zeilenanzahl. Übergeben Sie `bar.table` als Quelle, damit die Zahl den Filtern folgt.

Übergeben Sie `drill_to=grid`, ein `DataGrid`, um unter der Zahl eine Schaltfläche **View rows** hinzuzufügen. Wenn Sie sie wählen, zeigt das Raster auf die eigene Tabelle der Karte, sodass es die Zeilen hinter der Zahl auflistet.

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})` ist eine Tabellenansicht für Daten beliebiger Größe. Nur die aktuelle Seite wird an den Browser gesendet; Seitenwechsel, Sortierung, Summen und Export laufen alle auf dem Server.

- **Seitenwechsel** – 200, 500 oder 1.000 Zeilen pro Seite, mit den Schaltflächen Previous und Next und einem Zeilenzähler.
- **Sortierung** – klicken Sie auf eine Spaltenüberschrift. Die Sortierung gilt für die gesamte Tabelle, nicht nur für die sichtbare Seite.
- **Summen** – `totals` ordnet einer Spalte `sum`, `count`, `avg`, `min` oder `max` zu. Der Server berechnet jede davon über alle passenden Zeilen und fixiert das Ergebnis als letzte Zeile des Rasters.
- **Export** – die Schaltflächen **CSV** und **XLSX** laden alle passenden Zeilen in der aktuellen Sortierung herunter, bis zu `export_cap` Zeilen (standardmäßig 100.000). Ist die Tabelle größer, weist ein Hinweis darauf hin, die Filter einzuengen. Vor Textzellen, die mit `=`, `+`, `-` oder `@` beginnen, wird ein Apostroph gesetzt, damit eine Tabellenkalkulation sie als Text liest.
- **Zahlenformate** – `formats={"margin": "0.0%", "amount": "0,0"}` legt pro Spalte ein Anzeigeformat fest, mit Formatzeichenfolgen von [numbro](https://numbrojs.com/format.html). Ein `%`-Format multipliziert mit 100. Die Summenzeile verwendet dasselbe Format. Float-Spalten ohne Format zeigen bis zu zwei Dezimalstellen mit Tausendertrennzeichen. **Kopieren**, **CSV** und **XLSX** behalten die Rohwerte bei.
- **Schlüssel** – `key` ist die Spalte oder Liste von Spalten, die eine Zeile eindeutig identifiziert. Übergeben Sie ihn immer. Siehe [Stabiler Seitenwechsel](/de/guides/panel-apps/data-api/#stabiler-seitenwechsel).

- **Gruppieren nach** – `group_by=["region"]` zeigt eine Zeile pro Gruppe, mit den `totals`-Messgrößen und einer `rows`-Anzahl, alle vom Server berechnet, sowie einer Zeile **Gesamt** über alle passenden Zeilen. Übergeben Sie `groupable=["region", "year"]`, um eine Auswahl **Gruppieren nach** hinzuzufügen, mit der Betrachter die Spalten wählen. Ein Raster zeigt bis zu 1.000 Gruppen und weist darauf hin, wenn es die Liste gekürzt hat. Gruppenzeilen haben keine **Öffnen**-Links.
- **Bedingte Formatierung** – `rules` färbt Zellen nach Wert. Jede Regel nennt eine `column`, einen `op` (`>`, `>=`, `<`, `<=`, `==`, `!=` oder `between`), einen `value` (`[low, high]` bei `between`) und ein `token` (`success`, `warning`, `error` oder `info`), zum Beispiel `{"column": "margin", "op": "<", "value": 0, "token": "error"}`. Die Summenzeile wird nie gefärbt.
- **Kopieren** – die Schaltfläche **Kopieren** legt die aktuelle Seite mit den sichtbaren Spalten und der Summenzeile als tabulatorgetrennten Text in die Zwischenablage, der sich in Excel einfügen lässt.
- **In PlaidCloud öffnen** – ist die Quelle eine PlaidCloud-Tabelle, öffnet ein Link **Open in PlaidCloud** diese Tabelle.
- **Gespeichertes Spaltenlayout** – `layout_key="orders"` fügt die Auswahlen **Spalten** und **Pinned** hinzu, um Spalten auszuwählen, zu ordnen und einige davon anzuheften. Die Auswahl jedes Betrachters wird unter diesem Namen gespeichert und beim nächsten Öffnen der App wiederhergestellt.
- **Zeilenlinks** – `row_link` ist eine Funktion, die eine Zeile als Dictionary entgegennimmt und eine Webadresse zurückgibt, oder `None` für keinen Link. Das Raster fügt eine Spalte **Öffnen** mit einem Link in jeder Zeile hinzu, die einen hat. Nur `http`- und `https`-Adressen sowie Pfade auf derselben Website werden verlinkt.
- **Aktualisieren** – `grid.refresh()` fragt dieselbe Quelle erneut ab und behält Seite, Sortierung und Gruppierung bei. Rufen Sie es auf, nachdem eine [Ausführung](#ausführungsschaltflächen-und-aktualität) das Schreiben der Tabelle beendet hat.

`source` ist ein Tabellenname oder eine Tabelle aus der [Data API](/de/guides/panel-apps/data-api/). Um ein Raster neu zu filtern, setzen Sie `grid.source` auf eine gefilterte Tabelle oder erstellen Sie wie im Beispiel ein neues Raster aus `bar.table`.

Für das Raster gilt die Sicherheit auf Zeilenebene des Betrachters: Es liest über die eigene Verbindung des Betrachters.

## Chart

`pcp.Chart(obj, title=None, height=320)` setzt ein Diagramm in eine Karte mit Titel. `obj` kann eine Bokeh-Figur, ein hvPlot- oder HoloViews-Plot, eine Plotly-Figur, eine Matplotlib-Figur oder ein `pn.bind(...)` sein, das eines davon zurückgibt. Numerische Achsen bei Bokeh-Figuren zeigen Tausendertrennzeichen, sodass 800000 als 800.000 erscheint.

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")` ordnet Eingabe-Widgets als ein Formular mit einer Absenden-Schaltfläche an. `form.values()` gibt `{widget.name: widget.value}` für jedes benannte Widget zurück, und `on_submit` erhält dieses Dictionary, wenn auf die Schaltfläche geklickt wird.

## Section, Card, Tabs und Loading

| Komponente | Verwendung |
|---|---|
| `pcp.Section(title, *objects)` | Eine Gruppe mit Titel direkt auf dem Seitenhintergrund. |
| `pcp.Card(title, *objects)` | Eine Gruppe mit Titel auf einer erhöhten Fläche. |
| `pcp.Tabs(Overview=obj, Detail=obj)` | Registerkarten, die den Inhalt einer Registerkarte laden, wenn sie ausgewählt wird. Die aktive Registerkarte übernimmt die Markenfarbe. |
| `pcp.Loading(height=200)` | Ein schimmernder Platzhalter, der beim Laden von Daten angezeigt wird. |

## StatusBanner

`pcp.StatusBanner(message, kind="info")` zeigt einen Inline-Hinweis. `kind` ist `error`, `warning`, `success` oder `info`.

## Ausführungsschaltflächen und Aktualität

`pcp.run_workflow_button(workflow_id, label=None)` fügt eine Schaltfläche hinzu, die einen PlaidCloud-Workflow als die Person ausführt, die die App geöffnet hat, und **Wird ausgeführt…** zeigt, dann **Fertig** oder **Fehlgeschlagen**. Bei einem Fehler werden die fehlgeschlagenen Schritte genannt, bis zu fünf. Der Workflow gehört zum Projekt der App, sofern Sie nicht `project_id` übergeben.

`pcp.RunButton(label, start, status)` leistet dasselbe für jeden beliebigen Job. `start` startet ihn und gibt eine Ausführungs-ID zurück; `status(run_id)` gibt `"running"`, `"succeeded"` oder `"failed"` zurück, oder `("failed", reason)`, um einen Grund anzuzeigen. Beides sind gewöhnliche Funktionen, etwa Aufrufe einer REST-API. Der Wert `runs` der Schaltfläche steigt jedes Mal um eins, wenn eine Ausführung erfolgreich ist, sodass sich eine Ansicht, die danach aktualisiert werden muss, daran bindet:

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)` zeigt, wann eine Tabelle zuletzt geschrieben wurde, als **Updated 5 min ago**. Das Alter läuft weiter, während die Seite geöffnet bleibt. Übergeben Sie `stale_after=datetime.timedelta(hours=24)`, um ältere Daten mit einer Warnung zu kennzeichnen, und rufen Sie nach einer Ausführung `.refresh()` auf. Eine Tabelle, die sich nicht datieren lässt, zeigt **Last update unknown**; das ist nie ein Fehler. `pcp.Freshness(fetch)` leistet dasselbe für jede Quelle, wobei `fetch` zurückgibt, wann sich die Daten zuletzt geändert haben.

## Gespeicherte Einstellungen

`pcp.user_state` merkt sich die Auswahl jeder Person zwischen Besuchen, sodass sich eine App so öffnet, wie sie verlassen wurde.

- `pcp.user_state.persist(widget, "region")` stellt den gespeicherten Wert im Widget wieder her und speichert ihn bei jeder Änderung. Ein gespeicherter Wert, den das Widget nicht mehr anbietet, wird ignoriert.
- Die in `nav` gewählte Seite wird automatisch gespeichert.
- Ein Schlüssel, der mit `filters.` beginnt, etwa `pcp.user_state.persist(widget, "filters.region")`, enthält eine Filterauswahl. PlaidCloud kürzt ihn bei jedem Lesen auf den aktuellen Zeilenzugriff der Person, sodass ein gespeicherter Filter nie Werte zurückbringt, die sie nicht mehr sehen darf.
- `pcp.user_state.get(key, default)` und `pcp.user_state.set(key, value)` speichern jeden anderen kleinen Wert.

Gespeicherte Einstellungen gehören einer Person in einer App und sind auf 8 KB begrenzt. Einstellungen werden nie zwischen Personen geteilt. Ist PlaidCloud beim Speichern einer Einstellung nicht erreichbar, behält die App sie bis zum Ende der Sitzung.

## Drucken und als PDF speichern

`pcp.PrintButton()` öffnet den Druckdialog des Browsers, in dem als Ziel **Als PDF speichern** gewählt werden kann. Die Seite wird mit ausgeblendeter Seitenleiste und ausgeblendeten Steuerelementen und mit dem Branding Ihres Projekts gedruckt. Jedes `DataGrid` druckt seine gesamte aktuelle Seite, bis zu 1.000 Zeilen, mit der Summenzeile zuletzt. Eine dunkle App druckt mit der hellen Palette.

## Sprachen

Die eigenen Texte des Kits, etwa Schaltflächen, Hinweise, die Befehlspalette, die Tour, Meldungen zu Ausführung und Aktualität sowie die Fußzeile des Rasters, erscheinen auf Englisch, Deutsch oder Französisch. Die Sprache ist `?lang=de` oder `?lang=fr` in der Seitenadresse, sonst die Sprache des Browsers. Zahlen verwenden die Trennzeichen der Sprache. Ihre Daten, Spaltennamen und alle von Ihnen geschriebenen Bezeichnungen werden nie übersetzt.

## Leistungsbudgets

Ein Seitenaufruf, dessen erste Darstellung länger als 3.000 ms dauert oder der eine Abfrage ausführt, die langsamer als 2.000 ms ist, schreibt eine Warnung in das Protokoll der App, die nennt, was die Grenze überschritten hat. Dieselben Werte erscheinen auf der Registerkarte **Einblicke** in [Panel Studio](/de/guides/panel-apps/studio/#erkenntnisse). Um für eine App andere Grenzwerte festzulegen, setzen Sie diese Umgebungsvariablen:

| Variable | Standard | Legt fest |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | Millisekunden bis zur ersten Darstellung. |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | Millisekunden für eine Abfrage. |

Ein Wert, der keine ganze Zahl ist, wird ignoriert, und der Standard gilt.

## Farben für eigene Diagramme

`pcp.series()` gibt die PlaidCloud-Diagrammpalette als Liste von Farben in der richtigen Reihenfolge zurück. Verwenden Sie sie, damit von Ihnen selbst gezeichnete Diagramme zu den eigenen Komponenten des Kits passen, wie das Beispiel es für das Balkendiagramm tut.

## Nächste Schritte

- [Die Data API](/de/guides/panel-apps/data-api/) – filtern, paginieren, zählen und aggregieren Sie PlaidCloud-Tabellen aus Ihrer App.
- [Warnungen und Digests](/de/guides/panel-apps/alerts-and-digests/) – senden Sie KPI-Warnungen und geplante Zusammenfassungen aus einer App.
- [Projekt-Branding](/de/guides/panel-apps/branding/) – legen Sie Ihre Farben und Ihr Logo einmal für jede App in einem Projekt fest.
