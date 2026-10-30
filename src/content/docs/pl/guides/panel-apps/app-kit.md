---
title: Zestaw Panel App Kit
description: Twórz aplikacje Panel wyglądające jak PlaidCloud za pomocą zestawu plaidcloud_panel — powłoka App, paleta poleceń, FilterBar, KpiCard, DataGrid, Chart, Form, przyciski uruchamiania, zapisane ustawienia, drukowanie i tłumaczenia, w trybie jasnym i ciemnym.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

Każda serwerowa aplikacja Panel ma zainstalowany zestaw `plaidcloud_panel`. Nadaje on aplikacji wygląd PlaidCloud — te same kolory, krój pisma i odstępy co w pozostałej części platformy, w trybie jasnym i ciemnym — oraz udostępnia gotowe komponenty do ekranów, których potrzebuje większość aplikacji: filtrów, głównych liczb, dużej siatki danych, wykresów i formularzy. Aplikacja automatycznie przejmuje [branding projektu](/pl/guides/panel-apps/branding/).

```python
import plaidcloud_panel as pcp
```

Zaimportowanie zestawu stosuje też wygląd PlaidCloud do wykresów Plotly i Matplotlib.

## Zacznij od szablonu

W [Panel Studio](/pl/guides/panel-apps/studio/) opcja **Nowa aplikacja Studio** zaczyna od pustej aplikacji, tabeli lub widoku, innej aplikacji Studio albo aplikacji z [galerii](/pl/guides/panel-apps/gallery/), bez żadnego polecenia do uruchomienia.

Dla aplikacji przechowywanej w repozytorium git zestaw zawiera polecenie, które zapisuje działającą aplikację startową. Uruchom je z dowolnego folderu, a następnie zmień nazwy tabel i kolumn:

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
| `--dir` | Miejsce zapisu `app.py` i `requirements.txt`. Domyślnie bieżący folder. |

Polecenie kończy działanie bez zapisywania czegokolwiek, jeśli `app.py` już istnieje. Zatwierdź oba pliki w repozytorium i [opublikuj je jako aplikację serwerową](/pl/guides/panel-apps/creating/#tworzenie-aplikacji-serwerowej).

## Przykładowa aplikacja

Ta aplikacja filtruje tabelę sprzedaży według regionu i roku, pokazuje dwie główne liczby, wykres oraz siatkę z podziałem na strony pasujących wierszy. Siatka pokazuje kwoty z separatorami tysięcy, a marże jako procenty. Każdy element podąża za filtrami.

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

Wzorzec jest taki sam w każdej aplikacji korzystającej z zestawu: zbuduj `FilterBar` nad tabelą, a następnie powiąż każdy widok z `bar.table`. Widok niepowiązany z `bar.table` (ani z widżetem) nigdy się nie odświeża po zmianie filtrów.

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)` buduje powłokę aplikacji: nagłówek z tytułem, logo projektu i zalogowanym użytkownikiem, pasek boczny oraz obszar główny. Wywołaj `.servable()` na wyniku.

- **Nawigacja** — przekaż `nav=[("Overview", overview_page), ("Detail", detail_page)]`, aby uzyskać menu stron u góry paska bocznego. Każda strona to obiekt Panel albo funkcja, która go zwraca. Funkcje są uruchamiane po wybraniu strony.
- **Motyw** — aplikacja otwiera się w jasnym motywie. Przekaż `theme="dark"`, aby otworzyć ją w ciemnym motywie, albo dodaj `?theme=dark` do adresu URL. Przy `theme_toggle=True` (domyślnie) nagłówek zawiera przełącznik jasny/ciemny.
- **Branding** — aplikacja odczytuje kolory marki i logo swojego projektu na początku sesji. Projekt bez brandingu dostaje domyślne ustawienia PlaidCloud.
- **Paleta poleceń** — naciśnij Ctrl-K (Cmd-K na Macu), aby wyszukiwać i uruchamiać polecenia. Każda strona z `nav` jest wymieniona jako **Przejdź do** nazwy strony, a `commands={"Refresh data": refresh}` dodaje własne pozycje, każdą jako etykietę i funkcję bez argumentów. Wybierz pozycję, a aplikacja ją uruchomi.
- **Przewodnik przy pierwszym uruchomieniu** — `tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]` pokazuje krótkie wprowadzenie krok po kroku, każdy krok to nagłówek i wiersz tekstu. Pojawia się na górze strony, dopóki go nie ukończysz lub nie pominiesz, i nie jest już pokazywany ponownie.
- **Wszystko inne** — pozostałe argumenty nazwane są przekazywane do `FastListTemplate` Panel.

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))` tworzy jedno przeszukiwalne pole wielokrotnego wyboru dla każdej wskazanej kolumny, wyświetlające unikatowe wartości tej kolumny (do 1000, z komunikatem, gdy lista została obcięta). Gdy nic nie jest wybrane, pole pokazuje **Wszystkie**. Dla pozostałych przypadków przekaż własne widżety według nazwy kolumny.

