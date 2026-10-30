---
title: Panel Studio
description: Twórz, edytuj, wyświetlaj podgląd i publikuj aplikacje Panel bez opuszczania PlaidCloud — następnie przywróć wcześniejszą wersję, sprawdź użycie i szybkość aplikacji, skonfiguruj alerty i podsumowania, umieść ją w galerii i przypnij do strony głównej.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio to edytor aplikacji Panel wewnątrz PlaidCloud. Pokazuje pliki aplikacji obok edytora, buduje prywatny podgląd, który możesz otworzyć, i publikuje aplikację, gdy jesteś gotowy. Aby zacząć, nie potrzebujesz repozytorium git.

## Otwieranie Panel Studio

- Na tablicy **Strona główna** projektu wybierz **Otwórz w Studio** przy aplikacji Panel.
- W **Moje aplikacje Panel** wybierz **Otwórz w Studio** w wierszu aplikacji.

Aby zacząć nową aplikację, wybierz **Nowa aplikacja Studio**. To pierwszy przycisk na pasku narzędzi **Moje aplikacje Panel** i znajduje się w polu **Aplikacje Panel** na karcie **Strona główna** projektu. Aby zbudować aplikację na tabeli, wybierz ją na karcie **Tabele** projektu i wybierz **Utwórz aplikację Panel**.

## Tworzenie aplikacji

Okno **Nowa aplikacja Studio** pozwala zacząć z jednego z pięciu miejsc:

| Zacznij od | Otrzymujesz |
|---|---|
| **Pusta aplikacja** | Minimalną aplikację z plikami `app.py` i `requirements.txt`. |
| **Z tabeli** | Aplikację zbudowaną na wybranej tabeli. |
| **Z widoku** | To samo, zbudowane na widoku projektu. |
| **Z innej aplikacji Studio** | Kopię jednej z Twoich aplikacji Studio. |
| **Z galerii** | Kopię aplikacji, którą Twój obszar roboczy umieścił w [galerii aplikacji](/pl/guides/panel-apps/gallery/). |

Nazwij aplikację, wybierz jej **Projekt** i wybierz **Utwórz**. Studio otwiera nową aplikację z listą plików po lewej stronie. Dla tabeli lub widoku gotowy do wysłania jest monit Weave o zbudowanie pierwszej strony aplikacji. Zobacz [Tworzenie aplikacji Panel](/pl/guides/panel-apps/creating/).

## Edycja

Wybierz plik z listy, aby edytować go w edytorze. Zależności Python wymień w `requirements.txt`, jeden pakiet w wierszu. Są instalowane podczas budowania aplikacji.

Wybierz **Zapytaj Weave**, aby Weave napisał lub zmienił aplikację za Ciebie. Zobacz [Budowanie aplikacji Panel z Weave](/pl/guides/panel-apps/build-with-weave/).

## Zapis, podgląd i publikacja

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Zapis zachowuje wersję roboczą widoczną tylko dla Ciebie. Podgląd buduje prywatną kopię wersji roboczej dla edytora. Publikacja zastępuje działającą aplikację po potwierdzeniu." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Zapisz</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">tylko wersja robocza</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Podgląd</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">tylko edytor</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Opublikuj</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">działająca aplikacja</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Twoje zmiany docierają do oglądających dopiero po opublikowaniu.</figcaption>
</figure>

### Zapis

**Zapisz** przechowuje Twoje zmiany jako wersję roboczą. Działająca aplikacja się nie zmienia, a nikt inny nie widzi wersji roboczej.

### Podgląd

**Podgląd** buduje zapisaną wersję roboczą jako prywatną kopię i ją otwiera. Podgląd mogą otworzyć tylko edytorzy aplikacji.

- Podgląd jest usuwany po 24 godzinach bez zapisu.
- Obszar roboczy może mieć jednocześnie do 10 podglądów.
- Zapisz ponownie i wybierz **Podgląd**, aby zobaczyć najnowsze zmiany.

### Publikacja

**Opublikuj** zastępuje działającą aplikację zapisaną wersją roboczą. Wymaga uprawnienia do edycji w projekcie aplikacji, a Studio najpierw prosi o potwierdzenie.

Jeśli ktoś inny opublikował zmianę po otwarciu przez Ciebie aplikacji, Studio zgłasza konflikt zamiast nadpisać jego pracę. Załaduj aplikację ponownie, przenieś swoje zmiany i opublikuj jeszcze raz.

## Stan budowania i błędy

Karta **Build** pokazuje stan ostatniego budowania i aktualizuje się w trakcie jego trwania. Gdy budowanie się nie powiedzie, karta wymienia każdy błąd z plikiem i numerem wiersza, aby można było przejść prosto do wiersza. Problemy z zależnościami w `requirements.txt` zawierają podpowiedź, jak je naprawić.

