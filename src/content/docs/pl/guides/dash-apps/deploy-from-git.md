---
title: Wdrażanie aplikacji Dash z PlaidCloud Git
description: Pełna ścieżka udostępniania aplikacji Plotly Dash w PlaidCloud — umieść kod w repozytorium PlaidCloud Git, połącz go za pomocą zarządzanego połączenia bez poświadczeń i opublikuj aplikację na żywo.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/deploy-from-git.md
---

To kompletna ścieżka od kodu aplikacji Dash na Twoim komputerze do działającego adresu URL, z użyciem **[PlaidCloud Git](/pl/guides/git/)** — zarządzanej usługi Git wbudowanej w obszar roboczy — jako źródła. Ponieważ PlaidCloud Git jest usługą zarządzaną, połączenie, z którego wdrażana jest aplikacja, **nie wymaga adresu URL serwera, nazwy użytkownika ani tokenu**: PlaidCloud uwierzytelnia się w Twoim imieniu.

Ścieżka składa się z pięciu kroków:

1. Napisz minimalną aplikację Dash.
2. Umieść ją w repozytorium PlaidCloud Git.
3. Utwórz zarządzane połączenie PlaidCloud Git.
4. Opublikuj aplikację Dash wskazującą na repozytorium.
5. Otwórz udostępnioną aplikację — a jeśli się nie uruchamia, sprawdź dzienniki budowania.

Ta instrukcja jest niemal identyczna z [wdrażaniem aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/) — obie to aplikacje Python po stronie serwera, budowane z Git i udostępniane w ten sam sposób. Różnią się kodem aplikacji i jednym polem w oknie publikacji.

## Zanim zaczniesz

- Otwórz **Git** w obszarze roboczym, aby potwierdzić, że masz dostęp do PlaidCloud Git. Domyślnie organizacja Twojego obszaru roboczego zawiera repozytorium **`apps`** — naturalne miejsce także dla aplikacji Dash.
- Jeśli chcesz wypychać kod z własnego komputera, zainstaluj lokalnie `git` (pliki można też dodawać w interfejsie internetowym Git).

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

