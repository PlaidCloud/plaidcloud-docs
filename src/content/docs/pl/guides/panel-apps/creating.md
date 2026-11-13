---
title: Tworzenie aplikacji Panel
description: Utwórz aplikację Panel w Panel Studio, z pustej aplikacji, tabeli, widoku lub galerii, albo opublikuj aplikację serwerową z git lub statyczną aplikację WASM do indywidualnych potrzeb.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

Zacznij od Panel Studio. Nie wymaga repozytorium ani konfiguracji: budujesz aplikację w PlaidCloud, wyświetlasz jej podgląd i publikujesz, gdy jesteś gotowy. Środowisko uruchomieniowe na zamówienie wybieraj tylko wtedy, gdy Studio nie pasuje.

## Tworzenie aplikacji Studio

Otwórz **Aplikacje** i otwórz menu **New app**. Pod nagłówkiem **Aplikacja Panel** pozycja **Studio** pisze i publikuje aplikację w edytorze PlaidCloud ze standardowym układem oraz przechowuje dla Ciebie kod. Możesz też wybrać **Nowa aplikacja Studio** w polu **Aplikacje Panel** na karcie **Strona główna** projektu albo [zacząć od tabeli](#zacznij-od-tabeli).

1. Wybierz **New app** > **Studio**.
2. Wprowadź **Nazwa**. **Identyfikator URL (slug)** zostanie z niej uzupełniony.
3. Wybierz **Projekt**, do którego należy aplikacja. Potrzebujesz dostępu do edycji projektu.
4. W polu **Zacznij od** wybierz, od czego aplikacja się zaczyna:

   | Zacznij od | Otrzymujesz |
   |---|---|
   | **Pusta aplikacja** | Minimalną aplikację z plikami `app.py` i `requirements.txt`. |
   | **Z tabeli** | Aplikację zbudowaną na wybranej tabeli. |
   | **Z widoku** | To samo, zbudowane na widoku projektu. |
   | **Z innej aplikacji Studio** | Kopię jednej z Twoich aplikacji Studio. |
   | **Z galerii** | Kopię aplikacji, którą Twój obszar roboczy [umieścił w galerii](#zacznij-od-galerii). |

5. Wybierz **Utwórz**. Studio otworzy nową aplikację. W przypadku tabeli lub widoku gotowy do wysłania jest monit Weave o zbudowanie pierwszej strony.

Aby edytować, wyświetlać podgląd i publikować aplikację, zobacz [Panel Studio](/pl/guides/panel-apps/studio/).

### Zacznij od tabeli

Możesz też zacząć na karcie **Tabele** projektu. Zaznacz jedną tabelę lub widok, a następnie wybierz **Utwórz aplikację Panel** z menu **Nowy** lub z menu prawego przycisku myszy. Otworzy się okno **Nowa aplikacja Studio** z już wybranym projektem i tabelą. Polecenie jest dostępne, gdy masz dostęp do edycji projektu, a projekt nie jest tylko do odczytu.

### Zacznij od galerii

Wybierz **New app** > **From gallery…**, aby przeglądać aplikacje wystawione przez Twój obszar roboczy, a następnie **Utwórz aplikację na tej podstawie…**, aby utworzyć własną kopię. Możesz też wybrać **Z galerii** w oknie **New app** Studio. Zobacz [Galeria aplikacji](/pl/guides/panel-apps/gallery/), w tym jak wystawić własną aplikację.

## Inne środowiska uruchomieniowe

Aplikacje Studio obejmują większość pulpitów i narzędzi. Do indywidualnych potrzeb opublikuj za pomocą jednego z pozostałych [środowisk uruchomieniowych](/pl/guides/panel-apps/) z menu **New app**:

- **Browser only** — Twoje własne repozytorium; aplikacja działa w przeglądarce przeglądającego.
- **Server based** — Twoje własne repozytorium; aplikacja działa na serwerze PlaidCloud, na przykład aby ponownie użyć istniejącego kodu lub własnego procesu kompilacji.
- **Aplikacja Dash** — opublikuj aplikację Plotly Dash. Zobacz [Aplikacje Dash](/pl/guides/dash-apps/).

## Tworzenie aplikacji serwerowej

Aplikacja serwerowa jest budowana z repozytorium git i udostępniana pod adresem `https://<your-tenant-host>/serve/<slug>/`. Wskazujesz PlaidCloud gałąź repozytorium; buduje on kod w kontener, uruchamia na nim `panel serve` i automatycznie przebudowuje przy każdym wypchnięciu do tej gałęzi.

### Przygotowanie repozytorium aplikacji

Repozytorium potrzebuje dwóch rzeczy: **punktu wejścia** — pliku Python, który buduje aplikację Panel i oznacza ją `.servable()` — oraz opcjonalnie pliku **`requirements.txt`** z listą dodatkowych pakietów, w katalogu głównym repozytorium lub obok punktu wejścia.

```
my-panel-app/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

#### Hello World

Utwórz `app.py`:

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello, PlaidCloud 👋\n\nYour first server-side Panel app is running.").servable()
```

To kompletna aplikacja. Wywołanie `.servable()` decyduje o tym, co PlaidCloud udostępnia — wszystko, co ma być wyrenderowane, musi być oznaczone jako servable (bezpośrednio lub przez znajdowanie się w układzie servable).

#### Nieco bogatszy przykład

Aplikacje Panel są interaktywne. Ta dodaje suwak, który na żywo aktualizuje tabelę:

```python
import pandas as pd
import panel as pn

pn.extension()

multiplier = pn.widgets.IntSlider(name="Multiplier", start=1, end=10, value=3)

@pn.depends(multiplier)
def times_table(m):
    df = pd.DataFrame({"n": range(1, 6)})
    df["result"] = df["n"] * m
    return pn.pane.DataFrame(df, index=False)

pn.Column(
    "# Times Table",
    multiplier,
    times_table,
).servable()
```

#### Dodawanie zależności

Ten drugi przykład importuje `pandas`, które nie jest częścią obrazu bazowego, więc dodaj plik `requirements.txt` (w katalogu głównym repozytorium lub obok punktu wejścia):

```text
pandas
```

PlaidCloud instaluje je za pomocą `pip` podczas budowania obrazu. Popularne biblioteki wizualizacji — `plotly`, `holoviews`, `hvplot` — również nie są w obrazie bazowym, więc wymień tutaj każdą, którą importuje Twoja aplikacja.

> **Co platforma zapewnia — i czego oczekuje.** Pamiętaj o tych założeniach podczas pisania aplikacji:
>
> - **`panel` i `bokeh` są wstępnie zainstalowane** w obrazie bazowym platformy. Nie wymieniaj ich w `requirements.txt` i unikaj przypinania starszej wersji Panel — ponowne łączenie podczas aktualizacji na żywo wymaga nowej wersji.
> - **Biblioteki klienckie PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) są wstępnie zainstalowane.** Importuj bezpośrednio `plaidcloud.rpc` lub `plaidcloud.utilities` — nie wymieniaj ich w `requirements.txt`.
> - **`requirements.txt` może znajdować się w katalogu głównym repozytorium lub obok punktu wejścia.** We współdzielonym repozytorium (monorepo) przechowuj zależności każdej aplikacji w jej własnym folderze. Plik na poziomie głównym, jeśli istnieje, również jest instalowany — umieść tam zależności współdzielone, a specyficzne dla aplikacji obok niej.
> - **Aplikacja działa jako użytkownik inny niż root na systemie plików tylko do odczytu.** Zapisywalny jest tylko `/tmp`, więc zapisuj tam wszelkie pliki tymczasowe (większość bibliotek już respektuje `$TMPDIR`).
> - **Nie zapisuj na stałe portu, prefiksu URL ani hosta.** PlaidCloud przypisuje je i wstrzykuje podczas wdrażania — po prostu wywołaj `.servable()`.

Aby uzyskać wygląd PlaidCloud oraz gotowe filtry, siatki i wykresy, zbuduj aplikację za pomocą [zestawu Panel app kit](/pl/guides/panel-apps/app-kit/).

### Ustawianie motywu: jasny, ciemny lub przełącznik

Aplikacje serwerowe domyślnie renderują się we współczesnym projekcie **Fast** PlaidCloud — czystym wyglądzie w stylu Fluent stosowanym w całej platformie. W oknie publikacji **Projekt** steruje tą warstwą platformy:

- **FAST** — domyślne ustawienie PlaidCloud. Użyj go dla nowych aplikacji i aplikacji zbudowanych z szablonami Fast.
- **Domyślny** — domyślna stylizacja Panel. Użyj go, gdy CSS lub elementy wizualne istniejącej aplikacji psują się w FAST.

To, co kontrolujesz w kodzie aplikacji, to **motyw**: jasny, ciemny lub przełącznik, który może zmieniać przeglądający.

Motyw jest właściwością **szablonu**, który udostępniasz. Szablony Fast — `FastListTemplate` (pojedyncza kolumna) i `FastGridTemplate` (responsywna siatka) — przyjmują dwa ustawienia dotyczące motywu:

- **`theme`** — `"default"` dla jasnego lub `"dark"`. Ustawienie go przypina aplikację do tego motywu, nawet jeśli przeglądający doda `?theme=dark` do adresu URL.
- **`theme_toggle`** — `True` pokazuje przełącznik jasny/ciemny w nagłówku; `False` go ukrywa. Domyślnie `True`. Ukrycie przełącznika samo nie ustala motywu — przypnij go za pomocą `theme` (powyżej); ustaw `theme_toggle=False` po tym, aby przeglądający nie widzieli przełącznika, który niczego nie zmienia.

Wybierz wzorzec odpowiedni dla Twojej aplikacji.

**Tylko jasny** — najlepszy dla gęstych raportów i tabel finansowych, które zwykle są ręcznie stylizowane pod jasne tło:

```python
import panel as pn

pn.extension("tabulator")

pn.template.FastListTemplate(
    title="Sales Dashboard",
    theme="default",      # light
    theme_toggle=False,   # hide the switch
    main=[...],
).servable()
```

**Tylko ciemny:**

```python
pn.template.FastListTemplate(
    title="Ops Monitor",
    theme="dark",
    theme_toggle=False,
    main=[...],
).servable()
```

**Pozwól przeglądającemu wybrać** — domyślnie jasny, z przełącznikiem w nagłówku. Pomiń `theme`, aby podążał za przełącznikiem:

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **Jeśli dopuszczasz ciemny motyw, zadbaj, by tabele go uwzględniały.** `Tabulator` przypięty do jasnego motywu tabeli (`theme="bootstrap"`) lub własny CSS z zakodowanymi na stałe jasnymi kolorami, takimi jak `background: #fff`, renderuje się jako nieczytelny biały blok na ciemnej stronie. Użyj motywu tabeli, który podąża za aplikacją — `pn.widgets.Tabulator(..., theme="fast")` — i unikaj zakodowanych na stałe jasnych kolorów. Jeśli raport jest mocno ręcznie stylizowany pod jasny motyw, przypnij go do jasnego (pierwszy wzorzec powyżej).

Zwykła aplikacja bez szablonu — `pn.Column(...).servable()` — podąża za domyślnym ustawieniem Panel i nie podlega tym ustawieniom; sięgnij po szablon, gdy chcesz mieć jawną kontrolę.

Repozytorium musi być dostępne przez **połączenie git** w PlaidCloud. Jeśli Twój kod znajduje się w [PlaidCloud Git](/pl/guides/git/), utwórz zarządzane połączenie **PlaidCloud Git** w **Tools > Connections** — nie wymaga adresu URL serwera ani poświadczeń. Całą ścieżkę od pustego repozytorium do udostępnionej aplikacji znajdziesz w [Wdrażanie aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/).

### Publikowanie aplikacji

1. Wybierz **New app** > **Server based**, aby otworzyć okno **Opublikuj serwerową aplikację Panel**. Jego ustawienia są pogrupowane w sekcje.
2. W sekcji **Ustawienia katalogu**:
   - **Nazwa aplikacji** — nazwa wyświetlana na liście.
   - **Slug URL** — zarówno adres URL aplikacji, jak i jej nazwa wewnętrzna, więc musi być prawidłową etykietą DNS: małe litery, cyfry i łączniki, zaczynająca się od litery, do 40 znaków (na przykład `sales-dashboard`). Okno sprawdza to przed publikacją.
   - **Notatka** — opcjonalny opis.
   - **Projekt** — projekt, do którego należy aplikacja. Zapewnia [markę](/pl/guides/panel-apps/branding/) aplikacji i jest domyślnym projektem dla jej tabel. Nie możesz go tutaj zmienić po opublikowaniu; użyj [Assign](/pl/guides/panel-apps/branding/#dla-istniejących-aplikacji).
3. W sekcji **Połączenie Git i obserwator publikacji**:
   - **Połączenie Git** — połączenie, które przechowuje repozytorium Twojej aplikacji.
   - **Gałąź** — gałąź, z której budować. Wypchnięcia do tej gałęzi automatycznie przebudowują i ponownie wdrażają aplikację.
   - **Punkt wejścia** — plik `.py`, który Panel ma udostępniać (Twój `app.py`).
4. W sekcji **Środowisko uruchomieniowe**:
   - **CPU** i **Pamięć**, o które ma prosić kontener aplikacji.

     > Mniej zasobów (niższy CPU / pamięć) pozwala aplikacji szybciej się planować i uruchamiać na zimno.

   - **Projekt** — wybierz **FAST** dla nowoczesnego projektu PlaidCloud lub **Domyślny**, jeśli CSS aplikacji oczekuje domyślnej stylizacji Panel.
   - **Bezczynność (minuty)** — jak długo aplikacja pozostaje rozgrzana bez ruchu, zanim zostanie skalowana z powrotem do zera. Domyślnie 5 minut.
   - **Zezwól na dostęp publiczny** — zaznacz, aby zezwolić na dostęp bez uwierzytelniania; w przeciwnym razie przeglądający muszą zalogować się do Twojej dzierżawy.
5. W sekcji **Zaawansowane (osadzone udostępnianie)** — opcjonalnie. Domyślnie aplikacja jest udostępniana tylko z Twojej dzierżawy PlaidCloud. Aby osadzić ją w innej witrynie, kliknij **Dodaj domenę** i wprowadź każdą domenę, która może ją ładować, po jednej w wierszu — tylko host, bez schematu ani ścieżki (na przykład `example.com` lub `app.example.com:8443`). Pozostaw listę pustą, chyba że osadzasz aplikację gdzie indziej.
6. Kliknij **Opublikuj**.

Po opublikowaniu aplikacja jest **budowana** — jej **Stan** jest wyświetlany na liście i aktualizuje się automatycznie. Zobacz [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/), aby dowiedzieć się, co oznaczają stany, jak otworzyć aplikację, gdy jest gotowa, i jak wywołać przebudowę bez cofania publikacji.

> Adres URL aplikacji działa dopiero wtedy, gdy jej stan kompilacji to **Gotowe**, a pierwsze żądanie po okresie bezczynności ją uruchamia (~15 sekund).

### Zaawansowane: odtwórz PlaidCloud lokalnie

Użytkownicy techniczni mogą zbudować i przetestować aplikację z tymi samymi danymi wejściowymi, których używa PlaidCloud. To najbliższe lokalne sprawdzenie przed publikacją lub kliknięciem **Zbuduj ponownie**.

PlaidCloud buduje z wybranej gałęzi git za pomocą tego wygenerowanego pliku Dockerfile. Użyj tej samej zawartości lokalnie jako `Dockerfile.plaidcloud-panel`:

```dockerfile
FROM us-docker.pkg.dev/plaidcloud-build/panel-base/platform-panel-base:0.5.1
USER root
COPY . /app
RUN if [ -f /app/requirements.txt ]; then pip install --no-cache-dir -r /app/requirements.txt; fi
# If your entry point is in a subfolder, PlaidCloud also installs that folder's requirements.txt,
# after the root one (so a per-app pin wins). Replace <app-folder> with your entry point's folder,
# or drop this line if your app is at the repository root.
RUN if [ -f "/app/<app-folder>/requirements.txt" ]; then pip install --no-cache-dir -r "/app/<app-folder>/requirements.txt"; fi
USER 10001
```

Aby odtworzyć kompilację serwerową:

1. Pobierz tę samą gałąź, którą wybierasz w polu **Gałąź**.
2. Uruchom kompilację z katalogu głównego repozytorium, aby `COPY . /app` odpowiadało PlaidCloud.
3. Umieść opcjonalne zależności w `requirements.txt` — w katalogu głównym repozytorium lub obok punktu wejścia. Instalowane są oba, folder aplikacji jako ostatni (aby przypięcie dla aplikacji miało pierwszeństwo).
4. Użyj tej samej ścieżki punktu wejścia, którą wybierasz w polu **Punkt wejścia**.

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

Wdrożony obraz nie nadpisuje punktu wejścia obrazu bazowego. Uruchamia `panel serve` na podstawie zmiennych środowiskowych wstrzykiwanych przez PlaidCloud. Przetestuj zbudowany obraz z tym samym kontraktem uruchomieniowym:

```sh
docker run --rm \
  --cpus 0.5 \
  --memory 512m \
  -p 5006:5006 \
  -e APP_PATH=/app/app.py \
  -e PANEL_PREFIX=/serve/local \
  -e PANEL_PORT=5006 \
  -e PANEL_ORIGIN=localhost:5006 \
  -e PANEL_KEEP_ALIVE_MS=25000 \
  -e PLAID_PANEL_DESIGN=fast \
  local-panel-app:plaidcloud
```

Otwórz `http://localhost:5006/serve/local/`.

Podczas testowania dopasuj ustawienia okna publikacji:

- **Punkt wejścia** odpowiada `APP_PATH=/app/<entry-point>`.
- **CPU** i **Pamięć** odpowiadają limitom Dockera `--cpus` i `--memory`.
- **Projekt: FAST** odpowiada `PLAID_PANEL_DESIGN=fast`.
- **Projekt: Domyślny** oznacza pominięcie `PLAID_PANEL_DESIGN`.
- **Bezczynność (minuty)** odpowiada oknu skalowania w dół we wdrożeniu. Nie jest egzekwowane przez lokalnego Dockera, ale aplikacja nadal używa tych samych ustawień keepalive websocketu Panel i czyszczenia sesji.
- Domeny **Zaawansowane (osadzone udostępnianie)** odpowiadają `PANEL_ORIGIN`; użyj listy rozdzielonej spacjami, jeśli musisz przetestować więcej niż jednego hosta.

Jeśli nie potrzebujesz kontenera, nadal możesz przetestować warstwę serwującą z lokalnego środowiska Python. Zainstaluj ten sam `requirements.txt`, ustaw zmienne środowiskowe platformy, a następnie uruchom `panel serve` z tymi samymi flagami, których używa wdrożony obraz.

```sh
export APP_PATH=app.py
export PANEL_PREFIX=/serve/local
export PANEL_PORT=5006
export PANEL_ORIGIN=localhost:5006
export PANEL_KEEP_ALIVE_MS=25000
export PLAID_PANEL_DESIGN=fast

panel serve "$APP_PATH" \
  --address 0.0.0.0 \
  --port "$PANEL_PORT" \
  --prefix "$PANEL_PREFIX" \
  --allow-websocket-origin "$PANEL_ORIGIN" \
  --num-procs 1 \
  --keep-alive "$PANEL_KEEP_ALIVE_MS" \
  --unused-session-lifetime 15000 \
  --index "$(basename "$APP_PATH" .py)"
```

Otwórz `http://localhost:5006/serve/local/`.

Użyj `PLAID_PANEL_DESIGN=fast`, aby odtworzyć domyślny wygląd wdrożenia. Aby przetestować opcję **Domyślny** okna publikacji, pozostaw `PLAID_PANEL_DESIGN` nieustawione i uruchom to samo polecenie. Zachowaj `PANEL_PREFIX`, `PANEL_ORIGIN`, `--keep-alive` i `--unused-session-lifetime`; są one częścią kontraktu uruchomieniowego wdrożenia.

## Tworzenie aplikacji WASM

Aplikacja WASM działa w przeglądarce z gotowego pliku HTML.

1. Wybierz **New app** > **Browser only**, aby otworzyć okno **Opublikuj bezserwerową aplikację Panel**.
2. Wprowadź **Nazwa aplikacji** i **Wersja**.
3. Wybierz **Lokalizacja HTML aplikacji** — plik HTML na koncie dokumentów.
4. Wprowadź **Slug URL aplikacji** i opcjonalną **Notatka**.
5. Kliknij **Opublikuj**. Aplikacja WASM nie ma kroku kompilacji i jest udostępniana natychmiast.
