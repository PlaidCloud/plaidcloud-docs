---
title: Data API dla aplikacji Panel
description: Odczytuj tabele PlaidCloud z aplikacji Panel za pomocą panel_data — filtruj, stronicuj, zliczaj i agreguj na serwerze, jako zalogowany przeglądający, z zastosowanymi zabezpieczeniami na poziomie wierszy.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/data-api.md
---

`plaidcloud.utilities.panel_data` to sposób, w jaki serwerowa aplikacja Panel odczytuje tabelę bez ładowania całej tabeli do aplikacji. Opisujesz, czego potrzebujesz — wierszy spełniających pewne filtry, jednej ich strony, liczby lub zgrupowanej sumy — a pracę wykonuje baza danych PlaidCloud. Do aplikacji wraca tylko wynik.

Każde żądanie jest wykonywane jako osoba przeglądająca aplikację, więc jej uprawnienia do projektu i [zabezpieczenia na poziomie wierszy](/pl/guides/panel-apps/accessing-data/) dotyczą wszystkiego, co zostanie zwrócone.

```python
from plaidcloud.utilities.panel_data import table

sales = table("sales")
```

`table(name)` otwiera tabelę w projekcie aplikacji, czyli w projekcie, do którego aplikacja została [przypisana](/pl/guides/panel-apps/branding/#przypisywanie-aplikacji-do-projektu) podczas publikowania. Aby odczytać tabelę z innego projektu, przekaż go: `table("sales", project="Finance")`. Projektem może być identyfikator, nazwa lub ścieżka.

Uchwyt tabeli nigdy się nie zmienia. `filter` zwraca nowy uchwyt, więc możesz zachować ten niefiltrowany i wyprowadzić z niego kilka widoków.

## Filter

```python
emea = sales.filter(region="EMEA", year=[2025, 2026])
```

Każdy argument nazwany to nazwa kolumny. Pojedyncza wartość dopasowuje wiersze jej równe. Lista, krotka lub zbiór dopasowuje wiersze równe dowolnemu elementowi. Kilka argumentów łączy się operatorem AND, a ponowne wywołanie `filter` na wyniku dodaje kolejne warunki.

Wartość `None`, pusty ciąg lub pusta lista pozostawia tę kolumnę niefiltrowaną. Dzięki temu pusty widżet filtra nie wpływa na dane: `sales.filter(**widget_values)` działa bez wcześniejszego sprawdzania pustych wartości.

Wskazanie kolumny, która nie istnieje, zgłasza błąd podający tabelę i kolumnę.

## Page

```python
rows = emea.page(1, 200, sort=["-amount"], key="id")
```

`page(n, size, sort, key)` zwraca stronę `n` (licząc od 1) liczącą `size` wierszy jako ramkę danych pandas.

- `sort` to lista nazw kolumn. Poprzedź nazwę znakiem `-`, aby uzyskać porządek malejący: `["region", "-amount"]`.
- `key` to unikatowa kolumna lub lista unikatowych kolumn tabeli. Zawsze ją przekazuj.

### Stabilne stronicowanie

Stronicowanie pobiera wycinek uporządkowanej listy wierszy. Każde żądanie to osobne zapytanie. Jeśli dwa wiersze mają identyczne wartości w kolumnach sortowania, baza danych może zwrócić je w innej kolejności przy następnym żądaniu, więc wiersz może pojawić się w dwóch wycinkach lub w żadnym. `key` zamyka tę lukę: PlaidCloud dodaje go po kolumnach sortowania, więc kolejność jest zawsze pełna, a każdy wiersz trafia dokładnie do jednego wycinka.

Bez `key` stronicowanie wraca do porządkowania według wszystkich kolumn. Jest to wolne w szerokiej tabeli i nadal niestabilne, jeśli dwa wiersze są identyczne. Przekazuj unikatowy klucz zawsze, gdy stronicujesz, i z tego samego powodu przekazuj go do [`DataGrid`](/pl/guides/panel-apps/app-kit/#datagrid).

## Count

```python
total_rows = emea.count()
```

Zwraca liczbę wierszy spełniających filtry jako liczbę całkowitą.

## Aggregate

```python
by_region = sales.aggregate(by=["region"], total=("amount", "sum"), orders=("id", "count"))
grand_total = emea.aggregate(total=("amount", "sum"))
```

`aggregate(by=(), limit=1000, **measures)` zwraca ramkę danych z jednym wierszem na grupę, uporządkowaną według kolumn `by`. Każda miara ma postać `name=(column, function)`, gdzie funkcją jest `sum`, `count`, `avg`, `min` lub `max`. Wymagana jest co najmniej jedna miara.

Bez `by` otrzymujesz pojedynczy wiersz sum dla przefiltrowanych wierszy. `limit` ogranicza liczbę zwracanych grup.

Kolumny dziesiętne mogą docierać jako ciągi znaków. Przekonwertuj je za pomocą `float(...)` lub `astype(float)`, zanim zwizualizujesz je na wykresie lub sformatujesz.

## Złożenie wszystkiego razem

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

`FilterBar`, `KpiCard` i `DataGrid` przyjmują te uchwyty tabel, więc większość aplikacji nigdy nie wywołuje bezpośrednio `page`, `count` ani `aggregate`. Używaj ich, gdy budujesz własne widoki. Zobacz [Zestaw narzędzi aplikacji Panel](/pl/guides/panel-apps/app-kit/).

## Powiązane

- [Odczyt danych i zalogowany użytkownik](/pl/guides/panel-apps/accessing-data/) — łączenie jako przeglądający oraz kiedy używać `PlaidConnection` bezpośrednio.