- `bar.table` to tabela zawężona bieżącymi wyborami. Pusty widżet nie zawęża danych.
- Wybory są zapisywane w adresie URL strony (`?region=EU`), więc przefiltrowany widok można udostępnić jako link.

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)` pokazuje jedną główną liczbę. `fn` to `sum`, `count`, `avg`, `min` lub `max`, obliczane przez serwer dla całej tabeli. Bez `column` pokazuje liczbę wierszy. Przekaż `bar.table` jako źródło, aby liczba podążała za filtrami.

Przekaż `drill_to=grid`, czyli `DataGrid`, aby dodać przycisk **View rows** pod liczbą. Jego wybranie kieruje siatkę na tabelę samej karty, więc siatka wyświetla wiersze stojące za liczbą.

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})` to widok tabeli dla danych o dowolnym rozmiarze. Do przeglądarki wysyłana jest tylko bieżąca strona; podział na strony, sortowanie, sumy i eksport są wykonywane na serwerze.

- **Podział na strony** — 200, 500 lub 1000 wierszy na stronę, z przyciskami Poprzednia i Następna oraz licznikiem wierszy.
- **Sortowanie** — kliknij nagłówek kolumny. Sortowanie dotyczy całej tabeli, nie tylko widocznej strony.
- **Sumy** — `totals` przypisuje kolumnie `sum`, `count`, `avg`, `min` lub `max`. Serwer oblicza każdą z nich dla wszystkich pasujących wierszy i przypina wynik jako ostatni wiersz siatki.
- **Eksport** — przyciski **CSV** i **XLSX** pobierają wszystkie pasujące wiersze w bieżącym sortowaniu, do `export_cap` wierszy (domyślnie 100 000). Gdy tabela jest większa, komunikat każe zawęzić filtry. Komórki tekstowe zaczynające się od `=`, `+`, `-` lub `@` są poprzedzane apostrofem, aby arkusz kalkulacyjny odczytał je jako tekst.
- **Formaty liczb** — `formats={"margin": "0.0%", "amount": "0,0"}` ustawia format wyświetlania dla kolumny, używając ciągów formatu [numbro](https://numbrojs.com/format.html). Format `%` mnoży przez 100. Wiersz sumy używa tego samego formatu. Kolumny zmiennoprzecinkowe bez formatu pokazują do dwóch miejsc po przecinku z separatorami tysięcy. **Kopiuj**, **CSV** i **XLSX** zachowują surowe wartości.
- **Klucz** — `key` to kolumna lub lista kolumn, które jednoznacznie identyfikują wiersz. Zawsze go przekazuj. Zobacz [Stabilny podział na strony](/pl/guides/panel-apps/data-api/#stabilne-stronicowanie).

- **Grupuj według** — `group_by=["region"]` pokazuje jeden wiersz na grupę, z miarami `totals` i liczbą `rows`, wszystko obliczane przez serwer, oraz wiersz **Razem** dla wszystkich pasujących wierszy. Przekaż `groupable=["region", "year"]`, aby dodać selektor **Grupuj według**, w którym oglądający wybierają kolumny. Siatka pokazuje do 1000 grup i informuje, gdy obcięła listę. Wiersze grup nie mają linków **Otwórz**.
- **Formatowanie warunkowe** — `rules` koloruje komórki według wartości. Każda reguła wskazuje `column`, `op` (`>`, `>=`, `<`, `<=`, `==`, `!=` lub `between`), `value` (`[low, high]` dla `between`) i `token` (`success`, `warning`, `error` lub `info`), na przykład `{"column": "margin", "op": "<", "value": 0, "token": "error"}`. Wiersz Razem nigdy nie jest kolorowany.
- **Kopiuj** — przycisk **Kopiuj** umieszcza w schowku bieżącą stronę, z widocznymi kolumnami i wierszem Razem, jako tekst rozdzielany tabulatorami, który można wkleić do Excela.
- **Otwórz w PlaidCloud** — gdy źródłem jest tabela PlaidCloud, link **Open in PlaidCloud** otwiera tę tabelę.
- **Zapisany układ kolumn** — `layout_key="orders"` dodaje selektory **Kolumny** i **Pinned** do wybierania i porządkowania kolumn oraz przypinania niektórych z nich. Wybór każdego oglądającego jest zapisywany pod tą nazwą i przywracany przy następnym otwarciu aplikacji.
- **Linki wierszy** — `row_link` to funkcja, która przyjmuje wiersz jako słownik i zwraca adres internetowy albo `None`, gdy nie ma linku. Siatka dodaje kolumnę **Otwórz** z linkiem w każdym wierszu, który go ma. Linkowane są tylko adresy `http` i `https` oraz ścieżki w obrębie tej samej witryny.
- **Odśwież** — `grid.refresh()` ponownie wykonuje zapytanie do tego samego źródła i zachowuje stronę, sortowanie i grupowanie. Wywołaj go po tym, jak [uruchomienie](#przyciski-uruchamiania-i-aktualność) zakończy zapis tabeli.

`source` to nazwa tabeli albo tabela z [Data API](/pl/guides/panel-apps/data-api/). Aby ponownie przefiltrować siatkę, ustaw `grid.source` na przefiltrowaną tabelę lub zbuduj nową siatkę z `bar.table`, jak w przykładzie.

Siatka podlega zabezpieczeniom na poziomie wierszy oglądającego: odczytuje dane przez jego własne połączenie.

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

`pcp.StatusBanner(message, kind="info")` pokazuje wbudowany komunikat. `kind` to `error`, `warning`, `success` lub `info`.

## Przyciski uruchamiania i aktualność

`pcp.run_workflow_button(workflow_id, label=None)` dodaje przycisk, który uruchamia przepływ pracy PlaidCloud jako osoba, która otworzyła aplikację, i pokazuje **Uruchomiony…**, a następnie **Gotowe** lub **Niepowodzenie**. Niepowodzenie wymienia kroki, które się nie powiodły, do pięciu. Przepływ pracy należy do projektu aplikacji, chyba że przekażesz `project_id`.

`pcp.RunButton(label, start, status)` robi to samo dla dowolnego zadania. `start` je uruchamia i zwraca identyfikator uruchomienia; `status(run_id)` zwraca `"running"`, `"succeeded"` lub `"failed"` albo `("failed", reason)`, aby pokazać przyczynę. Obie są zwykłymi funkcjami, na przykład wywołaniami REST API. Wartość `runs` przycisku rośnie o jeden przy każdym udanym uruchomieniu, więc widok, który musi się potem odświeżyć, wiąże się z nią:

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)` pokazuje, kiedy tabela była ostatnio zapisywana, jako **Updated 5 min ago**. Wiek zmienia się, gdy strona pozostaje otwarta. Przekaż `stale_after=datetime.timedelta(hours=24)`, aby oznaczyć starsze dane ostrzeżeniem, i wywołaj `.refresh()` po uruchomieniu. Tabela, której nie można datować, pokazuje **Last update unknown**; nigdy nie jest to błąd. `pcp.Freshness(fetch)` robi to samo dla dowolnego źródła, gdzie `fetch` zwraca czas ostatniej zmiany danych.

## Zapisane ustawienia

`pcp.user_state` zapamiętuje wybory każdej osoby między wizytami, dzięki czemu aplikacja otwiera się tak, jak ją zostawiła.

- `pcp.user_state.persist(widget, "region")` przywraca zapisaną wartość do widżetu i zapisuje ją przy każdej zmianie. Zapisana wartość, której widżet już nie oferuje, jest ignorowana.
- Strona wybrana w `nav` jest zapisywana automatycznie.
- Klucz zaczynający się od `filters.`, na przykład `pcp.user_state.persist(widget, "filters.region")`, przechowuje wybór filtru. PlaidCloud przycina go do bieżącego dostępu do wierszy danej osoby przy każdym odczycie, więc zapisany filtr nigdy nie przywraca wartości, których osoba już nie widzi.
- `pcp.user_state.get(key, default)` i `pcp.user_state.set(key, value)` zapisują każdą inną małą wartość.

Zapisane ustawienia należą do jednej osoby w jednej aplikacji, do 8 KB. Ustawienia nigdy nie są współdzielone między osobami. Jeśli w chwili zapisu ustawienia nie można połączyć się z PlaidCloud, aplikacja zachowuje je do końca sesji.

## Drukowanie i zapis jako PDF

`pcp.PrintButton()` otwiera okno drukowania przeglądarki, w którym miejscem docelowym może być **Zapisz jako PDF**. Strona jest drukowana z ukrytym paskiem bocznym i kontrolkami oraz z zastosowanym brandingiem Twojego projektu. Każdy `DataGrid` drukuje całą swoją bieżącą stronę, do 1000 wierszy, z wierszem Razem na końcu. Ciemna aplikacja drukuje się w jasnej palecie.

## Języki

Własny tekst zestawu, taki jak przyciski, komunikaty, paleta poleceń, przewodnik, komunikaty o uruchomieniach i aktualności oraz stopka siatki, pojawia się po angielsku, niemiecku lub francusku. Język jest określany przez `?lang=de` lub `?lang=fr` w adresie strony, a w przeciwnym razie przez język przeglądarki. Liczby używają separatorów danego języka. Twoje dane, nazwy kolumn i etykiety, które piszesz, nigdy nie są tłumaczone.

## Budżety wydajności

Ładowanie strony, w którym pierwsze wyrenderowanie trwa dłużej niż 3000 ms lub które uruchamia zapytanie wolniejsze niż 2000 ms, zapisuje w dzienniku aplikacji ostrzeżenie wskazujące, co przekroczyło limit. Te same wartości pojawiają się na karcie **Wgląd** w [Panel Studio](/pl/guides/panel-apps/studio/#wgląd). Aby ustawić inne limity dla aplikacji, ustaw te zmienne środowiskowe:

| Zmienna | Domyślnie | Ustawia |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | Milisekundy do pierwszego wyrenderowania. |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | Milisekundy dla jednego zapytania. |

Wartość, która nie jest liczbą całkowitą, jest ignorowana i obowiązuje wartość domyślna.

## Kolory dla własnych wykresów

`pcp.series()` zwraca paletę wykresów PlaidCloud jako listę kolorów, w kolejności. Użyj jej, aby wykresy rysowane samodzielnie pasowały do własnych komponentów zestawu, jak w przykładzie dla wykresu słupkowego.

## Dalsze kroki

- [Data API](/pl/guides/panel-apps/data-api/) — filtruj, dziel na strony, zliczaj i agreguj tabele PlaidCloud z poziomu aplikacji.
- [Alerty i podsumowania](/pl/guides/panel-apps/alerts-and-digests/) — wysyłaj z aplikacji alerty KPI i zaplanowane podsumowania.
- [Branding projektu](/pl/guides/panel-apps/branding/) — ustaw kolory i logo raz dla każdej aplikacji w projekcie.
