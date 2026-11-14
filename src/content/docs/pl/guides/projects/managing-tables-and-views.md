---
title: Zarządzanie tabelami i widokami
description: Zarządzaj tabelami i widokami w projektach PlaidCloud, w tym ich tworzeniem, konfiguracją, uprawnieniami i organizacją obiektów danych.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

PlaidCloud umożliwia porządkowanie tabel i zarządzanie nimi, w tym etykietami. Tabele są dostępne dla wszystkich przepływów pracy w projekcie i mają wiele narzędzi i opcji.


Oprócz tabel PlaidCloud oferuje także widoki oparte na danych tabel. Korzystanie z widoków pozwala na natychmiastowe aktualizacje przy zmianach w tabelach źródłowych oraz oszczędza miejsce w magazynie danych.



Opcje obejmują:


* Ta sama tabela może istnieć w wielu ścieżkach hierarchii (hierarchie alternatywne)
* Tabele można oznaczać tagami, aby łatwiej je wyszukiwać i uwzględniać w procesach PlaidCloud
* Tabele można wersjonować
* Tabele można publikować, aby były dostępne dla wizualizacji pulpitów

PlaidCloud porządkuje tabele w systemie opartym na ścieżkach, podobnie jak nawigacja po serii folderów, co pozwala na elastyczniejszą i bardziej logiczną organizację tabel. W tym systemie tabele można przenosić w obrębie hierarchii albo tworzyć wiele odwołań do jednej tabeli z różnych miejsc hierarchii (hierarchie alternatywne). Zarządzanie tabelami tą metodą pozwala, aby struktura odzwierciedlała potrzeby operacyjne, raportowanie i kontrolę.



## Wyszukiwanie tabel


