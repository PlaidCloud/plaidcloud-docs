---
title: Die Data API für Panel-Apps
description: Lesen Sie PlaidCloud-Tabellen aus einer Panel-App mit panel_data – filtern, paginieren, zählen und aggregieren Sie auf dem Server, als der angemeldete Betrachter, unter Anwendung der Sicherheit auf Zeilenebene.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/data-api.md
---

`plaidcloud.utilities.panel_data` ist der Weg, auf dem eine Server-Panel-App eine Tabelle liest, ohne die gesamte Tabelle in die App zu laden. Sie beschreiben, was Sie möchten – Zeilen, die bestimmte Filter erfüllen, eine Seite davon, eine Anzahl, eine gruppierte Summe –, und die Datenbank von PlaidCloud erledigt die Arbeit. Nur das Ergebnis kommt zur App zurück.

Jede Anfrage läuft als die Person, die die App ansieht, sodass deren Projektberechtigungen und [Sicherheit auf Zeilenebene](/de/guides/panel-apps/accessing-data/) für alles gelten, was zurückgegeben wird.

```python
from plaidcloud.utilities.panel_data import table

sales = table("sales")
```

`table(name)` öffnet eine Tabelle im Projekt der App, also dem Projekt, dem die App beim Veröffentlichen [zugewiesen wurde](/de/guides/panel-apps/branding/#eine-app-einem-projekt-zuweisen). Um eine Tabelle aus einem anderen Projekt zu lesen, übergeben Sie es: `table("sales", project="Finance")`. Das Projekt kann eine ID, ein Name oder ein Pfad sein.

Ein Tabellen-Handle ändert sich nie. `filter` gibt ein neues Handle zurück, sodass Sie das ungefilterte behalten und mehrere Ansichten daraus ableiten können.

## Filter

```python
emea = sales.filter(region="EMEA", year=[2025, 2026])
```

Jedes Schlüsselwort ist ein Spaltenname. Ein einzelner Wert trifft auf Zeilen zu, die ihm entsprechen. Eine Liste, ein Tupel oder ein Set trifft auf Zeilen zu, die einem beliebigen Element entsprechen. Mehrere Schlüsselwörter werden mit UND verknüpft, und ein erneuter Aufruf von `filter` für das Ergebnis fügt weitere Bedingungen hinzu.

Ein Wert von `None`, eine leere Zeichenfolge oder eine leere Liste lässt diese Spalte ungefiltert. Deshalb kann ein leeres Filter-Widget die Daten unberührt lassen: `sales.filter(**widget_values)` funktioniert, ohne vorher auf leere Werte zu prüfen.

Wenn Sie eine nicht vorhandene Spalte angeben, wird ein Fehler ausgelöst, der die Tabelle und die Spalte nennt.

## Page

```python
rows = emea.page(1, 200, sort=["-amount"], key="id")
```

`page(n, size, sort, key)` gibt Seite `n` (ab 1 gezählt) mit `size` Zeilen als pandas-Dataframe zurück.

- `sort` ist eine Liste von Spaltennamen. Stellen Sie einem Namen `-` voran, um absteigend zu sortieren: `["region", "-amount"]`.
- `key` ist die eindeutige Spalte oder die Liste eindeutiger Spalten der Tabelle. Übergeben Sie ihn immer.

### Stabiler Seitenwechsel

Der Seitenwechsel nimmt einen Ausschnitt aus einer geordneten Liste von Zeilen. Jede Anfrage ist eine eigene Abfrage. Wenn zwei Zeilen in den Sortierspalten gleichauf liegen, kann die Datenbank sie bei der nächsten Anfrage in anderer Reihenfolge zurückgeben, sodass eine Zeile in zwei Ausschnitten oder in keinem erscheinen kann. `key` schließt diese Lücke: PlaidCloud hängt ihn hinter Ihre Sortierspalten, sodass die Reihenfolge immer vollständig ist und jede Zeile in genau einem Ausschnitt landet.

Ohne `key` fällt der Seitenwechsel auf die Sortierung nach jeder Spalte zurück. Das ist bei einer breiten Tabelle langsam und bleibt instabil, wenn zwei Zeilen identisch sind. Übergeben Sie beim Seitenwechsel immer einen eindeutigen Schlüssel, und aus demselben Grund auch an [`DataGrid`](/de/guides/panel-apps/app-kit/#datagrid).

## Count

```python
total_rows = emea.count()
```

Gibt die Anzahl der Zeilen, die die Filter erfüllen, als ganze Zahl zurück.

## Aggregate

```python
by_region = sales.aggregate(by=["region"], total=("amount", "sum"), orders=("id", "count"))
grand_total = emea.aggregate(total=("amount", "sum"))
```

`aggregate(by=(), limit=1000, **measures)` gibt einen Dataframe mit einer Zeile pro Gruppe zurück, geordnet nach den `by`-Spalten. Jede Kennzahl hat die Form `name=(column, function)`, wobei die Funktion `sum`, `count`, `avg`, `min` oder `max` ist. Mindestens eine Kennzahl ist erforderlich.

Ohne `by` erhalten Sie eine einzelne Summenzeile über die gefilterten Zeilen. `limit` begrenzt die Anzahl der zurückgegebenen Gruppen.

Dezimalspalten können als Zeichenfolgen ankommen. Konvertieren Sie sie mit `float(...)` oder `astype(float)`, bevor Sie sie in Diagrammen darstellen oder formatieren.

## Alles zusammen

```python
import panel as pn
import plaidcloud_panel as pcp
from plaidcloud.utilities.panel_data import table

pn.extension("tabulator")

orders = table("orders")
bar = pcp.FilterBar(orders, "status")

pcp.App(
    "Orders",
    sidebar=[bar],
    main=[
        pcp.KpiCard("Open value", bar.table, "amount"),
        pn.bind(lambda t: pcp.DataGrid(t, key="order_id"), bar.table),
    ],
).servable()
```

`FilterBar`, `KpiCard` und `DataGrid` nehmen alle diese Tabellen-Handles entgegen, sodass die meisten Apps `page`, `count` oder `aggregate` nie direkt aufrufen. Verwenden Sie sie, wenn Sie eigene Ansichten erstellen. Siehe [Das Panel App Kit](/de/guides/panel-apps/app-kit/).

## Verwandte Themen

- [Daten lesen und der angemeldete Benutzer](/de/guides/panel-apps/accessing-data/) – als der Betrachter verbinden und wann Sie `PlaidConnection` direkt verwenden.
