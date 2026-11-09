---
title: Korzystanie z aplikacji Panel
description: Śledź stan kompilacji, otwieraj, buduj ponownie, blokuj, wyświetlaj dzienniki i metryki użycia, edytuj oraz usuwaj opublikowane aplikacje HoloViz Panel z ekranu Moje aplikacje Panel w PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/using.md
---

Każda opublikowana aplikacja pojawia się na ekranie **Moje aplikacje Panel** wraz ze swoim **Środowiskiem uruchomieniowym**, **Stanem**, **Slug** i znacznikami czasu. Pierwsza kolumna od lewej otwiera aplikację; pozostałe ikony w wierszu pozwalają zablokować ją przed przypadkowymi zmianami, edytować ją, usunąć oraz — w przypadku aplikacji serwerowych — zbudować ją ponownie, wyświetlić jej dzienniki i metryki użycia. Ikona otwierania odzwierciedla środowisko uruchomieniowe aplikacji, dzięki czemu aplikacje WASM i serwerowe łatwo odróżnić na pierwszy rzut oka.

## Stan kompilacji (aplikacje serwerowe)

Kolumna **Stan** aplikacji serwerowej śledzi jej kompilację, a lista odświeża się automatycznie, gdy trwa kompilacja:

- **Budowanie…** — PlaidCloud buduje Twoje repozytorium w kontener. Aplikacja nie ma jeszcze adresu URL.
- **Gotowe** — kompilacja zakończyła się powodzeniem. Adres URL aplikacji jest aktywny, a w jej wierszu pojawia się ikona **Otwórz**.
- **Niepowodzenie** — kompilacja nie została ukończona. Sprawdź punkt wejścia i gałąź, a następnie edytuj aplikację, aby opublikować ją ponownie.

Aplikacje WASM nie mają etapu kompilacji i są dostępne zaraz po opublikowaniu.

## Ponowne budowanie aplikacji serwerowej

Kliknij ikonę **Zbuduj ponownie** w wierszu aplikacji serwerowej, aby zbudować ją i wdrożyć ponownie bez zmiany jej ustawień. Stan aplikacji wraca do **Budowanie…**, gdy PlaidCloud ponownie buduje tę samą gałąź i ten sam punkt wejścia, a następnie przełącza się z powrotem na **Gotowe**, gdy nowa kompilacja jest aktywna.

Użyj **Zbuduj ponownie** po zmianach zależności, aktualizacjach obrazu bazowego lub przejściowo nieudanej kompilacji. Edycja i zapisanie aplikacji serwerowej również ją przebudowuje, ale ponowne budowanie nie wymaga otwierania formularza edycji.

