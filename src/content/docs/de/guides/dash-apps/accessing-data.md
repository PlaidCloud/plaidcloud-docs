---
title: Daten und angemeldeten Benutzer in einer Dash-App lesen
description: Verbinden Sie eine Dash-App mit PlaidCloud als die Person, die sie gerade ansieht – lesen Sie Projektdaten und nutzen Sie die Identität des Betrachters für benutzerspezifisches Verhalten und Sicherheit auf Zeilenebene.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/accessing-data.md
---

Eine Dash-App kann Ihre PlaidCloud-Daten lesen – und zwar **als die Person, die sie ansieht**, genau wie eine serverseitige Panel-App. Wenn jemand die App öffnet, meldet PlaidCloud ihn mit demselben Single Sign-on an, das die übrige Plattform verwendet, und jeder Aufruf Ihrer App wird mit den **eigenen Berechtigungen dieses Betrachters** ausgeführt. Es gibt kein gemeinsames Dienstkonto, und die App kann nie Daten sehen, die der Betrachter selbst nicht sehen könnte.

Die Hilfsfunktionen befinden sich in `plaidcloud_dash`, das Teil des Dash-Basisimages ist:

```python
from plaidcloud_dash import current_user, get_connection
```

## Mit PlaidCloud verbinden

Rufen Sie `get_connection()` innerhalb eines Dash-Callbacks auf und geben Sie das Projekt an, dessen Daten Sie lesen möchten:

```python
from plaidcloud_dash import get_connection

conn = get_connection(project_id="<your-project-id>")
```

Mehr Einrichtung ist nicht nötig. Sie geben **kein** Token, keinen Benutzernamen und kein Passwort an – `get_connection()` authentifiziert sich automatisch als der angemeldete Betrachter, mit dem Zugriffstoken seiner aktuellen Sitzung. Die ID Ihres Projekts finden Sie in der URL des Projekts oder auf seiner Einstellungsseite.

> **Rufen Sie die Funktion innerhalb eines Callbacks auf.** `get_connection()` liest das Token des Betrachters aus der Flask-Sitzung der aktuellen Anfrage. Diese steht nur zur Verfügung, solange ein Callback die Anfrage dieses Betrachters verarbeitet. Wenn Sie einen blockierenden Aufruf an einen Hintergrund-Thread übergeben, überträgt ein einfacher Thread-Pool die Sitzung nicht – lesen Sie das Token stattdessen im Callback und übergeben Sie es explizit. Ein Aufruf von `get_connection()` außerhalb einer Anfrage (oder bei deaktivierter Authentifizierung) löst einen `RuntimeError` aus, statt stillschweigend eine Verbindung ohne dahinterstehende Identität zurückzugeben.

> **Geben Sie Ihr Projekt im Code an.** Im Veröffentlichungsdialog gibt es keine Projekteinstellung – eine Dash-App liest das Projekt, das Sie in `get_connection(project_id=...)` angeben, genau wie `PlaidConnection(project_id=...)` bei einer serverseitigen Panel-App – siehe [Daten und angemeldeten Benutzer lesen](/de/guides/panel-apps/accessing-data/). Ein einfaches `get_connection()` ohne `project_id` ist für eine App in Ordnung, die nie auf Projektdaten zugreift (etwa eine, die nur `current_user()` aufruft). Rufen Sie jedoch auf dieser Verbindung einen projektbezogenen Vorgang ohne gültige, zugängliche Projekt-ID auf, wird `Project Id has not been set` ausgelöst. (Um aus mehreren Projekten zu lesen, öffnen Sie pro Projekt eine Verbindung.)

### Eine Tabelle lesen

Mit einer Verbindung laden Sie eine Tabelle anhand ihres Namens in einen pandas-DataFrame:

```python
df = conn.get_dataframe("Sales Ledger")
```

Da die Verbindung der Betrachter ist, werden nur die Zeilen zurückgegeben, die der Betrachter sehen darf; hat er keinen Zugriff auf das Projekt, wird ein Berechtigungsfehler ausgelöst.

