---
title: Tworzenie aplikacji Panel
description: Utwórz aplikację Panel w Panel Studio, z pustej aplikacji, tabeli, widoku lub galerii, albo opublikuj aplikację serwerową z gita lub statyczną aplikację WASM na potrzeby niestandardowych rozwiązań.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

Zacznij od Panel Studio. Nie wymaga repozytorium ani konfiguracji: budujesz aplikację w PlaidCloud, wyświetlasz jej podgląd i publikujesz, gdy jest gotowa. Środowisko niestandardowe wybierz tylko wtedy, gdy Studio nie wystarcza.

## Tworzenie aplikacji Studio

Otwórz **Moje aplikacje Panel**. **Nowa aplikacja Studio** to pierwszy przycisk na pasku narzędzi. Możesz też wybrać **Nowa aplikacja Studio** w polu **Aplikacje Panel** na karcie **Strona główna** projektu albo [zacząć od tabeli](#zacznij-od-tabeli).

1. Wybierz **Nowa aplikacja Studio**.
2. Wpisz **Nazwę**. **Slug URL** zostanie wypełniony na jej podstawie.
3. Wybierz **Projekt**, który jest właścicielem aplikacji. Potrzebujesz dostępu do edycji projektu.
4. W polu **Zacznij od** wybierz, od czego aplikacja się zaczyna:

   | Zacznij od | Otrzymujesz |
   |---|---|
   | **Pusta aplikacja** | Minimalną aplikację z plikami `app.py` i `requirements.txt`. |
   | **Z tabeli** | Aplikację zbudowaną na wybranej tabeli. |
   | **Z widoku** | To samo, zbudowane na widoku projektu. |
   | **Z innej aplikacji Studio** | Kopię jednej z Twoich aplikacji Studio. |
   | **Z galerii** | Kopię aplikacji, którą Twój obszar roboczy [umieścił w galerii](#zacznij-od-galerii). |

5. Wybierz **Utwórz**. Studio otworzy nową aplikację. Dla tabeli lub widoku gotowy do wysłania jest monit Weave o zbudowanie pierwszej strony.

Zobacz [Panel Studio](/pl/guides/panel-apps/studio/), aby edytować, wyświetlać podgląd i publikować aplikację.

### Zacznij od tabeli

Możesz też zacząć na karcie **Tabele** projektu. Wybierz jedną tabelę lub widok, a następnie wybierz **Utwórz aplikację Panel** z menu **Nowy** albo z menu prawego przycisku myszy. Otworzy się okno **Nowa aplikacja Studio** z już wybranym projektem i tabelą. Polecenie jest dostępne, gdy masz dostęp do edycji projektu, a projekt nie jest tylko do odczytu.

### Zacznij od galerii

Wybierz **Galeria** na pasku narzędzi **Moje aplikacje Panel**, aby przeglądać aplikacje wymienione w Twoim obszarze roboczym, a następnie **Utwórz aplikację na tej podstawie…**, aby utworzyć własną kopię. Możesz też wybrać **Z galerii** w oknie **Nowa aplikacja Studio**. Zobacz [Galeria aplikacji](/pl/guides/panel-apps/gallery/), w tym jak umieścić własną aplikację na liście.

## Inne środowiska uruchomieniowe

Aplikacje Studio obejmują większość pulpitów i narzędzi. Na potrzeby niestandardowych rozwiązań opublikuj aplikację w jednym z pozostałych [środowisk uruchomieniowych](/pl/guides/panel-apps/) z paska narzędzi **Moje aplikacje Panel**:

- **Dodaj aplikację WASM** — opublikuj statyczną aplikację działającą w przeglądarce z pliku.
- **Nowa aplikacja serwerowa** — zbuduj i uruchom aplikację z repozytorium git, którym zarządzasz, na przykład aby ponownie użyć istniejącego kodu lub własnego procesu budowania.
- **Nowa aplikacja Dash** — opublikuj aplikację Plotly Dash. Zobacz [Aplikacje Dash](/pl/guides/dash-apps/).

## Tworzenie aplikacji serwerowej

Aplikacja serwerowa jest budowana z repozytorium git i udostępniana pod adresem `https://<your-tenant-host>/serve/<slug>/`. Wskazujesz PlaidCloud gałąź repozytorium; buduje on kod w kontenerze, uruchamia na nim `panel serve` i automatycznie buduje go ponownie przy każdym wypchnięciu zmian do tej gałęzi.

### Przygotowanie repozytorium aplikacji

Repozytorium potrzebuje dwóch rzeczy: **punktu wejścia** — pliku Python, który buduje aplikację Panel i oznacza ją jako `.servable()` — oraz, opcjonalnie, pliku **`requirements.txt`** z listą dodatkowych pakietów, w katalogu głównym repozytorium lub obok punktu wejścia.

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

To kompletna aplikacja. PlaidCloud udostępnia to, co wywołuje `.servable()` — wszystko, co ma być wyświetlone, musi być oznaczone jako servable (bezpośrednio albo przez umieszczenie w układzie oznaczonym jako servable).

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

Ten drugi przykład importuje `pandas`, który nie jest częścią obrazu bazowego, więc dodaj `requirements.txt` (w katalogu głównym repozytorium lub obok punktu wejścia):

```text
pandas
```

PlaidCloud instaluje je za pomocą `pip` podczas budowania obrazu. Popularne biblioteki wizualizacji — `plotly`, `holoviews`, `hvplot` — również nie ma w obrazie bazowym, więc wymień tutaj te, które importuje Twoja aplikacja.

> **Co platforma zapewnia — i czego oczekuje.** Pamiętaj o tych założeniach podczas pisania aplikacji:
>
> - **`panel` i `bokeh` są preinstalowane** w obrazie bazowym platformy. Nie wymieniaj ich w `requirements.txt` i unikaj przypinania starszej wersji Panel — ponowne połączenie aktualizacji na żywo wymaga nowej.
> - **Biblioteki klienckie PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) są preinstalowane.** Importuj `plaidcloud.rpc` lub `plaidcloud.utilities` bezpośrednio — nie wymieniaj ich w `requirements.txt`.
> - **`requirements.txt` może znajdować się w katalogu głównym repozytorium lub obok punktu wejścia.** We wspólnym repozytorium (monorepo) trzymaj zależności każdej aplikacji w jej własnym folderze. Plik w katalogu głównym, jeśli istnieje, jest instalowany także — umieść w nim zależności współdzielone, a zależności specyficzne dla aplikacji obok niej.
> - **Aplikacja działa jako użytkownik inny niż root w systemie plików tylko do odczytu.** Zapisywalny jest tylko `/tmp`, więc zapisuj tam wszelkie pliki tymczasowe (większość bibliotek już honoruje `$TMPDIR`).
> - **Nie wpisuj na stałe portu, prefiksu URL ani hosta.** PlaidCloud przypisuje je i wstrzykuje podczas wdrażania — po prostu wywołaj `.servable()`.

Aby uzyskać wygląd PlaidCloud oraz gotowe filtry, siatki i wykresy, zbuduj aplikację za pomocą [zestawu Panel App Kit](/pl/guides/panel-apps/app-kit/).

### Ustawianie motywu: jasny, ciemny lub przełącznik

Aplikacje serwerowe domyślnie są renderowane we współczesnym projekcie **Fast** PlaidCloud — czysty wygląd w stylu Fluent stosowany w całej platformie. W oknie publikacji pole **Projekt** steruje tą warstwą platformy:

- **FAST** — domyślny projekt PlaidCloud. Użyj go dla nowych aplikacji i aplikacji zbudowanych z szablonami Fast.
- **Domyślny** — domyślne style Panel. Użyj go, gdy CSS lub elementy wizualne istniejącej aplikacji psują się pod FAST.

W kodzie aplikacji kontrolujesz **motyw**: jasny, ciemny albo przełącznik, który może przestawić oglądający.

Motyw jest właściwością **szablonu**, który udostępniasz. Szablony Fast — `FastListTemplate` (jedna kolumna) i `FastGridTemplate` (siatka responsywna) — przyjmują dwa ustawienia motywu:

- **`theme`** — `"default"` dla jasnego lub `"dark"`. Ustawienie przypina aplikację do tego motywu, nawet jeśli oglądający doda `?theme=dark` do adresu URL.
- **`theme_toggle`** — `True` pokazuje w nagłówku przełącznik jasny/ciemny; `False` go ukrywa. Domyślnie `True`. Ukrycie przełącznika samo nie ustala motywu — przypnij go za pomocą `theme` (powyżej); ustaw `theme_toggle=False` dopiero wtedy, aby oglądający nie widzieli przełącznika, który nic nie zmienia.

Wybierz wzorzec odpowiedni dla swojej aplikacji.

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

**Pozwól oglądającemu wybierać** — domyślnie jasny, z przełącznikiem w nagłówku. Pomiń `theme`, aby aplikacja podążała za przełącznikiem:

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **Jeśli dopuszczasz tryb ciemny, dostosuj do niego tabele.** `Tabulator` przypięty do jasnego motywu tabeli (`theme="bootstrap"`) lub własny CSS z na stałe wpisanymi jasnymi kolorami, jak `background: #fff`, jest renderowany jako nieczytelny biały blok na ciemnej stronie. Użyj motywu tabeli, który podąża za aplikacją — `pn.widgets.Tabulator(..., theme="fast")` — i unikaj na stałe wpisanych jasnych kolorów. Jeśli raport jest mocno ręcznie stylizowany pod jasny motyw, przypnij go do jasnego (pierwszy wzorzec powyżej).

Zwykła aplikacja bez szablonu — `pn.Column(...).servable()` — podąża za domyślnymi ustawieniami Panel i te ustawienia jej nie dotyczą; sięgnij po szablon, gdy potrzebujesz jawnej kontroli.

Repozytorium musi być osiągalne przez **połączenie git** w PlaidCloud. Jeśli Twój kod jest w [PlaidCloud Git](/pl/guides/git/), utwórz zarządzane połączenie **PlaidCloud Git** w **Tools > Connections** — nie wymaga adresu serwera ani poświadczeń. Całą ścieżkę od pustego repozytorium do udostępnionej aplikacji opisuje [Wdrażanie aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/).

### Publikowanie aplikacji

1. Kliknij **Nowa aplikacja serwerowa**, aby otworzyć okno **Opublikuj serwerową aplikację Panel**. Jego ustawienia są pogrupowane w sekcje.
2. W sekcji **Ustawienia katalogu**:
   - **Nazwa aplikacji** — nazwa wyświetlana na liście.
   - **Slug URL** — zarówno adres URL aplikacji, jak i jej nazwa wewnętrzna, więc musi być poprawną etykietą DNS: małe litery, cyfry i łączniki, zaczynając od litery, nie więcej niż 40 znaków (na przykład `sales-dashboard`). Okno sprawdza to przed publikacją.
   - **Notatka** — opcjonalny opis.
   - **Projekt** — projekt, który jest właścicielem aplikacji. Dostarcza [branding](/pl/guides/panel-apps/branding/) aplikacji i jest domyślnym projektem jej tabel. Po opublikowaniu nie możesz go tu zmienić; użyj [Assign](/pl/guides/panel-apps/branding/#dla-istniejących-aplikacji).
3. W sekcji **Połączenie Git i obserwator publikacji**:
   - **Połączenie Git** — połączenie, które przechowuje repozytorium Twojej aplikacji.
   - **Gałąź** — gałąź, z której budować. Wypchnięcia do tej gałęzi automatycznie przebudowują i ponownie wdrażają aplikację.
   - **Punkt wejścia** — plik `.py`, który Panel ma udostępniać (Twój `app.py`).
4. W sekcji **Środowisko uruchomieniowe**:
   - **CPU** i **Pamięć**, o które powinien prosić kontener aplikacji.

     > Mniej zasobów (niższe CPU / pamięć) pozwala aplikacji szybciej się planować i uruchamiać z zimnego startu.

   - **Projekt** — wybierz **FAST** dla współczesnego projektu PlaidCloud albo **Domyślny**, jeśli CSS aplikacji oczekuje domyślnych stylów Panel.
   - **Bezczynność (minuty)** — jak długo aplikacja pozostaje rozgrzana bez ruchu, zanim zostanie skalowana z powrotem do zera. Domyślnie 5 minut.
   - **Zezwól na dostęp publiczny** — zaznacz, aby zezwolić na dostęp bez uwierzytelniania; w przeciwnym razie oglądający muszą zalogować się do Twojego tenanta.
5. W sekcji **Zaawansowane (osadzone udostępnianie)** — opcjonalnie. Domyślnie aplikacja jest udostępniana tylko z Twojego tenanta PlaidCloud. Aby osadzić ją w innej witrynie, kliknij **Dodaj domenę** i wpisz każdą domenę, której wolno ją ładować, po jednej w wierszu — tylko host, bez schematu i ścieżki (na przykład `example.com` lub `app.example.com:8443`). Pozostaw listę pustą, chyba że osadzasz aplikację gdzie indziej.
6. Kliknij **Opublikuj**.

Po opublikowaniu aplikacja jest **budowana** — jej **Stan** jest pokazywany na liście i aktualizowany automatycznie. Zobacz [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/), aby dowiedzieć się, co oznaczają stany, jak otworzyć aplikację, gdy jest gotowa, i jak wywołać przebudowanie bez cofania publikacji.

> Adres URL aplikacji działa dopiero, gdy stan jej budowania to **Gotowe**, a pierwsze żądanie po okresie bezczynności uruchamia ją (~15 sekund).

### Zaawansowane: odtworzenie PlaidCloud lokalnie

Użytkownicy techniczni mogą zbudować i przetestować aplikację z tymi samymi danymi wejściowymi, których używa PlaidCloud. To najbliższe lokalne sprawdzenie przed publikacją lub kliknięciem **Zbuduj ponownie**.

PlaidCloud buduje z wybranej gałęzi git za pomocą tego wygenerowanego pliku Dockerfile. Użyj lokalnie tej samej zawartości jako `Dockerfile.plaidcloud-panel`:

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

Aby odtworzyć build serwera:

1. Wyewidencjonuj tę samą gałąź, którą wybierasz w polu **Gałąź**.
2. Uruchom build z katalogu głównego repozytorium, aby `COPY . /app` odpowiadało PlaidCloud.
3. Umieść opcjonalne zależności w `requirements.txt` — w katalogu głównym repozytorium lub obok punktu wejścia. Instalowane są oba, plik folderu aplikacji jako ostatni (aby przypięcie dla aplikacji miało pierwszeństwo).
4. Użyj tej samej ścieżki punktu wejścia, którą wybierasz w polu **Punkt wejścia**.

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

Wdrożony obraz nie zastępuje punktu wejścia obrazu bazowego. Uruchamia `panel serve` na podstawie zmiennych środowiskowych wstrzykiwanych przez PlaidCloud. Przetestuj zbudowany obraz z tym samym kontraktem uruchomieniowym:

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

Podczas testów dopasuj ustawienia okna publikacji:

- **Punkt wejścia** odpowiada `APP_PATH=/app/<entry-point>`.
- **CPU** i **Pamięć** odpowiadają limitom Dockera `--cpus` i `--memory`.
- **Projekt: FAST** odpowiada `PLAID_PANEL_DESIGN=fast`.
- **Projekt: Domyślny** oznacza pominięcie `PLAID_PANEL_DESIGN`.
- **Bezczynność (minuty)** odpowiada oknu skalowania w dół we wdrożeniu. Lokalny Docker go nie wymusza, ale aplikacja nadal używa tych samych ustawień podtrzymywania websocketu Panel i czyszczenia sesji.
- Domeny **osadzonego udostępniania** odpowiadają `PANEL_ORIGIN`; użyj listy rozdzielonej spacjami, jeśli musisz przetestować więcej niż jeden host.

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

Użyj `PLAID_PANEL_DESIGN=fast`, aby odpowiadało to domyślnemu wyglądowi wdrożenia. Aby przetestować opcję **Domyślny** projektu w oknie publikacji, pozostaw `PLAID_PANEL_DESIGN` nieustawione i uruchom to samo polecenie. Zachowaj `PANEL_PREFIX`, `PANEL_ORIGIN`, `--keep-alive` i `--unused-session-lifetime`; są częścią kontraktu uruchomieniowego wdrożenia.

## Tworzenie aplikacji WASM

Aplikacja WASM działa w przeglądarce z gotowego pliku HTML.

1. Kliknij **Dodaj aplikację WASM**, aby otworzyć okno **Opublikuj bezserwerową aplikację Panel**.
2. Wpisz **Nazwę aplikacji** i **Wersję**.
3. Wybierz **Lokalizację HTML aplikacji** — plik HTML na koncie dokumentów.
4. Wpisz **Slug URL aplikacji** i opcjonalną **Notatkę**.
5. Kliknij **Opublikuj**. Aplikacja WASM nie ma kroku budowania i jest udostępniana natychmiast.
