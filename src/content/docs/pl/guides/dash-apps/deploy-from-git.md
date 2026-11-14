---
title: Wdrażanie aplikacji Dash z PlaidCloud Git
description: Pełna ścieżka udostępniania aplikacji Plotly Dash w PlaidCloud — umieść kod w repozytorium PlaidCloud Git, połącz je za pomocą zarządzanego połączenia bez poświadczeń i opublikuj aplikację.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/deploy-from-git.md
---

To kompletna ścieżka od kodu aplikacji Dash na Twoim komputerze do działającego adresu URL, z użyciem **[PlaidCloud Git](/pl/guides/git/)** — zarządzanej usługi Git wbudowanej w Twój obszar roboczy — jako źródła. Ponieważ PlaidCloud Git jest usługą zarządzaną, połączenie, z którego wdrażana jest aplikacja, **nie wymaga adresu URL serwera, nazwy użytkownika ani tokenu**: PlaidCloud uwierzytelnia Cię automatycznie.

Proces składa się z pięciu kroków:

1. Napisz minimalną aplikację Dash.
2. Umieść ją w repozytorium PlaidCloud Git.
3. Utwórz zarządzane połączenie PlaidCloud Git.
4. Opublikuj aplikację Dash wskazującą to repozytorium.
5. Otwórz udostępnioną aplikację — a jeśli się nie uruchomi, przejrzyj dzienniki budowania.

Ta instrukcja jest niemal identyczna z [wdrażaniem aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/) — obie to aplikacje w języku Python działające po stronie serwera, budowane z Git i udostępniane w ten sam sposób. Różni się kod samej aplikacji i jedno pole w oknie publikacji.

## Zanim zaczniesz

- Otwórz **Git** w swoim obszarze roboczym, aby sprawdzić, czy masz dostęp do PlaidCloud Git. Domyślnie organizacja Twojego obszaru roboczego zawiera repozytorium **`apps`** — naturalne miejsce także dla aplikacji Dash.
- Zainstaluj lokalnie `git`, jeśli chcesz wypychać kod ze swojego komputera (pliki możesz też dodawać w interfejsie internetowym Git).

## 1. Napisz minimalną aplikację Dash

Aplikacja potrzebuje **punktu wejścia** — pliku Python, który buduje aplikację Dash i udostępnia jej serwer Flask — oraz opcjonalnie pliku **`requirements.txt`** z dodatkowymi pakietami, umieszczonego w katalogu głównym repozytorium lub obok punktu wejścia.

```
apps/
├── app.py            # entry point — exposes `server`
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Utwórz plik `app.py`:

```python
import plaidcloud_dash as pcd
from dash import Dash, Input, Output, html

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you

app.layout = html.Div(
    [
        html.H1("Hello from PlaidCloud Git"),
        html.P(id="whoami"),
        html.Button("Who am I?", id="whoami-btn", n_clicks=0),
    ]
)


@app.callback(Output("whoami", "children"), Input("whoami-btn", "n_clicks"))
def _whoami(n_clicks):
    if not n_clicks:
        return ""
    return f"Signed in as {pcd.current_user()!r}"


if __name__ == "__main__":
    app.run(debug=True)
