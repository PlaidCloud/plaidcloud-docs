---
title: Wdrażanie aplikacji Panel z PlaidCloud Git
description: Kompletna ścieżka udostępniania aplikacji HoloViz Panel w PlaidCloud — umieść kod w repozytorium PlaidCloud Git, połącz je zarządzanym połączeniem bez poświadczeń i opublikuj na żywo.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

To kompletna ścieżka od kodu aplikacji Panel na Twoim komputerze do działającego adresu URL, z użyciem **[PlaidCloud Git](/pl/guides/git/)** — zarządzanej usługi Git wbudowanej w Twój obszar roboczy — jako źródła. Ponieważ PlaidCloud Git jest zarządzany, połączenie, z którego wdrażana jest aplikacja, **nie wymaga adresu URL serwera, nazwy użytkownika ani tokenu**: PlaidCloud uwierzytelnia się w Twoim imieniu.

Są pięć kroków:

1. Napisz minimalną aplikację Panel.
2. Umieść ją w repozytorium PlaidCloud Git.
3. Utwórz zarządzane połączenie PlaidCloud Git.
4. Opublikuj aplikację serwerową wskazującą repozytorium.
5. Otwórz udostępnioną aplikację — i przeczytaj dzienniki kompilacji, jeśli się nie uruchomi.

Każdy krok odsyła do bardziej szczegółowego przewodnika; ta strona łączy je w jedną ścieżkę.

## Zanim zaczniesz

- Otwórz **Git** ze swojego obszaru roboczego, aby upewnić się, że masz dostęp do PlaidCloud Git. Domyślnie organizacja Twojego obszaru roboczego zawiera repozytorium **`apps`** (oraz **`udfs`**) — naturalny dom dla aplikacji Panel.
- Zainstaluj lokalnie `git`, jeśli chcesz wypychać kod ze swojego komputera (pliki możesz też dodawać w interfejsie webowym Git).

## 1. Napisz minimalną aplikację Panel

Aplikacja potrzebuje **punktu wejścia** — pliku Python, który buduje aplikację Panel i oznacza ją `.servable()` — oraz opcjonalnie pliku **`requirements.txt`** z dodatkowymi pakietami, w katalogu głównym repozytorium lub obok punktu wejścia.

```
apps/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Utwórz `app.py`:

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello from PlaidCloud Git 👋\n\nServed straight from your workspace repository.").servable()
```

To kompletna aplikacja — PlaidCloud udostępnia to, co wywołuje `.servable()`. `panel`, `bokeh` i biblioteki klienckie PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) są preinstalowane, więc w `requirements.txt` wymieniaj tylko *dodatkowe* pakiety. Bogatsze przykłady, zależności i motywy jasny/ciemny opisuje [Tworzenie aplikacji Panel](/pl/guides/panel-apps/creating/).

## 2. Umieść aplikację w repozytorium PlaidCloud Git

