---
title: Odczyt danych i zalogowanego użytkownika w aplikacji Dash
description: Połącz aplikację Dash z PlaidCloud jako osoba, która ją przegląda — odczytuj dane projektu i wykorzystuj tożsamość przeglądającego do zachowań specyficznych dla użytkownika oraz zabezpieczeń na poziomie wierszy.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/accessing-data.md
---

Aplikacja Dash może odczytywać Twoje dane PlaidCloud — i robi to **jako osoba, która ją przegląda**, dokładnie tak samo jak serwerowa aplikacja Panel. Gdy ktoś otwiera aplikację, PlaidCloud loguje go za pomocą tego samego jednokrotnego logowania (SSO), z którego korzysta cała platforma, a każde wywołanie wykonywane przez aplikację działa z **uprawnieniami samego przeglądającego**. Nie ma współdzielonego konta usługi, a aplikacja nigdy nie zobaczy danych, których nie mógłby zobaczyć sam przeglądający.

Funkcje pomocnicze znajdują się w `plaidcloud_dash`, części bazowego obrazu Dash:

```python
from plaidcloud_dash import current_user, get_connection
```

## Połączenie z PlaidCloud

Wywołaj `get_connection()` z wnętrza wywołania zwrotnego (callbacku) Dash, podając projekt, z którego chcesz odczytać dane:

```python
from plaidcloud_dash import get_connection

conn = get_connection(project_id="<your-project-id>")
```

To cała wymagana konfiguracja. **Nie** podajesz tokenu, nazwy użytkownika ani hasła — `get_connection()` automatycznie uwierzytelnia się jako zalogowany przeglądający, używając tokenu dostępu z jego bieżącej sesji. Identyfikator projektu znajdziesz w adresie URL projektu lub na stronie jego ustawień.

> **Wywołuj ją z wnętrza callbacku.** `get_connection()` odczytuje token przeglądającego z sesji Flask bieżącego żądania, która jest dostępna tylko wtedy, gdy callback obsługuje żądanie tego przeglądającego. Jeśli przekażesz wywołanie blokujące do wątku w tle, surowa pula wątków nie przeniesie sesji — odczytaj token wewnątrz callbacku i przekaż go jawnie. Wywołanie `get_connection()` poza żądaniem (lub przy wyłączonym uwierzytelnianiu) zgłasza `RuntimeError`, zamiast po cichu zwracać połączenie bez żadnej tożsamości.

> **Podaj projekt w kodzie.** W oknie publikacji nie ma ustawienia projektu — aplikacja Dash odczytuje ten projekt, który podasz w `get_connection(project_id=...)`, tak samo jak `PlaidConnection(project_id=...)` w serwerowej aplikacji Panel — zobacz [Odczyt danych i zalogowanego użytkownika](/pl/guides/panel-apps/accessing-data/). Samo `get_connection()` bez `project_id` jest w porządku w aplikacji, która nigdy nie sięga do danych projektu (na przykład takiej, która wywołuje tylko `current_user()`); jeśli jednak wywołasz na takim połączeniu operację w zakresie projektu bez prawdziwego, dostępnego identyfikatora projektu, zgłosi ona błąd `Project Id has not been set`. (Aby odczytywać dane z więcej niż jednego projektu, otwórz osobne połączenie dla każdego projektu.)

### Odczyt tabeli

Mając połączenie, pobierz tabelę do ramki danych pandas według nazwy:

```python
df = conn.get_dataframe("Sales Ledger")
```

Ponieważ połączenie jest przeglądającym, zwraca ono tylko te wiersze, które przeglądający może zobaczyć, a jeśli nie ma on żadnego dostępu do projektu, zgłasza błąd uprawnień.

