---
title: Aplikacje Panel
description: Twórz i wdrażaj interaktywne aplikacje danych HoloViz Panel w PlaidCloud — jako statyczne aplikacje działające w przeglądarce lub aplikacje serwerowe budowane z repozytorium git.
sidebar:
  label: Aplikacje Panel
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/index.md
---

Aplikacje Panel pozwalają publikować interaktywne aplikacje [HoloViz Panel](https://panel.holoviz.org/) — z parametryzowanymi danymi wejściowymi, wykresami na żywo i osadzonymi tabelami danych — bezpośrednio z PlaidCloud. Zarządzasz nimi z ekranu **Moje aplikacje Panel**, który wymienia każdą aplikację wraz z jej środowiskiem uruchomieniowym, stanem kompilacji i adresem URL.

Są dwa środowiska uruchomieniowe, widoczne w kolumnie **Środowisko uruchomieniowe**:

- **WASM** — statyczna aplikacja działająca w całości w przeglądarce (Pyodide). Publikujesz gotowy plik HTML z konta dokumentów. Nie ma procesu serwerowego ani niczego do skalowania; aplikacja jest udostępniana natychmiast.
- **Serwer** — aplikacja budowana z repozytorium git i uruchamiana po stronie serwera. Podczas publikowania PlaidCloud buduje repozytorium w kontener, który pozostaje bezczynny przy zerze replik, budzi się przy pierwszym żądaniu do swojego adresu URL, obsługuje ruch (w tym aktualizacje na żywo) i skaluje się z powrotem do zera, gdy jest bezczynny. To właściwy wybór dla aplikacji, które potrzebują środowiska Python, obliczeń po stronie serwera lub bibliotek niemożliwych do uruchomienia w przeglądarce.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 250" role="img" aria-label="Dwa środowiska uruchomieniowe aplikacji Panel. Aplikacja WASM to gotowy plik HTML udostępniany prosto do przeglądarki bez serwera. Aplikacja serwerowa jest budowana z repozytorium git w kontener, który pozostaje bezczynny przy zerze replik, budzi się przy pierwszym żądaniu po około piętnastu sekundach, obsługuje ruch i skaluje się z powrotem do zera, gdy jest bezczynny." style="width:100%;max-width:680px;height:auto;">
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
  <text x="118" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">repo git</text>
  <path d="M166 149 L186 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="188" y="128" width="110" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="243" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">budowa kontenera</text>
  <path d="M298 149 L318 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="320" y="128" width="120" height="42" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="380" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">bezczynna · 0 replik</text>
  <text x="380" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">nic nie działa</text>
  <path d="M440 149 L474 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <text x="457" y="140" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">1. żądanie</text>
  <rect x="476" y="128" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="536" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">obsługa ruchu</text>
  <text x="536" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">budzi się ~15 s</text>
  <path d="M536 170 C536 212 380 212 380 174" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#pa-arrow)" />
  <text x="458" y="206" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">skaluje się z powrotem do 0, gdy bezczynna</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Dwa środowiska uruchomieniowe: aplikacja <strong>WASM</strong> to gotowy plik HTML udostępniany prosto do przeglądarki; aplikacja <strong>Serwer</strong> jest budowana z git, pozostaje bezczynna przy zerze, budzi się przy pierwszym żądaniu (~15 s), obsługuje ruch i skaluje się z powrotem do zera.</figcaption>
</figure>

## Wybór środowiska uruchomieniowego

| | WASM | Serwer |
|---|---|---|
| Źródło | Opublikowany plik HTML | Repozytorium git (połączenie, gałąź, punkt wejścia) |
| Działa | W przeglądarce | Po stronie serwera, ze skalowaniem do zera |
| Najlepsze dla | Lekkich, samodzielnych pulpitów | Aplikacji wymagających obliczeń po stronie serwera lub pełnych bibliotek Python |
| Zimny start | Brak | Pierwsze żądanie uruchamia aplikację (~15 sekund) |

## Następne kroki

- [Wdrażanie aplikacji Panel z PlaidCloud Git](/pl/guides/panel-apps/deploy-from-git/) — kompletna ścieżka od repozytorium do udostępnionej aplikacji, z użyciem zarządzanego połączenia bez poświadczeń.
- [Panel Studio](/pl/guides/panel-apps/studio/) — twórz, edytuj, przeglądaj i publikuj aplikację w PlaidCloud, bez konfigurowania repozytorium.
- [Tworzenie aplikacji Panel z Weave](/pl/guides/panel-apps/build-with-weave/) — opisz aplikację i zatwierdź dokładną zmianę, którą proponuje Weave.
- [Tworzenie aplikacji Panel](/pl/guides/panel-apps/creating/) — opublikuj aplikację serwerową z git lub aplikację WASM z pliku.
- [Zestaw narzędzi aplikacji Panel](/pl/guides/panel-apps/app-kit/) — twórz aplikacje wyglądające jak PlaidCloud, w trybie jasnym i ciemnym, z filtrami, głównymi liczbami, siatką danych stronicowaną na serwerze, wykresami, formularzami, przyciskami uruchamiania, zapisanymi ustawieniami i drukowaniem.
- [Data API dla aplikacji Panel](/pl/guides/panel-apps/data-api/) — filtruj, stronicuj, zliczaj i agreguj tabele na serwerze.
- [Alerty i podsumowania](/pl/guides/panel-apps/alerts-and-digests/) — otrzymuj powiadomienie push, e-mail lub wiadomość w Slack albo Teams, gdy liczba przekroczy limit, lub zaplanowane podsumowanie.
- [Galeria aplikacji](/pl/guides/panel-apps/gallery/) — wystaw aplikację jako szablon i twórz nowe aplikacje na podstawie wystawionych.
- [Branding projektu i projekty aplikacji](/pl/guides/panel-apps/branding/) — ustaw kolory i logo aplikacji projektu oraz przypisuj aplikacje do projektów.
- [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/) — stan kompilacji, otwieranie aplikacji, edycja i usuwanie.
- [Tworzenie agenta AI wewnątrz aplikacji Panel](/pl/get-started/tutorials/panel-ai-agent/) — samouczek: daj agentowi AI REST API jako narzędzia, ograniczone do własnych uprawnień przeglądającego.
