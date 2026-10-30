---
title: Korzystanie z aplikacji Panel
description: Śledź stan kompilacji, otwieraj, buduj ponownie, blokuj, wyświetlaj dzienniki i metryki użycia, edytuj oraz usuwaj opublikowane aplikacje HoloViz Panel na ekranie Moje aplikacje Panel w PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/using.md
---

Każda opublikowana aplikacja pojawia się na ekranie **Moje aplikacje Panel** wraz z kolumnami **Środowisko uruchomieniowe**, **Stan**, **Slug** i ze znacznikami czasu. Pierwsza kolumna od lewej otwiera aplikację; pozostałe ikony w wierszu pozwalają zablokować aplikację przed przypadkowymi zmianami, edytować ją, usunąć oraz — w przypadku aplikacji serwerowych — zbudować ją ponownie, wyświetlić jej dzienniki i metryki użycia. Ikona otwierania odzwierciedla środowisko uruchomieniowe aplikacji, dzięki czemu aplikacje WASM i serwerowe łatwo odróżnić na pierwszy rzut oka.

## Stan kompilacji (aplikacje serwerowe)

Kolumna **Stan** aplikacji serwerowej śledzi jej kompilację, a lista odświeża się automatycznie, gdy trwa kompilacja:

- **Budowanie…** — PlaidCloud buduje kontener z Twojego repozytorium. Aplikacja nie ma jeszcze adresu URL.
- **Gotowe** — kompilacja zakończyła się powodzeniem. Adres URL aplikacji jest aktywny, a w jej wierszu pojawia się ikona **Otwórz**.
- **Niepowodzenie** — kompilacja nie została ukończona. Sprawdź punkt wejścia i gałąź, a następnie edytuj aplikację, aby opublikować ją ponownie.

Aplikacje WASM nie mają kroku kompilacji i są dostępne zaraz po opublikowaniu.

## Ponowne budowanie aplikacji serwerowej

Kliknij ikonę **Zbuduj ponownie** w wierszu aplikacji serwerowej, aby zbudować ją i wdrożyć ponownie bez zmiany jej ustawień. Stan aplikacji wraca do **Budowanie…**, gdy PlaidCloud ponownie buduje tę samą gałąź i ten sam punkt wejścia, a po udostępnieniu nowej kompilacji zmienia się z powrotem na **Gotowe**.

Użyj opcji **Zbuduj ponownie** po zmianach zależności, aktualizacjach obrazu bazowego lub przejściowym niepowodzeniu kompilacji. Edycja i zapisanie aplikacji serwerowej również powoduje jej ponowne zbudowanie, ale ponowne zbudowanie nie wymaga otwierania formularza edycji.

