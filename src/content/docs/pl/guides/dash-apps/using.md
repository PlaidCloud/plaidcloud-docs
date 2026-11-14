---
title: Korzystanie z aplikacji Dash
description: Śledź stan budowania, otwieraj, buduj ponownie, blokuj, przeglądaj dzienniki, edytuj i usuwaj opublikowane aplikacje Plotly Dash na ekranie Aplikacje w PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/using.md
---

Aplikacje Dash są widoczne na tym samym ekranie **Aplikacje** co aplikacje Panel WASM i serwerowe — w kolumnie **Środowisko uruchomieniowe** mają wartość **Dash** i własną ikonę, dzięki czemu łatwo je odróżnić. Wszystko, co opisano na tej stronie, odpowiada stronie [Korzystanie z aplikacji Panel](/pl/guides/panel-apps/using/) w przypadku aplikacji serwerowej, z jednym wyjątkiem wskazanym poniżej: aplikacje Dash nie mają jeszcze funkcji **Usage Metrics**.

## Stan budowania

Kolumna **Stan** aplikacji Dash śledzi jej budowanie, a lista odświeża się samoczynnie, dopóki budowanie trwa:

- **Budowanie…** — PlaidCloud buduje kontener z Twojego repozytorium. Aplikacja nie ma jeszcze adresu URL.
- **Gotowe** — budowanie zakończyło się powodzeniem. Adres URL aplikacji działa, a w jej wierszu pojawia się ikona **Otwórz**.
- **Niepowodzenie** — budowanie nie zostało ukończone. Sprawdź punkt wejścia i gałąź, a następnie edytuj aplikację, aby opublikować ją ponownie.

## Ponowne budowanie aplikacji Dash

Kliknij ikonę **Zbuduj ponownie** w wierszu aplikacji Dash, aby ponownie ją zbudować i wdrożyć bez zmieniania jej ustawień. Stan aplikacji wraca do **Budowanie…**, gdy PlaidCloud ponownie buduje tę samą gałąź i ten sam punkt wejścia, a po uruchomieniu nowej wersji zmienia się z powrotem na **Gotowe**.

Użyj opcji **Zbuduj ponownie** po zmianie zależności, aktualizacji obrazu bazowego lub po przejściowym niepowodzeniu budowania. Edycja i zapisanie aplikacji Dash również powodują jej ponowne zbudowanie, ale ponowne budowanie nie wymaga otwierania formularza edycji.

## Blokowanie aplikacji

Kliknij ikonę **blokady** w wierszu aplikacji, aby chronić ją przed przypadkowymi zmianami. Gdy aplikacja Dash jest zablokowana:

- Operacje **Edytuj**, **Usuń** i **Zbuduj ponownie** nie są wykonywane, a komunikat informuje, że aplikacja jest zablokowana.
- **Wypchnięcie zmian do gałęzi aplikacji nie powoduje jej ponownego zbudowania** — automatyczne ponowne budowanie jest pomijane do czasu odblokowania aplikacji. Po odblokowaniu wypchnij zmiany ponownie (lub użyj opcji **Zbuduj ponownie**), aby je uwzględnić.
- Otwieranie aplikacji i przeglądanie jej dzienników nadal działa — blokada zatrzymuje tylko zmiany, nigdy osoby przeglądające.

Kliknij ikonę ponownie, aby odblokować aplikację. Ikona pokazuje bieżący stan aplikacji: zamkniętą kłódkę, gdy aplikacja jest zablokowana, i otwartą, gdy nie jest. Blokada chroni przed pomyłkami, a nie stanowi zabezpieczenia — każdy, kto może edytować aplikacje Dash, może je też odblokować.

## Otwieranie aplikacji Dash

Kliknij ikonę **Otwórz** na początku wiersza gotowej aplikacji, aby uruchomić ją na nowej karcie pod adresem `https://<your-tenant-host>/serve/<slug>/`. Ikona pojawia się dopiero wtedy, gdy aplikacja ma stan **Gotowe**.

Bezczynna aplikacja Dash jest skalowana do zera, aby oszczędzać zasoby, więc pierwsze otwarcie po okresie bezczynności wymaga jej uruchomienia. W tym czasie zamiast pustej karty widać **ekran ładowania PlaidCloud**, który pokazuje postęp aplikacji przez etapy **Uruchamianie**, **Przygotowywanie** i **Ładowanie aplikacji**, a aplikacja pojawia się samoczynnie, gdy będzie gotowa. Jeśli aplikacji nie można uruchomić, ekran ładowania zmienia się w komunikat, że aplikacja się nie uruchomiła, wraz z informacją, na którym etapie się zatrzymała, oraz przyciskiem **Spróbuj ponownie**. Jeśli sytuacja się powtarza, edytuj aplikację, sprawdź jej punkt wejścia i gałąź, a następnie opublikuj ją ponownie.

> **Komponent `dcc.Interval` (lub dowolne inne stałe odpytywanie) uniemożliwia skalowanie do zera, dopóki jego karta jest otwarta.** Skalowanie do zera wymaga, aby aplikacja się wyciszyła — bez żadnych trwających żądań — gdy nikt już z niej aktywnie nie korzysta. Komponent, który wysyła żądania według czasomierza, taki jak `dcc.Interval`, utrzymuje aplikację w stanie aktywnym tak długo, jak otwarta jest ta karta, nawet jeśli osoba, która ją przegląda, odeszła od komputera. Jeśli aplikacja ma być skalowana w dół między wizytami, unikaj stałego odpytywania lub zatrzymuj interwał, gdy strona przez pewien czas pozostaje bezczynna.

## Przeglądanie dzienników

Kliknij ikonę **Wyświetl dzienniki** w wierszu aplikacji Dash, aby otworzyć przeglądarkę jej dzienników z tymi samymi kartami **Środowisko uruchomieniowe** i **Budowanie**, filtrami, zakresem czasu i panelem szczegółów, jakie ma serwerowa aplikacja Panel — pełny opis działania znajdziesz w sekcji [Przeglądanie dzienników](/pl/guides/panel-apps/using/#przeglądanie-dzienników-aplikacje-serwerowe). Każdy wiersz dziennika środowiska uruchomieniowego jest oznaczony **użytkownikiem**, którego sesja go wygenerowała, tak samo jak w serwerowej aplikacji Panel.

**Funkcja Usage Metrics nie jest dostępna dla aplikacji Dash w tej wersji** — ikona **Usage Metrics**, która pojawia się w wierszu serwerowej aplikacji Panel, nie jest wyświetlana dla aplikacji Dash, więc nie można jeszcze sprawdzić podziału na unikalnych użytkowników i sesje.

## Edytowanie aplikacji

Kliknij ikonę **ołówka** w wierszu aplikacji Dash, aby ją edytować. Możesz zmienić nazwę, slug, gałąź, punkt wejścia, procesor, pamięć, okres bezczynności, flagę publiczną, domeny osadzonego udostępniania i notatkę. Pole **Połączenie Git** jest ustalane podczas tworzenia aplikacji i wyświetlane tylko do odczytu. Nie ma pola **Projekt** do edycji — to ustawienie dotyczy wyłącznie aplikacji Panel. Zapisanie powoduje ponowne zbudowanie aplikacji — jej stan wraca do **Budowanie…**, dopóki nowa wersja nie będzie gotowa.

## Usuwanie aplikacji

Kliknij ikonę **minusa** w wierszu aplikacji Dash i potwierdź. Usunięcie aplikacji likwiduje jej kompilację i wdrożenie, a adres URL aplikacji natychmiast przestaje działać.
