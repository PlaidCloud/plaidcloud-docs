---
title: Korzystanie z aplikacji Panel
description: Śledź stan budowania, otwieraj, buduj ponownie, blokuj, przeglądaj dzienniki i metryki użycia, edytuj i usuwaj opublikowane aplikacje HoloViz Panel na ekranie Aplikacje w PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/using.md
---

Każda opublikowana aplikacja jest widoczna na ekranie **Aplikacje** wraz z wartościami w kolumnach **Środowisko uruchomieniowe**, **Stan**, **Slug** oraz sygnaturami czasowymi. Kolumna położona najbardziej po lewej otwiera aplikację; pozostałe ikony w wierszu pozwalają zablokować ją przed przypadkowymi zmianami, edytować ją, usunąć, a — w przypadku aplikacji serwerowych — zbudować ją ponownie, przeglądać jej dzienniki i metryki użycia. Ikona otwierania odzwierciedla środowisko uruchomieniowe aplikacji, więc aplikacje WASM i serwerowe łatwo odróżnić na pierwszy rzut oka.

## Stan budowania (aplikacje serwerowe)

Kolumna **Stan** aplikacji serwerowej śledzi jej budowanie, a lista odświeża się samoczynnie, dopóki budowanie trwa:

- **Budowanie…** — PlaidCloud buduje kontener z Twojego repozytorium. Aplikacja nie ma jeszcze adresu URL.
- **Gotowe** — budowanie zakończyło się powodzeniem. Adres URL aplikacji działa, a w jej wierszu pojawia się ikona **Otwórz**.
- **Niepowodzenie** — budowanie nie zostało ukończone. Sprawdź punkt wejścia i gałąź, a następnie edytuj aplikację, aby opublikować ją ponownie.

Aplikacje WASM nie mają etapu budowania i są dostępne od razu po opublikowaniu.

## Ponowne budowanie aplikacji serwerowej

Kliknij ikonę **Zbuduj ponownie** w wierszu aplikacji serwerowej, aby ponownie ją zbudować i wdrożyć bez zmieniania jej ustawień. Stan aplikacji wraca do **Budowanie…**, gdy PlaidCloud ponownie buduje tę samą gałąź i ten sam punkt wejścia, a po uruchomieniu nowej wersji zmienia się z powrotem na **Gotowe**.

Użyj opcji **Zbuduj ponownie** po zmianie zależności, aktualizacji obrazu bazowego lub po przejściowym niepowodzeniu budowania. Edycja i zapisanie aplikacji serwerowej również powodują jej ponowne zbudowanie, ale ponowne budowanie nie wymaga otwierania formularza edycji.