Użyj istniejącego repozytorium **`apps`** swojego obszaru roboczego lub [utwórz nowe](/pl/guides/git/repositories/#tworzenie-repozytorium). Następnie umieść w nim kod.

Ponieważ logujesz się przez PlaidCloud, Twoje konto Git nie ma osobnego hasła — [wygeneruj osobisty token dostępu](/pl/guides/git/repositories/#generowanie-osobistego-tokenu-dostępu) (**Twój awatar → Ustawienia → Applications**) z zakresami **odczytu** i **zapisu** repozytorium i użyj go jako hasła, gdy Git o nie poprosi. Skopiuj adres klonowania **HTTPS** repozytorium z przycisku **Code**, a następnie:

```bash
git clone https://<your-git-host>/<org>/apps.git
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

Zanotuj ścieżkę repozytorium — `<org>/apps` — gdzie `<org>` to nazwa organizacji Twojego obszaru roboczego. Wpiszesz tę ścieżkę w następnym kroku. Pełne informacje o klonowaniu, zatwierdzaniu i wypychaniu znajdziesz w [Repozytoriach](/pl/guides/git/repositories/).

> **Token służy tu tylko do wypychania kodu przez *Ciebie*.** Połączenie, które utworzysz dalej, jest zarządzane i nie potrzebuje tokenu — nie myl tych dwóch.

## 3. Utwórz zarządzane połączenie PlaidCloud Git

**Połączenie** informuje wdrożenie Panel, gdzie znajduje się jego kod. W przypadku PlaidCloud Git połączenie jest *zarządzane* — PlaidCloud dostarcza host i poświadczenia, więc podajesz tylko cel w repozytorium.

1. Otwórz **Tools > Connections**, kliknij **Nowe połączenie** i wybierz **PlaidCloud Git**.
2. Nadaj połączeniu **Nazwa konta** (na przykład `Apps Repo`).
3. Ustaw **Repository Path** na `<org>/apps` — ścieżkę zanotowaną w kroku 2 — oraz **Domyślna gałąź** na `main`. Pozostaw **Ścieżka początkowa** puste, chyba że Twoje aplikacje znajdują się w podkatalogu.
4. Kliknij **Utwórz**.

Nie ma pola Server URL, User, Password ani SSL/SSH — PlaidCloud Git jest zarządzany, więc platforma obsługuje host i uwierzytelnianie. Pełny formularz, w tym **Użycie** połączenia i **Model zabezpieczeń** (kto w obszarze roboczym może z niego korzystać), opisuje [Połączenie PlaidCloud Git](/pl/guides/connections/plaidcloud-git/).

> **Starsza wersja obszaru roboczego?** Jeśli formularz nadal pokazuje pole Adres URL serwera lub pola poświadczeń, po prostu zostaw je puste — platforma uwierzytelnia się w Twoim imieniu w obu przypadkach.

## 4. Opublikuj aplikację serwerową

Teraz skieruj wdrożenie serwerowe na to połączenie.

1. Otwórz **Moje aplikacje Panel** i kliknij **Nowa aplikacja serwerowa**.
2. W sekcji **Ustawienia katalogu** ustaw **Nazwa aplikacji** i **Slug URL** — slug jest adresem URL i nazwą wewnętrzną aplikacji, więc użyj małych liter, cyfr i łączników, zaczynając od litery, maksymalnie 40 znaków (na przykład `hello-panel`).
3. W sekcji **Połączenie Git i obserwator publikacji**:
   - **Połączenie Git** — połączenie PlaidCloud Git utworzone w kroku 3.
   - **Gałąź** — `main`. Wypchnięcia do tej gałęzi automatycznie przebudowują i ponownie wdrażają aplikację.
   - **Punkt wejścia** — `app.py`.
4. W sekcji **Środowisko uruchomieniowe** wybierz **CPU**, **Pamięć**, **Projekt** (**FAST** dla nowoczesnego wyglądu PlaidCloud) i okno **Idle**. Zaznacz **Zezwól na dostęp publiczny** tylko wtedy, gdy aplikacja ma być dostępna bez logowania.
5. Kliknij **Opublikuj**.

Każde pole tego okna jest opisane w [Tworzeniu aplikacji Panel](/pl/guides/panel-apps/creating/#publikowanie-aplikacji).

## 5. Otwórz aplikację — i przeczytaj dzienniki, jeśli się nie uruchomi

Po opublikowaniu aplikacja jest **budowana**: PlaidCloud klonuje gałąź, instaluje Twój `requirements.txt` (z katalogu głównego repozytorium i z folderu aplikacji, jeśli istnieją) i buduje obraz kontenera. Jej **Stan** jest widoczny na liście **Moje aplikacje Panel** i aktualizuje się automatycznie.

- Gdy Stan to **Gotowe**, otwórz aplikację pod adresem `https://<your-tenant-host>/serve/<slug>/`. Pierwsze żądanie po okresie bezczynności uruchamia ją (~15 sekund).
- Jeśli kompilacja się nie powiedzie, otwórz aplikację i sprawdź jej dzienniki **Zbuduj** — brakująca zależność lub błąd importu pojawi się właśnie tam. W artykule [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/) dowiesz się, co oznacza każdy stan, jak czytać dzienniki i jak wywołać przebudowę.

Odtąd **każde wypchnięcie do gałęzi połączenia automatycznie przebudowuje i ponownie wdraża aplikację** — edytuj `app.py`, wykonaj `git push`, a zmiana zacznie działać. (Chyba że aplikacja jest **zablokowana** — zobacz [Blokowanie aplikacji](/pl/guides/panel-apps/using/#blokowanie-aplikacji) — wtedy wypchnięcia są pomijane do czasu odblokowania.)

## Następne kroki

- [Tworzenie aplikacji Panel](/pl/guides/panel-apps/creating/) — bogatsze przykłady, zależności i motywy jasny/ciemny
- [Połączenie PlaidCloud Git](/pl/guides/connections/plaidcloud-git/) — pełny formularz połączenia, użycie i model zabezpieczeń
- [Odczyt danych i zalogowany użytkownik](/pl/guides/panel-apps/accessing-data/) — zapytania do danych PlaidCloud jako osoba przeglądająca aplikację
- [Repozytoria](/pl/guides/git/repositories/) — gałęzie, tokeny i współpraca w PlaidCloud Git
