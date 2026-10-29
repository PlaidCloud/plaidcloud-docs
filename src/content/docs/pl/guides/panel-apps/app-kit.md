---
title: Zestaw narzędzi aplikacji Panel
description: Twórz aplikacje Panel wyglądające jak PlaidCloud za pomocą zestawu plaidcloud_panel — powłoka App, paleta poleceń, FilterBar, KpiCard, DataGrid, Chart, Form, przyciski uruchamiania, zapisane ustawienia, drukowanie i tłumaczenia, w trybie jasnym i ciemnym.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

Każda serwerowa aplikacja Panel ma zainstalowany zestaw `plaidcloud_panel`. Nadaje on aplikacji wygląd PlaidCloud — te same kolory, typografię i odstępy co reszta platformy, w trybie jasnym i ciemnym — oraz udostępnia gotowe komponenty do ekranów, których potrzebuje większość aplikacji: filtrów, głównych liczb, dużej siatki danych, wykresów i formularzy. Aplikacja automatycznie przejmuje [branding swojego projektu](/pl/guides/panel-apps/branding/).

```python
import plaidcloud_panel as pcp
```

Zaimportowanie zestawu stosuje też wygląd PlaidCloud do wykresów Plotly i Matplotlib.

## Zacznij od szablonu

Zestaw zawiera polecenie, które zapisuje działającą aplikację startową. Uruchom je z dowolnego folderu, a następnie zmień nazwy tabeli i kolumn:

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| Opcja | Co robi |
|---|---|
| `--layout dashboard` | Filtry na pasku bocznym, dwie główne liczby i wykres. |
| `--layout explorer` | Filtry na pasku bocznym, liczba wierszy i tabela wierszy. |
| `--table` | Tabela PlaidCloud, którą odczytuje aplikacja. |
| `--filters` | Kolumny do filtrowania, oddzielone przecinkami. Pierwsza z nich steruje wykresem. |
| `--measure` | Kolumna liczbowa do zsumowania. |
| `--dir` | Gdzie zapisać `app.py` i `requirements.txt`. Domyślnie bieżący folder. |

Polecenie kończy działanie bez zapisywania czegokolwiek, jeśli `app.py` już istnieje. Zatwierdź oba pliki w repozytorium i [opublikuj aplikację](/pl/guides/panel-apps/creating/).

## Przykładowa aplikacja

Ta aplikacja filtruje tabelę sprzedaży według regionu i roku, pokazuje dwie główne liczby, wykres oraz siatkę ze stronicowaniem pasujących wierszy. Siatka pokazuje kwoty z separatorami tysięcy, a marże jako procenty. Każdy element podąża za filtrami.

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

Schemat jest taki sam w każdej aplikacji zestawu: zbuduj `FilterBar` nad tabelą, a następnie powiąż każdy widok z `bar.table`. Widok, który nie jest powiązany z `bar.table` (ani z widżetem), nigdy nie odświeża się po zmianie filtrów.

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)` buduje powłokę aplikacji: nagłówek z tytułem, logo projektu i zalogowanym użytkownikiem, pasek boczny oraz obszar główny. Wywołaj `.servable()` na wyniku.

- **Nawigacja** — przekaż `nav=[("Overview", overview_page), ("Detail", detail_page)]`, aby uzyskać menu stron u góry paska bocznego. Każda strona jest obiektem Panel lub funkcją zwracającą taki obiekt. Funkcje są uruchamiane po wybraniu strony.
- **Motyw** — aplikacja otwiera się w jasnym motywie. Przekaż `theme="dark"`, aby otworzyć ją w ciemnym motywie, lub dodaj `?theme=dark` do adresu URL. Przy `theme_toggle=True` (wartość domyślna) nagłówek zawiera przełącznik jasny/ciemny.
- **Branding** — aplikacja odczytuje kolory marki i logo swojego projektu na początku sesji. Projekt bez brandingu otrzymuje domyślne ustawienia PlaidCloud.
- **Paleta poleceń** — naciśnij Ctrl-K (Cmd-K na Macu), aby wyszukiwać i uruchamiać polecenia. Każda strona w `nav` jest wymieniona jako **Przejdź do** z nazwą strony, a `commands={"Refresh data": refresh}` dodaje własne pozycje, każdą jako etykietę i funkcję bez argumentów. Wybierz pozycję, a aplikacja ją wykona.
- **Wycieczka po pierwszym uruchomieniu** — `tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]` pokazuje krótkie wprowadzenie krok po kroku, w którym każdy krok to nagłówek i wiersz tekstu. Pojawia się u góry strony, dopóki go nie ukończysz lub nie pominiesz, i nie jest już więcej wyświetlane.
- **Wszystko inne** — pozostałe argumenty nazwane są przekazywane do `FastListTemplate` z Panel.

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))` tworzy jedno przeszukiwalne pole wielokrotnego wyboru dla każdej wskazanej kolumny, wypisując jej unikatowe wartości (do 1000, z informacją, gdy lista jest przycięta). Pole pokazuje **Wszystkie**, gdy nic nie jest wybrane. Dla wszystkiego innego przekaż własne widżety według nazwy kolumny.