W przypadku aplikacji [App Runner](/pl/guides/workflows/use-converted-alteryx-apps/#utrzymywanie-aktualności-aplikacji) — formularza wejściowego generowanego dla przekonwertowanej aplikacji Alteryx — opcja **Zbuduj ponownie** oraz zapisanie edycji najpierw odświeżają jej wygenerowane pliki do bieżącej wersji App Runner, a dopiero potem ją budują. PlaidCloud robi to również dla każdej niezablokowanej aplikacji App Runner przy aktualizacji samego PlaidCloud; zablokowana aplikacja wymaga użycia opcji **Zbuduj ponownie** po jej odblokowaniu.

## Blokowanie aplikacji

Kliknij ikonę **blokady** w wierszu aplikacji, aby chronić ją przed przypadkowymi zmianami. Gdy aplikacja jest zablokowana:

- Operacje **Edytuj**, **Usuń** i **Zbuduj ponownie** nie są wykonywane, a komunikat informuje, że aplikacja jest zablokowana.
- **Wypchnięcie zmian do gałęzi aplikacji serwerowej nie powoduje jej ponownego zbudowania** — automatyczne ponowne budowanie jest pomijane do czasu odblokowania aplikacji. Pominięte wypchnięcie nie uruchamia żadnego budowania, więc w dziennikach budowania aplikacji nie pojawia się nic nowego; po odblokowaniu wypchnij zmiany ponownie (lub użyj opcji **Zbuduj ponownie**), aby je uwzględnić.
- Otwieranie aplikacji, przeglądanie jej dzienników i przeglądanie jej metryk użycia nadal działają — blokada zatrzymuje tylko zmiany, nigdy osoby przeglądające.

Kliknij ikonę ponownie, aby odblokować aplikację. Ikona pokazuje bieżący stan aplikacji: zamkniętą kłódkę, gdy aplikacja jest zablokowana, i otwartą, gdy nie jest.

Blokada chroni przed pomyłkami — błędną edycją, niezamierzonym usunięciem lub wypchnięciem zmian w Git do aplikacji, którą właśnie prezentujesz — tak samo jak blokada przepływów pracy i kroków przepływu pracy. **Nie** jest to zabezpieczenie: każdy, kto może edytować aplikacje Panel, może je też odblokować.

> Blokada nie obejmuje dwóch sytuacji: **budowanie, które już trwa** w chwili zablokowania, nadal się kończy i zostaje uruchomione, a pliki aplikacji **WASM** znajdują się na jej koncie dokumentów, więc zastąpienie tych plików zmienia działającą aplikację bez modyfikowania zablokowanego rekordu.

## Otwieranie aplikacji

Kliknij ikonę **Otwórz** na początku wiersza gotowej aplikacji, aby uruchomić ją na nowej karcie. Opcja **Otwórz** jest też pierwszą pozycją w menu **⋯** wiersza. Zobacz [Menu akcji wiersza](/pl/guides/dashboards/using-dashboards/#menu-akcji-wiersza).

- Aplikacja serwerowa jest udostępniana pod adresem `https://<your-tenant-host>/serve/<slug>/`.
- Ikona **Otwórz** pojawia się dopiero wtedy, gdy aplikacja serwerowa ma stan **Gotowe**.

Bezczynna aplikacja serwerowa jest skalowana do zera, aby oszczędzać zasoby, więc pierwsze otwarcie po okresie bezczynności wymaga jej uruchomienia. W tym czasie zamiast pustej karty widać **ekran ładowania PlaidCloud**: nazwę aplikacji, jej postęp przez etapy **Uruchamianie**, **Przygotowywanie** i **Ładowanie aplikacji** oraz identyfikator obszaru roboczego — w jasnym lub ciemnym motywie, zgodnie z Twoim ustawieniem. Aplikacja pojawia się samoczynnie, gdy tylko będzie gotowa (zwykle po kilku sekundach, a przy zimnym starcie po maksymalnie około minucie), a następnie odpowiada normalnie, dopóki ponownie nie przejdzie w stan bezczynności.

> Jeśli aplikacji nie można uruchomić, ekran ładowania zmienia się w komunikat, że aplikacja się nie uruchomiła, wraz z informacją, na którym etapie się zatrzymała, oraz przyciskiem **Spróbuj ponownie** — zamiast kręcić się bez końca. Jeśli sytuacja się powtarza, edytuj aplikację, sprawdź jej punkt wejścia i gałąź, a następnie opublikuj ją ponownie lub skontaktuj się z administratorem PlaidCloud.

### Wygląd

Serwerowe aplikacje Panel domyślnie korzystają z nowoczesnego projektu **Fast** platformy PlaidCloud, ale ustawienie **Projekt** aplikacji pozwala przywrócić styl **Domyślny** platformy Panel, gdy zależy od niego istniejący kod CSS. Motyw — jasny, ciemny lub przełącznik jasny/ciemny, którego mogą używać osoby przeglądające — ustawia się w szablonie aplikacji. Wzorce znajdziesz w sekcji [Ustawianie motywu](/pl/guides/panel-apps/creating/#ustawianie-motywu-jasny-ciemny-lub-przełącznik) w przewodniku dotyczącym tworzenia aplikacji. Jeśli tabele lub niestandardowe style aplikacji są przygotowane z myślą o jasnym tle, pozostaw na stałe jasny motyw.

## Przeglądanie dzienników (aplikacje serwerowe)

Kliknij ikonę **Wyświetl dzienniki** w wierszu aplikacji serwerowej, aby otworzyć przeglądarkę jej dzienników. (Aplikacje WASM działają w całości w przeglądarce i nie mają dzienników serwera, więc ikona pojawia się tylko w wierszach aplikacji serwerowych).

Przeglądarka ma dwie karty:

- **Środowisko uruchomieniowe** (wyświetlana jako pierwsza) — dane wyjściowe działającej aplikacji: wszystko, co zapisuje w dzienniku, wszystko, co wypisuje, oraz wszelkie nieprzechwycone błędy. Są one przechowywane także po przeskalowaniu aplikacji do zera, więc możesz sprawdzić, co działo się podczas wcześniejszej sesji.
- **Budowanie** — dane wyjściowe budowania kontenera aplikacji. Użyj jej, aby sprawdzić, *dlaczego* budowanie ma stan **Niepowodzenie** — na przykład z powodu zależności, której nie udało się zainstalować.

Każda karta zawiera filtry **Informacje / Ostrzeżenie / Błąd**, zakres czasu **Dzienniki od** (od ostatniej godziny do 30 dni albo wszystkie), przycisk **Odśwież** oraz opcję **Automatyczne odświeżanie**, która odpytuje o nowe wpisy — przydatną, gdy obserwujesz działającą aplikację lub trwające budowanie. Najnowsze wpisy są wyświetlane na początku.

> Jeśli nie udało się przechwycić danych wyjściowych budowania, karta Budowanie zamiast pozostawać pusta wyświetla krótką informację o przyczynie.

### Odczytywanie pełnego komunikatu dziennika

Tabela dziennika skraca długie wiersze, aby lista pozostała czytelna. Zaznacz wiersz dziennika, aby obok tabeli otworzyć **panel szczegółów** z pełnym komunikatem wpisu. To najprostszy sposób na przeczytanie czegoś, co jest zbyt długie dla tabeli — długiego komunikatu o błędzie lub pełnego śladu stosu — bez obcinania.

### Kopiowanie wierszy dziennika

Możesz zaznaczyć kilka wierszy dziennika naraz i kliknąć **Kopiuj**, aby umieścić je w schowku. Jest to przydatne przy wklejaniu dzienników do czatu z asystentem AI podczas debugowania aplikacji lub do wiadomości do zespołu albo pomocy technicznej PlaidCloud.

### Kto wygenerował wiersz dziennika

Gdy aplikacja loguje osoby przeglądające, każdy wiersz dziennika jest oznaczony **użytkownikiem**, którego sesja go wygenerowała, dzięki czemu możesz ustalić, która osoba napotkała dany błąd lub ostrzeżenie. Oznaczanie działa w miarę możliwości — niektóre wiersze platformy i uruchamiania powstają, zanim pojawi się jakakolwiek osoba przeglądająca, i mogą nie zawierać użytkownika.

## Usage Metrics (aplikacje serwerowe)

Kliknij ikonę **Usage Metrics** w wierszu aplikacji serwerowej — obok ikony **Wyświetl dzienniki** — aby zobaczyć, jak aplikacja jest używana. Widok podsumowuje:

- **Unikalni użytkownicy** — ile różnych osób otworzyło aplikację.
- **Sesje** — ile razy aplikacja została otwarta.
- **Średni i medianowy czas trwania sesji** — mniej więcej, jak długo trwa wizyta.
- **Ostatnio używane** — kiedy aplikacja została ostatnio otwarta.

Pod podsumowaniem znajduje się podział **na użytkowników** i **na dni**, dzięki któremu widać, kto korzysta z aplikacji i jak zmienia się jej użycie w czasie.

> Czasy trwania są przybliżone. Aplikacje serwerowe przechodzą w stan bezczynności i są skalowane w dół, gdy nikt z nich nie korzysta, więc dokładny koniec sesji nie zawsze jest rejestrowany — traktuj czasy trwania jako orientacyjne, a nie jako dokładny pomiar.

## Edytowanie aplikacji

Kliknij ikonę **ołówka** w wierszu aplikacji, aby ją edytować. Formularz edycji jest dopasowany do środowiska uruchomieniowego aplikacji.

W przypadku aplikacji **serwerowej** możesz zmienić nazwę, slug, gałąź, punkt wejścia, procesor, pamięć, projekt, okres bezczynności, flagę publiczną, domeny osadzonego udostępniania i notatkę. Pole **Połączenie Git** jest ustalane podczas tworzenia aplikacji i wyświetlane tylko do odczytu. Zapisanie powoduje ponowne zbudowanie aplikacji — jej stan wraca do **Budowanie…**, dopóki nowa wersja nie będzie gotowa.

## Usuwanie aplikacji

Kliknij ikonę **minusa** w wierszu aplikacji i potwierdź; usunięcie lub cofnięcie publikacji aplikacji zawsze wymaga wcześniejszego potwierdzenia. Usunięcie aplikacji serwerowej likwiduje jej kompilację i wdrożenie; usunięcie aplikacji WASM cofa publikację pliku statycznego. Adres URL aplikacji natychmiast przestaje działać.

Narzędzie MCP `panel_deployment_manage` nie oferuje już cofania publikacji. Zamiast tego usuń aplikację z tej listy.
