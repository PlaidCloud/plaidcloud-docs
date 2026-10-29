---
title: Aplikacje Dash
description: Twórz i wdrażaj serwerowe aplikacje danych Plotly Dash w PlaidCloud — publikowane z repozytorium Git i udostępniane z uwierzytelnianiem per użytkownik oraz skalowaniem do zera, na równi z serwerowymi aplikacjami Panel.
sidebar:
  label: Aplikacje Dash
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/index.md
---

Aplikacje Dash umożliwiają publikowanie interaktywnych aplikacji [Plotly Dash](https://dash.plotly.com/) — z callbackami, wykresami i siatkami danych (`dash-ag-grid`, `dash-mantine-components`) — bezpośrednio z PlaidCloud. Zarządzasz nimi na ekranie **Moje aplikacje Panel**, obok aplikacji Panel, gdzie każdy wiersz pokazuje środowisko uruchomieniowe, stan budowania i adres URL aplikacji.

## Miejsce Dash

Aplikacja Dash jest hostowana dokładnie tak jak **serwerowa aplikacja Panel**: wskazujesz PlaidCloud gałąź repozytorium Git, platforma buduje Twój kod w kontener, a kontener pozostaje w bezczynności na zerze replik, budzi się przy pierwszym żądaniu, obsługuje ruch i po okresie bezczynności ponownie skaluje się do zera. Dla Dash nie istnieje osobne środowisko „WASM" — każda aplikacja Dash jest aplikacją serwerową.

Sięgnij po aplikację Dash, gdy Twoja aplikacja jest napisana w Plotly Dash, a nie w HoloViz Panel — na przykład gdy masz istniejącą bazę kodu Dash albo zespół preferuje model callbacków Dash oraz ekosystem `dash-ag-grid` / `dash-mantine-components`. Jeśli zaczynasz od zera i nie masz preferencji, zobacz alternatywę w [Aplikacjach Panel](/pl/guides/panel-apps/).

Wszystko, co dostaje serwerowa aplikacja Panel, dostaje także aplikacja Dash:

- **Tożsamość per użytkownik.** Każdy przeglądający loguje się za pomocą jednokrotnego logowania platformy, a każde wywołanie odczytujące dane wykonywane przez aplikację działa jako *ten przeglądający* — to ten sam model [Odczytu danych i zalogowanego użytkownika](/pl/guides/panel-apps/accessing-data/), z użyciem własnego API pomocniczego Dash. Zobacz [Odczyt danych i zalogowanego użytkownika w aplikacji Dash](/pl/guides/dash-apps/accessing-data/).
- **Skalowanie do zera.** Aplikacja po skonfigurowanym oknie bezczynności przechodzi do zera replik i budzi się przy następnym żądaniu, wyświetlając podczas zimnego startu krótki ekran ładowania PlaidCloud — zobacz [Korzystanie z aplikacji Dash](/pl/guides/dash-apps/using/#otwieranie-aplikacji-dash).
- **Automatyczne przebudowywanie.** Każde wypchnięcie do połączonej gałęzi przebudowuje i ponownie wdraża aplikację.
- **Dzienniki środowiska uruchomieniowego i budowania**, z których każdy wiersz jest oznaczony przeglądającym, którego sesja go wygenerowała.

Dwóch rzeczy aplikacja Dash **nie** ma — z założenia i zgodnie z tym, czego brakuje także aplikacji Panel:

- **Brak ustawienia projektu graficznego/motywu.** Opcja **Projekt** w oknie publikacji Panel (FAST lub domyślny) dotyczy wyłącznie Panel — aplikacje Dash stylizują się w całości za pomocą wybranych komponentów (`dash-mantine-components`, własny CSS itd.), więc formularz publikacji nie ma odpowiadającego jej pola.
- **Brak listy dostępu per aplikacja.** Dostęp opiera się na bramce SSO obszaru roboczego — każdy zalogowany w Twoim tenancie może otworzyć aplikację (lub, jeśli włączysz **Zezwól na dostęp publiczny**, każdy bez wyjątku). Dla żadnego z typów aplikacji nie ma osobnej warstwy ACL per aplikacja.

## Kontrakt aplikacji

Plik wejściowy aplikacji Dash musi nazywać się `app.py` i musi udostępniać `server` — to cały kontrakt:

```python
from dash import Dash

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you
```

- **Nazwij plik `app.py`.** Program uruchamiający PlaidCloud importuje Twoją aplikację jako moduł `app` i odczytuje jego obiekt `server`, więc niezależnie od ścieżki ustawionej w polu **Punkt wejścia** (katalog główny repozytorium lub podkatalog) plik pod tą ścieżką musi nazywać się `app.py`.
- **Udostępnij `server = app.server`** na poziomie modułu. To obiekt, który importuje platforma.
- **Nie konfigurujesz logowania samodzielnie.** Platforma automatycznie obejmuje każde żądanie jednokrotnym logowaniem per użytkownik — nie wywołujesz `init_auth` ani nie importujesz `plaidcloud_dash` tylko po to, by uzyskać tożsamość. (Starsza aplikacja, która *wywołuje* `plaidcloud_dash.init_auth(server, url_base_pathname=os.environ["DASH_URL_BASE_PATHNAME"])`, nadal działa bez zmian — to wywołanie jest idempotentne, więc współistnieje z własnym okablowaniem platformy.)
- **Nie ustawiaj `requests_pathname_prefix` ani `url_base_pathname` w `Dash(__name__)`.** Każda aplikacja Dash jest udostępniana pod obowiązkowym prefiksem adresu URL (`/serve/<slug>/`), a platforma ustawia go za Ciebie przez zmienną środowiskową `DASH_URL_BASE_PATHNAME` — natywną zmienną konfiguracyjną Dash, odczytywaną przed jakimkolwiek argumentem konstruktora. Jawne przekazanie prefiksu dodatkowo koliduje z własną konfiguracją Dash i aplikacja się nie uruchamia.
- **`Entry Point` może wskazywać podkatalog.** Przed uruchomieniem aplikacji host ustawia katalog roboczy kontenera na własny folder pliku wejściowego — dzięki temu importy rodzeństwa z tego samego folderu (`import data`) i ścieżki względne do plików w aplikacji są rozwiązywane względem tego folderu, tak jak przy uruchomieniu `python app.py` z jego wnętrza.
- **Nie odczytuj danych podczas importu.** Odczyty z PlaidCloud wykonuj wewnątrz callbacków, a nie w zakresie modułu — zobacz [Odczyt danych i zalogowanego użytkownika w aplikacji Dash](/pl/guides/dash-apps/accessing-data/). Moduł aplikacji uruchamia się raz, przy starcie kontenera, zanim zaloguje się jakikolwiek przeglądający; połączenie lub odczyt tabeli w tym miejscu nie ma przeglądającego, jako którego mogłoby działać, i powoduje awarię aplikacji przy starcie.

PlaidCloud uruchamia Twoją aplikację pod **wielowątkowym gunicorn**, więc obsługuje ona równoczesnych przeglądających z jednego procesu — nie musisz robić nic dodatkowego, aby aplikacja mogła być używana przez więcej niż jedną osobę naraz.

## Wybór między Panel a Dash

| | Aplikacje Panel | Aplikacje Dash |
|---|---|---|
| Framework | HoloViz Panel | Plotly Dash |
| Środowiska uruchomieniowe | WASM (w przeglądarce) lub serwerowe | Tylko serwerowe |
| Model tożsamości | SSO per użytkownik (aplikacje serwerowe) | SSO per użytkownik |
| Skalowanie do zera | Tylko aplikacje serwerowe | Tak |
| Ustawienie projektu graficznego/motywu | Tak (FAST / domyślny) | Nie — stylizacja przez własne komponenty |
| Lista dostępu per aplikacja | Nie — bramka SSO obszaru roboczego | Nie — bramka SSO obszaru roboczego |

## Następne kroki

- [Wdrażanie aplikacji Dash z PlaidCloud Git](/pl/guides/dash-apps/deploy-from-git/) — pełna ścieżka od repozytorium do udostępnionej aplikacji, z zarządzanym połączeniem bez poświadczeń.
- [Odczyt danych i zalogowanego użytkownika w aplikacji Dash](/pl/guides/dash-apps/accessing-data/) — wykonuj zapytania do danych PlaidCloud jako osoba przeglądająca aplikację.
- [Korzystanie z aplikacji Dash](/pl/guides/dash-apps/using/) — stan budowania, otwieranie aplikacji, dzienniki i jej usuwanie.
