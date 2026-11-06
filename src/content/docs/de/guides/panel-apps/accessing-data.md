---
title: Daten lesen und der angemeldete Benutzer
description: Verbinden Sie eine serverseitige Panel-App mit PlaidCloud als die Person, die sie ansieht – lesen Sie Projektdaten und nutzen Sie die Identität des Betrachters für benutzerspezifisches Verhalten und Sicherheit auf Zeilenebene.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/accessing-data.md
---

Eine Server-Panel-App kann Ihre PlaidCloud-Daten lesen – und zwar **als die Person, die sie ansieht**. Wenn jemand die App öffnet, meldet PlaidCloud sie mit demselben Single Sign-on an, das auch der Rest der Plattform verwendet, und jeder Aufruf Ihrer App läuft mit **den eigenen Berechtigungen dieses Betrachters**. Es gibt kein gemeinsames Dienstkonto, und die App kann nie Daten sehen, die der Betrachter selbst nicht sehen könnte.

Dies gilt nur für **Server**-Apps. WASM-Apps laufen vollständig im Browser und haben keine serverseitige Verbindung.

## Mit PlaidCloud verbinden

Verwenden Sie `PlaidConnection` und nennen Sie das Projekt, dessen Daten Sie lesen möchten:

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection(project_id="<your-project-id>")
```

Mehr Einrichtung ist nicht nötig. Sie geben **kein** Token, keinen Benutzernamen und kein Kennwort an – die Verbindung authentifiziert sich automatisch als der angemeldete Betrachter. Die ID Ihres Projekts finden Sie in der URL des Projekts oder auf seiner Einstellungsseite.

> **Geben Sie Ihrem Projekt einen Namen.** Eine App, die mit einem Projekt in der Auswahl **Projekt** veröffentlicht wurde, liest dieses Projekt standardmäßig, und die [Data API](/de/guides/panel-apps/data-api/) verwendet es für `table("name")`. Übergeben Sie bei einer App ohne Projekt `project_id` wie oben an `PlaidConnection`; ein einfaches `PlaidConnection()` hat kein Projekt, das es lesen könnte.

### Eine Tabelle lesen

Mit einer Verbindung laden Sie eine Tabelle über ihren Namen in einen pandas-DataFrame:

```python
df = conn.get_dataframe("Sales Ledger")
```

Da die Verbindung der Betrachter ist, liefert dies nur die Zeilen, die der Betrachter sehen darf, und löst einen Berechtigungsfehler aus, wenn er überhaupt keinen Zugriff auf das Projekt hat.

> **Lesen Sie Tabellen über ihren Namen, nicht durch selbst geschriebenes SQL.** In einem Projekt, in dem ein Administrator [Zeilenzugriff](/de/administration/access/managing-security-groups-and-assignments/#zeilenzugriff-und-selbst-geschriebene-abfragen) aktiviert hat, wendet das Lesen über den Namen die Zeilenberechtigungen des jeweiligen Betrachters an, während eine Abfrage, die Ihre App selbst zusammenstellt, für alle abgelehnt wird, die nicht Architect des Projekts sind – es gibt keine einzelne Tabelle, auf die sich die Berechtigungen als Filter anwenden ließen. Wenn Sie über den Namen lesen, funktioniert Ihre App in beiden Fällen.

## Den Betrachter identifizieren

Wenn Sie anpassen möchten, was die App anzeigt, je nachdem, **wer sie ansieht** – etwa eine persönliche Begrüßung, das Ausblenden einer Registerkarte oder Sicherheit auf Zeilenebene –, lesen Sie den angemeldeten Benutzer aus Panel:

```python
import panel as pn

viewer = pn.state.user          # the viewer's email address
token  = pn.state.access_token  # their JWT, if you need claims or group membership
```

`pn.state.user` ist die E-Mail-Adresse des Betrachters aus seiner verifizierten Anmeldung – Sie können sie als seine Identität betrachten. `pn.state.access_token` ist sein unverarbeitetes Zugriffstoken, nützlich, wenn Sie Gruppen- oder Rollenansprüche für feinere Regeln auswerten müssen.

### Sicherheit auf Zeilenebene

Kombinieren Sie beides: Lesen Sie den Betrachter und filtern Sie dann jede Abfrage nach ihm. So sieht zum Beispiel jeder Regionalleiter nur seine eigene Region:

```python
import panel as pn
from plaidcloud.utilities.connect import PlaidConnection

pn.extension()

viewer = pn.state.user
conn = PlaidConnection(project_id="<your-project-id>")

sales = conn.get_dataframe("Regional Sales")
mine = sales[sales["manager_email"] == viewer]

pn.Column(
    f"# Sales for {viewer}",
    pn.pane.DataFrame(mine, index=False),
).servable()
```

Da die Verbindung bereits die Projektberechtigungen des Betrachters durchsetzt, ist dieses Filtern eine *zusätzliche* Eingrenzung dessen, was er sehen darf – und kein Ersatz für die Zugriffskontrolle von PlaidCloud selbst.

> **Führen Sie Datenaufrufe im Hauptablauf der App aus.** Der angemeldete Betrachter steht zur Verfügung, solange der Code Ihrer App für seine Sitzung läuft (dort findet die Arbeit mit `.servable()` statt). Wenn Sie einen blockierenden Aufruf in einen Hintergrund-Thread verlagern, verwenden Sie `asyncio.to_thread` – ein einfacher Thread-Pool übernimmt die Identität der Sitzung nicht, und die Verbindung schlägt mit einem deutlichen Fehler fehl, statt die falschen Daten zu lesen.

## Öffentliche Apps

Wenn Sie mit **Öffentlichen Zugriff zulassen** veröffentlicht haben, wird die App ohne Anmeldung bereitgestellt. Es gibt dann keinen Betrachter, als der gehandelt werden könnte – `pn.state.user` ist leer, und eine `PlaidConnection()` hat niemanden, als den sie sich authentifizieren könnte. Beschränken Sie öffentliche Apps auf Daten, die für jeden unbedenklich sind, oder lassen Sie den öffentlichen Zugriff deaktiviert, damit sich Betrachter anmelden und das oben beschriebene benutzerbezogene Modell gilt.
