---
title: Panel Studio
description: Twórz, edytuj, wyświetlaj w podglądzie i publikuj aplikacje Panel bez opuszczania PlaidCloud — następnie przywracaj wcześniejszą wersję, sprawdzaj użycie i szybkość aplikacji, konfiguruj alerty i zestawienia, wyświetlaj ją w galerii i przypinaj do strony głównej.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio to edytor aplikacji Panel w PlaidCloud. Pokazuje pliki aplikacji obok edytora, buduje prywatny podgląd, który możesz otworzyć, i publikuje aplikację, gdy jesteś gotowy. Aby zacząć, nie potrzebujesz repozytorium git.

## Otwieranie Panel Studio

- Na tablicy **Strona główna** projektu wybierz **Otwórz w Studio** przy aplikacji Panel.
- W **Moje aplikacje Panel** wybierz **Studio** w wierszu aplikacji.

Aby rozpocząć nową aplikację, wybierz **Nowa aplikacja Studio**. To pierwszy przycisk na pasku narzędzi **Moje aplikacje Panel**, a także w polu **Aplikacje Panel** na karcie **Strona główna** projektu. Aby zbudować aplikację na tabeli, zaznacz ją na karcie **Tabele** projektu i wybierz **Utwórz aplikację Panel**.

## Tworzenie aplikacji

Okno **Nowa aplikacja Studio** pozwala zacząć z jednego z pięciu miejsc:

| Zacznij od | Otrzymujesz |
|---|---|
| **Pusta aplikacja** | Minimalną aplikację z plikami `app.py` i `requirements.txt`. |
| **Z tabeli** | Aplikację zbudowaną na wybranej tabeli. |
| **Z widoku** | To samo, zbudowane na widoku projektu. |
| **Z innej aplikacji Studio** | Kopię jednej z Twoich aplikacji Studio. |
| **Z galerii** | Kopię aplikacji, którą Twój obszar roboczy wyświetlił w [galerii aplikacji](/pl/guides/panel-apps/gallery/). |

Nazwij aplikację, wybierz jej **Projekt** i wybierz **Utwórz**. Studio otwiera nową aplikację z listą plików po lewej stronie. W przypadku tabeli lub widoku gotowy do wysłania jest monit Weave o zbudowanie pierwszej strony aplikacji. Zobacz [Tworzenie aplikacji Panel](/pl/guides/panel-apps/creating/).

## Gdzie znajduje się twoja aplikacja

Aplikacja Studio to folder nazwany od aplikacji (`<app-slug>/`) w repozytorium `apps` Twojego obszaru roboczego w [PlaidCloud Git](/pl/guides/git/), tym samym, w którym znajdują się inne Twoje aplikacje Panel. Studio nie tworzy dla aplikacji osobnego repozytorium, więc jej kod źródłowy znajdziesz i edytujesz w `apps` obok innych aplikacji.

- **Gałąź robocza.** Prace, które nie są jeszcze na żywo, są przechowywane na gałęzi o nazwie `studio-<app-slug>`. **Opublikuj** kopiuje folder aplikacji z tej gałęzi na gałąź główną.
- **Przebudowy.** Wypchnięcie do `apps` przebudowuje aplikację tylko wtedy, gdy zmienił się folder tej aplikacji lub plik `requirements.txt` w katalogu głównym repozytorium.
- **Istniejące aplikacje.** Aplikacja Studio, która znajdowała się we własnym repozytorium, jest automatycznie przenoszona do swojego folderu. Stare repozytorium jest archiwizowane: pozostaje, tylko do odczytu, i nigdy nie jest usuwane.

## Edycja

Wybierz plik z listy, aby edytować go w edytorze. Zależności Pythona wymieniaj w `requirements.txt`, jeden pakiet w wierszu. Są instalowane podczas budowania aplikacji.

Wybierz **Zapytaj Weave**, aby Weave napisał lub zmienił aplikację za Ciebie. Zobacz [Tworzenie aplikacji Panel za pomocą Weave](/pl/guides/panel-apps/build-with-weave/).

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
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Twoje zmiany docierają do odbiorców dopiero po opublikowaniu.</figcaption>
</figure>

### Zapis

**Zapisz** zachowuje zmiany jako wersję roboczą. Działająca aplikacja nie zmienia się, a nikt inny nie widzi wersji roboczej.

### Podgląd

**Podgląd** buduje zapisaną wersję roboczą jako prywatną kopię i otwiera ją. Podgląd mogą otworzyć tylko edytorzy aplikacji.

- Podgląd jest usuwany po 24 godzinach bez zapisu.
- Obszar roboczy może mieć jednocześnie do 10 podglądów.
- Zapisz ponownie i wybierz **Podgląd**, aby zobaczyć najnowsze zmiany.

### Publikacja

**Opublikuj** zastępuje działającą aplikację zapisaną wersją roboczą. Wymaga uprawnień do edycji w projekcie aplikacji, a Studio najpierw prosi o potwierdzenie.

Jeśli ktoś inny opublikował zmianę po otwarciu przez Ciebie aplikacji, Studio zgłasza konflikt zamiast nadpisać jego pracę. Wczytaj aplikację ponownie, przenieś swoje zmiany i opublikuj jeszcze raz.

