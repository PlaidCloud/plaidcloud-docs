---
title: Wdrażanie aplikacji Dash z PlaidCloud Git
description: Pełna ścieżka udostępniania aplikacji Plotly Dash w PlaidCloud — umieść kod w repozytorium PlaidCloud Git, połącz je zarządzanym połączeniem bez poświadczeń i opublikuj aplikację na żywo.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/deploy-from-git.md
---

To kompletna ścieżka od kodu aplikacji Dash na Twoim komputerze do działającego adresu URL, z użyciem **[PlaidCloud Git](/pl/guides/git/)** — zarządzanej usługi Git wbudowanej w Twój obszar roboczy — jako źródła. Ponieważ PlaidCloud Git jest zarządzany, połączenie, z którego wdrażana jest aplikacja, **nie wymaga adresu serwera, nazwy użytkownika ani tokenu**: PlaidCloud uwierzytelnia się w Twoim imieniu.

Całość składa się z pięciu kroków:

1. Napisz minimalną aplikację Dash.
2. Umieść ją w repozytorium PlaidCloud Git.
3. Utwórz zarządzane połączenie PlaidCloud Git.
4. Opublikuj aplikację Dash wskazującą to repozytorium.
5. Otwórz udostępnioną aplikację — i przeczytaj dzienniki budowania, jeśli się nie uruchomi.

Ten przewodnik jest niemal identyczny z [Wdrażaniem aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/) — obie są serwerowymi aplikacjami Python budowanymi z Git i udostępnianymi w ten sam sposób. Różnią się kodem aplikacji oraz jednym polem w oknie publikacji.

## Zanim zaczniesz

- Otwórz **Git** ze swojego obszaru roboczego, aby upewnić się, że masz dostęp do PlaidCloud Git. Domyślnie organizacja Twojego obszaru roboczego zawiera repozytorium **`apps`** — naturalne miejsce także dla aplikacji Dash.
- Zainstaluj lokalnie `git`, jeśli chcesz wypychać kod ze swojego komputera (pliki możesz też dodawać w interfejsie internetowym Git).

## 1. Napisz minimalną aplikację Dash

Aplikacja potrzebuje **punktu wejścia** — pliku Python, który buduje aplikację Dash i udostępnia jej serwer Flask — oraz opcjonalnie pliku **`requirements.txt`** z dodatkowymi pakietami, umieszczonego w katalogu głównym repozytorium lub obok punktu wejścia.

```
apps/
├── app.py            # entry point — exposes `server`
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Utwórz `app.py`:

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

To kompletna aplikacja. Pakiety `dash`, `plotly`, `dash-mantine-components`, `dash-ag-grid` oraz biblioteki klienckie PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) są zainstalowane z góry, więc w `requirements.txt` wymieniaj tylko *dodatkowe* pakiety. Nie przekazuj `requests_pathname_prefix` ani `url_base_pathname` do `Dash(__name__)` — platforma ustawia prefiks adresu URL automatycznie przez `DASH_URL_BASE_PATHNAME`, a ustawienie obu powoduje błąd konfiguracji przy starcie. Pełny kontrakt aplikacji i funkcje pomocnicze dostępu do danych opisano w [Kontrakcie aplikacji](/pl/guides/dash-apps/#kontrakt-aplikacji) oraz w [Odczycie danych i zalogowanego użytkownika w aplikacji Dash](/pl/guides/dash-apps/accessing-data/).

## 2. Umieść aplikację w repozytorium PlaidCloud Git

Użyj istniejącego repozytorium **`apps`** w swoim obszarze roboczym lub [utwórz nowe](/pl/guides/git/repositories/#tworzenie-repozytorium). Następnie umieść w nim swój kod.

Ponieważ logujesz się przez PlaidCloud, Twoje konto Git nie ma osobnego hasła — [wygeneruj osobisty token dostępu](/pl/guides/git/repositories/#generowanie-osobistego-tokenu-dostępu) (**Twój awatar → Ustawienia → Aplikacje**) z zakresami **odczytu** i **zapisu** repozytorium i użyj go jako hasła, gdy Git o nie poprosi. Skopiuj adres klonowania **HTTPS** repozytorium z przycisku **Kod**, a następnie:

```bash
git clone https://<your-git-host>/<org>/apps.git
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

Zapamiętaj ścieżkę repozytorium — `<org>/apps` — gdzie `<org>` to nazwa organizacji Twojego obszaru roboczego. Wpiszesz ją w następnym kroku. Pełne informacje o klonowaniu, zatwierdzaniu i wypychaniu znajdziesz w [Repozytoriach](/pl/guides/git/repositories/).

> **Token tutaj służy tylko *Tobie* do wypychania kodu.** Połączenie, które utworzysz za chwilę, jest zarządzane i nie wymaga tokenu — nie myl tych dwóch rzeczy.

## 3. Utwórz zarządzane połączenie PlaidCloud Git

