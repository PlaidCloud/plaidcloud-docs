---
title: Panel Studio
description: Twórz, edytuj, wyświetlaj w podglądzie i publikuj aplikacje Panel bez opuszczania PlaidCloud, a następnie przywracaj wcześniejsze wersje, sprawdzaj użycie i szybkość aplikacji, konfiguruj alerty i zestawienia, wyświetlaj aplikację w galerii i przypinaj ją do strony głównej.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio to edytor aplikacji Panel w PlaidCloud. Pokazuje pliki aplikacji obok edytora, buduje prywatny podgląd, który można otworzyć, i publikuje aplikację, gdy będzie gotowa. Aby zacząć, nie potrzebujesz repozytorium git.

## Otwieranie Panel Studio

- Na tablicy **Strona główna** projektu wybierz **Otwórz w Studio** przy aplikacji Panel.
- W widoku **Moje aplikacje Panel** wybierz **Studio** w wierszu aplikacji.

Aby rozpocząć nową aplikację, wybierz **New app** > **Studio**. Ta opcja jest też dostępna w polu **Aplikacje Panel** na karcie **Strona główna** projektu. Aby zbudować aplikację na podstawie tabeli, zaznacz ją na karcie **Tabele** projektu i wybierz **Utwórz aplikację Panel**.

## Tworzenie aplikacji

Okno **Nowa aplikacja Studio** pozwala zacząć od jednego z pięciu punktów wyjścia:

| Zacznij od | Efekt |
|---|---|
| **Pusta aplikacja** | Minimalna aplikacja z plikami `app.py` i `requirements.txt`. |
| **Z tabeli** | Aplikacja zbudowana na wybranej tabeli. |
| **Z widoku** | To samo, ale zbudowane na widoku projektu. |
| **Z innej aplikacji Studio** | Kopia jednej z Twoich aplikacji Studio. |
| **Z galerii** | Kopia aplikacji, którą Twój obszar roboczy umieścił w [galerii aplikacji](/pl/guides/panel-apps/gallery/). |

Nadaj aplikacji nazwę, wybierz jej **Projekt** i kliknij **Utwórz**. Studio otworzy nową aplikację z listą plików po lewej stronie. W przypadku tabeli lub widoku gotowy do wysłania jest monit Weave, który buduje pierwszą stronę aplikacji. Zobacz [Tworzenie aplikacji Panel](/pl/guides/panel-apps/creating/).

## Gdzie znajduje się aplikacja

Aplikacja Studio to folder nazwany jak aplikacja (`<app-slug>/`) w repozytorium `apps` Twojego obszaru roboczego w [PlaidCloud Git](/pl/guides/git/), czyli w tym samym repozytorium, w którym znajdują się Twoje pozostałe aplikacje Panel. Studio nie tworzy dla aplikacji osobnego repozytorium, więc jej kod źródłowy można znaleźć i edytować w `apps` razem z innymi aplikacjami.

- **Gałąź robocza.** Prace, które nie są jeszcze aktywne, są przechowywane w gałęzi o nazwie `studio-<app-slug>`. Opcja **Opublikuj** kopiuje folder aplikacji z tej gałęzi do gałęzi głównej.
- **Ponowne budowanie.** Wypchnięcie zmian do `apps` ponownie buduje aplikację tylko wtedy, gdy zmienił się folder tej aplikacji lub plik `requirements.txt` w katalogu głównym repozytorium.
- **Istniejące aplikacje.** Aplikacja Studio, która znajdowała się we własnym repozytorium, jest automatycznie przenoszona do swojego folderu. Stare repozytorium jest archiwizowane: pozostaje tylko do odczytu i nigdy nie jest usuwane.

## Edycja

Wybierz plik z listy, aby edytować go w edytorze. Zależności Pythona wymieniaj w pliku `requirements.txt`, po jednym pakiecie w wierszu. Są instalowane podczas budowania aplikacji.

Wybierz **Zapytaj Weave**, aby Weave napisał lub zmienił aplikację za Ciebie. Zobacz [Budowanie aplikacji Panel z Weave](/pl/guides/panel-apps/build-with-weave/).

## Zapisywanie, podgląd i publikowanie

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Zapisanie tworzy wersję roboczą widoczną tylko dla Ciebie. Podgląd buduje prywatną kopię wersji roboczej dla edytora. Publikacja zastępuje aktywną aplikację po potwierdzeniu." style="width:100%;max-width:660px;height:auto;">
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
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">aktywna aplikacja</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Zmiany docierają do odbiorców dopiero po opublikowaniu.</figcaption>
</figure>

### Zapisywanie

Opcja **Zapisz** zapisuje zmiany jako wersję roboczą. Aktywna aplikacja się nie zmienia, a wersji roboczej nie widzi nikt inny.

### Podgląd

Opcja **Podgląd** buduje zapisaną wersję roboczą jako prywatną kopię i otwiera ją. Podgląd mogą otworzyć tylko edytorzy aplikacji.

- Podgląd jest usuwany po 24 godzinach bez zapisu.
- Obszar roboczy może mieć jednocześnie do 10 podglądów.
- Zapisz ponownie i wybierz **Podgląd**, aby zobaczyć najnowsze zmiany.

### Publikowanie

Opcja **Opublikuj** zastępuje aktywną aplikację zapisaną wersją roboczą. Wymaga uprawnienia do edycji w projekcie aplikacji, a Studio najpierw prosi o potwierdzenie.

