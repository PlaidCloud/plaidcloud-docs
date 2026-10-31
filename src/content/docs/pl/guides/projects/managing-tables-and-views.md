---
title: Zarządzanie tabelami i widokami
description: Zarządzaj tabelami i widokami w projektach PlaidCloud, w tym ich tworzeniem, konfiguracją, uprawnieniami i organizacją obiektów danych.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

PlaidCloud umożliwia organizowanie tabel i zarządzanie nimi, w tym etykietami. Tabele są dostępne dla wszystkich przepływów pracy w projekcie i mają wiele narzędzi oraz opcji.


Oprócz tabel PlaidCloud oferuje także Widoki oparte na danych tabel. Użycie widoków pozwala na natychmiastowe aktualizacje po zmianach w tabelach bazowych oraz oszczędza miejsce w magazynie danych.



Dostępne opcje:


* Ta sama tabela może istnieć w wielu ścieżkach hierarchii (alternatywne hierarchie)
* Tabele można oznaczać tagami, aby łatwiej je wyszukiwać i uwzględniać w procesach PlaidCloud
* Tabele mogą mieć wersje
* Tabele można opublikować, aby były dostępne dla wizualizacji pulpitów

PlaidCloud używa systemu opartego na ścieżkach do organizowania tabel, podobnie jak podczas poruszania się po serii folderów, co pozwala na bardziej elastyczną i logiczną organizację tabel. Dzięki temu systemowi tabele można przenosić w obrębie hierarchii lub tworzyć wiele odwołań do jednej tabeli z różnych miejsc hierarchii (alternatywne hierarchie). Możliwość zarządzania tabelami w ten sposób pozwala, aby struktura odzwierciedlała potrzeby operacyjne, raportowanie i kontrolę.



## Wyszukiwanie tabel


Użyj pola filtra w lewym dolnym rogu hierarchii, aby przeszukiwać nazwy i etykiety tabel. Dopasowania są pokazywane w hierarchii powyżej.


### Według przepływu pracy

Folder **Według przepływu pracy** na końcu karty **Tabele** grupuje tabele pod każdym przepływem pracy, który je odczytuje lub zapisuje. Otwórz przepływ pracy, aby zobaczyć jego tabele. Folder jest widokiem tych samych tabel, więc nie możesz niczego z niego przenosić ani kopiować.


### Według kolumny

Wpisz nazwę kolumny w polu wyszukiwania kolumn na karcie **Tabele** i naciśnij Enter albo wybierz lupę obok niego, aby pokazać tylko tabele, które mają kolumnę o tej nazwie. Wyszukiwanie odczytuje nazwy kolumn, a nie dane, więc jest szybkie. Wybierz **Zawiera**, aby dopasować część nazwy kolumny zamiast całej nazwy. Wyczyść pole, aby ponownie pokazać wszystkie tabele. Długie wyszukiwanie może zwracać wyniki stronami, a wiersz stanu informuje, kiedy wyszukiwanie wciąż trwa lub może być niekompletne.

Wybierz **Drzewo kolumn**, aby wyszukiwać w osobnym oknie. Każda tabela, która ma tę kolumnę, otwiera się z dwiema listami:

* **Zasilana przez** — tabele, które dostarczają kolumnę
* **Zasila** — tabele, które kolumna dalej zasila

Asystent AI połączony przez MCP znajduje te same tabele za pomocą `table_find(column=...)`, dopasowując całą nazwę lub jej część.


### Szukaj wartości

Aby znaleźć tabele zawierające daną wartość, wybierz **Szukaj wartości w danych… (wolne)** z menu **Akcje** na karcie **Tabele** albo kliknij tabelę prawym przyciskiem myszy i wybierz tę opcję, aby przeszukać tylko tę tabelę. Wpisz wartość, wybierz **Zawiera**, aby dopasować część wartości, i wybierz **Szukaj**. Każda tabela zawierająca wartość jest wymieniona wraz z kolumnami, w których się pojawia, i kilkoma pasującymi wartościami. Kliknij tabelę dwukrotnie lub naciśnij na niej Enter, aby otworzyć ją w Eksploratorze tabel. Kolumna otwiera tabelę przefiltrowaną do pasujących wierszy. Jeśli pole wyszukiwania kolumn zawiera tekst, wypełnia ono wartość do znalezienia.

Przed wyszukiwaniem pamiętaj, że:

* Wyszukiwanie odczytuje każdy wiersz każdej przeszukiwanej tabeli, więc może być bardzo wolne i zużywać dużo zasobów magazynu danych. Okno ostrzega o tym, a przyciski wyszukiwania pozostają wyłączone do zakończenia wyszukiwania.
* Widzisz tylko wiersze, które mogłeś już otworzyć. Zabezpieczenia na poziomie wierszy obowiązują w każdym wyszukiwaniu.
* Historia zapytań twojego magazynu danych rejestruje wyszukiwane wartości.
* Wyszukiwanie obejmuje kolumny tekstowe tabel. Tabele, które nie zostały zbudowane, są pomijane i wymienione w ostrzeżeniu.
* Wyniki są zwracane stronami. Gdy wiersz stanu informuje, że wyszukiwanie zakończyło się wcześniej, wybierz **Szukaj dalej**, aby kontynuować w tabelach, które nie zostały jeszcze przeszukane.

Asystent AI połączony przez MCP używa `table_value_search`. Zwraca tabele i kolumny zawierające wartość, nigdy same wartości. Gdy poprosisz asystenta AI w projekcie o znalezienie wartości, Weave wysyła dostawcy modelu językowego nazwy pasujących tabel i kolumn.



## Importuj plik CSV

**Aby zamienić plik CSV w nową tabelę w tym projekcie:**