**Połączenie** informuje wdrożenie Dash, gdzie znajduje się jego kod. W przypadku PlaidCloud Git połączenie jest *zarządzane* — PlaidCloud dostarcza host i poświadczenia, więc podajesz tylko docelowe repozytorium. To ten sam typ połączenia, którego używa serwerowa aplikacja Panel.

1. Otwórz **Narzędzia > Połączenia**, kliknij **Nowe połączenie** i wybierz **PlaidCloud Git**.
2. Nadaj połączeniu **Nazwę konta** (na przykład `Apps Repo`).
3. Ustaw **Ścieżkę repozytorium** na `<org>/apps` — ścieżkę zapamiętaną w kroku 2 — oraz **Domyślną gałąź** na `main`. Pozostaw **Ścieżkę początkową** pustą, chyba że Twoje aplikacje znajdują się w podkatalogu.
4. Kliknij **Utwórz**.

Nie ma pól Adres URL serwera, Użytkownik, Hasło ani SSL/SSH — PlaidCloud Git jest zarządzany, więc platforma obsługuje host i uwierzytelnianie. Pełny formularz, w tym **Użycie** i **Model zabezpieczeń** połączenia (kto w obszarze roboczym może go używać), opisano w [Połączeniu PlaidCloud Git](/pl/guides/connections/plaidcloud-git/).

## 4. Opublikuj aplikację Dash

Teraz skieruj wdrożenie Dash na to połączenie.

1. Otwórz **Moje aplikacje Panel** i kliknij **Nowa aplikacja Dash**.
2. W sekcji **Ustawienia katalogu** ustaw **Nazwę aplikacji** i **Slug URL** — slug to adres URL i wewnętrzna nazwa aplikacji, więc użyj małych liter, cyfr i łączników, zaczynając od litery, maksymalnie 40 znaków (na przykład `hello-dash`). Opcjonalna **Notatka** opisuje aplikację.
3. W sekcji **Połączenie Git i obserwator publikacji**:
   - **Połączenie Git** — połączenie PlaidCloud Git utworzone w kroku 3.
   - **Gałąź** — `main`. Wypchnięcia do tej gałęzi automatycznie przebudowują i ponownie wdrażają aplikację.
   - **Punkt wejścia** — `app.py`.
4. W sekcji **Środowisko uruchomieniowe** wybierz **CPU**, **Pamięć** i okno **Bezczynność (minuty)**. Zaznacz **Zezwól na dostęp publiczny** tylko wtedy, gdy aplikacja ma być dostępna bez logowania. Nie ma ustawienia **Projekt** — to opcja specyficzna dla Panel.
5. W sekcji **Zaawansowane (osadzone udostępnianie)** — opcjonalnie. Pozostaw puste, chyba że osadzasz aplikację w innej witrynie.
6. Kliknij **Opublikuj**.

## 5. Otwórz aplikację — i przeczytaj dzienniki, jeśli się nie uruchomi

Po opublikowaniu aplikacja jest **budowana**: PlaidCloud klonuje gałąź, instaluje Twój `requirements.txt` i buduje obraz kontenera na podstawie obrazu `platform-dash-base`. Jej **Stan** jest widoczny na liście **Moje aplikacje Panel** i aktualizuje się automatycznie.

- Gdy Stan to **Gotowe**, otwórz aplikację pod adresem `https://<your-tenant-host>/serve/<slug>/`. Pierwsze żądanie po okresie bezczynności uruchamia aplikację, wyświetlając w tym czasie krótki ekran ładowania PlaidCloud.
- Jeśli budowanie się nie powiedzie, otwórz aplikację i sprawdź jej dzienniki **Zbuduj** — brakująca zależność lub błąd importu będzie tam widoczny. W [Korzystaniu z aplikacji Dash](/pl/guides/dash-apps/using/) dowiesz się, co oznacza każdy stan, jak czytać dzienniki i jak wywołać ponowne budowanie.

Od tego momentu **każde wypchnięcie do gałęzi połączenia automatycznie przebudowuje i ponownie wdraża aplikację** — zmień `app.py`, wykonaj `git push`, a zmiana trafi na żywo. (Chyba że aplikacja jest **zablokowana** — wtedy wypchnięcia są pomijane do czasu odblokowania; zobacz [Korzystanie z aplikacji Dash](/pl/guides/dash-apps/using/#blokowanie-aplikacji).)

## Następne kroki

- [Odczyt danych i zalogowanego użytkownika w aplikacji Dash](/pl/guides/dash-apps/accessing-data/) — wykonuj zapytania do danych PlaidCloud jako osoba przeglądająca aplikację.
- [Korzystanie z aplikacji Dash](/pl/guides/dash-apps/using/) — stan budowania, dzienniki, blokowanie i usuwanie aplikacji.
- [Połączenie PlaidCloud Git](/pl/guides/connections/plaidcloud-git/) — pełny formularz połączenia, użycie i model zabezpieczeń.
- [Repozytoria](/pl/guides/git/repositories/) — gałęzie, tokeny i współpraca w PlaidCloud Git.
