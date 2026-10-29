---
title: Korzystanie z aplikacji Dash
description: Śledź stan budowania, otwieraj, przebudowuj, blokuj, przeglądaj dzienniki, edytuj i usuwaj opublikowane aplikacje Plotly Dash na ekranie Moje aplikacje Panel w PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/using.md
---

Aplikacje Dash pojawiają się na tym samym ekranie **Moje aplikacje Panel** co Twoje aplikacje Panel WASM i serwerowe, z wartością **Dash** w kolumnie **Środowisko uruchomieniowe** i własną ikoną, dzięki czemu łatwo je odróżnić. Wszystko na tej stronie odpowiada [Korzystaniu z aplikacji Panel](/pl/guides/panel-apps/using/) w przypadku aplikacji serwerowej, z jednym wyjątkiem opisanym poniżej: aplikacje Dash nie mają jeszcze **Metryk użycia**.

## Stan budowania

Kolumna **Stan** aplikacji Dash śledzi jej budowanie, a lista odświeża się sama w trakcie budowania:

- **Budowanie…** — PlaidCloud buduje Twoje repozytorium w kontener. Aplikacja nie ma jeszcze adresu URL.
- **Gotowe** — budowanie zakończyło się powodzeniem. Adres URL aplikacji działa, a w jej wierszu pojawia się ikona **Otwórz**.
- **Niepowodzenie** — budowanie nie zakończyło się. Sprawdź punkt wejścia i gałąź, a następnie edytuj aplikację, aby opublikować ją ponownie.

## Przebudowywanie aplikacji Dash

Kliknij ikonę **Zbuduj ponownie** w wierszu aplikacji Dash, aby przebudować i ponownie wdrożyć ją bez zmiany ustawień. Stan aplikacji wraca do **Budowanie…**, gdy PlaidCloud ponownie buduje tę samą gałąź i ten sam punkt wejścia, a następnie przechodzi z powrotem w **Gotowe**, gdy nowa wersja zacznie działać.

Użyj opcji **Zbuduj ponownie** po zmianach zależności, aktualizacjach obrazu bazowego lub przejściowo nieudanym budowaniu. Edycja i zapis aplikacji Dash również ją przebudowuje, ale ponowne budowanie nie wymaga otwierania formularza edycji.

## Blokowanie aplikacji

Kliknij ikonę **blokady** w wierszu aplikacji, aby zabezpieczyć ją przed przypadkowymi zmianami. Gdy aplikacja Dash jest zablokowana:

- **Edytuj**, **Usuń** i **Zbuduj ponownie** odmawiają wykonania i informują, że aplikacja jest zablokowana.
- **Wypchnięcie do gałęzi aplikacji nie przebudowuje jej** — automatyczne przebudowanie jest pomijane do czasu odblokowania aplikacji. Wypchnij ponownie (lub użyj opcji **Zbuduj ponownie**) po odblokowaniu, aby zmiana została uwzględniona.
- Otwieranie aplikacji i przeglądanie jej dzienników nadal działają — blokada zatrzymuje tylko zmiany, nigdy przeglądających.

Kliknij ikonę ponownie, aby odblokować. Ikona pokazuje bieżący stan aplikacji: zamknięta, gdy jest zablokowana, otwarta, gdy nie jest. Blokada chroni przed pomyłkami, a nie jest zabezpieczeniem — każdy, kto może edytować aplikacje Dash, może je też odblokować.

## Otwieranie aplikacji Dash

Kliknij ikonę **Otwórz** na początku wiersza gotowej aplikacji, aby uruchomić ją w nowej karcie pod adresem `https://<your-tenant-host>/serve/<slug>/`. Ikona pojawia się dopiero, gdy aplikacja jest **Gotowa**.

Aplikacja Dash skaluje się do zera, gdy jest bezczynna, aby oszczędzać zasoby, więc pierwsze otwarcie po okresie bezczynności musi ją uruchomić. W tym czasie zamiast pustej karty widzisz **ekran ładowania PlaidCloud**, a aplikacja pojawia się sama, gdy będzie gotowa. Jeśli aplikacja nie może się uruchomić, ekran ładowania zmienia się w komunikat **„This app didn't start"** z przyciskiem **Spróbuj ponownie**; jeśli problem się powtarza, edytuj aplikację, sprawdź jej punkt wejścia i gałąź, a następnie opublikuj ją ponownie.

> **`dcc.Interval` (lub dowolne inne stałe odpytywanie) uniemożliwia skalowanie do zera, dopóki jego karta pozostaje otwarta.** Skalowanie do zera opiera się na tym, że aplikacja cichnie — brak żądań w toku — gdy nikt aktywnie jej nie używa. Komponent, który stale wysyła żądania według czasomierza, taki jak `dcc.Interval`, utrzymuje aplikację aktywną tak długo, jak otwarta jest ta karta, nawet jeśli osoba, która na nią patrzy, odeszła od komputera. Jeśli chcesz, aby aplikacja skalowała się w dół między wizytami, unikaj stałego odpytywania lub zatrzymaj interwał, gdy strona przez jakiś czas pozostaje bezczynna.

## Przeglądanie dzienników

Kliknij ikonę **Wyświetl dzienniki** w wierszu aplikacji Dash, aby otworzyć jej przeglądarkę dzienników z tymi samymi kartami **Środowisko uruchomieniowe** i **Zbuduj**, filtrami, zakresem czasu i panelem szczegółów, jakie ma serwerowa aplikacja Panel — pełny opis działania znajdziesz w [Przeglądaniu dzienników](/pl/guides/panel-apps/using/#wyświetlanie-dzienników-aplikacje-serwerowe). Każdy wiersz dziennika środowiska uruchomieniowego jest oznaczony **użytkownikiem**, którego sesja go wygenerowała, tak samo jak w serwerowej aplikacji Panel.

**Metryki użycia nie są dostępne dla aplikacji Dash w tym wydaniu** — ikona **Metryk użycia**, która pojawia się w wierszu serwerowej aplikacji Panel, nie pojawia się dla aplikacji Dash, więc nie ma jeszcze zestawienia unikatowych użytkowników i sesji.

## Edycja aplikacji

Kliknij ikonę **ołówka** w wierszu aplikacji Dash, aby ją edytować. Możesz zmienić nazwę, slug, gałąź, punkt wejścia, CPU, pamięć, okno bezczynności, flagę publiczną, domeny osadzonego udostępniania i notatkę. **Połączenie Git** jest ustalone po utworzeniu aplikacji i wyświetlane tylko do odczytu. Nie ma pola **Projekt** do edycji — to ustawienie jest specyficzne dla Panel. Zapis przebudowuje aplikację — jej stan wraca do **Budowanie…**, dopóki nowa wersja nie będzie gotowa.

## Usuwanie aplikacji

Kliknij ikonę **minusa** w wierszu aplikacji Dash i potwierdź. Usunięcie likwiduje jej budowanie i wdrożenie, a adres URL aplikacji natychmiast przestaje działać.