1. Przeciągnij plik z komputera na listę **Tabele** projektu albo wybierz na pasku narzędzi **Nowy** > **Tabela z pliku CSV** i upuść plik w polu lub kliknij **Wybierz plik CSV**.
2. PlaidCloud przesyła plik na twój **Personal Temp Drive**, a jeśli go nie masz, na **Temp Drive** obszaru roboczego, i importuje go do nowej tabeli na najwyższym poziomie listy, nazwanej od pliku: `Sales Data.csv` staje się `sales_data`. Jeśli projekt ma już tabelę o tej nazwie, nowa otrzymuje numer, na przykład `sales_data_2`.
3. Lista odświeża się z zaznaczoną nową tabelą i otwiera się na niej **Twoje dane w skrócie**. Zobacz [Zacznij od własnego pliku CSV](/pl/get-started/quickstart/#zacznij-od-własnego-pliku-csv), aby dowiedzieć się, co pokazuje ten panel.

Akceptowane są tylko pliki z rozszerzeniem `.csv`. Potrzebujesz uprawnienia do tworzenia tabel i zapisu w magazynie dokumentów, a zablokowany projekt nie przyjmuje pliku CSV do czasu odblokowania. Jeśli import się nie powiedzie, okno podaje przyczynę, a projekt pozostaje bez zmian. PlaidCloud usuwa przesłany plik z dysku tymczasowego po zakończeniu importu, niezależnie od tego, czy się powiódł; w przeciwnym razie dysk tymczasowy usuwa go po jednym dniu.

## Przenoszenie


**Aby przenieść tabelę:**


1. Przeciągnij ją do folderu, w którym ma się znajdować

## Zmiana nazwy


**Aby zmienić nazwę tabeli:**


1. Kliknij tabelę prawym przyciskiem myszy
2. Wybierz opcję zmiany nazwy
3. Wpisz nową nazwę i zapisz ją
4. Tabela ma teraz nową nazwę, ale zachowuje swój pierwotny unikatowy identyfikator.

## Czyszczenie


**Aby wyczyścić tabelę:**


1. Zaznacz tabele w hierarchii
2. Kliknij przycisk czyszczenia na górnym pasku narzędzi.

*Uwaga: możesz wyczyścić jedną tabelę lub wiele tabel jednocześnie*



## Usuwanie


**Aby usunąć tabelę:**


1. Zaznacz tabele w hierarchii
2. Kliknij przycisk usuwania na górnym pasku narzędzi
3. Operacja usuwania sprawdzi, czy tabela jest używana przez kroki przepływu pracy lub widoki. Jeśli tak, zostaniesz poproszony o usunięcie tych powiązań, zanim usunięcie będzie możliwe.

*Uwaga: możesz też wymusić usunięcie tabel. Wymuszone usunięcie pozostawi uszkodzone odwołania, więc należy z niego korzystać oszczędnie.*


### Ostatni odczyt

Okno usuwania pokazuje, kiedy tabela była ostatnio odczytywana, na przykład **Last read 3 days ago by** osoba lub krok, dzięki czemu odróżnisz tabelę, z której nikt nie korzysta, od wciąż używanej. PlaidCloud pobiera to z historii zapytań twojego magazynu danych i pomija odczyty wykonane przez jego własne czynności porządkowe.

| Magazyn danych | Co jest potrzebne |
| --- | --- |
| Snowflake | Odczyty pochodzą z Access History, które Snowflake rejestruje z opóźnieniem do około 3 godzin. Rola połączenia wymaga roli bazy danych `SNOWFLAKE.GOVERNANCE_VIEWER` (działa też `IMPORTED PRIVILEGES` w bazie danych `SNOWFLAKE`). Wersja Snowflake Standard nie ma Access History. |
| Databricks | Odczyty pochodzą z tabeli lineage, którą Databricks również rejestruje z opóźnieniem, więc ostatni odczyt może jeszcze nie być widoczny. Tożsamość połączenia wymaga `USE CATALOG` w `system`, `USE SCHEMA` w `system.access` oraz `SELECT` w `system.access.table_lineage`. |
| PlaidCloud Lakehouse | Historia odczytów nie jest jeszcze dostępna. Okno pokazuje **Read history incomplete**. |

Podczas łączenia magazynu danych [sprawdzenie połączenia](/pl/guides/connections/external-lakehouse/#3-sprawdź-a-następnie-użyj) zaleca każde z brakujących uprawnień, wraz z instrukcją do uruchomienia. Są zalecane, a nie wymagane: bez nich magazyn danych się połączy, a okno pokaże **Read history incomplete**.

Gdy PlaidCloud nie może odczytać całej historii, wiersz mówi **Read history incomplete** i nigdy nie podaje w jego miejsce informacji „brak odczytów”. Każdy, kto ma bezpośredni dostęp SQL do twojego magazynu danych, może ustawić tag sesji, który zmienia sposób oznaczania jego własnych odczytów.

Asystent AI połączony przez MCP uzyskuje tę samą odpowiedź z `table_describe(include=['last_read'])`.



## Zobacz kolumny tabeli


Zaznaczenie tabeli otwiera jej panel szczegółów. Sekcja **Kolumny** wymienia każdą kolumnę z jej **Typem** i **Opisem**, przy czym opis pochodzi z **Właściwości kolumny**. Wskaż wiersz, aby przeczytać długi opis w całości.

Tabela, której w danej chwili nie ma w magazynie danych, ponieważ jej dane wygasły lub żaden krok jej nie zbudował, nie ma kolumn do wyświetlenia. Sekcja informuje o tym i pokazuje liczbę kolumn tabeli. Uruchom krok, który zapisuje tabelę, aby je wyświetlić.


## Zobacz, gdzie tabela jest używana


Zaznaczenie tabeli otwiera jej panel szczegółów, który wymienia kroki przepływu pracy, które jej dotyczą:


* **Tabela utworzona przez** — kroki, które zapisują do tabeli
* **Tabela wnosi wkład do** — kroki, które z niej odczytują
* **Może odwoływać się do tej tabeli** — kroki, które docierają do tabeli przez zmienną, której nie można rozstrzygnąć. Ta sekcja pojawia się tylko wtedy, gdy są takie kroki.


Krok może nazwać tabelę wprost albo dotrzeć do niej przez ścieżkę zawierającą zmienną, taką jak `/Periods/{period}/Sales`. Gdy zmienna ma bieżącą wartość, krok pojawia się w pierwszych dwóch listach z ikoną informacji obok. Najedź na wiersz, aby zobaczyć ścieżkę w postaci, w jakiej przechowuje ją krok.


Traktuj te wiersze jako słabszą odpowiedź, którą są. Opisują to, czego dotknęłoby uruchomienie rozpoczęte teraz — a nie wszystko, co kiedykolwiek dotykało tabeli. Zmień zmienną, a zostanie odczytana inna tabela.


Niektórych zmiennych nie można rozstrzygnąć. Albo nic w ogóle nie ustawiło zmiennej, albo wartość używana w uruchomieniu nie pochodzi z tego, co jest zapisane — krok Workflow Loop pobiera zmienne z danych podczas iteracji, krok Set Variable przypisuje je podczas uruchomienia, makro otrzymuje zmienne od dowolnego kroku, który je wywołuje, a uruchomienie rozpoczęte przez sensor niesie własne szczegóły tego sensora. W każdym z tych przypadków to, co jest zapisane między uruchomieniami, jest pozostałością po ostatnim z nich, a nie wartością, której można ufać. Zamiast rozstrzygać je do tabeli, która może być niewłaściwa, PlaidCloud wymienia kroki z nazwy w sekcji **Może odwoływać się do tej tabeli**, razem ze zmienną, której nie mógł rozstrzygnąć, abyś mógł je otworzyć i sprawdzić.


Krok, którego twoja rola nie może zobaczyć, jest nadal wymieniony, dzięki czemu wiesz, że tabela jest używana, ale bez nazwy i przepływu pracy, i nie możesz go otworzyć. Nadal liczy się przy usuwaniu tabeli. Krok, który możesz zobaczyć, jest wymieniony bez przepływów pracy ukrytych przed twoją rolą. Przed Architektem nic nie jest ukryte.


*Uwaga: gdy usuwasz tabele z listy **Tabele**, krok, który dociera do tabeli przez ścieżkę, ze zmienną lub bez niej, liczy się jako jej używający, nawet jeśli jego zmiennej nie można rozstrzygnąć. Okno usuwania wymienia krok, a usunięcie przebiega tylko wtedy, gdy je wymusisz.*



## Utwórz nową strukturę katalogów


**Aby dodać nowy folder:**


1. Kliknij przycisk Nowy folder na pasku narzędzi

**Aby dodać folder do istniejącego folderu:**


1. Kliknij folder prawym przyciskiem myszy
2. Wybierz Nowy folder


## Wyświetlanie danych (Eksplorator tabel)


Dane tabeli są wyświetlane za pomocą Eksploratora danych. Eksplorator danych zapewnia widok siatki danych oraz podsumowanie wartości i statystyk kolumna po kolumnie. Dostępne jest filtrowanie metodą wskaż i kliknij oraz eksport do znanych formatów plików. Wybory filtrów można też zapisać jako krok Extract, którego można użyć w przepływie pracy.



## Opublikuj tabelę do raportowania


Wizualizacje pulpitów są celowo ograniczone do tabel, które zostały opublikowane. Podczas publikowania tabeli możesz podać unikatową nazwę, która może wyróżniać dane. Może to być przydatne, gdy tabela ma bardziej niejasną nazwę w części przepływu pracy, która ją wygenerowała, ale potrzebuje wyraźniejszej nazwy dla osób budujących pulpity.


Opublikowane tabele nie mają przypisanych ścieżek. Pojawiają się jako lista tabel do użycia w obszarze pulpitów.



## Oznacz tabelę dla ról wyświetlających


Wyświetlaniem tabel przez różne role można sterować, klikając pola wyboru Eksplorator lub Menedżer. Jeśli trzeba zaktualizować wiele tabel, zaznacz je w hierarchii i wybierz żądaną rolę wyświetlającą z menu Akcje na górnym pasku narzędzi.



## Notatki opisujące zawartość tabeli


Dodaj notatkę do tabeli, aby ułatwić zrozumienie danych.



## Wyświetl kształt, rozmiar i czas ostatniej aktualizacji tabeli


Liczba wierszy, kolumn i rozmiar danych każdej tabeli są pokazane w hierarchii tabel. W przypadku bardzo dużych tabel (wiele milionów wierszy) liczba wierszy może być szacowana i zostanie wyświetlony wskaźnik przybliżonej liczby wierszy.



## Wyświetl dodatkowe atrybuty tabeli


**Aby wyświetlić i edytować inne atrybuty tabeli:**


1. Zaznacz tabelę
2. Kliknij widok formularza kontekstu tabeli po prawej stronie.


## Duplikowanie tabeli


**Aby zduplikować tabelę:**


1. Zaznacz tabelę
2. Kliknij przycisk duplikowania na górnym pasku narzędzi.


## Utwórz aplikację Panel z tabeli


Zaznacz tabelę lub widok i wybierz **Utwórz aplikację Panel** z menu **Nowy** albo z menu kontekstowego. Otwiera się okno **Nowa aplikacja Studio** z już wybranym projektem i tabelą. Aplikacja przyjmuje nazwę tabeli; możesz ją zmienić, a następnie wybierz **Utwórz**, po czym Panel Studio otwiera aplikację z Weave gotowym do zbudowania jej pierwszej strony. Polecenie jest dostępne, gdy zaznaczysz jedną tabelę lub widok, masz dostęp do edycji projektu, a projekt nie jest tylko do odczytu. Zobacz [Tworzenie aplikacji Panel](/pl/guides/panel-apps/creating/#zacznij-od-tabeli).


## Zobacz, co przechowują tabele


Lista **Tabele** pokazuje kolumny **Dane bieżące**, **Historia**, **Dni Time Travel** i **Uwaga** obok rozmiaru każdej tabeli. **Dni Time Travel** to własne ustawienie tabeli; **1** oznacza, że używa ustawienia domyślnego projektu. Pasek stanu pod listą podaje sumę dla projektu: ile przechowuje i ile z tego stanowią dane bieżące, a ile historia. Rozmiary oznaczone jako **Szacunkowo** pochodzą z kształtu tabeli do czasu, aż PlaidCloud ją zmierzy.

Wybierz **Magazyn** na pasku narzędzi, aby otworzyć okno **Magazyn** projektu z sugestiami zwolnienia miejsca i ustawieniami time travel. Zobacz [Zarządzanie magazynem](/pl/guides/projects/managing-storage/#okno-magazyn-dla-projektu).


## Utwórz edytor danych z tabeli


Możesz zamienić tabelę w skonfigurowany edytor danych w jednym kroku — zaznacz tabelę i wybierz **Utwórz edytor danych z tabeli** z menu **Nowy** albo z menu kontekstowego. PlaidCloud analizuje kolumny tabeli i wstępnie buduje kontrolki wejściowe edytora. Szczegóły znajdziesz w [Utwórz edytor danych z tabeli](/pl/guides/projects/managing-data-editors/#tworzenie-edytora-danych-z-tabeli).
