---
title: Tworzenie aplikacji Panel
description: Opublikuj w PlaidCloud serwerową aplikację HoloViz Panel z repozytorium git (z przykładem hello-world) lub statyczną aplikację WASM z pliku.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

Otwórz **Moje aplikacje Panel**. Pasek narzędzi oferuje dwa sposoby publikowania, po jednym dla każdego [środowiska uruchomieniowego](/pl/guides/panel-apps/):

- **Nowa aplikacja serwerowa** — zbuduj i uruchom aplikację z repozytorium git.
- **Dodaj aplikację WASM** — opublikuj statyczną aplikację działającą w przeglądarce z pliku.

Aby napisać aplikację w PlaidCloud, bez konfigurowania repozytorium, użyj [Panel Studio](/pl/guides/panel-apps/studio/).

## Tworzenie aplikacji serwerowej

Aplikacja serwerowa jest budowana z repozytorium git i udostępniana pod adresem `https://<your-tenant-host>/serve/<slug>/`. Wskazujesz PlaidCloud gałąź repozytorium; buduje on kod w kontener, uruchamia na nim `panel serve` i automatycznie przebudowuje go przy każdym wypchnięciu zmian do tej gałęzi.

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

To kompletna aplikacja. PlaidCloud udostępnia to, co wywołuje `.servable()` — wszystko, co ma zostać wyrenderowane, musi być oznaczone jako servable (bezpośrednio lub przez umieszczenie w układzie, który jest servable).

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

PlaidCloud instaluje je za pomocą `pip` podczas budowania obrazu. Popularne biblioteki wizualizacji — `plotly`, `holoviews`, `hvplot` — również nie ma w obrazie bazowym, więc wymień tu te, które importuje Twoja aplikacja.

> **Co platforma zapewnia — i czego oczekuje.** Pamiętaj o tych założeniach podczas pisania aplikacji:
>
> - **`panel` i `bokeh` są preinstalowane** w obrazie bazowym platformy. Nie wymieniaj ich w `requirements.txt` i unikaj przypinania starszej wersji Panel — ponowne łączenie przy aktualizacjach na żywo wymaga nowej wersji.
> - **Biblioteki klienckie PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) są preinstalowane.** Importuj `plaidcloud.rpc` lub `plaidcloud.utilities` bezpośrednio — nie wymieniaj ich w `requirements.txt`.
> - **`requirements.txt` może znajdować się w katalogu głównym repozytorium lub obok punktu wejścia.** We współdzielonym repozytorium (monorepo) trzymaj zależności każdej aplikacji w jej własnym folderze. Plik w katalogu głównym, jeśli istnieje, również jest instalowany — umieść w nim zależności współdzielone, a specyficzne dla aplikacji obok niej.
> - **Aplikacja działa jako użytkownik inny niż root w systemie plików tylko do odczytu.** Zapisywalny jest tylko `/tmp`, więc zapisuj tam wszelkie pliki tymczasowe (większość bibliotek już respektuje `$TMPDIR`).
> - **Nie koduj na stałe portu, prefiksu URL ani hosta.** PlaidCloud przypisuje je i wstrzykuje podczas wdrażania — po prostu wywołaj `.servable()`.

Aby uzyskać wygląd PlaidCloud oraz gotowe filtry, siatki i wykresy, zbuduj aplikację za pomocą [zestawu narzędzi aplikacji Panel](/pl/guides/panel-apps/app-kit/).

### Ustawianie motywu: jasny, ciemny lub przełącznik

Aplikacje serwerowe domyślnie renderują się we współczesnym wyglądzie **Fast** PlaidCloud — czystym, w stylu Fluent, stosowanym w całej platformie. W oknie publikowania **Projekt** steruje tą warstwą platformy:

- **FAST** — wartość domyślna PlaidCloud. Użyj jej dla nowych aplikacji i aplikacji zbudowanych z szablonami Fast.
- **Domyślny** — domyślna stylizacja Panel. Użyj jej, gdy CSS lub elementy wizualne istniejącej aplikacji przestają działać pod FAST.

To, co kontrolujesz w kodzie aplikacji, to **motyw**: jasny, ciemny lub przełącznik, który może przestawić przeglądający.

Motyw jest właściwością **szablonu**, który udostępniasz. Szablony Fast — `FastListTemplate` (jedna kolumna) i `FastGridTemplate` (siatka responsywna) — przyjmują dla niego dwa ustawienia:

- **`theme`** — `"default"` dla jasnego lub `"dark"`. Ustawienie go przypina aplikację do tego motywu, nawet jeśli przeglądający doda `?theme=dark` do adresu URL.
- **`theme_toggle`** — `True` pokazuje w nagłówku przełącznik jasny/ciemny; `False` go ukrywa. Domyślnie `True`. Ukrycie przełącznika samo nie ustala motywu — przypnij go za pomocą `theme` (powyżej); ustaw `theme_toggle=False` dopiero wtedy, aby przeglądający nie widzieli przełącznika, który niczego nie zmienia.

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

**Pozwól wybrać przeglądającemu** — domyślnie jasny, z przełącznikiem w nagłówku. Pomiń `theme`, aby podążał za przełącznikiem:

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **Jeśli dopuszczasz tryb ciemny, dostosuj tabele do niego.** `Tabulator` przypięty do jasnego motywu tabeli (`theme="bootstrap"`) lub własny CSS z twardo zakodowanymi jasnymi kolorami, takimi jak `background: #fff`, renderuje się jako nieczytelny biały blok na ciemnej stronie. Użyj motywu tabeli, który podąża za aplikacją — `pn.widgets.Tabulator(..., theme="fast")` — i unikaj twardo zakodowanych jasnych kolorów. Jeśli raport jest mocno ręcznie stylizowany pod jasny tryb, przypnij go do jasnego (pierwszy wzorzec powyżej).

Zwykła aplikacja bez szablonu — `pn.Column(...).servable()` — podąża za domyślnymi ustawieniami Panel i nie podlega tym ustawieniom; sięgnij po szablon, gdy chcesz mieć jawną kontrolę.

Repozytorium musi być osiągalne przez **połączenie git** w PlaidCloud. Jeśli Twój kod znajduje się w [PlaidCloud Git](/pl/guides/git/), utwórz zarządzane połączenie **PlaidCloud Git** w **Tools > Connections** — nie wymaga adresu URL serwera ani poświadczeń. Całą ścieżkę od pustego repozytorium do działającej aplikacji opisuje [Wdrażanie aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/).

### Publikowanie aplikacji