Błędy i ostrzeżenia są też zaznaczone w odpowiednich wierszach w edytorze, więc widzisz problem tam, gdzie jest.

Co oznacza każdy stan po opublikowaniu aplikacji, zobacz w [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/#stan-kompilacji-aplikacje-serwerowe).

## Historia i przywracanie

Karta **Historia** wymienia każdą opublikowaną wersję aplikacji, od najnowszej, wraz z jej stanem budowania. Wybierz **Załaduj więcej**, aby zobaczyć starsze.

Aby wrócić do wcześniejszej wersji, wybierz **Przywróć** przy niej i potwierdź. Przywrócona wersja staje się działającą aplikacją i jest budowana ponownie. Twoja niezapisana wersja robocza nie przepada: pozostaje w wersji roboczej i trafia na żywo na przywróconą wersję przy następnej publikacji. Jeśli aplikacja już odpowiada tej wersji, Studio to zgłasza i niczego nie zmienia. Jeśli ktoś opublikował zmiany w trakcie przywracania, Studio niczego nie przywraca i prosi o ponowną próbę.

## Wgląd

Karta **Wgląd** pokazuje, jak ludzie używają aplikacji i jak szybko reaguje. Wybierz ostatnie 7, 14 lub 30 dni.

| Sekcja | Pokazuje |
|---|---|
| **Wyświetlenia dziennie** | Ile razy aplikacja była otwierana każdego dnia. |
| **Czas ładowania strony** | Medianę czasu ładowania oraz czas, który pokonuje 95 procent ładowań, na podstawie ładowań stron w danym okresie. |
| **Najwolniejsze zapytania** | Zapytania, które trwały najdłużej, z informacją, jak często były uruchamiane, oraz ich medianą, czasem na wolnym końcu i najwolniejszym czasem. |
| **Błędy** | Co poszło nie tak w okresie, według rodzaju błędu i miejsca w aplikacji, w którym wystąpił. |

Gdy okres zawiera więcej aktywności, niż Wgląd może odczytać, informuje, że dane są częściowe. Gdy ładowania stron przekraczają [budżet wydajności](/pl/guides/panel-apps/app-kit/#budżety-wydajności) aplikacji, Wgląd ostrzega, ile ich było i które zapytania były wolne. Wgląd nigdy nie pokazuje danych zwróconych przez zapytanie ani nazw osób, które otworzyły aplikację.

Obie karty wymagają, aby aplikacja była przypisana do projektu; nieprzypisana aplikacja pokazuje monit o przypisanie.

## Alerty i podsumowania

Wybierz **Alerty i zestawienia**, aby skonfigurować powiadomienia, które obserwują liczbę w danych aplikacji i informują, gdy przekroczy limit, lub wysyłają podsumowanie według harmonogramu. Zobacz [Alerty i podsumowania](/pl/guides/panel-apps/alerts-and-digests/).

## Umieszczanie aplikacji w galerii

Wybierz **Galeria…** w Studio. Wybierz **Wyświetlaj w galerii**, aby umieścić aplikację jako szablon, na podstawie którego każdy, kto może wyświetlić jej projekt, może utworzyć własną aplikację, albo **Usuń z galerii**, aby ją usunąć. Przycisk jest dostępny dla aplikacji należących do projektu. Potrzebujesz dostępu do edycji projektu. Zobacz [Galeria aplikacji](/pl/guides/panel-apps/gallery/).

## Przypinanie do strony głównej

Wybierz **Przypnij do strony głównej**, aby dodać aplikację do tablicy **Strona główna** projektu, a **Odepnij od strony głównej**, aby ją usunąć.

## Usuwanie aplikacji

Usunięcie aplikacji Panel najpierw prosi o potwierdzenie. W **Moje aplikacje Panel** użyj ikony **minus** w wierszu aplikacji. Cofnięcie publikacji również prosi o potwierdzenie.

## Dalsze kroki

- [Budowanie aplikacji Panel z Weave](/pl/guides/panel-apps/build-with-weave/) — opisz aplikację i zatwierdź dokładną zmianę.
- [Zestaw Panel App Kit](/pl/guides/panel-apps/app-kit/) — komponenty, których używają początki Studio z tabeli i widoku.
- [Alerty i podsumowania](/pl/guides/panel-apps/alerts-and-digests/) — powiadamiaj ludzi, gdy liczba przekroczy limit, lub według harmonogramu.
- [Galeria aplikacji](/pl/guides/panel-apps/gallery/) — udostępnij aplikację jako punkt wyjścia dla innych.
- [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/) — dzienniki, użycie i przebudowania po opublikowaniu.