> **Odczytuj tabele według nazwy, nie pisząc SQL.** W projekcie, w którym administrator włączył [Dostęp do wierszy](/pl/administration/access/managing-security-groups-and-assignments/#dostęp-do-wierszy-i-zapytania-pisane-samodzielnie), odczyt według nazwy stosuje uprawnienia do wierszy każdego przeglądającego, natomiast zapytanie skomponowane przez samą aplikację jest odrzucane dla każdego, kto nie jest Architektem projektu — nie ma bowiem jednej tabeli, którą uprawnienia mogłyby filtrować. Odczyt według nazwy sprawia, że aplikacja działa w obu przypadkach.

## Odczyt w callbacku, nigdy podczas importu ani w zakresie procesu

Jeden proces obsługuje wszystkich przeglądających. Poprawna izolacja danych sprowadza się do dwóch zasad:

- **Nigdy nie otwieraj połączenia ani nie odczytuj tabeli w zakresie modułu (podczas importu).** Plik `app.py` i wszystkie importowane przez niego moduły uruchamiają się **raz**, przy starcie kontenera — zanim ktokolwiek się zaloguje. `get_connection()` lub `PlaidConnection()` w tym miejscu nie ma przeglądającego, jako którego mogłoby się uwierzytelnić, i powoduje awarię aplikacji przy starcie (to najczęstsza przyczyna pętli awarii „aplikacja się nie uruchomiła"). Wszystkie odczyty umieszczaj wewnątrz callbacku, gdzie obecne jest żądanie przeglądającego — i jego token sesji.

- **Nigdy nie przechowuj w pamięci podręcznej wyniku zależnego od przeglądającego w zakresie modułu lub procesu.** Wielowątkowy worker gunicorn współdzieli jeden proces Pythona między wszystkich równoczesnych przeglądających, więc ramka danych zapisana w zmiennej na poziomie modułu, w globalnym słowniku lub w `lru_cache` jest widoczna dla *każdego* innego przeglądającego — wiersze jednej osoby trafiają do widoku innej. Dane zależne od przeglądającego obliczaj wewnątrz callbacku i pozwól im wyjść poza zakres, gdy callback się zakończy:

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

### Współdzielone dane referencyjne

Jeśli kilku przeglądających rzeczywiście potrzebuje *tych samych* danych referencyjnych — tabeli wyszukiwania, listy produktów — nie próbuj współdzielić ich przez pamięć podręczną na poziomie procesu. Przyznaj te tabele użytkownikom aplikacji za pomocą standardowych [uprawnień Dostęp do wierszy / projektu](/pl/administration/access/managing-security-groups-and-assignments/) PlaidCloud i pozwól każdemu przeglądającemu odczytać je przez własne `get_connection()`. Wszyscy otrzymają te same wiersze referencyjne, ponieważ wszyscy mają przyznany ten sam dostęp — a nie dlatego, że odczyt jednego przeglądającego został użyty ponownie dla innego.

## Identyfikacja przeglądającego

Aby dopasować to, co pokazuje aplikacja, do **osoby, która na nią patrzy** — spersonalizowane powitanie, ukrycie karty lub zabezpieczenia na poziomie wierszy — wywołaj `current_user()`:

```python
from plaidcloud_dash import current_user

viewer = current_user()  # the viewer's identifier
```

`current_user()` zwraca identyfikator zalogowanego przeglądającego — jego nazwę użytkownika, a gdy brak roszczenia z nazwą użytkownika, adres e-mail, a następnie identyfikator konta — pobrany z jego zweryfikowanego logowania, więc możesz mu ufać jako tożsamości. Nigdy nie zgłasza wyjątku; wywołana przy wyłączonym uwierzytelnianiu lub poza żądaniem zwraca pusty ciąg.

### Zabezpieczenia na poziomie wierszy

Połącz oba elementy: odczytaj przeglądającego, a następnie filtruj każde zapytanie według niego. Na przykład, aby pokazać każdemu kierownikowi regionu tylko jego własny region:

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

Ponieważ połączenie już wymusza uprawnienia projektu przeglądającego, to filtrowanie jest *dodatkowym* kształtowaniem tego, co wolno mu zobaczyć — a nie zamiennikiem własnej kontroli dostępu PlaidCloud.

## Aplikacje publiczne

Jeśli opublikujesz aplikację z opcją **Zezwól na dostęp publiczny**, jest ona udostępniana bez logowania, więc nie ma przeglądającego, jako którego można działać — `current_user()` zwraca pusty ciąg, a `get_connection()` nie ma tokenu sesji do uwierzytelnienia, więc zgłasza błąd. Ogranicz aplikacje publiczne do danych, które są bezpieczne dla każdego, lub pozostaw dostęp publiczny wyłączony, aby przeglądający logowali się i obowiązywał opisany wyżej model per użytkownik.