1. Kliknij **Nowa aplikacja serwerowa**, aby otworzyć okno **Opublikuj serwerową aplikację Panel**. Jego ustawienia są pogrupowane w sekcje.
2. W sekcji **Ustawienia katalogu**:
   - **Nazwa aplikacji** — nazwa wyświetlana na liście.
   - **Slug URL** — zarówno adres URL aplikacji, jak i jej nazwa wewnętrzna, więc musi być prawidłową etykietą DNS: małe litery, cyfry i łączniki, zaczynająca się od litery, maksymalnie 40 znaków (na przykład `sales-dashboard`). Okno sprawdza to przed opublikowaniem.
   - **Notatka** — opcjonalny opis.
   - **Projekt** — projekt, do którego należy aplikacja. Dostarcza [branding](/pl/guides/panel-apps/branding/) aplikacji i jest projektem domyślnym dla jej tabel. Po opublikowaniu nie można go tu zmienić; użyj [Przypisz](/pl/guides/panel-apps/branding/#dla-istniejących-aplikacji).
3. W sekcji **Połączenie Git i obserwator publikacji**:
   - **Połączenie Git** — połączenie przechowujące repozytorium aplikacji.
   - **Gałąź** — gałąź, z której ma być budowana aplikacja. Wypchnięcia do tej gałęzi automatycznie przebudowują i ponownie wdrażają aplikację.
   - **Punkt wejścia** — plik `.py`, który Panel ma udostępniać (Twój `app.py`).
4. W sekcji **Środowisko uruchomieniowe**:
   - **CPU** i **Pamięć**, o które ma prosić kontener aplikacji.

     > Mniej zasobów (niższe CPU / pamięć) pozwala aplikacji szybciej się zaplanować i uruchomić od zera.

   - **Projekt** — wybierz **FAST** dla nowoczesnego wyglądu PlaidCloud lub **Domyślny**, jeśli CSS aplikacji oczekuje domyślnej stylizacji Panel.
   - **Bezczynność (minuty)** — jak długo aplikacja pozostaje gotowa bez ruchu, zanim skaluje się z powrotem do zera. Wartość domyślna to 5 minut.
   - **Zezwól na dostęp publiczny** — zaznacz, aby zezwolić na dostęp bez uwierzytelniania; w przeciwnym razie przeglądający muszą zalogować się do Twojego tenanta.
5. W sekcji **Zaawansowane (osadzone udostępnianie)** — opcjonalnie. Domyślnie aplikacja jest udostępniana wyłącznie z Twojego tenanta PlaidCloud. Aby osadzić ją w innej witrynie, kliknij **Dodaj domenę** i wprowadź każdą domenę, która może ją ładować, po jednej w wierszu — tylko host, bez schematu i ścieżki (na przykład `example.com` lub `app.example.com:8443`). Pozostaw listę pustą, chyba że osadzasz aplikację gdzie indziej.
6. Kliknij **Opublikuj**.

Po opublikowaniu aplikacja jest **budowana** — jej **Stan** jest widoczny na liście i aktualizuje się automatycznie. W artykule [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/) dowiesz się, co oznaczają stany, jak otworzyć aplikację, gdy będzie gotowa, i jak wywołać przebudowę bez cofania publikacji.

> Adres URL aplikacji działa dopiero wtedy, gdy jej stan kompilacji to **Gotowe**, a pierwsze żądanie po okresie bezczynności uruchamia ją (~15 sekund).

### Zaawansowane: odtworzenie środowiska PlaidCloud lokalnie

Użytkownicy techniczni mogą zbudować i przetestować aplikację z tymi samymi danymi wejściowymi, których używa PlaidCloud. To najbliższe lokalne sprawdzenie przed opublikowaniem lub kliknięciem **Zbuduj ponownie**.

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

Aby odtworzyć kompilację serwerową:

1. Wyewidencjonuj tę samą gałąź, którą wybierasz w polu **Gałąź**.
2. Uruchom kompilację z katalogu głównego repozytorium, aby `COPY . /app` zgadzało się z PlaidCloud.
3. Umieść opcjonalne zależności w pliku `requirements.txt` — w katalogu głównym repozytorium lub obok punktu wejścia. Oba są instalowane, ten z folderu aplikacji jako ostatni (aby przypięcie per aplikacja miało pierwszeństwo).
4. Użyj tej samej ścieżki punktu wejścia, którą wybierasz w polu **Punkt wejścia**.

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

Wdrożony obraz nie nadpisuje punktu wejścia obrazu bazowego. Uruchamia `panel serve` ze zmiennych środowiskowych wstrzykiwanych przez PlaidCloud. Przetestuj zbudowany obraz z tym samym kontraktem uruchomieniowym:

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

Podczas testów dopasuj ustawienia okna publikowania:

- **Punkt wejścia** odpowiada `APP_PATH=/app/<entry-point>`.
- **CPU** i **Pamięć** odpowiadają limitom Dockera `--cpus` i `--memory`.
- **Projekt: FAST** odpowiada `PLAID_PANEL_DESIGN=fast`.
- **Projekt: Domyślny** oznacza pominięcie `PLAID_PANEL_DESIGN`.
- **Bezczynność (minuty)** odpowiada oknu skalowania w dół we wdrożeniu. Lokalny Docker go nie egzekwuje, ale aplikacja nadal używa tych samych ustawień podtrzymywania połączenia websocket Panel i czyszczenia sesji.
- Domeny **osadzonego udostępniania** odpowiadają `PANEL_ORIGIN`; użyj listy rozdzielonej spacjami, jeśli chcesz przetestować więcej niż jednego hosta.

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

Użyj `PLAID_PANEL_DESIGN=fast`, aby odpowiadać domyślnemu wdrożonemu wyglądowi. Aby przetestować opcję **Domyślny** z okna publikowania, pozostaw `PLAID_PANEL_DESIGN` nieustawione i uruchom to samo polecenie. Zachowaj `PANEL_PREFIX`, `PANEL_ORIGIN`, `--keep-alive` i `--unused-session-lifetime`; są częścią kontraktu uruchomieniowego wdrożenia.

## Tworzenie aplikacji WASM

Aplikacja WASM działa w przeglądarce z gotowego pliku HTML.

1. Kliknij **Dodaj aplikację WASM**, aby otworzyć okno **Opublikuj bezserwerową aplikację Panel**.
2. Wprowadź **Nazwa aplikacji** i **Wersja**.
3. Wybierz **Lokalizacja HTML aplikacji** — plik HTML na koncie dokumentów.
4. Wprowadź **Slug URL aplikacji** i opcjonalną **Notatka**.
5. Kliknij **Opublikuj**. Aplikacja WASM nie ma etapu kompilacji i jest udostępniana natychmiast.