- `bar.table` to tabela zawężona bieżącymi wyborami. Pusty widżet nie zawęża danych.
- Wybory są zapisywane w adresie URL strony (`?region=EU`), więc przefiltrowany widok można udostępnić jako łącze.

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)` pokazuje jedną główną liczbę. `fn` to `sum`, `count`, `avg`, `min` lub `max`, obliczane przez serwer dla całej tabeli. Bez `column` pokazuje liczbę wierszy. Przekaż `bar.table` jako źródło, aby liczba podążała za filtrami.

Przekaż `drill_to=grid`, czyli `DataGrid`, aby dodać pod liczbą przycisk **View rows**. Jego wybranie kieruje siatkę na tabelę karty, więc siatka wyświetla wiersze stojące za liczbą.

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})` to widok tabeli dla danych dowolnej wielkości. Do przeglądarki wysyłana jest tylko bieżąca strona; stronicowanie, sortowanie, sumy i eksport działają po stronie serwera.

- **Stronicowanie** — 200, 500 lub 1000 wierszy na stronę, z przyciskami Previous i Next oraz licznikiem wierszy.
- **Sortowanie** — kliknij nagłówek kolumny. Sortowanie dotyczy całej tabeli, a nie tylko widocznej strony.
- **Sumy** — `totals` mapuje kolumnę na `sum`, `count`, `avg`, `min` lub `max`. Serwer oblicza każdą z nich dla wszystkich pasujących wierszy i przypina wynik jako ostatni wiersz siatki.
- **Eksport** — przyciski **CSV** i **XLSX** pobierają wszystkie pasujące wiersze w bieżącej kolejności sortowania, do `export_cap` wierszy (domyślnie 100 000). Gdy tabela jest większa, komunikat informuje o konieczności zawężenia filtrów. Komórki tekstowe zaczynające się od `=`, `+`, `-` lub `@` są poprzedzane apostrofem, aby arkusz kalkulacyjny odczytał je jako tekst.
- **Formaty liczb** — `formats={"margin": "0.0%", "amount": "0,0"}` ustawia format wyświetlania dla każdej kolumny, przy użyciu ciągów formatu [numbro](https://numbrojs.com/format.html). Format `%` mnoży przez 100. Wiersz Total używa tego samego formatu. Kolumny zmiennoprzecinkowe bez formatu pokazują do dwóch miejsc po przecinku z separatorami tysięcy. **Kopiuj**, **CSV** i **XLSX** zachowują surowe wartości.
- **Klucz** — `key` to kolumna lub lista kolumn, które jednoznacznie identyfikują wiersz. Zawsze go przekazuj. Zobacz [Stabilne stronicowanie](/pl/guides/panel-apps/data-api/#stabilne-stronicowanie).

- **Grupuj według** — `group_by=["region"]` pokazuje jeden wiersz na grupę, z miarami z `totals` i liczbą `rows`, wszystko obliczone przez serwer, oraz wiersz **Razem** dla wszystkich pasujących wierszy. Przekaż `groupable=["region", "year"]`, aby dodać selektor **Grupuj według**, w którym przeglądający wybierają kolumny. Siatka pokazuje do 1000 grup i informuje, gdy przycięła listę. Wiersze grup nie mają łączy **Otwórz**.
- **Formatowanie warunkowe** — `rules` koloruje komórki według wartości. Każda reguła wskazuje `column`, `op` (`>`, `>=`, `<`, `<=`, `==`, `!=` lub `between`), `value` (`[low, high]` dla `between`) oraz `token` (`success`, `warning`, `error` lub `info`), na przykład `{"column": "margin", "op": "<", "value": 0, "token": "error"}`. Wiersz Total nigdy nie jest kolorowany.
- **Kopiowanie** — przycisk **Kopiuj** umieszcza w schowku bieżącą stronę, z widocznymi kolumnami i wierszem Total, jako tekst rozdzielony tabulatorami, który wkleja się do Excela.
- **Open in PlaidCloud** — gdy źródłem jest tabela PlaidCloud, łącze **Open in PlaidCloud** otwiera tę tabelę.
- **Zapisany układ kolumn** — `layout_key="orders"` dodaje selektory **Kolumny** i **Pinned** do wyboru i porządkowania kolumn oraz przypinania niektórych z nich. Wybór każdego przeglądającego jest zapisywany pod tą nazwą i przywracany przy następnym otwarciu aplikacji.
- **Łącza wierszy** — `row_link` to funkcja, która przyjmuje wiersz jako słownik i zwraca adres internetowy lub `None`, gdy łącza nie ma. Siatka dodaje kolumnę **Otwórz** z łączem w każdym wierszu, który je ma. Łączone są tylko adresy `http` i `https` oraz ścieżki w obrębie tej samej witryny.
- **Odśwież** — `grid.refresh()` ponownie wykonuje zapytanie do tego samego źródła i zachowuje stronę, sortowanie oraz grupowanie. Wywołaj go po tym, jak [uruchomienie](#przyciski-uruchamiania-i-aktualność) zakończy zapis tabeli.

`source` to nazwa tabeli lub tabela z [Data API](/pl/guides/panel-apps/data-api/). Aby ponownie przefiltrować siatkę, ustaw `grid.source` na przefiltrowaną tabelę lub zbuduj nową siatkę z `bar.table`, jak w przykładzie.

Siatka podlega zabezpieczeniom na poziomie wierszy przeglądającego: odczytuje dane przez jego własne połączenie.

## Chart

`pcp.Chart(obj, title=None, height=320)` umieszcza wykres w karcie z tytułem. `obj` może być figurą Bokeh, wykresem hvPlot lub HoloViews, figurą Plotly, figurą Matplotlib albo wywołaniem `pn.bind(...)`, które zwraca dowolną z nich. Osie liczbowe na figurach Bokeh pokazują separatory tysięcy, więc 800000 jest wyświetlane jako 800,000.

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")` układa widżety wejściowe w jeden formularz z przyciskiem zatwierdzania. `form.values()` zwraca `{widget.name: widget.value}` dla każdego nazwanego widżetu, a `on_submit` otrzymuje ten słownik po kliknięciu przycisku.

## Section, Card, Tabs i Loading

| Komponent | Do czego służy |
|---|---|
| `pcp.Section(title, *objects)` | Grupa z tytułem bezpośrednio na tle strony. |
| `pcp.Card(title, *objects)` | Grupa z tytułem na podniesionej powierzchni. |
| `pcp.Tabs(Overview=obj, Detail=obj)` | Karty, które ładują zawartość karty po jej wybraniu. Aktywna karta przyjmuje kolor marki. |
| `pcp.Loading(height=200)` | Migoczący element zastępczy do pokazania podczas ładowania danych. |

## StatusBanner

`pcp.StatusBanner(message, kind="info")` pokazuje komunikat w wierszu. `kind` to `error`, `warning`, `success` lub `info`.

## Przyciski uruchamiania i aktualność

`pcp.run_workflow_button(workflow_id, label=None)` dodaje przycisk, który uruchamia przepływ pracy PlaidCloud jako osoba, która otworzyła aplikację, i pokazuje **Running…**, a następnie **Gotowe** lub **Niepowodzenie**. Niepowodzenie wymienia kroki, które się nie powiodły, do pięciu. Przepływ pracy należy do projektu aplikacji, chyba że przekażesz `project_id`.

`pcp.RunButton(label, start, status)` robi to samo dla dowolnego zadania. `start` uruchamia je i zwraca identyfikator uruchomienia; `status(run_id)` zwraca `"running"`, `"succeeded"` lub `"failed"` albo `("failed", reason)`, aby pokazać przyczynę. Oba są zwykłymi funkcjami, na przykład wywołaniami REST API. Wartość `runs` przycisku rośnie o jeden po każdym udanym uruchomieniu, więc widok, który musi się potem odświeżyć, wiąże się z nią:

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)` pokazuje, kiedy tabela została ostatnio zapisana, jako **Updated 5 min ago**. Wiek aktualizuje się, gdy strona pozostaje otwarta. Przekaż `stale_after=datetime.timedelta(hours=24)`, aby oznaczyć starsze dane ostrzeżeniem, i wywołaj `.refresh()` po uruchomieniu. Tabela, której nie można datować, pokazuje **Last update unknown**; nigdy nie jest to błąd. `pcp.Freshness(fetch)` robi to samo dla dowolnego źródła, gdzie `fetch` zwraca czas ostatniej zmiany danych.

## Zapisane ustawienia

`pcp.user_state` zapamiętuje wybory każdej osoby między wizytami, więc aplikacja otwiera się tak, jak ją zostawiła.

- `pcp.user_state.persist(widget, "region")` przywraca zapisaną wartość do widżetu i zapisuje ją przy każdej zmianie. Zapisana wartość, której widżet już nie oferuje, jest ignorowana.
- Strona wybrana w `nav` jest zapisywana automatycznie.
- Klucz zaczynający się od `filters.`, na przykład `pcp.user_state.persist(widget, "filters.region")`, przechowuje wybór filtra. PlaidCloud przycina go do bieżącego dostępu danej osoby do wierszy przy każdym odczycie, więc zapisany filtr nigdy nie przywraca wartości, których osoba ta już nie widzi.
- `pcp.user_state.get(key, default)` i `pcp.user_state.set(key, value)` zapisują dowolną inną niewielką wartość.

Zapisane ustawienia należą do jednej osoby w jednej aplikacji, do 8 KB. Ustawienia nigdy nie są współdzielone między osobami. Jeśli podczas zapisu ustawienia PlaidCloud jest nieosiągalny, aplikacja przechowuje je do końca sesji.

## Drukowanie i zapis jako PDF

`pcp.PrintButton()` otwiera okno drukowania przeglądarki, w którym celem może być **Save as PDF**. Strona jest drukowana z ukrytym paskiem bocznym i kontrolkami oraz z zastosowanym brandingiem Twojego projektu. Każdy `DataGrid` drukuje całą swoją bieżącą stronę, do 1000 wierszy, z wierszem Total na końcu. Aplikacja w trybie ciemnym drukuje się z jasną paletą.

## Języki

Własny tekst zestawu, taki jak przyciski, komunikaty, paleta poleceń, wycieczka, komunikaty uruchamiania i aktualności oraz stopka siatki, pojawia się po angielsku, niemiecku lub francusku. Język określa `?lang=de` lub `?lang=fr` w adresie strony, a w przeciwnym razie język przeglądarki. Liczby używają separatorów danego języka. Twoje dane, nazwy kolumn i wszelkie etykiety, które sam piszesz, nigdy nie są tłumaczone.

## Budżety wydajności

Wczytanie strony, w którym pierwsze renderowanie trwa dłużej niż 3000 ms lub które wykonuje zapytanie wolniejsze niż 2000 ms, zapisuje w dzienniku aplikacji ostrzeżenie wskazujące, co przekroczyło limit. Te same wartości pojawiają się na karcie **Wgląd** w [Panel Studio](/pl/guides/panel-apps/studio/#wgląd). Aby ustawić inne limity dla aplikacji, ustaw te zmienne środowiskowe:

| Zmienna | Wartość domyślna | Co ustawia |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | Milisekundy do pierwszego renderowania. |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | Milisekundy dla jednego zapytania. |

Wartość niebędąca liczbą całkowitą jest ignorowana i obowiązuje wartość domyślna.

## Kolory dla własnych wykresów

`pcp.series()` zwraca paletę wykresów PlaidCloud jako listę kolorów, po kolei. Użyj jej, aby wykresy rysowane samodzielnie pasowały do własnych komponentów zestawu, jak w przykładzie dla wykresu słupkowego.

## Następne kroki

- [Data API](/pl/guides/panel-apps/data-api/) — filtruj, stronicuj, zliczaj i agreguj tabele PlaidCloud z poziomu aplikacji.
- [Alerty i podsumowania](/pl/guides/panel-apps/alerts-and-digests/) — wysyłaj alerty KPI i zaplanowane podsumowania z aplikacji.
- [Branding projektu](/pl/guides/panel-apps/branding/) — ustaw kolory i logo raz dla wszystkich aplikacji w projekcie.