W przypadku aplikacji [App Runner](/pl/guides/workflows/use-converted-alteryx-apps/#utrzymywanie-aktualności-aplikacji) — formularza wejściowego generowanego dla przekonwertowanej aplikacji Alteryx — **Zbuduj ponownie** oraz zapisanie edycji najpierw odświeżają jej wygenerowane pliki do bieżącej wersji App Runner, a następnie ją budują. PlaidCloud robi to również dla każdej niezablokowanej aplikacji App Runner podczas aktualizacji samego PlaidCloud; zablokowana aplikacja wymaga **Zbuduj ponownie** po jej odblokowaniu.

## Blokowanie aplikacji

Kliknij ikonę **blokady** w wierszu aplikacji, aby chronić ją przed przypadkowymi zmianami. Gdy aplikacja jest zablokowana:

- **Edytuj**, **Usuń** i **Zbuduj ponownie** odmawiają uruchomienia i informują, że aplikacja jest zablokowana.
- **Wypchnięcie do gałęzi aplikacji serwerowej nie powoduje jej przebudowania** — automatyczne budowanie jest pomijane, dopóki nie odblokujesz aplikacji. Dla pominiętego wypchnięcia nie jest uruchamiana żadna kompilacja, więc w dziennikach kompilacji aplikacji nie pojawia się nic nowego; po odblokowaniu wypchnij zmiany ponownie (lub użyj **Zbuduj ponownie**), aby je uwzględnić.
- Otwieranie aplikacji, wyświetlanie jej dzienników i wyświetlanie jej metryk użycia nadal działają — blokada zatrzymuje tylko zmiany, nigdy przeglądających.

Kliknij ikonę ponownie, aby odblokować. Ikona pokazuje bieżący stan aplikacji: zamknięta, gdy jest zablokowana, otwarta, gdy nie jest.

Blokada chroni przed przypadkami — błędną edycją, niezamierzonym usunięciem lub wypchnięciem git na aplikację, którą demonstrujesz — tak samo jak blokada przepływów pracy i kroków przepływu pracy. **Nie** jest to mechanizm zabezpieczający: każdy, kto może edytować aplikacje Panel, może je również odblokować.

> Dwie rzeczy, których blokada nie obejmuje: **kompilacja już w toku** w chwili zablokowania nadal się kończy i zaczyna działać, a pliki aplikacji **WASM** znajdują się na jej koncie dokumentów, więc zastąpienie tych plików zmienia działającą aplikację bez dotykania zablokowanego rekordu.

## Otwieranie aplikacji

Kliknij ikonę **Otwórz** na początku wiersza gotowej aplikacji, aby uruchomić ją w nowej karcie. **Otwórz** jest także pierwszą pozycją w menu **⋯** wiersza. Zobacz [Menu akcji wiersza](/pl/guides/dashboards/using-dashboards/#menu-akcji-wiersza).

- Aplikacja serwerowa jest udostępniana pod adresem `https://<your-tenant-host>/serve/<slug>/`.
- Ikona **Otwórz** pojawia się dopiero wtedy, gdy aplikacja serwerowa ma stan **Gotowe**.

Aplikacja serwerowa skaluje się do zera w stanie bezczynności, aby oszczędzać zasoby, więc pierwsze otwarcie po okresie bezczynności wymaga jej uruchomienia. W tym czasie widzisz **ekran ładowania PlaidCloud** — nazwę aplikacji, wskaźnik postępu i dane obszaru roboczego — zamiast pustej karty. Aplikacja pojawia się sama, gdy tylko jest gotowa (zwykle w kilka sekund, a przy zimnym starcie do około minuty), a następnie odpowiada normalnie, dopóki ponownie nie przejdzie w stan bezczynności.

> Jeśli aplikacja nie może się uruchomić, ekran ładowania zmienia się w komunikat **„This app didn't start”** z przyciskiem **Spróbuj ponownie**, zamiast kręcić się w nieskończoność. Jeśli problem się powtarza, edytuj aplikację, aby sprawdzić jej punkt wejścia i gałąź, a następnie opublikuj ją ponownie, lub skontaktuj się z administratorem PlaidCloud.

### Wygląd

Serwerowe aplikacje Panel domyślnie używają nowoczesnego projektu **Fast** PlaidCloud, ale ustawienie **Projekt** aplikacji może przywrócić stylizację **Domyślny** Panel, gdy istniejący kod CSS od niej zależy. Motyw — jasny, ciemny lub przełącznik jasny/ciemny, który przeglądający mogą zmieniać — ustawiasz w szablonie swojej aplikacji. Wzorce znajdziesz w sekcji [Ustawianie motywu](/pl/guides/panel-apps/creating/#ustawianie-motywu-jasny-ciemny-lub-przełącznik) w przewodniku Tworzenie. Jeśli tabele lub niestandardowa stylizacja Twojej aplikacji są przygotowane dla jasnego tła, zablokuj ją na motywie jasnym.

## Wyświetlanie dzienników (aplikacje serwerowe)

Kliknij ikonę **Wyświetl dzienniki** w wierszu aplikacji serwerowej, aby otworzyć przeglądarkę dzienników. (Aplikacje WASM działają w całości w przeglądarce i nie mają dzienników serwera, więc ikona pojawia się tylko w wierszach aplikacji serwerowych.)

Przeglądarka ma dwie karty:

- **Środowisko uruchomieniowe** (wyświetlana jako pierwsza) — własne dane wyjściowe działającej aplikacji: wszystko, co rejestruje, wszystko, co wypisuje, oraz wszelkie nieprzechwycone błędy. Są one zachowywane nawet po skalowaniu aplikacji do zera, więc możesz przejrzeć, co robiła wcześniejsza sesja.
- **Zbuduj** — dane wyjściowe budowania kontenera aplikacji. Użyj jej, aby zobaczyć, *dlaczego* kompilacja ma stan **Niepowodzenie** — na przykład z powodu zależności, której nie udało się zainstalować.

Każda karta zawiera filtry **Informacje / Ostrzeżenie / Błąd**, zakres czasu **Dzienniki od** (od ostatniej godziny do 30 dni lub wszystkie), przycisk **Odśwież** oraz **Automatyczne odświeżanie** do sprawdzania nowych wpisów — przydatne podczas obserwowania działającej aplikacji lub trwającej kompilacji. Najnowsze wpisy są wyświetlane jako pierwsze.

> Jeśli nie udało się przechwycić danych wyjściowych kompilacji, karta Zbuduj pokazuje krótką notatkę wyjaśniającą dlaczego, zamiast być pusta.

### Odczytywanie pełnego komunikatu dziennika

Tabela dziennika przycina długie wiersze, aby lista pozostała czytelna. Wybierz wiersz dziennika, aby otworzyć **panel szczegółów** obok tabeli, który pokazuje pełny komunikat wpisu. To najłatwiejszy sposób na odczytanie czegoś, co jest zbyt długie dla tabeli — długiego komunikatu o błędzie lub pełnego śladu stosu — bez obcinania.

### Kopiowanie wierszy dziennika

Możesz zaznaczyć kilka wierszy dziennika naraz i kliknąć **Kopiuj**, aby umieścić je w schowku. Jest to przydatne do wklejania dzienników do rozmowy z asystentem AI podczas debugowania aplikacji albo do wiadomości do zespołu lub do pomocy technicznej PlaidCloud.

### Kto wywołał wiersz dziennika

Gdy Twoja aplikacja loguje przeglądających, każdy wiersz dziennika jest oznaczany **użytkownikiem**, którego sesja go wygenerowała, dzięki czemu wiadomo, który przeglądający natrafił na dany błąd lub ostrzeżenie. Oznaczanie jest realizowane w miarę możliwości — niektóre wiersze frameworka i uruchamiania powstają, zanim zaangażowany jest jakikolwiek przeglądający, i mogą nie pokazywać użytkownika.

## Metryki użycia (aplikacje serwerowe)

Kliknij ikonę **Usage Metrics** w wierszu aplikacji serwerowej — obok **Wyświetl dzienniki** — aby zobaczyć, jak aplikacja jest używana. Widok podsumowuje:

- **Unikalni użytkownicy** — ile różnych osób otworzyło aplikację.
- **Sesje** — ile razy została otwarta.
- **Średni i medianowy czas trwania sesji** — mniej więcej, jak długo trwa wizyta.
- **Ostatnio używane** — kiedy aplikacja była ostatnio otwierana.

Poniżej podsumowania znajduje się zestawienie **według użytkownika** i **według dnia**, dzięki czemu widać, kto korzysta z aplikacji i jak zmienia się użycie w czasie.

> Czasy trwania są przybliżone. Aplikacje serwerowe przechodzą w stan bezczynności i skalują się w dół, gdy nikt z nich nie korzysta, więc dokładny koniec sesji nie zawsze jest zaobserwowany — traktuj wartości czasu trwania jako wskazówkę, a nie dokładny pomiar.

## Edytowanie aplikacji

Kliknij ikonę **ołówka** w wierszu aplikacji, aby ją edytować. Formularz edycji odpowiada środowisku uruchomieniowemu aplikacji.

W przypadku aplikacji **serwerowej** możesz zmienić nazwę, slug, gałąź, punkt wejścia, CPU, pamięć, projekt, okno bezczynności, flagę publiczną, domeny osadzonego udostępniania oraz notatkę. **Połączenie Git** jest ustalane po utworzeniu aplikacji i wyświetlane tylko do odczytu. Zapisanie przebudowuje aplikację — jej stan wraca do **Budowanie…**, dopóki nowa kompilacja nie będzie gotowa.

## Usuwanie aplikacji

Kliknij ikonę **minus** w wierszu aplikacji i potwierdź; usunięcie lub cofnięcie publikacji aplikacji zawsze wymaga wcześniejszego potwierdzenia. Usunięcie aplikacji serwerowej likwiduje jej kompilację i wdrożenie; usunięcie aplikacji WASM cofa publikację pliku statycznego. Adres URL aplikacji przestaje działać natychmiast.

Narzędzie MCP `panel_deployment_manage` nie oferuje już cofania publikacji. Usuń aplikację z tej listy.