```

To kompletna aplikacja. Pakiety `dash`, `plotly`, `dash-mantine-components`, `dash-ag-grid` oraz biblioteki klienckie PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) są zainstalowane z góry, więc w pliku `requirements.txt` wymieniaj tylko *dodatkowe* pakiety. Nie przekazuj `requests_pathname_prefix` ani `url_base_pathname` do `Dash(__name__)` — platforma automatycznie ustawia prefiks adresu URL przez `DASH_URL_BASE_PATHNAME`, a ustawienie obu powoduje błąd konfiguracji podczas uruchamiania. Pełny kontrakt aplikacji i funkcje pomocnicze dostępu do danych opisano w sekcjach [Kontrakt aplikacji](/pl/guides/dash-apps/#kontrakt-aplikacji) oraz [Odczyt danych i zalogowanego użytkownika w aplikacji Dash](/pl/guides/dash-apps/accessing-data/).

## 2. Umieść aplikację w repozytorium PlaidCloud Git

Użyj istniejącego repozytorium **`apps`** w swoim obszarze roboczym lub [utwórz nowe](/pl/guides/git/repositories/#tworzenie-repozytorium). Następnie umieść w nim swój kod.

Ponieważ logujesz się przez PlaidCloud, Twoje konto Git nie ma osobnego hasła — [wygeneruj osobisty token dostępu](/pl/guides/git/repositories/#generowanie-osobistego-tokenu-dostępu) (**Twój awatar → Settings → Applications**) z uprawnieniem **write:repository** i użyj go jako hasła, gdy Git o nie poprosi. Wypychanie do `apps` wymaga dostępu **Contributor**; jeśli na karcie **Git** widzisz siebie jako **Przeglądającego**, poproś administratora obszaru roboczego o dodanie Cię do grupy **Git Contributors**. Użyj przycisku kopiowania obok adresu klonowania repozytorium na karcie **Git**, a następnie:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

Zapisz ścieżkę repozytorium — `<org>/apps` — gdzie `<org>` to nazwa organizacji Twojego obszaru roboczego. Wpiszesz ją w następnym kroku. Pełne informacje o klonowaniu, zatwierdzaniu i wypychaniu zmian znajdziesz w sekcji [Repozytoria](/pl/guides/git/repositories/).

> **Token służy tutaj wyłącznie do wypychania kodu przez *Ciebie*.** Połączenie, które utworzysz za chwilę, jest zarządzane i nie wymaga tokenu — nie myl tych dwóch rzeczy.

## 3. Utwórz zarządzane połączenie PlaidCloud Git

**Połączenie** informuje wdrożenie Dash, gdzie znajduje się jego kod. W przypadku PlaidCloud Git połączenie jest *zarządzane* — PlaidCloud dostarcza hosta i poświadczenia, więc podajesz tylko docelowe repozytorium. Jest to ten sam typ połączenia, którego używa serwerowa aplikacja Panel.

1. Otwórz **Tools > Connections**, kliknij **Nowe połączenie** i wybierz **PlaidCloud Git**.
2. Nadaj połączeniu **Nazwę konta** (na przykład `Apps Repo`).
3. Ustaw **Repository Path** na `<org>/apps` — ścieżkę zapisaną w kroku 2 — a **Domyślną gałąź** na `main`. Pole **Ścieżka początkowa** pozostaw puste, chyba że Twoje aplikacje znajdują się w podkatalogu.
4. Kliknij **Utwórz**.

Nie ma pól Server URL, User, Password ani SSL/SSH — PlaidCloud Git jest zarządzany, więc platforma obsługuje hosta i uwierzytelnianie. Pełny formularz, w tym **Użycie** i **Model zabezpieczeń** połączenia (kto w obszarze roboczym może z niego korzystać), opisano w sekcji [Połączenie PlaidCloud Git](/pl/guides/connections/plaidcloud-git/).

## 4. Opublikuj aplikację Dash

Teraz wskaż wdrożeniu Dash to połączenie.

1. Otwórz **Aplikacje** i wybierz **Nowa aplikacja** > **Aplikacja Dash**.
2. W sekcji **Ustawienia katalogu** ustaw **Nazwę aplikacji** i **Slug URL** — slug to adres URL i wewnętrzna nazwa aplikacji, więc użyj małych liter, cyfr i myślników, zaczynając od litery, maksymalnie 40 znaków (na przykład `hello-dash`). Opcjonalna **Notatka** opisuje aplikację.
3. W sekcji **Połączenie Git i obserwator publikacji**:
   - **Połączenie Git** — połączenie PlaidCloud Git utworzone w kroku 3.
   - **Gałąź** — `main`. Wypchnięcia do tej gałęzi automatycznie przebudowują i ponownie wdrażają aplikację.
   - **Punkt wejścia** — `app.py`.
4. W sekcji **Środowisko uruchomieniowe** wybierz **CPU**, **Pamięć** i okno **Bezczynność (minuty)**. Zaznacz **Zezwól na dostęp publiczny** tylko wtedy, gdy aplikacja ma być dostępna bez logowania. Nie ma ustawienia **Projekt** — to opcja specyficzna dla aplikacji Panel.
5. W sekcji **Zaawansowane (osadzone udostępnianie)** — opcjonalnie. Pozostaw ją pustą, chyba że osadzasz aplikację w innej witrynie.
6. Kliknij **Opublikuj**.

## 5. Otwórz aplikację — a jeśli się nie uruchomi, przejrzyj dzienniki

Po opublikowaniu aplikacja jest **budowana**: PlaidCloud klonuje gałąź, instaluje pakiety z pliku `requirements.txt` i buduje obraz kontenera na podstawie obrazu `platform-dash-base`. Jej **Stan** jest widoczny na liście **Aplikacje** i aktualizuje się automatycznie.

- Gdy Stan to **Gotowe**, otwórz aplikację pod adresem `https://<your-tenant-host>/serve/<slug>/`. Pierwsze żądanie po okresie bezczynności uruchamia aplikację, wyświetlając przy tym krótki ekran ładowania PlaidCloud.
- Jeśli budowanie się nie powiedzie, otwórz aplikację i sprawdź jej dzienniki **Zbuduj** — brakująca zależność lub błąd importu będą tam widoczne. W sekcji [Korzystanie z aplikacji Dash](/pl/guides/dash-apps/using/) dowiesz się, co oznacza każdy stan, jak czytać dzienniki i jak wywołać ponowne budowanie.

Odtąd **każde wypchnięcie do gałęzi połączenia automatycznie przebudowuje i ponownie wdraża aplikację** — edytuj `app.py`, wykonaj `git push`, a zmiana trafi na żywo. (Chyba że aplikacja jest **zablokowana** — wtedy wypchnięcia są pomijane do czasu jej odblokowania; zobacz [Korzystanie z aplikacji Dash](/pl/guides/dash-apps/using/#blokowanie-aplikacji).)

## Następne kroki

- [Odczyt danych i zalogowanego użytkownika w aplikacji Dash](/pl/guides/dash-apps/accessing-data/) — wykonuj zapytania do danych PlaidCloud jako osoba przeglądająca aplikację.
- [Korzystanie z aplikacji Dash](/pl/guides/dash-apps/using/) — stan budowania, dzienniki, blokowanie i usuwanie aplikacji.
- [Połączenie PlaidCloud Git](/pl/guides/connections/plaidcloud-git/) — pełny formularz połączenia, użycie i model zabezpieczeń.
- [Repozytoria](/pl/guides/git/repositories/) — gałęzie, tokeny i współpraca w PlaidCloud Git.