To kompletna aplikacja. Pakiety `dash`, `plotly`, `dash-mantine-components`, `dash-ag-grid` oraz biblioteki klienckie PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) są preinstalowane, więc w `requirements.txt` wymieniaj tylko *dodatkowe* pakiety. Nie przekazuj `requests_pathname_prefix` ani `url_base_pathname` do `Dash(__name__)` — platforma ustawia prefiks adresu URL automatycznie przez `DASH_URL_BASE_PATHNAME`, a ustawienie obu powoduje błąd konfiguracji przy uruchomieniu. Pełny kontrakt aplikacji i funkcje pomocnicze dostępu do danych opisują [Kontrakt aplikacji](/pl/guides/dash-apps/#kontrakt-aplikacji) oraz [Odczyt danych i zalogowanego użytkownika w aplikacji Dash](/pl/guides/dash-apps/accessing-data/).

## 2. Umieść aplikację w repozytorium PlaidCloud Git

Użyj istniejącego repozytorium **`apps`** swojego obszaru roboczego lub [utwórz nowe](/pl/guides/git/repositories/#tworzenie-repozytorium). Następnie umieść w nim swój kod.

Ponieważ logujesz się przez PlaidCloud, Twoje konto Git nie ma osobnego hasła — [wygeneruj osobisty token dostępu](/pl/guides/git/repositories/#generowanie-osobistego-tokenu-dostępu) (**Twój awatar → Ustawienia → Aplikacje**) z uprawnieniem **write:repository** i użyj go jako hasła, gdy Git o nie poprosi. Wypychanie do `apps` wymaga dostępu **Contributor**; jeśli karta **Git** informuje, że masz dostęp do odczytu, poproś administratora obszaru roboczego o dodanie Cię do grupy **Git Contributors**. Wybierz **Copy clone URL** przy repozytorium na karcie **Git**, a następnie:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

Zapamiętaj ścieżkę repozytorium — `<org>/apps` — gdzie `<org>` to nazwa organizacji Twojego obszaru roboczego. Wpiszesz ją w następnym kroku. Pełne informacje o klonowaniu, zatwierdzaniu i wypychaniu znajdziesz w artykule [Repozytoria](/pl/guides/git/repositories/).

> **Token służy tutaj wyłącznie do wypychania kodu przez *Ciebie*.** Połączenie, które utworzysz w następnym kroku, jest zarządzane i nie wymaga tokenu — nie myl tych dwóch rzeczy.

## 3. Utwórz zarządzane połączenie PlaidCloud Git

**Połączenie** informuje wdrożenie Dash, gdzie znajduje się jego kod. W przypadku PlaidCloud Git połączenie jest *zarządzane* — PlaidCloud dostarcza hosta i poświadczenia, więc wpisujesz tylko docelowe repozytorium. To ten sam typ połączenia, którego używa serwerowa aplikacja Panel.

1. Otwórz **Tools > Connections**, kliknij **Nowe połączenie** i wybierz **PlaidCloud Git**.
2. Nadaj połączeniu **Nazwę konta** (na przykład `Apps Repo`).
3. Ustaw **Repository Path** na `<org>/apps` — ścieżkę zapamiętaną w kroku 2 — a **Domyślną gałąź** na `main`. Pole **Ścieżka początkowa** pozostaw puste, chyba że aplikacje znajdują się w podkatalogu.
4. Kliknij **Utwórz**.

Nie ma pól Adres URL serwera, Użytkownik, Hasło ani SSL/SSH — PlaidCloud Git jest zarządzany, więc platforma obsługuje hosta i uwierzytelnianie. Pełny opis formularza, w tym **Użycia** i **Modelu zabezpieczeń** połączenia (kto w obszarze roboczym może z niego korzystać), znajdziesz w artykule [Połączenie PlaidCloud Git](/pl/guides/connections/plaidcloud-git/).

## 4. Opublikuj aplikację Dash

Teraz skieruj wdrożenie Dash na to połączenie.

1. Otwórz **Moje aplikacje Panel** i kliknij **Nowa aplikacja Dash**.
2. W sekcji **Ustawienia katalogu** ustaw **Nazwę aplikacji** i **Slug URL** — slug to adres URL aplikacji i jej nazwa wewnętrzna, więc użyj małych liter, cyfr i łączników, zaczynając od litery, maksymalnie 40 znaków (na przykład `hello-dash`). Opcjonalna **Notatka** opisuje aplikację.
3. W sekcji **Połączenie Git i obserwator publikacji**:
   - **Połączenie Git** — połączenie PlaidCloud Git utworzone w kroku 3.
   - **Gałąź** — `main`. Wypchnięcia do tej gałęzi automatycznie przebudowują i ponownie wdrażają aplikację.
   - **Punkt wejścia** — `app.py`.
4. W sekcji **Środowisko uruchomieniowe** wybierz **CPU**, **Pamięć** i okno **Bezczynność (minuty)**. Zaznacz **Zezwól na dostęp publiczny** tylko wtedy, gdy aplikacja ma być dostępna bez logowania. Nie ma ustawienia **Projekt** — to opcja specyficzna dla Panel.
5. W sekcji **Zaawansowane (osadzone udostępnianie)** — opcjonalnie. Pozostaw ją pustą, chyba że osadzasz aplikację w innej witrynie.
6. Kliknij **Opublikuj**.

## 5. Otwórz aplikację — i przeczytaj dzienniki, jeśli się nie uruchamia

Po opublikowaniu aplikacja jest **budowana**: PlaidCloud klonuje gałąź, instaluje pakiety z `requirements.txt` i buduje obraz kontenera na podstawie obrazu `platform-dash-base`. Jej **Stan** jest widoczny na liście **Moje aplikacje Panel** i aktualizuje się automatycznie.

- Gdy Stan to **Gotowe**, otwórz aplikację pod adresem `https://<your-tenant-host>/serve/<slug>/`. Pierwsze żądanie po okresie bezczynności uruchamia aplikację, a w tym czasie wyświetlany jest krótki ekran ładowania PlaidCloud.
- Jeśli budowanie się nie powiodło, otwórz aplikację i sprawdź dzienniki **Zbuduj** — brakująca zależność lub błąd importu będą tam widoczne. Znaczenie poszczególnych stanów, sposób czytania dzienników i ponowne budowanie opisuje artykuł [Korzystanie z aplikacji Dash](/pl/guides/dash-apps/using/).

Od tej chwili **każde wypchnięcie do gałęzi połączenia automatycznie przebudowuje i ponownie wdraża aplikację** — edytuj `app.py`, wykonaj `git push`, a zmiana trafi na żywo. (Chyba że aplikacja jest **zablokowana** — wtedy wypchnięcia są pomijane do czasu odblokowania; zobacz [Korzystanie z aplikacji Dash](/pl/guides/dash-apps/using/#blokowanie-aplikacji).)

## Następne kroki

- [Odczyt danych i zalogowanego użytkownika w aplikacji Dash](/pl/guides/dash-apps/accessing-data/) — odpytuj dane PlaidCloud jako osoba przeglądająca aplikację.
- [Korzystanie z aplikacji Dash](/pl/guides/dash-apps/using/) — stan budowania, dzienniki, blokowanie i usuwanie aplikacji.
- [Połączenie PlaidCloud Git](/pl/guides/connections/plaidcloud-git/) — pełny formularz połączenia, użycie i model zabezpieczeń.
- [Repozytoria](/pl/guides/git/repositories/) — gałęzie, tokeny i współpraca w PlaidCloud Git.