W przypadku aplikacji [App Runner](/pl/guides/workflows/use-converted-alteryx-apps/#utrzymywanie-aktualności-aplikacji) — formularza wejściowego generowanego dla przekonwertowanej aplikacji Alteryx — opcja **Zbuduj ponownie** oraz zapisanie edycji najpierw odświeżają wygenerowane pliki aplikacji do bieżącej wersji App Runner, a następnie ją budują. PlaidCloud robi to również dla każdej niezablokowanej aplikacji App Runner podczas aktualizacji samego PlaidCloud; zablokowana aplikacja wymaga **Zbuduj ponownie** po odblokowaniu.

## Blokowanie aplikacji

Kliknij ikonę **blokady** w wierszu aplikacji, aby zabezpieczyć ją przed przypadkowymi zmianami. Gdy aplikacja jest zablokowana:

- Opcje **Edytuj**, **Usuń** i **Zbuduj ponownie** odmawiają wykonania i informują, że aplikacja jest zablokowana.
- **Wypchnięcie zmian do gałęzi aplikacji serwerowej nie powoduje jej ponownego zbudowania** — automatyczna kompilacja jest pomijana do czasu odblokowania aplikacji. Dla pominiętego wypchnięcia nie jest uruchamiana żadna kompilacja, więc w dziennikach kompilacji aplikacji nie pojawia się nic nowego; po odblokowaniu wypchnij zmiany ponownie (lub użyj **Zbuduj ponownie**), aby je uwzględnić.
- Otwieranie aplikacji, wyświetlanie jej dzienników i metryk użycia nadal działa — blokada powstrzymuje tylko zmiany, nigdy odbiorców.

Kliknij ikonę ponownie, aby odblokować. Ikona pokazuje bieżący stan aplikacji: zamknięta, gdy aplikacja jest zablokowana, otwarta, gdy nie jest.

Blokada chroni przed wypadkami — omyłkową edycją, niezamierzonym usunięciem lub wypchnięciem zmian z gita do aplikacji, którą akurat demonstrujesz — podobnie jak blokada przepływów pracy i kroków przepływu pracy. **Nie** jest to mechanizm zabezpieczeń: każdy, kto może edytować aplikacje Panel, może je również odblokować.

> Blokada nie obejmuje dwóch rzeczy: **kompilacja już trwająca** w chwili zablokowania nadal się kończy i zostaje udostępniona, a pliki aplikacji **WASM** znajdują się w jej koncie dokumentów, więc zastąpienie tych plików zmienia działającą aplikację bez dotykania zablokowanego rekordu.

## Otwieranie aplikacji

Kliknij ikonę **Otwórz** na początku wiersza gotowej aplikacji, aby uruchomić ją w nowej karcie.

- Aplikacja serwerowa jest udostępniana pod adresem `https://<your-tenant-host>/serve/<slug>/`.
- Ikona **Otwórz** pojawia się dopiero wtedy, gdy aplikacja serwerowa ma stan **Gotowe**.

Aplikacja serwerowa skaluje się do zera, gdy jest bezczynna, aby oszczędzać zasoby, więc pierwsze otwarcie po okresie bezczynności wymaga jej uruchomienia. W tym czasie zamiast pustej karty widzisz **ekran ładowania PlaidCloud** — nazwę aplikacji, wskaźnik postępu i szczegóły obszaru roboczego. Aplikacja pojawia się sama, gdy tylko jest gotowa (zwykle po kilku sekundach, a przy zimnym starcie nawet po około minucie), a następnie odpowiada normalnie, aż do kolejnego okresu bezczynności.

> Jeśli aplikacja nie może się uruchomić, ekran ładowania zamienia się w komunikat **„This app didn't start”** z przyciskiem **Spróbuj ponownie**, zamiast kręcić się w nieskończoność. Jeśli problem się powtarza, edytuj aplikację, sprawdź jej punkt wejścia i gałąź, opublikuj ją ponownie lub skontaktuj się z administratorem PlaidCloud.

### Wygląd

Aplikacje serwerowe Panel domyślnie korzystają z nowoczesnego wyglądu **FAST** PlaidCloud, ale ustawienie **Projekt** aplikacji pozwala przełączyć je z powrotem na styl **Domyślny** Panel, gdy istniejący kod CSS od niego zależy. Motyw — jasny, ciemny lub przełącznik jasny/ciemny, który mogą przestawiać odbiorcy — ustawia się w szablonie aplikacji. Wzorce znajdziesz w sekcji [Ustawianie motywu](/pl/guides/panel-apps/creating/#ustawianie-motywu-jasny-ciemny-lub-przełącznik) w przewodniku Tworzenie. Jeśli tabele lub niestandardowe style aplikacji są przygotowane z myślą o jasnym tle, pozostaw aplikację ustawioną na jasny motyw.

## Wyświetlanie dzienników (aplikacje serwerowe)

Kliknij ikonę **Wyświetl dzienniki** w wierszu aplikacji serwerowej, aby otworzyć przeglądarkę dzienników. (Aplikacje WASM działają w całości w przeglądarce i nie mają dzienników serwera, więc ikona pojawia się tylko w wierszach aplikacji serwerowych.)

Przeglądarka ma dwie karty:

- **Środowisko uruchomieniowe** (wyświetlana jako pierwsza) — własne dane wyjściowe działającej aplikacji: wszystko, co zapisuje do dziennika, wszystko, co wypisuje, oraz wszelkie nieprzechwycone błędy. Są one zachowywane nawet po skalowaniu aplikacji do zera, więc możesz przejrzeć, co robiła wcześniejsza sesja.
- **Build** — dane wyjściowe z budowania kontenera aplikacji. Użyj jej, aby sprawdzić, *dlaczego* kompilacja ma stan **Niepowodzenie** — na przykład z powodu zależności, której nie udało się zainstalować.

Każda karta udostępnia filtry **Informacje / Ostrzeżenie / Błąd**, zakres czasu **Dzienniki od** (od ostatniej godziny do 30 dni lub wszystkie), przycisk **Odśwież** oraz **Automatyczne odświeżanie**, które sprawdza nowe wpisy — przydatne podczas obserwowania działającej aplikacji lub trwającej kompilacji. Najnowsze wpisy są wyświetlane jako pierwsze.

> Jeśli nie udało się przechwycić danych wyjściowych kompilacji, karta Build wyświetla krótką notatkę wyjaśniającą powód, zamiast być pusta.

### Odczytywanie pełnego komunikatu dziennika

Tabela dziennika przycina długie wiersze, aby lista pozostała czytelna. Zaznacz wiersz dziennika, aby otworzyć obok tabeli **panel szczegółów** z pełnym komunikatem wpisu. To najłatwiejszy sposób, aby odczytać coś, co jest za długie dla tabeli — długi komunikat o błędzie lub pełny ślad stosu — bez obcinania.

### Kopiowanie wierszy dziennika

Możesz zaznaczyć kilka wierszy dziennika naraz i kliknąć **Kopiuj**, aby umieścić je w schowku. Przydaje się to do wklejania dzienników do rozmowy z asystentem AI podczas debugowania aplikacji albo do wiadomości do zespołu lub do pomocy technicznej PlaidCloud.

### Kto wywołał wiersz dziennika

Gdy aplikacja loguje odbiorców, każdy wiersz dziennika jest oznaczony **użytkownikiem**, którego sesja go wygenerowała, dzięki czemu wiesz, który odbiorca napotkał dany błąd lub ostrzeżenie. Oznaczanie odbywa się w miarę możliwości — niektóre wiersze frameworka i uruchamiania powstają, zanim jakikolwiek odbiorca jest zaangażowany, i mogą nie wskazywać użytkownika.

## Metryki użycia (aplikacje serwerowe)

Kliknij ikonę **Metryki użycia** w wierszu aplikacji serwerowej — obok **Wyświetl dzienniki** — aby zobaczyć, jak aplikacja jest używana. Widok podsumowuje:

- **Unikalni użytkownicy** — ile różnych osób otworzyło aplikację.
- **Sesje** — ile razy została otwarta.
- **Średni i mediana czasu trwania sesji** — mniej więcej, jak długo trwa wizyta.
- **Ostatnio używane** — kiedy aplikacja została otwarta ostatnio.

Pod podsumowaniem znajdziesz zestawienie **według użytkownika** i **według dnia**, aby zobaczyć, kto korzysta z aplikacji i jak zmienia się użycie w czasie.

> Czasy trwania są przybliżone. Aplikacje serwerowe przechodzą w stan bezczynności i skalują się w dół, gdy nikt z nich nie korzysta, więc dokładny koniec sesji nie zawsze jest obserwowany — traktuj wartości czasu jako wskazówkę, a nie dokładny pomiar.

## Edytowanie aplikacji

Kliknij ikonę **ołówka** w wierszu aplikacji, aby ją edytować. Formularz edycji odpowiada środowisku uruchomieniowemu aplikacji.

W przypadku aplikacji **serwerowej** możesz zmienić nazwę, slug, gałąź, punkt wejścia, procesor, pamięć, projekt, okno bezczynności, flagę publiczną, domeny osadzonego udostępniania i notatkę. Pozycja **Połączenie Git** jest stała po utworzeniu aplikacji i jest wyświetlana tylko do odczytu. Zapisanie powoduje ponowne zbudowanie aplikacji — jej stan wraca do **Budowanie…**, dopóki nowa kompilacja nie będzie gotowa.

## Usuwanie aplikacji

Kliknij ikonę **minus** w wierszu aplikacji i potwierdź; usunięcie lub cofnięcie publikacji aplikacji zawsze wymaga najpierw potwierdzenia. Usunięcie aplikacji serwerowej likwiduje jej kompilację i wdrożenie; usunięcie aplikacji WASM cofa publikację pliku statycznego. Adres URL aplikacji natychmiast przestaje działać.

Narzędzie MCP `panel_deployment_manage` nie oferuje już cofania publikacji. Zamiast tego usuń aplikację z tej listy.
