---
title: Panel Studio
description: Twórz, edytuj, przeglądaj i publikuj aplikacje Panel bez opuszczania PlaidCloud — następnie przywracaj wcześniejszą wersję, sprawdzaj użycie i szybkość aplikacji, konfiguruj alerty i podsumowania, wystawiaj ją w galerii i przypinaj do strony głównej.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio to edytor aplikacji Panel wewnątrz PlaidCloud. Pokazuje pliki aplikacji obok edytora, buduje prywatny podgląd, który możesz otworzyć, i publikuje aplikację, gdy jesteś gotowy. Nie potrzebujesz repozytorium git, aby zacząć.

## Otwieranie Panel Studio

- Na tablicy **Strona główna** projektu wybierz **Open in Studio** przy aplikacji Panel.
- W **Moje aplikacje Panel** wybierz **Open in Studio** w wierszu aplikacji.

Aby rozpocząć nową aplikację, wybierz **Create app** w jednym z tych miejsc.

## Tworzenie aplikacji

Okno **Create app** pozwala zacząć od jednego z pięciu miejsc:

| Zacznij od | Otrzymujesz |
|---|---|
| **Blank** | Minimalną aplikację z plikami `app.py` i `requirements.txt`. |
| **Tabela** | Aplikację zbudowaną na wybranej tabeli. |
| **Widok** | To samo, zbudowane na widoku projektu. |
| **Szablon** | Gotową aplikację z [zestawu narzędzi aplikacji Panel](/pl/guides/panel-apps/app-kit/#zacznij-od-szablonu). |
| **From the gallery** | Kopię aplikacji wystawionej przez Twój obszar roboczy w [galerii aplikacji](/pl/guides/panel-apps/gallery/). |

Nazwij aplikację, wybierz jej **Projekt** i wybierz **Utwórz**. Studio otwiera nową aplikację z listą plików po lewej stronie.

## Edycja

Wybierz plik z listy, aby edytować go w edytorze. Wymień zależności Python w `requirements.txt`, jeden pakiet w wierszu. Są one instalowane podczas budowania aplikacji.

Wybierz **Ask Weave**, aby Weave napisał lub zmienił aplikację za Ciebie. Zobacz [Tworzenie aplikacji Panel z Weave](/pl/guides/panel-apps/build-with-weave/).

## Zapis, podgląd i publikowanie

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Zapis zachowuje wersję roboczą, którą widzisz tylko Ty. Podgląd buduje prywatną kopię wersji roboczej dla edytora. Publikowanie zastępuje działającą aplikację po Twoim potwierdzeniu." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Zapisz</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">tylko wersja robocza</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Podgląd</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">tylko dla edytora</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Opublikuj</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">działająca aplikacja</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Twoje zmiany docierają do przeglądających dopiero po opublikowaniu.</figcaption>
</figure>

### Zapis

**Zapisz** przechowuje zmiany jako wersję roboczą. Działająca aplikacja się nie zmienia, a nikt inny nie widzi wersji roboczej.

### Podgląd

**Podgląd** buduje zapisaną wersję roboczą jako prywatną kopię i ją otwiera. Podgląd mogą otworzyć tylko edytorzy aplikacji.

- Podgląd jest usuwany po 24 godzinach bez zapisu.
- Obszar roboczy może mieć jednocześnie do 10 podglądów.
- Zapisz ponownie i wybierz **Podgląd**, aby zobaczyć najnowsze zmiany.

### Publikowanie

**Opublikuj** zastępuje działającą aplikację zapisaną wersją roboczą. Wymaga uprawnienia do edycji projektu aplikacji, a Studio najpierw prosi o potwierdzenie.

Jeśli ktoś inny opublikował zmianę po otwarciu przez Ciebie aplikacji, Studio zgłasza konflikt zamiast nadpisać jego pracę. Wczytaj aplikację ponownie, przenieś swoje zmiany i opublikuj jeszcze raz.

## Stan kompilacji i błędy

Karta **Zbuduj** pokazuje stan najnowszej kompilacji i aktualizuje się w trakcie jej trwania. Gdy kompilacja się nie powiedzie, karta wymienia każdy błąd wraz z plikiem i numerem wiersza, abyś mógł przejść prosto do wiersza. Problemy z zależnościami w `requirements.txt` zawierają wskazówkę dotyczącą naprawy.

Błędy i ostrzeżenia są też oznaczone w swoich wierszach w edytorze, więc widzisz problem tam, gdzie jest.

Co oznacza każdy stan po opublikowaniu aplikacji, wyjaśnia [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/#stan-kompilacji-aplikacje-serwerowe).

## Historia i przywracanie

Karta **Historia** wymienia wszystkie opublikowane wersje aplikacji, od najnowszej, wraz ze stanem kompilacji. Wybierz **Załaduj więcej**, aby zobaczyć starsze.

Aby wrócić do wcześniejszej wersji, wybierz przy niej **Przywróć** i potwierdź. Przywrócona wersja staje się działającą aplikacją i jest przebudowywana. Twoja niezapisana wersja robocza nie przepada: pozostaje w wersji roboczej i zacznie działać na wierzchu przywróconej wersji przy następnym opublikowaniu. Jeśli aplikacja już odpowiada tej wersji, Studio informuje o tym i niczego nie zmienia. Jeśli ktoś opublikował zmiany w trakcie przywracania, Studio niczego nie przywraca i prosi o ponowną próbę.

## Wgląd

Karta **Wgląd** pokazuje, jak ludzie korzystają z aplikacji i jak szybko ona odpowiada. Wybierz ostatnie 7, 14 lub 30 dni.

| Sekcja | Pokazuje |
|---|---|
| **Views per day** | Ile razy aplikacja była otwierana każdego dnia. |
| **Page load** | Medianę czasu ładowania oraz czas, który pokonuje 95 procent wczytań, na podstawie wczytań stron w danym okresie. |
| **Slowest queries** | Zapytania, które trwały najdłużej, wraz z liczbą ich uruchomień oraz ich medianą, czasem na wolnym końcu i najwolniejszym czasem. |
| **Błędy** | Co poszło nie tak w danym okresie, według rodzaju błędu i miejsca w aplikacji, w którym wystąpił. |

Gdy okres zawiera więcej aktywności, niż Wgląd potrafi odczytać, informuje, że liczby są częściowe. Gdy wczytania stron przekraczają [budżet wydajności](/pl/guides/panel-apps/app-kit/#budżety-wydajności) aplikacji, Wgląd ostrzega, ile ich było i które zapytania były wolne. Wgląd nigdy nie pokazuje danych zwróconych przez zapytanie ani nazw osób, które otworzyły aplikację.

Obie karty wymagają przypisania aplikacji do projektu; nieprzypisana aplikacja pokazuje monit o przypisanie.

## Alerty i podsumowania

Wybierz **Alerts & Digests**, aby skonfigurować powiadomienia, które obserwują liczbę w danych aplikacji i informują, gdy przekroczy ona limit, lub wysyłają podsumowanie według harmonogramu. Zobacz [Alerty i podsumowania](/pl/guides/panel-apps/alerts-and-digests/).

## Wystawianie aplikacji w galerii

Wybierz **Gallery…**, aby wystawić aplikację jako szablon, na podstawie którego każdy, kto może wyświetlać jej projekt, może utworzyć własną aplikację, lub aby usunąć ją z galerii. Zobacz [Galeria aplikacji](/pl/guides/panel-apps/gallery/).

## Przypinanie do strony głównej

Wybierz **Pin to Home**, aby dodać aplikację do tablicy **Strona główna** projektu, a **Unpin from Home**, aby ją usunąć.

## Usuwanie aplikacji

Usunięcie aplikacji Panel najpierw prosi o potwierdzenie. W **Moje aplikacje Panel** użyj ikony **minus** w wierszu aplikacji. Cofnięcie publikacji również prosi o potwierdzenie.

## Następne kroki

- [Tworzenie aplikacji Panel z Weave](/pl/guides/panel-apps/build-with-weave/) — opisz aplikację i zatwierdź dokładną zmianę.
- [Zestaw narzędzi aplikacji Panel](/pl/guides/panel-apps/app-kit/) — komponenty, z których korzystają starty ze Studio z tabeli, widoku i szablonu.
- [Alerty i podsumowania](/pl/guides/panel-apps/alerts-and-digests/) — powiadamiaj osoby, gdy liczba przekroczy limit, lub według harmonogramu.
- [Galeria aplikacji](/pl/guides/panel-apps/gallery/) — udostępnij aplikację jako punkt wyjścia dla innych.
- [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/) — dzienniki, użycie i przebudowy po opublikowaniu.