Jeśli ktoś inny opublikował zmianę po otwarciu aplikacji przez Ciebie, Studio zgłasza konflikt zamiast nadpisać jego pracę. Załaduj aplikację ponownie, przenieś swoje zmiany i opublikuj jeszcze raz.

## Stan budowania i błędy

Karta **Zbuduj** pokazuje stan ostatniego budowania i aktualizuje się w trakcie jego trwania. Gdy budowanie się nie powiedzie, karta wyświetla każdy błąd wraz z plikiem i numerem wiersza, dzięki czemu można od razu przejść do właściwego wiersza. Problemy z zależnościami w `requirements.txt` zawierają wskazówkę dotyczącą poprawki.

Błędy i ostrzeżenia są też oznaczone w odpowiednich wierszach w edytorze, więc problem widać tam, gdzie występuje.

Znaczenie poszczególnych stanów po opublikowaniu aplikacji opisano w [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/#stan-budowania-aplikacje-serwerowe).

## Historia i przywracanie

Karta **Historia** wyświetla wszystkie opublikowane wersje aplikacji, od najnowszej, wraz ze stanem budowania. Wybierz **Załaduj więcej**, aby zobaczyć starsze.

Aby wrócić do wcześniejszej wersji, wybierz przy niej **Przywróć** i potwierdź. Przywrócona wersja staje się aktywną aplikacją i jest budowana ponownie. Niezapisana wersja robocza nie przepada: pozostaje w wersji roboczej i przy następnej publikacji zostanie uruchomiona na przywróconej wersji. Jeśli aplikacja już odpowiada tej wersji, Studio informuje o tym i niczego nie zmienia. Jeśli ktoś opublikował zmiany w trakcie przywracania, Studio niczego nie przywraca i prosi o ponowną próbę.

## Wnioski

Karta **Wnioski** pokazuje, jak ludzie korzystają z aplikacji i jak szybko odpowiada. Wybierz ostatnie 7, 14 lub 30 dni.

| Sekcja | Pokazuje |
|---|---|
| **Wyświetlenia dziennie** | Ile razy aplikację otwierano każdego dnia. |
| **Wczytanie strony** | Medianę czasu wczytywania oraz czas, który 95 procent wczytań mieści się poniżej, na podstawie wczytań stron w danym okresie. |
| **Najwolniejsze zapytania** | Zapytania, które trwały najdłużej, wraz z liczbą uruchomień oraz ich medianą, czasem na wolnym końcu rozkładu i czasem najwolniejszym. |
| **Błędy** | Co poszło nie tak w danym okresie, z podziałem na rodzaj błędu i miejsce w aplikacji, w którym wystąpił. |

Gdy okres zawiera więcej aktywności, niż Wnioski są w stanie odczytać, widać informację, że dane są częściowe. Gdy wczytania stron przekraczają [budżet wydajności](/pl/guides/panel-apps/app-kit/#budżety-wydajności) aplikacji, Wnioski ostrzegają, ile ich było i które zapytania były wolne. Wnioski nigdy nie pokazują danych zwróconych przez zapytanie ani nazw osób, które otworzyły aplikację.

Karty **Historia** i **Wnioski** wymagają przypisania aplikacji do projektu; nieprzypisana aplikacja wyświetla monit o przypisanie.

## Alerty i zestawienia

Wybierz **Alerty i zestawienia**, aby skonfigurować powiadomienia, które monitorują liczbę w danych aplikacji i informują o przekroczeniu limitu albo wysyłają podsumowanie według harmonogramu. Zobacz [Alerty i zestawienia](/pl/guides/panel-apps/alerts-and-digests/).

## Wyświetlanie aplikacji w galerii

Wybierz **Galeria…** w Studio. Wybierz **Wyświetlaj w galerii**, aby udostępnić aplikację jako szablon, z którego każdy, kto może wyświetlić jej projekt, może utworzyć własną aplikację, albo **Usuń z galerii**, aby ją usunąć. Przycisk jest dostępny dla aplikacji należących do projektu. Potrzebujesz dostępu do edycji projektu. Zobacz [Galeria aplikacji](/pl/guides/panel-apps/gallery/).

## Przypinanie do strony głównej

Wybierz **Przypnij do strony głównej**, aby dodać aplikację do tablicy **Strona główna** projektu, oraz **Odepnij od strony głównej**, aby ją usunąć.

## Usuwanie aplikacji

Usunięcie aplikacji Panel wymaga wcześniejszego potwierdzenia. W widoku **Moje aplikacje Panel** użyj ikony **minus** w wierszu aplikacji. Cofnięcie publikacji również wymaga potwierdzenia.

## Następne kroki

- [Budowanie aplikacji Panel z Weave](/pl/guides/panel-apps/build-with-weave/) — opisz aplikację i zatwierdź dokładną zmianę.
- [Zestaw komponentów aplikacji Panel](/pl/guides/panel-apps/app-kit/) — komponenty używane przez punkty startowe Studio oparte na tabelach i widokach.
- [Alerty i zestawienia](/pl/guides/panel-apps/alerts-and-digests/) — powiadamiaj ludzi, gdy liczba przekroczy limit, lub według harmonogramu.
- [Galeria aplikacji](/pl/guides/panel-apps/gallery/) — udostępnij aplikację jako punkt wyjścia dla innych.
- [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/) — dzienniki, użycie i ponowne budowanie po opublikowaniu.