## Stan kompilacji i błędy

Karta **Zbuduj** pokazuje stan ostatniej kompilacji i aktualizuje się w trakcie jej trwania. Gdy kompilacja się nie powiedzie, karta wyświetla każdy błąd wraz z plikiem i numerem wiersza, dzięki czemu możesz przejść od razu do tego wiersza. Problemy z zależnościami w `requirements.txt` zawierają wskazówkę dotyczącą poprawki.

Błędy i ostrzeżenia są też oznaczone w swoich wierszach w edytorze, więc widzisz problem tam, gdzie występuje.

Znaczenie poszczególnych stanów po opublikowaniu aplikacji opisano w [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/#stan-budowania-aplikacje-serwerowe).

## Historia i przywracanie

Karta **Historia** wyświetla każdą opublikowaną wersję aplikacji, od najnowszej, wraz z jej stanem kompilacji. Wybierz **Załaduj więcej**, aby zobaczyć starsze.

Aby wrócić do wcześniejszej wersji, wybierz przy niej **Przywróć** i potwierdź. Przywrócona wersja staje się działającą aplikacją i jest przebudowywana. Niezapisana wersja robocza nie przepada: pozostaje w wersji roboczej i trafia na żywo na wierzch przywróconej wersji przy następnej publikacji. Jeśli aplikacja już odpowiada tej wersji, Studio informuje o tym i niczego nie zmienia. Jeśli ktoś opublikował zmiany w trakcie przywracania, Studio niczego nie przywraca i prosi o ponowną próbę.

## Wnioski

Karta **Wnioski** pokazuje, jak ludzie korzystają z aplikacji i jak szybko ona odpowiada. Wybierz ostatnie 7, 14 lub 30 dni.

| Sekcja | Pokazuje |
|---|---|
| **Wyświetlenia dziennie** | Ile razy aplikacja była otwierana każdego dnia. |
| **Wczytanie strony** | Medianę czasu wczytania oraz czas, który 95 procent wczytań poprawia, na podstawie wczytań stron w danym okresie. |
| **Najwolniejsze zapytania** | Zapytania, które trwały najdłużej, wraz z częstością ich uruchamiania oraz medianą, czasem górnego zakresu i najdłuższym czasem. |
| **Błędy** | Co poszło nie tak w danym okresie, według rodzaju błędu i miejsca w aplikacji, w którym wystąpił. |

Gdy okres zawiera więcej aktywności, niż Wnioski mogą odczytać, informuje to, że wartości są częściowe. Gdy wczytania stron przekraczają [budżet wydajności](/pl/guides/panel-apps/app-kit/#budżety-wydajności) aplikacji, Wnioski ostrzegają, ile ich było i które zapytania były wolne. Wnioski nigdy nie pokazują danych zwróconych przez zapytanie ani nazw osób, które otworzyły aplikację.

Karty **Historia** i **Wnioski** wymagają przypisania aplikacji do projektu; nieprzypisana aplikacja pokazuje monit o przypisanie.

## Alerty i zestawienia

Wybierz **Alerty i zestawienia**, aby skonfigurować powiadomienia, które obserwują liczbę w danych aplikacji i informują, gdy przekroczy limit, lub wysyłają podsumowanie według harmonogramu. Zobacz [Alerty i zestawienia](/pl/guides/panel-apps/alerts-and-digests/).

## Wyświetlanie aplikacji w galerii

Wybierz **Galeria…** w Studio. Wybierz **Wyświetlaj w galerii**, aby wystawić aplikację jako szablon, z którego każdy, kto może wyświetlać jej projekt, może utworzyć własną aplikację, lub **Usuń z galerii**, aby ją usunąć. Przycisk jest dostępny dla aplikacji należących do projektu. Potrzebujesz uprawnień do edycji projektu. Zobacz [Galeria aplikacji](/pl/guides/panel-apps/gallery/).

## Przypinanie do strony głównej

Wybierz **Przypnij do strony głównej**, aby dodać aplikację do tablicy **Strona główna** projektu, i **Odepnij od strony głównej**, aby ją usunąć.

## Usuwanie aplikacji

Usunięcie aplikacji Panel najpierw wymaga potwierdzenia. W **Moje aplikacje Panel** użyj ikony **minus** w wierszu aplikacji. Cofnięcie publikacji również wymaga potwierdzenia.

## Następne kroki

- [Tworzenie aplikacji Panel za pomocą Weave](/pl/guides/panel-apps/build-with-weave/) — opisz aplikację i zatwierdź dokładną zmianę.
- [Zestaw narzędzi aplikacji Panel](/pl/guides/panel-apps/app-kit/) — komponenty używane przez starty Studio z tabeli i widoku.
- [Alerty i zestawienia](/pl/guides/panel-apps/alerts-and-digests/) — powiadamiaj ludzi, gdy liczba przekroczy limit, lub według harmonogramu.
- [Galeria aplikacji](/pl/guides/panel-apps/gallery/) — udostępnij aplikację jako punkt wyjścia dla innych.
- [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/) — dzienniki, użycie i przebudowy po opublikowaniu.