Użyj pola **Filtr** u dołu listy, obok liczby wierszy, aby przeszukiwać nazwy i etykiety tabel. Naciśnij **/** lub Ctrl/Cmd+F, aby do niego przejść. Ten sam filtr dotyczy drzewa i spłaszczonej listy. Przełącznik **Wszystkie | Opublikowane** obok filtra zawęża listę do opublikowanych tabel; domyślnie ustawiony jest na **Wszystkie** i działa zarówno w drzewie, jak i na liście płaskiej.


### Według przepływu pracy

Folder **Według przepływu pracy** na końcu karty **Tabele** grupuje tabele pod każdym przepływem pracy, który je odczytuje lub zapisuje. Otwórz przepływ pracy, aby zobaczyć jego tabele. Folder jest widokiem tych samych tabel, więc nie można z niego niczego przenieść ani skopiować.


### Według kolumny

Wpisz nazwę kolumny w polu wyszukiwania kolumn na karcie **Tabele** i naciśnij Enter lub wybierz lupę obok pola, aby pokazać tylko tabele, które mają kolumnę o tej nazwie. Wyszukiwanie obejmuje nazwy kolumn, a nie dane, więc jest szybkie. Wybierz **Zawiera**, aby dopasować część nazwy kolumny zamiast całej nazwy. Wyczyść pole, aby ponownie pokazać wszystkie tabele. Długie wyszukiwanie może zwracać wyniki stronami, a wiersz stanu informuje, kiedy wyszukiwanie jeszcze trwa lub może być niekompletne.

Wybierz **Drzewo kolumn**, aby wyszukiwać z osobnego okna. Każda tabela, która ma daną kolumnę, otwiera się z dwiema listami:

* **Zasilana przez** — tabele, które dostarczają kolumnę
* **Zasila** — tabele, które kolumna dalej zasila

Asystent AI połączony przez MCP znajduje te same tabele za pomocą `table_find(column=...)`, dopasowując całą nazwę lub jej część.


### Szukaj wartości

Aby sprawdzić, które tabele zawierają wartość, wybierz **Szukaj wartości w danych… (wolne)** z menu **Akcje** na karcie **Tabele** albo kliknij tabelę prawym przyciskiem myszy i wybierz tę opcję, aby przeszukać tylko tę tabelę. Wpisz wartość, wybierz **Zawiera**, aby dopasować część wartości, i kliknij **Szukaj**. Każda tabela zawierająca wartość jest wyświetlana wraz z kolumnami, w których występuje, i kilkoma pasującymi wartościami. Kliknij tabelę dwukrotnie lub naciśnij na niej Enter, aby otworzyć ją w **Eksplorator tabel**. Kolumna otwiera tabelę przefiltrowaną do pasujących wierszy. Jeśli pole wyszukiwania kolumn zawiera tekst, wypełnia ono wartość do wyszukania.

Przed wyszukiwaniem warto wiedzieć, że:

* Wyszukiwanie odczytuje każdy wiersz każdej przeszukiwanej tabeli, więc może być bardzo wolne i zużywać dużo zasobów hurtowni danych. Okno ostrzega o tym, a przyciski wyszukiwania pozostają wyłączone do zakończenia wyszukiwania.
* Widzisz tylko wiersze, które możesz już otworzyć. Zabezpieczenia na poziomie wierszy obowiązują w każdym wyszukiwaniu.
* Historia zapytań Twojej hurtowni danych zapisuje wyszukiwane wartości.
* Wyszukiwanie obejmuje kolumny tekstowe tabel. Tabele, które nie zostały zbudowane, są pomijane i wymienione w ostrzeżeniu.
* Wyniki są zwracane stronami. Gdy wiersz stanu informuje, że wyszukiwanie zatrzymało się wcześniej, wybierz **Szukaj dalej**, aby kontynuować z tabelami, które nie zostały jeszcze przeszukane.

Asystent AI połączony przez MCP używa `table_value_search`. Zwraca tabele i kolumny, które zawierają wartość, a nigdy same wartości. Gdy w projekcie poprosisz asystenta AI o znalezienie wartości, Weave wysyła nazwy pasujących tabel i kolumn do dostawcy modelu językowego.



## Importuj plik CSV

**Aby zamienić plik CSV w nową tabelę w tym projekcie:**

1. Przeciągnij plik z komputera na listę **Tabele** projektu albo wybierz **Nowy** > **Tabela z pliku CSV** na pasku narzędzi i upuść plik w polu lub kliknij **Wybierz plik CSV**.
2. PlaidCloud przesyła plik na Twój **Personal Temp Drive** lub, jeśli go nie masz, na **Temp Drive** obszaru roboczego i importuje go do nowej tabeli na najwyższym poziomie listy, nazwanej od pliku: `Sales Data.csv` staje się `sales_data`. Jeśli projekt ma już tabelę o tej nazwie, nowa otrzymuje numer, na przykład `sales_data_2`.
3. Lista odświeża się z zaznaczoną nową tabelą, a **Twoje dane w skrócie** otwiera się na niej. To, co pokazuje panel, opisano w [Zacznij od własnego pliku CSV](/pl/get-started/quickstart/#zacznij-od-własnego-pliku-csv).

Akceptowane są tylko pliki z rozszerzeniem `.csv`. Potrzebujesz uprawnienia do tworzenia tabel i zapisu w magazynie dokumentów, a zablokowany projekt nie przyjmuje pliku CSV do czasu odblokowania. Jeśli import się nie powiedzie, okno podaje powód, a projekt pozostaje bez zmian. PlaidCloud usuwa przesłany plik z dysku tymczasowego po zakończeniu importu, niezależnie od tego, czy się powiódł; w przeciwnym razie dysk tymczasowy usuwa go po dobie.

## Przenoszenie


**Aby przenieść tabelę:**


1. Przeciągnij ją do folderu, w którym ma się znajdować

## Zmiana nazwy


**Aby zmienić nazwę tabeli:**


1. Kliknij tabelę prawym przyciskiem myszy
2. Wybierz opcję zmiany nazwy
3. Wpisz nową nazwę i zapisz
4. Tabela otrzymała nową nazwę, ale zachowuje swój pierwotny unikatowy identyfikator.

## Czyszczenie


**Aby wyczyścić tabelę:**


1. Zaznacz tabele w hierarchii ‘
2. Kliknij przycisk czyszczenia na górnym pasku narzędzi.

*Uwaga: można wyczyścić pojedynczą tabelę lub wiele tabel*



## Usuwanie


**Aby usunąć tabelę:**


1. Zaznacz tabele w hierarchii
2. Kliknij przycisk usuwania na górnym pasku narzędzi
3. Operacja usuwania sprawdzi, czy tabela jest używana przez kroki przepływu pracy lub widoki. Jeśli tak, pojawi się prośba o usunięcie tych powiązań, zanim usunięcie będzie możliwe.

*Uwaga: tabele można też usunąć w trybie wymuszonym. Wymuszone usunięcie tabel pozostawia uszkodzone odwołania, dlatego należy z niego korzystać oszczędnie.*


### Ostatni odczyt

Okno usuwania pokazuje, kiedy tabela była ostatnio odczytywana, na przykład **Last read 3 days ago by** osoba lub krok, dzięki czemu można odróżnić tabelę, której nikt nie używa, od takiej, która nadal jest w użyciu. PlaidCloud pobiera te informacje z historii zapytań Twojej hurtowni danych i pomija odczyty wykonywane przez własne działania porządkowe.

| Hurtownia danych | Co jest potrzebne |
| --- | --- |
| Snowflake | Odczyty pochodzą z Access History, które Snowflake rejestruje z opóźnieniem do około 3 godzin. Rola połączenia wymaga roli bazy danych `SNOWFLAKE.GOVERNANCE_VIEWER` (działa też `IMPORTED PRIVILEGES` w bazie danych `SNOWFLAKE`). Wersja Snowflake Standard nie ma Access History. |
| Databricks | Odczyty pochodzą z tabeli pochodzenia danych, którą Databricks również rejestruje z opóźnieniem, więc niedawny odczyt może jeszcze się nie pojawić. Tożsamość połączenia wymaga `USE CATALOG` w `system`, `USE SCHEMA` w `system.access` i `SELECT` w `system.access.table_lineage`. |
| PlaidCloud Lakehouse | Historia odczytów nie jest jeszcze dostępna. Okno pokazuje **Read history incomplete**. |

Gdy łączysz hurtownię danych, [sprawdzenie połączenia](/pl/guides/connections/external-lakehouse/#3-sprawdź-a-następnie-użyj) zaleca każde z tych uprawnień, którego brakuje, wraz z instrukcją do uruchomienia. Są zalecane, a nie wymagane: bez nich hurtownia danych się łączy, a okno pokazuje **Read history incomplete**.

Gdy PlaidCloud nie może odczytać całej historii, wiersz mówi **Read history incomplete** i nigdy nie zgłasza w jego miejsce „brak odczytów”. Każdy, kto ma bezpośredni dostęp SQL do Twojej hurtowni danych, może ustawić tag sesji, który zmienia sposób oznaczania jego własnych odczytów.

Asystent AI połączony przez MCP otrzymuje tę samą odpowiedź z `table_describe(include=['last_read'])`.



## Wyświetlanie kolumn tabeli


Zaznaczenie tabeli otwiera jej panel szczegółów. Sekcja **Kolumny** wyświetla każdą kolumnę z jej **Typ** i **Opis**, przy czym opis pochodzi z **Właściwości kolumny**. Wskaż wiersz, aby przeczytać długi opis w całości.

Tabela, której w danej chwili nie ma w hurtowni danych, ponieważ jej dane wygasły lub żaden krok jej nie zbudował, nie ma kolumn do wyświetlenia. Sekcja informuje o tym i pokazuje, ile kolumn ma tabela. Uruchom krok, który zapisuje tabelę, aby wyświetlić kolumny.


## Sprawdzanie, gdzie tabela jest używana


Zaznaczenie tabeli otwiera jej panel szczegółów, który wyświetla kroki przepływu pracy mające z nią styczność:


* **Tabela utworzona przez** — kroki, które zapisują do tabeli
* **Tabela wnosi wkład do** — kroki, które z niej odczytują
* **Może odwoływać się do tej tabeli** — kroki, które docierają do tabeli przez zmienną, której nie można rozwiązać. Ta sekcja pojawia się tylko wtedy, gdy takie kroki istnieją.


Zaznaczenie innej tabeli od razu czyści te listy. Krok w innym projekcie, który współdzieli dane tego projektu, taki jak krok **Import: zewnętrzna tabela projektu** odczytujący tę tabelę, jest również wymieniony, bez nazwy i przepływu pracy, ponieważ możesz nie mieć dostępu do tego projektu. Takie kroki mogą pojawić się chwilę po pozostałych.


Krok może wskazywać tabelę wprost albo docierać do niej przez ścieżkę zawierającą zmienną, na przykład `/Periods/{period}/Sales`. Gdy ta zmienna ma bieżącą wartość, krok pojawia się na pierwszych dwóch listach z ikoną informacji obok. Najedź na wiersz, aby zobaczyć ścieżkę w postaci, w jakiej krok ją przechowuje.


Traktuj te wiersze jako słabszą odpowiedź, którą są. Opisują to, czego dotknęłoby uruchomienie rozpoczęte teraz — a nie wszystko, co kiedykolwiek miało styczność z tabelą. Zmień zmienną, a odczytana zostanie inna tabela.


Niektórych zmiennych nie można rozwiązać. Albo nic w ogóle nie ustawiło zmiennej, albo wartość używana przez uruchomienie nie pochodzi z tego, co jest zapisane — Worklow Loop pobiera zmienne z danych podczas iteracji, krok Set Variable przypisuje w trakcie uruchomienia, makro otrzymuje zmienne od dowolnego kroku, który je wywołuje, a uruchomienie rozpoczęte przez czujnik niesie własne szczegóły tego czujnika. W każdym z tych przypadków to, co jest zapisane między uruchomieniami, pozostaje po ostatnim, a nie jest wartością godną zaufania. Zamiast rozwiązywać je do tabeli, która może być niewłaściwa, PlaidCloud wymienia kroki z nazwy w sekcji **Może odwoływać się do tej tabeli**, wraz ze zmienną, której nie mógł rozwiązać, abyś mógł je otworzyć i sprawdzić.


Krok, którego Twoja rola nie może zobaczyć, jest nadal wymieniony, abyś wiedział, że tabela jest używana, ale bez nazwy i przepływu pracy, i nie możesz go otworzyć. Nadal liczy się przy usuwaniu tabeli. Krok, który możesz zobaczyć, jest wymieniony bez przepływu pracy ukrytego przed Twoją rolą. Przed Architektem nic nie jest ukryte.


*Uwaga: gdy usuwasz tabele z listy **Tabele**, krok docierający do tabeli przez ścieżkę, ze zmienną lub bez niej, jest uznawany za jej użytkownika, nawet gdy jego zmiennej nie można rozwiązać. Okno usuwania wymienia krok, a usunięcie przebiega tylko wtedy, gdy je wymusisz.*



## Tworzenie nowej struktury katalogów


**Aby dodać nowy folder:**


1. Kliknij przycisk Nowy folder na pasku narzędzi

**Aby dodać folder do istniejącego folderu:**


1. Kliknij folder prawym przyciskiem myszy
2. Wybierz Nowy folder


## Wyświetlanie danych (Eksplorator tabel)


Dane tabel wyświetla się za pomocą Eksploratora danych. Eksplorator danych udostępnia widok siatki danych oraz podsumowanie wartości i statystyk kolumna po kolumnie. Dostępne jest filtrowanie metodą wskaż i kliknij oraz eksport do znanych formatów plików. Wybrane filtry można też zapisać jako krok Extract do użycia w przepływie pracy.



## Publikowanie tabeli na potrzeby raportowania


Wizualizacje pulpitów są celowo ograniczone do tabel, które zostały opublikowane. Przy publikowaniu tabeli można podać unikatową nazwę, która może wyróżniać dane. Może to być przydatne, gdy tabela ma mniej czytelną nazwę w części przepływu pracy, która ją wygenerowała, a potrzebuje wyraźniejszej nazwy dla osób budujących pulpity.


Opublikowane tabele nie mają powiązanych ścieżek. Pojawiają się jako lista tabel do użycia w obszarze pulpitów.



## Oznaczanie tabeli dla ról przeglądających


Wyświetlanie tabel przez różne role można kontrolować, klikając pola wyboru Eksplorator lub Menedżer. Jeśli trzeba zaktualizować wiele tabel, zaznacz tabele w hierarchii i wybierz żądaną rolę przeglądającą z menu Akcje na górnym pasku narzędzi.



## Notatki opisujące zawartość tabeli


Dodaj notatkę do tabeli, aby ułatwić zrozumienie danych.



## Wyświetlanie kształtu, rozmiaru i czasu ostatniej aktualizacji tabeli


Liczba wierszy, kolumn i rozmiar danych każdej tabeli są pokazane w hierarchii tabel. W przypadku bardzo dużych tabel (wiele milionów wierszy) liczba wierszy może być szacowana i wyświetlany jest wskaźnik przybliżonej liczby wierszy.



## Wyświetlanie dodatkowych atrybutów tabeli


**Aby wyświetlić i edytować inne atrybuty tabeli:**


1. Zaznacz tabelę
2. Kliknij, aby wyświetlić formularz kontekstowy tabeli po prawej stronie.


## Duplikowanie tabeli


**Aby zduplikować tabelę:**


1. Zaznacz tabelę
2. Kliknij przycisk duplikowania na górnym pasku narzędzi.


## Tworzenie aplikacji Panel z tabeli


Zaznacz tabelę lub widok i wybierz **Utwórz aplikację Panel** z menu **Nowy** lub z menu prawego przycisku myszy. Otwiera się okno **Nowa aplikacja Studio** z już wybranym projektem i tabelą. Aplikacja przyjmuje nazwę tabeli; zmień ją, jeśli chcesz, a następnie wybierz **Utwórz**, a Panel Studio otworzy ją z Weave gotowym do zbudowania jej pierwszej strony. Polecenie jest dostępne, gdy zaznaczysz pojedynczą tabelę lub widok, masz dostęp do edycji projektu, a projekt nie jest tylko do odczytu. Zobacz [Tworzenie aplikacji Panel](/pl/guides/panel-apps/creating/#zacznij-od-tabeli).


## Co przechowują tabele


Lista **Tabele** pokazuje kolumny **Dane bieżące**, **Historia**, **Dni Time Travel** i **Uwaga** obok rozmiaru każdej tabeli. **Dni Time Travel** to własne ustawienie tabeli; **1** oznacza, że używa ustawienia domyślnego projektu. Pasek stanu pod listą podaje sumę dla projektu: ile przechowuje, w tym ile to dane bieżące, a ile historia. Rozmiary oznaczone jako **Szacunkowo** pochodzą z kształtu tabeli, dopóki PlaidCloud ich nie zmierzy.

Wybierz **Magazyn** z menu **Akcje**, aby otworzyć okno **Magazyn** projektu z sugestiami zwolnienia miejsca i ustawieniami time travel. Zobacz [Zarządzanie magazynem](/pl/guides/projects/managing-storage/#okno-magazyn-dla-projektu).


## Tworzenie edytora danych z tabeli


Tabelę można zamienić w skonfigurowany edytor danych w jednym kroku — zaznacz tabelę i wybierz **Utwórz edytor danych z tabeli** z menu **Nowy** lub z menu prawego przycisku myszy. PlaidCloud analizuje kolumny tabeli i wstępnie buduje kontrolki wprowadzania edytora. Szczegóły opisano w [Tworzenie edytora danych z tabeli](/pl/guides/projects/managing-data-editors/#tworzenie-edytora-danych-z-tabeli).
