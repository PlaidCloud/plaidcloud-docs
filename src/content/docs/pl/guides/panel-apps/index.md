---
title: Aplikacje Panel
description: Twórz i wdrażaj interaktywne aplikacje danych HoloViz Panel w PlaidCloud — jako statyczne aplikacje w przeglądarce lub aplikacje po stronie serwera budowane z repozytorium git.
sidebar:
  label: Aplikacje Panel
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/index.md
---

Aplikacje Panel pozwalają publikować interaktywne aplikacje [HoloViz Panel](https://panel.holoviz.org/) — z parametryzowanymi danymi wejściowymi, wykresami na żywo i osadzonymi tabelami danych — bezpośrednio z PlaidCloud. Zarządzasz nimi z ekranu **Aplikacje**, który wyświetla każdą aplikację wraz z jej środowiskiem uruchomieniowym, stanem kompilacji i adresem URL.

Zacznij od [Panel Studio](/pl/guides/panel-apps/studio/): wybierz **Nowa aplikacja** > **Studio**, aby zbudować aplikację w PlaidCloud z pustej aplikacji, tabeli, widoku lub galerii, bez konfigurowania repozytorium. W indywidualnych potrzebach opublikuj za pomocą jednego z poniższych środowisk uruchomieniowych, pokazanych w kolumnie **Środowisko uruchomieniowe**:

- **WASM** — statyczna aplikacja działająca w całości w przeglądarce (Pyodide). Publikujesz gotowy plik HTML z konta dokumentów. Nie ma procesu serwerowego i nic do skalowania; jest udostępniana natychmiast.
- **Serwer** — aplikacja budowana z repozytorium git i uruchamiana po stronie serwera. Przy publikacji PlaidCloud buduje Twoje repozytorium w kontener, który pozostaje w stanie bezczynności z zerem replik, budzi się przy pierwszym żądaniu do swojego adresu URL, obsługuje ruch (w tym aktualizacje na żywo) i skaluje się z powrotem do zera, gdy jest bezczynny. To właściwy wybór dla aplikacji, które wymagają środowiska Python, obliczeń po stronie serwera lub bibliotek, które nie mogą działać w przeglądarce.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 250" role="img" aria-label="Dwa środowiska uruchomieniowe aplikacji Panel. Aplikacja WASM to gotowy plik HTML udostępniany bezpośrednio przeglądarce bez serwera. Aplikacja serwerowa jest budowana z repozytorium git w kontener, który pozostaje bezczynny z zerem replik, budzi się przy pierwszym żądaniu w około piętnaście sekund, obsługuje ruch i skaluje się z powrotem do zera, gdy jest bezczynny." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pa-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="14" y="40" font-size="12" font-weight="700" fill="var(--sl-color-accent)">WASM</text>
  <rect x="70" y="24" width="150" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="49" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">gotowy plik HTML</text>
  <path d="M220 45 L286 45" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="288" y="24" width="164" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="370" y="43" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">przeglądarka · Pyodide</text>
  <text x="370" y="58" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">udostępniana natychmiast</text>
  <line x1="14" y1="96" x2="666" y2="96" stroke="var(--sl-color-gray-5)" stroke-dasharray="3 3" />
  <text x="14" y="146" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Serwer</text>
  <rect x="70" y="128" width="96" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="118" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">repozytorium git</text>
  <path d="M166 149 L186 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="188" y="128" width="110" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="243" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">budowa kontenera</text>
  <path d="M298 149 L318 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="320" y="128" width="120" height="42" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="380" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">bezczynny · 0 replik</text>
  <text x="380" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">nic nie działa</text>
  <path d="M440 149 L474 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <text x="457" y="140" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">1. żądanie</text>
  <rect x="476" y="128" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="536" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">obsługa ruchu</text>
  <text x="536" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">budzi się ~15 s</text>
  <path d="M536 170 C536 212 380 212 380 174" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#pa-arrow)" />
  <text x="458" y="206" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">skaluje się z powrotem do 0, gdy jest bezczynny</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Dwa środowiska uruchomieniowe: aplikacja <strong>WASM</strong> to gotowy plik HTML udostępniany bezpośrednio przeglądarce; aplikacja <strong>serwerowa</strong> jest budowana z git, pozostaje bezczynna na zerze, budzi się przy pierwszym żądaniu (~15 s), obsługuje ruch i skaluje się z powrotem do zera.</figcaption>
</figure>

## Wybór środowiska uruchomieniowego

| | WASM | Serwer |
|---|---|---|
| Źródło | Opublikowany plik HTML | Repozytorium git (połączenie, gałąź, punkt wejścia) |
| Działa | W przeglądarce | Po stronie serwera, skalowanie do zera |
| Najlepsze dla | Lekkich, samodzielnych pulpitów | Aplikacji wymagających obliczeń serwerowych lub pełnych bibliotek Python |
| Zimny start | Brak | Pierwsze żądanie uruchamia aplikację (~15 sekund) |

## Następne kroki

- [Panel Studio](/pl/guides/panel-apps/studio/) — twórz, edytuj, wyświetlaj podgląd i publikuj aplikację w PlaidCloud, bez konfigurowania repozytorium.
- [Wdrażanie aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/) — kompletna ścieżka od repozytorium do udostępnionej aplikacji, z użyciem zarządzanego połączenia bez poświadczeń.
- [Tworzenie aplikacji Panel za pomocą Weave](/pl/guides/panel-apps/build-with-weave/) — opisz aplikację i zatwierdź dokładną zmianę, którą proponuje Weave.
- [Tworzenie aplikacji Panel](/pl/guides/panel-apps/creating/) — zacznij aplikację Studio od pustej aplikacji, tabeli lub galerii albo opublikuj aplikację serwerową z git lub aplikację WASM z pliku.
- [Zestaw Panel App Kit](/pl/guides/panel-apps/app-kit/) — twórz aplikacje wyglądające jak PlaidCloud, w jasnym i ciemnym motywie, z filtrami, liczbami nagłówkowymi, siatką danych stronicowaną na serwerze, wykresami, formularzami, przyciskami uruchamiania, zapisanymi ustawieniami i drukowaniem.
- [Data API dla aplikacji Panel](/pl/guides/panel-apps/data-api/) — filtruj, stronicuj, zliczaj i agreguj tabele na serwerze.
- [Alerty i podsumowania](/pl/guides/panel-apps/alerts-and-digests/) — otrzymuj powiadomienie push, e-mail albo wiadomość Slack lub Teams, gdy liczba przekroczy limit, lub zaplanowane podsumowanie.
- [Galeria aplikacji](/pl/guides/panel-apps/gallery/) — wystawiaj aplikację jako szablon i twórz nowe aplikacje na podstawie wystawionych.
- [Marka projektu i projekty aplikacji](/pl/guides/panel-apps/branding/) — ustaw kolory i logo dla aplikacji projektu oraz przypisuj aplikacje do projektów.
- [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/) — stan kompilacji, otwieranie aplikacji, edycja i usuwanie.
- [Tworzenie agenta AI wewnątrz aplikacji Panel](/pl/get-started/tutorials/panel-ai-agent/) — samouczek: daj agentowi AI REST API jako jego narzędzia, ograniczone do uprawnień samego przeglądającego.