> **Lesen Sie Tabellen anhand des Namens, schreiben Sie keine SQL-Abfragen.** In einem Projekt, in dem ein Administrator [Zeilenzugriff](/de/administration/access/managing-security-groups-and-assignments/#zeilenzugriff-und-selbst-geschriebene-abfragen) aktiviert hat, wendet das Lesen per Namen die Zeilenberechtigungen des jeweiligen Betrachters an, während eine von Ihrer App selbst zusammengestellte Abfrage für alle abgelehnt wird, die nicht Projekt-Architect sind – es gibt keine einzelne Tabelle, auf die die Berechtigungen als Filter wirken könnten. Wenn Sie per Namen lesen, funktioniert Ihre App in beiden Fällen.

## In einem Callback lesen, nie beim Import oder im Prozessbereich

Ein Prozess bedient alle Betrachter. Für die richtige Datentrennung gelten zwei Regeln:

- **Öffnen Sie nie eine Verbindung und lesen Sie nie eine Tabelle im Modulbereich (beim Import).** Ihre `app.py` und alle Module, die sie importiert, werden **einmal** ausgeführt, wenn der Container startet – bevor sich irgendjemand angemeldet hat. Ein `get_connection()` oder `PlaidConnection()` an dieser Stelle hat keinen Betrachter, als den es sich authentifizieren könnte, und lässt die App beim Start scheitern (das ist die häufigste Ursache für eine Absturzschleife mit „App wurde nicht gestartet“). Halten Sie jeden Lesezugriff innerhalb eines Callbacks, wo die Anfrage eines Betrachters – und damit sein Sitzungstoken – vorhanden ist.

- **Speichern Sie nie ein benutzerspezifisches Ergebnis im Modul- oder Prozessbereich zwischen.** Der Gunicorn-Worker mit Threads teilt sich einen Python-Prozess über alle gleichzeitigen Betrachter hinweg. Ein DataFrame, den Sie in einer Variablen auf Modulebene, einem globalen Dictionary oder einem `lru_cache` ablegen, ist daher für *jeden* anderen Betrachter sichtbar – die Zeilen einer Person landen in der Ansicht einer anderen. Berechnen Sie benutzerspezifische Daten innerhalb des Callbacks und lassen Sie sie den Gültigkeitsbereich verlassen, wenn der Callback zurückkehrt:

  ```python
  # WRONG — a module/process-global cache is shared across all viewers
  _CACHE = {}

  @app.callback(...)
  def _load(n):
      viewer = current_user()
      if viewer not in _CACHE:                      # still process-global; leaks under load
          _CACHE[viewer] = get_connection(project_id="…").get_dataframe("Sales")
      return _CACHE[viewer].to_dict("records")

  # RIGHT — read inside the callback, no shared state
  @app.callback(...)
  def _load(n):
      conn = get_connection(project_id="…")          # this viewer, this request
      return conn.get_dataframe("Sales").to_dict("records")
  ```

### Gemeinsame Referenzdaten

Wenn mehrere Betrachter tatsächlich *dieselben* Referenzdaten benötigen – eine Nachschlagetabelle, eine Produktliste –, versuchen Sie nicht, sie über einen Cache auf Prozessebene zu teilen. Erteilen Sie den Benutzern der App den Zugriff auf diese Tabellen über die normalen [Zeilenzugriffs- bzw. Projektberechtigungen](/de/administration/access/managing-security-groups-and-assignments/) von PlaidCloud und lassen Sie jeden Betrachter sie mit seinem eigenen `get_connection()` lesen. Alle erhalten dieselben Referenzzeilen, weil alle denselben Zugriff haben – nicht weil der Lesezugriff eines Betrachters für einen anderen wiederverwendet wird.

## Den Betrachter identifizieren

Um darzustellen, was die App **je nach Betrachter** zeigt – eine persönliche Begrüßung, eine ausgeblendete Registerkarte oder Sicherheit auf Zeilenebene –, rufen Sie `current_user()` auf:

```python
from plaidcloud_dash import current_user

viewer = current_user()  # the viewer's identifier
```

`current_user()` gibt die Kennung des angemeldeten Betrachters zurück – seinen Benutzernamen, ersatzweise seine E-Mail-Adresse und dann seine Konto-ID, falls kein Benutzername-Claim vorhanden ist. Sie stammt aus seiner verifizierten Anmeldung, sodass Sie sie als seine Identität verwenden können. Die Funktion löst nie eine Ausnahme aus; bei deaktivierter Authentifizierung oder außerhalb einer Anfrage gibt sie eine leere Zeichenfolge zurück.

### Sicherheit auf Zeilenebene

Kombinieren Sie beides: Lesen Sie den Betrachter und filtern Sie dann jede Abfrage nach ihm. So zeigen Sie beispielsweise jedem Regionalleiter nur seine eigene Region:

```python
from dash import Input, Output
from plaidcloud_dash import current_user, get_connection


@app.callback(Output("sales-table", "children"), Input("load-btn", "n_clicks"))
def _load_my_region(n_clicks):
    viewer = current_user()
    conn = get_connection(project_id="<your-project-id>")

    sales = conn.get_dataframe("Regional Sales")
    mine = sales[sales["manager_email"] == viewer]

    return mine.to_dict("records")
```

Da die Verbindung die Projektberechtigungen des Betrachters bereits durchsetzt, ist dieses Filtern eine *zusätzliche* Eingrenzung dessen, was er sehen darf – kein Ersatz für die eigene Zugriffssteuerung von PlaidCloud.

## Öffentliche Apps

Wenn Sie mit **Öffentlichen Zugriff zulassen** veröffentlicht haben, wird die App ohne Anmeldung bereitgestellt. Es gibt also keinen Betrachter, als den sie handeln könnte – `current_user()` gibt eine leere Zeichenfolge zurück, und `get_connection()` hat kein Sitzungstoken zur Authentifizierung und löst daher eine Ausnahme aus. Beschränken Sie öffentliche Apps auf Daten, die für jeden unbedenklich sind, oder lassen Sie den öffentlichen Zugriff deaktiviert, damit sich Betrachter anmelden und das oben beschriebene benutzerspezifische Modell gilt.
